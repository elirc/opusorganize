# 02 — Idempotency keys & duplicate delivery

**Problem.** Retries deliver the *same intent* more than once. They come from clients, the network, queue redelivery, webhook resends and outbox republishes.

**Tools, strongest first**
1. **DB uniqueness** on a natural or client-supplied key (`UNIQUE(tenant_id, idempotency_key)`). Insert, then catch the unique violation (Postgres `23505`). Don't check-then-insert, which races (see [03](03-concurrency-races.md)).
2. **An idempotency-key store** for APIs, mapping key → stored response. Only cache **terminal success** (or errors that are explicitly final). Caching transient failures blocks legitimate retries.
3. **An inbox/processed-message table** for consumers, keyed by a **stable message id** that survives republishing.
4. **Set-based idempotent operations** (`UPDATE … WHERE status='Open'`), so a second run is a no-op.

**Review questions**
- What is the key, and who generates it?
- Is it stable across retries?
- What is its scope (tenant, user, endpoint), and how long is it retained?
- What does a duplicate return: the same response, a 409, or a 200 no-op?

**Worked examples in your repos**
- netstripe:
  - `training/incidents/001-idempotency-caches-failures.md`: the middleware caches a 400, so retries keep replaying "already paid".
  - A review finding: the webhook `EventId` is parsed but never deduplicated.
- netintercom: `training/ladder/M2`, `incidents/003`, and the curriculum need "unique-violation handling + `ChangeTracker.Clear`".
- modular-monolith-with-ddd: the inbox is keyed by an id that changes on republish (`training/navigation/04-*`).
