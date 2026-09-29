# netdrop (NetDropbox): B01 report

**Tier:** LAB (Phases 2, 3, 4, 5)  **Repo:** `C:\Users\Owner\Desktop\netdrop` (own `.git`)  **Base:** `main` @ `d612e0b` (single commit)
**Training commit:** `7329298` "training: add B01 apprenticeship materials" (pathspec commit, `training/` only, 54 files). The user's 15 uncommitted changes (Astra upload-integrity work, `astraupskill/`, new `tests/.../Uploads/`) were not touched.

## What I created (`netdrop\training\`)
- `README.md`: index, suggested order, about 50 h total (a one-weekend subset is included).
- `ladder/`: README plus 11 tickets. **J0** make main build/boot (setup). **J1** upload-status 404 plus a query handler. **J2** folder move cycle. **J3** unique live sibling names. **M1** idempotent upload completion. **M2** search at 2 M files. **M3** scan state follows the bytes. **M4** storage accounting and blob GC. **S1** durable processing pipeline. **S2** migrations baseline plus a zero-downtime move of scan status. **S3** three replicas in the cloud with rollback.
- `review/`: `EXERCISE.md` (60-min blind review of committed `main`) and `COMPARE.md`.
- `incidents/`: README (worktree instructions) plus 5 briefs.
- `navigation/`: `ARCHITECTURE.md` (evidence-cited, 3 flows, data model, self-check), `FIRST_CHANGE.md`, `TRADEOFFS.md` (5 "Why?" drills), `CHANGE_REQUEST.md` (CR-14, Editor uploads into a shared folder).
- `agentic/`: `EXERCISE.md` (spec → implementer → adversarial reviewer → revision → verify → graded explanation, on M1) and `VERIFY_CHECKLIST.md`.
- `interview/`: `PROJECT_STORIES.md` (5 STAR scaffolds), `TECHNICAL_QUESTIONS.md` (20), `SYSTEM_DESIGN.md`, `MOCK_DEFENSE.md` (buzzword-refusing interviewer script plus an /18 rubric), `FLASHCARDS.md` (25, with a spoiler warning).
- `_answers/` (sealed, 23 files): `review.md` (29 ranked findings), `incident-001..005.md`, `ladder-J0..S3.md` (11), `navigation-architecture.md`, `navigation-change-request.md`, `agentic-rubric.md`, `interview-technical.md`, `interview-system-design.md`.

## Incident branches (each = HEAD + "add Infrastructure/Storage adapters so this branch builds" + the bug PR)
| Branch | Bug commit | Symptom (not the cause) |
|---|---|---|
| `training/incidents/001-quota-meter-drift` | `8bf1241` | Usage meter far above real file sizes; "Storage quota exceeded" on upload resume; deleting files doesn't help |
| `training/incidents/002-scan-backlog` | `e1aec2a` | New files stuck "Pending" for tens of minutes; scan p95 2 s → 38 min while CPU drops |
| `training/incidents/003-shared-download-exposure` | `fab82db` | Bug bounty: a user downloaded a file from an unrelated account (200 for one file ID, 404 for another) |
| `training/incidents/004-slow-folder-listing` | `1b2980f` | `GET /api/v1/files` p95 180 ms → 3.7 s; statements/s ×27; API memory ×4 |
| `training/incidents/005-staging-token-anomaly` | `5cecfaf` | Everyone logged out right after a deploy; days later, a report that self-signed JWTs are accepted |

The vendoring commits (`89fb32b`, `321c5ba`, `687cf78`, `520abbb`, `aa42ed4`) force-add the 3 storage adapters. `LocalBlobStorage` and `S3CompatibleBlobStorage` come verbatim from the working tree (unchanged by Astra). `FileSystemChunkStorage` comes from `astraupskill/snapshots/*FileSystemChunkStorage.cs.original.txt`. Worktrees were removed after committing.

## Verification
- **BUILD: VERIFIED for all 5 incident branches.** `dotnet build src/NetDropbox.Api/NetDropbox.Api.csproj` succeeded with 0 warnings and 0 errors, using the .NET SDK 10.0.302 targeting net8.0. There's no global.json in this repo, so the orchestrator's global.json tip didn't apply.
- On the 001 branch, `dotnet test` (with `DOTNET_ROLL_FORWARD=Major`, since only the .NET 10 runtime is installed) passed 6/6. The existing tests stay green on a bugged branch, which is intentional and part of the lesson.
- **Verified by execution:** (a) `main` is missing `Infrastructure/Storage/*.cs` from git (`git ls-files`, `git check-ignore -v` → `.gitignore:8 storage/`). (b) The committed EF model throws `InvalidOperationException: The member 'FileNode._versions' cannot use field '_versions' because it is already used by 'FileNode.Versions'`. I checked this with a scratch console in the scratchpad that built `db.Model`. (c) After patching that line in a throwaway worktree, the `Version` concurrency token is a plain `bigint` with `ValueGenerated=Never`, and the whole model has exactly **one** FK.
- **UNVERIFIED:** runtime behavior of the incidents (no Postgres or API was run); the web client build (`web/node_modules` is absent; no incident touches TS); the .NET 8 `StopHost` default claim in review #7 (documented behavior, not reproduced); the ImageSharp HEIC failure in INC-002 (library knowledge, not executed); the answers' cost figures in S3 (order of magnitude only).

## Issues found in the project
- **Presented as working but broken:** `main` doesn't compile from a clean clone (`.gitignore:8` swallows `src/NetDropbox.Infrastructure/Storage/`), and CI (`.github/workflows/ci.yml`) would fail. The committed EF model throws on first use (`NetDropboxDbContext.cs:44`). The README advertises CI, reference counts, retry/dead-letter, Redis and RabbitMQ (unused), and previews/thumbnails (never served).
- **Security (top):** Copy launders quarantined files (`FileService.cs:76`). `download?versionId=` bypasses the scan gate (`FileService.cs:118-120`). JWT signing key falls back silently to a constant (`Program.cs:42`, `AuthController.cs:32`). The public share survives trash (`ShareService.cs:62`). Login is unthrottled with timing-based user enumeration.
- **Consistency:** a DB→in-memory-Channel dual write loses scans (`CompleteUpload.cs:82-84`); `processing_jobs` is never read back. The concurrency tokens are inert. `Release`/`RemoveReference` have zero callers. There are no FKs except one.
- **Secrets (locations only; all dev defaults, not live credentials):** JWT signing key and S3 access/secret key in `src/NetDropbox.Api/appsettings.json`; the same values in `docker-compose.yml` and `.env.example`; the Postgres password in the connection-string fallbacks (`Program.cs:74`, `DependencyInjection.cs:20`); seed user passwords in `DbSeeder.cs` and `README.md`.
- **Stale docs:** `docs/upskill/README.md` says "Pinned snapshot: UNCOMMITTED-NO-HEAD", but the repo now has commit d612e0b.

## Skill links (for COMPETENCY_GRAPH)
- web/TS/React → `interview/TECHNICAL_QUESTIONS.md` Q17–18; review #24; INC-004 (task 4, backward-compatible pagination)
- API design → `ladder/J1-upload-status-404.md`; `ladder/M2` (keyset, compatible contract); Q1–4
- data modeling/SQL/indexes → `ladder/J3-name-conflicts.md`, `ladder/M2-search-at-scale.md`, INC-004, Q6–8
- transactions/concurrency → `ladder/M1-idempotent-complete.md`, `ladder/J2` (concurrent moves), `ladder/M4`, INC-001, Q5, Q9, Q12
- migrations → `ladder/S2-zero-downtime-migration.md`, `ladder/J3` (index on existing data)
- authn/authz/multi-tenancy → INC-003, INC-005, `navigation/CHANGE_REQUEST.md` (CR-14), `interview/SYSTEM_DESIGN.md` (tenancy), Q14–16
- testing → `ladder/J0` (model-builds test), J1 (WebApplicationFactory), M1 (Testcontainers concurrency), INC-004 (query-count test), `agentic/VERIFY_CHECKLIST.md`, Q19
- async jobs/queues/idempotency/outbox → `ladder/S1-durable-processing.md`, INC-002, M1, Q10–11
- caching → thin here (only a CDN mention in S3); not a strength of this project
- observability → INC-003/005 (no user ID in logs), S1 metrics and alerts, S3 dashboards
- deployment/cloud/config/secrets → INC-005, `ladder/S3-three-replicas.md`, J0 (gitignore/CI)
- security (OWASP) → INC-003 (IDOR), INC-005 (fail-open secret), M3 (quarantine bypass), review #3–5, #20–21
- performance → INC-004 (N+1 plus overfetch), M2, Q8, Q17–18
- reliability/incidents → all 5 incidents plus postmortems; review #7 (worker stops host)
- backward compatibility → M2/INC-004 pagination, S2 expand/contract, J1 DTO field
- design docs/ADRs → `navigation/TRADEOFFS.md` (5 "Why?" drills), S1–S3 design docs
- code review → `review/EXERCISE.md` + `_answers/review.md` + `COMPARE.md`; every incident has a "why review missed it"
- unfamiliar-codebase navigation → `navigation/ARCHITECTURE.md`, `FIRST_CHANGE.md`, CR-14
- agentic engineering → `agentic/EXERCISE.md`, `VERIFY_CHECKLIST.md`, `_answers/agentic-rubric.md`

## Curriculum needs (one central page each; not written)
1. **Dual writes and the transactional outbox.** DB + queue/blob without a distributed transaction; outbox vs jobs-table-as-queue vs broker; when to switch.
2. **Postgres as a job queue (`FOR UPDATE SKIP LOCKED`, leases, backoff without head-of-line blocking).** Claim queries, visibility timeouts, poison classification.
3. **Optimistic concurrency in EF Core + Npgsql.** `IsConcurrencyToken` vs `IsRowVersion`/`xmin`; atomic `ExecuteUpdate`; why an unwritten token is inert.
4. **Idempotent endpoints.** Claim-by-update, idempotency keys, the "same request → same response" contract, crash windows.
5. **Expand/contract migrations and batched backfills on Postgres.** Baseline on a hand-made schema, `CONCURRENTLY`, `NOT VALID` FKs, rollback points.
6. **Authorization patterns for ORM apps.** Inline predicates vs policy service vs global query filters vs RLS; the authorization-matrix test.
7. **Fail-closed configuration and secrets in ASP.NET Core.** Options validation plus `ValidateOnStart`, config layering and env-var mapping, no fallbacks for secrets.
8. **Postgres text search.** `pg_trgm` vs `tsvector`, expression indexes, keyset pagination.
9. **Content-addressed storage with refcounts and GC.** Dedupe side channels, mark → grace → delete.

## Existing learning-doc trees
- `docs/upskill/` (47 files, 1,356 lines; cartography, patterns, drills, tickets, risk register). **KEEP** (link as background reading). Its `08-reference/risk-register.md` is accurate as far as it goes, but it misses the build and EF model breakage, both quarantine bypasses, the inert concurrency token and the never-called Release/RemoveReference. Its `06-contribution-practice/*` tickets are one-paragraph prompts that the new ladder supersedes (**CONVERT**: already done in substance by M1/M2/M4/S1; no move needed). Its README header about the snapshot is stale.
- `astraupskill/` (untracked; 23 files including evidence and snapshots). A worked change for upload integrity that matches the user's uncommitted diffs (22 tests reported passing in their own run). **KEEP.** It's referenced from `training/README.md` as a second opinion after M1. Don't merge or move it. It isn't committed, and it documents uncommitted code.

## Honest caveats
- All exercises target committed `main`, which doesn't build or boot as-is. J0 is a mandatory first step, and incident branches carry an extra vendoring commit so they compile. The vendoring commit's message is neutral, but it does hint at review finding #1.
- The incident *symptoms* (metrics and logs) are synthetic but consistent with the code paths. Nothing was run against a live database.
- The brief's "no hint of the cause" rule holds for the incident briefs. Flashcards and three technical questions reveal causes, so they carry spoiler warnings and are ordered last.
- The ladder answers are reference analyses, not implemented solutions. No fix branches were created.
- Scratch artifacts (the modelcheck console and patch files) are left in the session scratchpad only, not in the repo.
