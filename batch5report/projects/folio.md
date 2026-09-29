# folio: B05 report (LAB tier, 5 incidents): CRDT and offline sync

**Repo:** `C:\Users\Owner\Desktop\gitvg\folio` (its own `.git`, remote github.com/elirc/folio, **not pushed**). Base: `main @ af51546`.
**Tier:** LAB (Phases 2, 3, 4, 5). The working tree was clean before and after (no user changes present). Deps were installed once with
`pnpm install --frozen-lockfile --store-dir <SCRATCH>/folio/pnpm-store` (private store). There were no recursive deletes. The worktrees were removed with `git worktree remove`.

## Commits
- `da45b9c` on `main`: "training: add B05 apprenticeship materials" (pathspec commit, `training/` only, 45 files)
- Incident branches (each one commit on top of `af51546`):

| Branch | Commit | Symptom (not the cause) |
|---|---|---|
| `training/incidents/001-lab-panes-diverge` | `a338859` | The crdt-101 lab panes show `bc` vs `cb` after reconnecting. CI green. |
| `training/incidents/002-second-tab-edits-vanish` | `7cfb4ff` | Text typed in a second tab of the same doc never reaches teammates or the server. |
| `training/incidents/003-big-docs-open-slowly` | `ece7793` | Heavily edited docs grow 2–3× and take seconds to open. Server CPU per keystroke up. |
| `training/incidents/004-reconnect-storm` | `24df431` | Every deploy becomes a multi-minute outage (ingress spike, repeated restarts). |
| `training/incidents/005-callouts-vanish` | `d406b42` | New "callout" blocks disappear seconds after creation in shared docs. |

## What I created (`C:\Users\Owner\Desktop\gitvg\folio\training\`)
- `README.md`: index, setup, suggested order (~50–60 h), real bugs on main, links to curriculum 05/07/08/11/12/14
- `ladder/`: J1 sync-status indicator (a11y live region), J2 merge characterization test, M1 offline edits never arrive + system-level property
  test, M2 restore no-op vs tombstone/GC growth, M3 sync protocol versioning, M4 conflict UX for non-mergeable fields, S1 multi-device
  sync + auth + presence at scale, S2 snapshot/compaction strategy, S3 schema migration with offline clients
- `review/EXERCISE.md`, `review/COMPARE.md` → `_answers/review.md` (23 findings, ✅ proven vs 🧠 reasoned, AI-smell tagged)
- `incidents/001…005-*.md` → `_answers/incident-00N.md` (root cause, measured repro, fix, regression test, postmortem)
- `navigation/ARCHITECTURE.md`, `FIRST_CHANGE.md`, `TRADEOFFS.md` (4 "Why?" drills), `CHANGE_REQUEST.md` (CR-31) → `_answers/navigation-change-request.md`
- `agentic/WORKFLOW.md` (M1: spec → implementer → adversarial reviewer → verification checklist → graded explanation)
- `interview/PROJECT_STORIES.md` (5), `TECHNICAL_QUESTIONS.md` (20) → `_answers/interview-technical.md`, `SYSTEM_DESIGN.md`, `MOCK_DEFENSE.md`, `FLASHCARDS.md` (24)
- 15 sealed answer files in `_answers/`

None of the 5 flaw-ledger flaws (`docs/sprints/flaw-ledger.md`) or its in-PR arcs was reused.

## Verification (what I actually ran)
- **Baseline tests, main:** crdt-101 10, collab 56, editor 74, shared 41, storage 6, api 8 = **195 green**. The api needed `pnpm --filter @folio/db generate`
  first (2 suites fail to import without it).
- **Incident branches (vitest, via a scratch config that resolves the worktree's source against main's node_modules, so nothing was installed in the worktrees):**
  - 001: crdt-101 10/10 green on the branch (the weakened assertion). With the original assertion, fast-check found a counterexample 3/3 runs. A deterministic 2-replica
    repro gives `["bc","cb"]` on the branch and `["cb","cb"]` on main.
  - 002: collab security tests 9/9 green. Provider+YRooms probe: with a stable clientID, tab 2's text is lost on the server and teammate (converges without it).
  - 003: collab 57/57 + api yroom/drain 5/5 green. Measured state/load/server-work ratios (gc on vs off): e.g. 576 KB → 1,512 KB, cold load ~0.3–0.46 s → 4.9–7.0 s.
  - 004: collab 57/57 + api 5/5 green (the PR's own test passes). Probe: per-reconnect upstream 0.04 KB → 274 KB and server CPU 4.5 → 43 ms per client.
  - 005: editor 76/76 green. Node probe: an old-schema client rendering a new-schema doc emits a delete update. The server ends with the callout removed.
- **Main-branch bugs proven by probes:** offline/handshake-gap edits lost (the Provider↔YRooms property test fails on the first case; the reference fix passes 200/200),
  early `sync1` dropped before join, split rooms on concurrent cold joins, restore returns 2 bytes, `verifyUpdateAuthorship` false for delete-only updates,
  y-prosemirror delete on unknown node, J2 merge outcomes (with fixed clientIDs), the M2 forward restore via `updateYFragment` (verified).
- **UNVERIFIED:** `tsc` typecheck of the 5 incident branches (vitest transpiles without type-checking; the changes are small and typed, but I didn't run it). No browser/e2e run
  (no Postgres started, no dev server); incident 005's browser path is inferred from y-prosemirror source plus the Node repro. Incident alert/dashboard numbers
  are framed as production, but are extrapolated from laptop probes (stated in `training/README.md`). Reasoned-only findings are marked 🧠 in `_answers/review.md`.

## Issues found in the project (things presented as working that aren't)
- **Offline-first doesn't work:** the server never sends `sync1`, and the Provider detaches its relay during every handshake, so offline edits and edits typed in the first
  round trip never reach the server (`packages/collab/src/provider.ts:43-66`; no `writeSyncStep1` in `apps/api`). `docs/sync-protocol.md` documents the missing half.
- `ws.ts` drops messages that arrive before the async `rooms.join` finishes. Concurrent cold joins create two rooms (`apps/api/src/yroom.ts:40-52`).
- Version **restore is a no-op** (`history.ts:60-66`), applied with a non-relayed origin (`ProseMirrorView.tsx:49`). Its test asserts only replica equality.
- S13–S15 hardening is library-only: `safeApplyUpdate`, `verifyUpdateAuthorship` (also buggy: rejects deletions), `DivergenceAlerter`, telemetry, backup and `drain()` have no
  callers; `setCanEdit` has no caller. The web never sends `member`, so every socket can edit (`ws.ts:51`).
- `docs/runbooks/sync-operations.md` and `docs/postmortems/split-brain-drill.md` describe instances, monitors and log exchange that don't exist (a fabricated drill timeline).
  `chaos.convergence.test.ts` claims to prove "OUR transport" but only uses bare `Y.Doc`s. "The update log is the history", yet only one overwritten blob is stored.
- The server re-encodes, decodes and extracts the full document on every update (`ws.ts:79-99`): ~29 ms (fresh 500-block doc) to ~1 s (churned) per keystroke on this laptop.
- `.env.example` lists `REDIS_URL` "for multi-instance fan-out", but no Redis code exists.
- **Secrets:** none found. Only `.env.example` exists, with placeholder values (not printed).

## Skill links (for COMPETENCY_GRAPH)
- **CRDT / offline sync (new, thin → now strong):** folio `ladder/J2`, `ladder/M1`, `ladder/M2`, `ladder/S2`, `ladder/S3`, `incidents/001`, `incidents/002`, `incidents/003`,
  `navigation/TRADEOFFS.md` W1–W4, interview Q1, Q5–Q9, Q13
- **Testing (property-based, system-level, deterministic CRDT tests):** `ladder/M1` (Provider↔YRooms property), `ladder/J2`, `incidents/001` (a weakened property assertion), review R17
- **Backward compatibility / API versioning:** `ladder/M3`, `ladder/M4` (409 + legacy clients), `incidents/005`, `ladder/S3`
- **Zero-downtime migrations (client-fleet expand/contract):** `ladder/S3`, `ladder/M3`, `incidents/005` → curriculum 07
- **Realtime:** `ladder/S1`, `incidents/004`, `ladder/M1` → curriculum 08
- **Load / back-pressure / retry storms:** `incidents/004` → curriculum 14
- **Accessibility:** `ladder/J1` (sync status live region), `ladder/M4` (conflict banner) → curriculum 11
- **Frontend / React performance:** `ladder/J1` (render cost of per-update state), `ladder/M2` (budgets) → curriculum 12
- **Performance (server hot path, measured):** review R10, `incidents/003`, `ladder/M2`, `ladder/S2`
- **Data modeling / storage design:** `ladder/S2`, `navigation/TRADEOFFS.md` W2
- **Reliability / incidents:** 5 incident branches + postmortems
- **Code review:** `review/EXERCISE.md` (23 findings)
- **Design docs:** S1–S3 + 4 "Why?" drills
- **Unfamiliar codebase:** `navigation/*`, `CHANGE_REQUEST.md`
- **Agentic engineering:** `agentic/WORKFLOW.md` (M1), incident 001 (an agent-style "de-flake" of a property test), interview story 5
- Authz, idempotency, outbox, concurrency: only referenced (saturated). Review R3/R8 are included once each and not expanded.

## Curriculum needs (one central page each; not written)
1. **"CRDT & offline sync" (recommended as curriculum 16).** Scope: item identity (clientID, clock), tombstones and GC, state vectors and the two-sided handshake,
   what "converges" does and doesn't promise (intent loss, LWW attributes), and how to test your *transport* rather than the library. Worked examples: folio M1/J2/INC-001/002.
2. **"Evolving replicated schemas and client fleets".** Scope: expand/contract when old clients rewrite data they don't understand, version handshakes, close codes,
   and stale-bundle control. It could be a section appended to curriculum 07 instead of a new page. Worked examples: folio INC-005, M3, S3.
3. (Smaller) **"Property-based testing discipline".** Scope: seeds, shrinking, turning counterexamples into examples, never weakening assertions, and deterministic
   randomness (fixed clientIDs). Could fold into curriculum 04. Worked examples: folio INC-001, J2.

## Existing learning-doc trees in the repo (verdicts)
- `docs/curriculum/` (15 sprint lessons + RETROSPECTIVE): **KEEP.** A course narrative; link it from the graph as background reading.
- `docs/adr/` (17 ADRs): **KEEP.** Used by `navigation/TRADEOFFS.md`. ADR-0009 §3 and ADR-0014 §3 are deliberately challenged by M4 and INC-002.
- `docs/sprints/` (PR write-ups + `flaw-ledger.md`): **KEEP as a spoiler/answer key.** Don't reuse it for exercises (honored).
- `docs/runbooks/sync-operations.md`, `docs/postmortems/split-brain-drill.md`: **CONVERT TO EXERCISE.** "Verify every runbook step against the code" (they reference
  unwired functions and a fictional drill). Partially done via review R15/R16/R18.
- `docs/sync-protocol.md`, `threat-model.md`, `latency-budget.md`, `perf-audit.md`, `audits/`: **KEEP** (referenced). `sync-protocol.md` must be corrected by M1.
- `LEARNER-GUIDE.md`, `COURSE-RETROSPECTIVE.md`: **KEEP** (course framing). `githelp.md`: **IGNORE** (generic git help).
- No MERGE proposals.

## Honest caveats
- All timings come from vitest probes on this laptop (known to be slow); the ratios are the durable result. Probe code lives only in the session scratchpad, but the
  essential repro code is reproduced inside the sealed answers.
- The incident briefs dress probe numbers as production telemetry, including metrics (event-loop lag, ingress) that Folio doesn't emit. The README says so.
- The incident 004 branch contains a *partially correct* fix for a real main bug, so M1 and INC-004 overlap on purpose. The README orders M1 before INC-004.
- Several ladder answers contain design sketches (S1–S3, M3, M4) that weren't implemented. M1's fix, M2's restore and INC-003's re-encode shrink were verified in probes.
