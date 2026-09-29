# buildevent: B04 report (LAB, load and back-pressure)

**Repo:** `C:\Users\Owner\Desktop\buildevent` (own `.git`, `main` @ 645435c, remote elirc, **not pushed**)
**Tier:** LAB (phases 2-5). **Training commit:** `baf46ea` "training: add B04 apprenticeship materials" (53 files, a pathspec commit of `training/` only).
The user's 7 uncommitted items (README.md, checkin.routes.ts, checkin.service.ts, order.service.ts, deleted web tsbuildinfo, untracked `apps/api/tests/order-checkin.test.ts`, `astraupskill/`) were **not touched**.

## Created (all under `C:\Users\Owner\Desktop\buildevent\training\`)
- `README.md`: the index, setup, a suggested order (~50 to 60 h), real-bugs-on-main list, and existing-tree verdicts
- `ladder/`: J1 availability contract + CDN, J2 health/readiness, J3 Reserve button + busy/Retry-After + first web tests; **M1 inventory under spike (the real main bug)**,
  M2 expiry workers + back-pressure, M3 rate limit + waiting room, M4 k6 + SLOs; S1 50k-user drop capacity plan, S2 offline-first check-in, S3 timeout budget / bulkheads / degradation
- `review/EXERCISE.md`, `review/COMPARE.md` → `_answers/review.md` (25 findings, AI-smell tagged)
- `incidents/001-005` briefs → `_answers/incident-00N.md` (+ sealed repro tools `_answers/tools/inc002-redis-pressure.mts`, `inc005-qr-drain.mts`)
- `navigation/` ARCHITECTURE, FIRST_CHANGE, TRADEOFFS (5 "Why?" drills), CHANGE_REQUEST (presale codes) → `_answers/navigation-*.md`
- `agentic/WORKFLOW.md` (M1 via spec → implementer → adversarial reviewer → verification checklist → graded explanation)
- `interview/` PROJECT_STORIES (5), TECHNICAL_QUESTIONS (20), SYSTEM_DESIGN, MOCK_DEFENSE, FLASHCARDS (24) → `_answers/interview-technical.md`
- `load/drop.k6.js`: the **k6 skeleton** (3 scenarios, numbered TODOs M4-1..11, thresholds shape), plus `load/README.md`. **Not wired into CI.**
- `tools/drop-sim.mts`: an in-process drop simulator (reserve / browse / checkout-with-fake-slow-Stripe / cleanup) that calls the real services against a real Postgres
- `_answers/ladder-M1-reference.diff`: the lab patch used for the measured "after" numbers

## Incident branches (symptom only)
| branch | commit | symptom |
|---|---|---|
| `training/incidents/001-reserve-retry-storm` | bbf65c2 | "fixed the 500s": reserve now spins 15 s, and most of 200 buyers still fail |
| `training/incidents/002-redis-cache-eviction` | 3ee1a02 + 2f57148 | "Sold out" with 480 tickets unsold. No errors anywhere |
| `training/incidents/003-checkout-pool-exhaustion` | 462e5a1 | Stripe slow, and door check-in at another event fails, with every route slow |
| `training/incidents/004-availability-hot-row` | 87d5454 | Read-only availability endpoint 3× slower after an analytics feature |
| `training/incidents/005-qr-queue-backlog` | 35364f1 | Tickets without QR codes for ~10 min after purchase |
(002 has two commits: a benign "start workers" commit so the expiry queue exists, then the suspect cache PR.)

## Verification
- `npm ci` (package-lock) in the main tree, once. The shared and renderer packages built. A scratch **native Postgres 18** (initdb in the scratchpad, port 5451) plus
  **Docker Redis 7** (`-p buildevent-training`, ports 6391 allkeys-lru 4 MB / 6392 noeviction). All were stopped and removed at the end. Worktrees and junctions were removed.
- **HEAD:** api `tsc --noEmit` 0 errors, `vitest` 1/1.
- **All 5 incident branches:** api `tsc --noEmit` 0 errors (INC-004 after `prisma generate` with its schema). The Prisma client was regenerated back to HEAD's schema afterwards.
- **Run-verified incidents (numbers are in the briefs and answers):**
  - main: 40 concurrent reserves → 5 ok / 35 P2034 (500). The PG log shows 750 × "could not serialize access due to concurrent update". 200 buyers → 3 ok.
  - 001: 38 ok but p95 3.6 s → 14.3 s. With pollers → P2028. 200 buyers → 175 P2028.
  - 002: after ~1k unique-URL cache writes, the `order-expiry` repeatable + delayed job were **evicted** (repeatables=1 → 0). BullMQ printed its "Eviction policy is allkeys-lru" warning.
  - 003: fake Stripe 3 s → unrelated reads p95 96 ms → 10 s, 20/78 reads P2024, 20/40 checkouts P2024.
  - 004: availability 972 → 334 req/s, p50 47 → 167 ms. `Lock:transactionid`/`Lock:tuple` waits observed.
  - 005: 400 tickets. Webhooks acked in 8.4 s, and the last QR at t+30.7 s (~13/s, concurrency 1). 400 completed jobs retained in Redis.
  - The M1 reference fix measured: 0 × 5xx at 40 and 200 buyers, and counters match. The DoD's "503 p95 < 1.5 s" was NOT met by the lab patch (the 5 s queue wait). That's stated in the answer.
- **UNVERIFIED:** the k6 skeleton (k6 isn't installed, never run), the web (J3) and scanner items (no web tests or builds run), and "production dashboard" numbers in briefs 002 and 005
  (illustrative, and labelled as such in `training/README.md`). All numbers come from a slow laptop (bcrypt compare 1.3 s). They're relative, not absolute.

## Issues found in the project (on `main`)
- **Claimed but not true:** the README says optimistic locking with retries protects reservations. In practice `Serializable` turns every conflict into a 500 (measured 35/40).
  The README says expiry jobs release pending orders, but **nothing imports `jobs/*.ts`**. README setup calls `npm run db:push`, which doesn't exist at the root (only in the api workspace).
- **Fake integrations:** the Stripe webhook verifies a `JSON.stringify`-re-serialized body (it can't verify real events). The web checkout never sets `clientSecret`. The Reserve button has no handler.
  My Tickets (unauthenticated fetch) and event availability silently fall back to **demo data** on any error.
- **Load bugs:** `count(*)` order numbers, an implicit 5-connection pool shared by all routes, a global 100/min per-IP in-memory rate limit (hits webhooks and venue scanners),
  bcryptjs cost 12 (1.3 s/compare measured), the Stripe SDK's 80 s default timeout, Redis `maxRetriesPerRequest: null`, `allkeys-lru` with BullMQ,
  100 concurrent webhooks → P2028 (QR CPU on the same event loop), and expiry capped at 100/min.
- **Secrets:** no real secrets committed. `apps/api/src/config.ts:10-14` has **hardcoded default secrets for all environments** (JWT, refresh, ticket signing), so production can
  boot with publicly known keys. `.env.example` and `.github/workflows/ci.yml` hold placeholder values only.
- The migrations folder is git-ignored (`.gitignore:10`). `fastify-plugin` is not declared in `apps/api/package.json`. Tests: 1 Zod test, and the other workspaces `echo`.

## Skill links (for COMPETENCY_GRAPH)
- **Load / back-pressure** → ladder M1, M2, M3, M4, S1; incidents 001, 005; `tools/drop-sim.mts`; interview Q15-17
- **Performance (measured)** → incidents 001, 003, 004 (run-verified before/after); M1 table
- **Reliability / incidents** → incidents 001-005 (5 sealed postmortems)
- **Async jobs / queues** (back-pressure angle only, not idempotency) → M2, incident 002, incident 005
- **Caching** → incident 002 (unbounded keys, TTL, key normalization), J1 (CDN `s-maxage`, 404 caching)
- **Observability** → incident 002 (heartbeat and invariant alerts on absent signals), incident 005 (age-of-oldest-job), review #19 (log levels)
- **Deployment / config** → J2 (liveness vs readiness), S3 (timeout budget, bulkheads), Redis policy per role
- **SQL / transactions** → M1 (isolation level vs optimistic locking, single-statement decrement), incident 004 (row locks, MVCC/HOT), M2 (`SKIP LOCKED` batch sweeper)
- **Security** (drop-relevant only) → S2 (HS256 vs ES256 for offline verification), review #23/#24
- **Web / React** → J3 (double-submit guard, Retry-After backoff, first web tests), T5 (demo fallback as a correctness bug)
- **Testing** → J1-J3 integration/inject tests, M1 concurrency integration test, interview Q20
- **Code review** → `review/EXERCISE.md` (25 findings)
- **Agentic engineering** → `agentic/WORKFLOW.md` (M1)
- **Design docs / trade-offs** → navigation/TRADEOFFS T1-T5, S1-S3
- **Unfamiliar-codebase navigation** → navigation/ARCHITECTURE + FIRST_CHANGE + CHANGE_REQUEST

## Curriculum needs (pages worth writing once; not written)
1. **Load, back-pressure and admission control:** arrival vs service rate, Little's law, rate limiting vs concurrency limiting, waiting rooms, and 503 + Retry-After semantics. Worked examples: buildevent M1/M3/incident 001.
2. **Timeouts, retries and bulkheads:** retry amplification across layers, one retrying layer, jittered backoff, time budgets, per-route pools, circuit breakers. buildevent incidents 001/003, S3.
3. **Load testing that tells the truth (k6):** open vs closed model, coordinated omission, SLO thresholds, seeding and reset, and never in CI. buildevent M4.
4. **Hot rows and lock contention in Postgres:** isolation-level semantics under concurrent update, row-lock queues, MVCC/HOT churn, and sharded counters. buildevent M1/incident 004. (Could extend page 03 or 10, but it's distinct: throughput, not correctness.)
5. **Queue operations:** worker concurrency sizing, retention, age-of-oldest-job SLOs, Redis `noeviction`, workers as import side effects. buildevent incidents 002/005, M2.

## Existing learning-doc trees
- `docs/upskill/` (committed, ~3,350 lines, generic lab: cartography, katas, tickets): **KEEP** as background. Its ticket lists are superseded by `training/ladder`, and it asserts that the jobs run (they don't).
- `astraupskill/` (untracked, tied to the user's uncommitted idempotency/check-in change): **KEEP** as is. It covers the saturated idempotency/race skill, and the lab links to it instead of duplicating it.

## Caveats
- The laptop is slow: absolute numbers (≈10 to 12 reservations/s, a 1.3 s bcrypt compare) are not production estimates. Only same-machine comparisons are valid.
- Incident 004's harm to *reservations* did not reproduce on this laptop (reservations were not worse). Only the read-path latency and throughput regression did. This is stated in the answer.
- INC-002/005 production dashboards are narrative. The lab repro is real but scaled (a 4 MB Redis cap).
- Incident 003's motivation (double PaymentIntents) touches idempotency, but the lesson is the resource and pool. Curriculum 02 is linked, not re-taught.
- The node_modules install stays in the main tree (gitignored).
