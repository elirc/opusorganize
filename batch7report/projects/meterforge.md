# B07 — MeterForge (LAB tier, focus: real SQL Server + EF Core depth)

Repo: `C:\Users\Owner\Desktop\meterforge` (own `.git`, remote github.com/elirc/meterforge — **not pushed**). `main` HEAD before work: `43ee18d`.
The 9 uncommitted user files (7 modified in the Usage/Api/Errors area + untracked `astraupskill/` and `tests/MeterForge.Api.Tests/Usage/`) were not touched; commits used `git commit ... -- training` only.

## What I created
**On `main` (pathspec commits `567f53a`, `9f5023c`, "training: add B07 apprenticeship materials"):** `training/`
- `README.md`: index, branch table, suggested order, about 30–36 h
- `lab/sqlserver/`: `README.md` (setup), `start-sqlserver.ps1` / `stop-sqlserver.ps1` (mssql 2022 on port 14337, throwaway SA password, compat 150), `sql/01-usage-summary-plan.sql` (STATISTICS IO/TIME + actual plan XML), `02-plan-cache.sql`, `03-blocking-and-deadlocks.sql` (blocking chain + `system_health` deadlock graphs + RCSI), `04-index-usage.sql`; `evidence/` (offline-generated DDL, EF SQL, parameter types, decimal probe, and an UNVERIFIED checklist with exact commands)
- `ladder/`: J1 run on SQL Server · J2 read an actual plan · J3 real-DB integration tests · M1 Postgres→SQL Server port review (collation, trailing spaces, datetimeoffset, decimal, identity vs sequence, JSON, filtered vs partial, upsert) · M2 covering INCLUDE + filtered index + parameter sniffing · M3 RCSI vs locking, blocking, deadlock graphs · M4 EF translation (split queries, AsNoTracking, compiled queries) · S1 Azure SQL zero-downtime migration + rollback · S2 100M-row stats/index maintenance/partitioning
- `incidents/001..005` briefs (symptoms only) · `review/EXERCISE.md` + `COMPARE.md` · `navigation/` (ARCHITECTURE, FIRST_CHANGE, TRADEOFFS ×5, CHANGE_REQUEST usage caps) · `agentic/WORKFLOW.md` (M2 via implementer + adversarial reviewer) · `interview/` (5 STAR, 20 questions, system design, mock defense, 25 flashcards)
- `_answers/`: J1–J3, M1–M4, S1–S2, review (25 findings), tradeoffs, change-request, agentic-rubric, `incidents/001..005`

**Branches (all local, based as noted):**
| Branch | Commit | Base | Content / symptom |
|---|---|---|---|
| `training/lab/sqlserver` | `d7a4fd6` | `43ee18d` | New `MeterForge.Infrastructure.SqlServer` (EF Core SqlServer 10.0.12, `InitialSqlServer` migration, usage store, read model, claim-then-MERGE rollup job, invoice snapshot store), opt-in API wiring (`ConnectionStrings:MeterForgeSqlServer`) + `GET /usage-summary`, `tools/MeterForge.SqlLab` harness (migrate/seed ~1M skewed rows/summary/bench-sniff/rollup/ingest/soak), env-gated `tests/MeterForge.SqlServer.Tests`, local `dotnet-tools.json` (dotnet-ef) |
| `training/incidents/001-usage-summary-latency` | `40bc092` | lab | Usage page slow for small tenants after a failover; whale fine |
| `training/incidents/002-batch-ingest-1205` | `2e8ee19` | lab | Batch ingestion fails with SQL error 1205 at the top of each hour |
| `training/incidents/003-ingest-cpu-climb` | `8f73bc2` | lab | Ingestion p95 climbs daily with table size, DB CPU pinned |
| `training/incidents/004-usage-undercount` | `2ae9c0e` | lab | Customer's sent-event count 3% above what we bill; replay rate jumped |
| `training/incidents/005-proration-reconciliation-drift` | `9fe78a5` | lab | Reconciliation mismatches of exactly 0.01 on prorated invoices |

Incident branches are based on the lab branch, not on `main` HEAD, because the SQL Server code exists only there (the brief forbids the EF SQL Server provider on main). All worktrees were removed.

## Verification
- **Built:** lab branch full solution (`dotnet build MeterForge.slnx`: 0 warnings, 0 errors with TreatWarningsAsErrors); `tools/MeterForge.SqlLab` on every incident branch; `MeterForge.Api` on inc-002.
- **Tests:** lab branch `dotnet test`: Domain 26, Application 9, Api 6, Architecture 1 = **42 passed**; SqlServer.Tests **4 skipped** (no server).
- **Offline-verified with real tool output** (in `training/lab/sqlserver/evidence/`): migration DDL (`dotnet ef migrations script`); INC-001 wire change (`'tenant-0001'` literal → `@_8__locals1_tenant varchar(64)`); INC-003 parameter types (EF `varchar(64)/(128)` vs `FromSqlRaw` `nvarchar(11)/(12)`); INC-004 migration drops/recreates the unique index and `ALTER COLUMN` without COLLATE; INC-005 `decimal(18,2)` + EF's own `DecimalTypeDefaultWarning` ("silently truncated") + `SqlDecimal.AdjustScale` truncation 27.76 vs round 27.77; M2 covering index DDL `... INCLUDE (...) WITH (ONLINE = ON)` generated exactly.
- **UNVERIFIED (needs a live SQL Server):** everything run against the engine: `start-sqlserver.ps1`, `SqlLab migrate/seed`, J1 HTTP flow, the 4 integration tests, all plans/reads/timings (J2, M2, INC-001, INC-003), blocking/deadlock capture (M3, INC-002; the deadlock is derived from code + documented locking and **may not reproduce as described**), INC-004 REPLAY and INC-005 stored 27.76, and the M1 T-SQL proofs. Every such spot is labelled UNVERIFIED in the answers, with the exact command (`evidence/README.md`):
  `docker run -d --name meterforge-training-mssql -e ACCEPT_EULA=Y -e "MSSQL_SA_PASSWORD=MeterForge#Lab2026" -e MSSQL_PID=Developer -e MSSQL_MEMORY_LIMIT_MB=2048 -p 14337:1433 mcr.microsoft.com/mssql/server:2022-latest`
- **Why:** `docker pull` of mssql hung at the 502 MB layer (it had fetched the image by hand from MCR and was running `docker load` when the C: drive filled up); then Docker's engine/WSL distro broke after the orchestrator's reset. No LocalDB on the machine. No container was ever created; the scratch image tarball was deleted.
- `dotnet format --verify-no-changes` reports ENDOFLINE on **every** file in the worktree (a CRLF checkout artifact, pre-existing files included), so formatting wasn't a meaningful check here.

## Issues found in the project (on `main`)
- **Presented as working but isn't:** `/health/ready` always returns ready with `postgresAdapterAvailable = true`, but the Npgsql adapter is never registered (`Program.cs:27-30,47-53`); "Outbox and webhooks" is a table + model with no writer or publisher; `entitlements/check` and `reconciliation/payments` evaluate caller-supplied numbers; the payments `Idempotency-Key` is required but a new attempt is created on every call; the CI `dotnet list package --vulnerable` step can't fail.
- **Real bugs:** ingestion find-then-add with `TryAdd` result ignored (a concurrent duplicate gets 201 + a phantom id); the domain trims `ExternalEventId` but the lookup uses the raw value (`" evt_1"` → 201 phantom); replay with a different payload is accepted silently; failed payments return 200 with `providerReference: null`. The user's uncommitted changes touch exactly this ingestion area, so they may be fixing some of these already.
- **Secrets:** none, apart from local-only placeholders: `docker-compose.yml` (Postgres password) and the lab's throwaway SA password in `training/lab/sqlserver/start-sqlserver.ps1` and `SqlServerRegistration.cs`/SqlLab defaults on the lab branch. `.gitignore` excludes `.env` and `secrets.json`. `FLAW-LEDGER.local.md` is gitignored (a spoiler); I didn't read or reuse it.

## Skill links (for COMPETENCY_GRAPH)
- **SQL Server (real):** `training/lab/sqlserver/*` → J1, J2, M1, M2, M3, S1, S2 → INC-001/002/003/004/005 → TECHNICAL_QUESTIONS 5–13, FLASHCARDS 1–25
- **SQL: plans, indexes, sniffing:** ladder/J2, M2 → INC-001 (sniffing), INC-003 (implicit conversion) → questions 6–8
- **Transactions / locking / deadlocks:** ladder/M3 → INC-002 → questions 11–12, 19 (concurrency is saturated; this is SQL Server lock mechanics, not races)
- **.NET / EF Core depth:** ladder/M4, J3, `agentic/WORKFLOW.md` → INC-003 (FromSqlRaw), INC-005 (decimal mapping) → questions 8, 13–14
- **Code migration / porting regressions:** ladder/M1, S1 → INC-004 (collation), INC-005 (money scale)
- **Zero-downtime migrations / cloud:** ladder/S1 (Azure SQL), S2 (partitioning, online index)
- **Money correctness:** INC-005, `navigation/TRADEOFFS.md` T3
- **Code review:** `review/EXERCISE.md` → `_answers/review.md` (25 findings, 9 AI-smell)
- **Unfamiliar codebase:** `navigation/*`
- **Agentic engineering:** `agentic/WORKFLOW.md` + `_answers/agentic-rubric.md`
- **Design/trade-offs:** `navigation/TRADEOFFS.md` (5), `CHANGE_REQUEST.md`, `interview/SYSTEM_DESIGN.md`

## Curriculum needs (one central page each; not written)
1. **SQL Server for Postgres developers**: collation/case sensitivity, trailing spaces, `datetimeoffset` vs `timestamptz`, identity vs sequence, JSON, filtered vs partial indexes, upsert equivalents. Two-line scope: the port checklist, and which differences change data silently.
2. **Parameter sniffing & plan stability**: compile-once-reuse, skew, the fixes (covering index, RECOMPILE, OPTIMIZE FOR, literal inlining/EF.Constant, PSPO at compat 160, Query Store forcing) and their costs.
3. **SQL Server locking, RCSI and deadlock graphs**: lock modes, escalation, HOLDLOCK/UPDLOCK/READPAST, how to read `xml_deadlock_report`, what RCSI does and doesn't fix.
4. **Money precision across layers**: domain rounding vs DB scale vs driver truncation vs EF defaults (already in the curriculum backlog as "Money: rounding vs truncation"; now needed by 2+ projects).
5. **Implicit conversions & typed parameters**: nvarchar vs varchar, CONVERT_IMPLICIT, SQL vs Windows collations, typing SqlParameter/Dapper/FromSql.

## Existing learning-doc trees
- `astraupskill/` (untracked, user's own, 7 files + VERIFICATION): **KEEP** (in-memory domain + ingestion walkthrough; complementary; not in git, not touched).
- `docs/sprints/` (15 sprint notes), `docs/curriculum/` (SPEC, RETROSPECTIVE): **KEEP** as course history/reference.
- `docs/quality/FLAW-HARVEST.md`, `FLAW-LEDGER.local.md`: **IGNORE** for new exercises (spoilers for the course's planted flaws).
- `docs/operations/` (RUNBOOK, INCIDENT-DRILL, RELEASE-CHECKLIST), `docs/security/THREAT-MODEL.md`: **KEEP** (INCIDENT-DRILL could be **CONVERTED** into an exercise later).
- `LEARNER-GUIDE.md`, `TESTREADME.md`, `OEReadMe.md`: **KEEP** (short; the over-engineering review is a good read).

## Honest caveats
- The core promise of the batch ("actually run them against the container and capture plans/deadlock graphs") was **not** met: 0 live runs, for environment reasons (see Verification). The track is built so the user can run it, and each answer says what to expect and to trust their own output over it. INC-002 in particular is reasoned, not observed: the soak harness may need tuning (writers, batch size, replay %) to trigger the deadlock.
- `start-sqlserver.ps1` has never been executed.
- The lab code is mine (not the course author's), so the review's "lab pass" findings 21–25 critique my own deliberate simplifications. That's intended as teaching material, and the report flags it.
- `/health/ready` on the lab branch still says `durableDefault = false` (stale on that branch; mentioned in J1's answer as a finding).
- Nothing pushed. The remote exists; branches are local only.
