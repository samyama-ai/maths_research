# BRIEFING — 2026-06-20T22:00:32+05:30

## Mission
Generate a catalog of 1,000+ math research problems distributed across the 10 fields defined in TAXONOMY.md, strictly adhering to the 10-section structure in TEMPLATE.md.

## 🔒 My Identity
- Archetype: teamwork_preview_orchestrator
- Roles: orchestrator, user_liaison, human_reporter, successor
- Working directory: /Users/user/projects/Madhulatha-Sandeep/maths_ws/maths_research/.agents/orchestrator
- Original parent: top-level
- Original parent conversation ID: 5e6d62ac-b5e7-4dbd-8e9d-677e4d7e0e01

## 🔒 My Workflow
- **Pattern**: Project
- **Scope document**: /Users/user/projects/Madhulatha-Sandeep/maths_ws/maths_research/.agents/orchestrator/PROJECT.md
1. **Decompose**: Decompose the task into distinct milestones: Planning, Candidate Discovery, Generation of 1000+ problems, Indexing, Verification, and final Hardening.
2. **Dispatch & Execute**:
   - **Delegate (sub-orchestrator)**: For large milestones, spawn sub-orchestrators/workers.
3. **On failure** (in this order):
   - Retry: nudge stuck agent or re-send task
   - Replace: spawn fresh agent with partial progress
   - Skip: proceed without (only if non-critical)
   - Redistribute: split stuck agent's remaining work
   - Redesign: re-partition decomposition
   - Escalate: report to parent (sub-orchestrators only, last resort)
4. **Succession**: Self-succeed at 16 spawns, write handoff.md, spawn successor, kill timers.
- **Work items**:
  1. Initialize PROJECT.md and plans [pending]
  2. Setup test suite and verify current status [pending]
  3. Discover candidates (100 per topic) [pending]
  4. Generate problem pages (100 per topic) [pending]
  5. Run indexing and verification checks [pending]
  6. Perform random structure audit of generated files [pending]
  7. Verify global index and completion criteria [pending]
- **Current phase**: 1
- **Current focus**: Initialize PROJECT.md and plans

## 🔒 Key Constraints
- NEVER write, modify, or create source code files directly.
- NEVER run build/test commands yourself — require workers to do so.
- You MAY use file-editing tools ONLY for metadata/state files (.md) in your .agents/ folder.
- Never reuse a subagent after it has delivered its handoff — always spawn fresh.
- Integrity: No hardcoded test results, no dummy implementations.

## Current Parent
- Conversation ID: 5e6d62ac-b5e7-4dbd-8e9d-677e4d7e0e01
- Updated: not yet

## Key Decisions Made
- Initialized Project pattern.

## Team Roster
| Agent | Type | Work Item | Status | Conv ID |
|-------|------|-----------|--------|---------|
| explorer_setup | teamwork_preview_explorer | Verify environment and codebase | completed | 84353b8c-7b17-43a3-880c-10d1de19887e |
| worker_discovery_test | teamwork_preview_worker | Run discovery test on single topic | in-progress | 984c96a8-05a6-43b6-9120-06cda0299e96 |

## Succession Status
- Succession required: no
- Spawn count: 2 / 16
- Pending subagents: 984c96a8-05a6-43b6-9120-06cda0299e96
- Predecessor: none
- Successor: not yet spawned

## Active Timers
- Heartbeat cron: task-33
- Safety timer: none

## Artifact Index
- /Users/user/projects/Madhulatha-Sandeep/maths_ws/maths_research/.agents/orchestrator/BRIEFING.md — Persistent memory
- /Users/user/projects/Madhulatha-Sandeep/maths_ws/maths_research/.agents/orchestrator/progress.md — Progress heartbeat and status tracker
