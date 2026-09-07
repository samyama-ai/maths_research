# Original User Request

## 2026-06-20T16:28:47Z

# Teamwork Project Prompt

Generate a catalog of 1,000+ math research problems distributed across the 10 fields defined in TAXONOMY.md, strictly adhering to the 10-section structure in TEMPLATE.md.

Working directory: /Users/user/projects/Madhulatha-Sandeep/maths_ws/maths_research
Integrity mode: development

## Requirements

### R1. Generate 1,000+ Problems
The system must generate over 1,000 distinct markdown files describing mathematical research problems. These problems must be categorized under the 10 subfields defined in `TAXONOMY.md`.

### R2. Strict Schema Adherence
Every generated problem file must strictly adhere to the 10-section structure specified in `TEMPLATE.md` (including LaTeX foundations, history, bounds, and references).

### R3. Automated Generation using AGY CLI
The generation must be scaled programmatically using custom `agy` CLI automation scripts rather than manual drafting, as explicitly requested by the user.

## Verification Resources
- Existing `gen_index.sh` script to parse headers and build the index.
- Existing `tools/generate_catalog.py` script as a baseline reference for programmatic generation.

## Acceptance Criteria

### Programmatic Verification
- [ ] Running `find topics -type f -name "*.md" | wc -l` from the working directory outputs a number greater than 1,000.
- [ ] Running `./gen_index.sh` successfully parses all generated files without errors and populates `INDEX.md`.

### Structure Audit
- [ ] A programmatic or agentic check on a random sample of 5 files confirms the presence of all 10 required section headers defined in `TEMPLATE.md`.
