# 22 — SQL Server for Postgres developers (with EF Core)

Most of your practice is Postgres. .NET shops usually run SQL Server or Azure SQL. These are the differences that actually bite.

| Topic | Postgres habit | SQL Server reality | Worked example |
|---|---|---|---|
| **Collation** | case-sensitive by default | usually **case-insensitive** (`SQL_Latin1_General_CP1_CI_AS`), so `ABC` = `abc` in unique indexes | meterforge INC-004: a collation change merges distinct external ids, and 3% of events go unbilled |
| **String types** | `text` | `varchar` vs **`nvarchar`**. Comparing a `varchar` column with an `nvarchar` parameter causes an **implicit conversion**, which turns an index seek into a scan | meterforge INC-003: raw SQL sends `nvarchar` where EF sends `varchar`, and CPU climbs daily |
| **Money precision** | `numeric(p,s)` | `decimal(18,2)` is the EF default when unconfigured, and values are **silently truncated** | meterforge INC-005: 27.76 vs 27.77, off by exactly 0.01 on prorated invoices ([20](20-money-and-time.md)) |
| **Plans** | `EXPLAIN (ANALYZE, BUFFERS)` | actual execution plan + `SET STATISTICS IO, TIME ON`; Query Store for history | meterforge lab `training/lab/sqlserver/*.sql`; atlas `training/ladder/M1` |
| **Parameter sniffing** | generic plans after 5 executions | the plan is compiled for the **first** parameter values and cached. A skewed tenant makes it wrong for everyone else. Fixes: `OPTION (RECOMPILE)`, `OPTIMIZE FOR`, better indexes, plan forcing via Query Store | meterforge INC-001: usage page slow for small tenants after a failover (the tenant id becomes a `varchar(64)` parameter) |
| **Concurrency** | MVCC: readers never block writers | default READ COMMITTED **uses locks**, so readers and writers block, and deadlocks give **error 1205**. Enable **RCSI** (`READ_COMMITTED_SNAPSHOT ON`), keep lock order consistent, and retry 1205 | meterforge INC-002: batch ingest fails with 1205 every hour (the rollup job vs the writer) |
| **Indexes** | `INCLUDE`, partial indexes | `INCLUDE` covering indexes, **filtered** indexes (`WHERE …`); build with `ONLINE = ON` (Enterprise/Azure SQL) | meterforge ladder M2; atlas M1 |
| **Identity** | `serial` / `identity`, sequences | `IDENTITY` or `SEQUENCE`; watch gaps and reseeds | — |

**EF Core habits that matter on SQL Server:**
- `AsNoTracking` for reads;
- split queries for big includes;
- configure `HasPrecision` and `IsUnicode(false)` explicitly;
- read the SQL with `ToQueryString()`;
- check migrations with `dotnet ef migrations script`.

**Status:** meterforge's lab (`training/lab/sqlserver` branch) builds, and its DDL and parameter evidence come from real EF output. **Plans, deadlock graphs and timings are UNVERIFIED** until you run the container:
`docker run -d --name meterforge-training-mssql -e ACCEPT_EULA=Y -e "MSSQL_SA_PASSWORD=MeterForge#Lab2026" -e MSSQL_PID=Developer -e MSSQL_MEMORY_LIMIT_MB=2048 -p 14337:1433 mcr.microsoft.com/mssql/server:2022-latest`.
The checklist is in `training/lab/sqlserver/evidence/README.md`.
