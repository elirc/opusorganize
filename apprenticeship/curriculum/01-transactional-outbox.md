# 01 — Transactional outbox & its failure windows

**Problem.** You must change the DB *and* tell another component (a queue, module or service). That is two writes with no shared transaction, so one can succeed while the other fails.

**The pattern.** Write the business change and an `OutboxMessage` row in **one** DB transaction. A separate dispatcher reads unsent rows, publishes them, then marks them sent.

**What it guarantees, and what it doesn't**
- Guarantees: no event is *lost* if the business write committed, because it is durable in the outbox.
- Not exactly-once: if the dispatcher crashes between *publish* and *mark sent*, it re-publishes. Delivery is **at-least-once**, so consumers must be idempotent (→ [02](02-idempotency.md)).
- No automatic retries: rows stuck in a failed state need a sweeper/backoff/DLQ policy.
- Ordering is only as good as the dispatcher's query: use `ORDER BY` with a single dispatcher, or a partition key.

**Failure-window checklist (use in every review)**
1. Is the outbox row written in the *same* transaction as the state change?
2. What happens if the process dies after publish but before mark-sent? Is the message id **stable** across republishes?
3. What retries stranded rows? What alerts when the backlog grows?
4. With several dispatcher replicas, use `FOR UPDATE SKIP LOCKED` or a lease; otherwise messages are published twice.

**Worked examples in your repos**
- eShop: `training/navigation/01-checkout-outbox-correctness.md` and `03-outbox-sweeper-tradeoff.md`. Nothing retries stranded `PublishedFailed` rows.
- modular-monolith-with-ddd: `training/navigation/04-outbox-inbox-processing.md`. Each republish creates a **new Guid**, which defeats the inbox dedup and produces a duplicate `MeetingFee`.
- netdrop: the upload commits to the DB, then enqueues the scan on an in-memory channel. A crash in between means the file is never scanned. See `training/incidents/002-scan-backlog` and `training/ladder/S1` (a durable pipeline).
- netintercom: `training/ladder/S3` (design one yourself) and `training/incidents/003` (duplicate escalations across replicas).

Interview framing: "at-least-once delivery plus an idempotent consumer gives effectively-once." Be ready to name the exact crash window.
