# astradocs — context pack for GPT Astra

Purpose: this folder gives an external model (GPT "Astra") the context of the B08 **learn pass** so it can produce its
own independent version of the same deliverable. Astra should treat everything here as ground truth about what exists
on disk, and then design its *own* study guides — not copy Claude's.

## What the portfolio is
~354 project dirs on this machine were audited read-only (`opusorganize\portfolio-audit\FINAL_REPORT.md`, 18 sections).
31 of them were then turned into an apprenticeship (batches B01–B07): each got a `training/` folder (tickets, sealed
answers, blind reviews, interview kits) plus `training/incidents/NNN-slug` branches with seeded, evidence-verified bugs
— 92 incident branches, 22 central curriculum pages in `opusorganize\apprenticeship\curriculum\`.

## What the B08 learn pass added (Claude's version)
For each of the 31 repos, a root-level `learn/` folder:
- `learn/README.md` — repo-specific study guide: prerequisites (linked to central curriculum), a timed session route
  through the existing `training/` material, a **do-vs-delegate** column (what the learner does by hand vs delegates to
  a coding agent and then verifies), and exit criteria.
- `learn/00-onramp.md` — junior-level warm-ups grounded in that repo's real files (answers sealed in `learn/_answers/`).
- `learn/01-agentic-practice.md` — drills that turn existing incidents into agent-direction practice: learner writes the
  spec, an agent implements, learner does an adversarial review against the sealed answer.
Full spec: `opusorganize\apprenticeship\B08_LEARN_BRIEF.md`. Per-repo results: `opusorganize\batch8report\projects\`.

## The learner
CS graduate, junior level, weak fundamentals, no LeetCode/DSA goals. Target: mid→senior CRUD web roles
(TS/React/Next, Node, C#/.NET, PostgreSQL/SQL Server) in the agentic-engineering era — directing coding agents,
verifying their output, owning production consequences. Core rule: **manufacture practice; the learner does the
thinking.** Generic material (anything not naming the repo's own files/failure modes) is rejected.

## Rules Astra must also respect if it writes into these repos
1. Never touch production code on main; new folders only (suggested: `learn-astra/` to avoid colliding with `learn/`).
2. Never recursively delete anything (npm workspace junctions have destroyed real source here before).
3. No installs/builds — several repos have node_modules removed and Docker is currently broken on this machine.
4. Answers sealed in `_answers/`; concepts link to `opusorganize\apprenticeship\curriculum\`, never duplicated.
5. Evidence or it didn't happen: every claim cites a real path.

## Files in this folder
- `MODIFIED_PROJECTS.md` — the report/list of every project modified in the B08 pass (paths, branches, commits, files).
  *(Note 2026-10-06: this file is not in the repository. It was planned but never committed, and only 4 of 31 per-repo reports are in `batch8report/projects/`. See the B08 status note in `../apprenticeship/PROGRESS.md` for which repos have `learn/` on GitHub.)*
- `../apprenticeship/COMPETENCY_GRAPH.md`, `PROGRESS.md`, `ADVICE.md` — the skill map, batch log, meta-advice.
