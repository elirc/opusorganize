# B02 Agent Brief — operating rules for ONE project

Read `C:\Users\Owner\Desktop\opusorganize\apprenticeship\BATCH_PROMPT.md` (the master prompt) fully. You execute it for exactly ONE project,
at the tier you are given, **skipping Phase 1 (already done) and Phase 6 (the orchestrator does it)**. Tier → phases:
LAB = Phases 2, 3, 4, 5 · DRILL = Phase 3 (+ a small Phase 5 interview kit: PROJECT_STORIES + 10 TECHNICAL_QUESTIONS) · READ = Phase 4.

Prior audit evidence for this project: `C:\Users\Owner\Desktop\opusorganize\portfolio-audit\projects\batch-01.md` (search its name).
The user explicitly authorized modifying the project to create the training material, within the rules below.

## Git + filesystem rules (strict — this machine has quirks)
- The whole home folder `C:\Users\Owner` is a stray git repo. Only trust a project's own `.git` directory. Never run git commands that
  would hit the home repo.
- The project's working tree may have **uncommitted user changes** (e.g. netdrop has 15). Never stage, stash, reset, checkout or discard them.
  Stage ONLY paths under `training/` using `git add -- training` and commit with
  `git commit -m "training: add B02 apprenticeship materials" -- training` (pathspec commit). Commit messages: use `-F <file>` if multi-line.
- **Incident branches:** never switch the main working tree's branch. For each incident use a worktree:
  `git -C <repo> worktree add <SCRATCH>\<repo>-inc-NNN -b training/incidents/NNN-slug HEAD` → edit there → commit there →
  `git -C <repo> worktree remove <SCRATCH>\<repo>-inc-NNN`. SCRATCH = `C:\Users\Owner\AppData\Local\Temp\claude\C--Users-Owner-Desktop-opusorganize\c655b30d-97ab-4d7f-b112-a2000c3afe47\scratchpad`.
  Use a UNIQUE scratch subfolder per project (e.g. SCRATCH/<project>/). Incident branches are based on HEAD (committed code), so check the bug makes sense against committed files.
  Note: HEAD won't contain your training/ commit if you create worktrees first — order doesn't matter, incidents only touch source.
- Keep bug diffs small and realistic (like a plausible PR). Where feasible and cheap, run `dotnet build` on the affected project inside the worktree to
  make sure the incident compiles; if you skip it or it fails for environment reasons, mark the incident `BUILD: UNVERIFIED` in its answer file.
  Do not run the full test suites of huge OSS repos. Don't install global tools. Don't start long-running servers.
- **For OSS clones (READ tier):** no incident branches, no source edits; write only `training/` and commit it the same pathspec way.
- Don't write to shared files (`apprenticeship\COMPETENCY_GRAPH.md`, `apprenticeship\curriculum\`, `PROGRESS.md`). Instead, report needs in your output file.

## Your two outputs
1. Materials inside `<repo>\training\` (+ incident branches), per the master prompt's layout: `ladder/`, `review/`, `incidents/`, `navigation/`,
   `agentic/`, `interview/`, `_answers/`, plus `training/README.md` = the index + a suggested order + time estimate.
2. A report file `C:\Users\Owner\Desktop\opusorganize\batch2report\projects\<project>.md` with:
   - tier, what you created (paths), incident branch names + 1-line symptom each (NOT the cause), commit hashes
   - verification: what you built/checked, what's UNVERIFIED
   - issues found in the project (secrets: report location only, never values; things presented as working that aren't)
   - **skill links** for the competency graph: `skill area → exercise/incident/question path`
   - **curriculum needs**: concepts you referenced that deserve ONE central page (title + 2-line scope), don't write them
   - existing learning-doc trees in the repo and your KEEP / MERGE / CONVERT / IGNORE verdict for each
   - honest caveats

Quality bar: every exercise names real files and data from THIS repo; answers sealed in `_answers/`; no generic tutorials; tickets and incident briefs ≤ 1 page.

## B02-specific rules
- These are LLM-built course repos with remotes on github.com/elirc. **Never push.** Commit locally only.
- **Existing planted-flaw ledgers are answer keys** (`FLAW-LEDGER.local.md`, `docs/sprints/flaw-ledger.md`): the learner may have seen them. Do NOT reuse
  those flaws as your incidents; design NEW ones. In `training/README.md`, tell the learner which existing ledgers/docs are spoilers to avoid.
- Node/TS repos have no `node_modules`. Parallel package installs have broken this machine before, so: only the gitjira-app agent may run
  `npm ci` (once, inside an incident worktree or the main tree — node_modules is gitignored). All other TS agents: do NOT install; verify incidents
  by careful reading and mark `BUILD: UNVERIFIED (no deps installed)`. .NET repos: `dotnet build` is fine (SDK 10.0.302 installed; if global.json pins an
  older SDK, override it only inside the worktree and never commit that).
- Report `.env`/secret locations only.

## HARD SAFETY RULE (added 2026-09-24 after a data-loss incident)
Never recursively delete anything inside a repo (no rm -rf / Remove-Item -Recurse / rmdir /s), especially node_modules: workspace junctions make recursive deletes destroy real source. If deps are broken, stop and report.
