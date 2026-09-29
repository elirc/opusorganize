# 14 — Load, back-pressure, timeouts, retries and bulkheads

**Problem.** Under a spike (a ticket drop, a retry storm, a slow dependency), systems fail *collectively*. One slow thing holds scarce resources
(DB connections, workers, event-loop time), and everything else queues behind it.

**The toolkit**
- **Admission control:** decide who gets in *before* taking scarce resources. Use a rate limit per identity and route (never one global limit that also blocks webhooks and scanners), a waiting room or queue, and a `429 + Retry-After`.
- **Timeouts on every outbound call,** set shorter than the caller's timeout. Library defaults are usually wrong (Stripe SDK 80 s, Anthropic SDK 10 min, Redis retry forever).
- **Retries:** only for idempotent operations, with exponential backoff + jitter, a small cap, and **retries at ONE layer**. SDK × app × queue retries multiply: 3 × 2 × 3 = 18 attempts.
- **Bulkheads:** separate pools per dependency or route class, so slow Stripe calls can't eat the connections that check-in needs.
- **Queue operations:** size worker concurrency to throughput, alert on **the age of the oldest job**, not just queue length, and never run BullMQ on a Redis with `allkeys-lru` (it needs `noeviction`).
- **Contention:** hot rows (a per-event counter) serialize everything. Shard counters, use atomic `UPDATE … WHERE remaining > 0`, and avoid Serializable where it only yields retries.

**Load testing honestly:** a real-shaped scenario (spike, not ramp), an SLO-based pass/fail, a warm-up, and numbers compared only against a baseline taken on the same machine.

**Worked examples in your repos**
- **buildevent** (the main lab):
  - 001 reserve retry storm: p95 3.6 → 14.3 s.
  - 002 Redis eviction killed the expiry-job schedule after about 1,000 cache writes.
  - 003 a slow Stripe exhausts the shared 5-connection pool, and check-in at another event fails (96 ms → 10 s).
  - 004 a hot-row lock halves availability throughput.
  - 005 QR backlog at concurrency 1.
  - Tools: `training/load/drop.k6.js` and `training/tools/drop-sim.mts`.
  - `main` itself: 40 concurrent reserves give 35 × 500 (Serializable + P2034).
- **buildermentor:**
  - `training/incidents/002-llm-retry-usage`: the invoice is 4× the ledger because of layered retries.
  - `005-genjob-expiry`: the queue timeout is not a kill switch, so one job produced 4 handler runs.
  - `ladder/M4`: one retry/timeout policy.
- **astraspacegameweb:**
  - `training/incidents/001-resolver-oldest-first`: silent contention.
  - `ladder/S2`: 1,000 arrivals/s.
  - `ladder/S3`: backlog catch-up.
- **gitjira-app:** `training/ladder/M3` (Redis as a soft dependency).
