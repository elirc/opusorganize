# lucasrouter: RouteIQ delivery-route optimizer (B03 report)

**Tier:** LAB (Phases 2, 3, 4 and 5), 5 incidents. **Batch focus:** the frontend lab (React render cost, zustand selector granularity,
the Next module graph and bundles, Core Web Vitals with calibrated numbers, and accessibility). **Repo:** `C:\Users\Owner\Desktop\lucasrouter`
(own `.git`, remote `elirc/lucasrouter`, **not pushed**). HEAD at start was `fafe0c7`.

## What was created
All of it is under `training/`, in one pathspec commit **`b3ee4c8`** "training: add B03 apprenticeship materials" on `main`.
- `training/README.md`: the index, the suggested order (~45–55 h), and the real bugs on `main`.
- `training/tools/frontend-probe.mjs`: a reusable puppeteer probe. It records LCP/CLS/FCP/JS bytes per route, the marker-click p75
  (an INP proxy via Event Timing), the typing long-task count and time, whether the toast's live region existed before its text
  (plus how long the toast stayed visible), and whether the driver sheet closes on Escape, returns focus, and is `:modal`. It passes the
  repo's `eslint --max-warnings=0`.
- `ladder/`: J1 overview counts (a correctness bug on `main`), **J2 component-test foundation** (Vitest projects + Testing Library;
  the first frontend testing layer), J3 `/api/optimize` body limits, **M1 marker-click INP**, **M2 the vanishing toast**
  (a real bug), **M3 axe + keyboard + screen-reader audit** (the required a11y audit ticket), **M4 per-route JS budgets + calibrated
  CWV**, S1 scaling to 1,500 stops, and S2 frontend quality gates + RUM + runbook.
- `review/EXERCISE.md` + `COMPARE.md`, with the sealed `_answers/review.md` (24 findings, several verified by running the app).
- `incidents/001..005-*.md` (briefs), with sealed answers in `_answers/incident-00N.md`.
- `navigation/`: ARCHITECTURE (with evidence and 3 traced flows), FIRST_CHANGE, TRADEOFFS (4 "Why?" drills), CHANGE_REQUEST (late stops).
- `agentic/WORKFLOW.md`: M1 run through spec → implementer → adversarial reviewer → verification, with the AI-output checklist.
- `interview/`: PROJECT_STORIES (5), TECHNICAL_QUESTIONS (20), SYSTEM_DESIGN, MOCK_DEFENSE (scored rubric), FLASHCARDS (24).
- `_answers/`: 17 sealed files (ladder ×9, incidents ×5, review, change request, interview).

## Incident branches (symptom only)
| Branch | Commit | Symptom (as on-call sees it) |
|---|---|---|
| `training/incidents/001-landing-bundle` | `4c9f7e1` | Is the landing page still static? Hydration-critical JS on `/` 591→619 KB raw (184→194 KB gzip), while total JS moved only +6 KB |
| `training/incidents/002-toast-announcements` | `ceb3572` | A screen-reader user no longer hears move/optimize confirmations. axe, Lighthouse and the smoke run are all green |
| `training/incidents/003-driver-sheet-keyboard` | `20f0177` | Escape doesn't close the driver sheets, switch access scans the page behind, and TalkBack reads background content |
| `training/incidents/004-search-highlight` | `5ef3a5b` | Stop search stutters on older PCs after the "dim non-matching stops" feature |
| `training/incidents/005-optimizer-status-strip` | `860f5f3` | The dispatcher map jumps down after load and a misclick hits the Legend chip. CLS 0→0.04 |
Four of the five are frontend perf or a11y regressions (001 bundle, 002 live region, 003 modality and keyboard, 004 re-render storm).
005 is a CLS regression.

## Verification: what was actually run
- `pnpm install --frozen-lockfile` (main tree, once). **`vitest run --no-file-parallelism`: 167/167 passed** on the working tree (it
  includes the user's uncommitted changes). `pnpm typecheck` clean.
- For each of the 5 incident branches: `next build` **exit 0** and `eslint . --max-warnings=0` **exit 0**, run in a scratch worktree.
  **All five pass every existing gate**, which is the point of S2.
- Each incident's symptom was **reproduced with the probe on production builds** (same laptop, same session):
  - 001: critical JS on `/` 591 KB / 184 KB gzip (9 scripts) → 619 / 194 (10 scripts, one of which contains the store + seed). Total fetched
    609 → 615 KB.
  - 002: `regionExistedBefore` true → **false**.
  - 003: `{closedByEscape, focusReturned, modal}` true/true/true → **false/false/false**.
  - 004: long tasks while typing (25 keys, 4× CPU, 3 runs) 0/1/1 (≤ 57 ms) → **20–21 tasks, 1.4–1.9 s**.
  - 005: `/dispatch` CLS **0 → 0.04** (390 px, 4× CPU).
- **Real bugs on `main`, measured:** (a) the "Routes ready" toast is visible for **161–180 ms** instead of 3.7 s. A reference fix applied in
  scratch gave **3,728 ms**, and it's in the M2 answer. (b) Marker-click p75 is **224–240 ms at 1×** and 1.06–1.46 s at 4×. A scratch
  experiment moving the selection subscription out of `DispatchScreen` did **not** change it within noise, and the M1 answer teaches
  exactly that. (c) axe-core 4.10.2: **color-contrast ×13/×14 on the landing page** (the docs claim a11y 100, measured before the
  rebuild), target-size ×13–19 on the markers, and a `region` ×2 on `/driver/D1`. (d) Keyboard: **116 Tab presses** to reach Export on
  `/dispatch`, including 46 marker stops and unnamed focusable polylines.
- Calibration is stated everywhere. Timings are same-session medians and deltas on this laptop (slower than Lighthouse's reference,
  per DECISIONS #44). Byte counts are the stable signal.
- All servers and worktrees were stopped and removed. Scratch logs remain in the session scratchpad.

**UNVERIFIED / caveats**
- The M2 *mechanism* (a stale queued `setShown(null)` from the idle exit timer winning over the render-phase update) is the best-supported
  explanation from instrumentation plus a minimal-fix experiment. The answer file says so explicitly and doesn't claim a React bug.
- The screen-reader behaviour for 002 was inferred from live-region semantics plus the DOM check. It wasn't tested with NVDA or VoiceOver.
- "Enter on a focused marker doesn't open the popup" was seen only in headless Chrome and is flagged in the answer to confirm by hand.
- No Lighthouse runs. No mobile hardware. J2/J3/M4 reference code is a sketch and wasn't executed.
- The incident commits are plain "realistic PR" commits without the co-author trailer. The training commit has it.

## Issues found in the project
- **Presented as working, but not:** the dispatcher's success toast after Optimize vanishes in about 170 ms (M2). The landing's
  "a11y 100" (DECISIONS #44) is stale after the rebuild, with 13–14 contrast failures. DECISIONS #54 describes `experimental.inlineCss`,
  but `next.config.ts` doesn't set it. The per-route "JS KB" in docs/REBUILD.md includes Next's idle `<Link>` prefetch of other routes
  (on `main` the landing page already downloads a 43 KB store + seed chunk at idle), so the table mixes a page's own cost with prefetch.
- Other: the `StopSearch` result count is a live region mounted along with its text. The Undo toast has a 3.5 s timeout with no pause.
  `/api/optimize` is public, unauthenticated and CPU-bound, and parses unbounded bodies. `repair.ts` has a wall-clock budget (load-dependent
  output). There are no component tests, no CI and no RUM.
- **Secrets:** `.env.local` (a Vercel OIDC token) is present, gitignored, and never committed (`git log --all -- .env.local` is empty).
  Location only.
- Uncommitted user work was left untouched (5 modified, 4 untracked, the delivery-validation change + astraupskill/dfableandopus).
  `git status` is identical before and after, apart from the new commit.

## Skill links (for COMPETENCY_GRAPH)
- **Web/TS/React (render cost, selectors, state placement):** ladder/M1, ladder/M2, incidents/004, interview Q1–6, TRADEOFFS #3
- **Performance, frontend (INP / CWV / bundles):** ladder/M1, ladder/M4, incidents/001, incidents/004, incidents/005, ladder/S1, tools/frontend-probe.mjs
- **Accessibility (first exercises in the portfolio):** ladder/M3 (the axe + keyboard + SR audit), incidents/002 (live region), incidents/003
  (modality and keyboard), review #4/#5/#11/#23/#24, interview Q11–14
- **Testing (component layer, e2e strategy):** ladder/J2, ladder/S2 (gate matrix), _answers/incident-002 (regression test)
- **Observability (RUM, alerting on vitals):** ladder/S2
- **Deployment / rollback:** ladder/S2 (Vercel promote-previous), SYSTEM_DESIGN
- **API design / input limits:** ladder/J3
- **Backward compatibility:** TRADEOFFS #4 (the `/api/optimize` contract), S1
- **Code review:** review/EXERCISE.md (24 findings)
- **Codebase navigation:** navigation/*
- **Agentic engineering:** agentic/WORKFLOW.md (on M1, which has the planted "the obvious memo fix doesn't move the number" lesson)
- **Design docs / trade-offs:** navigation/TRADEOFFS.md (4), S1, S2

## Curriculum needs (one central page each; not written)
1. **Live regions that actually announce.** A region must exist before its content changes. Conditional and keyed mounts, polite vs
   assertive, toast timing (2.2.1). Examples: lucasrouter 002, M2, StopSearch.
2. **Keyboard and focus management for modal UI.** `showModal` vs `show`, inert, focus in and return, Escape, the top layer vs z-index,
   popover. Examples: lucasrouter 003, `DriverDialog.tsx`.
3. **Measuring frontend performance honestly.** Lab vs field, calibration (`benchmarkIndex`), medians and deltas, INP proxies vs RUM,
   long tasks vs Event Timing, critical vs prefetched JS. Examples: lucasrouter probe, M1, M4, 001, 004.
4. **React render cost and state placement.** Subscription level, selector stability (zustand 5 / uSES), when `memo` helps and when it
   costs, Profiler-then-trace. Examples: M1, 004.
5. **App Router module graph and bundle budgets.** The `'use client'` boundary, layout-level imports, dynamic import side effects,
   `<Link>` prefetch. Example: 001.

## Existing learning-doc trees in this repo
| Tree | Verdict | Why |
|---|---|---|
| `astraupskill/` (untracked, 9 md + evidence) | **KEEP** | It covers the uncommitted delivery-proof runtime-validation change (store boundary, sanitizer). It's state/validation-focused and complementary, and the lab doesn't duplicate it. |
| `dfableandopus/` (untracked, 7 md) | **KEEP** (link its interview kit) | Interview material for that same validation change. `training/interview/` explicitly defers to it for that story. |
| `docs/REBUILD.md`, `docs/performance-*.json`, `DECISIONS.md` | **CONVERT TO EXERCISE** (done, in part) | Their claims feed review #14/#16/#23 and ladder M4. The prefetch-inflated JS numbers and stale a11y/inlineCss claims are now exercises. |
| `docs/ALGORITHM_INTEGRATION.md` | KEEP | The contract doc referenced by J3, TRADEOFFS #4 and S1. |

## Honest caveats
- It's a demo with no backend, so the senior tickets are design-only. Only frontend numbers are real.
- Perf numbers come from one Windows laptop under background load. Run-to-run spread at 4× is ±150–200 ms for clicks and hundreds of ms for FCP.
  The exercises teach comparing medians within one session. Don't reuse the absolute values.
- Incident 005's effect is modest (0.04 < the 0.1 "good" threshold). The brief says so and asks the learner to argue why it still matters.
- Effort: ~7 builds + ~15 probe runs. Each production build takes about 4 minutes on this machine.
