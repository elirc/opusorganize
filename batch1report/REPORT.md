# Batch 01 Report: Desktop .NET projects

*2026-09-23 · I ran `apprenticeship/BATCH_PROMPT.md` against audit batch 01. The per-project detail is in `projects/<name>.md`.
Shared outputs: `apprenticeship/COMPETENCY_GRAPH.md`, `apprenticeship/curriculum/01–05`, `apprenticeship/PROGRESS.md`.*

## 1. What to review first (15 minutes)
1. **Do the tiers look right?** See §2. You asked for the whole batch done end to end, so I chose the tiers without the Phase-1 stop. Change anything you disagree with.
2. **Start with netintercom's `training/README.md`.** It's a good sample of a full lab. Don't open `_answers/`.
3. **Look at the real defects in §5.** Several apps in this batch **don't compile on `main`**, and one pattern (§6) affects the whole Net-fleet.

## 2. Triage and tiers
| Project | What it is | Tier | Why |
|---|---|---|---|
| **netdrop** | Dropbox-style file storage, .NET 8 + React + PG + worker | **LAB** | richest distinct domain in the fleet: uploads, background scanning, quotas, sharing |
| **netintercom** | Intercom-style support inbox, .NET 8 + SignalR + Hangfire + 2 React apps | **LAB** | the only realtime app plus multi-replica jobs |
| .netstripe | subscription billing, minimal APIs | DRILL | money and idempotency flaws; zero tests |
| .netramp | expense approvals, flat ASP.NET | DRILL | approval state machine and upload trust; zero tests |
| netauth | OIDC identity provider | DRILL | auth-security specialty |
| eShop (netopen1) | OSS dotnet/eShop | READ | distributed outbox flow; already has a 72-story graded course |
| modular-monolith-with-ddd | OSS kgrzybek | READ | enforced module boundaries, outbox/inbox |
| netairag, netdocu, netlinear, netnotion, netshop | generated Net-fleet CRUD apps | SKIP | same Api/Application/Domain/Infrastructure shape as the two labs, so no distinct lessons |
| OrchardCore, CleanArchitecture | OSS with EXCELLENT existing curricula | SKIP (KEEP existing) | already covered |
| Umbraco, jellyfin, nopCommerce, eShopOnWeb | huge OSS clones | SKIP | low value for the effort |
| netsnapshot, netsnapshot1, csharptut, c#interview, csbootcamp | existing curricula | SKIP (KEEP existing) | already learning material |
| .nethris | empty | SKIP | — |

## 3. What was created
Every repo has a `training/` folder committed **by itself** (pathspec commit, so no source was touched on `main`). Bugged code exists only on `training/incidents/*` branches.
I checked afterwards: your uncommitted work is untouched (netdrop 15 files, eShop 3, modular-monolith 6), and no temporary worktrees are left.

| Project | Commit | Contents | Incident branches | Est. effort |
|---|---|---|---|---|
| netdrop | `7329298` | 11 ladder tickets (J0–J3, M1–M4, S1–S3), blind review (29 sealed findings), navigation + 5 "Why?" drills + CR-14, agentic exercise, full interview kit, 23 sealed answers | 5 | ~50 h |
| netintercom | `467ab4a` | 10 tickets (J1–J3, M1–M4, S1–S3), blind review (26), navigation + 4 trade-offs + CR, agentic workflow, full interview kit, 20 sealed answers | 5 | ~40 h |
| .netstripe | `b0e5001` | blind review (19), BillingEngine characterization-test exercise, mini interview kit | 2 | ~6–8 h |
| .netramp | `d89be45` | blind review (18), state-machine characterization-test exercise (reference verified), mini interview kit | 2 | ~6–8 h |
| netauth | `9e39ddd` | security-focused blind review (14, ASVS-tagged), mini interview kit | 2 | ~4–5 h |
| eShop | `6c9ebc5` | outbox-correctness trace, onboarding, sweeper trade-off, change request (links to the existing `astra/` 72 stories) | — | ~2 h |
| modular-monolith-with-ddd | `a7d111a` | boundary enforcement (ArchTests), command flow, cross-module event flow, outbox/inbox, "Why modular monolith?", change request | — | ~3 h |

**Incident symptoms** (the causes are sealed in each repo's `_answers/`):

**netdrop**
- 001: the usage meter drifts above real file sizes; "quota exceeded" on resume
- 002: files stuck on Pending while CPU drops
- 003: a user downloaded another account's file
- 004: folder listing p95 went from 180 ms to 3.7 s
- 005: everyone logged out after a deploy; later, self-signed JWTs were accepted

**netintercom**
- 001: agent-only text appeared in the widget preview
- 002: chats pile up unassigned while agents show as online
- 003: SLA toasts repeat 3–4× and grow after moving to 3 replicas
- 004: a pentest found a visitor could read another customer's replies
- 005: inbox p95 went from 180 ms to 3.7 s

**.netstripe**
- 001: legitimate payment retries get "already paid"
- 002: MRR is slightly under-reported

**.netramp**
- 001: Finance reimbursed an unapproved expense
- 002: a receipt-upload anomaly

**netauth**
- 001: a 401 spike at token expiry
- 002: an open redirect on the authorize endpoint

## 4. Verification (what's proven and what isn't)
| Check | Result |
|---|---|
| Incident branches compile | netdrop 5/5, netintercom 5/5, netstripe 2/2, netramp 2/2 build with 0 errors on SDK 10.0.302 · netauth 002 builds (Application project) · **netauth 001 is blocked** by the pre-existing compile error on `main` (the change is 1 line). |
| Tests | netintercom: 27/27 unit tests pass on INC-004/005. netramp: the characterization-test reference was run, 14/14 pass on main and 3 fail with incident 001, so the exercise works. netdrop INC-001: the existing 6 tests stay green on purpose (the lesson is that the tests don't catch it). |
| Not verified | Runtime symptoms: no Postgres/API/Docker was run, so the metrics and logs in the briefs are synthetic but consistent with the code paths. Frontend builds of incident changes. netintercom integration tests (they need Docker). |

## 5. Real defects found in your repos (documented, NOT fixed)
The committed `main` of 3 of the 5 generated apps does **not** build from a clean clone:
- **netauth:** `Program.cs:141` calls `Database.GetMigrationsAsync()`, **an EF Core API that doesn't exist**. The generator made it up. I found this with my own verification build.
- **netdrop:** `.gitignore:8` (`storage/`) matched `src/NetDropbox.Infrastructure/Storage/*.cs`, so the storage code was **never committed**. The EF model also throws on first use (`NetDropboxDbContext.cs:44`). Ticket J0 turns this into the first exercise.
- **.netstripe:** two compile errors (a missing `using` in `IdempotencyMiddleware.cs`; a `Money?` ternary at `Program.cs:143`). Its incident branches carry one-line fixes so the planted bug can be built.

Other notable real issues:

**netdrop**
- The concurrency token is inert (`Version` is never changed).
- Quarantined files can be downloaded (a copy is marked clean at `FileService.cs:76`; old versions skip the scan check).
- It silently falls back to a known JWT key (`Program.cs:42`).
- Uploads have a DB-then-in-memory-queue dual write.
- Storage is never released.
- The README claims Redis/RabbitMQ, retries and thumbnails that aren't really there.

**netintercom**
- `Seed:Enabled=true` sits in the base `appsettings.json`, so every environment gets a known admin password.
- The widget never rejoins its SignalR group after a reconnect.
- OTel has no exporter.
- Snooze never wakes.
- Its own `docs/architecture-review.md` §2.3 is wrong about concurrent SLA sweeps.

**.netstripe**
- A duplicate-invoice race.
- Webhook `EventId` is never deduplicated.
- `PaymentWorker` hardcodes success.
- Webhook "delivery" never sends.
- There is no auth at all.

**.netramp**
- Handlers and the worker change a shared `Expense` without locking, despite a "thread-safe" comment.
- The login "constant-time" comment is false: it returns early when the user doesn't exist.
- Uploaded files and sessions are never cleaned up.

**netauth**
- A critical unauthenticated `user_id` on `/connect/authorize`.
- Missing tenant isolation on admin APIs, plus `ValidateAudience=false`. The repo's own `docs2/08` already lists these, and the exercise tells you not to open it first.

**modular-monolith-with-ddd (upstream OSS)**
- The outbox gives each republished event a new Guid, which can create a duplicate `MeetingFee` that the inbox primary key doesn't catch.

**Secrets:** all are dev defaults (JWT keys, a Postgres password, seed passwords) in appsettings, docker-compose and README files. Locations are in each project report, and no values were printed.

**Git housekeeping:** eShop and modular-monolith-with-ddd had no git identity, so the agents set a **repo-local** name and email (yours) to commit. Nothing was pushed anywhere.

## 6. Pattern across the batch: the curriculum was written against code that never ran
The Net-fleet curricula (47–93 files each) describe runtime behavior of apps that don't compile, and they miss the defects above. This is now
[curriculum page 05](../apprenticeship/curriculum/05-verify-before-trust.md) and the strongest agentic-era lesson of this batch. The 5 skipped Net-fleet apps
(netairag, netdocu, netlinear, netnotion, netshop) almost certainly have the same problem. Checking that they build would be a good 30-minute exercise for you.

## 7. Existing learning docs: verdicts (nothing moved or deleted)
| Repo | Doc tree | Verdict |
|---|---|---|
| netdrop | `docs/upskill/` (47) | KEEP. The ladder supersedes its tickets; its risk register misses the build/model/quarantine defects. |
| netdrop | `astraupskill/` (untracked) | KEEP as a second opinion after M1. |
| netintercom | `docs/upskill/` (47) | KEEP |
| netintercom | `docs/architecture-review.md` | CONVERT TO EXERCISE. It is effectively an unsealed answer key and now serves as the second reference in the blind-review compare. |
| .netstripe | `docs/upskill/` + `docs2/` (93) | KEEP, with the caveat that they were written against non-compiling code |
| .netramp | `docs/upskill/` (46) | KEEP |
| netauth | `docs2/` | KEEP (`docs2/08` is a gated answer key) · `docs/upskill/` (47, 34 empty stubs): **IGNORE** |
| eShop | `astra/`, `fabledocs/`, `fabledoc2/` | KEEP all three (distinct and evidence-backed) |
| modular-monolith-with-ddd | parent `astraupskill/` | KEEP |

No MERGE was needed. Concepts that recur across projects went into 5 new central pages instead (`apprenticeship/curriculum/01–05`).

## 8. Gap report
- **Now well covered (don't add more in the next batches):** authn/authz/IDOR, CRUD-level concurrency, idempotency, outbox, code review, reliability incidents.
- **Still thin:**
  - **Observability** (only designs; nothing emits and is watched)
  - **Cloud deployment** (only S-rung designs)
  - **Caching**
  - **Frontend/React**
  - **Performance measured with real numbers**
  - **SQL Server** (none)
- Best archive projects to fill them next (from `portfolio-audit/FINAL_REPORT.md`):

| Gap | Project |
|---|---|
| Observability, incidents on a live stack | `astraspacegameweb` (Prometheus/Grafana/Tempo) |
| Postgres perf with real EXPLAIN | `astra1` |
| Cloud deploy, zero-downtime migration | `gitjira-app` |
| SQL Server, API versioning | `gitvg\atlas` |
| Frontend perf/a11y | `lucasrouter` |
| Caching | `gitvg\bazaar` |

- **Recommended next batch (B02):** `gitjira-app` + `gitvg\atlas` as LABs, with `gitvg\pulse` and `perch` as DRILLs (flaw ledgers). This matches the audit roadmap's NOW wave.

## 9. What you should do first (suggested order, about 2 weeks part-time)
1. **netdrop ticket J0:** make `main` build and boot. It's the real `.gitignore` bug, so it's a real first day on a broken repo.
2. **netdrop blind review** (60 min), then COMPARE. This is where your own blind spots show up.
3. **netdrop INC-004** (a latency incident), then **INC-003** (a security incident). Work them before opening the answers.
4. **netramp characterization tests.** Short, and the payoff is verified.
5. **netintercom INC-003 + ladder M2** (concurrency across replicas), with curriculum pages 01–03 alongside.
6. **Agentic exercise on netdrop M1:** write the spec yourself, let an agent implement it, review adversarially, then write your explanation.
7. **Mock defense** (`netdrop/training/interview/MOCK_DEFENSE.md`) with a model as interviewer.
