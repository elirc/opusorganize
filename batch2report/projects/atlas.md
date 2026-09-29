# atlas (gitvg/atlas) — B02 report

**Tier:** LAB (Phases 2–5) · **Repo:** `C:\Users\Owner\Desktop\gitvg\atlas` (remote elirc/atlas, **not pushed**)
· **Base:** `main` @ 4df694c (v1.0.0) · **Training commit:** `e85c35a` (46 files, `training/` only, pathspec commit)

## What was created
`training/` (index + order + time estimate ≈ 32–40 h in `training/README.md`):
- `review/EXERCISE.md`, `review/COMPARE.md` → sealed `_answers/review.md` (23 findings, AI-smells flagged, ledger flaws excluded)
- `ladder/` J1 filter-runs-by-state · J2 unpaid-leave-in-payroll · M1 cost report at 1.3M payslips (Postgres + SQL Server plans, covering/online index) · M2 prepare at 25k workers (N+1, batching, race) · M3 payslip v3 + v2 deprecation + v1 410 + golden contract tests · M4 truthful request metrics + payroll-run signals · S1 Azure Container Apps + Azure SQL with rollback · S2 payroll prepare as a durable chunked job. Each has a sealed answer or rubric in `_answers/`.
- `incidents/001..005-*.md` (symptoms, logs, metrics, suspect PR; no cause) → `_answers/INC-001..005.md`
- `navigation/ARCHITECTURE.md` (3 flows traced file by file), `ONBOARDING.md`, `TRADEOFFS.md` (4 "Why?" drills → `_answers/tradeoffs.md`), `CHANGE_REQUEST.md` (off-cycle bonus → `_answers/change-request.md`)
- `agentic/WORKFLOW.md` (M2 via implementer + adversarial reviewer), `VERIFY_AI_OUTPUT.md` → `_answers/agentic.md`
- `interview/` PROJECT_STORIES (5), TECHNICAL_QUESTIONS (20 → `_answers/technical-questions.md`), SYSTEM_DESIGN (→ `_answers/system-design.md`), MOCK_DEFENSE, FLASHCARDS (24)

## Incident branches (local only, based on HEAD 4df694c)
| Branch | Commit | Symptom (not cause) |
|---|---|---|
| `training/incidents/001-payslip-history-latency` | 0289689 | New "worker payslip history" v2 endpoint: p95 3.7 s, DB CPU 86% on payroll-review day, returns only 26 rows |
| `training/incidents/002-partner-sync-null-fields` | 6376bd9 | Partners report draft runs imported as "posted" and a Python job `KeyError`. Atlas shows all 200s, CI 922/922 green |
| `training/incidents/003-run-list-memory` | 451813e | API replicas OOM-killed Monday mornings, run-index p95 2.4 s for the big org, DB healthy |
| `training/incidents/004-canary-rollback` | 13f044d | ACA canary healthy, old revision 500s (42703), traffic "rollback" raises errors to 40% |
| `training/incidents/005-payroll-day-log-cap` | 5f52e96 | Log Analytics daily cap hit on payroll day (no logs during an outbox lag), salary data found in log search/SIEM |

## Verification
- Baseline HEAD: `dotnet build -warnaserror` OK. `dotnet test` **922/922** (Application 267, Domain 437, Architecture 5, Api 213).
- Each incident branch: `dotnet build -warnaserror` OK (0 warnings) and full `dotnet test` run.
  - 002, 004, 005: 922/922 green with no spec change. For 002 that's the point: the OpenAPI drift test does NOT catch it.
  - 001: 925/925 after re-blessing `docs/openapi/atlas-v1.json` (+53 lines). Before the bless only the drift test failed.
  - 003: 923/923 after re-bless (+10/−1). Before the bless only the drift test failed.
  - 004: migration generated with the repo's local `dotnet-ef` 10.0.10 (`dotnet tool restore`, not global), snapshot updated.
- A throwaway spike test (not committed) **confirmed review finding 6 / M4**: an anonymous `GET /api/v1/payslips/{id}` returns 401, `http.server.request.duration` records `status=200`, and the response has no `X-Correlation-Id`.
- **UNVERIFIED:** `dotnet format --verify-no-changes`. On this Windows checkout it reports ENDOFLINE for every file (CRLF vs LF `.editorconfig`), which is environmental. The incident scenario numbers (latencies, GB/day, row counts) are fictional-but-computed and not measured. No Postgres/Docker run: the plan shapes in INC-001/M1 answers are reasoned, not captured. The SQL Server/Azure content is design-only (no SqlServer provider exists in the repo).

## Issues found in the project (see `_answers/review.md` for all 23)
- **Presented as working but isn't:** `NoUnpaidLeaveCalendar` (returns 0) is still registered at v1.0.0, so approved unpaid leave is never deducted, and `LeaveRequest` has no paid/unpaid kind at all. "Active worker" has no termination (`HiredOn <= asOf` only). `PayslipVersioningTests` and `docs/concepts/contract-evolution.md` claim a byte-for-byte proof that doesn't exist (tolerant deserialization, circular comparison). `CachingFxRates` is unregistered dead code. 10+ comments reference a non-existent `NOTES.md`/`meta/NOTES.md`. The README's 5 personas: only OrgAdmin memberships can be created (`RegisterOrg.cs:53`).
- **Ops/correctness:** the default provider is `sqlite`, and on non-Npgsql `migrate` = `EnsureCreated`, so a misconfigured prod deploy silently writes to a per-replica local file. Telemetry records the wrong status for every thrown error and drops the correlation header (verified). The concurrent double-prepare → unmapped `DbUpdateException` → 500. The outbox dispatcher has no row claiming (duplicates at >1 replica). Serial webhook delivery with a 10 s timeout causes cross-tenant head-of-line blocking. Payroll reads are `RequireUser()` only (latent).
- **Secrets (locations only):** local dev DB credentials in `src/Atlas.Api/appsettings.Development.json`, `src/Atlas.Infrastructure/Persistence/DesignTimeDbContextFactory.cs` and `docker-compose.yml` (compose-only, low risk). No production secrets were found.
- **Working tree:** the ~181 "modified" files show **no content diff** (`git diff` and `--ignore-cr-at-eol` are both empty). It's line-ending churn only. Left untouched.

## Skill links (competency graph)
- data/SQL/indexes/migrations → `ladder/M1-cost-report-at-1m-payslips.md`, `incidents/001-payslip-history-latency.md`, `incidents/004-canary-rollback.md`, `ladder/M2-prepare-run-at-scale.md`, interview Q5–Q9, flashcards 15–20
- performance → `incidents/003-run-list-memory.md`, `ladder/M2`, `incidents/001`, `ladder/M1`
- backward compatibility → `incidents/002-partner-sync-null-fields.md`, `ladder/M3-payslip-v3-and-contract-tests.md`, `incidents/004`, Q1–Q3, Q13
- API design → `ladder/J1`, `ladder/M3`, `navigation/CHANGE_REQUEST.md`
- observability → `ladder/M4-payroll-run-observability.md`, `incidents/005-payroll-day-log-cap.md`, `navigation/TRADEOFFS.md` T3, Q18–Q19
- deployment/cloud/config/secrets → `ladder/S1-azure-container-apps-azure-sql.md`, `incidents/004`, review #3, Q20
- async jobs/queues/idempotency/outbox → `ladder/S2-payroll-as-a-background-job.md`, `ladder/M2` (race), `TRADEOFFS.md` T4, review #11 (light touch, as instructed)
- testing → `ladder/M3` (golden contracts), `INC-004` (migration linter), `INC-001` (model-index fitness), `J2` (stub-registration fitness)
- security (OWASP) → `incidents/005` (PII in logs), review #8 (latent authz), Q16–Q17
- reliability/incidents → 5 incidents + postmortems in `_answers/INC-*.md`
- code review → `review/EXERCISE.md` (23-finding model)
- navigation → `navigation/ARCHITECTURE.md`, `ONBOARDING.md`
- design docs/trade-offs → `navigation/TRADEOFFS.md`, `ladder/S1`, `ladder/S2`
- agentic engineering → `agentic/WORKFLOW.md`, `agentic/VERIFY_AI_OUTPUT.md`
- money correctness (niche) → `ladder/J2`, `ladder/M3` (money as string, frozen FX)
- caching → review #15 only (thin here; bazaar covers it)

## Curriculum needs (one central page each; not written)
1. **Reading query plans (Postgres EXPLAIN + SQL Server actual plans).** Seq/Clustered scan vs seek, rows examined vs returned, buffers/logical reads, key lookups, parameter sniffing. Used by INC-001 and M1.
2. **Index design and online index builds.** Column order for equality+range+order, INCLUDE/covering, and CONCURRENTLY vs ONLINE/RESUMABLE with their failure modes. Used by INC-001, M1 and S2.
3. **Expand/contract migrations and N-1 compatibility.** Why canaries don't protect against migrations, migration classes, the linter pattern. Used by INC-004 and S1 (netdrop S2 likely overlaps).
4. **API contract testing: schema vs behaviour.** Raw-JSON goldens, null-vs-absent, deprecation/sunset headers, 410 policy. Used by INC-002 and M3 (overlaps the backward-compat backlog).
5. **Truthful request telemetry.** Middleware order vs the exception handler, route-template tags, cardinality, logs vs metrics pipelines, ingestion caps and PII. Used by M4 and INC-005.
6. **Deploying .NET to Azure Container Apps.** Revisions, traffic split, jobs for migrations, managed identity to Azure SQL, probes. Used by S1 and INC-004.

## Existing learning-doc trees
- `docs/adr/` (19): **KEEP.** Linked from ladder M1/M3/M4.
- `docs/concepts/` (15): **KEEP.** `query-shape.md` and `observability.md` are **MERGE** candidates for curriculum pages 1/5 above (with user approval). `contract-evolution.md` overclaims and needs a correction note.
- `docs/runbooks/`: **KEEP / CONVERT** (deploy.md → INC-004/S1 raw material).
- `docs/postmortems/`: **KEEP** (spoiler-flagged; format templates).
- `docs/sprints/`, `LEARNER-GUIDE.md`, `docs/curriculum/SPEC.md`, `docs/COURSE-RETROSPECTIVE.md`: **KEEP** (the original course; spoiler-flagged).
- `FLAW-LEDGER.local.md`: **IGNORE** (a private duplicate of `docs/sprints/flaw-ledger.md`). None of its 5 flaws were reused.

## Honest caveats
- Atlas's real DB is Postgres. SQL Server appears as a **translation and design target** (M1, S1, INC-001 answer), not runnable code. A learner can't execute SQL Server plans without adding the provider (that's S1's job).
- The incident telemetry is invented to be *consistent* with the code (the route-less metric, log-line metrics), and the scale numbers were computed but never measured.
- The ARCHITECTURE doc restates several review findings. The README tells the learner to do the review first.
- **Shared-scratchpad collision:** the parallel gitjira-app agent overwrote my commit-message file (`msg005.txt`) between write and commit. INC-005's commit briefly carried the gitjira agent's commit message, and it was fixed with `--amend` on my own fresh local branch (content unaffected). Future agents should use unique scratch subfolders.
- All worktrees removed. Incident branches and the training commit are local only (never pushed).
