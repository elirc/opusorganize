# vg (Velocity Grid): B07 report

- **Path:** `C:\Users\Owner\Desktop\_Organized Desktop\09 Grav And VG Projects\vg`
- **Tier:** DRILL (Phase 3 + mini interview kit). I added a characterization harness because legacy rescue is a thin skill.
- **Git:** the repo had no usable `.git`: the old folder held only a GitKraken `gk/config`. I moved it to `.git_broken_backup/` (excluded via
  `.git/info/exclude`, not deleted), ran `git init`, and committed a baseline, **`99bb8b2` "chore: baseline snapshot before training"**
  (respects `.gitignore`: no `node_modules`, no `.env`). Training commit: **`c74a7f0`** (pathspec `-- training` only). Nothing pushed; no remote.
- **Deps:** `npm ci` in the main tree (package-lock). Vitest was **not** added to `package.json`. It runs via `npx vitest@3`, or the scratch install at
  `<SCRATCH>\vg\tools`.

## Created (all under `vg\training\`)
- `README.md`: index, order, ≈9-10 h
- `review/EXERCISE.md`, `review/COMPARE.md`, `review/CHARACTERIZATION_PAYROLL.md` (legacy-rescue ticket)
- `harness/`: `vitest.config.mjs`, `global-setup.mjs` (refuses DB names without test/training), `helpers.mjs`, `README.md`, and a learner skeleton `payroll.characterization.test.mjs`
- `incidents/001-completed-run-no-payslips.md`, `incidents/002-leave-pending-days-jump.md`
- `interview/TECHNICAL_QUESTIONS.md` (10), `interview/PROJECT_STORIES.md` (4)
- `_answers/review.md` (23 findings: 13 from the earlier fable review, plus new R5 R6 R7 R14 R15 R16 R19), `_answers/characterization/payroll.characterization.test.mjs`
  (reference suite with 13 tests and 10 `BUG?` pins), `_answers/incidents/001…md`, `_answers/incidents/002…md`, `_answers/interview.md`

## Incident branches (from `99bb8b2`)
| Branch | Commit | Symptom |
|---|---|---|
| `training/incidents/001-completed-run-no-payslips` | `ce903a3` | The payroll run shows COMPLETED, but no employee gets a payslip and no item is PAID |
| `training/incidents/002-leave-pending-days-jump` | `fd2260d` | Pending leave jumps to 32 after a 3-day + 2-day request; later requests are rejected as "Insufficient leave balance" |

Worktrees were removed after committing. `git worktree list` shows only the main tree.

## Verification
- **INC-001 mechanism verified** with this repo's `@prisma/client`: an un-awaited `updateMany` sends no query and raises no error; awaiting it does
  hit the DB (it raised `PrismaClientInitializationError` against an unreachable URL).
- **INC-002 mechanism verified** with `Prisma.Decimal`: `Decimal(0)+3 === "03"`, `Decimal(3)+2 === "32"`, `Decimal("1.5")+1 === "1.51"`;
  `Decimal - Decimal` stays numeric (`10-3-0 = 7`).
- Both incident files pass `node --check`. All harness and reference `.mjs` files pass `node --check`.
- **UNVERIFIED: the reference characterization suite has not been confirmed green end to end.** Before the disk-full crash, a run against
  `postgres:16-alpine` reached the payroll tests and failed with Prisma's `Transaction not found`. That is a real finding (R14: `calculatePayrollRun`
  does `db` reads inside a 5 s interactive transaction), made worse by this slow laptop. After the resume, **Docker hung**: even `docker ps` timed out
  (124) three times, so I couldn't re-run. The expected totals were computed by hand and checked with a float-vs-exact rounding script, not by a green run.
  Next step: run `training/harness/README.md` on a responsive Docker. If the timeout still hits, either note it as the finding or raise
  Prisma's `transactionOptions.timeout` via env in the harness only.
- **Cleanup needed by the orchestrator:** a queued `docker run --name vg-training-pg` (port 55437) may appear once Docker recovers.
  Remove it with `docker rm -f vg-training-pg`.

## Issues found in the project
- **Secrets:** a real `.env` sits at the repo root (gitignored, not committed; values not read into any output). `src/lib/auth.js:10` falls back
  to a hardcoded public `AUTH_SECRET` string.
- **Presented as working but isn't:** leave management (no accrual code; balances start at 0, so every request 400s: R19); "encrypted bank
  details" (the column doesn't exist, and `encryptField` is never called); the domain-event outbox (never retries FAILED, no atomic claim; "processing" just
  writes `IntegrationLog SUCCESS`: R16); every payroll write answers 500 after committing (BigInt, fable A1).
- **New money bugs:** a future-dated raise zeroes pay (R5); YTD counts unapproved CALCULATED runs (R6); the YTD year uses the server's local TZ (R7).
  This laptop is UTC-7, so R7 is live here for January runs.

## Skill links (for COMPETENCY_GRAPH)
- testing / **legacy rescue (characterization)** → `vg/training/review/CHARACTERIZATION_PAYROLL.md` + `harness/` (real Postgres; teeth check against INC-001)
- reliability/incidents → `incidents/001` (lazy promise / silent success on an empty set), `incidents/002` (Decimal `+` concatenation)
- data modeling / money → `_answers/review.md` R5-R9; `TECHNICAL_QUESTIONS.md` Q4, Q5, Q6
- transactions → Q2, Q3 (side effects and `db` reads inside `tx`); R14/R15
- async jobs / outbox → Q8, R16 (curriculum 01)
- code review → `review/EXERCISE.md` + `COMPARE.md`
- agentic engineering / verify-before-trust → INC-002 (a PR comment's false claim about ORM types), `interview/PROJECT_STORIES.md` #4
- authz → Q9 only (saturated, so no new exercises added)

## Curriculum needs (don't write; candidates for one central page each)
1. **Money and time in payroll-like code:** integer minor units vs Decimal vs float, rounding rules as product decisions, UTC period boundaries,
   and effective-dated records (`isCurrent` flags vs effective-date queries). vg R5/R7/R9, atlas and VGdemo would all link here.
2. **Lazy/floating promises and ORM return types in plain JS:** `PrismaPromise` laziness, `Decimal`/`BigInt` at boundaries, `@ts-check`/`checkJs` as a
   cheap safety net for legacy JS. Recurs in INC-001/002 and the fable A1 BigInt 500.

## Existing learning-doc trees
- `fable/` (5 files, an evidence-based bug/scope review): **CONVERT TO EXERCISE**. It's now the "second reviewer" in `_answers/review.md` (cited as
  [fable …]), and the exercise tells the learner not to open it first. Keep it in place.
- `docs/architecture.md`, `automation-opportunities.md`, `improved-implementation-plan.md`: **IGNORE** (generic generated plans).
- `docs/file-explanations/` (a per-file narration mirror of `src/`): **IGNORE**. It's passive and repeats the code.

## Caveats
- The DRILL scope was stretched with the harness/characterization ticket, since that skill is thin. There's no ladder or navigation pack.
- Incident briefs include fictional org and run ids and counts (e.g. 212 employees). The mechanisms are real and verified.
- The reference suite's exact expected numbers are hand-derived and still need one green run (see Verification).
