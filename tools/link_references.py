#!/usr/bin/env python3
"""Resolve Section 9 references against Crossref and arXiv, and attach identifiers.

The catalog's references name real authors, titles, venues and years, but carry no
DOI or arXiv id, so `audit.py --links` had 2 URLs to check across 124 pages against
dbms_research's 6,700. A citation nobody can resolve is a lead, not a reference.

Matching is deliberately conservative, because a confidently wrong DOI is worse
than none: a candidate is accepted only when the normalised Crossref title matches
the cited title closely (token F1 >= 0.9) and the year agrees within one, to allow
for preprint-vs-publication drift. Everything else is left alone and counted, so
the miss rate is visible rather than hidden.

  python3 tools/link_references.py --dry-run          # report, touch nothing
  python3 tools/link_references.py --limit 20         # first 20 files
  python3 tools/link_references.py                    # whole catalog
"""
import argparse
import glob
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = "maths_research-linker/1.0 (mailto:research@samyama.ai)"
CACHE_PATH = os.path.join(os.path.expanduser("~"), ".cache", "maths_research-crossref.json")

# arXiv asks for one request every 3 seconds. Enforced as a next-allowed clock
# rather than a trailing sleep, so retries and error paths are paced too.
ARXIV_MIN_INTERVAL = float(os.getenv("ARXIV_MIN_INTERVAL", "3.5"))
_ARXIV_NEXT_OK = 0.0

# A reference line looks like:
#   - **[Foundational]** Author, A. *Title.* Venue, Year.
#
# The category tag is stripped before the title is read. Left in place, the first
# *...* group in the line is the tag's own emphasis markers, so every lookup
# searched Crossref for the word "Foundational" and matched nothing -- 0% resolved
# across the whole catalog, with no error to show for it.
TAG_RE = re.compile(r"^\s*-\s+(?:\*\*\[[^\]]+\]\*\*)?\s*")
TITLE_RE = re.compile(r"\*([^*]{8,300})\*")
YEAR_RE = re.compile(r"\b(1[89]\d{2}|20[0-4]\d)\b")


# Edition and volume suffixes are bibliographic decoration, not part of the title.
# "Unsolved Problems in Number Theory (3rd ed.)" scored 0.83 against Crossref's
# "Unsolved problems in number theory" -- the same book, rejected by the 0.9
# threshold purely on the suffix.
EDITION_RE = re.compile(
    r"[\s,;]*[\(\[]?\s*(?:\d+\s*(?:st|nd|rd|th)\s+(?:ed\.?|edition)|"
    r"(?:revised\s+)?(?:ed\.|edition)|revised|reprint|"
    r"vol\.?\s*\d+|volume\s+\d+|part\s+[IVX\d]+)\s*[\)\]]?\s*\.?\s*$", re.I)


def strip_edition(s):
    prev = None
    while prev != s:
        prev = s
        s = EDITION_RE.sub("", s).strip().rstrip(",;")
    return s


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def f1(a, b):
    ta, tb = set(norm(strip_edition(a)).split()), set(norm(strip_edition(b)).split())
    if not ta or not tb:
        return 0.0
    inter = len(ta & tb)
    if not inter:
        return 0.0
    p, r = inter / len(ta), inter / len(tb)
    return 2 * p * r / (p + r)


def load_cache():
    if os.path.exists(CACHE_PATH):
        try:
            return json.load(open(CACHE_PATH, encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_cache(cache):
    os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
    json.dump(cache, open(CACHE_PATH, "w", encoding="utf-8"))


def crossref(title, cache):
    """One Crossref query per distinct title, cached across runs."""
    key = norm(title)
    if key in cache:
        return cache[key]
    url = ("https://api.crossref.org/works?rows=5&select=title,DOI,issued&query.bibliographic="
           + urllib.parse.quote(title[:280]))
    # Crossref answers 429 under sustained load: 18 of the first ~3,900 queries in
    # the full pass. A 429 is not an answer, so it must not be cached as "no
    # results" -- that would bake a lost reference into the cache permanently.
    # Back off and retry instead.
    out = []
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=25) as r:
                items = json.loads(r.read().decode()).get("message", {}).get("items", [])
        except Exception as e:
            code = getattr(e, "code", None)
            if code == 429 and attempt < 3:
                wait = 5 * (attempt + 1)
                print(f"    crossref 429; backing off {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            print(f"    crossref error for {title[:50]!r}: {e}", file=sys.stderr)
            return None                  # None = unknown, do not cache a failure
        for it in items:
            t = (it.get("title") or [""])[0]
            parts = it.get("issued", {}).get("date-parts", [[None]])
            out.append({"title": t, "doi": it.get("DOI", ""),
                        "year": parts[0][0] if parts and parts[0] else None})
        cache[key] = out
        return out
    return None


# Journal-level records, not articles. A reference line that italicises the venue
# instead of the paper title matched its journal's ISSN DOI at f1 = 1.00 -- a link
# that resolves, looks right, and points at the wrong kind of thing entirely.
ISSN_DOI = re.compile(r"\(issn\)", re.I)
VENUE_WORDS = re.compile(
    r"^(the\s+)?(bulletin|journal|proceedings|transactions|annals|notices|acta|"
    r"comptes rendus|archiv|memoirs|s[ée]minaire)\b", re.I)


def best_match(title, year, cands):
    """Accept only a close title match whose year agrees within one.

    Coverage is deliberately sacrificed for correctness: an unresolved reference
    is honest, a confidently wrong DOI is not.
    """
    if VENUE_WORDS.match(title.strip()):
        return None, 0.0                   # a venue name, not a paper title
    best, best_score = None, 0.0
    for c in cands or []:
        if ISSN_DOI.search(c.get("doi", "")) or not c.get("year"):
            continue                       # journal record, not an article
        score = f1(title, c["title"])
        if score < 0.9:
            continue
        if year and abs(int(year) - int(c["year"])) > 1:
            continue
        if score > best_score:
            best, best_score = c, score
    return best, best_score



def arxiv(title, cache):
    """Search arXiv by title. Crossref indexes journals; a large share of the
    literature this catalog cites is preprints that never got a DOI, or got one
    years later under a different title."""
    key = "arxiv:" + norm(title)
    if key in cache:
        return cache[key]
    q = urllib.parse.quote(f'ti:"{title[:200]}"')
    url = f"https://export.arxiv.org/api/query?search_query={q}&max_results=5"

    # The sleep used to run only after a successful call, so the error path
    # returned immediately and a failing query spun with no delay at all. That is
    # what earned an HTTP 429 in the first place. Pace every request, and back off
    # when told to.
    global _ARXIV_NEXT_OK
    for attempt in range(4):
        wait = _ARXIV_NEXT_OK - time.time()
        if wait > 0:
            time.sleep(wait)
        _ARXIV_NEXT_OK = time.time() + ARXIV_MIN_INTERVAL
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                body = r.read().decode()
        except Exception as e:
            code = getattr(e, "code", None)
            if code == 429:
                backoff = ARXIV_MIN_INTERVAL * (4 ** (attempt + 1))
                print(f"    arxiv 429; backing off {backoff:.0f}s", file=sys.stderr)
                _ARXIV_NEXT_OK = time.time() + backoff
                continue
            print(f"    arxiv error for {title[:50]!r}: {e}", file=sys.stderr)
            return None
        out = []
        for entry in re.findall(r"<entry>(.*?)</entry>", body, re.S):
            tm = re.search(r"<title>(.*?)</title>", entry, re.S)
            im = re.search(r"<id>https?://arxiv\.org/abs/([^<v]+)", entry)
            pm = re.search(r"<published>(\d{4})", entry)
            if tm and im:
                out.append({"title": " ".join(tm.group(1).split()),
                            "arxiv": im.group(1),
                            "year": int(pm.group(1)) if pm else None})
        cache[key] = out
        return out
    print(f"    arxiv rate-limited after 4 attempts for {title[:50]!r}", file=sys.stderr)
    return None


def best_arxiv(title, year, cands):
    best, best_score = None, 0.0
    for c in cands or []:
        score = f1(title, c["title"])
        if score < 0.9:
            continue
        if year and c["year"] and abs(int(year) - int(c["year"])) > 2:
            continue                       # preprint often predates publication
        if score > best_score:
            best, best_score = c, score
    return best, best_score


def process(path, cache, dry_run, use_arxiv=True, resume=False):
    text = open(path, encoding="utf-8").read()
    if "## 9." not in text:
        return 0, 0
    head, _, rest = text.partition("## 9.")
    sec, sep, tail = rest.partition("## 10.")
    if resume and ("doi.org/" in sec or "arxiv.org/" in sec):
        return 0, 0

    linked = skipped = 0
    lines = sec.split("\n")
    for i, line in enumerate(lines):
        if not line.strip().startswith("-"):
            continue
        if "doi.org/" in line or "arxiv.org/" in line:
            continue                       # already carries an identifier
        m = TITLE_RE.search(TAG_RE.sub("", line))
        if not m:
            skipped += 1
            continue
        title = m.group(1).strip().rstrip(".")
        ym = YEAR_RE.search(line)
        year = ym.group(1) if ym else None
        hit, _ = best_match(title, year, crossref(title, cache))
        if hit and hit["doi"]:
            lines[i] = (line.rstrip().rstrip(".")
                        + f". [DOI](https://doi.org/{hit['doi']})")
            linked += 1
            time.sleep(0.2)                # Crossref etiquette
            continue
        if VENUE_WORDS.match(title.strip()):
            skipped += 1
            continue
        # arXiv started in 1991 and costs 3.5s a query. Spending that on a 1930s
        # paper that cannot be there is how a 5,000-reference pass becomes a day.
        if not use_arxiv or not year or int(year) < 1991:
            skipped += 1
            continue
        ahit, _ = best_arxiv(title, year, arxiv(title, cache))
        if ahit:
            lines[i] = (line.rstrip().rstrip(".")
                        + f". [arXiv:{ahit['arxiv']}](https://arxiv.org/abs/{ahit['arxiv']})")
            linked += 1
            continue
        skipped += 1

    if linked and not dry_run:
        new = head + "## 9." + "\n".join(lines) + sep + tail
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(new)
        os.replace(tmp, path)
    return linked, skipped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--no-arxiv", action="store_true",
                    help="Crossref only. arXiv costs 3.5s a query against its rate "
                         "limit, so a first full pass finishes in hours instead of days.")
    ap.add_argument("--resume", action="store_true",
                    help="Skip files whose Section 9 already carries identifiers.")
    a = ap.parse_args()

    files = sorted(p for p in glob.glob(os.path.join(ROOT, "topics", "*", "*.md"))
                   if os.path.basename(p) != "README.md")
    if a.limit:
        files = files[:a.limit]

    cache = load_cache()
    total_l = total_s = 0
    try:
        for n, p in enumerate(files, 1):
            l, s = process(p, cache, a.dry_run, not a.no_arxiv, a.resume)
            total_l += l
            total_s += s
            if n % 25 == 0:
                print(f"  {n}/{len(files)} files, {total_l} linked, {total_s} unmatched",
                      flush=True)
                save_cache(cache)
    finally:
        save_cache(cache)

    rate = 100 * total_l / max(total_l + total_s, 1)
    print(f"-- {len(files)} files: {total_l} references linked, {total_s} unmatched "
          f"({rate:.0f}% resolved){' [dry run]' if a.dry_run else ''} --")
    return 0


if __name__ == "__main__":
    sys.exit(main())
