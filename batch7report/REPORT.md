# Batch 07 Report: .NET legacy rescue, porting regressions, SQL Server

> **Status note (added 2026-10-06):** this report is a frozen record of the batch and was not updated afterwards. Not every `training/incidents/*` branch it describes is on GitHub: only 21 of the 92 from B01–B07 were pushed, and several projects now live under different elirc repo names. Before you try to check out an incident, see the incident-branch availability note at the top of [`apprenticeship/PROGRESS.md`](../apprenticeship/PROGRESS.md).

*2026-09-24 · I ran `apprenticeship/BATCH_PROMPT.md` on 5 projects covering the last thin skills: **SQL Server**, **.NET/EF Core depth**,
**legacy rescue** of untested AI-generated code, and **porting regressions**. Per-project detail is in `projects/<name>.md`.
Shared outputs: `apprenticeship/curriculum/20–22` (new), `COMPETENCY_GRAPH.md` (updated), `PROGRESS.md`.*

## ⚠ 1. Read first
- **This batch ran through the same disk-full outage as B06.** See `batch6report/REPORT.md` §1 for the cleanup and the Docker wipe.
- **Docker needs you.** After the data-disk wipe, Docker Desktop did not re-create its VM: `wsl -l -v` shows **no installed distributions**.
  Open Docker Desktop and use **Troubleshoot → Restart**, or **Reset to factory defaults**. Everything inside Docker was already wiped, so a reset loses nothing more.
- **Consequence: the SQL Server lab is built but was never run against a live engine.** No mssql container could start, and SQL Server LocalDB isn't installed.
  Everything that needs the engine is marked UNVERIFIED, with the exact command to run later:
  `docker run -d --name meterforge-training-mssql -e ACCEPT_EULA=Y -e "MSSQL_SA_PASSWORD=MeterForge#Lab2026" -e MSSQL_PID=Developer -e MSSQL_MEMORY_LIMIT_MB=2048 -p 14337:1433 mcr.microsoft.com/mssql/server:2022-latest`
  (checklist: `meterforge/training/lab/sqlserver/evidence/README.md`).

## 2. Tiers
| Project | What it is | Tier |
|---|---|---|
| **meterforge** | .NET 10 modular-monolith usage metering/billing on Postgres | **LAB**: a real SQL Server track (lab branch) |
| globehire | .NET 10 hiring/EOR API, in-memory | DRILL: DI lifetimes, time zones, EF-swap exercise |
| VGdemo | TS/Express/Prisma app plus a C# port | DRILL: port parity |
| vg | untested AI-generated Next.js JS EOR app | DRILL: legacy rescue |
| reviewboard | OSS Django + TS (Review Board) with 25 generated security stories | READ: verified security-story bank |

## 3. What was created
| Project | Commits | Contents | Incidents | Effort |
|---|---|---|---|---|
| meterforge | `567f53a`, `9f5023c`; lab branch `training/lab/sqlserver` (`d7a4fd6`: SQL Server data project on EF Core 10, migrations, 1M-row skewed seed harness, gated SQL Server tests) | 9 tickets (J1 run on SQL Server, J2 actual plans, J3 real-DB tests, M1 the PG→SQL Server port, M2 covering/filtered indexes + sniffing, M3 locking/RCSI/deadlocks, M4 EF translation, S1 Azure SQL migration with rollback, S2 100M rows) · review (25) · navigation · agentic · full interview kit · T-SQL scripts for plans, plan cache, blocking and deadlocks, and index usage | 5 | ~45 h |
| globehire | `36018f1` | review (23) · EF-swap exercise (characterization tests first) · mini kit | 2 | ~6.5 h |
| VGdemo | baseline `61367ad` (new git, plus a root `.gitignore`) + `1d5af1c` | review of the port (24) · **port-parity drill**: `contract.mjs` runs 20 HTTP checks against both TS and .NET, plus `restore-ts-oracle.mjs` · xUnit regression tests · mini kit | 2 | ~7 h |
| vg | baseline `99bb8b2` (new git) + `c74a7f0` | review (23; adds 7 findings beyond its own `fable/` review) · characterization-test ticket for payroll with a throwaway-DB harness · dead-schema triage · a PR-sized plan for the `fable/02` punch list · mini kit | 2 | ~9–10 h |
| reviewboard | baseline `bb3d688` (new git) + `415c038` | **SECURITY-STORY-BANK.md**: all 25 stories verified, 14 REAL / 10 ALREADY-HANDLED / 1 UNCLEAR, grouped by OWASP with file:line evidence · sealed placements for the top 8 · Django/TS seam note | — | ~6 h |

**Git notes**
- Every training commit touches only `training/` (checked). Nothing was pushed, and no worktrees are left.
- Your uncommitted work is untouched: meterforge 9 files, globehire 3.
- **vg:** its old `.git` held only a GitKraken config; that was moved into `.git_broken_backup/`, which now contains only it.
- **Repo-local git identities:** vg, VGdemo and reviewboard had none, so the agents set your name and email for each repo only.

**Incident symptoms** (causes sealed in `_answers/`)

*meterforge (SQL Server)*
1. The usage page is slow for small tenants after a failover.
2. Batch ingestion fails with error 1205 at the top of every hour.
3. Ingestion latency climbs day by day and database CPU is pinned.
4. A customer sent 3% more events than we bill.
5. Reconciliation is off by exactly 0.01 on prorated invoices.

*globehire*
1. After a deploy, cross-tenant approvals all show one person's name, a different one per pod.
2. US plans are accepted with yesterday's start date.

*VGdemo*
1. A LOCKED payroll run reopens with new totals.
2. An ACTIVE new hire is silently missing from a locked payroll.

*vg*
1. A payroll run shows COMPLETED but nobody is paid.
2. A 3-day plus a 2-day leave request leaves 32 pending days.

## 4. Verification
| Project | Verified | Not verified |
|---|---|---|
| meterforge | Lab and incident branches build; 42 tests pass. **Real EF output (no DB needed):**<br>• INC-001: the tenant id becomes a `varchar(64)` parameter<br>• INC-003: raw SQL sends `nvarchar` where EF sends `varchar`<br>• INC-004: the collation change rebuilds the unique index<br>• INC-005: EF warns values are "silently truncated" (27.76 vs 27.77)<br>• the covering index is generated `ONLINE = ON` | **everything needing a live engine:** plans, timings, deadlock graphs; the 4 SQL Server tests were skipped; the INC-002 deadlock is reasoned from code and documented locking |
| globehire | INC-002 branch passes the full `dotnet test` (it slips past CI, as designed); both incidents reproduced with throwaway tests; 3 review findings confirmed against the running API | startup scope validation for INC-001 (documented .NET behaviour, not run) |
| VGdemo | Existing 10 xUnit tests green. INC-001: 3 new tests fail on the branch and pass on main. INC-002: 2 fail as designed. **Live parity run:** TS 17/20 vs .NET 13/20, with INC-001 scoring 11/20 and reproducing live. | the token bypass and worker self-approval (read from code) |
| vg | Both mechanisms checked against the repo's own Prisma client: an un-awaited query never runs; `Decimal(3)+2` gives `"32"` | **the reference payroll test suite has never been seen passing** (Docker hung). Run it first (`training/harness/README.md`). |
| reviewboard | all 25 stories checked against the source | djblets isn't in the tree, so dependent claims are UNVERIFIED |

## 5. Real defects found (documented, NOT fixed)

**VGdemo's .NET port**
- The auth token is just the user id, so **anyone can log in as anyone**.
- Most role checks were dropped: a client admin can approve their own payroll.
- No validation (a negative salary is accepted); 403/404 come back as 400; nothing survives a restart.
- Its README admits it was never compiled when written.
- The TS original is broken too: `npm ci` fails (lockfile out of sync), and there are two copies of zod, so validation errors become 500s.

**vg**
- A future-dated raise stops pay.
- YTD totals count unapproved runs.
- The year boundary uses the server's time zone (live on this UTC-7 laptop).
- Leave accrual doesn't exist.
- "Encrypted bank details" refers to a column that doesn't exist.
- The domain-event worker never retries and just logs success.
- Every payroll write returns 500 after commit.
- Payroll reads the database inside a 5-second transaction ("Transaction not found" on this laptop).
- `auth.js:10` falls back to a public secret.
- A real `.env` exists (gitignored, not read).

**globehire**
- `FLAW-HARVEST.md` claims the approval race is fixed, but hire-case writes are still unlocked read-then-mutate.
- Sprint 6–13 features are stateless "validate" endpoints that save nothing.
- The employment-change endpoint takes `Today` from the request body.

**meterforge**
- `/health/ready` always says ready.
- The payments `Idempotency-Key` creates a new attempt on every call.
- The outbox table is never written.
- The CI vulnerability step can never fail.
- Usage ingestion ignores whether the add succeeded, so a concurrent duplicate gets a 201 with an id that was never stored.

**reviewboard (upstream)**
- The webhook Basic auth header is built from bytes (`Basic b'...'`, reproduced).
- Webhook URLs are logged with credentials.
- No SSRF guard; HMAC-SHA1 signatures.
- Possibly missing repository-access checks on 3 endpoints (UNVERIFIED).

## 6. Existing learning docs: verdicts
| Repo | Verdict |
|---|---|
| meterforge | `docs/sprints`, `docs/curriculum`, `docs/operations`, threat model, guides: KEEP (`INCIDENT-DRILL.md` is a later CONVERT candidate) · `FLAW-HARVEST.md`, `FLAW-LEDGER.local.md`: IGNORE (spoilers) · `astraupskill/`: KEEP |
| globehire | `docs/`, root guides, `astraupskill/`: KEEP · FLAW-LEDGER: IGNORE |
| VGdemo | `fable/`: gated spoiler (read after the review) |
| vg | `fable/`: CONVERT (now the punch-list exercise) · `docs/`: IGNORE |
| reviewboard | `User Stories/`: CONVERTED (the verified bank; don't follow the plans as written) · `docs/upskill/`: KEEP as an index (94 stale links; never mentions Django Evolution) · `Application Rewrite Plan/`: IGNORE as a plan, reuse as a system-design critique · `Junior/`, `25-Mixed`: IGNORE |

## 7. Curriculum and totals
- **New:** [20 Money and time](../apprenticeship/curriculum/20-money-and-time.md), [21 Legacy rescue and ports](../apprenticeship/curriculum/21-legacy-rescue-and-ports.md), [22 SQL Server for Postgres developers](../apprenticeship/curriculum/22-sqlserver-for-postgres-devs.md).
- **Backlog:** DI lifetimes and captive dependencies; SSRF-safe outbound HTTP; security audit logging vs notifications; Python async event-loop blocking.
- **Totals after B01–B07:**
  - 31 projects
  - 92 incident branches
  - 27 blind reviews
  - about 140 ladder tickets
  - 13 full + 14 mini interview kits
  - **22 curriculum pages**
- **Every thin skill from the original audit now has exercises.** The only gaps left need *doing*, not generating:
  a live SQL Server run (once Docker is fixed), a real cloud deploy, and a first upstream PR. **No further batch recommended.**

## 8. What to do first (about 1.5 weeks part-time)
1. **Fix Docker** (Troubleshoot → Restart or Reset). Then start the meterforge SQL Server container and run the `evidence/README.md` checklist.
   **That turns the SQL Server lab from built into verified.**
2. **meterforge J2 → INC-003 → INC-001:** read real execution plans, then find the implicit conversion and the parameter-sniffing regression (page 22).
3. **VGdemo parity drill:** run `contract.mjs` against both stacks and classify every difference, then do INC-001 (page 21).
4. **vg:** run the reference payroll characterization suite first, then INC-002 (Decimal concatenation) and INC-001 (the un-awaited query) (page 20).
5. **globehire INC-001:** a captive-dependency DI bug. A classic .NET interview question with a real repro.
6. **reviewboard SECURITY-STORY-BANK:** classify the stories yourself before opening the evidence. It's practice in verifying generated tickets.
