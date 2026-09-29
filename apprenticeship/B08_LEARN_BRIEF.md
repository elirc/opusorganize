# B08 — LEARN PASS (all 31 apprenticeship repos): junior on-ramp + agentic-era study guide

You are one of 7 Opus agents. Each agent owns ONE batch group (B01–B07) of repos. Fable orchestrates and reviews.

## Audience shift (why this pass exists)
B01–B07 built mid→senior material (incidents, tickets, blind reviews). The learner is actually a **junior SWE with weak
fundamentals** who wants to upskill *through these projects* into the **agentic-engineering era**: directing coding agents,
verifying their output, owning production consequences. This pass adds the missing on-ramp and the "how do I even study this
repo" guidance, per repo.

## Your deliverable per repo: a root-level `learn/` folder
Create `<repo>/learn/` (next to `training/`, do NOT move or rewrite `training/`) containing:

1. **`learn/README.md`** — the study guide for THIS repo. Required sections:
   - *What this app is and why it's in the portfolio* (2–4 lines, cite real paths).
   - *Prerequisites*: the 3–6 concrete fundamentals you need first, each linked to the central curriculum page
     (`Desktop\opusorganize\apprenticeship\curriculum\NN-*.md`) or to a specific file in the repo to read.
   - *Study route*: an ordered list of timed sessions (45–90 min each, ~6–12 sessions) walking from "run/read it" →
     `training/` tickets → incident branches → blind review → interview kit. Each session names exact files/branches
     and ends with a **verifiable exit criterion** ("test X fails/passes", "you can explain Y without notes").
   - *Do vs. delegate*: for each session, mark which parts the learner must do BY HAND (reading, diagnosis, review,
     writing the spec) and which parts they should delegate to a coding agent — then verify. This is the agentic-era core.
   - *How you know you're done here* + where to go next (name the next repo in the competency graph).
2. **`learn/00-onramp.md`** — junior-level warm-ups grounded in THIS repo (not generic): 5–10 short exercises
   (read this function and predict output; trace this request end to end; write one characterization test; explain this
   schema). Must be solvable before the harder `training/` material. Answers sealed in `learn/_answers/00-onramp.md`.
3. **`learn/01-agentic-practice.md`** — 3–5 drills that turn existing `training/` incidents into agent-direction practice:
   for a chosen incident, the learner writes the spec/prompt themselves, has an agent implement or fix it, then performs an
   adversarial review against the sealed answer. Include a short **verification checklist** (what a reviewer checks before
   trusting agent output in this codebase: tests, invariants, security spots — name real files). Answers/rubrics sealed in
   `learn/_answers/`.
4. **Content gaps (small, optional but encouraged)**: if the repo's `training/REPORT` or batch report flags something thin
   (e.g. "no frontend tickets", "interview kit is mini"), add 1–3 new exercises under `training/` following the existing
   format. Do NOT add new incident branches in this pass. Cite what gap you filled.

Quality bar (inherits BATCH_PROMPT.md hard rules 2–5): every exercise names this project's files, data and failure modes;
generic material is rejected; answers sealed; concepts live once in the central curriculum — link, don't copy.

## Hard rules (unchanged from B01–B07 + new)
- **NEVER recursively delete anything** (`rm -rf`, `Remove-Item -Recurse`, `rmdir /s`) — junctions. No exceptions.
- **Docs-only pass**: do NOT run `npm install`/`pnpm install`/`dotnet restore`, builds, tests, or Docker. If you want to
  claim runtime behavior, cite the batch report or existing training evidence instead, or mark `UNVERIFIED`.
- Don't touch production code on main. New files only: `learn/**` (+ small additions under `training/` per item 4).
- Unique scratch dir: `<scratchpad>\b08-<group>` only. Never write temp files into repos or shared folders.
- Commits: `git add learn training` (pathspec), one commit per repo on the SAME branch where that repo's previous
  training commits live (check `git log --all --oneline | head` first; some repos use a `training` branch, Outline uses
  its training branch, not master). Message: `docs(training): add learn/ study guide + junior on-ramp (B08)`.
  gitjira-app has commitlint — the `docs(training):` prefix is required there.
  End every commit message with:
  `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`
- If a repo path or git state doesn't match expectations, STOP for that repo, record it in your report, move on.

## Inputs you must read first (in this order, skim hard)
1. `Desktop\opusorganize\apprenticeship\PROGRESS.md` — your group's table (paths hints, commit hashes, caveats).
2. `Desktop\opusorganize\batch<N>report\REPORT.md` + `batch<N>report\projects\<repo>.md` — per-repo findings, exact paths.
3. `Desktop\opusorganize\apprenticeship\COMPETENCY_GRAPH.md` + `curriculum\README.md` — what exists centrally; link to it.
4. In each repo: `training/` tree (README/REPORT, tickets, incident list) — you are writing the guide TO this material.

## Report back
Write `Desktop\opusorganize\batch8report\projects\<repo>.md` for each repo:
path, branch + commit hash of your commit, files added, gaps filled, anything skipped/UNVERIFIED, and a 3-line summary of
the study route you designed. Keep it under ~60 lines. Do NOT edit PROGRESS.md or COMPETENCY_GRAPH.md (Fable consolidates).
