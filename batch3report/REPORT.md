# Batch 03 Report: operating a live stack + frontend

*2026-09-24 · I ran `apprenticeship/BATCH_PROMPT.md` on 4 projects chosen to fill the gaps left after B02: **operating** a real stack,
**frontend/accessibility**, raw-SQL performance, and the first upstream contribution. Per-project detail is in `projects/<name>.md`.
Shared outputs: `apprenticeship/curriculum/11–13` (new) plus additions to 09 and 10, and `apprenticeship/COMPETENCY_GRAPH.md` (updated after B04).*

## 1. Headline
This is the first batch where incidents were **reproduced on a live system and measured**, not just compiled:
- **astraspacegameweb:** all 5 incidents were run against a real Prometheus/Grafana/Tempo stack.
- **lucasrouter:** all 5 were measured on production builds.

## 2. Tiers
| Project | What it is | Tier | Why |
|---|---|---|---|
| **astraspacegameweb** | Warband browser strategy game: TS server roles, Postgres, Redis, Prometheus/Grafana/Tempo, chaos tests | **LAB** | the only project with a full operations stack |
| **lucasrouter** | RouteIQ route optimizer: Next 16, React 19, Leaflet, zustand | **LAB** | frontend performance + accessibility (0 exercises before this batch) |
| astra1 | Helios multi-tenant ops sim on raw SQL + OTel | DRILL | query plans without an ORM; a telemetry bug |
| Outline (masteroutline) | OSS wiki (Koa/Sequelize/Yjs) with an excellent existing 4-part curriculum | READ | collaborative-save trace + first upstream-PR kit |

## 3. What was created
| Project | Commit(s) | Contents | Incidents | Effort |
|---|---|---|---|---|
| astraspacegameweb | `2fca582` | `ops/` lab kit (compose.observe.yaml, load injector, two-tab repro, LAB0 bring-up with 8 questions answered from dashboards); tickets J1–J3, M1–M4 (M1 = 2 SLOs + burn-rate alerts), S1–S3; review (24); navigation; agentic; interview kit | 5 | ~45 h |
| lucasrouter | `b3ee4c8` | 9 tickets (J2 sets up the first component tests, M1 marker-click INP, M3 axe + keyboard + screen-reader audit, M4 per-route JS budgets); review (24); `tools/frontend-probe.mjs` (Web Vitals, JS bytes, input latency, a11y checks); interview kit | 5 | ~35 h |
| astra1 | `9d64e5a` | review; **EXPLAIN journal** exercise for the 3 heaviest queries; mini interview kit | 2 | ~6 h |
| Outline | baseline `37ca0d5` + `cca361b` | collaborative-save-path trace (file:line); **upstream-contribution kit** with 3 real candidate PRs + sealed placement answers; reading order through the 4 existing fabledocs trees | — | ~4 h, plus a real PR |

**Git notes**
- Outline had **no git**, so the agent ran `git init` and made a baseline commit (2,631 files; `node_modules` excluded; branch `master`) before adding `training/`.
- The other repos got `training/`-only commits.
- Your uncommitted files are unchanged: lucasrouter 9, astra1 7.
- Nothing was pushed, and no worktrees are left.

**Incident symptoms** (causes sealed in each repo's `_answers/`)

*astraspacegameweb*
1. The world falls behind at a load it handled last week, with no errors or retries.
2. Players report late battles, but the lag panel is flat and nothing pages.
3. One of a player's two tabs stops getting live updates.
4. After a release, every role restarts in a loop.
5. A 40-second Redis restart makes every request return 502.

*lucasrouter*
1. JS needed before the landing page is interactive grows by 28 KB.
2. Toast messages are no longer announced to screen readers.
3. The driver sheet loses Escape, focus return and modality.
4. Typing in stop search produces about 20 long tasks (1.4–1.9 s).
5. `/dispatch` starts to shift layout (CLS 0 → 0.04).

*astra1*
1. A new paginated invoice-history endpoint gets slow.
2. `/api/metrics` undercounts. **This bug is real and already on `main`**, traced to the historic commit `75c4d82`.

## 4. Verification
| Project | Verified | Not verified |
|---|---|---|
| astraspacegameweb | **Live stack:** 5 roles scraped, dashboards loaded, traces received. **Each incident run:**<br>• 001: drain 151–154 s vs 91–115 s, about 3.5× more rollbacks, invisible in the metrics<br>• 002: lag p99 flat at 2.0 while the oldest event is 137 s old<br>• 003: the second tab gets 0 of 5 updates<br>• 004: crash loop reproduced<br>• 005: the existing chaos test fails on the branch and passes on `main`<br>**Also:** the reference M1 SLO rules pass `promtool test rules`; typecheck passes; 63 tests that don't need a DB pass | DB integration tests, e2e, `recovery.ts`/`load.ts`; answers for M4/S1/S3 are reasoned; timings are noisy (shared laptop) |
| lucasrouter | vitest 167/167 and typecheck; every incident builds and lints. **Measured on production builds:**<br>• JS bundle: 591 → 619 KB<br>• long tasks: 0–1 → ~20<br>• CLS: 0 → 0.04<br>**Baseline measurements:**<br>• 13–14 axe contrast failures; 116 Tabs to reach "Export JSON"<br>• toast visible only ~170 ms (a reference fix gives 3.7 s)<br>• marker-click INP 224–240 ms, 1.06–1.46 s at 4× CPU | no real screen reader was used; no Lighthouse runs |
| astra1 | index gaps checked against `db/migrations/*.sql`; the telemetry bug traced in the code and git history | query plans reasoned (Docker was off when it ran); incident 001 not compiled |
| Outline | file:line citations read from the source | nothing installed or run; the candidate PRs are not yet checked against live upstream issues |

**Docker Desktop is now running.** The astraspacegameweb agent started it (it takes about 10 minutes to come up). It was left running so the B04 agents could use it. Its own containers are stopped.

## 5. Real defects found (documented, NOT fixed)

**astraspacegameweb**
- **Line endings break startup** (verified on `main`): there's no `.gitattributes`, and the migration checksum is taken over raw bytes, so a CRLF checkout refuses a database migrated from LF files. An image built from a Windows checkout would crash-loop.
- There's no real rollback: `compose.production.yaml` uses `build: .` with no image tag.
- There's no Alertmanager, so alerts reach no one.
- Histograms clip (lag at 60 s, resolver at 30 s).
- The health check both routes traffic and checks only the DB.
- Connection pools total 7 × 16 = 112, above Postgres's default of 100.
- Side jobs retry forever.
- The 1,000 arrivals/s target isn't met (the docs say so honestly).
- There's a hardcoded fallback JWT secret outside production (`transport/app.ts:47`).

**lucasrouter**
- `DECISIONS.md` #44 claims accessibility 100, which is out of date. #54 describes an `inlineCss` setting that doesn't exist.
- `docs/REBUILD.md`'s per-route JS figures include idle prefetch.
- The result-count live region mounts along with its text, so it may not be announced.
- The Undo toast disappears after 3.5 s with no pause.
- `/api/optimize` is public and accepts bodies of any size.
- There are no component tests, no CI and no real-user monitoring.
- **`.env.local` holds a Vercel token.** It is gitignored and never committed, but consider rotating it if the file has ever left this machine.

**astra1**
- Four tables are missing the composite index their main reads need, while 5 sibling tables have it.
- An audit query's `OR` branch can't use the index, and it's duplicated in `queries.ts:28` and `agent-tools.ts:61`.
- Spans for unauthenticated requests are dropped.

**Outline (upstream)**
- A missing `aria-label` at `Collaborators.tsx:167`.
- An untested `DocumentUpdateTextTask.ts`.
- No failure metric for collaborative saves.

All three are candidates for your **first upstream PR**.

## 6. Existing learning docs: verdicts
| Repo | Verdict |
|---|---|
| astraspacegameweb | `docs/` (architecture, ADRs, runbooks, verification): KEEP · `docs/final-improvements*`, `npcs.md`, `spawning.md`: IGNORE · `artifacts/`: IGNORE for learning (the drills write there, so run them from a worktree) |
| lucasrouter | `astraupskill/`, `dfableandopus/`, `docs/ALGORITHM_INTEGRATION.md`: KEEP · `DECISIONS.md` and `docs/REBUILD.md`: CONVERT (their stale claims now feed review findings and ticket M4) |
| astra1 | `astraupskill/`, `upskilling/`: KEEP |
| Outline | all 4 fabledocs trees: KEEP, with the reading order in `training/README.md` |

## 7. Curriculum updates
- **New pages:**
  - 11: accessibility that actually works
  - 12: measuring frontend performance honestly
  - 13: release safety (health checks, reproducible artifacts, rollback)
- **Additions:**
  - page 09: PromQL SLO traps (clipped histograms, `le="2.0"`, zero-traffic alerts, age-of-oldest-item)
  - page 10: astra1 examples plus the aggregate-then-limit trap

## 8. What to do first (about 1.5 weeks part-time)
1. **astraspacegameweb LAB0:** bring the stack up with `training/ops/compose.observe.yaml` and answer the 8 dashboard questions. This is your first time *operating* something.
2. **astraspacegameweb M1** (write the 2 SLOs + alerts; verify them with `promtool test rules`), then **INC-002** (the flat lag panel).
3. **lucasrouter M3:** the axe + keyboard + screen-reader audit. Then do **INC-003** and **INC-002** without looking at the answers.
4. **lucasrouter INC-004:** measure first with `training/tools/frontend-probe.mjs`, then fix.
5. **astra1 EXPLAIN journal:** capture real plans now that Docker runs.
6. **Outline upstream kit:** pick one of the 3 candidates, confirm it against GitHub issues, and open a real PR.
