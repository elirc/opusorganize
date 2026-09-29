# buildermentor (ShipShape): B04 report

**Tier:** LAB (Phases 2, 3, 4 and 5) · **Batch focus:** AI-backend engineering (the portfolio's LLM lab) · **Repo:** `C:\Users\Owner\Desktop\buildermentor` (own `.git`, no remote, nothing pushed)

## What I created
Everything is under `C:\Users\Owner\Desktop\buildermentor\training\` (55 files, committed on `main` as **e6b3925** "training: add B04 apprenticeship materials", a pathspec commit of `training/` only).
- `README.md`: index, incident table, suggested order, about 55–60 h estimate.
- `ladder/`: README + 10 tickets.
  - J1: semantic MCQ validation.
  - J2: meter embeddings.
  - J3: grader hallucinated-credit reconciliation + eval case.
  - M1: offline retrieval eval harness + golden set.
  - M2: content-hashed prompt versions.
  - M3: budget reserve/settle.
  - M4: one retry/timeout policy + honest job failures.
  - S1: eval-gated prompt release.
  - S2: multi-provider fallback + LLM observability.
  - S3: prompt-injection defense for uploads.
- `review/EXERCISE.md` and `COMPARE.md`; `_answers/review.md` has 23 ranked findings + a tests section, with AI-smell tags.
- `incidents/001..005-*.md`: symptom-only briefs.
- `navigation/`: `ARCHITECTURE.md` (3 traced flows, data model, boundaries, tests, build), `FIRST_CHANGE.md`, `TRADEOFFS.md` (5 "Why?" drills), `CHANGE_REQUEST.md` ("Why was this question generated?" + per-learner report).
- `agentic/`: `WORKFLOW.md` (M4 via implementer + adversarial reviewer), `VERIFY_AI_OUTPUT.md` (ShipShape-specific checklist).
- `interview/`: `PROJECT_STORIES.md` (5), `TECHNICAL_QUESTIONS.md` (20, incl. a React polling question), `SYSTEM_DESIGN.md` (5,000 learners), `MOCK_DEFENSE.md`, `FLASHCARDS.md` (25).
- `_answers/`: one sealed file per ticket and incident, review, navigation change request, agentic rubric, technical questions, flashcards. Also `regression-tests/` (4 runnable Vitest regression tests used to verify the incidents) and `inc005-pgboss-expiry.mjs`.

## Incident branches (all based on 98aca37; small single-purpose diffs)
| Branch | Commit | Symptom (not cause) |
|---|---|---|
| `training/incidents/001-embed-batch-order` | 4bbc188 | citations unrelated to the question, only for big books; nothing red |
| `training/incidents/002-llm-retry-usage` | a8b4fac | provider invoice 4× ShipShape's own cost ledger; daily budget never trips |
| `training/incidents/003-loose-gen-schema` | c9c4d2c | study submits fail with "validation" 400s; generation job failures drop to zero |
| `training/incidents/004-grounding-in-system` | f162cc7 | an MCQ tells a learner to visit a website, from material she never uploaded |
| `training/incidents/005-genjob-expiry` | c14f85d | item banks 3× over target, generate jobs "failed", spend doubled |

## Verification
- `pnpm install --frozen-lockfile` in the main tree (once): OK. The `canvas` native build fails on Windows, which is harmless and already known.
- **Main tree:** `vitest run` gives 38/38 green (30 committed + 8 from the owner's uncommitted test), and `tsc --noEmit` passes. Note the main tree includes the owner's uncommitted `retrieve.ts` edits.
- **All 5 incident branches:** `tsc --noEmit` exit 0. I ran it in worktrees with junctioned `node_modules`, and removed the junctions and worktrees afterwards.
- **INC-001–004 are RUN-VERIFIED.** The regression tests in `_answers/regression-tests/` pass on HEAD and fail on each branch:
  - 001: vectors out of order across batches with a jittered fake embedder.
  - 002: 3 calls, maxTokens 8000/16000/32000; billed 18000/24000 tokens but recorded 9000/8000.
  - 003: a malformed 3-option MCQ is inserted (2 inserted, 1 invalid).
  - 004: the poisoned chunk lands in `system`, and the mock produces 40 items for count=2.

  All four use fakes and mocks only.
- **INC-005 is RUN-VERIFIED for the mechanism.** Docker became available mid-task, so I ran the repo's pg-boss 10.4.2 against a throwaway `postgres:16-alpine` container (`buildermentor-training-db`, port 55439, **removed afterwards**). With the branch's option shape scaled down: 4 runs of one job, 4 inserts, 2 concurrent handlers for the same job, and the final state `failed` "handler execution exceeded". I did **not** run the full `topUpBank` path with a slow fake provider (UNVERIFIED).
- **No real LLM or embedding API was called at any point.**
- **UNVERIFIED (static only):**
  - review finding 8 (HNSW post-filter recall loss): needs a pgvector image and multi-user data;
  - the SSRF finding;
  - real-model behaviour for INC-004 (the brief uses a narrated fixture);
  - all ladder answers (reference designs, not implemented).
- The training commit lacks the Co-Authored-By trailer because I used the brief's exact `git commit -m` command. The incident branch commits have it.

## Issues found in the project
- **Secrets:** none. There is no `.env`. `.env.example` has placeholders only. `apps/api/src/env.ts:8` has a fail-open `SESSION_SECRET` default (a dev string, not a real secret). `.env.example` sets `LLM_PROVIDER=anthropic` while the code default is `mock`, so copying it switches to the paid provider.
- **Presented as working, but isn't (or only partly):**
  - The README says "Every LLM call flows through one `callLlm` wrapper". Embeddings bypass it, so they are unmetered and unbudgeted.
  - The README says "raw request/response on disk". Only the last response is logged.
  - "Cost guardrails" are a pre-call check, not a ceiling: concurrent calls race it, and the cache only increments existing entries.
  - `composer.ts`: the "20s budget" isn't enforced inside a call.
  - `nightlyRun`'s `catch { break }` claims "budget exhausted" but stops on any error.
  - `jsonSchema: {}` is plumbed but unused.
  - `OpenAiProvider` is a stub selectable via env (the README does say "stub").
  - CI provisions pgvector, but no test uses the DB. The Playwright e2e is not run in CI.
- **Most serious design issue:** `items` has no owner, so questions generated from user A's private upload are served to user B (a confidentiality issue plus the path for multi-user prompt injection). Also: SSRF in URL ingest; simulator grading failures are scored as 0 and the job reports success; `ZodError` → 400 masks corrupt stored data; the migration and Drizzle schema drift (index names, env-driven vector dimension).
- Untouched owner work in the tree: modified `README.md` and `apps/api/src/rag/retrieve.ts`, untracked `apps/api/test/ingest-retrieval.test.ts`, `apps/api/test/fixtures/` and `astraupskill/`.

## Skill links (for COMPETENCY_GRAPH)
This needs a new row, **"AI/LLM integration (evals, cost, latency, failure modes)"**. Today it has 0 items in the graph, and this lab adds about 20.
- **AI/LLM: structured output validation** → `ladder/J1`, `incidents/003-loose-gen-schema`, TQ 2, 3
- **AI/LLM: evals / golden sets** → `ladder/M1`, `ladder/J3`, `ladder/S1`, `incidents/001-embed-batch-order` (eval that catches the class)
- **AI/LLM: RAG retrieval quality** → `ladder/M1`, `incidents/001`, review #8, #9, TQ 6–9
- **AI/LLM: cost and token budgets** → `ladder/J2`, `ladder/M3`, `incidents/002-llm-retry-usage`, TQ 1, 20
- **AI/LLM: timeouts, retries, fallback** → `ladder/M4`, `ladder/S2`, `incidents/002`, `incidents/005`, TQ 11–13
- **AI/LLM: prompt versioning and release** → `ladder/M2`, `ladder/S1`
- **AI security: prompt injection** → `ladder/S3`, `incidents/004-grounding-in-system`, review #1, #2, TQ 18
- **Observability (LLM)** → `ladder/S2`, `incidents/002` (a ledger that lies; links curriculum 09)
- **Async jobs (pg-boss failure handling)** → `incidents/005-genjob-expiry`, `ladder/M4` (a saturated skill; the angle here is cost of duplicates and non-cancellable handlers)
- **Security OWASP (SSRF)** → review #3, TQ 19
- **Web/React** → TQ 5 (unbounded polling in `SimRunner.tsx`), `navigation/CHANGE_REQUEST.md`
- **Agentic engineering** → `agentic/WORKFLOW.md` (M4), `agentic/VERIFY_AI_OUTPUT.md`
- **Code review** → `review/` (23 findings)
- **Codebase navigation / design trade-offs** → `navigation/*` (5 "Why?" drills)
- **Interview** → `interview/*` (full kit)

## Curriculum needs (one central page each; not written)
1. **"Evaluating LLM features offline"**: golden sets, paired comparison, recorded fixtures vs live canaries, and LLM-as-judge drift. Worked examples: ShipShape M1/S1/J3.
2. **"Where LLM money goes: retries, tokens and reconciliation"**: multiplying retry layers (SDK × app × queue), usage accounting per attempt, reserve/settle budgets, and reconciling against the provider. Worked examples: ShipShape INC-002, M3, M4.
3. **"Prompt injection: trust levels and isolation"**: untrusted-input classification, why prompt wording is not a control, output guards, and per-tenant isolation of generated content. Worked examples: ShipShape INC-004, S3.
4. (Backlog candidate) **"Queue timeouts are not kill switches"**: visibility timeouts, non-cancellable handlers, AbortSignal plumbing. ShipShape INC-005 plus any BullMQ/pg-boss project.

## Existing learning-doc trees
- `astraupskill/` (**uncommitted**, owner's; 7 chapters + `evidence/` + `snapshots/`; a retrieval-boundary trace course tied to the uncommitted `retrieve.ts` refactor and `ingest-retrieval.test.ts`): **KEEP.** Link it from the graph as a prerequisite reading for M1. It is specific and non-generic, and it overlaps M1 only on retrieval contracts, not on evals. Note: M1 asks the learner to extract `rankCandidates` and to coordinate with the uncommitted `rankRetrievedRows` rather than clobber it.
- No other doc trees exist (README only).

## Honest caveats
- The incident briefs' logs and metrics (invoice numbers, user quotes, SQL outputs) are narrated. The code behaviour behind them is verified as described above.
- The INC-004 "real model obeys the injection" behaviour is asserted from well-known LLM behaviour, not reproduced. Only the prompt-construction change and mock steerability were run.
- Ladder answers are reference designs. None were implemented, so their code sketches are unverified.
- The machine is slow (the Vitest suite takes about 64 s, `tsc` a few minutes per worktree), so I didn't run the web build or Playwright.
