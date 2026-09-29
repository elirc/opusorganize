# B07 — globehire — DRILL tier

Repo: `C:\Users\Owner\Desktop\globehire` (.NET 10 modular monolith; a fictional EOR/workforce platform; 69 files / ~2.9k lines in `src/`, 4 test projects). Remote `github.com/elirc/globehire` exists and **was not pushed**.

## Git
- The repo already had git (main @ `22eeb47`). No baseline commit was needed.
- Training commit **`36018f1`** "training: add B07 apprenticeship materials" on `main`, pathspec `-- training` only (11 files).
- The user's 3 uncommitted items were left untouched (verified before and after): `M README.md`, `?? astraupskill/`, `?? tests/GlobeHire.Application.Tests/HireCases/`.
- Incident worktrees were created under `scratchpad/globehire/`, committed, then removed with `git worktree remove`. `git worktree list` now shows main only.
- Resumed after the disk-full crash: the temporary repro probes are all deleted, and the worktrees were clean before removal.

## Created (`training/`)
- `README.md`: index, order, ~6.5 h estimate, links to central curriculum 02/03/04/05/13
- `review/EXERCISE.md` (60-min blind review framed as a "swap to SQL Server and go" pilot), `review/COMPARE.md` (scorecard → misses → pattern → habit)
- `_answers/review.md`: 23 ranked findings with file:line evidence, `[AI-smell]` tags, a "what's good" section and grading notes
- `incidents/001-approver-identity.md`, `incidents/002-start-date-calendar.md` (≤1 page each: alert, logs, metrics, suspect PR diff, no cause)
- `_answers/incident-001-approver-identity.md`, `_answers/incident-002-start-date-calendar.md` (root cause, diagnostic path, fix, regression tests, postmortem)
- `interview/PROJECT_STORIES.md` (5 STAR skeletons), `interview/TECHNICAL_QUESTIONS.md` (10 questions), `_answers/technical-questions.md`

## Incident branches (symptom only)
| Branch | Commit(s) | Symptom |
|---|---|---|
| `training/incidents/001-approver-identity` | `fb15c04`, `5217ca6` | After a deploy, Legal approvals fail with a separation-of-duties error, and Finance approvals across tenants show one person's name (a different one per pod). A restart helps briefly. |
| `training/incidents/002-start-date-calendar` | `bb8077c` | US workforce plans are accepted with yesterday's start date, and later activation of the same worker is rejected. Start-date 422s *dropped* after the "fix". |

## Verification
- `dotnet test GlobeHire.slnx` on the 002 branch: **all green** (Domain 43, Architecture 3, Application 6, Api 8). The bug ships past CI, as intended.
- 001 branch: Api test project builds and its new single-request test passes. The **bug was reproduced live** with a throwaway two-request test (expected `finance-bo`, got `finance-ana`), then deleted.
- 002: the **bug was reproduced live** with a throwaway 4-row table test (US 10:00 ET → 07-14; GB 00:30 BST → previous day; the reported 21:30 ET case and GB winter are correct), then deleted.
- Review findings 3, 5 and 6 were **verified live** against the API (second offer for the same hire case → 201; idempotency key reused with a different body → 200 with the old plan; role `"7"` → 200). The other findings are static evidence.
- UNVERIFIED: the claim that in the Development environment `builder.Build()` throws on the singleton→scoped capture (documented .NET behaviour, not run). SQL Server was not used; this repo's incidents target DI/time, not the database.

## Issues found in the project (main; not fixed, they are review material)
1. `docs/quality/FLAW-HARVEST.md` row 4 claims the approval race was fixed by atomic mutation, but hire-case writes are still unlocked read-then-mutate (`src/GlobeHire.Application/HireCases/HireCaseUseCases.cs:58-59, 69-70`). **Docs claim more than the code does.**
2. Multiple offers per hire case lead to multiple employments (`OfferUseCases.cs:30-35`; employment dedupe is per offer). Verified.
3. Idempotency replay ignores the body (`InMemoryWorkforcePlanRepository.cs:33-37`). Verified.
4. `Enum.TryParse` accepts numeric roles (`OfferEndpoints.cs:32`). Verified.
5. The employment-change endpoint takes `Today` from the request body (`EmploymentLifecycleEndpoints.cs:18,30`).
6. **Presented as working but isn't:** Sprints 6–13 features (payroll, people-ops, contractors, employment changes, integrations, bulk/report, compliance) are stateless "validate" endpoints that persist nothing; the workforce report always returns `items: []` (`BulkDataEndpoints.cs:13-19`). Payroll preview trusts caller-supplied rates.
7. No auth and in-memory storage are **honestly disclosed** (README, ADR-0002, `/health/ready` reports `durable=false`).
- Secrets: none found. No `.env` is tracked, the tracked `appsettings*.json` have no keys or connection strings, and grep hits for "secret/password" in docs/CI are prose only. `FLAW-LEDGER.local.md` (an answer key) is correctly gitignored.

## Skill links (for COMPETENCY_GRAPH)
- .NET/EF Core depth (DI lifetimes, captive dependency, scope validation) → `training/incidents/001-approver-identity.md`; TECHNICAL_QUESTIONS Q1, Q2, Q6
- data modeling / concurrency / migrations (SQL Server concurrency token, unique index) → TECHNICAL_QUESTIONS Q5, Q6, Q7; review findings 3, 4
- correctness: calendar dates vs instants → `training/incidents/002-start-date-calendar.md`; TECHNICAL_QUESTIONS Q3, Q4
- testing (boundary tables, "one request proves nothing", characterization first) → both incident answers; Q4, Q10
- API design (412/428 vs 422, Location escaping) → review findings 11, 21; Q9
- idempotency → review findings 5, 14; Q8 (**saturated**: review items only, no new exercise)
- security (actor spoofing, SSRF on webhooks) → review findings 2, 13
- code review → `training/review/EXERCISE.md` + `COMPARE.md`
- reliability/incidents + telemetry correctness ("the error rate dropped and that was the bug") → incident 002
- legacy rescue → TECHNICAL_QUESTIONS Q10; PROJECT_STORIES #4
- agentic engineering / verify-before-trust → both incidents (true PR descriptions, green CI); PROJECT_STORIES #5

## Curriculum needs (one central page each; not written)
- **DI lifetimes & captive dependencies (.NET)**: singleton/scoped/transient, root-provider resolution, `ValidateScopes`/`ValidateOnBuild`, why "stateless" is a claim about the whole dependency graph over time.
- **Calendar dates vs instants**: when a business date is a local calendar date, "today in zone X", DST, choosing boundary instants for tests, where the zone should live (policy data).

## Existing learning-doc trees → verdict
- `docs/sprints/`, `docs/concepts/`, `docs/adr/`, `docs/quality/`, `docs/operations/`, `docs/security/`, `docs/curriculum/`, `LEARNER-GUIDE.md`, `TESTREADME.md`, `OEReadMe.md`: **KEEP** (the project's own course; ADR-0002 and THREAT-MODEL are good). Caveat: FLAW-HARVEST overclaims (see issue 1). Linking it as "trust but verify" material is itself useful.
- `astraupskill/` (untracked, user WIP): **KEEP, untouched.** It's a tenant-boundary lab on the same hire-case path. It overlaps the saturated authz/IDOR skill, so don't MERGE.
- `FLAW-LEDGER.local.md`: **IGNORE** (answer key; its five flaws are already harvested in FLAW-HARVEST).

## Caveats
- DRILL tier: no ladder/navigation/agentic material, by design.
- Both incidents avoid the saturated skills (authz/IDOR, races, idempotency). 001 *touches* approval identity, but the lesson is DI lifetime, not authz.
- Incident briefs quote "PR #76/#77/#78". Those are fictional PR numbers; the real commits exist only on the local training branches.
- The review's line numbers are against `main @ 22eeb47`.
