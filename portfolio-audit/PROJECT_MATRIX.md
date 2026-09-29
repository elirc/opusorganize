# Project Scoring Matrix (supporting evidence, not a replacement for judgment)

Scale 1–5. Scored from batch records + spot checks on 2026-09-23 (atlas: 119 `*Tests*.cs` files, 16 commits, tags v0.5.0/v1.0.0,
`src/Atlas.Api/Idempotency/IdempotencyMiddleware.cs`; gitjira-app: 209 commits, `docs/adr` + 33 ADR-matching files, `postmortems/`,
`threat-model.md`, `RUNBOOK.md`, 4 workflows; astraspacegameweb: `compose.production.yaml`, `infra/Caddyfile`, `infra/tempo.yaml`, `ci.yml`;
astra1: `src/instrumentation.ts`, `api/metrics/route.ts`, `server/audit.ts`, `ci.yml`).

Columns: **Q** current code quality · **Arch** architectural depth · **Real** business realism · **Dbg** debugging potential ·
**DB** database learning · **FE** · **BE** · **Prod** production-engineering potential · **SD** system-design · **Int** interview relevance ·
**Docs** existing docs · **Mod** modernization upside · **Uniq** uniqueness · **Overall**

| Project | Q | Arch | Real | Dbg | DB | FE | BE | Prod | SD | Int | Docs | Mod | Uniq | Overall |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| atlas (.NET EOR) | 4 | 5 | 5 | 4 | 4 | 1 | 5 | 3 | 5 | 5 | 4 | 4 | 4 | **5** |
| gitjira-app | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 3 | 4 | **5** |
| astraspacegameweb | 4 | 4 | 3 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4 | 3 | 5 | **5** |
| astra1 (Helios) | 4 | 5 | 4 | 4 | 5 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | **5** |
| aicallhelper (Tauri v3) | 4 | 4 | 5 | 4 | 2 | 4 | 3 | 3 | 3 | 5 | 5 | 2 | 5 | **4.5** |
| master1 (GlobalWork) | 4 | 4 | 5 | 3 | 4 | 3 | 5 | 3 | 4 | 4 | 5 | 3 | 2 (EOR dup) | 4 |
| buildermentor (ShipShape) | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 4 | 4 |
| buildevent | 3 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3 | 5 | 4 | 4 |
| pulse (gitvg) | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 |
| bazaar (gitvg) | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 |
| astra5 (Stockade) | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 3 | 4 | 4 |
| aaa1 | 3 | 4 | 4 | 3 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 3 | 3 | 4 |
| globehire / meterforge | 4 | 4 | 4 | 5 | 4 | 1 | 4 | 2 | 3 | 5 | 4 | 3 | 4 | 4 |
| perch | 4 | 3 | 4 | 5 | 3 | 3 | 4 | 2 | 3 | 5 | 5 | 3 | 3 | 4 |
| grokbuildmultitenant | 3 | 3 | 4 | 4 | 4 | 3 | 4 | 2 | 3 | 4 | 4 | 3 | 3 | 3.5 |
| tagalog | 3 | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 3 | 4 | 3 | 4 | 4 | 3.5 |
| borrowbox | 4 | 3 | 3 | 3 | 3 | 1 | 4 | 2 | 2 | 3 | 5 | 2 | 3 | 3.5 |
| opusboot1 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 3 | 3 | 4 | 3 | 3 | 4 | 3.5 |
| lucasrouter | 4 | 3 | 4 | 3 | 1 | 5 | 2 | 3 | 3 | 4 | 4 | 2 | 4 | 3.5 |
| aiheartbeat | 4 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 4 | 4 | 3 | 5 | 3.5 |
| VGdemo | 3 | 3 | 4 | 5 | 3 | 3 | 4 | 2 | 3 | 5 | 4 | 3 | 4 | 3.5 |
| masteroutline (OSS) | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 4 | 5 | – | 4 | **D★** |
| eShop (OSS) | 5 | 5 | 4 | 4 | 4 | 3 | 5 | 5 | 5 | 4 | 5 | – | 5 | **D★** |
| twenty / openstatus (OSS) | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4 | 5 | – | 4 | **D★** |
| numbered-experiment corpus | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 1 | 1 | 2 | 3 | 1 | 1 | 1.5 |
| newcodex3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1.5 |

Reading notes
- Frontend is the weakest dimension almost everywhere except gitjira-app, lucasrouter, aaa1, astraspacegameweb and tagalog.
- "Prod" ≥4 exists only where there is Docker + CI + some telemetry: astraspacegameweb, gitjira-app, astra1, pulse, bazaar, buildevent, tagalog.
- None of these is deployed to AWS or Azure (see GAP_ANALYSIS.md).
