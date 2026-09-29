# bazaar — B02 report

**Project:** `C:\Users\Owner\Desktop\gitvg\bazaar` (Node/TS pnpm workspace — e-commerce course repo:
`apps/{api,admin,storefront,worker}`, `packages/{cache,db,config,search,shared}`, `docs/`, `observability/`,
`deploy/`, `scripts/k6/`)

**Tier:** DRILL (Phase 3: blind review + incidents, + small Phase 5 interview kit per B02 brief). Focus:
2 NEW caching incidents (caching is the thinnest-drilled skill so far), deliberately distinct from this
repo's own ledgered flaws.

## What was created

All under `<repo>\training\`, committed on `main` via pathspec commit (no other working-tree changes
touched — tree was already clean at session start):

- `training/review/EXERCISE.md` + `training/_answers/review.md` (14 ranked findings, evidence-cited) +
  `training/review/COMPARE.md`
- `training/incidents/001-storefront-cache-tag-mismatch.md` (symptom-only brief) +
  `training/_answers/incidents/001-storefront-cache-tag-mismatch.md` (root cause, diagnostic path, fix,
  regression test, postmortem)
- `training/incidents/002-personalized-price-shared-cache-key.md` (symptom-only brief) +
  `training/_answers/incidents/002-personalized-price-shared-cache-key.md`
- `training/interview/PROJECT_STORIES.md` (5 STAR skeletons) and `training/interview/TECHNICAL_QUESTIONS.md`
  (10 questions, all citing real files)
- `training/README.md` — index, suggested order (~2.5–3.5h), spoiler warning, existing-doc verdicts,
  skill links

Commit: `4d6eb1f` — "training: add B02 apprenticeship materials" (10 files, +601).

## Incident branches

- `training/incidents/001-storefront-cache-tag-mismatch` (commit `2223d2c`) — **symptom:** storefront
  keeps showing a product's old price ~20+ minutes after the merchant fixed it in admin, well past the
  cache's 300s TTL; admin view and a cold process both show the correct price immediately.
- `training/incidents/002-personalized-price-shared-cache-key` (commit `e4c1a2a`) — **symptom:** a VIP
  customer's discounted price shows up on the public product page for non-VIP customers, but only for
  visitors who load the page within ~5 minutes of the VIP customer's own visit; the discount rule engine
  itself tests green in isolation.

Both branches are built on `HEAD` (`6464359`, sprint-15) via git worktrees under the session scratchpad,
committed there, then the worktrees were removed (`git worktree remove`); the branches remain in the repo.
Neither reuses a mechanism from `docs/sprints/flaw-ledger.md`'s two caching entries (#1 "no tag/dependency
tracking" harvested S06, #3 "no stampede protection" harvested S06) — see `training/README.md` for the
explicit distinction (001 = tag identity mismatch between read/invalidate paths; 002 = per-user data cached
under a key built for shared/anonymous data).

Each incident adds one new ~35–65 line source file wiring the previously-unused `@bazaar/cache` package
into `apps/api` (plus an `apps/api/package.json` dependency add and an `index.ts` export line) and one
happy-path-only test file that would plausibly have passed review without catching the bug.

## Verification

- Confirmed via `grep` that before this batch, `@bazaar/cache` (`packages/cache/src/index.ts` —
  `ReadThroughCache`, `TaggedCache`, `SingleFlight`, `ProtectedReadThroughCache`,
  `StaleWhileRevalidateCache`, `HotSetWarmer`, `TrendWarmer`) had **zero call sites** anywhere under `apps/`
  — it was built and unit-tested in isolation only. This is why both incidents needed to add the wiring
  themselves as part of the "PR" rather than editing existing call sites.
- Traced both bugs by hand against real exports (`entityTag`, `cacheKey`, `safeStorefrontCacheKey`,
  `CatalogPublisher.productPublished`, `discounts.ts`'s `customer_in` condition) — no invented APIs.
- **BUILD: UNVERIFIED (no deps installed).** Confirmed no `node_modules` anywhere in the repo (root or any
  workspace). Per B02 rules, no TS agent besides gitjira-app runs `npm ci`; did not install. Both new files
  typecheck by inspection against the actual type signatures read from source, but `tsc`/`vitest` were not
  run. Flagged in `training/README.md` and both sealed answers.
- `git worktree list` and `git branch --list "training/*"` confirmed both branches exist and worktrees were
  cleanly removed; `git status --short` on the main tree is clean after the `training/` commit.

## Issues found in the project

(Full ranked list in `training/_answers/review.md`; sealed, not reused as answers here beyond a summary.)

- **Caching library built but never wired into any app** (`packages/cache/src/`) — the top finding; this is
  also *why* the incident PRs had to add the wiring rather than editing an existing bug.
- `CatalogPublisher.productPublished`'s invalidation contract only covers collections a caller explicitly
  passes as the product's *current* membership — a product removed from a smart collection has no
  invalidation path for the collection it left.
- `StaleWhileRevalidateCache`'s background refresh swallows all errors silently (no log/metric) —
  persistent origin failures would serve stale data indefinitely with zero operator signal.
- No secrets found (`grep` for common secret/key/password literal patterns and `.env*` files — none in the
  repo). No other things-presented-as-working-that-aren't beyond the caching-wiring gap above; this is a
  well-hardened repo (15 sprints of deliberate flaw-plant-and-harvest, all 5 ledgered flaws harvested).
- Minor: `apps/admin/src/catalog-admin.ts` hardcodes `currency: "USD"` in its price formatter despite the
  storefront supporting GBP/EUR (sprint 14) — a real display bug if multi-currency reaches admin, not
  caching-related, noted in the review answer key (#11) for completeness.

## Skill links (for COMPETENCY_GRAPH.md — not written there, per B02 rules)

- caching / invalidation-contract identity → `training/incidents/001-storefront-cache-tag-mismatch.md`,
  `training/_answers/incidents/001-storefront-cache-tag-mismatch.md`,
  `training/interview/TECHNICAL_QUESTIONS.md` Q1, Q4, Q8
- caching / per-user data under a shared key → `training/incidents/002-personalized-price-shared-cache-key.md`,
  `training/_answers/incidents/002-personalized-price-shared-cache-key.md`,
  `training/interview/TECHNICAL_QUESTIONS.md` Q6, Q7, Q10
- caching / stampede protection, single-flight, SWR (already taught by this repo's own ledger; referenced
  not retaught) → `packages/cache/src/index.ts`, `training/interview/TECHNICAL_QUESTIONS.md` Q2, Q3
- code review / "tested-in-isolation but never wired" smell → `training/review/EXERCISE.md`,
  `training/_answers/review.md` finding #1
- observability / silent background-failure → `training/_answers/review.md` finding #4

## Curriculum needs (candidates for `apprenticeship\curriculum\`, not written)

- **"caching" curriculum page** (the one requested by the brief) — title: **`caching-correctness.md`** or
  `NN-caching/README.md`. Scope (2 lines): *the four ways a cache goes wrong in production — stale-forever
  from a missing/mismatched invalidation key, stampede on a hot key, wrong-key sharing across audiences
  (per-user data under a shared key), and silent background-refresh failure — with worked diagnosis steps
  for each.* Exact worked examples to cite from this batch:
  - stale-forever via key/tag mismatch → this repo's incident 001 (`bazaar/training/incidents/001-...`)
  - per-user data under a shared key → this repo's incident 002 (`bazaar/training/incidents/002-...`)
  - stampede / single-flight / SWR (already-working reference implementation) →
    `bazaar/packages/cache/src/index.ts` (`SingleFlight`, `ProtectedReadThroughCache`,
    `StaleWhileRevalidateCache`) + this repo's own ledger flaw #3 (S06, `docs/sprints/flaw-ledger.md`)
  - silent background-refresh failure → `bazaar/packages/cache/src/index.ts`'s
    `StaleWhileRevalidateCache.read`, flagged in `training/_answers/review.md` finding #4 (illustrative,
    no incident planted for it this batch — candidate for a future caching incident in another project)
- No other new concept pages needed from this batch; everything else (webhook idempotency, reservation
  compensation, inventory races) is either already covered elsewhere in the archive or noted as an existing
  strength, not a gap.

## Existing learning-doc trees — verdicts

- `docs/sprints/` (`flaw-ledger.md`, `00-workflow.md`, `sprint-01.md`…`sprint-15.md`) — **KEEP**, flagged
  as a spoiler for this batch's exercises (it's the answer key for a different, already-solved flaw set;
  the learner may have seen it). Genuinely good material as a second worked example once this batch is done.
- `docs/audits/sprint-12-audit.md` — **KEEP**, same spoiler flag.
- `docs/adr/`, `docs/postmortems/`, `docs/runbooks/`, `docs/security/` — **KEEP**, out of scope for this
  DRILL pass; not evaluated in depth.
- `observability/{dashboards,slo}`, `performance/`, `scripts/k6/` — **IGNORE for this batch** (out of scope
  for a caching-focused DRILL pass); flagged in `training/README.md` as candidate material for a future
  observability/perf-focused pass on this project.

## Honest caveats

- BUILD/typecheck/test run were not actually executed (no `node_modules`, per B02 rule for non-gitjira-app
  TS repos) — both incidents are verified by careful manual type/identifier tracing only, explicitly marked
  `BUILD: UNVERIFIED (no deps installed)` in the README and both sealed answers.
- The review (`training/_answers/review.md`) covers the files most relevant to caching plus a handful of
  other high-signal files (inventory, checkout, payments, discounts, degradation) rather than an exhaustive
  repo-wide pass — this is a DRILL tier, and the repo is already unusually well-hardened (15 sprints,
  5/5 ledgered flaws harvested), so the true finding count at staff-review depth is genuinely smaller than
  a typical fresh course repo; 14 ranked findings reflects that, not a truncated effort.
- Did not touch `apps/worker` in depth (no caching code found there via grep) — if it turns out to have
  cache-adjacent logic on a later pass, it wasn't covered here.
