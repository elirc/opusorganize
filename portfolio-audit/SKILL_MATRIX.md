# Engineering Skill Matrix

**Method.** Every meaningful project record in `projects/batch-*.md` carries skill tags from a fixed vocabulary (`_AGENT_BRIEF.md`).
Counts below = number of records (231 tagged records) carrying the tag. Cluster records (e.g. "78 numbered experiments", "20 newcodexJS apps")
count **once**, so real repetition of CRUD/Prisma/React is far higher than the numbers show. Depth is judged from the best examples, not the count.

## Matrix

| Skill | Records | Depth | Best example(s) (evidence) | Gap |
|---|---|---|---|---|
| **React** | 83 | High | gitjira-app, lucasrouter, aaa1 | little FE *architecture*/perf work |
| Next.js (App Router) | 41 | High | astra1, aaa1, buildevent, storefront | caching/RSC trade-offs rarely discussed |
| TypeScript types | 49 | Med-High | opusboot1, gitjira-app | advanced generics / type-level design rare |
| Frontend state | 22 | Medium | calendar+jobtrack (Zustand), lucasrouter | server-state vs client-state trade-offs |
| Forms + validation (FE) | 14 | Medium | anti* (Zod+RHF) | — |
| **Frontend testing** | 8 | Low | gitjira-app e2e, ankijs (Playwright+Vitest) | component testing strategy thin |
| **Frontend performance** | 4 | Very Low | lucasrouter (Lighthouse before/after) | bundle, rendering, Web Vitals investigations |
| **Accessibility** | 4 | Very Low | perch (a11y audit) | almost absent |
| Node/Express | 70 | High | grokbuild*, anti*, gitjira-app | overtrained |
| NestJS | 7 | Medium | master1, buildreviewer, antitestbuild | — |
| **C#/.NET** | 46 | High | atlas, borrowbox, globehire, meterforge, Net-fleet | strong coverage (good for the target) |
| Python backend | 23 | Medium | HNJOBTRACK (FastAPI), pp8, aicallhelper2, Django OSS | not a target stack; fine |
| REST API design | 40 | Med-High | atlas (v1/v2 contracts), gitjira-app | versioning practice rare |
| GraphQL / tRPC | 2 | Very Low | aral (tRPC), Saleor (OSS) | — (low priority) |
| Validation (BE) | 39 | High | grokbuild* (Zod), atlas | — |
| Error handling | 12 | Medium | fablereview items (400 vs 500, Express handler arity) | consistent error contracts |
| Async jobs / workers | 33 | Med-High | buildevent (BullMQ), buildermentor (pg-boss), master1 | job observability, poison messages |
| Authentication | 37 | Med-High | netauth (IdP), astraspacegameweb (refresh-token reuse detection) | OAuth/OIDC with a real provider |
| **Authorization / RBAC** | 54 | High | grokbuildmultitenant, rewritepy2js IDOR fix, NextCRM CVE | overtrained at the "scope by tenant" level |
| Multi-tenancy | ~10 | Medium | astra1, aaa1, grokbuildteam (compound FKs), OrchardCore | — |
| **Postgres** | 88 | High | astra1 (raw SQL), JS1 (EXCLUDE gist, FOR UPDATE) | overtrained for CRUD |
| **SQL Server** | 2 | Very Low | nopCommerce (OSS, supports it) | **major gap given .NET target** |
| SQLite | 34 | High | many local-first apps | — |
| ORM (Prisma/EF/Drizzle/Knex) | 84 | Very High | everywhere | **overtrained** |
| Data modeling | 14 | Medium | atlas, master1 | explicit modeling exercises rare |
| Migrations | 22 | Medium | Prisma/EF migrations | **zero-downtime (expand/contract): 1 record** |
| Raw SQL | 14 | Medium | astra1, JS1, newcodexJS (Knex) | — |
| **Indexes / query performance** | 5 | Very Low | fablereview notes only | **EXPLAIN ANALYZE practice absent** |
| Transactions | 19 | Medium | JS1 org-explorer, newcodexJS 13/14, numbered corpus | — (well covered at CRUD level) |
| Concurrency | 28 | Med-High | JS1 room-booking, grokbuildorder (optimistic), Plane/pretalx TOCTOU | — |
| Unit tests | 83 | High | atlas (119 test files), aicallhelper (570) | — |
| Integration tests | 33 | Medium | master1 (Testcontainers), newcodexJS disposable schema | — |
| E2E tests | 27 | Medium | gitjira-app (e2e.yml), astraspacegameweb | — |
| **Tests in CI** | 3 (+~15 repos with ci.yml) | Low | gitjira-app, gitvg fleet | CI rarely gates anything you touch daily |
| Modular monolith | 27 | Med-High | globehire, meterforge, modular-monolith-with-ddd (OSS) | — |
| Clean/hex architecture | 11 | Medium | atlas, CleanArchitecture (OSS) | — |
| **Microservices** | 6 | Low | eShop (OSS), OpenSlides (OSS) | **never built or operated one yourself** |
| Event-driven | 19 | Medium | astra1 sagas, astra5 sagas, eShop | — |
| Queues | 32 | Medium | BullMQ/pg-boss/Hangfire | DLQ + replay practice thin (pulse-net only) |
| Outbox | 17 | Medium | atlas, master1, astra1; Outline capstone | — |
| Idempotency | 20 | Medium | atlas `IdempotencyMiddleware.cs`, meterforge ledger | — |
| **Caching** | 10 | Low | bazaar, ww30/31 | cache invalidation under load, Redis ops |
| Realtime / WebSockets | 31 | Med-High | gitjira-app (Socket.IO), netintercom (SignalR), buildwhiteboard (Yjs) | — |
| Docker | 25 | Medium | astraspacegameweb (compose.production.yaml) | — |
| CI/CD | 24 | Medium | gitjira-app (ci/deploy/e2e/secrets.yml) | **deploy pipelines to a real cloud** |
| **AWS** | 3 | Very Low | 3buildhyper (Amplify) | **major gap** |
| **Azure** | 3 | Very Low | — | **major gap for .NET** |
| Deployment | 11 | Low | tagalog (aral-deploy/DEPLOY.md), gitjira-app deploy.yml | nothing running in production today |
| Config / secrets | 22 | Medium | gitjira-app secrets.yml | real secrets leaks found (Shopify token, buildreviewer .env) |
| Logging | 20 | Medium | astra1 audit.ts | — |
| **Metrics / tracing** | 11 | Low | astraspacegameweb (Prometheus/Grafana/Tempo), astra1 OTel, hnrandom (OTLP) | **no SLOs, alerts, dashboards you have *used*** |
| OWASP / security | 41 | Med-High | threat-model.md (gitjira-app), IDOR stories, JWT fallback | — |
| **Performance investigation** | 6 | Very Low | lucasrouter, pulse load/ | **profiling, load tests, flame graphs** |
| **Incident debugging** | 9 | Low | gitjira-app postmortems/, Outline fire drills | real on-call style practice |
| **Backward compatibility / versioning** | 7 | Low | atlas v1/v2 API | contract tests, deprecation |
| Design docs / ADRs | 66 | High (to read) | gitjira-app 33 ADRs, Outline 10 ADRs | **you have read many; written few yourself** |
| Legacy / unfamiliar codebases | 35 | High | 40 OSS clones with curricula | — (opportunity: *contribute* to one) |
| Code review | 23 | Medium | fablereview/, Infisical critique | reviewing *someone else's* PR under time pressure |
| Mobile RN | 9 | Medium | tagalog, spacegame | not a target |
| Desktop (Electron/Tauri) | 9 | Med-High | aicallhelper family | not a target, but a unique story |
| LLM integration | 29 | Med-High | buildermentor (RAG), HNJOBTRACK, aicallhelper | evals/cost/latency budgets partly covered |
| **Agentic engineering** | 10 | Medium | aiheartbeat, the Astra/Fable pipelines themselves, ctvodejs | see GAP_ANALYSIS |
| Basic CRUD | 56 (+~200 in clusters) | Very High | everywhere | **heavily overtrained** |

## Overrepresented (diminishing returns reached)
1. **React + Express/Next + Prisma/ORM + Postgres CRUD with JWT auth and Zod.** ≥150 folders. The fablereview LEARNING_PATH already extracts the ~30 useful ones.
2. **"Scope every query by tenant/owner" authorization.** Taught in dozens of Astra lessons, anti*, grokbuild*, rewritepy2js, NextCRM. You know this.
3. **CRUD-level transactions/race fixes** (`FOR UPDATE`, optimistic `version` column, unique-constraint idempotency). ~10 numbered-corpus lessons + JS1 + newcodexJS + grokbuild. Enough.
4. **Reading generated curricula.** ≈200 `astraupskill` packs + 35 fabledocs + 40 career packs. Reading more is not progress.
5. **SaaS clone generation.** Help desk ×12, trackers ×12, e-commerce ×13, EOR ×7.

## Underrepresented (blocking Mid→Senior)
In priority order: cloud deployment (AWS/Azure) · SQL Server + query plans/indexing · zero-downtime migrations · metrics/tracing/SLOs you operate ·
performance investigation · incident response · backward-compatible API evolution · frontend performance/a11y/testing · authoring design docs ·
building/operating a small distributed system yourself · reviewing others' code. Details and project mappings: GAP_ANALYSIS.md.
