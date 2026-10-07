# 14 — Load, back-pressure, timeouts, retries and bulkheads

**Where these repos live now (checked 2026-10-06):** buildevent → `elirc/build-event` (`main` @ `b941e78`; the five incident branches are **not** on GitHub) · buildermentor → `elirc/buildermentor` (`main` @ `8fcdb9d`; all five incident branches are on GitHub) · astraspacegameweb → `elirc/astraspacegameweb` (`main` @ `736b75f`; incident branches on GitHub) · gitjira-app → `elirc/gitjira` (`main` @ `42abd2c`).

**Problem.** Under a spike (a ticket drop, a retry storm, a slow dependency), systems fail *collectively*. One slow thing holds scarce resources
(DB connections, workers, event-loop time), and everything else queues behind it.

**The toolkit**
- **Admission control:** decide who gets in *before* taking scarce resources. Use a rate limit per identity and route (never one global limit that also blocks webhooks and scanners), a waiting room or queue, and a `429 + Retry-After`.
- **Timeouts on every outbound call,** set shorter than the caller's timeout. Library defaults are usually wrong. The commonly cited defaults are the Stripe SDK at 80 s and the Anthropic SDK at 10 min, and an ioredis client with `maxRetriesPerRequest: null` retries forever. (The SDK numbers are from the libraries' own docs. The repos below simply don't override them.)
- **Retries:** only for idempotent operations, with exponential backoff + jitter, a small cap, and **retries at ONE layer**. SDK × app × queue retries multiply: 3 × 2 × 3 = 18 attempts.
- **Bulkheads:** separate pools per dependency or route class, so slow Stripe calls can't eat the connections that check-in needs.
- **Queue operations:** size worker concurrency to throughput, alert on **the age of the oldest job**, not just queue length, and never run BullMQ on a Redis with `allkeys-lru` (it needs `noeviction`).
- **Contention:** hot rows (a per-event counter) serialize everything. Shard counters, use atomic `UPDATE … WHERE remaining > 0`, and avoid Serializable where it only yields retries.

**Load testing honestly:** a real-shaped scenario (spike, not ramp), an SLO-based pass/fail, a warm-up, and numbers compared only against a baseline taken on the same machine.

**Worked examples in your repos** (buildevent numbers were measured on one slow laptop on 2026-09-24 and recorded in `batch4report/projects/buildevent.md` and the training briefs. They are relative, not absolute.)
- **buildevent** (the main lab):
  - 001 reserve retry storm: p95 3.6 → 14.3 s.
  - 002 Redis eviction killed the expiry-job schedule after about 1,000 cache writes.
  - 003 a slow fake Stripe exhausts the shared 5-connection pool: unrelated reads go from p95 96 ms to 10 s, and P2024 pool timeouts hit every route, including door check-in.
  - 004 a hot-row lock cuts availability throughput to about a third (972 → 334 req/s; p50 47 → 167 ms). *(Corrected 2026-10-06: an earlier version said "halves".)*
  - 005 QR backlog at concurrency 1.
  - Tools: `training/load/drop.k6.js` (a skeleton, never run: k6 wasn't installed) and `training/tools/drop-sim.mts`.
  - `main` itself: 40 concurrent reserves give 35 × 500 (Serializable + P2034).
- **buildermentor:**
  - `training/incidents/002-llm-retry-usage`: the invoice is about 4× the ledger because of layered retries.
  - `005-genjob-expiry`: the queue timeout is not a kill switch, so one job produced 4 handler runs.
  - `ladder/M4`: one retry/timeout policy.
- **astraspacegameweb:**
  - `training/incidents/001-resolver-oldest-first`: silent contention.
  - `ladder/S2`: 1,000 arrivals/s.
  - `ladder/S3`: backlog catch-up.
- **gitjira-app:** `training/ladder/M3-redis-soft-dependency.md` (Redis as a soft dependency).

---

## Worked trace: one `POST /orders/reserve` on buildevent `main` (`b941e78`)

1. **Route.** `apps/api/src/routes/order.routes.ts:14-15` parses the body and calls `reservationService.reserveTickets`.
2. **A UX guard outside the transaction.** `apps/api/src/services/reservation.service.ts:16-30` refuses a second pending checkout for the same user and event. It is check-then-act (two tabs can race), so it's a UX guard, not a correctness guard. See [03](03-concurrency-races.md).
3. **App-level retry loop.** `:32-42` tries up to `maxRetryAttempts = 5` (`:7`), sleeping `Math.random() * 100 * (attempt + 1)` ms, but **only** for `OptimisticLockError`.
4. **The transaction.** `:52-131` is an interactive Prisma transaction at `Serializable` isolation (`:131`). Inside it: read the tier (`:64`), compute `available` (`:77`), and do a version-checked `updateMany` (`:88-96`).
5. **A second hot spot.** `:111` calls `generateOrderNumber`, which is `tx.order.count()` + 1 (`apps/api/src/services/order-number.ts:6-8`). Every reservation reads the whole `Order` table inside a Serializable transaction.
6. **Shared resources.** One Prisma pool serves every route (the incident 003 log shows `connection limit: 5`). One global rate limit, `max: 100, timeWindow: '1 minute'` (`apps/api/src/server.ts:35`), covers buyers, webhooks and scanners alike.

## Failure mode, step by step: from 35 × 500 to the retry storm (INC-001)

1. Forty buyers hit the same tier. Under Serializable, Postgres aborts most of the concurrent transactions with `could not serialize access due to concurrent update` (the lab saw 750 of them, `training/_answers/ladder-M1.md`).
2. Prisma surfaces that as **P2034**. The loop at `:36` catches only `OptimisticLockError`, so P2034 becomes a 500. Result on `main`: 5 ok, 35 × 500, with 145 tickets still unsold.
3. PR #61 (quoted in `training/incidents/001-reserve-retry-storm.md`) "fixes" it: 20 attempts, a fixed 10 ms delay with no jitter, and P2034 now counts as retryable.
4. Every retry is a new Serializable transaction that conflicts with the others. Attempts per success grow with concurrency, and DB CPU sits near 100%.
5. Each attempt holds a pool connection, so callers queue for connections. Prisma's `maxWait` (2 s by default, per the M1 answer) turns that into **P2028**. With 200 buyers: 175 × P2028, 25 ok.
6. p95 goes from 3.6 s to 14.3 s. The 500s are gone, but the system is slower *and* still fails most buyers.

The M1 sealed answer recommends a single conditional `UPDATE`, a sequence-based order number, an in-process admission cap below the pool size, and P2034/P2028 mapped to 503 + `Retry-After` as a safety net. That measured 0 × 5xx at both 40 and 200 buyers. The DoD's "503 p95 < 1.5 s" target was **not** met (the 503s arrived after the 5 s queue wait), and the answer says so.

## Goal + **Check** ladder

1. **Goal (junior):** find every unbounded outbound call. **Check:** `elirc/build-event: apps/api/src/plugins/stripe.ts:6-8` constructs Stripe with no `timeout` or `maxNetworkRetries`. `apps/api/src/plugins/redis.ts:7` and `apps/api/src/jobs/redis-connection.ts:9` set `maxRetriesPerRequest: null`. List each one, with the value you'd pick and why.
2. **Goal (junior):** spot the queue-killer config. **Check:** `docker-compose.yml:17` runs Redis with `--maxmemory-policy allkeys-lru`. BullMQ needs `noeviction`. Explain how incident 002 lost the `order-expiry` repeatable job (the B04 run saw repeatables go from 1 to 0).
3. **Goal (junior → mid):** count the retry layers in buildermentor. **Check:** `elirc/buildermentor: apps/api/src/llm/providers/anthropic.ts:9` builds the SDK client with no `maxRetries` or `timeout` override (layer 1). `apps/api/src/llm/callLlm.ts:117` loops `attempt < 2` for schema repair (layer 2). `apps/api/src/jobs/boss.ts:31` sets `retryLimit: 3` on queued jobs (layer 3). Multiply them, then write the M4 policy that keeps retries at one layer.
4. **Goal (mid):** explain why a queue timeout isn't a kill switch. **Check:** the INC-005 sealed answer's repro line reads `runs=4 inserts=4 maxConcurrentForOneJob=2` with the final state `failed`. The handler kept running after pg-boss expired it, so a retry overlapped it. Name the missing piece (an `AbortSignal` plumbed into the handler).
5. **Goal (mid → senior):** design S3's timeout budget for buildevent. **Check:** each hop's timeout is shorter than its caller's, Stripe calls get their own pool or concurrency limit (a bulkhead), and you can say which routes degrade first.

## Verified senior findings

- **Isolation level changes the failure mode, not just the speed.** The M1 answer explains that at READ COMMITTED the version-checked `updateMany` would *wait* for the row lock, match 0 rows, and take the designed `OptimisticLockError` path. At Serializable it aborts with P2034 instead, which the retry loop doesn't catch. The README's "optimistic locking with retries" claim was true of the code's intent, not of its behaviour (B04 report).
- **The cost ledger hides retries.** buildermentor INC-002's sealed answer ranks the causes: the PR overwrote `usage` per attempt instead of summing it, escalated `max_tokens`, and pg-boss `retryLimit: 3` multiplied the whole thing (up to 16 billed attempts per topic-modality). On `main` today, `callLlm.ts:128` sums usage across attempts, which is the fixed shape.

## Debugging scenario: "every route got slow, and only checkout changed"

(1) Look for errors that name a shared resource rather than a route: `P2024 Timed out fetching a new connection … connection limit: 5` on `GET /events`, check-in and webhooks (INC-003's log). (2) Find what holds connections longest. In INC-003, a Stripe call made inside the DB transaction holds a connection for the whole Stripe latency. (3) Do the arithmetic the brief asks for: with Stripe at p50 1.5 s and 5 connections, checkout throughput is capped at a few per second per instance, and every other route waits behind it. (4) Fix by moving the external call out of the transaction and giving it a bulkhead. Then re-run `drop-sim.mts checkout` against the same baseline.

**Honesty cap:** buildevent's incident branches were never pushed, so the briefs' quoted diffs are the only public form of the bugs. The k6 skeleton has never run. INC-002/005's "production dashboard" figures are labelled narrative in the training README, and only the scaled lab repros are real. I re-read the code paths above at `b941e78` and `8fcdb9d` on 2026-10-06 and ran nothing.
