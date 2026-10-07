# Batch 04 Report: load, AI features, agentic engineering

> **Status note (added 2026-10-06):** this report is a frozen record of the batch and was not updated afterwards. Not every `training/incidents/*` branch it describes is on GitHub: only 21 of the 92 from B01–B07 were pushed, and several projects now live under different elirc repo names. Before you try to check out an incident, see the incident-branch availability note at the top of [`apprenticeship/PROGRESS.md`](../apprenticeship/PROGRESS.md).

*2026-09-24 · I ran `apprenticeship/BATCH_PROMPT.md` on 4 projects covering the audit's "Wave 3": load and back-pressure,
LLM-backed features, AI latency, and the safety of running coding agents. Per-project detail is in `projects/<name>.md`.
Shared outputs: `apprenticeship/curriculum/14–15` (new), `apprenticeship/COMPETENCY_GRAPH.md` (rebuilt across B01–B04), `apprenticeship/PROGRESS.md`.*

## ⚠ 1. Read first: a data-loss incident during this batch, now recovered
**What happened.**
- The `aiheartbeat` agent ran `rm -rf node_modules` to clear a broken install.
- On Windows, npm workspace links (`node_modules/@pulse/*` → `packages/*`) are **directory junctions**, and the recursive delete followed them.
  It deleted the real `packages/core`, `packages/dashboard` and `packages/shared` source.
- The agent restored all *committed* files with `git checkout`.
- But 3 of your **uncommitted** files were reset to their committed state, losing your in-progress edits:
  - `packages/dashboard/app/api/workspace/route.ts`
  - `packages/dashboard/lib/workspace-store.ts`
  - `packages/dashboard/lib/workspace-store.test.ts`

**Recovery.**
- The earlier Astra pass had recorded SHA-256 hashes of those files' final versions in `aiheartbeat/astraupskill/evidence/root-final-source-hashes.json`.
- I found copies with **exactly matching hashes** in `Desktop\AstraOrganized2\astra-remaining-improvements\stage\9e1958f807df\` and restored all 3.
- The restored diff is the `assertCollection`/`assertId` input-validation fix and its regression test (+42/−1 lines, including your untouched README edit).
- `git status` now shows your original 4 modified files plus 2 untracked folders.

**Caveats and what to check.**
- The recovered version is the one recorded on **2026-09-12**. If you edited these files after that, those later edits are not recoverable.
- **Please look at `git diff` in `aiheartbeat`** to confirm it's what you expect.

**Prevention.** A hard rule now sits in `BATCH_PROMPT.md` and every agent brief: no recursive deletes inside repos, ever.
This is also a worked example in curriculum page 15 ("destructive commands need guardrails even for cleanup").

## 2. Tiers
| Project | What it is | Tier | Why |
|---|---|---|---|
| **buildevent** | ticketing: Next + Fastify + Prisma/PG + Redis/BullMQ + Stripe + QR | **LAB** | ticket-drop load and back-pressure |
| **buildermentor** | ShipShape study engine: RAG (pgvector), LLM item generation, pg-boss, cost guardrails | **LAB** | the portfolio's LLM-backend lab |
| aicallhelper | AI call assistant v3 (Tauri/Rust + React), streaming STT + LLM | DRILL | latency budgets and cancellation |
| aiheartbeat | hourly `claude -p` orchestrator + dashboard | DRILL | agent-harness safety |

## 3. What was created
| Project | Commit | Contents | Incidents | Effort |
|---|---|---|---|---|
| buildevent | `baf46ea` | 10 tickets (M1 = the real Serializable/500 bug on main; S2 offline check-in; S3 timeouts and bulkheads) · review (25) · navigation · agentic (M1) · full interview kit · `training/load/drop.k6.js` · `training/tools/drop-sim.mts` (real services in-process against real Postgres) | 5 | ~50–60 h |
| buildermentor | `e6b3925` | 10 tickets (J3 eval case, M1 offline retrieval eval + golden set, M2 prompt versions, M3 budget as a real ceiling, M4 one retry/timeout policy, S1 eval-gated release, S2 multi-provider fallback + LLM observability, S3 injection defense) · review (23) · navigation · agentic (M4) · full interview kit · **runnable regression tests** in `_answers/regression-tests/` | 5 | ~45 h |
| aicallhelper | `5010b59` | review (builds on the repo's own `docs/REVIEW.md`; 5 of its 9 MEDIUM+ findings are now fixed) · mini interview kit with a **latency budgets for AI features** set | 2 | ~5 h |
| aiheartbeat | `fcbf2af` | agent-harness review (15) · mini kit with a **"how do you safely run coding agents in automation"** set | 2 | ~5 h |

**Git hygiene.**
- Every commit touches only `training/` (checked).
- Your uncommitted work is intact: buildevent 7, buildermentor 5, aiheartbeat 6 (after the recovery above).
- Nothing was pushed, and no containers or worktrees are left.

**Incident symptoms** (causes sealed in `_answers/`):

*buildevent*
1. "We fixed the 500s", but reserve now spins for 15 s and most buyers still fail.
2. "Sold out" with 480 tickets unsold, and no errors.
3. A slow Stripe makes door check-in at *another* event fail.
4. A read-only availability endpoint gets 3× slower.
5. Tickets have no QR code for about 10 minutes.

*buildermentor*
1. Citations are unrelated to the question, only for big books.
2. The invoice is 4× the app's own cost ledger.
3. Study submits fail with 400s while job failures drop to zero.
4. An item tells a learner to visit a website, built from material they never uploaded.
5. Item banks are 3× over target and spend doubles.

*aicallhelper*
1. Tokens are billed for answers that were superseded and never finished.
2. Stop doesn't reliably stop the Anthropic request.

*aiheartbeat*
1. The tool allowlist is widened, re-opening an injection path.
2. A hung agent process survives the "killed" log.

## 4. Verification (the strongest batch so far)
| Project | Verified |
|---|---|
| buildevent | Real Postgres 18 (native, port 5451) plus Docker Redis. `main` itself fails under load: 40 concurrent reserves give 35 × 500 (Serializable P2034). **Every incident measured:**<br>• 001: p95 3.6 → 14.3 s, 175 × P2028 across 200 buyers<br>• 002: expiry schedule evicted after about 1,000 cache writes<br>• 003: unrelated reads 96 ms → 10 s, P2024<br>• 004: 972 → 334 req/s, with lock waits<br>• 005: about 13 QR/s at concurrency 1<br>**Not run:** k6 (not installed), web tests. |
| buildermentor | 38/38 tests and typecheck. Incidents 001–004: each regression test passes on main and fails on its branch. Incident 005 reproduced with real pg-boss 10.4.2 plus a throwaway Postgres container: 1 job ran its handler 4× and still ended "failed". No real LLM API was called. |
| aicallhelper | 001: vitest 53/53 → 51/53. 002: `cargo test -p app-core` 8/8 → 7/8 (a second billed request fires after cancel). |
| aiheartbeat | 001: `config.test.ts` 9 → 8 passing. 002: 5 existing tests fail deterministically. A third incident was **abandoned** because it wouldn't reproduce, rather than shipping an untested claim. |

## 5. Real defects found (documented, NOT fixed)

**buildermentor: most serious**
- **Generated items are shared across all users.** The `items` table has no owner, so questions built from one user's private upload are served to everyone, and a prompt injection in one upload reaches every user.

**buildermentor: other**
- **SSRF** in URL ingest.
- The budget is a pre-check, not a ceiling, and embeddings aren't metered.
- Retries multiply across the SDK, the app and pg-boss, with no timeouts.
- Grading failures are scored as 0 while the job reports success.
- Every `ZodError` becomes a 400.
- The README claims don't match the code (a 20 s budget, full logging, "all calls through `callLlm`").

**buildevent**
- The README claims optimistic locking, but every conflict is a 500.
- Expiry jobs are never imported.
- `npm run db:push` doesn't exist.
- The Stripe webhook verifies a re-serialized body, so it can't verify real events.
- The checkout stub never sets `clientSecret`.
- Pages silently fall back to demo data on errors.
- Order numbers come from `count(*)`.
- One shared 5-connection pool; a global per-IP limit that also throttles webhooks and scanners.
- bcrypt takes 1.3 s; the Stripe timeout is 80 s; Redis retries forever; `allkeys-lru` is incompatible with BullMQ.
- `config.ts:10-14` falls back to default secrets in **every** environment.

**aicallhelper**
- 2 of `docs/REVIEW.md`'s MEDIUM+ findings are still open; one HIGH wasn't re-verified.

**aiheartbeat**
- The report parser prefers the *last* fenced block, which quoted attacker text can spoof.
- Stale-action recovery keys off `created_at` instead of the actual start time.

**Secrets:** none real in any repo, but:
- buildermentor's `.env.example` sets `LLM_PROVIDER=anthropic`, so copying it switches to the paid provider.
- buildevent falls back to default secrets everywhere.

## 6. Existing learning docs: verdicts
| Repo | Verdict |
|---|---|
| buildevent | `docs/upskill/`: KEEP as background. The ladder supersedes its tickets, and it wrongly says the jobs run. · `astraupskill/`: KEEP (tied to your uncommitted change) |
| buildermentor | `astraupskill/` (yours, uncommitted): KEEP, as prerequisite reading for M1 |
| aicallhelper | `docs/REVIEW.md`: CONVERT (now a dated second reference in the blind-review compare) · 17 ADRs and `docs/learn`: KEEP (gated as spoilers) |
| aiheartbeat | `astraupskill/`, `dfableandopus/`: KEEP (they also held the hashes that made the recovery possible) |

## 7. Status after four batches (see `apprenticeship/COMPETENCY_GRAPH.md`)
- **20 projects** turned into training material: 58 incident branches, 17 blind reviews, about 90 ladder tickets, 8 full + 9 mini interview kits, and 15 central curriculum pages.
- **Saturated (stop adding):**
  - authz/IDOR
  - concurrency races
  - idempotency/outbox
  - authn/security
- **Now good:**
  - query plans
  - migrations
  - observability (operated)
  - load/back-pressure
  - frontend performance
  - realtime
  - API versioning
  - AI/LLM features
  - agent safety
- **Still thin:**
  - **deploying to a real cloud and operating it** (every cloud item is still a design)
  - **SQL Server** (translation only)
  - **accessibility beyond one lab**
  - **real upstream contributions** (0)
- **Suggested next step: stop generating and start doing.** More batches would mostly repeat covered skills.
  The best remaining steps are *executions*, not new material:
  - **Deploy one lab for real:** gitjira-app to AWS, or atlas to Azure (its S1 ticket).
  - **SQL Server:** add a provider to atlas.
  - **Open the first Outline PR.**
  - If you want another batch anyway: `relay` (durable execution) and `folio` (CRDT/offline sync) are the only distinct topics left in the archive.

## 8. What to do first from B04 (about 1.5 weeks part-time)
1. **buildevent M1:** fix the real Serializable → 500 bug on `main` under `drop-sim`, then do INC-001 (retry storm) and INC-003 (pool exhaustion) with curriculum page 14.
2. **buildermentor M1:** build the offline retrieval eval, then diagnose INC-001 with it. This is the "evals before vibes" lesson.
3. **buildermentor INC-004 + ticket S3** (prompt injection and trust levels). Page 15.
4. **aicallhelper INC-001/002:** cancellation and billing. Short, and every test is runnable.
5. **aiheartbeat INC-001, plus the "safely running agents" interview set.** Then re-read §1 of this report: it's a live example of why the rules exist.
