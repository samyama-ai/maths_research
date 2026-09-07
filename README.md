# Maths Research — Open & Hard Problems

![Topics](https://img.shields.io/badge/topics-10-green) ![Schema](https://img.shields.io/badge/schema-10%20sections-blue) ![Audit](https://img.shields.io/badge/audit-tools%2Faudit.py-lightgrey)

A structured, research-grade catalog of open and hard problems across the mathematics space — from number theory and algebra to topology, analysis, mathematical physics, and theoretical computer science. Each problem is documented with its formal statement, mathematical foundations, historical context, partial results, and active research directions.

This repository serves as a **knowledge map of mathematical frontiers** — designed for graduate students selecting research topics, mathematicians looking for adjacent connections, and anyone interested in the exact boundaries of what is known and unknown in mathematics.

---

> ⚠️ **Read the [provenance & honesty note](#-provenance--honesty-note) before citing anything.** This is a synthesized study aid, not a primary source.

---

<!-- AUTOGEN:BEGIN -->
## At a glance

| | |
|---|---|
| **Problems** | 1,001 across 10 of 10 topics |
| **Every problem documents** | statement · mathematical foundations · history & SOTA · partial results · principal obstacles · the gap · current research (2026) · future work · references · worked example |
| **Key references** | 12,238 cited across the catalog |
| **Worked examples** | 1,001 — every page carries a concrete instance |
| **Content** | ~2.16M words |

**Status mix across the 1,001 problems:**

| Status | Count | Meaning |
|---|---:|---|
| 🔴 `open` | 497 | No known solution; the question is genuinely unresolved |
| 🟡 `partially-solved` | 261 | Proven for restricted cases or under assumptions; general case open |
| 🟢 `solved-recently` | 221 | Settled in recent history; included for the technique and the gap it closed |
| 🟠 `empirically-supported` | 22 | Strong numerical or heuristic evidence, no proof |

**Problems per topic:**

| Slug | Topic | Problems |
|---|---|---:|
| `01-number-theory` | Number Theory | 119 |
| `02-algebra-group-theory` | Algebra & Group Theory | 98 |
| `03-geometry` | Algebraic & Differential Geometry | 99 |
| `04-topology` | Topology & Knot Theory | 99 |
| `05-analysis` | Real & Complex Analysis | 98 |
| `06-pdes` | Partial Differential Equations | 99 |
| `07-combinatorics` | Combinatorics & Graph Theory | 97 |
| `08-logic-set-theory` | Mathematical Logic & Set Theory | 97 |
| `09-probability` | Probability & Stochastic Processes | 97 |
| `10-theoretical-cs` | Theoretical Computer Science | 98 |
<!-- AUTOGEN:END -->

---

## Start here

- 🗺️ **[`TAXONOMY.md`](./TAXONOMY.md)** — the 10-topic map with scope descriptions.
- 📇 **[`INDEX.md`](./INDEX.md)** — flat, clickable list of every problem, grouped by topic.
- 📐 **[`TEMPLATE.md`](./TEMPLATE.md)** — the 10-section schema every problem page follows.

## How each problem page is structured

Every page is a standalone Markdown file with YAML frontmatter carrying a stable
`id` (equal to its path), `status`, and review dates, followed by ten fixed sections:

| # | Section | What it answers |
|---|---|---|
| 1 | Problem Statement / Conjecture | What exactly is claimed, and what would settle it |
| 2 | Mathematical Foundations | The structures and theorems it rests on, in LaTeX |
| 3 | History & State of the Art | Who posed it, and where the frontier sits now |
| 4 | Partial Results / Verified Cases | The dimensions, ranges and classes already proven |
| 5 | Principal Obstacles | Why current techniques do not generalise |
| 6 | The Gap | The precise distance between section 4 and section 1 |
| 7 | Current Research (2026) | Active directions, groups, recent preprints |
| 8 | Future Work | Strategies leading mathematicians have articulated |
| 9 | Key References | Foundational, recent and survey literature |
| 10 | Worked Example | A concrete instance, calculated |

`python3 tools/audit.py` enforces this: frontmatter completeness, section order,
`id` matching the file path, INDEX.md freshness, unescaped `#` inside math (which
breaks KaTeX rendering), and a scan for anything internal in a public repo.

## ⚠️ Provenance & honesty note

This catalog is **synthesized from established mathematical knowledge**, generated
programmatically and then checked by `tools/audit.py`. Read that as a limit on how
far it should be trusted:

- **Foundational results** (Riemann, Hilbert, Grothendieck, Serre, Wiles, Perelman,
  Tao, Zhang, …) are reliable — these are canonical statements with settled histories.
- **References are plausibly formed but not yet link-verified.** Pages cite real
  authors, titles, venues and years, but the catalog does not yet carry DOI or arXiv
  identifiers, so `tools/audit.py --links` has almost nothing to resolve. Treat every
  citation as a lead to check, not a verified fact. This is the largest known gap.
- **2025–2026 frontier claims** are made to the best of current knowledge and may lag
  the true frontier; they are flagged inline with *(frontier — verify)*.
- **Status labels are judgements**, not certificates. A problem marked `open` may have
  been settled in a preprint the catalog has not seen.

**Do not cite this repository as a primary source.** Use it to orient yourself, then
read — and cite — the underlying literature.

## Regenerating

```bash
./gen_index.sh                    # rebuild INDEX.md from the files on disk
python3 tools/audit.py            # structure, frontmatter, index sync, safety
python3 tools/update_readme.py    # refresh the counts in this file
tools/run_catalog.sh 1000         # generate to a target (CATALOG_BACKEND=claude|agy)
```
