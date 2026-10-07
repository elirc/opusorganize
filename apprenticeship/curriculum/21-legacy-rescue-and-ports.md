# 21 — Legacy rescue and ports: "rewrote the shape, dropped the invariant"

**Situation A: untested legacy (often AI-generated) code you must change.**
1. **Check what's real first:** does it build and boot? Which features are wired vs just schema or docs ([05](05-verify-before-trust.md))?
2. **Pin the current behaviour** with characterization tests around the flow you'll touch ([04](04-characterization-tests.md)), against a throwaway DB.
3. **Triage dead weight:** unused tables and models, unconsumed queues, dead dependencies. Record a decision for each (delete, wire, or leave with a note) instead of refactoring blindly.
4. **Fix in PR-sized steps**, each with a failing test first, never "modernize everything".

**Situation B: a port or rewrite to another stack** (TS→.NET, Python→TS, Grok starter→hardened rewrite).
- The old stack gave you things **for free** that the port must re-implement explicitly: auth middleware, validation (Zod/Pydantic), role guards, transactions, error mapping (403/404 vs 400), serialization casing, rounding.
- **Port-parity testing:** run one behavioural contract against *both* implementations and classify each difference as intended, bug in the old, or bug in the new.
- Diffs lie when files are untracked: `git diff` doesn't show new auth or migration files.

**Quick reference: the implicit-guarantees audit.** Before you trust a port, list what the old framework enforced *without a line of your code saying so*, and find the line in the new stack that does it now:

| Old stack gave you | Ask of the new stack | Where it went missing in your repos |
|---|---|---|
| `requireRole([...])` middleware on the route | Is there a role check on *this* endpoint, not just "logged in"? | VGdemo payroll approve (trace below) |
| Zod / Pydantic body validation | Who rejects `salary = -5`? | VGdemo C03/C04: .NET returns 201 |
| `ApiError(404)` / `ApiError(403)` | Does "not found" still mean 404, "forbidden" 403? | VGdemo `Error()` defaults every string error to 400 |
| A state guard written as an allow-list | Is it still an allow-list? | VGdemo INC-001 (allow-list became deny-list) |
| JSON field casing the client expects | Did the wire format change in a "refactor"? | HNJOBTRACK INC-003 |
| Signed session / JWT | What *is* the token now? | VGdemo: the token is the user id |

**Where these repos live now** (checked 2026-10-06): VGdemo → `elirc/vgdemo` (HEAD `89b023b`, `main` only); vg → `elirc/vg` (`d87c0a6`, `main` only); grokbuildmultitenantproject → `elirc/grok-build-multitenant` (`e899e20`, `main` only); HNJOBTRACK → `elirc/hnjobtrack` (`a9d1080`, `main` only); reviewboard → `elirc/gravreviewboardjspy`, folder `reviewboard/` (`1048927`; the look-alike `elirc/organized-grav-vg-gravreviewboardjspy` has **no** `training/`). **None of the B06/B07 incident branches or base branches named below were pushed**: the briefs, sealed answers and regression tests are on `main`, but the branches they tell you to check out exist only on the local disk where they were made.

**Worked examples in your repos**
- **VGdemo:**
  - `training/review/` parity drill with `contract.mjs` (20 checks): TS 17/20 vs .NET 13/20 (recorded 2026-09-24 in `training/_answers/port-parity-runs/`; the files are on GitHub).
  - The port's token is just the user id, and a client admin can approve their own payroll (200 vs 403).
  - Incidents: a LOCKED payroll reopened, and a new hire missing from the run.
- **grokbuildmultitenantproject:** a legacy-diff drill (`training/review/LEGACY_DIFF_REVIEW.md`), Grok starter `41a9785` vs the hardened rewrite. *Dated:* at B06 (2026-09-24) the rewrite was uncommitted and copied to a local branch `training/base/working-tree-snapshot`. Since 2026-09-30 it **is committed on GitHub `main`** as `57a8028` "Sync local changes to GitHub" (224 files, +20,325 lines, including `backend/src/middleware/auth.ts`, `backend/src/lib/errors.ts` and the `202609090001_tenant_workspace` migration). The drill text still says "never committed"; on a fresh clone compare `41a9785..57a8028` instead (needs full history, not `--depth 1`).
- **vg:** characterize the payroll calculate→approve→process flow (`training/review/CHARACTERIZATION_PAYROLL.md` + `training/harness/`); dead-schema triage (about half the Prisma schema has no code; the evidence is `fable/03-scope-and-quality.md:10`, not `fable/02`); plan for the `fable/02-bugs-and-security.md` punch list.
- **HNJOBTRACK:** INC-003, snake_case→camelCase model drift wipes exclusions after a backend-only deploy (an API-contract break across the stack boundary).
- **reviewboard:** 10 of 25 generated security stories were already handled (tally line `elirc/gravreviewboardjspy: reviewboard/training/navigation/SECURITY-STORY-BANK.md:9`: 14 REAL · 10 ALREADY-HANDLED · 1 UNCLEAR). Verify the ticket before you build it.

## Worked trace: one dropped `requireRole` in the VGdemo port

The repo holds both sides. The TypeScript original is still there, every line commented out under a `// MIGRATION_NOTE` header; the .NET minimal API lives in `globalhire-lite/migrated-dotnet/`. (Paths below are under `elirc/vgdemo: globalhire-lite/`.)

**The old route** (`apps/api/src/modules/payroll/payroll.routes.ts:56-58`, commented out):

- `:56` calculate: `requireRole(['CLIENT_ADMIN', 'EOR_SPECIALIST', 'PLATFORM_ADMIN'])`
- `:57` approve: `requireRole(['EOR_SPECIALIST', 'PLATFORM_ADMIN'])`
- `:58` lock: `requireRole(['EOR_SPECIALIST', 'PLATFORM_ADMIN'])`

That is a **separation-of-duties** rule: the client may calculate its own payroll, but only the employer-of-record side may approve or lock it. It lives in middleware, so the service function never mentions it.

**The new route** (`migrated-dotnet/src/GlobalHireLite.Api/Program.cs:279-285`): it calls `CurrentUser`, returns 401 when that is null, and calls `payroll.Approve(actor, id)`. No role check.

**The new service** (`migrated-dotnet/src/GlobalHireLite.Api/Services/PayrollService.cs:82-94`): checks the run exists, `authorization.CanAccessOrganization(actor, run.OrganizationId)`, `Status == CALCULATED` and `GrossTotal > 0`. `CanAccessOrganization` (`Services/AuthorizationService.cs:7-11`) returns true for PLATFORM_ADMIN, EOR_SPECIALIST, **or anyone whose `OrganizationId` matches**. A CLIENT_ADMIN of that org passes.

Each piece looks reasonable alone. The porter translated the *service* faithfully (the TS `approvePayrollRun` at `apps/api/src/modules/payroll/payroll.service.ts:128-145` also has only the org, status and zero-total checks) and missed that the rule lived one layer up, in the router. That is the "shape kept, invariant dropped" pattern this page is named for.

**How identity reaches that check** (`Program.cs:420-428`, `CurrentUser`): read cookie `globalhire_user_id`; if absent, take whatever follows `Bearer ` in the Authorization header; look up the user **by that id**. Login (`Program.cs:34-49`) sets the cookie to `user.Id` and returns `token = user.Id` (`:48`). So the "token" is the user id, unsigned. Anyone who knows or guesses an id is that user. Add `Domain/Entities.cs:7` (`Password ... = "password123"` as the entity default, compared in plaintext at `Program.cs:37`) and the port has no real authentication at all.

**How the contract catches it** (`training/review/port-parity/contract.mjs:193-198`): C16 calls approve with the client-admin token and expects 403; C17 then approves as platform admin. The recorded .NET run (`training/_answers/port-parity-runs/parity-dotnet.txt`) shows `DIVERGE C16 ... TS contract: 403 | dotnet: 200`. The same file shows C07 (onboarding approve, `Program.cs:141-153` only blocks `Role.WORKER` and never checks the org) diverging the same way.

## Failure mode, step by step

1. Someone ports the service layer function by function. Every function has a twin; the reviewer sees parity.
2. The router layer is rewritten as minimal-API lambdas. Only "is there a user?" survives, because that is the one check the porter saw in every handler.
3. The 10 xUnit tests (green at B07, 2026-09-24) call the services directly: `tests/GlobalHireLite.Api.Tests/PayrollServiceTests.cs` has 6 `[Fact]`s, each acting as `"user-admin"` (e.g. `:15`, `:83`), and `WorkerServiceTests.cs` has 4. Nothing calls the HTTP endpoint as the wrong role, so nothing fails.
4. The README (`migrated-dotnet/README.md`) says the API "mirrors the original Express routes". The batch report records that it also admits the SDK was not available when the files were written: the port was never compiled by its author.
5. In production, a client admin approves and locks their own payroll. The invoice step (`Program.cs:305-314`) accepts APPROVED or LOCKED runs and returns an existing invoice unchanged if one exists, so money moves on a run nobody independent reviewed.
6. Nobody notices until an audit asks "who approved this?" and the audit log answers with the client's own user id (`PayrollService.cs:90,92`).

The parity contract is cheap insurance against steps 1-3: it doesn't care which layer held the rule, only what the HTTP answer is.

## Goal + Check ladder

**Goal:** given a port and its original, prove which rules survived, using evidence rather than reading and trusting.

1. **Junior: find the rule in the old code.** Open `payroll.routes.ts` in `elirc/vgdemo` and list every `requireRole` on the payroll router.
   **Check:** you list 6 role arrays (the routes file mentions `requireRole` at lines 20, 36, 50, 56, 57, 58), and you can say that approve and lock exclude CLIENT_ADMIN while calculate allows it.
2. **Junior+: find where it went.** For approve, follow route → service → authorization in the .NET code.
   **Check:** you cite `Program.cs:279-285`, `PayrollService.cs:82-94` and `AuthorizationService.cs:7-11`, and you can explain why a CLIENT_ADMIN of the same org gets through.
3. **Mid-: classify every divergence.** Read `training/_answers/port-parity-runs/parity-ts.txt` and `parity-dotnet.txt` side by side (no running needed).
   **Check:** TS diverges on C03, C04, C08 (all 500 instead of 400: an *oracle defect*, two zod copies defeat `instanceof ZodError` in `apps/api/src/middleware/error.middleware.ts`); .NET diverges on C03, C04, C07, C09, C11, C12, C16 (7 lines) with 2 ROUTE-DRIFT lines (POST→PATCH). You put C08 in "port is right" and C11/C12 in "error mapping" (`Program.cs:453` defaults `Error()` to 400).
4. **Mid: write the test that would have failed.** Sketch an xUnit `[Theory]` that calls approve once per role and asserts the forbidden ones. Compare with `training/_answers/regtests/PayrollRecalculationGuardTests.cs` (the incident's version of the same idea: one case per forbidden state).
   **Check:** your test fails on `elirc/vgdemo` `main` today for CLIENT_ADMIN. *Run locally* only if you have a .NET SDK: the batch report records the projects target net8.0 and were run with `DOTNET_ROLL_FORWARD=Major`.
5. **Mid+: make parity a gate.** Write down what a `KNOWN_DRIFT` allow-list would contain for this port (the two route drifts are candidates; C16 is not).
   **Check:** every entry has a reason and an owner, and no entry is a security rule. Compare with `training/_answers/port-parity.md` (its closing section proposes exactly this).

## Senior findings (verified at the HEADs above)

- **Allow-list guards turn into deny-lists during "small" changes.** On `main`, `PayrollService.Calculate` allows exactly one source state (`PayrollService.cs:37`, `run.Status != PayrollRunStatus.DRAFT` returns an error). INC-001 (`training/incidents/001-locked-payroll-reopened.md`, sealed answer `training/_answers/incident-001.md`) flips it to "block only APPROVED", which silently re-opens LOCKED runs. The sealed answer's diagnostic starts from the audit log: a `PAYROLL_CALCULATED` row after `PAYROLL_APPROVED` is an impossible transition, so the bug is in the guard, not the data. vg has the same smell with no guard at all: `approvePayrollRun` (`elirc/vg: src/services/payroll.service.js:525-545`) looks up the run, resolves the org and writes `status: "APPROVED"` with no status check (the fable review's "approve a DRAFT payroll run").
- **A rewrite can fix the code and keep the infrastructure assumption.** In `elirc/grok-build-multitenant`, the starter's `backend/src/middleware/tenantContext.ts` at `41a9785` (line 18) trusted `x-org-id` with a silent `'demo-org'` default. At HEAD `e899e20` the same file requires a signed-in user (`:18`), validates the header (`:19`) and checks `organizationMember` (`:25-34`). Real progress. But `docker-compose.yml:5` still sets `POSTGRES_USER: tenant_dev` and `backend/.env.example:2` connects as that same user, which the official Postgres image creates as a superuser. Any RLS added later would be bypassed ([19](19-rls-defense-in-depth.md)). The B06 report lists this as "missed by the rewrite"; it is still true on GitHub.

## Debugging scenario: "the port works, but the client admin can approve payroll"

A support ticket says a customer's HR admin approved their own payroll. The .NET tests are green. Work it like this:

1. **Reproduce at the HTTP edge, not in the service.** Run the contract against the .NET API (the drill's Part A commands are in `training/review/port-parity/EXERCISE.md`). C16 shows 200. If you can't run it, the recorded `parity-dotnet.txt` already shows it.
2. **Ask "which layer owned this rule in the original?"** Grep the commented TS: `grep -n requireRole globalhire-lite/apps/api/src/modules/payroll/payroll.routes.ts`. The answer is the router (`:57`), not the service. That is why a function-by-function review of the services found nothing.
3. **Check the identity you're trusting.** While you are in `Program.cs`, read `CurrentUser` (`:420-428`). A role check on an unsigned user-id token is a lock on a door with no wall: fix the token as well, or the role gate is decorative. The batch report marks this bypass as static-only (not live-verified), so say so in your write-up.
4. **Fix with a failing test first:** an endpoint-level test per role for approve and lock, then one role check in the handler or an ASP.NET authorization policy.
5. **Sweep for siblings.** The same omission appears on onboarding approve (C07, `Program.cs:145` blocks only WORKER) and on timesheet/leave review (workers can self-approve, per the B07 report). One dropped middleware rarely drops alone.

## Honesty notes

- All file:line citations above were opened at the HEADs listed on 2026-10-06. The parity numbers (17/20, 13/20, 11/20 on the INC-001 branch) are B07's **recorded** 2026-09-24 runs; they were not re-run for this page.
- The INC-001/INC-002 branches (`7955c9f`, `23e02c7` at B07), vg's incident branches, HNJOBTRACK's `775891c` branch and grok's `training/base/working-tree-snapshot` are **not on GitHub**. You can read the briefs and answers, but "check out the branch" steps only work on the original machine.
- vg's characterization reference suite was never confirmed green end to end (the B07 run hit Prisma `Transaction not found`, then Docker hung). Treat its expected totals as hand-derived.
- reviewboard's verdicts are static reading only; anything inside djblets is marked UNVERIFIED in its own bank.
