# 22 — SQL Server for Postgres developers (with EF Core)

Most of your practice is Postgres. .NET shops usually run SQL Server or Azure SQL. These are the differences that actually bite.

**Where these repos live now (2026-10-06):** meterforge → `elirc/meterforge` (`main` @ `8e702ad`; `training/` is on `main`, but the `training/lab/sqlserver` and `training/incidents/*` **branches are not on GitHub**, see Status); atlas → code in `elirc/atlas` (`main` @ `19e8c2d`, no `training/`), training pack in the monorepo `elirc/gitvg` under `atlas/training/` (@ `af91bab`).

| Topic | Postgres habit | SQL Server reality | Worked example |
|---|---|---|---|
| **Collation** | case-sensitive by default | usually **case-insensitive** (`SQL_Latin1_General_CP1_CI_AS`), so `ABC` = `abc` in unique indexes | meterforge INC-004: a collation change merges distinct external ids, and 3% of events go unbilled |
| **String types** | `text` | `varchar` vs **`nvarchar`**. Comparing a `varchar` column with an `nvarchar` parameter causes an **implicit conversion**, which turns an index seek into a scan | meterforge INC-003: raw SQL sends `nvarchar` where EF sends `varchar`, and CPU climbs daily |
| **Money precision** | `numeric(p,s)` | `decimal(18,2)` is the EF default when unconfigured, and values are **silently truncated** | meterforge INC-005: 27.76 vs 27.77, off by exactly 0.01 on prorated invoices ([20](20-money-and-time.md)) |
| **Plans** | `EXPLAIN (ANALYZE, BUFFERS)` | actual execution plan + `SET STATISTICS IO, TIME ON`; Query Store for history | meterforge lab `training/lab/sqlserver/sql/*.sql` (on `main`); atlas `training/ladder/M1` |
| **Parameter sniffing** | generic plans after 5 executions | the plan is compiled for the **first** parameter values and cached. A skewed tenant makes it wrong for everyone else. Fixes: `OPTION (RECOMPILE)`, `OPTIMIZE FOR`, better indexes, plan forcing via Query Store | meterforge INC-001: usage page slow for small tenants after a failover (the tenant id becomes a `varchar(64)` parameter) |
| **Concurrency** | MVCC: readers never block writers | default READ COMMITTED **uses locks**, so readers and writers block, and deadlocks give **error 1205**. Enable **RCSI** (`READ_COMMITTED_SNAPSHOT ON`), keep lock order consistent, and retry 1205 | meterforge INC-002: batch ingest fails with 1205 every hour (the rollup job vs the writer) |
| **Indexes** | `INCLUDE`, partial indexes | `INCLUDE` covering indexes, **filtered** indexes (`WHERE …`); build with `ONLINE = ON` (Enterprise/Azure SQL) | meterforge ladder M2; atlas M1 |
| **Identity** | `serial` / `identity`, sequences | `IDENTITY` or `SEQUENCE`; watch gaps and reseeds | meterforge `initial-sqlserver.sql:51` (`seq bigint IDENTITY`) |

**EF Core habits that matter on SQL Server:**
- `AsNoTracking` for reads;
- split queries for big includes;
- configure `HasPrecision` and `IsUnicode(false)` explicitly;
- read the SQL with `ToQueryString()`;
- check migrations with `dotnet ef migrations script`.

**Status:** At B07 (2026-09-24) meterforge's lab branch `training/lab/sqlserver` (`d7a4fd6`) built and its 42 tests passed, with the 4 SQL Server integration tests skipped (no server). Its DDL and parameter evidence come from real EF output and **are on `main`** in `training/lab/sqlserver/evidence/`. **Plans, deadlock graphs, timings and stored values are still UNVERIFIED**: `evidence/README.md` at `8e702ad` still says "Honest status (2026-09-24)" and records no live run. To run them you need a container:
`docker run -d --name meterforge-training-mssql -e ACCEPT_EULA=Y -e "MSSQL_SA_PASSWORD=MeterForge#Lab2026" -e MSSQL_PID=Developer -e MSSQL_MEMORY_LIMIT_MB=2048 -p 14337:1433 mcr.microsoft.com/mssql/server:2022-latest`.
The checklist is in `training/lab/sqlserver/evidence/README.md`.
**Correction (2026-10-06):** the lab and incident branches are **not on GitHub**. `git ls-remote` on `elirc/meterforge` lists only `main`, two tags and closed-PR refs, and `training/README.md` now says the same in its status note. The current local clone (`Desktop\claiufe\meterforge`) doesn't contain `d7a4fd6` either. So the SQL Server adapter code (`MeterForge.Infrastructure.SqlServer`, `tools/MeterForge.SqlLab`) can't be opened from a fresh clone today, and the lab and incident steps are **reading exercises** until those branches turn up and are pushed. `main` itself has no EF Core at all: `src/MeterForge.Infrastructure/MeterForge.Infrastructure.csproj:9` references only `Npgsql`.

## Worked trace: one string, three wire shapes (meterforge evidence on `main`)

Everything in this trace is real tool output (EF Core 10.0.12 `ToQueryString()` and `dotnet ef migrations script`, generated with no database) and is committed at `elirc/meterforge` `8e702ad`. You don't need the missing branches to read it.

1. **The column as designed.** `elirc/meterforge: training/lab/sqlserver/evidence/initial-sqlserver.sql:58` declares `[external_event_id] varchar(128) COLLATE Latin1_General_100_BIN2 NOT NULL`. That's a binary, case-sensitive collation, chosen on purpose so that `evt_7hQ2mZx1` and `evt_7Hq2mZX1` are different ids. In the same file, `:86` creates the dedupe key `ux_usage_events_tenant_external (tenant_id, external_event_id)`, and `:51` makes `seq bigint IDENTITY` the clustered key.
2. **The EF LINQ lookup.** `dedupe-lookup-sql.txt:5-6`: EF sends `@tenantId varchar(64)` and `@externalEventId varchar(128)`. EF types the parameter **from the column mapping**: non-Unicode with a max length gives `varchar(n)`. That is what `IsUnicode(false)` + `HasMaxLength` buy you. Same type on both sides means the seek works.
3. **The raw-SQL lookup (INC-003 shape).** `dedupe-lookup-sql.txt:16-17`: `@tenant nvarchar(11) = N'tenant-0042'`. The probe that produced it (`probe-dedupe.cs.txt:13-14`) passes `new SqlParameter("@tenant", tenantId)` with no type, and `:26` shows SqlClient inferred `SqlDbType: NVarChar`. The `11` is just `"tenant-0042".Length`, so every distinct length is also a separate cached plan.
4. **The collation change (INC-004 shape).** `inc-004-migration.sql:2` drops the unique index, `:9` runs `ALTER COLUMN [external_event_id] varchar(128) NOT NULL` with **no `COLLATE`** (so it falls back to the database default), and `:10` recreates the unique index. The migration id at `:13` is `UseDatabaseDefaultCollation`. It sounds harmless, but it isn't.
5. **The sniffing setup (INC-001 shape).** `usage-summary-sql.txt:12` shows the lab query inlining `'tenant-0001'` as a literal (`EF.Constant`), which gives one plan per tenant. `:17` and `:25` show the incident version sending `@_8__locals1_tenant varchar(64)`, which gives one shared plan, compiled for whoever runs first.

Concept tie-in: in Postgres, all of these are `text` with one collation, and a type mismatch usually errors out loudly. On SQL Server, each one is a **silent** change in either cost (steps 3 and 5) or meaning (step 4).

## Failure mode, step by step: INC-004 "3% unbilled"

From `training/_answers/incidents/004-usage-undercount.md` (the sealed answer; the live REPLAY output is UNVERIFIED):
1. The migration in step 4 changes `external_event_id` from `Latin1_General_100_BIN2` to the database default `SQL_Latin1_General_CP1_CI_AS`, which is case-insensitive.
2. It **succeeds**, because no two *existing* rows collide case-insensitively at that moment. Had they, `CREATE UNIQUE INDEX` would have failed, which would have been the better outcome.
3. A new event `evt_7Hq2mZX1` arrives. The dedupe lookup matches the stored `evt_7hQ2mZx1`.
4. The ingestion service treats the new event as a **replay** and returns `200 isReplay: true`. Nothing is stored and nothing errors.
5. The customer's ids are 8 random base62 characters, so case-only collisions grow with volume. Billing undercounts, and the only signal is the replay rate jumping on the migration date.

The fix is to set the collation explicitly in the model (`UseCollation("Latin1_General_100_BIN2")`), plus a test that inserts two ids differing only by case and expects two rows.

## Goal + Check ladder

**Goal:** be able to say, from generated SQL alone, whether a SQL Server query will seek, sniff, truncate or silently merge, before anyone runs it.

1. **Junior: collation.** Open `initial-sqlserver.sql:58` and `inc-004-migration.sql:9` in `elirc/meterforge`.
   **Check:** the first line has `COLLATE Latin1_General_100_BIN2` and the second has no `COLLATE` clause. Explain in one sentence which default the second one falls back to.
2. **Junior: parameter types.** Compare `dedupe-lookup-sql.txt:5-6` with `:16-17`.
   **Check:** you can name both types (`varchar(64)` vs `nvarchar(11)`), say which side SQL Server converts (the **column**, because `nvarchar` has higher type precedence; `_answers/incidents/003-ingest-cpu-climb.md` explains why), and say why the length is 11.
3. **Mid: money precision.** Read `decimal-mapping.txt:4-11` and `inc-005-migration.sql:6`.
   **Check:** you predict `27.76` stored for `49 × 17 / 30` under truncation vs `27.77` under rounding, and you quote EF's own warning text ("silently truncated"). Then run `grep -rn "HasPrecision" src/Atlas.Infrastructure/Persistence/Configurations` in `elirc/atlas`: at `19e8c2d` you'll find hits in 7 files, and `grep -rn "ConfigureConventions\|HavePrecision"` finds **nothing**. So atlas gets precision right one property at a time, and nothing would catch the next decimal property someone adds without it.
4. **Mid: plan stability.** Read `usage-summary-sql.txt:12` vs `:25` and `_answers/incidents/001-usage-summary-latency.md`.
   **Check:** you list three fixes with their costs (a covering index, `EF.Constant` for one plan per tenant, `OPTION (RECOMPILE)` at ~1–5 ms of compile per call, `OPTIMIZE FOR UNKNOWN` for an average plan). You can also say why compat level 160's Parameter Sensitive Plan optimization can **mask** the incident (the lab pins 150).
5. **Senior (run locally; needs Docker plus the lab branch, which is not public today).** Follow `evidence/README.md`'s table.
   **Check:** the expected outcomes written there: INC-003's `nvarchar` query shows an Index Scan with `CONVERT_IMPLICIT` and thousands of reads, against < 10 reads for `varchar`; INC-004 prints `REPLAY` (`CREATED` on the lab branch); INC-005 prints `27.76`. Any number you get replaces the reference's "UNVERIFIED".

## Verified senior findings (at current HEADs)

- **meterforge readiness still lies** (`elirc/meterforge: src/MeterForge.Api/Program.cs:56-62` @ `8e702ad`): `/health/ready` returns `postgresAdapterAvailable = true` (`:60`), but the registrations at `:31-39` wire only in-memory stores, including `IUsageEventStore` → `InMemoryUsageEventStore`. B07 reported this at `43ee18d` (then lines 47–53), and it's still true. When you add a SQL Server adapter, readiness must actually open a connection, or a failover looks "ready" while every write fails.
- **The in-memory store can't teach you collation** (`src/MeterForge.Infrastructure/Usage/InMemoryUsageEventStore.cs:9,20`): the key is a C# tuple `(TenantId, ExternalEventId)` compared **ordinally** (case-sensitive), after `UsageEvent.cs:20` trims the id. Since commit `4e3f344` (2026-09-30), `main` dedupes atomically with `GetOrAdd`, and `UsageIngestionService.cs:23-30` returns 409-style `usage.idempotency_conflict` on a changed payload. B07's "`TryAdd` result ignored / phantom id / trim mismatch" bugs describe `43ee18d`, not today's `main`. But the semantics now live in C#, so the in-memory tests stay green under any SQL collation. Only a **parity test run against both stores** (the same "two ids differing only by case" input) would catch INC-004. This is an inference from the code, not an observed failure.
- **atlas has no SQL Server provider yet** (`elirc/atlas: src/Atlas.Infrastructure/DependencyInjection.cs:30-36` @ `19e8c2d`): the provider switch accepts only `postgres` and `sqlite` and throws otherwise. So `elirc/gitvg: atlas/training/ladder/M1-cost-report-at-1m-payslips.md` asks for SQL Server DDL **on paper**. Its query still folds decimal sums in C# because SQLite stores decimal as TEXT (`ReportQueries.cs:79`), and `payslips` has only a `RunId` index (`PayrollConfigurations.cs:110`).

## Debugging scenario: "p95 climbs a little every day, CPU 96%" (INC-003)

The brief (`training/incidents/003-ingest-cpu-climb.md`) gives a **narrative** Query Store table. It was written for the exercise, not measured: the dedupe lookup at 61.4 ms average CPU and 41,880 average logical reads, against 0.2 ms and 6 reads the week before. The suspect PR replaced the LINQ lookup with `FromSqlRaw … WITH (UPDLOCK)`.
1. **Rule out locks.** Sessions are `RUNNABLE`/`SOS_SCHEDULER_YIELD`, not waiting on locks, so this is CPU, not blocking. That separates it from INC-002.
2. **Reads per execution ≈ an index scan.** Growth tracks table size, which is a scan signature. A wrong plan would jump, not creep.
3. **Look at parameter types** in the plan's `ParameterList`: `@tenant nvarchar(11)`. That matches `dedupe-lookup-sql.txt:16`.
4. **Find `CONVERT_IMPLICIT`** on the column in the predicate, plus the plan warning about the seek plan.
5. **Fix:** revert to LINQ (EF types it `varchar` from the mapping) or type the parameter explicitly (`SqlDbType.VarChar, 64`).
6. **Bonus finding from the answer key:** a standalone `SELECT … WITH (UPDLOCK)` releases its lock when its implicit transaction commits, and without `HOLDLOCK` it takes no key-range lock. So the PR added cost and **no** protection. The unique index was always the real guard.

**Honesty cap:** every meterforge plan, read count, deadlock graph and stored value on this page is either brief narrative or "expected" from documented SQL Server behaviour. No SQL Server has run this code (B07 report, `evidence/README.md` @ `8e702ad`). `decimal-mapping.txt:8-10` also shows that SqlClient has both a truncating path (`AdjustScale` with `fRound:false` gives `27.76`) and a rounding path (`ConvertToPrecScale` gives `27.77`). Which one actually happens on the wire is exactly what INC-005's live run has to show.
