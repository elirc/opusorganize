# VGdemo (GlobalHire Lite, TS → .NET port) — B07 DRILL report

**Repo:** `C:\Users\Owner\Desktop\_Organized Desktop\09 Grav And VG Projects\VGdemo`. **Tier:** DRILL (Phase 3 + small Phase 5 kit).
**No `.git` existed.** I ran `git init` and committed a baseline, `61367ad chore: baseline snapshot before training` (respects the repo `.gitignore`:
node_modules, bin, obj, .env, *.log). The branch is `master`. No remote. Nothing was pushed.
The session was interrupted by the disk-full incident and resumed. The work was finished after the resume; nothing was redone.

## Commits
- `61367ad` baseline (master)
- `1d5af1c training: add B07 apprenticeship materials` (master, pathspec commit of `training/` only)
- `7955c9f` on `training/incidents/001-locked-payroll-reopened`
- `23e02c7` on `training/incidents/002-worker-missing-from-payroll`

## Created (`training/`)
- `README.md`: index, order, about 7 h, run notes, doc-tree warnings
- `review/EXERCISE.md`, `review/COMPARE.md` → `_answers/review.md` (24 findings: 5 Critical, 6 High, 7 Medium, 6 Low; each labelled regression/inherited/AI-smell)
- `review/port-parity/EXERCISE.md` + `contract.mjs` (a zero-dependency Node black-box contract, 20 checks, with a route-drift fallback) + `tools/restore-ts-oracle.mjs`
  (un-comments the `// MIGRATION_NOTE` TS original into a folder *outside* the repo) → `_answers/port-parity.md` + `_answers/port-parity-runs/*.txt` (recorded live output)
- `incidents/001-locked-payroll-reopened.md`, `incidents/002-worker-missing-from-payroll.md` → `_answers/incident-00{1,2}.md`
- `_answers/regtests/PayrollRecalculationGuardTests.cs`, `PayrollCompletenessTests.cs` (xUnit regression tests for the incidents)
- `interview/PROJECT_STORIES.md` (5 STAR skeletons), `interview/TECHNICAL_QUESTIONS.md` (10) → `_answers/interview-questions.md`

## Incidents (symptom only)
- `training/incidents/001-locked-payroll-reopened`: a LOCKED payroll run shows CALCULATED again with new totals, and its already-issued invoice no longer matches.
- `training/incidents/002-worker-missing-from-payroll`: an ACTIVE new hire is missing from a locked payroll run, with zero errors anywhere.

## Verification (all 2026-09-24)
- **.NET build/tests:** the projects target net8.0 and only SDK 10 is installed. Everything ran with `DOTNET_ROLL_FORWARD=Major`. Baseline suite: 10 tests, green.
  - INC-001 branch + guard regtest: **3/3 new cases fail** (10 existing pass). On master: they pass.
  - INC-002 branch + both regtests: **2 fail** / 13 pass. On master: 1 fails (that one is the test for the *fix*, by design) / 14 pass.
- **Live parity run:** I restored the TS oracle into scratch, `npm install` (see issues), seeded it on a private native PostgreSQL 18 (port 55440), and ran the .NET API on 5391
  and the INC-001 branch on 5392. Contract results: TS 17/20, .NET 13/20 (7 diverge, 2 route drifts), INC-001 branch 11/20 (C19/C20 reproduce the incident live).
- **Not live-verified (static only):** the bearer-token-is-user-id bypass (Part C #1), worker self-approval, offboarding self-complete, concurrency corruption, rounding drift (marked UNKNOWN).
- **Cleanup:** both incident worktrees removed; all 3 API processes and PG stopped. No Docker used. Left in scratch (outside any repo, not deleted per the no-recursive-delete
  rule): `SCRATCH/VGdemo/ts-oracle2` (restored TS app **with node_modules**), `ts-oracle`, `pgdata` (stopped PG cluster), `regtests`, and logs. The orchestrator can reclaim them.

## Issues found in the project
- **Authentication bypass:** the bearer token = raw user id (`migrated-dotnet/src/GlobalHireLite.Api/Program.cs:48,420-428`), and seeded ids are guessable (`user-admin`).
- Plaintext passwords with a shared default on the entity (`Domain/Entities.cs:7`).
- Role gates missing vs TS on payroll approve/lock, onboarding review (also no tenant check), timesheet/leave review (workers can self-approve), offboarding and onboarding submit.
  Live: C07 and C16 return 200 where TS returns 403.
- No request validation (live: negative salary and `"DOLLARS"` currency accepted), 403/404 collapsed to 400, partial state machines, a non-thread-safe singleton `List<T>` store, and no persistence.
- **Presented as working, but isn't:** `migrated-dotnet/README.md` claims the API "mirrors the original Express routes" and admits the SDK "was not available on this machine when the
  migration files were created". It has route drift (POST→PATCH, `generate-invoice`→`invoice`) and response-shape drift that break the original web app.
- **The TS oracle is broken too:** `npm ci` fails (the lockfile is out of sync with package.json), and validation errors return **500** instead of 400 because two zod copies
  (`apps/api/node_modules/zod`, `packages/shared/node_modules/zod`) defeat `instanceof ZodError` in `apps/api/src/middleware/error.middleware.ts:10`.
- **Secrets (locations only):** `globalhire-lite/apps/api/.env` (gitignored, untracked); a hardcoded JWT_SECRET default in `globalhire-lite/apps/api/src/config/env.ts` (commented-out TS);
  dev DB credentials in `globalhire-lite/docker-compose.yml`; the default password in `Domain/Entities.cs:7`.
- `globalhire-lite/api.dev.log`, `api.runtime.log`, `web.dev.log` sit in the tree. They are excluded from the baseline by the `*.log` rule I added in `.gitignore`.

## Skill links (for the competency graph)
- code migration / porting regressions → `training/review/port-parity/EXERCISE.md`, `incidents/002-worker-missing-from-payroll.md`, TQ 2, 8
- black-box contract / characterization testing → `review/port-parity/contract.mjs`, `_answers/regtests/*`, TQ 8
- state machines / forbidden transitions → `incidents/001-locked-payroll-reopened.md`, TQ 5
- data canonicalization + fail-closed money code → `incidents/002-worker-missing-from-payroll.md`, TQ 9, 10
- .NET/ASP.NET Core auth (cookie/JWT, policies) → TQ 1; review findings 1–5
- .NET/EF Core + SQL Server design (unique index, rowversion, conditional update, 2601/2627) → TQ 4 (question only, **no SQL Server lab**, because the port has no DB)
- money/rounding parity → TQ 6; review finding 18
- verify-before-trust (never-compiled port, oracle bug) → `review/EXERCISE.md`, `_answers/port-parity.md`
- code review (migration PR) → `review/EXERCISE.md` + `COMPARE.md`

## Curriculum needs (one central page each; not written)
- **Port-parity testing (strangler/oracle contracts):** running old and new side by side over HTTP, classifying divergences (regression / oracle defect / intentional drift),
  and a KNOWN_DRIFT allow-list as a CI gate. Recurs in VGdemo, and likely in atlas and the *-net rebuilds.
- **Implicit guarantees audit when switching stacks:** list what the old framework/ORM/validator enforced implicitly (requireRole, zod, `$transaction`, unique constraints, bcrypt) and
  check each one in the new stack. It is the top lesson of this project.
- (Optional) **State-machine guards: allow-list source states + a transition-matrix test.** It might fold into 04-characterization-tests.

## Existing learning-doc trees
- `fable/` (8 files, about 1.8k lines, an accurate review of the .NET port): **KEEP**, but it spoils the blind review. The README tells the learner to read it after exercise 1.
  Its exercises 2.1/2.2 overlap the saturated authz skill.
- `globalhire-lite/docs/learning` (14), `architectural-cartographer` (7), `mission-learning-path` (6), `user-story-build-path` (3): all describe the TS/Prisma stack (no .NET mentions),
  which is now commented out. **IGNORE** for training. They are useful only as the oracle's spec.
- `globalhire-lite/prep/` (13 files, .NET interview prep): **MERGE**. It holds near-duplicate pairs (`001-`/`01-`, `007-`/`07-`, `008-`/`08-`, which differ slightly). User material, left untouched.
- `docs/learning/` at the repo root: empty. **IGNORE**.

## Caveats
- No SQL Server/EF Core lab: the port is purely in-memory, and adding EF Core to it would be a rewrite, not a PR-sized incident. The SQL Server depth is interview questions only.
- The live parity numbers depend on the seed and the random period years in `contract.mjs`. The TS oracle was freshly seeded. The .NET API had already served earlier requests before the recorded run, which is harmless because the checks create their own data.
- `restore-ts-oracle.mjs` was used to produce the oracle, but the oracle's install needed `npm install` (which rewrote its lockfile in scratch), not `npm ci`.
