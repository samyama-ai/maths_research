#!/usr/bin/env python3
import os
import sys
import json
import time
import argparse
import asyncio
from pathlib import Path
import shutil
import subprocess
import re

ROOT = Path(__file__).resolve().parent.parent

# sys.path is fixed up here, not in main(). fix_math_hash was imported inside
# generate_problem_file and only resolved because main() appended tools/ first,
# so every page failed with ModuleNotFoundError the moment the module was driven
# from anywhere but its own CLI.
sys.path.insert(0, str(ROOT / "tools"))
from fix_math_hash import transform as fix_math_hash_transform  # noqa: E402

# Backend: "claude" or "agy". Both are print-mode CLIs that take a prompt and
# return text, so only the argv differs. agy is kept because it was the original
# mandate; claude is the default after agy's subscription quota stopped a run at
# 124 of 1,000 files.
BACKEND = os.getenv("CATALOG_BACKEND", "claude").lower()

# Both CLIs have independent subscription budgets, and this run has now been
# stopped by each of them in turn: agy at 124 files, claude at 563. Failing over
# to the other backend turns a hard stop into a slower run. FAILOVER=0 disables.
FAILOVER = os.getenv("CATALOG_FAILOVER", "1") != "0"
_EXHAUSTED = set()
_BACKEND_LOCK = asyncio.Lock()

# Each call takes tens of seconds, so the run is latency-bound, not CPU-bound.
# Bound total in-flight calls across all topics.
AGY_CONCURRENCY = int(os.getenv("AGY_CONCURRENCY", "8"))
AGY_TIMEOUT = os.getenv("AGY_PRINT_TIMEOUT", "10m")
AGY_SEMAPHORE = asyncio.Semaphore(AGY_CONCURRENCY)

# A quota wall is not a transient error. The first long run burned 20 minutes and
# ~1,100 queued calls retrying against "Individual quota reached", producing nothing:
# every call returned in under 10 seconds, so the retry loop just spun. Once this is
# seen, the whole run aborts and says when the quota resets.
# Every phrasing either CLI uses to say "stop asking". The first version matched
# only agy's wording ("quota reached ... Resets in"), so claude's
# "You've hit your session limit - resets 1:10pm" sailed straight past it: 709
# calls retried into a wall that was never going to answer, which is the exact
# failure this class was added to prevent.
QUOTA_RE = re.compile(
    r"quota reached|quota exceeded|rate limit|resets? (in|at|\d)|"
    r"(session|usage|weekly|daily) limit|hit your limit|"
    r"upgrade your subscription|too many requests|429", re.I)


class QuotaExhausted(RuntimeError):
    pass


# Progress accounting, so the log shows completions rather than only the queue
# being drained. Every "+ Generating" line is printed at enqueue time, which made
# 2,081 of them appear in the first seconds of a run that had written no files.
PROGRESS = {"done": 0, "failed": 0, "total": 0}


def note(msg):
    print(msg, flush=True)

# System instruction to enforce math detail and schema adherence
SYSTEM_INSTRUCTION = """You are a world-class mathematician, theoretical computer scientist, and editor of a comprehensive open math catalog.
Your goal is to identify and write highly detailed, rigorous, and accurate markdown pages for open and hard mathematical problems.
All mathematical equations must be properly formatted using LaTeX: $...$ for inline and $$...$$ for display blocks.
All citations and references must be real, verifiable publications (papers, books, surveys) with accurate titles, authors, venues, and years.
You must adhere strictly to the 10-section TEMPLATE.md schema.
Do not skip any sections. Do not use placeholders."""

# The 10 section headings TEMPLATE.md requires, matched by prefix.
REQUIRED_SECTIONS = [f"{i}." for i in range(1, 11)]

# Let's define the topics from TAXONOMY.md
TOPICS = {
    "01-number-theory": "Number Theory",
    "02-algebra-group-theory": "Algebra & Group Theory",
    "03-geometry": "Algebraic & Differential Geometry",
    "04-topology": "Topology & Knot Theory",
    "05-analysis": "Real & Complex Analysis",
    "06-pdes": "Partial Differential Equations",
    "07-combinatorics": "Combinatorics & Graph Theory",
    "08-logic-set-theory": "Mathematical Logic & Set Theory",
    "09-probability": "Probability & Stochastic Processes",
    "10-theoretical-cs": "Theoretical Computer Science"
}


FM_ORDER = ["id", "title", "topic", "status", "first_added", "last_reviewed",
            "last_substantive_update", "stale_since", "provenance"]


def normalize_markdown(text, topic_slug, slug, title, status, month=None):
    """Strip code fences the model wraps output in, then force the frontmatter.

    The model reliably fences the YAML block (```yaml ... ```), which makes the file
    fail the frontmatter check and renders the block as a code sample. Frontmatter
    fields are also identity, not prose, so they are rewritten from the candidate
    rather than trusted: `id` must equal the file's path or the audit rejects it.
    """
    text = text.strip()

    # A whole-response ```markdown fence.
    if text.startswith("```"):
        first, _, rest = text.partition("\n")
        if first.strip("` ").lower() in ("markdown", "md", "yaml", "", "text"):
            text = rest
            if text.rstrip().endswith("```"):
                text = text.rstrip()[:-3]
    text = text.strip()

    # A fence closing right after the frontmatter block.
    text = re.sub(r"\A(---\n.*?\n---)\n```\s*\n", r"\1\n", text, flags=re.S)

    month = month or time.strftime("%Y-%m")
    body = text
    if body.startswith("---"):
        end = body.find("\n---", 3)
        if end >= 0:
            body = body[end + 4:].lstrip("\n")

    # The model sometimes emits the frontmatter fields with no opening '---'.
    # The delimited strip above then matches nothing, the generated header is
    # prepended anyway, and the original fields survive as visible body text --
    # 18 pages shipped with their frontmatter printed twice before this was
    # caught, and audit.py missed it because the first block parses correctly.
    # Drop a leading run of bare frontmatter keys, and any stray '---' after it.
    lines = body.lstrip("\n").split("\n")
    cut = 0
    while cut < len(lines) and re.match(r"^(" + "|".join(FM_ORDER) + r"):\s", lines[cut]):
        cut += 1
    if cut:
        while cut < len(lines) and lines[cut].strip() in ("", "---"):
            cut += 1
        body = "\n".join(lines[cut:])

    # A lone ``` left over from the model fencing its frontmatter. The opener is
    # removed by the fence handling above; when the block was not delimited the
    # closer had nothing to pair with and survived into the page.
    body = re.sub(r"\A\s*```[a-z]*\s*\n", "", body.lstrip("\n"))

    fm = {
        "id": f"{topic_slug}/{slug}",
        "title": f'"{title}"',
        "topic": topic_slug,
        "status": status,
        "first_added": month,
        "last_reviewed": month,
        "last_substantive_update": month,
        "stale_since": '""',
        "provenance": "synthesized",
    }
    header = "---\n" + "\n".join(f"{k}: {fm[k]}" for k in FM_ORDER) + "\n---\n\n"
    return header + body



async def _switch_backend(reason):
    """Move to the other CLI when this one's budget is gone. True if switched."""
    global BACKEND
    if not FAILOVER:
        return False
    async with _BACKEND_LOCK:
        _EXHAUSTED.add(BACKEND)
        other = "agy" if BACKEND == "claude" else "claude"
        if other in _EXHAUSTED:
            return False                   # both gone; let the run abort
        if not shutil.which(other):
            return False
        note(f"!! {BACKEND} is out of budget ({reason[:80]}); "
             f"switching to {other}")
        BACKEND = other
        return True


async def call_agy_cli(prompt, is_json=False):
    """Run one prompt through the configured CLI backend and return its text."""
    
    # The claude backend takes the role instruction as a real system prompt, which
    # also replaces Claude Code's own harness prompt. Left as a prefix, the default
    # agent boots MCP servers and project context for every call: one page took
    # 283s that way and 30s with --strict-mcp-config and --system-prompt.
    # Recomputed per attempt inside _run, not once here: claude takes the role
    # instruction through --system-prompt while agy needs it prefixed, so a
    # failover mid-page would otherwise send agy a prompt with no role at all.
    def _compose():
        base = prompt if BACKEND == "claude" else SYSTEM_INSTRUCTION + "\n\n" + prompt
        if is_json:
            base += ("\n\nCRITICAL: Return ONLY valid JSON. Do not wrap it in markdown "
                     "blocks (e.g. ```json ... ```). Just raw JSON.")
        return base

    full_prompt = prompt if BACKEND == "claude" else SYSTEM_INSTRUCTION + "\n\n" + prompt
    if is_json:
        full_prompt += "\n\nCRITICAL: Return ONLY valid JSON. Do not wrap it in markdown blocks (e.g. ```json ... ```). Just raw JSON."
        
    loop = asyncio.get_event_loop()
    
    def _run():
        composed = _compose()
        if BACKEND == "agy":
            cmd = ["agy", "-p", composed, "--print-timeout", AGY_TIMEOUT]
        else:
            cmd = ["claude", "-p", composed,
                   "--output-format", "text",
                   "--strict-mcp-config",
                   "--system-prompt", SYSTEM_INSTRUCTION]
        model = os.getenv("CATALOG_MODEL") or os.getenv("AGY_MODEL")
        if model:
            cmd += ["--model", model]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            err = (result.stderr + result.stdout).strip()
            if QUOTA_RE.search(err):
                raise QuotaExhausted(err[:200])
            raise RuntimeError(f"{BACKEND} -p failed: {err[:500]}")
        return result.stdout.strip()

    async with AGY_SEMAPHORE:
        response_text = ""
        for attempt in range(3):
            try:
                response_text = await loop.run_in_executor(None, _run)
                if response_text:
                    break
                # rc 0 with nothing on stdout. This is how the CLI reports being
                # unable to start a session, and it was the run's worst failure
                # mode: silent. 16 workers cycled every 60s writing nothing, and
                # the swallowed exception meant neither the log nor the file count
                # showed a reason. Always say it happened.
                note(f"    {BACKEND} returned an empty response "
                     f"(attempt {attempt + 1}/3)")
            except QuotaExhausted as e:
                if not await _switch_backend(str(e)):
                    raise
                continue                   # retry this same page on the other CLI
            except Exception as e:
                note(f"    {BACKEND} call failed (attempt {attempt + 1}/3): {e}")
            await asyncio.sleep(5 * (attempt + 1))
        else:
            raise RuntimeError(f"{BACKEND} returned nothing after 3 attempts")
    
    if is_json:
        # Strip potential markdown formatting if model didn't listen
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.startswith("```"):
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        response_text = response_text.strip()
        
    return response_text

async def discover_candidates(topic_slug, topic_name, limit=100):
    """Generate a list of candidate math problems for a topic."""
    print(f"=== Discovering {limit} candidates for {topic_name} ===")
    
    prompt = f"""Identify exactly {limit} distinct open, hard, or recently solved mathematical problems, conjectures, or theorems in the field of {topic_name}.
For each problem, you must provide:
1. The official/common Title (e.g. "Collatz Conjecture", "Navier-Stokes Smoothness").
2. A kebab-case filename slug (e.g. "collatz-conjecture", "navier-stokes-smoothness").
3. The Status: one of "open" (completely unsolved), "partially-solved" (proven for subclasses or under assumptions), "solved-recently" (proven in recent history), or "empirically-supported" (strong heuristic/numerical evidence but no proof).
4. A very brief 1-sentence Description (maximum 12 words) summarizing the core question. Do NOT use LaTeX, math blocks ($ or $$), or backslashes. Keep it strictly plain text.

Return this list as a JSON array of objects matching the following schema:
[
  {{
    "title": "Problem Title",
    "slug": "problem-slug",
    "status": "open|partially-solved|solved-recently|empirically-supported",
    "description": "1-sentence summary of the problem."
  }}
]
Ensure the response contains only the valid JSON array."""

    result_text = await call_agy_cli(prompt, is_json=True)
    try:
        # Escape any backslashes that are not part of valid JSON escape sequences
        sanitized_text = re.sub(r'\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})', r'\\\\', result_text)
        candidates = json.loads(sanitized_text)
        # Save to candidates.json
        topic_dir = ROOT / "topics" / topic_slug
        topic_dir.mkdir(parents=True, exist_ok=True)
        candidates_file = topic_dir / "candidates.json"
        with open(candidates_file, "w", encoding="utf-8") as f:
            json.dump(candidates, f, indent=2)
        print(f"Discovered {len(candidates)} candidates for {topic_slug} -> saved to {candidates_file.relative_to(ROOT)}")
        return candidates
    except Exception as e:
        print(f"Error parsing candidates JSON for {topic_slug}: {e}")
        print("Model returned:")
        print(result_text)
        return []


async def topup_candidates(topic_slug, topic_name, extra):
    """Ask for `extra` more candidates for a topic, excluding the ones already held.

    Deduplication across topics removes candidates, and some generation calls fail,
    so the pool has to run ahead of the target rather than exactly meet it. The
    exclusion list is sent verbatim: without it the model re-proposes the same
    headline conjectures and the pool does not grow.
    """
    topic_dir = ROOT / "topics" / topic_slug
    topic_dir.mkdir(parents=True, exist_ok=True)
    candidates_file = topic_dir / "candidates.json"
    existing = json.loads(candidates_file.read_text(encoding="utf-8")) if candidates_file.exists() else []
    have = {c["slug"] for c in existing}

    print(f"=== Topping up {topic_name} by {extra} (have {len(have)}) ===")
    prompt = f"""Identify exactly {extra} distinct open, hard, or recently solved mathematical problems, conjectures, or theorems in the field of {topic_name}.

You must NOT return any of the following, which are already catalogued:
{", ".join(sorted(have))}

Go deeper into the specialised sub-areas of the field to find problems that are genuinely distinct from that list.
For each problem, provide:
1. The official/common Title.
2. A kebab-case filename slug.
3. The Status: one of "open", "partially-solved", "solved-recently", or "empirically-supported".
4. A very brief 1-sentence Description (maximum 12 words). Do NOT use LaTeX, math blocks ($ or $$), or backslashes. Keep it strictly plain text.

Return a JSON array of objects with keys: title, slug, status, description.
Ensure the response contains only the valid JSON array."""

    result_text = await call_agy_cli(prompt, is_json=True)
    try:
        sanitized_text = re.sub(r'\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})', r'\\\\', result_text)
        new = json.loads(sanitized_text)
    except Exception as e:
        print(f"Error parsing topup JSON for {topic_slug}: {e}")
        return existing

    added = [c for c in new if c.get("slug") and c["slug"] not in have]
    merged = existing + added
    candidates_file.write_text(json.dumps(merged, indent=2), encoding="utf-8")
    print(f"Topped up {topic_slug}: +{len(added)} -> {len(merged)}")
    return merged


async def generate_problem_file(topic_slug, topic_name, candidate):
    """Generate a single problem markdown file following TEMPLATE.md."""
    title = candidate["title"]
    slug = candidate["slug"]
    status = candidate["status"]
    
    topic_dir = ROOT / "topics" / topic_slug
    file_path = topic_dir / f"{slug}.md"
    
    if file_path.exists():
        return True
        
    note(f"  + queued: {title} ({status})")
    
    # Read TEMPLATE.md to feed into prompt
    template_path = ROOT / "TEMPLATE.md"
    template_content = template_path.read_text(encoding="utf-8") if template_path.exists() else ""
    
    prompt = f"""Write a comprehensive, research-grade catalog page for the mathematical problem/conjecture: "{title}" under the topic "{topic_name}".

You must strictly adhere to the following template schema. Do not skip any sections and do not use placeholders.

---
TEMPLATE SCHEMA FOR EACH PAGE:
{template_content}
---

Topic slug: {topic_slug}
Problem slug: {slug}
Status: {status}

Additional Instructions:
- Section 2 (Mathematical Foundations) must contain exact mathematical formulations, definitions, and equations using LaTeX.
- Section 4 (Partial Results / Verified Cases) must mention concrete classes, ranges, dimensions, or parameters where it is solved.
- Section 5 (Principal Obstacles) must explain why current mathematical techniques fail.
- Section 9 (Key References) must list real, accurate, and verifiable papers, books, or survey works with correct titles, authors, venues, and years.
- Section 10 (Worked Example) must provide a concrete, calculated instance or walk through a simplified case to illustrate the problem.

LENGTH: target 1,400-1,900 words for the whole page. This is a catalog entry, not
a survey article. Uncapped, pages came back at 4,500 words and 400 seconds each,
which is 3x the length of the rest of the catalog and puts a 1,000-page run at
12 hours. Be dense and specific rather than expansive: name the theorem, state
the bound, cite the paper, move on.

Return only the markdown content, starting with the YAML frontmatter block."""

    started = time.time()
    markdown_content = await call_agy_cli(prompt, is_json=False)
    elapsed = time.time() - started
    markdown_content = normalize_markdown(
        markdown_content, topic_slug, slug, title, status)

    missing = [h for h in REQUIRED_SECTIONS if f"## {h}" not in markdown_content]
    if missing:
        PROGRESS["failed"] += 1
        note(f"    ! {slug}.md: missing sections {missing}, skipping write")
        return False

    
    # Post-process to fix math hash character parsing issues
    cleaned_content, n_escapes = fix_math_hash_transform(markdown_content)
    if n_escapes > 0:
        print(f"    Fixed {n_escapes} '#' in math mode for {slug}.md")
        
    # Write through a temp file in the same directory, then rename. A run killed
    # mid-write otherwise leaves a truncated page that the next pass skips as
    # "already exists", so the damage is permanent and silent.
    tmp = file_path.with_suffix(".md.tmp")
    tmp.write_text(cleaned_content, encoding="utf-8")
    tmp.replace(file_path)

    PROGRESS["done"] += 1
    note(f"  [{PROGRESS['done']}/{PROGRESS['total']}] {file_path.relative_to(ROOT)} "
         f"({len(cleaned_content) // 1024} KB, {elapsed:.0f}s)")
    return True


async def generate_interleaved(target_topics, limit_generate):
    """Generate across all topics round-robin instead of topic by topic.

    asyncio.gather queues per topic in order, and the semaphore hands out slots
    FIFO, so the first topic's whole backlog is served before the second topic
    gets a single slot. The first long run hit the agy quota wall after 124 files
    and 117 of them were Number Theory; eight topics had nothing at all. Round-robin
    means an interrupted run leaves the catalog evenly covered rather than deep in
    one field.
    """
    queues = []
    for slug, name in target_topics.items():
        f = ROOT / "topics" / slug / "candidates.json"
        if not f.exists():
            print(f"No candidates.json for {slug}; run --stage discovery first.")
            continue
        cands = sorted(json.loads(f.read_text(encoding="utf-8")), key=lambda c: c["slug"])
        queues.append((slug, name, cands[:limit_generate]))

    ordered = []
    for i in range(max((len(q[2]) for q in queues), default=0)):
        for slug, name, cands in queues:
            if i < len(cands):
                ordered.append((slug, name, cands[i]))
    PROGRESS["total"] = len(ordered)
    note(f"=== Generating {len(ordered)} problems, round-robin across "
         f"{len(queues)} topics ===")
    run_started = time.time()

    results = await asyncio.gather(*(
        generate_problem_file(slug, name, cand) for slug, name, cand in ordered
    ), return_exceptions=True)
    for r in results:
        if isinstance(r, QuotaExhausted):
            raise r
    errs = [r for r in results if isinstance(r, Exception)]
    if errs:
        PROGRESS["failed"] += len(errs)
        note(f"  {len(errs)} calls raised; first: {errs[0]}")

    mins = (time.time() - run_started) / 60
    note(f"=== pass done: {PROGRESS['done']} written, {PROGRESS['failed']} rejected, "
         f"{mins:.0f} min ({PROGRESS['done'] / max(mins, 1):.1f} files/min) ===")

    for slug, name, _ in queues:
        await generate_topic_readme(slug, name)


async def process_topic(topic_slug, topic_name, limit_candidates, limit_generate, stage):
    """Process a single topic (discovery and/or generation)."""
    topic_dir = ROOT / "topics" / topic_slug
    topic_dir.mkdir(parents=True, exist_ok=True)
    candidates_file = topic_dir / "candidates.json"
    
    candidates = []
    if stage == "topup":
        candidates = await topup_candidates(topic_slug, topic_name, limit_candidates)
    elif stage in ["discovery", "all"] or not candidates_file.exists():
        candidates = await discover_candidates(topic_slug, topic_name, limit_candidates)
    else:
        with open(candidates_file, "r", encoding="utf-8") as f:
            candidates = json.load(f)
            
    if stage in ["generation", "all"] and candidates:
        print(f"=== Generating up to {limit_generate} problems for {topic_name} ===")
        # Sort candidates to ensure deterministic ordering
        candidates = sorted(candidates, key=lambda x: x["slug"])
        
        # Limit to the requested generation limit
        candidates_to_gen = candidates[:limit_generate]
        
        results = await asyncio.gather(*(
            generate_problem_file(topic_slug, topic_name, cand)
            for cand in candidates_to_gen
        ), return_exceptions=True)
        for r in results:
            if isinstance(r, QuotaExhausted):
                raise r
            
    # Update the topic README.md index
    await generate_topic_readme(topic_slug, topic_name)

def topic_scope(topic_slug):
    """Pull the topic's scope blurb out of TAXONOMY.md, if present."""
    tax = ROOT / "TAXONOMY.md"
    if not tax.exists():
        return ""
    for line in tax.read_text(encoding="utf-8").splitlines():
        if f"`{topic_slug}`" in line and line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells:
                return cells[-1]
    return ""


def candidate_descriptions(topic_slug):
    """Map slug -> 1-line description from candidates.json, if present."""
    f = ROOT / "topics" / topic_slug / "candidates.json"
    if not f.exists():
        return {}
    try:
        return {c["slug"]: c.get("description", "") for c in json.loads(f.read_text(encoding="utf-8"))}
    except Exception:
        return {}


async def generate_topic_readme(topic_slug, topic_name):
    """Regenerate the topic's README.md based on generated markdown files.

    Preserves the hand-written intro paragraph when one already exists; falls
    back to the topic scope from TAXONOMY.md. Per-problem descriptions come
    from candidates.json.
    """
    topic_dir = ROOT / "topics" / topic_slug
    readme_path = topic_dir / "README.md"

    intro = ""
    if readme_path.exists():
        body = readme_path.read_text(encoding="utf-8").split("## Problems Index")[0]
        intro = "\n".join(l for l in body.splitlines() if l.strip() and not l.startswith("# ")).strip()
    if not intro:
        intro = topic_scope(topic_slug) or "Overview of the research topic and cataloged open problems."

    descriptions = candidate_descriptions(topic_slug)
    if readme_path.exists():
        # Keep descriptions already written into the index for files that have
        # no candidates.json entry (e.g. hand-authored problems).
        for line in readme_path.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\* \S+ \[.*?\]\(\./(.+?)\.md\)\s+\u2014\s+(.+)$", line)
            if m and not descriptions.get(m.group(1)):
                descriptions[m.group(1)] = m.group(2)

    problem_files = sorted(p for p in topic_dir.glob("*.md") if p.name != "README.md")

    lines = [f"# {topic_name}", "", intro, "", "## Problems Index", ""]

    for f in problem_files:
        text = f.read_text(encoding="utf-8")
        title_line = ""
        status = "open"

        for line in text.splitlines():
            if line.startswith("title:"):
                title_line = line.split(":", 1)[1].strip().strip('"').strip("'")
            elif line.startswith("status:"):
                status = line.split(":", 1)[1].strip()

        # Prefer the page's own H1. The frontmatter title comes from the candidate
        # record, which is ASCII and often terse: 'Erdos-Straus Conjecture' where
        # the page itself says 'Erdős-Straus Conjecture', and 'Berger Conjecture'
        # where the page says 'Berger Conjecture (Manifolds All of Whose Geodesics
        # Are Closed)'. INDEX.md already reads the H1, so reading it here too makes
        # the two indexes agree and keeps the better-formed name.
        h1 = re.search(r"^# (.+)$", text, re.M)
        if h1:
            title_line = h1.group(1).strip()

        if not title_line:
            title_line = f.stem.replace("-", " ").title()

        status_emoji = {
            "partially-solved": "\U0001F7E1",
            "solved-recently": "\U0001F7E2",
            "empirically-supported": "\U0001F7E0",
        }.get(status, "\U0001F534")

        entry = f"* {status_emoji} [{title_line}](./{f.name})"
        desc = descriptions.get(f.stem, "").strip()
        if desc:
            entry += f" \u2014 {desc}"
        lines.append(entry)

    readme_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Updated README.md index for {topic_slug}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate the Maths Research Catalog via the claude or agy CLI "
                    "(set CATALOG_BACKEND=claude|agy; default claude).")
    parser.add_argument("--topic", help="Specific topic slug to generate (default: all topics).")
    parser.add_argument("--stage", choices=["discovery", "topup", "generation", "all"], default="all",
                        help="Execution stage: discovery, generation, or all.")
    parser.add_argument("--limit-candidates", type=int, default=100,
                        help="Number of candidates to discover per topic (default: 100).")
    parser.add_argument("--limit-generate", type=int, default=100,
                        help="Number of files to generate per topic in this run (default: 100).")
    return parser.parse_args()

async def main():
    args = parse_args()
    
    target_topics = {}
    if args.topic:
        if args.topic in TOPICS:
            target_topics = {args.topic: TOPICS[args.topic]}
        else:
            print(f"Error: Unknown topic slug '{args.topic}'.")
            sys.exit(1)
    else:
        target_topics = TOPICS
        
    print(f"Starting Maths Research Catalog generator (backend={BACKEND}, "
          f"concurrency={AGY_CONCURRENCY}). Target topics: {len(target_topics)}")
    
    async def _one(slug, name):
        try:
            await process_topic(slug, name, args.limit_candidates, args.limit_generate, args.stage)
        except QuotaExhausted:
            raise
        except Exception as e:
            print(f"Failed processing topic {slug}: {e}")

    try:
        if args.stage == "generation":
            await generate_interleaved(target_topics, args.limit_generate)
        else:
            await asyncio.gather(*(_one(s, n) for s, n in target_topics.items()))
    except QuotaExhausted as e:
        print(f"\nABORT: {BACKEND} quota exhausted -- {e}")
        print("Re-run tools/run_catalog.sh once it resets; generated files are skipped.")
        subprocess.run([str(ROOT / "gen_index.sh")], cwd=str(ROOT))
        sys.exit(2)
            
    print("Regenerating global INDEX.md...")
    subprocess.run([str(ROOT / "gen_index.sh")], cwd=str(ROOT))
    print("Done!")

if __name__ == "__main__":
    asyncio.run(main())
