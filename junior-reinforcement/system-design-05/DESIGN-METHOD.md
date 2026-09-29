# A worked method for system design

Use this guide with one of the [ten project cases](README.md). The goal is to explain how a bounded user operation remains correct through load, concurrency, and failure. A small design with a precise recovery story is more useful than a large diagram whose arrows hide the hard decisions.

## 1. Turn a feature into a contract

Start with a person doing one thing. For BuildEvent, a buyer asks for the last ticket. For aaa1, an operator submits an import and expects truthful row outcomes. For RouteIQ, a driver reconnects with an offline delivery command. These journeys are specific enough to identify input, authority, acceptance, and recovery.

Write three functional requirements and two non-goals. Then write an invariant that can be violated by a concrete example: accepted holds must not exceed capacity; one logical row must not create two untracked lead effects; an older stop command must not silently overwrite a newer accepted revision. Avoid substituting vague goals such as reliable or scalable for these rules.

Separate requirements from assumptions. Active users, requests per minute, average payload size, acceptable staleness, and recovery objectives are inputs to discuss. If the repository has no measured production workload, label your numbers hypothetical. Do not borrow a historical local test and relabel it as a current production capacity result.

## 2. Find the authority before choosing infrastructure

A local draft belongs to the user's current interaction. An accepted shared record belongs to its authoritative operation. A cache, search index, browser query, or notification may represent that record without owning the final decision. Draw these separately.

For each operation, ask which component has enough trusted information to accept or reject it. A browser countdown cannot authorize a ticket hold. A hidden button cannot enforce a server capability. A worker's selection query does not alone claim an event. A model-generated source ID does not authorize access to the referenced document.

The API should return outcomes that let callers act correctly. Distinguish success, empty success, invalid input, unauthorized scope, conflict, unavailable dependency, and uncertain completion when the contract needs them. A timeout after a commit is not a confirmed rollback. An asynchronous receipt is not the authority for whether an application was accepted.

## 3. Sketch keys and relationships with the request path

List the authoritative entities, their keys, and which operation can change them. Include organization or owner scope where it changes meaning. Distinguish a record ID from the identity of one logical command. A command may be delivered repeatedly while representing the same intent.

For a proposed API, show one literal request and response, then an edge case. Explain missing versus null, zero versus absent, a stale version, and a forbidden field as applicable. An unchecked type assertion does not validate an external payload. Construct an accepted shape instead of letting a generic object merge decide which fields are writable.

Choose an index from a specific predicate and order. An index has storage and write costs; it is not a free improvement for every query. A uniqueness rule enforces a different property from a fast lookup. Review both with the actual schema. PostgreSQL's constraint documentation describes the supported constraint boundaries and limitations; it does not replace a concurrency proof for a multi-step workflow. [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html).

## 4. Work one concurrent schedule by hand

Example: editors A and B both read revision4. A conditionally writes against4 and commits revision5. B's later conditional write against4 must reject. If the code instead checks4 in a separate read and later performs an unconditional write, both callers can pass the early check. Put the condition at the actual authority boundary.

Do not treat the word transaction as a complete isolation argument. PostgreSQL's default Read Committed level gives an ordinary SELECT a statement-level view; two statements in one transaction can observe intervening commits. Choose and test the mechanism needed by the invariant, including conflict/serialization retry behavior where relevant. [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html).

Name the failed attempt's result and its retry identity. A retry after rollback may legitimately perform the operation. A replay after successful commit should recover the recorded result under an idempotency contract. A reused identity with a different payload needs an explicit conflict policy. Receipt retention changes how long that guarantee can be offered.

## 5. Treat every asynchronous arrow as a failure window

Draw these separately: select work, claim ownership, apply an effect, commit, publish, and acknowledge. If the process exits after any step, what can a replacement observe? Which identity connects the replacement to the same logical work?

An outbox is one way to persist business changes and delivery intent together, then let another process deliver the intent. It addresses the database/message dual-write window; consumers can still see repeats and need an appropriate idempotent handling policy. It does not make an external provider effect part of the local transaction. [Transactional outbox guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html).

For leases, include a generation or equivalent ownership check when an old worker can finish after replacement. A lease expiring does not stop the old process from running. For notifications, decide whether the message is authoritative data, a replayable event, or a hint to fetch a current snapshot. Each choice has different ordering and reconnect obligations.

## 6. Give caches and replicas a bounded job

A cache key states which requests can share one representation. Store, locale, currency, owner, query, and version matter only where they affect that representation or its safe sharing scope. Normalize fields according to their semantics. Lowercasing an opaque store ID can merge distinct identities.

Freshness is an endpoint contract. A public catalog view may tolerate an explicit stale interval, while reservation admission consults authoritative inventory. A replica can serve permitted stale reads but may complicate immediate read-after-write behavior. State which request uses which source and what the user sees during lag.

Work the late-fill race: load begins, write commits, invalidation occurs, old load completes. Deleting a key does not cancel an outstanding loader. If a generation policy is used, explain where comparison and fill are coordinated. A process-local promise gate reduces duplicate work inside its own process; it does not automatically coordinate several servers.

## 7. Reproduce a capacity estimate and break it

Suppose a queue has900 existing jobs, ongoing arrivals of40 jobs/s, and ideal service capacity of45 jobs/s. Only5 jobs/s reduce the backlog, so the ideal drain time is180 seconds. At45 arrivals/s there is no positive drain rate. Reporting20 seconds from900/45 would ignore continuing arrivals.

Now add a slow downstream dependency, retries, a hot tenant, or a serial ordering constraint. Decide which assumption fails. More workers help only if useful work can run in parallel and downstream capacity permits it. A queue absorbs a temporary burst; it cannot hide sustained overload forever. Define admission, backpressure, and a truthful user outcome when the budget is exhausted.

For reads, compare warm and cold cache conditions. Bazaar's worksheet uses1000 eligible reads/s: a95 percent hit rate yields50 origin reads/s, while a cold cache yields1000. This is arithmetic, not a database benchmark. It suggests a load/recovery case to measure before promising capacity.

Use query plans on representative data to examine the likely bottleneck. EXPLAIN ANALYZE actually executes the statement, so inspect the operation and environment before using it for writes. The plan must be interpreted with the query, data distribution, and measured execution context. [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html).

## 8. Keep deployment boundaries separate from code organization

A module boundary can clarify ownership without requiring a network service. Helios's repair invariant benefits from a clear transaction across participating writes. Splitting those writes across services changes the consistency and recovery problem; it is not a purely organizational refactor.

A separate service can be justified by independently measured load, ownership, deployment, or isolation requirements. Explain its API, failure behavior, data authority, and operating cost. For sharding or partitioning, name the key and the operations that cross it. For a hot single record, adding partitions elsewhere may not relieve the decisive contention.

Prefer a reversible first step when evidence is incomplete: characterize a query, bound a batch, add a clear contract, or separate a module before distributing it. The architecture should evolve from an observed constraint rather than from a list of fashionable components.

## 9. Design recovery, observability, and privacy together

Pick signals that correspond to meaningful boundaries. HTTP availability, worker progress, and correct domain outcomes are different. Warband's pending-event count and oldest-overdue age complement completed-resolution metrics. A graph of completed work can stop changing when no work completes; that is not automatically a reassuring state.

Define a hypothetical availability/latency objective for a specific operation, not the entire diagram. State what the measurement includes and how failures are counted. A30-day99.9 percent time-based availability target permits43.2 minutes of unavailability under that simplified definition. It is not automatically the same as a request-based success objective or a guarantee the project currently meets.

For recovery, state RPO as the tolerated loss window and RTO as time to useful restored service. Then rehearse a restore and reconcile delayed events, receipts, and external effects against restored state. Backups that have never been restored are incomplete evidence of recovery. Read models may be rebuilt differently from authoritative records.

Keep sensitive data out of routine metrics and unnecessary logs. Authorization also affects cache scope, exports, search indexes, stored generated content, and deletion propagation. A field hidden in a component may still be exposed in a raw response or diagnostic artifact.

## 10. Finish with a decision and a proof plan

A useful decision record states context, invariant, chosen boundary, rejected alternative, accepted cost, and revisit trigger. A useful interview answer walks a successful request, one failed or competing request, one calculation with units, and one limitation. A useful implementation plan names the smallest test that would reject the plausible wrong design.

Keep source observations, proposed design, calculated examples, historical tests, and newly executed checks visibly separate. A learner can explain a studied design honestly without claiming ownership of all existing code or inventing production impact. Use the project journal to preserve the assumption that changed, then try a second design with one requirement altered.
