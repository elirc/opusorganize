# pulse — B02 report

**Project:** `C:\Users\Owner\Desktop\gitvg\pulse` (Node/TS pnpm workspace — PostHog/Mixpanel-style analytics
course repo: `apps/{ingest,consumer,api,jobs,web}`, `packages/{auth,config,db,flags,insights,loadgen,sdk,shared,
stream}`, `docs/`, `load/`)

**Tier:** DRILL (Phase 3: blind review + incidents, + small Phase 5 interview kit per B02 brief). Focus per
orchestrator instruction: **2 NEW incidents biased to performance/ingestion throughput and observability**
(e.g. ingest backlog, slow aggregation query, unbounded batch) — not this repo's own ledgered flaws.

## What was created

All under `<repo>\training\`, committed on `main` via pathspec commit (no other working-tree changes touched —
tree was already clean at session start):

- `training/review/EXERCISE.md` + `training/_answers/review.md` (17 ranked findings, evidence-cited) +
  `training/review/COMPARE.md`
- `training/incidents/001-pipeline-health-severity-inversion.md` (symptom-only brief) +
  `training/_answers/001-pipeline-health-severity-inversion.md` (root cause, diagnostic path, fix, regression
  test, postmortem paragraph)
- `training/incidents/002-rollup-eligibility-array-identity.md` (symptom-only brief) +
  `training/_answers/002-rollup-eligibility-array-identity.md`
- `training/interview/PROJECT_STORIES.md` (5 STAR prompts, learner completes after doing the work) and
  `training/interview/TECHNICAL_QUESTIONS.md` (10 questions, all citing real files) +
  `training/_answers/TECHNICAL_QUESTIONS.md` (terse answer key)
- `training/README.md` — index, suggested order (~2.5–3.5h), spoiler warning, existing-doc verdicts

Commit: `67fb143` — "training: add B02 apprenticeship materials" (11 files, +732).

## Incident branches

- `training/incidents/001-pipeline-health-severity-inversion` (commit `3f8b1a7`) — **symptom:** consumer lag
  crossed the documented critical threshold (`pulse_stream_backlog` ≥ 250,000, per
  `docs/ops/dashboards/pipeline.json`) and stayed there for 40+ minutes, but `assessPipeline`'s reported status
  stayed `"degraded"` the whole time, so after-hours on-call paging (configured to fire only on `"critical"`)
  never triggered — on-call found out from a customer support ticket instead.
- `training/incidents/002-rollup-eligibility-array-identity` (commit `8188f38`) — **symptom:** `/insights/trend`
  p95 roughly tripled (410ms → 1,180ms) and ClickHouse cluster CPU rose from ~35% to ~71%, with every response
  still correct (200, right data) — the `x-served-by` debug header showed `raw` for query shapes that should
  read `rollup`, matching the ~70%-of-load hot/stable shapes this repo's own `docs/perf/query-shape-audit.md`
  documents as the rollup's whole reason to exist.

Both branches are built on `HEAD` (`0b6d520`, sprint-15) via git worktrees under the session scratchpad,
committed there, then the worktrees were removed (`git worktree remove`); the branches remain in the repo.
Neither reuses a mechanism from `docs/sprints/flaw-ledger.md`'s five entries (retry jitter, per-event enrichment,
client timestamp trust, live-feed indexing, share-token expiry — all already harvested) — see `training/README.md`
for the explicit spoiler warning.

Each incident is a single-file, single-purpose diff (5 and 4 lines changed respectively) disguised as a small,
plausible, well-intentioned PR ("widen the warn band for earlier visibility," "name the empty-filters check for
readability") — both are directly covered by pre-existing unit tests (`pipeline-health.test.ts:14`,
`rollup.test.ts`'s first `it` block) that would have failed on the bug had they been run before merge; the
incidents' own sealed answers make that gap ("tests existed, weren't run/weren't blocking") part of the lesson.

## Verification

- Traced both bugs by hand against the actual functions and their existing test files — no invented APIs; both
  are real, minimal, single-file regressions in genuinely pure/unit-tested code (`packages/shared/src/
  pipeline-health.ts`, `packages/insights/src/rollup.ts`).
- **BUILD: UNVERIFIED (no deps installed).** Confirmed no `node_modules` anywhere in the repo. Per B02 rules, no
  TS agent besides gitjira-app runs `npm ci`; did not install. Both new diffs typecheck by inspection (string/
  boolean logic only, no new imports or signature changes) but `tsc`/`vitest` were not actually run. Flagged in
  `training/README.md` and both sealed answers.
- `git worktree list` and `git branch --list "training/incidents/*"` confirmed both branches exist and worktrees
  were cleanly removed; `git status --short` on the main tree is clean after the `training/` commit (only
  `training/` staged and committed, verified before commit).

## Issues found in the project

(Full ranked list in `training/_answers/review.md`; sealed, not reused as answers here beyond a summary. Findings
1-9 are the assigned perf/ingestion/observability bias; 10-17 are broader, lower-priority findings.)

- **Real, currently unfixed, non-planted issues** worth flagging separately from the incidents (all with
  file:line evidence in the sealed review):
  - `apps/ingest/src/server.ts:163-181` — a batch POST (up to 100 events) issues one sequential, awaited Redis
    `XADD` per event (`packages/stream/src/redis.ts:34-37` has no pipelined/multi variant) — N round-trips on the
    hot path where the file's own comment targets "p95 < 15ms."
  - `apps/consumer/src/worker.ts:63-77` — enrichment is explicitly vectorized across the batch (the ledger's own
    harvested flaw #2 fix), but the very next stage, identity resolution, is NOT — one `await` per event, each a
    potential DB round-trip on a cache miss. Same bug shape the ledger already fixed once, not applied here.
  - `apps/consumer/src/identity.ts:44` and `packages/auth/src/resolver.ts:53` — both caches are plain `Map`s with
    only lazy TTL-at-read eviction, no size cap — unbounded growth for high-cardinality anonymous ids / long-lived
    processes, with no metric exposing cache size.
  - `apps/consumer/src/columnstore.ts` — `BufferedColumnStore`'s doc comment says it "flushes on size or time";
    the code only flushes on size (`maxRows`, default 10,000). No timer exists anywhere in `apps/consumer/src`.
    Under moderate (sub-10k-events-between-restarts) traffic, accepted events can sit unflushed — and therefore
    invisible to ClickHouse, dashboards, and the loss-reconciliation job — indefinitely. **Presented as working
    (doc comment) but isn't (code)** — flagged explicitly as an old-AI-generated-code smell.
- No secrets found (grepped for common secret/key/password literal patterns and `.env*` files — none present;
  the repo, like its siblings, ships no `.env` files, keys are read via `env.ts` from process env only).
- Nothing else presented as definitively working that isn't, beyond the buffer-flush doc/code mismatch above —
  this is a well-hardened repo (15 sprints, 5/5 ledgered flaws already harvested), consistent with the
  batch-02 audit's structural read (`portfolio-audit/projects/batch-02.md`: "no old-AI-generated quality smells...
  at the structural level").

## Skill links (for COMPETENCY_GRAPH.md — not written there, per B02 rules)

- observability / alert-severity-ladder ordering → `training/incidents/001-pipeline-health-severity-inversion.md`,
  `training/_answers/001-pipeline-health-severity-inversion.md`, `training/interview/TECHNICAL_QUESTIONS.md` Q4
- performance / precompute-eligibility routing, reference-vs-value-equality footgun →
  `training/incidents/002-rollup-eligibility-array-identity.md`,
  `training/_answers/002-rollup-eligibility-array-identity.md`, `training/interview/TECHNICAL_QUESTIONS.md` Q9
- performance / batching-vs-sequential-round-trips (ingest + consumer identity resolve, real unfixed bugs) →
  `training/_answers/review.md` findings #1, #2; `training/interview/TECHNICAL_QUESTIONS.md` Q3
- observability / unbounded in-memory caches, doc-vs-code mismatch → `training/_answers/review.md` findings #3, #4
- data modeling / evidence-driven engine migration (PG→ClickHouse) → `docs/perf/load-report-pg-breaks.md`,
  `docs/perf/query-shape-audit.md`, `training/interview/PROJECT_STORIES.md` prompt 4,
  `training/interview/TECHNICAL_QUESTIONS.md` Q10
- code review / "tests exist and would have caught it, but weren't run before merge" → both incidents' sealed
  answers' "what let this merge" sections

## Curriculum needs (candidates for `apprenticeship\curriculum\`, not written)

- **"Threshold-ladder / severity-escalation correctness" page** — title suggestion:
  **`threshold-alerting-correctness.md`**. Scope (2 lines): *why if/else-if threshold checks must test the
  strictest bound first, how a "harmless" reorder silently disables a severity level, and how to structurally
  guard against it (shared helper + monotonicity test) rather than relying on manual ordering discipline.*
  Worked example: this project's incident 001.
- **"Reference vs. value equality" page** — title suggestion: **`reference-vs-value-equality.md`**. Scope (2
  lines): *why `=== []` / `=== {}` is a near-guaranteed bug in JS/TS, the difference between reference and
  structural equality, and a grep-able detection habit.* Worked example: this project's incident 002. This is a
  general JS/TS footgun likely to recur across the fleet (TS course repos) — worth checking if another project's
  DRILL/LAB pass in this batch already proposed something similar before duplicating the page.
- Both are small, single-purpose pages (this batch already has 5 central pages at similar scope:
  `01-transactional-outbox.md` through `05-verify-before-trust.md`) — not proposing anything sprawling.

## Existing learning-doc trees — verdicts

- `docs/sprints/` (`flaw-ledger.md`, `00-workflow.md`, `sprint-01.md`…`sprint-15.md`) — **KEEP**, flagged as a
  spoiler for this batch's exercises (it's the answer key for a different, already-solved flaw set the learner
  may have seen). Genuinely good material as a second worked example once this batch is done.
- `docs/audits/sprint-13-audit.md` — **KEEP**, same spoiler flag (likely discusses ledger-flaw harvest detail).
- `docs/perf/` (`baseline-01.md`, `baseline-02.md`, `load-report-pg-breaks.md`, `query-shape-audit.md`) —
  **KEEP**, not a spoiler (these document a real, already-executed migration decision, not answers to this
  batch's exercises) — actively cited from this batch's incident 002, interview questions, and curriculum-needs
  note above as excellent worked examples of evidence-driven performance decisions.
- `docs/ops/` (`dashboards/pipeline.json`, `postmortems/2026-07-consumer-stall.md`, `runbooks.md`, `backups.md`,
  `deploy.md`) — **KEEP**, actively cited from incident 001 and the review's observability findings; genuinely
  strong material (the postmortem is a good blameless-postmortem worked example, cited in PROJECT_STORIES.md
  prompt 5).
- `docs/adr/`, `docs/experiments/`, `docs/curriculum/`, `docs/threat-model.md`, `funnel-semantics.md`,
  `RETROSPECTIVE.md` — **KEEP**, out of scope for this DRILL pass; not evaluated in depth.

## Honest caveats

- BUILD/typecheck/test run were not actually executed (no `node_modules`, per B02 rule for non-gitjira-app TS
  repos) — both incidents are verified by careful manual type/identifier/control-flow tracing only, explicitly
  marked `BUILD: UNVERIFIED (no deps installed)` in the README and both sealed answers.
- The review covers the files most relevant to the assigned bias (ingest, consumer worker/identity/columnstore,
  pipeline-health, rollup routing, plus auth resolver and jobs reconciliation for a few broader findings) rather
  than an exhaustive repo-wide pass — `apps/web`, `packages/flags`, `packages/loadgen`, and most of
  `packages/insights`' funnel/retention/cohort compute were not deep-read this pass; a follow-up DRILL/READ pass
  on the read-side (`apps/api`'s remaining endpoints, funnel/retention correctness) would likely surface more.
- Incident severity/timeline numbers (backlog figures, p95 values, CPU percentages) in both incident briefs are
  constructed to be internally consistent with the repo's own documented thresholds and baselines
  (`pipeline.json`, `query-shape-audit.md`), not pulled from a real production run — flagged implicitly by their
  presentation as a synthetic on-call transcript, consistent with how the master prompt's incident format works
  for a course repo with no live deployment.
