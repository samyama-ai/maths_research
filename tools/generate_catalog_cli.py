#!/usr/bin/env python3
import os
import sys
import json
import time
import argparse
import asyncio
from pathlib import Path
import subprocess
import re

ROOT = Path(__file__).resolve().parent.parent

# System instruction to enforce math detail and schema adherence
SYSTEM_INSTRUCTION = """You are a world-class mathematician, theoretical computer scientist, and editor of a comprehensive open math catalog.
Your goal is to identify and write highly detailed, rigorous, and accurate markdown pages for open and hard mathematical problems.
All mathematical equations must be properly formatted using LaTeX: $...$ for inline and $$...$$ for display blocks.
All citations and references must be real, verifiable publications (papers, books, surveys) with accurate titles, authors, venues, and years.
You must adhere strictly to the 10-section TEMPLATE.md schema.
Do not skip any sections. Do not use placeholders."""

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

async def call_agy_cli(prompt, is_json=False):
    """Call agy CLI to generate content."""
    
    full_prompt = SYSTEM_INSTRUCTION + "\n\n" + prompt
    if is_json:
        full_prompt += "\n\nCRITICAL: Return ONLY valid JSON. Do not wrap it in markdown blocks (e.g. ```json ... ```). Just raw JSON."
        
    loop = asyncio.get_event_loop()
    
    def _run():
        result = subprocess.run(
            ["agy", "prompt", full_prompt],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise RuntimeError(f"agy prompt failed: {result.stderr}")
        return result.stdout.strip()
        
    response_text = await loop.run_in_executor(None, _run)
    
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

async def generate_problem_file(topic_slug, topic_name, candidate):
    """Generate a single problem markdown file following TEMPLATE.md."""
    title = candidate["title"]
    slug = candidate["slug"]
    status = candidate["status"]
    
    topic_dir = ROOT / "topics" / topic_slug
    file_path = topic_dir / f"{slug}.md"
    
    if file_path.exists():
        print(f"  - {slug}.md already exists. Skipping.")
        return True
        
    print(f"  + Generating: {title} ({status})")
    
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

Return only the markdown content, starting with the YAML frontmatter block."""

    markdown_content = await call_agy_cli(prompt, is_json=False)
    
    # Post-process to fix math hash character parsing issues
    from fix_math_hash import transform
    cleaned_content, n_escapes = transform(markdown_content)
    if n_escapes > 0:
        print(f"    Fixed {n_escapes} '#' in math mode for {slug}.md")
        
    # Write to file
    file_path.write_text(cleaned_content, encoding="utf-8")
    print(f"    Wrote file: {file_path.relative_to(ROOT)}")
    return True

async def process_topic(topic_slug, topic_name, limit_candidates, limit_generate, stage):
    """Process a single topic (discovery and/or generation)."""
    topic_dir = ROOT / "topics" / topic_slug
    topic_dir.mkdir(parents=True, exist_ok=True)
    candidates_file = topic_dir / "candidates.json"
    
    candidates = []
    if stage in ["discovery", "all"] or not candidates_file.exists():
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
        
        for cand in candidates_to_gen:
            await generate_problem_file(topic_slug, topic_name, cand)
            
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
    parser = argparse.ArgumentParser(description="Generate Maths Research Catalog using AGY CLI.")
    parser.add_argument("--topic", help="Specific topic slug to generate (default: all topics).")
    parser.add_argument("--stage", choices=["discovery", "generation", "all"], default="all",
                        help="Execution stage: discovery, generation, or all.")
    parser.add_argument("--limit-candidates", type=int, default=100,
                        help="Number of candidates to discover per topic (default: 100).")
    parser.add_argument("--limit-generate", type=int, default=100,
                        help="Number of files to generate per topic in this run (default: 100).")
    return parser.parse_args()

async def main():
    args = parse_args()
    sys.path.append(str(ROOT / "tools"))
    
    target_topics = {}
    if args.topic:
        if args.topic in TOPICS:
            target_topics = {args.topic: TOPICS[args.topic]}
        else:
            print(f"Error: Unknown topic slug '{args.topic}'.")
            sys.exit(1)
    else:
        target_topics = TOPICS
        
    print(f"Starting Maths Research Catalog generator (AGY CLI). Target topics: {len(target_topics)}")
    
    for slug, name in target_topics.items():
        try:
            await process_topic(slug, name, args.limit_candidates, args.limit_generate, args.stage)
        except Exception as e:
            print(f"Failed processing topic {slug}: {e}")
            
    print("Regenerating global INDEX.md...")
    subprocess.run([str(ROOT / "gen_index.sh")], cwd=str(ROOT))
    print("Done!")

if __name__ == "__main__":
    sys.path.append(str(ROOT / "tools"))
    asyncio.run(main())
