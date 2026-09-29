# Central curriculum (single home for concept pages)

Rule: a concept gets a page here only when ≥2 projects' exercises need it. Pages are short and point at **worked examples in your own repos**
(the exercises are where learning happens). Projects link here instead of re-explaining.

| # | Page | Worked examples (B01) |
|---|---|---|
| 01 | [Transactional outbox & failure windows](01-transactional-outbox.md) | eShop, modular-monolith-with-ddd, netintercom |
| 02 | [Idempotency keys & duplicate delivery](02-idempotency.md) | netstripe, netintercom, modular-monolith-with-ddd |
| 03 | [Check-then-act races & optimistic concurrency](03-concurrency-races.md) | netintercom, netstripe, netramp |
| 04 | [Characterization tests for untested code](04-characterization-tests.md) | netramp, netstripe |
| 05 | [Verifying code you didn't write (AI or human)](05-verify-before-trust.md) | netstripe, netramp, netintercom, netauth |
| 06 | [Caching correctness: the four ways a cache lies](06-caching-correctness.md) | bazaar, pulse, netintercom |
| 07 | [Zero-downtime schema changes (expand/contract)](07-zero-downtime-migrations.md) | gitjira-app, netdrop, atlas |
| 08 | [Realtime fan-out across instances](08-realtime-fanout.md) | gitjira-app, netintercom |
| 09 | [Telemetry you can trust](09-telemetry-correctness.md) | atlas, gitjira-app, pulse, netintercom |
| 10 | [Diagnosing slow queries: plans, indexes, N+1](10-query-plans-and-indexes.md) | atlas, netdrop, netintercom, gitjira-app, pulse |
| 11 | [Accessibility that actually works](11-accessibility-essentials.md) | lucasrouter, outline, perch |
| 12 | [Measuring and fixing frontend performance](12-frontend-performance.md) | lucasrouter, perch, gitjira-app |
| 13 | [Release safety: health checks, reproducible artifacts, rollback](13-release-safety.md) | astraspacegameweb, gitjira-app, atlas |
| 14 | [Load, back-pressure, timeouts, retries, bulkheads](14-load-backpressure-timeouts.md) | buildevent, buildermentor, astraspacegameweb, gitjira-app |
| 15 | [Shipping LLM features: evals, cost, latency, injection, agent safety](15-llm-features-in-production.md) | buildermentor, aicallhelper, aiheartbeat |
| 16 | [Sagas vs 2PC vs outbox](16-sagas-vs-2pc-vs-outbox.md) | astra5, relay, eShop, modular-monolith-with-ddd, atlas |
| 17 | [CRDTs & offline sync](17-crdt-offline-sync.md) | folio, Outline, buildwhiteboard |
| 18 | [Durable execution: checkpoints, determinism, leases, timers](18-durable-execution.md) | relay, buildermentor, atlas, buildevent |
| 19 | [Database-enforced isolation: RLS & tenant-safe keys](19-rls-defense-in-depth.md) | grokbuildmultitenantproject, HNJOBTRACK, aaa1 |
| 20 | [Money and time in business code](20-money-and-time.md) | vg, globehire, netstripe, atlas |
| 21 | [Legacy rescue and ports](21-legacy-rescue-and-ports.md) | VGdemo, grokbuildmultitenantproject, vg, HNJOBTRACK, reviewboard |
| 22 | [SQL Server for Postgres developers (EF Core)](22-sqlserver-for-postgres-devs.md) | meterforge, atlas |

Backlog (only one project needs these so far; write a page when a second one does):
- (SignalR lifecycle and groups → now page 08)
- EF migrations on an `EnsureCreated` database
- Recurring jobs across replicas
- Keyset pagination (partly in page 10)
- (Row-level multi-tenancy → now page 19)
- JWT clock skew
- `redirect_uri` exact match
- Refresh-token rotation and reuse detection
- (Money rounding → now page 20)
- Architecture tests (NetArchTest)
- Modular monolith vs microservices decision
- Table-driven state machines
- Placing a change in an event-choreographed system
