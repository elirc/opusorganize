# Competency Graph

This maps each skill to its central concept page, the projects that practise it, and the exercises, incidents and interview questions.
It is updated at the end of every batch. Paths are relative to each repo's `training/` folder.
Counts are practice items (tickets, incidents, drills, review findings used as exercises).

Last updated: **B07 (2026-09-24)**. Batches B01–B07 cover 31 projects:

| Batch | LAB | DRILL | READ |
|---|---|---|---|
| B01 | netdrop, netintercom | .netstripe, .netramp, netauth | eShop, modular-monolith-with-ddd |
| B02 | gitjira-app, atlas | pulse, perch, bazaar | — |
| B03 | astraspacegameweb, lucasrouter | astra1 | Outline |
| B04 | buildevent, buildermentor | aicallhelper, aiheartbeat | — |
| B05 | relay, folio | astra5 | — |
| B06 | aaa1, HNJOBTRACK | grokbuildmultitenantproject | — |
| B07 | meterforge | globehire, VGdemo, vg | reviewboard |

Totals:
- 92 incident branches
- 27 blind reviews
- about 140 ladder tickets
- 13 full + 14 mini interview kits
- 22 curriculum pages

| Skill area | Concept page(s) | Where to practise (strongest first) | Count | Level |
|---|---|---|---|---|
| SQL: plans, indexes, N+1 | [10](curriculum/10-query-plans-and-indexes.md) | atlas M1/INC-001/003 · astra1 EXPLAIN journal + INC-001 · netdrop INC-004 · netintercom INC-005 · gitjira-app INC-001 · buildevent INC-004 (hot row) | ~15 | good |
| Transactions / concurrency | [03](curriculum/03-concurrency-races.md) | B01 labs · atlas M2 · buildevent M1 (Serializable → P2034 on main) | ~15 | saturated |
| Zero-downtime migrations | [07](curriculum/07-zero-downtime-migrations.md) | gitjira-app INC-003/S2 · atlas INC-004 · netdrop S2 | 5 | good |
| Queues / idempotency / outbox | [01](curriculum/01-transactional-outbox.md), [02](curriculum/02-idempotency.md) | B01–B02 · buildevent INC-002/005 · buildermentor INC-005 | ~22 | saturated |
| **Load / back-pressure / timeouts** | [14](curriculum/14-load-backpressure-timeouts.md) | **buildevent** (5 measured incidents, k6 skeleton, drop-sim) · buildermentor INC-002/M4 · astraspacegameweb INC-001/S2/S3 · gitjira-app M3 | ~14 | **good** (new in B04) |
| Caching | [06](curriculum/06-caching-correctness.md) | bazaar INC-001/002 · buildevent INC-002 (eviction) · pulse · netintercom M1 | 5 | medium |
| Observability / SLOs (operated) | [09](curriculum/09-telemetry-correctness.md) | **astraspacegameweb** LAB0 + M1 + INC-002 (live stack) · gitjira-app INC-004/M2/S3 · atlas M4/INC-005 · pulse INC-001 · astra1 INC-002 | ~14 | good |
| Release safety / deploy / rollback | [13](curriculum/13-release-safety.md) | astraspacegameweb INC-004/005, S1 · atlas INC-004/S1 (Azure) · gitjira-app J1/S1 (Fly→AWS) · netdrop S3 | ~9 | medium (still nothing actually deployed to a cloud) |
| API versioning / back-compat | — | atlas M3/INC-002 · netdrop M2/S2 · netintercom M2 | 7 | good |
| Realtime | [08](curriculum/08-realtime-fanout.md) | gitjira-app INC-005/M4 · astraspacegameweb INC-003 · netintercom | 8 | good |
| Frontend performance | [12](curriculum/12-frontend-performance.md) | **lucasrouter** INC-001/004/005, M1, M4, probe tool · perch INC-001 · gitjira-app M1 | ~9 | good (was thin) |
| **Accessibility** | [11](curriculum/11-accessibility-essentials.md) | **lucasrouter** INC-002/003, M3 audit · Outline upstream candidate A | 4 | medium (was 0) |
| Web / React / frontend testing | [12](curriculum/12-frontend-performance.md) | lucasrouter J2 (first component tests) · perch INC-002 · netintercom M3/M4 · buildevent J3 | ~7 | medium |
| Authn / authz / security | — | B01 (netauth ASVS, IDORs) · perch · bazaar INC-002 · buildermentor (items shared across users, SSRF) | ~20 | saturated |
| **AI / LLM integration** | [15](curriculum/15-llm-features-in-production.md) | **buildermentor** (10 tickets, 5 incidents: evals, cost, schema, injection, jobs) · aicallhelper INC-001/002 (cancellation, billing, latency-budget questions) | ~20 | **good** (new in B04) |
| **Agentic engineering** | [05](curriculum/05-verify-before-trust.md), [15](curriculum/15-llm-features-in-production.md) | aiheartbeat INC-001/002 + agent-harness review + "safely running agents" questions · agentic workflows in all 8 LABs | ~12 | good |
| Testing | [04](curriculum/04-characterization-tests.md) | characterization tests (netramp, netstripe) · runnable regression tests (buildermentor `_answers/regression-tests`) · atlas contract tests | ~13 | medium |
| Reliability / incidents | — | 92 incident branches with sealed postmortems | 92 | strong |
| Code review | [05](curriculum/05-verify-before-trust.md) | 27 blind reviews | 27 | strong |
| Design docs / trade-offs | — | ~35 "Why?" drills + S-rung design docs | ~35 | good |
| Unfamiliar codebases / upstream contribution | — | 11 navigation packs (8 LABs + eShop, mm-ddd, Outline) · Outline upstream-PR kit | 12 | good (0 real PRs yet) |
| **Durable execution / workflows** | [18](curriculum/18-durable-execution.md) | **relay** (runnable lab, 5 live-reproduced incidents, M1–M4, S1–S2) · buildermentor INC-005 · atlas S2 | ~13 | **good** (new in B05) |
| **Sagas / compensation** | [16](curriculum/16-sagas-vs-2pc-vs-outbox.md) | astra5 INC-001 + Worker.cs crash-window finding + sagas-vs-2PC-vs-outbox questions · relay S1 · eShop · mm-ddd | ~6 | medium (new in B05) |
| **CRDT / offline sync** | [17](curriculum/17-crdt-offline-sync.md) | **folio** (5 measured incidents, property-test M1 on a real main bug) · Outline save-path trace | ~11 | **good** (new in B05) |
| **SQL Server** | [22](curriculum/22-sqlserver-for-postgres-devs.md) | **meterforge** lab branch + 5 incidents (sniffing, 1205 deadlock, implicit conversion, collation, decimal truncation), ladder J1–S2 · atlas M1 | ~15 | medium (built; **runtime UNVERIFIED** until Docker/SQL Server runs) |
| **DB-enforced tenant isolation (RLS)** | [19](curriculum/19-rls-defense-in-depth.md) | **aaa1** RLS lab + 5 live incidents · HNJOBTRACK Supabase RLS probes · grokbuild compound FKs + PG18 probe | ~14 | **good** (new in B06) |
| **Python / FastAPI** | backlog | HNJOBTRACK (async loop blocking, Pydantic, maybe_single crash, contract drift) | ~9 | medium (new in B06) |
| **Legacy rescue / ports** | [21](curriculum/21-legacy-rescue-and-ports.md), [04](curriculum/04-characterization-tests.md) | VGdemo parity drill (TS 17/20 vs .NET 13/20) + 2 port incidents · vg characterization + dead-schema triage · grokbuild legacy-diff · globehire EF-swap exercise | ~12 | **good** (new in B07) |
| **Money & time** | [20](curriculum/20-money-and-time.md) | vg INC-001/002 · globehire INC-002 (TZ) · meterforge INC-005 · netstripe INC-002 | ~8 | good |
| **.NET DI / async** | — | globehire INC-001 (captive dependency) · async/await exercises | ~3 | medium |
| Cloud deploy (actually running) | [13](curriculum/13-release-safety.md) | designs only | 0 executed | **thin** |
