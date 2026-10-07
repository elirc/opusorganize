# Batch 02 Report: gitvg course repos + gitjira-app

> **Status note (added 2026-10-06):** this report is a frozen record of the batch and was not updated afterwards. Not every `training/incidents/*` branch it describes is on GitHub: only 21 of the 92 from B01–B07 were pushed, and several projects now live under different elirc repo names. Before you try to check out an incident, see the incident-branch availability note at the top of [`apprenticeship/PROGRESS.md`](../apprenticeship/PROGRESS.md).

*2026-09-23 · I ran `apprenticeship/BATCH_PROMPT.md` against audit batch 02. The batch was deliberately biased toward the skills B01 left thin
(query plans, migrations, observability, deploy, caching, frontend). Per-project detail is in `projects/<name>.md`.
Shared outputs: `apprenticeship/COMPETENCY_GRAPH.md` (updated), `apprenticeship/curriculum/06–10` (new), `apprenticeship/PROGRESS.md`.*

## 1. What to review first
1. **Tiers (§2).** Change anything you disagree with.
2. **`gitvg\atlas\training\README.md`:** the best-verified lab so far (every incident builds and passes the full 922-test suite).
3. **§5, real defects.** Several of these would be serious in a real product, and they make excellent interview stories.

## 2. Triage and tiers
| Project | What it is | Tier | Why |
|---|---|---|---|
| **gitjira-app** | Jira clone, Express/React/Prisma/BullMQ/Socket.IO, 209 commits, real CI/deploy | **LAB** | audit flagship; production and realtime track |
| **gitvg\atlas** | EOR/payroll, .NET 10 hexagonal, V1/V2 APIs, outbox, 922 tests | **LAB** | audit flagship; SQL/.NET/API-evolution track |
| gitvg\pulse | analytics ingestion (PostHog-style) | DRILL | ingestion performance and alerting |
| perch | applicant-tracking system | DRILL | frontend (the thinnest core skill) |
| gitvg\bazaar | e-commerce | DRILL | caching (the thinnest skill after B01) |
| tracer, harbor | same course template | SKIP | same lessons as the above |
| relay (durable execution), folio (CRDT/offline merge) | same template, but distinct topics | SKIP for now | **revisit later**: distinct distributed-systems lessons |
| *-net / *-app rebuilds (tracer-net, harbor-net, pulse-net, atlas-net, agora-net, relay-app, folio-app, bazaar-app) | .NET rebuilds of the same courses | SKIP | duplicates |
| agora, storefront, gitvg\astra, gitjira (spec), docs/tools/prompts | thin history / docs only | SKIP | — |

## 3. What was created
Every commit is `training/`-only (checked: 0 non-training files). Your uncommitted work is untouched: gitjira-app 14 files, and atlas 181
(which turn out to be **line-ending churn only**, with no content diff). No worktrees are left, and nothing was pushed.

| Project | Commit(s) | Contents | Incidents | Est. effort |
|---|---|---|---|---|
| gitjira-app | `a0b506c`, `b778462` | 10 tickets: J1 readiness vs liveness, J2 table stops at 50, J3 queue metrics, M1 board at 2k issues, M2 SLOs, M3 Redis as a soft dependency, M4 Socket.IO on 2 machines, S1 Fly → AWS, S2 expand/contract on 2M rows, S3 notification-latency SLO · review (29) · navigation + CR-21 · agentic (M3) · full interview kit | 5 | ~40–50 h |
| atlas | `e85c35a` | 8 tickets: J1–J2, M1 query plans at 1.3M payslips (PG + SQL Server), M2 25k-worker prepare, M3 v3/deprecation/contract tests, M4 telemetry, S1 Azure Container Apps + SQL, S2 durable payroll job · review (23) · navigation + 4 trade-offs + CR · agentic (M2) · full interview kit | 5 | ~32–40 h |
| pulse | `67fb143` | review (17) · mini interview kit | 2 | ~5–6 h |
| perch | `f56f063` | review (14) · mini interview kit | 2 | ~5–6 h |
| bazaar | `4d6eb1f` | review (14) · mini interview kit | 2 | ~5–6 h |

**Incident symptoms** (causes are sealed in each repo's `_answers/`):

gitjira-app:
- 001: Postgres and event-loop lag spike when a big team opens its board.
- 002: repeat assignments and mentions never notify.
- 003: 4 minutes of 5xx during a deploy, then story points are gone.
- 004: dashboards show "No data", memory climbs, p99 spikes every 15 s.
- 005: the live board goes stale about 15 minutes after load.

atlas:
- 001: payslip-history p95 is 3.7 s for 26 rows.
- 002: a partner imports draft runs as "posted" while Atlas shows only 200s.
- 003: replicas are OOM-killed while the DB looks healthy.
- 004: the canary is healthy, but the old revision 500s and the rollback raises errors to 40%.
- 005: the log cap is hit on payroll day, and salary data shows up in the SIEM.

pulse:
- 001: a severe backlog is reported only as "degraded", so nobody is paged.
- 002: trend-query load and latency jump after a readability refactor.

perch:
- 001: search API calls go up about 4× and results flicker after a "debounce" deploy.
- 002: the careers form rejects valid emails, and the server sees nothing.

bazaar:
- 001: the storefront shows a stale price 20+ minutes after a fix.
- 002: a VIP customer's discounted price leaks to other shoppers.

## 4. Verification
| Project | Status |
|---|---|
| atlas | **Strongest.** Unchanged, it builds warnings-free with 922/922 tests; each incident builds and passes the suite. The 001/003 branches have the OpenAPI doc updated; 002 passes unchanged on purpose because contract tests can't see it. The 004 migration was generated with the repo's own `dotnet-ef`. **Unverified:** real Postgres plans (no Docker), SQL Server/Azure (design only). |
| gitjira-app | 001 and 004 were **run**: `join-project` fired 25× in 300 ms vs 1×, and there were ~504k metric series / a 55 MB scrape vs 36 series. For 003, `prisma migrate diff` reproduces the DROP + ADD. 002 was checked against the BullMQ source only (no Redis). For 005, web tests pass 16/16, but the reconnect behavior wasn't run. API integration tests and e2e weren't run. |
| pulse, perch, bazaar | `BUILD: UNVERIFIED`. No dependencies are installed, and parallel pnpm installs have broken this machine before, so incidents were hand-traced. Pulse's incidents are covered by existing unit tests, so running `pnpm test` would show them failing. |

To verify the three pnpm repos later, install one repo at a time, then run `pnpm test` on each incident branch.

## 5. Real defects found (documented, NOT fixed)

**gitjira-app**
- Deploy (actually to **Fly.io**, not AWS) ships only the API, never the worker or web app, and doesn't wait for CI.
- Attachments are stored on local disk and vanish across machines; a missing file crashes the API.
- Socket.IO has no adapter, and broadcasts fire before commit.
- Redis is a hard dependency, even though the RUNBOOK says the API degrades gracefully.
- The board only shows the newest 50 issues.
- There is no graceful shutdown, and the watch endpoint has no authz.
- The repo's own AUDIT admits its rollback drill and postmortem were narrated, not run.

**atlas**
- Approved unpaid leave is never deducted (`NoUnpaidLeaveCalendar` returns 0 at v1.0.0).
- "Active worker" never ends, so terminated workers would keep being paid.
- The "byte-for-byte" v1 contract test compares the code against itself.
- `CachingFxRates` is dead code.
- Over 10 comments cite a `NOTES.md` that doesn't exist.
- The default DB provider is SQLite, so a prod deploy missing one env var would write to a local file on each replica.
- The outbox has no row claiming, so multiple replicas send duplicate webhooks.
- Webhooks are delivered serially with a 10 s timeout.
- An anonymous 401 is recorded in the duration metric as 200.

**pulse**
- Redis `XADD` runs once per event with no pipelining (`apps/ingest/src/server.ts:163-181`).
- Identity is resolved with one DB round-trip per event.
- In-memory caches are unbounded.
- `BufferedColumnStore` claims "flush on size or time" but only flushes on size.

**perch**
- **Sign-in has no credential check at all.**
- The server wires only in-memory demo repos, although Prisma repos exist and the runbooks assume persistence.
- The public apply endpoint has no rate limit.
- There are zero frontend component tests.

**bazaar**
- The whole `@bazaar/cache` library is built and tested but **never wired into any app**.
- Background-refresh errors are silently swallowed.

**Secrets:** dev defaults only; locations are listed in the project reports.

**Deviations the agents made**
- gitjira-app's commitlint rejects the type `training`, so the commits use `docs(training): …`. No hooks were bypassed.
- `node_modules` (873 packages, gitignored) was left installed in gitjira-app.

## 6. Existing learning docs: verdicts (nothing moved or deleted)
| Repo | Verdict |
|---|---|
| gitjira-app | ADRs: KEEP. `docs/concepts/`: MERGE candidate (only with your approval). RUNBOOK and postmortems: CONVERT (now gated exercises). `astraupskill/`: KEEP. |
| atlas | `docs/adr`, `runbooks`, `postmortems`, `sprints`, course guides: KEEP. `docs/concepts`: KEEP (`query-shape.md` and `observability.md` are MERGE candidates; `contract-evolution.md` overclaims). `FLAW-LEDGER.local.md`: IGNORE (spoiler). |
| pulse, perch, bazaar | KEEP everything. Their flaw ledgers are spoilers and are named in each `training/README.md`. |

**Spoiler rule** for these course repos: don't open `FLAW-LEDGER.local.md`, `docs/sprints/flaw-ledger.md` or `docs/postmortems/` before doing the exercises.

## 7. Gap report (after B01 + B02)
- **Now good:** query plans/N+1, zero-downtime migrations, observability/SLO correctness, API versioning, realtime, plus everything from B01.
- **Saturated (stop adding):** authz/IDOR, concurrency races, idempotency/outbox.
- **Still thin:**
  - **Accessibility:** 0 exercises.
  - **Frontend/React:** 6 exercises, still the weakest core skill.
  - **SQL Server:** only a translation exercise.
  - **Anything actually deployed and operated:** everything so far is design only.
- **Recommended B03:**
  - **LAB:** `astraspacegameweb`. It has a real Prometheus/Grafana/Tempo stack and chaos tests, so it's the chance to *operate* something.
  - **LAB:** `lucasrouter`. It has frontend performance with measured Lighthouse numbers, plus an accessibility track.
  - **DRILL:** `astra1` (raw-SQL Postgres, OTel).
  - **READ:** Outline, with its fire drills and first upstream-PR prep.

## 8. What to do first (suggested order, about 2 weeks part-time; after B01's first steps)
1. **atlas M1** (query plans at 1.3M rows), then **netdrop INC-004** and **atlas INC-001**. Same symptom, three causes; use curriculum page 10.
2. **gitjira-app INC-003** (the deploy that dropped story points), then **ticket S2** (expand/contract). Use page 07.
3. **gitjira-app INC-004** (metric cardinality) and **pulse INC-001** (the alert that never fires). Use page 09.
4. **bazaar INC-001 + INC-002** (caching). Use page 06.
5. **perch INC-002** (client/server validation drift): a short frontend drill.
6. **atlas M3** (API v3 with contract tests): your backward-compatibility interview story.
7. **Mock defense:** `gitvg\atlas\training\interview\MOCK_DEFENSE.md` with a model as the interviewer.
