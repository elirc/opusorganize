# Prioritized Roadmap — Mid → Senior apprenticeship

Principle: **depth on a few codebases you own, operated like production**, instead of more generated CRUD apps or more curricula.
The CRUD-reliability fundamentals are already covered by `AstraOrganized2\fablereview\LEARNING_PATH.md` (Stages 0–4, ~30 projects).
Treat that path as a *maintenance* track (1 session/week, max) and only for the items you haven't done.

## Week 0 — hygiene (half a day, before any learning)
1. **Revoke the Shopify `shpat_` token** found in `AstraOrganized2\astra-remaining-improvements\backups\cf8875344b43\scripts\populate-metaobjects.js`; check `buildreviewer\.env` and `vg\.env` contents.
2. `git commit` (or at least init + commit) the flagships' uncommitted work: grokbuild* post-snapshot changes; confirm atlas/gitjira-app/astra1/astraspacegameweb/aicallhelper remotes are pushed.
3. Freeze scope: no new generated apps or curriculum packs until Wave 2 is done.

## NOW — Wave 1 (≈6–8 weeks): production engineering on 2 flagships
| Project | Goal | Concrete deliverables |
|---|---|---|
| **gitjira-app** (TS) | take a real app to production and keep it alive | deploy to AWS (ECS Fargate + RDS Postgres) via existing `deploy.yml`; one zero-downtime expand/contract migration under load; 2 SLOs + alert; write *your own* ADR + postmortem for one induced failure |
| **atlas** (.NET) | the .NET/SQL flagship | SQL Server provider profile + 1M-row seed; capture and fix 2 slow queries with execution plans; Azure deploy (Container Apps + Azure SQL); contract tests guarding the existing V1/V2 APIs |

Why these two: highest combined scores (PROJECT_MATRIX), real history/CI (gitjira-app: 209 commits, 4 workflows), real depth
(atlas: 119 test files, idempotency middleware, outbox, V1/V2), and together they cover both target stacks.

## NEXT — Wave 2 (≈6 weeks): gaps that make you senior
| Project | Gap filled |
|---|---|
| **astraspacegameweb** | observability + incidents: use the existing Prometheus/Grafana/Tempo + chaos tests; run 3 timed fire drills; write postmortems |
| **astra1 (Helios)** | Postgres performance: `pg_stat_statements`, EXPLAIN journal, index design for multi-tenant queries; trace a request end to end with OTel |
| **Outline** (reference) | unfamiliar codebase: do fabledocs4 fire drills + outbox capstone; then land **one upstream PR** (Outline/Twenty/OpenStatus) |
| **eShop** (reference) | distributed systems: run with Aspire, kill RabbitMQ, observe retries/DLQ, work 10 of the 72 graded stories (`astra/check_course.py`) |

## LATER — Wave 3: specialization & interview polish
- **buildevent**: spike handling (ticket drop), queue back-pressure, idempotent Stripe webhooks, k6 load test.
- **aicallhelper**: present as the AI product + latency-budget story; add evals/cost dashboards; decide canonical version vs aicallhelper5.
- **buildermentor**: RAG evals, cost guardrails, pg-boss failure modes.
- **lucasrouter / gitjira-app web**: frontend perf + a11y audit with before/after numbers.
- **Exercise rotation** (1 per week, timed 60–90 min): globehire/meterforge/perch flaw ledgers → vg punch list → Review Board security stories → VGdemo .NET regression → anti* JWT fail-closed → obsidian-claude broken build.
- **Agentic engineering**: for each Wave task, write the spec/design doc yourself first, have an agent implement, then do an adversarial review (the pattern used in aiheartbeat / fablereview) and record what the human review caught.

## REFERENCE (read, don't build)
Outline, Twenty, OpenStatus, eShop, OrchardCore, modular-monolith-with-ddd, Infisical (architecture critique), CleanArchitecture,
Plane vs Teable (CRDT vs OT), NextCRM (real IDOR CVE), Umami (orderBy SQLi), Paperless-ngx (SSRF), OpenSlides (only microservices OSS),
bulletproof-react, rn1/Bluesky. C# trio (csharptut → csbootcamp → c#interview) and JSTut as personal reference.

## ARCHIVE (no further investment; move to a cold folder later, delete nothing without review)
05 Numbered Experiments (keep rn1, z1, z3, g1/X1, B1 + 3 samples), newcodex3, most of newcodexJS/JS1 (keep LEARNING_PATH items),
grokjs, groktuts, trainjs, jstrain* apps except jstrain2.2, all empty dirs (`10 New Folders\*`, opusboot2/4.2, opusdavinci, codexlearnp1, master 5,
master555, f1, j6, aff-wt-be06, …), geminiorganized, AstraOrganized (≡ project-inventory), superseded versions (aihelper, fableaihelperv3,
fableaihelperv2\cuedeck, spacegame v1, jobtrack, astraboot1, atlas-net, agora-net, master6, jsdrillapp\reps), recipe/jeopardy duplicates,
bare OSS clones without curricula (Novu, Supabase, ToolJet, Typebot, Indico, Umbraco, jellyfin), VTCode.
