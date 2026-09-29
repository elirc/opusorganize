# netstripe — SubscriptionBillingDashboard — B01 batch report

**Tier:** DRILL (Phase 3 review + incidents, plus a small Phase 5 interview kit per
B01_AGENT_BRIEF.md's tier table: "DRILL = Phase 3 (+ a small Phase 5 interview kit:
PROJECT_STORIES + 10 TECHNICAL_QUESTIONS)").

Path: `C:\Users\Owner\Desktop\.netstripe` — .NET 8 minimal-API backend
(`src/Billing.Api`, ~1,480 lines, no MVC controllers, unusual among the Net-fleet) +
React 19/Vite 6 frontend (`src/Billing.Web`, not in the `.sln`). Billing domain:
customers, plans, subscriptions, coupons, invoices, usage events, webhooks. Money stored
as integer minor units. Zero test files anywhere (confirmed via `find -iname "*test*"`).

## What was created

All under `<repo>\training\`, committed to `main` at `b0e5001` (pathspec commit,
`training/` only — nothing else in the working tree was touched or staged):

- `training/README.md` — index, suggested order (~4-5 hrs), layout map, incident branch
  notes, a warning that both incident branches bundle unrelated pre-existing build fixes.
- `training/review/EXERCISE.md` — 60-minute blind code review over the whole backend,
  explicitly told to try `dotnet build` first rather than trust the curriculum volume.
- `training/review/characterization-tests-billingengine.md` — the requested
  characterization-test exercise: scaffold a real `Billing.Api.Tests` xUnit project
  (none exists) and write 8 specific pinning tests for `BillingEngine`, including one
  aimed straight at the duplicate-invoice race and one at the double-`ApplyPaymentResult`
  shape.
- `training/incidents/001-idempotency-caches-failures.md` — symptom-only brief (support
  tickets + a log excerpt showing the dashboard and the pay-endpoint response
  contradicting each other), no cause stated.
- `training/incidents/002-mrr-rounding-drift.md` — symptom-only brief (finance's weekly
  reconciliation report + a reproduction recipe via the live API, since the seeded data
  alone doesn't trigger it), no cause stated.
- `training/interview/PROJECT_STORIES.md` — 5 STAR prompts (debugging, trade-off,
  incident, agent-caught-bug re: the build failure, money-domain-knowledge).
- `training/interview/TECHNICAL_QUESTIONS.md` — 10 questions citing real files/lines
  (API design ×2, data modeling ×2, concurrency ×1, testing ×1, security ×2,
  operations ×1, domain modeling ×1).
- `training/_answers/review.md` — 19 ranked findings (severity: correctness, security,
  concurrency, data integrity, operability, maintainability, tests), each with file:line
  evidence and a production-impact sentence; closes with an explicit
  "old-AI-generated smells present" and severity-ranking-rationale summary.
- `training/_answers/COMPARE.md` — your-findings-vs-sealed template with a
  pattern-behind-the-misses section.
- `training/_answers/001-idempotency-caches-failures.md` and
  `.../002-mrr-rounding-drift.md` — root cause, exact diff, diagnostic path, regression
  test, fix, and a model postmortem each, per Phase 3's spec.

### Incident branches

- `training/incidents/001-idempotency-caches-failures` @ `8b0c838` — a "fix duplicate
  side effects on retry" PR to `IdempotencyMiddleware.InvokeAsync` that removes the
  `context.Response.StatusCode is >= 200 and < 300` guard before caching a response,
  so *every* response (including failures) gets pinned to the client's `Idempotency-Key`
  for up to 24h. Symptom given: support tickets where a customer's invoice genuinely
  returns to `Open` (confirmed on the dashboard, confirmed via a real webhook decline in
  the log) but `POST /api/invoices/{id}/pay` keeps returning a stale, replayed
  `400 "Invoice is already paid."` for the rest of the day.
- `training/incidents/002-mrr-rounding-drift` @ `bfce8de` — a "drop the redundant
  `decimal.Round` call, the `(long)` cast already truncates" perf-motivated PR to
  `Money.Multiply`. Truncation and `MidpointRounding.AwayFromZero` agree whenever the
  fractional remainder is `< 0.5` (which is most round-number test inputs a developer
  would try by hand) and disagree by exactly 1 minor unit — always downward — whenever it
  isn't. Symptom given: finance's weekly MRR reconciliation is consistently a few cents
  under their own number, tracking the count of annual-cycle customers, never monthly.
  Also affects `Coupon.CalculateDiscount`'s percent-off math (same `Multiply` method) —
  flagged in the sealed answer as a wider blast radius than the ticket that reported it.

Both branches are based on `main` @ `a84f11b` (HEAD before the `training/` commit) and
were never merged; the main working tree's branch was never switched. Both commits also
carry two one-line, unrelated fixes for the pre-existing build failure described below —
called out explicitly in each commit message and in `training/README.md` so they aren't
mistaken for part of either puzzle.

## Verification

- **`dotnet --version`** on this machine: `10.0.302`. No `global.json` anywhere in this
  repo, so SDK resolution is unconstrained — the orchestrator's global.json workaround
  wasn't needed.
- **The repo as committed on `main` does not build.** `dotnet build src/Billing.Api` on a
  clean checkout of `a84f11b` fails with two independent errors:
  `CS0246` (missing `using Billing.Api.Domain;` in
  `Infrastructure/IdempotencyMiddleware.cs`, needed for `IBillingClock`) and `CS0173`
  (`Program.cs:143`'s coupon-creation ternary — `Money` is a non-nullable
  `readonly record struct`, so `null : Money.FromMajor(...)` can't be typed without an
  explicit `(Money?)null`). This is a genuine, previously-unreported finding — the prior
  audit noted the missing tests but didn't run a build. It's now finding 0 (BLOCKER) in
  `training/_answers/review.md`.
- **Both incident branches build clean** after also applying the two fixes above (bundled
  into each incident's commit, since an unbuildable baseline made it impossible to verify
  the planted bug in isolation otherwise): `dotnet build src/Billing.Api` inside each
  worktree → `Build succeeded. 0 Warning(s). 0 Error(s).` for both. Worktrees were removed
  after committing; branches themselves remain.
- **The planted bugs were reasoned through by hand, not executed against a running app**
  (no test project exists yet to run them through — that's the point of the
  characterization-tests exercise). The idempotency incident's cache/replay logic and the
  Money.Multiply truncation math were traced against the actual source, not assumed.
- **UNVERIFIED**: the frontend (`src/Billing.Web`) was not built or run; no dev server was
  started anywhere, consistent with the brief's "don't start long-running servers" rule.
  The `docs/upskill/` and `docs2/` curriculum trees (46 + 47 files) were not re-audited
  file-by-file this batch — see the KEEP verdict below, resting on the prior audit's
  sampling, not an independent full read.

## Issues found in the project (beyond what was planted)

Full detail + file:line evidence in `training/_answers/review.md`; highlights:

- **The repo doesn't compile as committed** (finding 0, above) — the most severe finding
  in this pass, and not something the prior audit or either curriculum tree caught.
- **Real concurrency race, not the planted incident**: `BillingEngine.RunBillingCycle`
  checks `subscription.CurrentPeriodEnd <= billingDate` then calls `GenerateInvoice`,
  which performs several separate, individually-locked `BillingStore` writes rather than
  one atomic read-decide-write — two overlapping calls to
  `POST /api/simulator/run-cycle` can generate two invoices for the same subscription and
  period (finding 1, BLOCKER).
- **Real idempotency gap, not the planted incident**: `POST /api/webhooks/payment-provider`
  carries `payload.EventId` but never checks it against anything already processed — a
  retried webhook delivery (which real payment providers do) double-processes a payment
  and double-fires the outbound webhook (finding 2, HIGH).
- **`PaymentWorker` hardcodes `succeeded: true` for every payment job**
  (`PaymentWorker.cs:42`), independent of whatever the real provider later reports via the
  webhook — the two paths can flip an invoice's status back and forth within seconds
  (finding 3, HIGH).
- **Webhook "delivery" never delivers anything**: `WebhookDeliveryWorker.Deliver` always
  marks events `Succeeded` and writes a literal `"Simulated delivery..."` message, and
  every webhook targets a hardcoded `"https://example.com/webhooks/billing"` — a fake
  integration presented as working in the dashboard UI (finding 4, HIGH).
- **No authentication or authorization anywhere** — `GET /api/dashboard` returns every
  customer's PII and every financial record to any caller (finding 5, HIGH).
- **Hardcoded webhook-signing secret default** (`"dev_secret_replace_me"`) with no
  startup guard against it still being in effect (finding 9, MEDIUM).
- **No secrets found** beyond that intentionally-placeholder default — no real API keys,
  connection strings, or credentials anywhere in the codebase.

## Skill links (for the competency graph — not written there, per the brief)

- `idempotency` / `money` → `training/incidents/001-idempotency-caches-failures.md` +
  its sealed answer + `interview/TECHNICAL_QUESTIONS.md` Q1, Q2
- `idempotency` (webhook event dedup, distinct from the above) →
  `_answers/review.md` finding 2 + `TECHNICAL_QUESTIONS.md` Q2
- `db-modeling` / `concurrency` (check-then-act race) → `_answers/review.md` finding 1
  + `characterization-tests-billingengine.md` item 6 + `TECHNICAL_QUESTIONS.md` Q3, Q5
- `money-correctness` / `rounding` → `training/incidents/002-mrr-rounding-drift.md` +
  its sealed answer + `PROJECT_STORIES.md` #3, #5
- `security-owasp` (no authn/authz; hardcoded secret default) → `_answers/review.md`
  findings 5, 9 + `TECHNICAL_QUESTIONS.md` Q7, Q8
- `test-unit` / `characterization-testing` (zero-test codebase) →
  `training/review/characterization-tests-billingengine.md` + `TECHNICAL_QUESTIONS.md` Q6
- `code-review` → `training/review/EXERCISE.md` + `_answers/review.md` +
  `_answers/COMPARE.md`
- `reliability` (fake integration; non-durable in-memory queues) → `_answers/review.md`
  findings 4, 6 + `TECHNICAL_QUESTIONS.md` Q9
- `build-hygiene` / `verify-before-trust` → `_answers/review.md` finding 0 +
  `PROJECT_STORIES.md` #4

## Curriculum needs (concepts referenced that deserve ONE central page)

Not written to `apprenticeship\curriculum\` per the brief — reporting only:

- **"Verify the build before trusting anything else about a codebase"** (2-line scope:
  a concrete worked example — this project's curriculum is 90+ files deep and the code
  underneath never compiled; likely recurs across the Net-fleet given how the curriculum
  pipeline was generated without ever running the code).
- **"Truncation vs. rounding in money math, and why round-number test inputs hide it"**
  (2-line scope: `(long)` casts on `decimal` truncate toward zero; a test suite that only
  tries whole-dollar/evenly-divisible inputs will never catch this class of bug — this
  project's incident 002 is a concrete worked example, and the same pattern is plausible
  anywhere else in the archive doing `Money`-style minor-unit arithmetic).
- **"Two workers writing the same entity from two different trust sources"** (2-line
  scope: `PaymentWorker`'s simulated-success path and the real payment-provider webhook
  both call the same state-mutating method independently — a pattern worth a named
  central page since it'll recur in any project with both a background simulator and a
  real external callback, e.g. other Net-fleet apps with payment/webhook flows).

## Existing learning-doc trees in this repo — KEEP/MERGE/CONVERT/IGNORE

- `docs/upskill/` (46 files, standard 8-section structure) — **KEEP**, with a caveat not
  present in the prior audit's disposition: this curriculum was generated against a
  codebase that does not compile (finding 0). Spot-checked
  `docs/upskill/05-quality-engineering/01-testing-strategy.md` exists and matches the
  prior audit's description; did not re-verify every claim inside it against running
  code (can't — nothing runs yet). Link it from the competency graph as reading material,
  but flag in the graph entry that its accuracy about runtime behavior is unverified
  pending someone actually getting the app to build and run.
- `docs2/` (47 files, same 8-section structure, independently numbered "01.01" style
  headers) — **KEEP**, same caveat as above. The prior audit's sample specifically praised
  `docs2/01-codebase-cartography/01-system-map.md` for correctly noting the `.sln`/
  `Billing.Web` gap (confirmed still true this batch — see `_answers/review.md`
  finding 18). Two near-parallel curriculum generations over the same code is redundant
  content, not redundant *value* — `docs2` reads as the more detailed/precise of the two
  from the sample checked; no MERGE action taken (per the brief, don't move files without
  explicit approval), just noting a diff-and-consolidate pass would be reasonable if this
  project is ever promoted to LAB tier.

## Honest caveats

- This is a DRILL-tier pass: no `ladder/`, `navigation/`, or `agentic/` directories were
  created, per the brief's tier table. If this project is later promoted to LAB tier,
  those phases still need doing — and the LAB-tier `training/ladder/` work in particular
  would need to grapple with the fact that several "junior rung" tickets (a real
  endpoint, a unit test) are blocked on first fixing finding 0's build failure.
- Neither incident's planted bug was verified by actually running the app end-to-end
  against a live HTTP request — verification was `dotnet build` only (consistent with the
  brief's "don't start long-running servers" rule) plus hand-traced logic through the
  actual source. The characterization-tests exercise (`training/review/
  characterization-tests-billingengine.md`) is explicitly designed to be the vehicle for
  someone to build the missing test project and run these paths for real; I did not
  scaffold and run that test project myself in this pass (unlike the netramp batch
  report's precedent, where a throwaway verification project was built) — the
  `BillingEngine`/`BillingStore` seed-data dependency graph is larger here, and DRILL
  tier doesn't call for that additional build-and-run step. Noted as UNVERIFIED, not
  silently skipped.
- `docs/upskill/` and `docs2/`'s full 93 files combined were not re-audited file-by-file
  this batch; the KEEP verdicts rest on the prior audit's sampling plus a 2-file spot
  check, not an independent full read — and now carry a new caveat (build failure) the
  prior audit didn't have.
- I did not run the frontend or start the backend server at all.
