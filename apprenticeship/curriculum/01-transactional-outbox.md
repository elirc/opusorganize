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

**Where these repos live now.** The Desktop folders above are gone. eShop → `elirc/netopen1` (`eShop/` subfolder) · modular-monolith-with-ddd → `elirc/netarchitectureproject` (`modular-monolith-with-ddd/` subfolder) · netdrop → `elirc/dotnet-drop` · netintercom → `elirc/dotnet-intercom`. I checked each mapping by finding the cited `training/` file in the repo. Everything below was re-read on 2026-10-06 at netopen1 `4bb1118`, netarchitectureproject `bf7fa14`, dotnet-drop `d7ae725` and dotnet-intercom `74e0a28`. Line numbers are for those commits.

> **Incident branches.** The netdrop and netintercom `training/incidents/*` branches were never pushed: `git ls-remote origin` on both repos lists only `main`. Each repo's `training/README.md` says so and explains how to work the incidents from the briefs.

---

## Worked trace: eShop checkout, one line at a time

The question to ask of every line: what has committed by this point, and what is only in memory?

1. **The command opens a transaction.** `elirc/netopen1: eShop/src/Ordering.API/Application/Behaviors/TransactionBehavior.cs:38` calls `BeginTransactionAsync()`. Line 43 runs `next()`, which is the whole command handler chain.
2. **The handler writes the outbox row inside that transaction.** `eShop/src/Ordering.API/Application/Commands/CreateOrderCommandHandler.cs:32-33` builds an `OrderStartedIntegrationEvent` and calls `AddAndSaveEventAsync`. That goes to `OrderingIntegrationEventService.cs:40`, which passes `_orderingContext.GetCurrentTransaction()` to the event log. `eShop/src/IntegrationEventLogEF/Services/IntegrationEventLogService.cs:38-43` creates an `IntegrationEventLogEntry` tagged with that transaction id, enlists in the *same* DB transaction (`UseTransaction`, line 40), and saves. Six domain-event handlers do the same thing (grep `AddAndSaveEventAsync` under `Ordering.API/Application/DomainEventHandlers/`).
3. **Commit.** `TransactionBehavior.cs:47` commits. From here on, the order and its outbox rows (state `NotPublished`, see `EventStateEnum.cs:5`) are durable together. This is the half the pattern gets right.
4. **Publish, in the same request, after commit.** `TransactionBehavior.cs:52` calls `PublishEventsThroughEventBusAsync(transactionId)`. `OrderingIntegrationEventService.cs:15` loads pending rows. `IntegrationEventLogService.cs:19-23` filters on `TransactionId == transactionId && State == NotPublished`, so it only sees **this request's** rows.
5. **Per event:** mark `InProgress` (line 23, which also increments `TimesSent` at `IntegrationEventLogService.cs:66-67`), `PublishAsync` to RabbitMQ (line 24), then mark `Published` (line 25).
6. **On any exception:** `catch` at lines 27-32 logs, marks the row `PublishedFailed`, and **does not rethrow**. The HTTP caller already has a committed order and gets a success response.

## The failure windows, step by step

| Crash or failure at… | What's durable | What happens next |
|---|---|---|
| Before step 3 (commit) | nothing | The whole transaction rolls back and the client retries. Safe, as long as the client resends the same `x-requestid` (see [02](02-idempotency.md)). |
| **Between step 3 and step 4** (process killed, pod evicted) | order + rows in `NotPublished` | The only reader is step 4's query, which is scoped to one transaction id and runs only inside the request that created it. **Nothing ever reads these rows again.** The event is never delivered. |
| Between `PublishAsync` (24) and `MarkEventAsPublished` (25) | rows in `InProgress`; RabbitMQ *has* the message | No sweeper, so the message isn't duplicated today. But a future sweeper can't tell "in flight" from "already sent" by looking at an `InProgress` row, so it must republish, and the consumer must be idempotent. |
| `PublishAsync` throws (broker blip) | rows in `PublishedFailed` | The exception is swallowed (27-32). Nothing reads `PublishedFailed`. The order sits in its first status forever. |

How to confirm "nothing reads them". Run `grep -rn "PublishedFailed" eShop/src --include=*.cs`. It returns exactly two lines: the enum (`EventStateEnum.cs:8`) and the setter (`IntegrationEventLogService.cs:58`). `grep -rln "BackgroundService" eShop/src --include=*.cs` returns two files, `OrderProcessor/Services/GracePeriodManagerService.cs` and `Shared/MigrateDbContextExtensions.cs`, and neither touches the event log. This is the same finding as `training/navigation/01-checkout-outbox-correctness.md` row 4, which was written against baseline `9b4f943` on 2026-09-23. It still holds at `4bb1118`.

**What this is called:** a *transactional outbox without a relay*. The write side is correct. The read side is a best-effort publish that runs once.

## The second repo: when the outbox works but the id isn't stable

modular-monolith-with-ddd has a real relay: a Quartz job polls the outbox. Its gap is one hop further downstream.

- `elirc/netarchitectureproject: modular-monolith-with-ddd/src/Modules/Meetings/Infrastructure/Configuration/Processing/Outbox/ProcessOutboxCommandHandler.cs:35-43` selects rows `WHERE ProcessedDate IS NULL ORDER BY OccurredOn`. Line 62 publishes and lines 64-68 set `ProcessedDate`. These are two separate statements. A crash between them means a republish, which is at-least-once as designed.
- The republished domain notification reaches `.../Meetings/Application/Meetings/SendMeetingAttendeeAddedEmail/MeetingAttendeeAddedPublishEventNotificationHandler.cs:18-19`, which builds the integration event with **`Guid.NewGuid()`** as its id.
- Payments' `.../Payments/Infrastructure/Configuration/EventsBus/IntegrationEventGenericHandler.cs:25-34` inserts `@event.Id` into `[payments].[InboxMessages]`, where `Id` is the only key.

The republish carries a fresh Guid, so the inbox primary key sees a *new* message and accepts it. The inbox only deduplicates if the id is derived from something stable, such as the outbox row id. This is checklist question 2 in practice.

## Goal + Check ladder

**Goal:** given any "DB write + notify" code path, name every crash window and say what recovers each one.

1. **Junior: find the two writes.** In `elirc/dotnet-drop`, open `src/NetDropbox.Application/Uploads/CompleteUpload.cs`.
   **Check:** you point to line 85 (`SaveChangesAsync`) and line 87 (`queue.EnqueueAsync`), and to `src/NetDropbox.Infrastructure/Processing/ChannelProcessingQueue.cs:8`, where the queue is `Channel.CreateUnbounded` (in-process memory). Note: `training/ladder/S1-durable-processing.md` cites `CompleteUpload.cs:82-84`. At `d7ae725` the same pair sits at 85/87.
2. **Junior+: prove nothing recovers the gap.** `grep -rn "ProcessingJobs" src --include=*.cs` in dotnet-drop.
   **Check:** the only hits are the `DbSet` declarations, the `Add` at `CompleteUpload.cs:81`, and `ProcessingWorker.cs:32`, which loads a job *by the id carried in the channel message*. No code queries for `Queued` rows. So a restart between lines 85 and 87 strands that `processing_jobs` row and leaves the file `Pending`. This is also the answer shape for INC-002 task 5.
3. **Mid: fill in the eShop table above from memory**, then compare it with `training/navigation/01-checkout-outbox-correctness.md`.
   **Check:** your table has the commit→publish window and the swallowed-exception window, each with its line number.
4. **Mid: spot the unstable id.** Without reading this page's previous section, trace a republished outbox row in modular-monolith-with-ddd to the Payments inbox.
   **Check:** you land on `Guid.NewGuid()` at `MeetingAttendeeAddedPublishEventNotificationHandler.cs:19` and can explain why the inbox PK doesn't catch the duplicate.
5. **Mid→senior: design the relay.** Do dotnet-intercom `training/ladder/S3-sla-escalation-pipeline.md`, or dotnet-drop `training/ladder/S1-durable-processing.md`, then open the sealed `_answers/ladder-S*.md`.
   **Check:** your design states the claim mechanism (`FOR UPDATE SKIP LOCKED` or a lease), what happens to an `InProgress` row after a crash, the stable message id, and the alert on oldest-pending age.

## Verified senior findings

- **eShop's outbox reader is scoped to one transaction.** `RetrieveEventLogsPendingToPublishAsync(Guid transactionId)` (`IntegrationEventLogService.cs:19`) is the only read API on `IIntegrationEventLogService` (`IIntegrationEventLogService.cs:5`). So adding a sweeper isn't just a new `BackgroundService`: the interface needs an unscoped "stale rows" query. `training/navigation/03-outbox-sweeper-tradeoff.md` option B makes the same point.
- **"Marking sent" is a separate `SaveChangesAsync`.** `UpdateEventStatus` (`IntegrationEventLogService.cs:61-70`) saves after each state change. If the DB is unavailable when the catch block calls `MarkEventAsFailedAsync`, that call throws out of the `catch`. `TransactionBehavior.cs:57-61` then logs and rethrows, so the client sees an error *for an order that committed*. (This is inferred from reading the code. I haven't run it.)

## Debugging scenario

*"Orders placed during Tuesday's RabbitMQ restart are stuck in `Submitted`. No errors in the API's 5xx dashboard."*

1. Where to look first: the integration-event log table, grouped by `State`. Expect rows in `PublishedFailed` (broker threw), and possibly `NotPublished` (pod died after commit), with `CreationTime` inside the restart window.
2. Why no 5xx: the catch at `OrderingIntegrationEventService.cs:27-32` swallows the publish error. The only trace is the `LogError` "Error publishing integration event" line, so search the logs for it.
3. Why they don't self-heal: nothing reads those states (the greps above).
4. Fix now: republish those rows once, by hand. That is safe only because consumers guard on status (`training/navigation/01-*` row 6 explains how far that guard goes). Fix properly: build a sweeper with a claim step and an alert on the oldest pending row's age (`03-outbox-sweeper-tradeoff.md`).
