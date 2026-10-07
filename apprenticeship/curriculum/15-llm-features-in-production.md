# 15 — Shipping LLM features: evals, cost, latency, injection, agent safety

**Where these repos live now (checked 2026-10-06):** buildermentor → `elirc/buildermentor` (`main` @ `8fcdb9d`; incident branches 001–005 on GitHub) · aicallhelper → `elirc/aicallhelper` (`main` @ `a86e4c2`; incident branches 001–002 on GitHub) · aiheartbeat → `elirc/aiheartbeat` (default branch `master` @ `ca5564f`; incident branches 001–002 on GitHub).

**1. Evals before vibes.** Keep a golden set with an offline harness: retrieval recall@k, citation grounding and schema validity. Run it on every prompt, model or chunking change, and gate the release on it.
- buildermentor `training/ladder/M1-retrieval-eval-harness.md` (eval harness), `S1-eval-gated-prompt-release.md` (eval-gated prompt release).
- `training/incidents/001-embed-batch-order`: citations go wrong only for big books, and nothing alerts. An eval would have caught it.

**2. Structured output is untrusted input.** Validate it against a schema. A validation failure on *our own* stored data is a 500, not a 400.
- buildermentor `training/incidents/003-loose-gen-schema`: study submits return 400s while job failures drop to zero.
- The real finding is that every `ZodError` becomes a 400 (`elirc/buildermentor: apps/api/src/server.ts:61-62`, still true at `8fcdb9d`).

**3. Money is a first-class metric.**
- Record tokens and cost per call, *including embeddings and retries*.
- Treat a budget as **reserve → call → settle**, not a pre-check that concurrent calls race past.
- Reconcile the ledger against the provider invoice.
- Examples:
  - buildermentor `incidents/002-llm-retry-usage` (invoice about 4× the ledger; the brief's daily ratio reaches 4.4) and `ladder/M3-budget-as-a-ceiling.md`.
  - aicallhelper `incidents/001-ask-supersede-cancel-dropped`: a superseded answer keeps streaming and billing.

**4. Latency budgets and cancellation.**
- Set a budget for time to first token.
- Stream end to end; never buffer the whole answer.
- Stop must cancel the upstream request at **every** retry point.
- Timeouts belong on every layer, but retries on only one ([14](14-load-backpressure-timeouts.md)).
- Examples: aicallhelper `incidents/002-retry-cancel-race` (Stop doesn't stop the request) and its interview set on latency budgets (`training/interview/TECHNICAL_QUESTIONS.md`).

**5. Prompt injection: trust levels.**
- User-uploaded or retrieved text is **data**. Never put it in the system role.
- Isolate by tenant: generated artifacts derived from private input must be owner-scoped.
- Treat tool calls triggered by model output as untrusted.
- Examples:
  - buildermentor `incidents/004-grounding-in-system`: an item tells a learner to visit a site from material they never uploaded.
  - Real finding: the `items` table has no owner, so one user's upload reaches everyone.
  - `ladder/S3-prompt-injection-defense.md`.
- A separate real finding in buildermentor: URL ingest is an SSRF.

**6. Running coding agents in automation (agent harness safety)**
- Grant least-privilege tool allowlists. Writing via `gh` is a privilege escalation.
- Put hard timeouts on agent processes that **kill the process tree**, and use single-run locks/leases.
- Never trust the agent's self-reported success; verify artifacts.
- Keep secrets out of prompts and logs.
- Keep a human gate on irreversible actions.
- Examples:
  - aiheartbeat `training/incidents/001-gh-write-allowlist-leak`: `Bash(gh pr comment:*)` re-opens an injection path.
  - `002-timeout-no-kill`: a hung `claude` process survives the "killed" log.
  - Real findings: the report parser prefers the *last* fenced block, which quoted attacker text can spoof; stale-action recovery keys off `created_at`, not the actual start time.
- **Also a lesson from this very apprenticeship run:** an agent's `rm -rf node_modules` followed Windows workspace junctions and deleted real source. Destructive commands need guardrails even for "cleanup". See `batch4report/REPORT.md`.

---

## Worked trace: one LLM call in buildermentor (`apps/api/src/llm/callLlm.ts` @ `8fcdb9d`)

1. **Budget pre-check.** `:91` calls `wouldExceedBudget(userId)`. In `apps/api/src/llm/budget.ts:37-41` that means "today's spend ≥ budget", where today's spend comes from an in-memory per-user cache that is only recomputed hourly (`budget.ts:5-19`). The check reserves nothing. N concurrent calls all see the same spend and all pass. On refusal, `callLlm` writes an `over_budget` row (`:92-101`).
2. **Provider.** `:105` picks Anthropic, OpenAI or a mock (`:23-31`). The Anthropic client is built with only an API key (`providers/anthropic.ts:9`), so the SDK's own retry and timeout defaults apply underneath everything.
3. **Schema-repair loop.** `:117` allows two attempts. Each response is parsed leniently (`tryParseJson`, `:39-59`, which strips fences and salvages the first `{…}`), then checked with `schema.safeParse` (`:131`). On failure the model's answer and the validation error go back in as conversation turns (`:136-141`).
4. **Accounting.** `:128` *sums* usage across attempts. That is exactly the line INC-002's PR broke by overwriting it.
5. **Ledger row.** On success or invalid JSON, `:183-197` inserts one `llm_calls` row with tokens, cost, latency and status. A thrown provider error writes a row with `status: "error"` (`:145-158`). `addToSpendCache` (`:198`) updates the cached spend only if the user already has a cache entry (`budget.ts:22-25`).
6. **Failure mapping.** `apps/api/src/server.ts:61-62` maps any `ZodError` to **400**, `BudgetExceededError` to 402 (`:66-69`) and `InvalidJsonError` to 502 (`:71-74`).

Where the untrusted text goes: the grounding chunks are rendered into `contextBlock` (`apps/api/src/llm/prompts/generate.ts:20-31`), which is interpolated into the **`user`** message (for example `:52-53`), not into `system`. INC-004's branch changes `prompts/generate.ts` and `providers/mock.ts` (+23/−9) to move that material into the system role.

## Failure mode, step by step: INC-003 (a "helpful" loose schema)

1. Before the PR, one malformed item in a generated batch failed the whole `safeParse`. That gave `InvalidJsonError` and a failed pg-boss job (the brief counts 23 the week before).
2. The PR, "don't discard a whole paid batch when one item is malformed", replaces the five modality schemas in `items/generate.ts` with one `.passthrough()` envelope. The comment claims items are "checked individually below", but the only check is `if (!stem) continue;` (sealed answer). The PR description describes code that doesn't exist.
3. The malformed items are stored in `items`. The `invalid_json` rate falls from 6.1% to 0.0%, and failed jobs fall to 0. Both dashboards "improve".
4. A learner is served one of those items. On submit, `apps/api/src/study/attempts.ts:100` (`McqPayload.parse(payload)`) or `:139` (`RecallPayload.parse`) re-validates the stored payload with the strict schema, and it throws a `ZodError`. The grading functions in `study/grading.ts:60-151` do the same for the other modalities.
5. `server.ts:61-62` turns that into **400 `validation`**. To on-call, a 400 is the client's fault, so the 5xx rate stays flat at 0.1% and nothing pages. The brief's access log shows 400s at 6.2%, up from 0.3%.
6. Every user who gets a poisoned item fails on it. The fix keeps the good N-1 items, rejects the bad one *at generation time*, and treats a `ZodError` on our own stored data as a 500.

## Goal + **Check** ladder

1. **Goal (junior):** say what a 400 means and who is to blame. **Check:** read `server.ts:55-75` and write, for each branch, whether the error is the client's fault or ours. A `ZodError` from parsing a request body is the client's. A `ZodError` from re-validating a stored row is ours.
2. **Goal (junior):** find the race in the budget. **Check:** in `budget.ts:37-41` and `callLlm.ts:91`, show that there is no reservation step. Describe two concurrent calls that both pass with $0.01 of budget left. M3's ticket is the reserve → settle fix.
3. **Goal (junior → mid):** list the three cancellation checks in aicallhelper. **Check:** `elirc/aicallhelper: src-tauri/core/src/llm/retry.rs:76` is `with_retry_once`. The checks are at `:88` (before any attempt), `:100` (after the first failure, before any retry), and `:120` (after the second failure). INC-002's failing assertion `left: [0, 1] right: [0]` means a second request went out after cancel. Say which check the branch removes, then confirm with `git diff main origin/training/incidents/002-retry-cancel-race`.
4. **Goal (mid):** audit an agent allowlist. **Check:** `elirc/aiheartbeat: packages/shared/src/config.ts:26-36` allows only read `gh` subcommands, and `:51-67` denies write verbs, including `Bash(gh pr comment:*)` at `:61`. The INC-001 branch moves that entry from the deny list to the allowlist, with a "lets the agent immediately ack a PR" comment (verified by diffing the pushed branch). Explain why issue #61's body ending up in a PR comment is an injection path, not a coincidence.
5. **Goal (mid → senior):** design S3's defence. **Check:** your design keeps retrieved text in a delimited user-role block, scopes `items` by owner, validates outputs, and adds an eval case built from INC-004's poisoned chunk.

## Verified senior findings

- **No owner on shared artifacts.** `apps/api/src/db/schema.ts:125-154` defines `items` with `topicId`, `payload`, `sourceChunkIds` and `generationCallId`, but **no `userId`**. The next table, `item_memory`, does have one (`:159`). Items generated from user A's private upload can be served to user B. That's a confidentiality issue, and it is the delivery path for multi-user prompt injection.
- **SSRF in URL ingest.** `apps/api/src/ingest/parse.ts:89-93` calls `fetch(url, { redirect: "follow", signal: AbortSignal.timeout(30_000) })` with no scheme, host or private-IP check, and follows redirects. The timeout is there, but the allowlist isn't.
- **Agent harness details (aiheartbeat):** `packages/core/src/prompt/parse.ts:4-25` prefers the *last* ```json fence, so a quoted attacker block late in the output can win. `packages/shared/src/db/actions.ts:177` fails "stale" executing actions by `created_at`, not by when execution started. On `main`, the timeout path calls `killTree(child)` (`packages/core/src/claude/invoke.ts:291-292`), which uses `taskkill /T /F` on Windows (`:251`). The INC-002 branch deletes that call and replaces it with a comment claiming the runtime will kill the process.

## Debugging scenario: "the provider invoice is 4× our ledger"

(1) Cross-check two independent signals. INC-002's sealed answer notes that 21.9k recorded output tokens at about 100 tok/s is about 220 s, but the recorded latency is 468 s, so about 26k more tokens were generated than recorded. (2) Read the accounting line (`callLlm.ts:128`) on the deployed commit: is usage summed or overwritten? (3) Count retry layers: SDK, `callLlm`'s loop, pg-boss `retryLimit` (`jobs/boss.ts:31`). (4) Add a reconciliation job that compares the provider's usage API with `sum(cost_usd)` and alerts at ±10%, as the sealed answer proposes.

**Honesty cap:** B04 run-verified buildermentor 001–004 via regression tests and 005 against a real pg-boss + Postgres container. aicallhelper's tests failed as designed (vitest 51/53, cargo 7/8). On 2026-10-06 I only re-read the code and diffed the pushed aiheartbeat incident branches. I ran nothing. The SDK default timeout and retry values are library facts, not something verified in these repos.
