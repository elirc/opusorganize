# 15 — Shipping LLM features: evals, cost, latency, injection, agent safety

**1. Evals before vibes.** Keep a golden set with an offline harness: retrieval recall@k, citation grounding and schema validity. Run it on every prompt, model or chunking change, and gate the release on it.
- buildermentor `training/ladder/M1` (eval harness), `S1` (eval-gated prompt release).
- `training/incidents/001-embed-batch-order`: citations go wrong only for big books, and nothing alerts. An eval would have caught it.

**2. Structured output is untrusted input.** Validate it against a schema. A validation failure on *our own* stored data is a 500, not a 400.
- buildermentor `training/incidents/003-loose-gen-schema`: study submits return 400s while job failures drop to zero.
- The real finding is that every `ZodError` becomes a 400.

**3. Money is a first-class metric.**
- Record tokens and cost per call, *including embeddings and retries*.
- Treat a budget as **reserve → call → settle**, not a pre-check that concurrent calls race past.
- Reconcile the ledger against the provider invoice.
- Examples:
  - buildermentor `incidents/002-llm-retry-usage` (invoice 4× the ledger) and `ladder/M3`.
  - aicallhelper `incidents/001-ask-supersede-cancel-dropped`: a superseded answer keeps streaming and billing.

**4. Latency budgets and cancellation.**
- Set a budget for time to first token.
- Stream end to end; never buffer the whole answer.
- Stop must cancel the upstream request at **every** retry point.
- Timeouts belong on every layer, but retries on only one ([14](14-load-backpressure-timeouts.md)).
- Examples: aicallhelper `incidents/002-retry-cancel-race` (Stop doesn't stop the request) and its interview set on latency budgets.

**5. Prompt injection: trust levels.**
- User-uploaded or retrieved text is **data**. Never put it in the system role.
- Isolate by tenant: generated artifacts derived from private input must be owner-scoped.
- Treat tool calls triggered by model output as untrusted.
- Examples:
  - buildermentor `incidents/004-grounding-in-system`: an item tells a learner to visit a site from material they never uploaded.
  - Real finding: the `items` table has no owner, so one user's upload reaches everyone.
  - `ladder/S3`.
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
