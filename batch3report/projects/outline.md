# outline (masteroutline) — B03 report

**Path:** `C:\Users\Owner\Desktop\masteroutline\outline`
**Tier:** READ (Phase 4 only, per B03_AGENT_BRIEF.md)
**Stack:** TypeScript monorepo — Koa/Sequelize/PostgreSQL server, React17+MobX client, Redis+Bull async, Yjs/Hocuspocus real-time collaboration.

## Git

Repo had no `.git`. Ran `git init` + baseline commit respecting `.gitignore`
(no `node_modules`; `.env`/`.env.local`/`.env.production` excluded, but
`.env.sample`/`.env.development`/`.env.test` were **not** gitignored by the
repo's own `.gitignore` and got committed as part of the baseline — these
are template/test files, same as ship in the real upstream repo; did not
inspect their contents for secrets beyond confirming they're not the
`.gitignore`-excluded runtime `.env` files).

- Baseline: `37ca0d5` — "chore: baseline snapshot before training" (2631 files)
- Training commit: `cca361b` — "training: add B03 apprenticeship materials" (pathspec commit, `-- training` only, 5 files)
- Branch: `master` (git init default on this machine, not `main`)
- Default commit type `training: ...` was accepted; no pre-commit hook rejection.

## What was created

All under `<repo>\training\` (no source files edited):

- `training/README.md` — index, scope note, suggested order across all five curricula (four existing + this one)
- `training/navigation/01-collaborative-save-path-trace.md` — file:line trace of the collaborative-edit save path: client `HocuspocusProvider` (`app/scenes/Document/components/MultiplayerEditor.tsx:94-98`) → `server/services/collaboration.ts` (Hocuspocus server config, debounce/timeout/extension order) → `server/collaboration/PersistenceExtension.ts` (`onLoadDocument` lazy-conversion-under-lock, `onChange` Redis bookkeeping, `onStoreDocument`) → `server/commands/documentCollaborativeUpdater.ts` (transaction, `lock_timeout`, content round-trip canonicalization, two independent no-op guards, `Event.schedule`) → Bull fan-out to `server/queues/processors/DebounceProcessor.ts` (distributed 5-min debounce) and `RevisionsProcessor.ts` (`done`-gated) → `server/queues/tasks/DocumentUpdateTextTask.ts` (async text/language projection refresh). Extends `fabledocs3/adr-007-crdt-triple-representation.md` rather than restating it.
- `training/navigation/02-upstream-contribution-kit.md` — this repo's actual contribution rules evidenced from `AGENTS.md` + `.github/workflows/ci.yml` (lint/types/test/audit jobs, path-filtered); a method for vetting a genuine upstream good-first-issue; a first-PR checklist; 3 real candidate change areas with placement exercises (unsealed).
- `training/navigation/03-existing-curriculum-verdicts.md` — KEEP verdicts on all four fabledocs trees + recommended 5-tree order.
- `training/_answers/02-change-candidates-answers.md` — sealed placements for the 3 contribution-kit candidates.

## Verification

- All file:line citations in the save-path trace were read directly from source (`PersistenceExtension.ts`, `documentCollaborativeUpdater.ts`, `DocumentUpdateTextTask.ts`, `MetricsExtension.ts`, `services/collaboration.ts`, `DebounceProcessor.ts`, `RevisionsProcessor.ts`, `models/Event.ts`) — not inferred from the ADR alone.
- The three contribution candidates were confirmed by direct grep/read, not assumed:
  - Candidate A (a11y): confirmed `app/components/Collaborators.tsx:167-178` `NudeButton` has no `aria-label`/`aria-labelledby` while the `PopoverContent` two lines below does.
  - Candidate B (test gap): confirmed `server/queues/tasks/DocumentUpdateTextTask.ts` has no matching `.test.ts` by listing the directory; confirmed sibling tasks do have tests; confirmed `server/test/factories.ts` exists and is the convention used by comparable task tests (read `CleanupDocumentInsightsTask.test.ts` in full).
  - Candidate C (observability): confirmed `PersistenceExtension.ts`'s `onStoreDocument` catch block (lines ~138-143) only logs, no metric; confirmed `MetricsExtension.ts`'s `onStoreDocument` hook increments `collaboration.change` unconditionally on every store attempt (not gated on success).
  - Confirmed as a supporting fact: `app/components/` has zero `*.test.tsx` files anywhere (searched the whole `app/` tree for `*.test.tsx`/`*.test.ts`; all matches are model/util/hook tests, none are component-render tests) — used to give an honest (not padded) answer on whether Candidate A needs a new test.
- **UNVERIFIED / not run:** did not run `yarn install`, `yarn lint`, `yarn tsc`, or any `yarn test:*` — no npm/yarn install was performed for this READ-tier pass (brief permits installing deps but this pass stayed read-only/static since no code changes were made that needed compiling or testing). Did not spin up Postgres/Redis/Docker. All claims about CI gates come from reading `.github/workflows/ci.yml` directly (static), not from a live CI run.
- Did not attempt to reproduce the collaboration save path against a running instance (two browsers editing the same doc) — traced statically from source only.

## Issues found in the project

- No secrets found in files that were read. `.env.sample`/`.env.development`/`.env.test` were committed as part of the baseline (per `.gitignore` rules, not excluded); did not print or inspect their values beyond confirming they're the template/test files, not the real runtime `.env`.
- Nothing presented as working that isn't found in the areas read for this pass (the 3 contribution candidates are real gaps, not claims of brokenness — they're absence-of-coverage, not bugs).

## Skill links (for the competency graph)

- **Unfamiliar-codebase navigation / distributed systems (CRDT collaboration):** `training/navigation/01-collaborative-save-path-trace.md` — builds on `fabledocs3/adr-007-crdt-triple-representation.md`.
- **Observability (thin skill area per B03 targeting):** `training/navigation/02-upstream-contribution-kit.md` §4 Candidate C + sealed answer — a real, unfiled metric-blind-spot in `server/collaboration/PersistenceExtension.ts` / `MetricsExtension.ts`.
- **Accessibility (thin skill area):** `training/navigation/02-upstream-contribution-kit.md` §4 Candidate A + sealed answer — `app/components/Collaborators.tsx:167`.
- **Testing / OSS contribution workflow:** `training/navigation/02-upstream-contribution-kit.md` §1-3 (CI gates, first-PR checklist) + §4 Candidate B (`server/queues/tasks/DocumentUpdateTextTask.ts` missing test).
- **Async jobs/queues (debounce, event fan-out):** `training/navigation/01-collaborative-save-path-trace.md` step 6 (`DebounceProcessor` + `RevisionsProcessor`'s `done`-gating) — cross-links to the saturated concurrency/idempotency skill area but doesn't add new exercises there (per B03 saturation rule); reference only.

## Curriculum needs (don't write, just flagging)

- No new central curriculum page needed. Everything referenced (CRDT collaboration mechanics, ADR-driven navigation, OSS contribution workflow) is either already covered by this repo's own `fabledocs3`/`fabledocs2`, or is specific enough to this repo (Hocuspocus extension ordering, this exact debounce architecture) that a generic central page would either genericize it against master-prompt rule 3 or duplicate what's already here.

## Existing learning-doc trees — verdicts

| Tree | Verdict | One-line why |
| --- | --- | --- |
| `fabledocs/` | KEEP | Most complete of the four; own ladder + interview prep; nothing here substitutes for it. |
| `fabledocs2/` | KEEP | Distinct onboarding-narrative voice, complements rather than duplicates `fabledocs/`; this pass's save-path trace extends its rule 5 rather than restating it. |
| `fabledocs3/` | KEEP | Rigorous evidence-cited ADRs; this pass's save-path trace is explicitly built as "one level below ADR-007," not a replacement. |
| `fabledocs4/` | KEEP | Only tree with hands-on labs/capstones; capstone 3 (collab harness) is the natural next step after this pass's trace. |

No MERGE/CONVERT candidates — full reasoning and recommended reading order across all five trees is in `training/navigation/03-existing-curriculum-verdicts.md` (not duplicated further here).

## Honest caveats

- This is a large, real OSS monorepo; the save-path trace covers the collaborative-editing write path in depth but does not trace every consumer of the triple representation (search indexing, export, public API reads) — those are named as "readers who must know which representation they're reading" per ADR-007 but not individually traced here, to stay in scope and not duplicate `fabledocs4`'s labs.
- The 3 contribution candidates are genuine, evidence-backed gaps in this local clone as of baseline commit `37ca0d5` — they were not cross-checked against the live upstream `outline/outline` GitHub issue tracker (no network access used for this), so it's possible one is already fixed or filed upstream. The kit's §2 method (how to vet a real good-first-issue) is written precisely to cover that gap — a learner using this kit for a real contribution should re-verify against live upstream before starting work.
- No dependency install or test run was performed, so the CI-gate description in the contribution kit (`§1`) is accurate to what's *configured*, not empirically confirmed to pass on this checkout.
