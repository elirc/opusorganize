# aicallhelper — B04 DRILL report

Project: `C:\Users\Owner\Desktop\aicallhelper` (AI Call Assistant v3, Tauri 2/Rust core +
React/TS/Vite, Deepgram streaming STT + Claude Haiku 4.5 streaming answers). Tier: **DRILL**
(2 incidents). Batch focus: AI latency & streaming failure modes.

No prior-audit record for this project was found under
`portfolio-audit\projects\batch-*.md` (searched all 14 batch files, case-insensitive, no
hit) — triaged fresh from the repo itself.

## What was created

All under `<repo>\training\`, committed on `main` at `5010b59` ("training: add B04
apprenticeship materials") via the pathspec commit (`git add -- training`), on top of the
clean, unmodified `f1cf524`:

- `training/README.md` — index, suggested order (~2.5-3.5h), gate list, incidents-at-a-glance
  table.
- `training/review/EXERCISE.md` + `COMPARE.md` — blind 60-min review, split into two
  choosable areas (answer pipeline vs. frontend session shell).
- `training/_answers/review.md` — sealed reference. Re-verifies the repo's own existing
  `docs/REVIEW.md` (dated 2026-08-20, commit `d18cd33`) against current HEAD `f1cf524`
  instead of assuming it still holds — found 5 of 9 MEDIUM findings already fixed by the two
  feature commits since, and 1 HIGH finding not re-verified.
- `training/incidents/001-ask-supersede-cancel-dropped.md` + sealed answer.
- `training/incidents/002-retry-cancel-race.md` + sealed answer.
- `training/interview/PROJECT_STORIES.md` (5 STAR prompts) + `TECHNICAL_QUESTIONS.md` (10
  questions, the last 5 a dedicated "latency budgets for AI features" set using this repo's
  real constants) + sealed `_answers/interview-technical-questions.md`.
- No `ladder/`, `navigation/`, or `agentic/` — out of scope for DRILL per the brief; noted
  explicitly in `training/README.md` so it doesn't read as an omission.

## Incident branches

Both based on `f1cf524`, built in isolated worktrees under the session scratch dir (never
switched the main tree's branch), each a single-purpose diff with a plausible
"refactor/cleanup" commit message and no hint of cause in the branch itself:

- **`training/incidents/001-ask-supersede-cancel-dropped`** (commit `2b1d015`) — 1 line
  removed from `src/state/useSession.ts`'s `submitAsk()`: the `bridge.cancelSession(...)`
  call that fires when asking a follow-up while a previous answer is still streaming.
  Symptom as reported: Anthropic usage shows output tokens billed for questions the user
  never saw finish; the UI itself looks completely normal (the frontend's stale-id drop
  logic hides the orphaned stream regardless of whether the backend actually cancelled it).
- **`training/incidents/002-retry-cancel-race`** (commit `dddd160`) — 3 lines removed from
  `src-tauri/core/src/llm/retry.rs`'s `with_retry_once()`: one of three cancellation checks
  (the one between the first attempt's failure and the retry decision). Symptom as reported:
  Stop doesn't always stop the Anthropic request; narrows to a deterministic unit-test
  failure once isolated.

## Verification

- **INC-001**: ran `npx vitest run src/state/useSession.test.ts` on both the clean baseline
  (`main` @ `f1cf524`) and the incident worktree. Baseline: **53/53 passed**. Incident:
  **51 passed, 2 failed** — both failures are `expect(fake.bridge.cancelSession)
  .toHaveBeenCalledWith(1)` returning "Number of calls: 0", exactly the predicted
  regression, in `useSession.test.ts:458` and `:900`.
- **INC-002**: `cargo check -p app-core` on the incident worktree — **compiles clean** (this
  is a pure logic bug, not a type error; confirms the `BUILD` bar without being a full
  workspace build). Additionally ran the affected test module directly:
  `cargo test -p app-core --lib llm::retry::` — **7 passed, 1 failed**
  (`cancellation_during_the_first_attempt_yields_aborted_not_the_http_error`, assertion
  `left: [0, 1] right: [0]`), confirming a second live attempt fires after cancellation, as
  predicted before running it. Both cargo commands compiled from a warm `target/` dir already
  present in the repo; the `check` took ~5 min and the `test` build ~8.5 min on this machine
  (cold test-profile compile of the full dependency tree — reqwest/tokio-tungstenite/etc.),
  scoped to the one crate (`-p app-core`) per the B04 Rust rule, no full workspace build.
- Worktrees were built with a Windows directory-junction pointing `node_modules` at the main
  tree's install (no `npm ci` re-run needed); one junction attempt silently fell back to a
  real recursive copy instead (an `ln -s`-in-git-bash quirk on this machine) — flagged here
  as a Windows/git-bash gotcha, not a repo issue. Both worktrees were removed cleanly after
  verification (`git worktree remove`), main tree confirmed clean (`git status --short`
  empty) and on `main` at `5010b59` before finishing.
- Not run: `cargo test` for the full `app-core` suite (242 tests per `docs/REVIEW.md`) or the
  Tauri shell crate — out of scope per the "single affected crate, no full workspace builds"
  rule. Not run: any real Deepgram/Anthropic network call (no paid API calls were made
  anywhere in this pass; all verification was local unit/type-level).

## Issues found in the project

- **This is an unusually mature codebase.** `docs/REVIEW.md` (in-repo, dated) already
  concludes "genuinely good code" after a 6-reviewer pass; my own spot checks agree — no
  typical old-AI-generated smells found (no fake integrations, no assertion-free tests, no
  hardcoded secrets/fallbacks; DPAPI secret handling, XSS defense, and CSP were all
  substantively verified by the existing review, not just asserted).
- **One HIGH finding carried forward, not independently re-verified this pass**: the
  screen-share content-protection call (`src-tauri/src/lib.rs`, `set_content_protected`) may
  fail open silently on pre-2004 Windows 10 with no OS-level readback — per `docs/REVIEW.md`,
  requires reading vendored `tao`/`tauri-runtime-wry` source to confirm; flagged in
  `training/_answers/review.md` as still open and worth re-checking.
- **Several MEDIUM findings from the dated review are already fixed** at HEAD (Groq
  mid-stream error swallowing, the ask-event-before-adoption race, driver-panic session
  stranding, dead `open_external` IPC surface, missing React error boundary) — confirmed via
  direct code re-checks (grep + read), not assumed. Two are still open (empty-answer via
  `saw_event` proxy in both LLM providers; STT drain-timeout silent tail truncation in
  `deepgram.rs:414`) plus a frontend-only one (`finalizing` UI state has no timeout escape).
  Full detail in `training/_answers/review.md`.
- **No secrets found in tracked files.** `src-tauri/core/src/store/secrets.rs` uses DPAPI
  with an explicit fail-closed `plain:` fallback (per the existing review, independently
  spot-read and consistent). No `.env` or credential files were found in the repo tree.
- **Nothing presented as working that isn't**, beyond the two planted incidents (which exist
  only on their own branches, not on `main`).

## Skill links (for the competency graph — not written there per the B04 rule)

- **AI/LLM integration — latency** → `training/interview/TECHNICAL_QUESTIONS.md` Q6-10 +
  `_answers/interview-technical-questions.md` (STT/LLM budget breakdown using real
  `limits::` constants, prewarm, coalescing-window trade-off, 429/529 retry trade-off,
  cloud-vs-local budget disclosure).
- **AI/LLM integration — streaming failure modes** → `training/incidents/001-*` (frontend
  cancel-on-supersede) and `training/incidents/002-*` (Rust retry/cancel race), both with
  sealed root-cause + fix + "what regression test should exist" answers.
- **AI/LLM integration — cost/billing correctness** → same two incidents (billing continues
  after a cancelled/superseded session in both layers).
- **Code review / verify-before-trust** → `training/review/` — this is the strongest
  instance of this skill in the batch so far: the exercise's own answer key demonstrates
  re-verifying a dated AI-adjacent review document against current code and finding it
  partly stale, which is the exact "trust but verify" lesson curriculum page
  `05-verify-before-trust.md` already anchors.
- **Testing (unit, Rust + TS)** → both incidents are detected by existing, specific unit
  tests (`useSession.test.ts:458,900`; `retry.rs`'s
  `cancellation_during_the_first_attempt_yields_aborted_not_the_http_error`) — good material
  for "why did CI not catch this" framing.
- **Agentic engineering** → `training/interview/PROJECT_STORIES.md` story 3 (both incidents
  are exactly the shape of bug a coding agent introduces — plausible commit message, small
  diff, compiles clean).

## Curriculum needs (titles + scope only, not written)

- **"Cancellation propagation across an IPC/process boundary"** — 2-line scope: when a
  frontend cancel action must reach a backend `CancellationToken`/retry policy, and the two
  distinct failure modes (frontend never sends the cancel; backend receives it but a
  downstream retry/select race ignores it anyway). Both aicallhelper incidents are direct
  material; likely also fits pulse/gitjira-app's realtime work from earlier batches.
- **"Latency budgets for streaming AI features"** — 2-line scope: decomposing a product
  latency promise into per-stage budgets with concrete timeouts-as-ceilings vs.
  typical-case numbers, and the specific trade-off between token-forwarding batching and
  first-token-latency. No existing curriculum page covers this; COMPETENCY_GRAPH currently
  has no "AI/LLM integration" skill row at all as of B02 — this project is the first to
  populate it.

## Existing learning-doc trees — KEEP / MERGE / CONVERT / IGNORE

- **`docs/REVIEW.md`** — **KEEP**, with a caveat now on record: it's dated (commit `d18cd33`,
  two feature commits behind HEAD) and several of its MEDIUM findings are already fixed.
  `training/_answers/review.md` links to it and re-verifies rather than duplicating it.
  Don't merge into central curriculum — it's project-specific evidence, not a general
  concept.
- **`docs/adr/` (17 ADRs + README with an "interview prep" reading guide already built in)**
  — **KEEP**, explicitly gated (not opened by me before/during incident design beyond what
  the README table-of-contents already reveals; the numbered list and one-line descriptions
  were read to select which ADRs to point trainees at post-exercise, but the ADR bodies for
  006/011/015 — the ones closest to the two incidents — were not read). This is unusually
  good material: each ADR already ends with an "interview translation." Nothing to convert;
  it already reads like curriculum. Recommend the *repo owner* eventually mine 2-3 of these
  ADRs (006 retry-once-delta-guard; 015 session-outcomes-and-adoption) into
  `apprenticeship\curriculum\` as cross-project concept pages, since the retry/cancellation
  and event-adoption patterns generalize well beyond this one app — flagged as a curriculum
  need above rather than done here (rule 5/B04: don't write shared files from inside a
  project).
- **`docs/learn/` (10 files)** — **KEEP**, gated, not opened this pass beyond confirming it
  exists and covers the same invariants (per its listing in `docs/README.md`'s doc index,
  which I did read). Likely largely redundant with the ADRs for training purposes; not
  independently assessed for MERGE vs IGNORE — flag for a future pass if this project gets
  revisited at a higher tier.
- **`docs/SPEC.md` (1257 lines), `docs/TROUBLESHOOTING.md`, `docs/IDEAS.md`,
  `docs/DEVELOPMENT.md`, `docs/SECURITY.md`, `docs/RELEASE_CHECKLIST.md`,
  `docs/FREE_VOICE_MODE.md`, `docs/FREE_VOICE_TEST_RESULTS.md`, `docs/LOCAL_MODELS_REPORT.md`**
  — **IGNORE for this pass** (not read beyond section headers/grep hits used to verify
  specific claims). Not spoilers in the same way as REVIEW.md/adr/learn, so not gated in
  `training/README.md`, but also not incorporated — out of scope for a DRILL-tier budget.
- **`docs/fabledocs/`, `local-voice/`** — present in the repo root; **not inspected at all**
  this pass. Flag for whoever next touches this project.

## Honest caveats

- The HIGH finding (screen-share content-protection fail-open) in `training/_answers/review.md`
  is carried from the existing `docs/REVIEW.md` without independent re-verification against
  HEAD — it would require reading vendored `tao`/`tauri-runtime-wry` dependency source, which
  I judged out of scope for a DRILL-tier budget. Said so explicitly in the answer file rather
  than presenting it as confirmed.
- Several LOW findings in `training/_answers/review.md` are likewise carried forward from
  the dated review without re-verification (labeled as such in the file) — the review
  exercise's real teaching point (re-verify MEDIUM+ claims) was prioritized over exhaustively
  re-checking every LOW item under the time budget.
- `docs/learn/` (10 files) and most of `docs/SPEC.md`/`docs/TROUBLESHOOTING.md` were not read
  — gated as spoilers but not inspected for content quality, so my KEEP verdict on
  `docs/learn/` is based on its listing/purpose, not a read-through.
- No `.env` files were found and no secrets were reported to have specific values anywhere
  in this report, per the B04 rule.
- `docker` was not used (irrelevant to this project — no containers here) and no real Deepgram
  or Anthropic API calls were made anywhere in this pass.
