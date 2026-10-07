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
- netintercom: `training/ladder/M2` and `incidents/003`. The batch-1 report also flagged "unique-violation handling + `ChangeTracker.Clear`" as a needed concept. The sealed `training/_answers/ladder-M2.md` (line 5) now covers it.
- modular-monolith-with-ddd: the inbox is keyed by an id that changes on republish (`training/navigation/04-*`).

**Where these repos live now.** netstripe → `elirc/dotnet-stripe` · netintercom → `elirc/dotnet-intercom` · modular-monolith-with-ddd → `elirc/netarchitectureproject` (`modular-monolith-with-ddd/` subfolder) · eShop (used below) → `elirc/netopen1` (`eShop/` subfolder). Re-read on 2026-10-06 at dotnet-stripe `8f40257`, dotnet-intercom `74e0a28`, netarchitectureproject `bf7fa14` and netopen1 `4bb1118`. Line numbers are for those commits. dotnet-stripe's two incident branches **are** on GitHub (`8b0c838`, `bfce8de`). dotnet-intercom's are not (see its `training/README.md`).

---

## Worked trace: dotnet-stripe's `IdempotencyMiddleware`

File: `elirc/dotnet-stripe: src/Billing.Api/Infrastructure/IdempotencyMiddleware.cs`. It is registered for every request (`Program.cs:35`), and its store is a singleton (`Program.cs:17`).

| Line(s) | What it does | Review-question answer |
|---|---|---|
| 11-15, 70-72 | Applies only to `POST/PUT/PATCH/DELETE` under `/api` | Scope: mutating API calls |
| 17-21 | **No `Idempotency-Key` header → just runs the request** | Opt-in. Callers that don't send a key get no protection |
| 24-29 | Key must be 8-200 chars | — |
| 32-33 | `requestHash` = SHA-256 of method+path+body. `cacheKey` = method+path+key | Scope is per endpoint, **not** per user or tenant (the app has no auth at all, see review finding 5) |
| 35-49 | Cache hit: different body → **409**, same body → replay the stored status and body with `Idempotency-Replayed: true` | Duplicate returns the original response |
| 51-61 | Buffers the response so it can be stored | — |
| 63-67 | Stores it **only if 2xx**, with TTL `IdempotencyTtlHours` (24, from `appsettings.json:7`) | Retention: 24 h, in process memory |
| 90-120 | `IdempotencyStore`: a `Dictionary` under a `lock`, purged lazily on read | Lost on restart, and not shared across replicas |

**Incident 001** is a one-line idea. Fetch the branch and diff it:

```
git fetch --depth 2 origin training/incidents/001-idempotency-caches-failures
git diff FETCH_HEAD~1 FETCH_HEAD -- src
```

The diff deletes the `is >= 200 and < 300` guard at lines 63-67, so a `400 "Invoice is already paid."` from `BillingEngine.QueuePayment` (`BillingEngine.cs:136-139`) is cached under the key for 24 h. When the provider later declines the payment and the invoice goes back to `Open` (`ApplyPaymentResult`, `BillingEngine.cs:165-167`), retries with the same key still replay the stale 400. The same commit also carries the two unrelated build fixes (a `using Billing.Api.Domain;` and a `(Money?)null` cast), because `main` doesn't compile (see [05](05-verify-before-trust.md)).

## The failure windows, step by step

**Window 1: two in-flight requests with the same key.**
1. Request A calls `store.TryGet` (line 35). It misses, and the lock is released.
2. Request B calls `store.TryGet`. It also misses, because A hasn't finished.
3. Both run `next(context)` (line 55). For `POST /api/invoices/{id}/pay`, both reach `QueuePayment`. The invoice is still `Open`, so the `Paid` check at `BillingEngine.cs:136` passes for both. Both save a `Payment` and enqueue a payment job (lines 152-153).
4. Both responses are 2xx, and both call `store.Set` (line 66). The last write wins.

The `lock` makes each dictionary call atomic, not the whole lookup → execute → store sequence. This is a check-then-act race ([03](03-concurrency-races.md)). A real fix reserves the key *before* running the handler: insert an "in progress" row under a unique constraint, and make a concurrent duplicate wait or get a 409.

**Window 2: webhook redelivery.** `POST /api/webhooks/payment-provider` (`Program.cs:223-250`) verifies the signature, deserializes `EventId` (declared at `Contracts/Requests.cs:34`), and calls `ApplyPaymentResult` without checking `EventId` anywhere. It only echoes it back on line 244. `ApplyPaymentResult` (`BillingEngine.cs:157-199`) has no status guard, so every redelivery adds a new `Payment` row and enqueues a new outbound webhook. Payment providers don't send `Idempotency-Key` headers, so the middleware doesn't help here either (lines 17-21).

**Window 3: process restart.** The store is a dictionary in process memory (line 93). After a deploy, every key is forgotten, and a client retrying across the deploy executes again.

## A second shape: eShop's request table

`elirc/netopen1: eShop/src/Ordering.Infrastructure/Idempotency/RequestManager.cs:21-37` checks `ExistAsync` and then inserts a `ClientRequest`. The id is the client's `x-requestid` header (`Ordering.API/Apis/OrdersApi.cs:23` and others). `ClientRequest.Id` is the entity key (`ClientRequest.cs:7`, mapped to table `requests` in `ClientRequestEntityTypeConfiguration.cs:8`), so the **database** backstops the race. The loser of two concurrent inserts gets a key violation instead of creating a second order. And the key is stable: the web app generates it once per checkout, not per click (`WebApp/Services/BasketState.cs:80-82`). Compare that with the next finding.

## Verified senior findings

- **dotnet-stripe's own frontend defeats its idempotency middleware.** `src/Billing.Web/src/api.ts:154` sends `"Idempotency-Key": newIdempotencyKey()` on *every* `postJson` call, and `newIdempotencyKey` (`api.ts:179-185`) returns a fresh `crypto.randomUUID()`. A user who clicks "Pay" again after a timeout sends a **new** key, so the server sees two different intents. The key has to be minted once per *user intent* (form load, checkout session) and reused on retry, which is what eShop's `BasketState.cs:80-82` does. Review question 2 ("is it stable across retries?") catches this in one read.
- **"Insert, catch, then re-read" needs a clean change tracker in EF.** After a `DbUpdateException` caused by a unique violation, the failed entities are still tracked. dotnet-intercom's sealed `training/_answers/ladder-M2.md` (line 5) walks through it: catch `PostgresException { SqlState: "23505" }`, call `ChangeTracker.Clear()`, re-query the winner, and return it. M2's own brief (`training/ladder/M2-idempotent-visitor-send.md`) hints at `PostgresErrorCodes.UniqueViolation`, so you can detect it without matching on message strings.

## Goal + Check ladder

**Goal:** for any endpoint or consumer, say who owns the key, what the DB enforces, and what a duplicate returns, then prove it with a test.

1. **Junior: answer the four review questions for `IdempotencyMiddleware.cs`** using only that file and `Program.cs`.
   **Check:** your answers match the table above (opt-in key, per method+path scope, 24 h in-memory, replay or 409).
2. **Junior: read incident 001 as a diff.** Run the two `git` commands above in a clone of `elirc/dotnet-stripe`.
   **Check:** exactly two files change, `IdempotencyMiddleware.cs` and `Program.cs`. Only the removed 2xx guard is the planted bug.
3. **Mid: name the concurrent-duplicate window** for `POST /api/invoices/{id}/pay` with one shared key.
   **Check:** you cite `IdempotencyMiddleware.cs:35` / `:55` / `:66` and `BillingEngine.cs:136`. *Run locally* (after the [04](04-characterization-tests.md) test project exists and the two build fixes are applied): fire two `Task.WhenAll` requests with the same key. Based on the code, expect two `Payment` rows for the invoice, not one.
4. **Mid: design webhook dedup.** Where would `EventId` be recorded, and what does a duplicate return?
   **Check:** your design records `EventId` under a uniqueness guarantee *in the same atomic step* as `ApplyPaymentResult`'s state change, and returns 200 to a duplicate so the provider stops retrying. Compare with sealed `training/_answers/review.md` finding 2.
5. **Mid→senior: dotnet-intercom M2.** Do the ticket, including the concurrent-duplicate test against Testcontainers Postgres.
   **Check:** the constraint is enforced by PostgreSQL, the legacy no-key path still works, and you can explain why `(VisitorId, ClientMessageId)` handles the "first message creates the conversation" case.

## Debugging scenario

*Support: "A customer clicked Pay twice on a slow connection and we see two pending payments for one invoice. The dashboard sends idempotency keys, so how?"*

1. Check whether both requests carried the same key. With `api.ts:154`, they didn't, because each click mints a new UUID. Under per-intent keys this would be impossible, so the client is the first suspect.
2. Even with the same key, ask whether the requests overlapped. If so, window 1 applies: both missed the cache before either stored.
3. Check whether a provider webhook arrived twice. `EventId` is never deduplicated (window 2), so look for two `provider-webhook` payments (`BillingEngine.cs:175`) with the same `providerReference`.
4. Fix in order: a per-intent key in the client, then a reserve-before-execute key store backed by a unique constraint, then `EventId` dedup on the webhook.
