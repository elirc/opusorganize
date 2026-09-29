# astra5 — Stockade

Tier: **DRILL** (Phase 3 + mini interview kit only, per B05_AGENT_BRIEF). Batch focus: sagas & compensation
across a polyglot boundary (Next.js ↔ .NET "Fulfil" service).

## What was created

Committed to `main` in one pathspec commit `bdd63f9` ("training: add B05 apprenticeship materials"), on top
of the pre-existing single commit `7a9e422`:

- `training/review/EXERCISE.md` — 60-min timed blind-review prompt scoped to `Worker.cs`, `Commerce.cs`,
  `Payments.cs`, `Integrations.cs`, `Rules.cs`, `Data/Transactions.cs`, `StockadeDb.cs`, plus the Next.js
  proxy/SDK.
- `training/review/COMPARE.md` — self-vs-model compare template.
- `training/_answers/review.md` — sealed, 16 ranked findings, each with file/line evidence, covering
  correctness, security, concurrency/sagas, performance, operability, tests, maintainability.
- `training/incidents/001-payment-status-drift.md` — on-call brief, no hint of cause.
- `training/_answers/incidents/001-payment-status-drift.md` — sealed root cause, mechanism trace, why tests
  stayed green, why the app's own health metric missed it, fix, regression test, postmortem.
- `training/interview/PROJECT_STORIES.md` — 5 STAR-story prompts (debugging, trade-off, incident, migration
  /consistency, agent-caught-bug), all citing this repo.
- `training/interview/TECHNICAL_QUESTIONS.md` — 10 questions; Q1–Q5 are a dedicated "sagas vs. 2PC vs.
  outbox" set built entirely from this codebase's own code (`Worker.cs`, `Commerce.cs`, `Data/Transactions.cs`,
  `OutboxEvent`); Q6–Q10 cover API contracts, DB integrity, frontend proxy/cookie design, testing, ops.
- `training/README.md` — index, suggested order (~2.5–3.5h), real-vs-planted disclosure, curriculum links,
  doc-tree verdicts, caveats.

**Incident branch:** `training/incidents/001-payment-status-drift` (local only, not pushed), based on `HEAD`
`7a9e422`, commit `5b0a209`.
- 1-line symptom (no cause): checkout orders that require 3-D Secure/bank action get stuck forever —
  customer never gets a confirmation, order never ships, the admin dashboard's "Stuck payments" counter never
  lights up.
- `dotnet build` verified green (0 warnings/errors) in an isolated worktree before committing.

## Verification

- **Built:** `dotnet build` on `services/Fulfil` inside the incident worktree — succeeded (0 warnings, 0
  errors, ~82s). Incident is `BUILD: VERIFIED` (not unverified).
- **Not run:** `npm ci` / the TS/Playwright/Vitest suite. Skipped deliberately — the working tree already has
  4 modified + 5 untracked files including in-progress TS changes (`src/lib/health.ts`,
  `tests/health.test.ts`, `src/components/Panels.tsx`) tied to a refund-health feature the user is mid-way
  through. Running `npm ci`/tests risked interacting with that state or producing a misleading result against
  unfinished work, so it was skipped and disclosed in `training/README.md` rather than attempted. If the TS
  side should be verified, run it yourself in a clean checkout of this repo.
- **Not run:** Docker/compose (no incident needed a live Postgres; the reviewed logic and the planted bug are
  both statically traceable and the C# side was verified via `dotnet build`, not a live DB). No containers
  were started, so none needed to be stopped.
- Review findings were derived by reading committed `HEAD` source directly (not the 9 modified/untracked
  working-tree files, which were read only where already-modified files needed a `git show HEAD:<path>`
  baseline — e.g. `Panels.tsx` — never their working-tree contents).

## Issues found in the project (for the record, not necessarily "planted")

- **Real bug (not planted), most severe finding:** `services/Fulfil/Services/Worker.cs:70-78` — the
  `void_pending` reconciliation branch runs `CompleteCapture` and the subsequent release/refund/cancel step as
  **two separate committed transactions**. If the process crashes between them, the order is left captured
  (money taken), stock never released, refund never queued, and — because `PaymentState` becomes `"captured"`,
  which is outside the recovery scan's state filter (`Worker.cs:24`) and `Attempts` is never incremented — the
  order silently drops out of the reconciliation loop forever and is invisible to the app's own `stuckSagas`
  health metric. Full detail in `training/_answers/review.md` finding 1.
- **Contract drift (planted for INC-001):** the payment-state vocabulary (`"action_required"`, etc.) is a bare
  `string` duplicated across `Payments.cs`, `Rules.cs`, `Worker.cs` (4 sites), `Integrations.cs` — no shared
  enum/constant. The one function that produces it from Stripe (`Payments.Parse`) is also the one code path
  the existing test suite structurally cannot reach, because `Payments:Mode=Simulator` (what tests/dev use)
  bypasses it entirely.
- **Secrets:** none found in the reviewed source. `docs/SECURITY.md` and `Payments.cs:58`/`61-62`
  (`SimulatorGuard`, the `sk_test_` prefix check) actively guard against live keys; no hardcoded secrets or
  fallback keys were seen in `services/Fulfil` or `src/`. Not reporting any location because none was found —
  did not exhaustively grep `.env*`/uncommitted files per the "never touch the 9 uncommitted files" rule, so
  this is scoped to committed source only.
- **Presented-as-working-but-isn't:** none found beyond finding 1 above (which the app doesn't claim to have
  solved — `stuckSagas` is presented as a real signal but has a real blind spot, which is a finding, not a
  false claim in the docs). `docs/SECURITY.md` is notably honest about unverified areas (quoted in review
  finding 16) — a strength, not a smell.

## Skill links (for the competency graph)

- **Sagas / compensation across services** (thin skill, per batch focus) → `training/_answers/review.md`
  finding 1 (split-transaction stuck saga) · `training/incidents/001-payment-status-drift.md` +
  `_answers/incidents/001-payment-status-drift.md` (contract-drift stuck saga) ·
  `training/interview/TECHNICAL_QUESTIONS.md` Q1–Q5 (sagas vs. 2PC vs. outbox, all project-specific)
- **Idempotency** (saturated per B05 rules — no new exercises added, only cross-referenced) →
  `Data/Transactions.cs` `Command()` idempotency-key handling, cited in review finding 5 and
  `TECHNICAL_QUESTIONS.md` Q4/Q5; linked to `apprenticeship/curriculum/02-idempotency.md`
- **Outbox pattern** → `Worker.Deliver` (`Worker.cs:168-210`), contrasted against the saga design in
  `TECHNICAL_QUESTIONS.md` Q4; linked to `apprenticeship/curriculum/01-transactional-outbox.md`
- **Contract drift / API versioning between polyglot services** → INC-001 in full; review findings 2, 13
- **Code review (blind, staff-level)** → `training/review/EXERCISE.md` + `_answers/review.md` (16 findings)
- **Operability / health signals that lie** → review finding 6, INC-001's "why didn't `stuckSagas` catch it"
  section
- **DB integrity (CHECK constraints + app-level guards)** → review finding 7,
  `TECHNICAL_QUESTIONS.md` Q7
- **Reliability / incidents (sealed postmortem)** → `_answers/incidents/001-payment-status-drift.md`

## Curriculum needs (concepts referenced, not written — central pages only)

- **"Sagas vs. two-phase commit vs. outbox"** (2-line scope: when to coordinate multi-system state with a
  sequence of local transactions + compensation vs. XA/2PC vs. an outbox+consumer; how to choose given
  external-system control and downtime tolerance). Referenced heavily in `TECHNICAL_QUESTIONS.md` Q1–Q4 and
  review finding 1/INC-001, but no `apprenticeship/curriculum/` page currently covers this triad head-on —
  `01-transactional-outbox.md` and existing concurrency pages are adjacent but don't compare the three. This
  is the orchestrator's requested topic; recommend adding it as the next curriculum page (e.g. `16-`).
- No other new central-curriculum concept was needed beyond what 01/02/14 already cover; this project mostly
  needed *application* of those, not new concept prose (per Hard Rule 5, dedupe against the central
  curriculum — did not write per-project copies).

## Existing learning-doc trees — KEEP / MERGE / CONVERT / IGNORE

| Tree | Verdict | Why |
|---|---|---|
| `astradocs/` (6 files, committed) | **KEEP** | Career/roadmap style (CODE_WALKTHROUGHS, SWE_ROADMAP, PROJECT_SUMMARY, NEXT_STEPS, LEARNING_LOG_TEMPLATE, README) distinct from this batch's exercise-based material; no overlap to merge, link it from the competency graph as-is |
| `astraupskill/` (untracked, one of the 9 uncommitted paths) | **IGNORE for this pass** | It's the user's own in-progress work (generic 8-chapter template + evidence/snapshots tied to the uncommitted refund-health feature). Never touched, per the hard rule. Revisit once committed. |
| `docs/` (11 files: ARCHITECTURE, SECURITY, API, CONTRACT_LOG, OPEN_THREADS, PERFORMANCE, PHASE_2_STORIES, RUNBOOK, UPSKILLING, VERIFICATION, runs/) | **KEEP as product docs** | Real engineering documentation, not teaching material — out of scope to convert. `docs/SECURITY.md` was cited directly as a review strength (finding 16); `docs/UPSKILLING.md`/`PHASE_2_STORIES.md` weren't read in depth this pass (DRILL tier budget) — worth a look if this project is ever promoted to LAB |

## Honest caveats

- This project was pre-tiered **DRILL** by the orchestrator/brief, not re-triaged by me — I did not re-run
  Phase 1. Given the depth of material found (deepest saga/security modeling in the astra family per the
  batch-06 audit), it would be a strong **LAB** candidate for a future batch if the orchestrator wants the
  full ladder/navigation/agentic treatment.
- Only 1 incident was planted (DRILL allows 1–2). A second, distinct "non-idempotent compensation double-
  releases stock" incident (the other example in the batch-focus prompt) was investigated but not planted:
  `Commerce.Release`'s reservation-state guard (`Commerce.cs:146-156`) is currently correct and idempotent by
  construction, and every double-release scenario I could construct required either breaking that one guard
  in a way that wouldn't survive `dotnet build`'s own logic review as "realistic" (too on-the-nose) or relying
  on a race the `Serializable` isolation level + advisory-lock leasing already close. I judged the single
  contract-drift incident plus the real (unplanted) split-transaction finding gave better, more honest
  coverage of "sagas & compensation" than forcing a second, weaker planted bug. Flagging this so the
  orchestrator can ask for a second incident explicitly if desired — the idempotency angle is instead covered
  as review finding 5 + `TECHNICAL_QUESTIONS.md` Q5.
- TS/frontend side was reviewed by reading source only (proxy route, SDK, Admin/OrderDetail/Panels via `git
  show HEAD:`), not executed — see Verification section for why `npm ci`/tests were skipped.
- `git commit` produced CRLF-conversion warnings (`LF will be replaced by CRLF...`) on every new file — cosmetic,
  matches this repo's existing line-ending convention (no `.gitattributes` enforcing LF was present), not an
  error.
