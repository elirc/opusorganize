# Batch 03 — AI assistant / agent apps
Scope: Desktop\{aiapplybot, aicallhelper, aicallhelper2, aicallhelper5, aiheartbeat, aihelper, fableaihelperv2, fableaihelperv3, finalcallhelp, hermes, lucasrouter}  |  Candidate dirs inspected: 11  |  Meaningful projects: 10  |  Tiny/empty/boilerplate: 1 (hermes is docs/prompts-only, no app code — counted separately below)

**Version-lineage note (read this first):** this batch contains two separate "call/interview copilot" families plus one standalone project that got vendored twice.

- **Interview-copilot family (4 generations, 4 different tech stacks):**
  1. `aihelper` — **v1**, Electron/JS. Commit: "Initial commit: AI Call Assistant v1 — Electron interview copilot" (2026-07-17).
  2. `fableaihelperv3` — **v2**, Electron/TS rewrite of v1 for latency (Deepgram streaming WS + parallel session-open). README: "AI Call Assistant v2 ... This is the v2 rewrite of `Desktop/aihelper`". Commit: "Initial commit: AI Call Assistant v2" (2026-07-17).
  3. `aicallhelper` — **v3** (Tauri 2 / Rust core + React/TS front end), independent rebuild, *not* a rewrite of v2's Electron code — it's a fresh architecture (crate/module map, 14 ADRs). Self-identifies "AI Call Assistant v3" in its README. Latest commit 2026-09-23 ("v3.1: call profiles, dock-to-camera...").
  4. `aicallhelper2` — **also "v3"**, but Python/pywebview, a *parallel* independent v3 rebuild on a different stack from #3 (same version number, different tech — confirmed by `pyproject.toml`/`app_core/` vs. `src-tauri/`). Latest commit 2026-09-23 ("Production-readiness pass: fix review backlog R01-R13...").
  5. `aicallhelper5` — **v4**, ground-up rebuild explicitly of the *Python v3* (#4) onto Tauri 2 (Rust) + React/TS: README states "v4 is a ground-up rebuild of the Python/pywebview v3.1.0 on Tauri 2 (Rust core) with a React/TypeScript front end." Latest commit 2026-09-23.
  - So the true chain is: `aihelper`(v1, Electron) → `fableaihelperv3`(v2, Electron) → **fork into two parallel v3 rebuilds** [`aicallhelper` (Rust/Tauri) and `aicallhelper2` (Python)] → `aicallhelper5`(v4, Tauri, rebuilds specifically off the *Python* v3 branch, not the Rust one).

- **CueDeck family (conversation-practice coach, unrelated purpose to the interview copilot — it's a rehearsal/roleplay tool, not a live-call assistant):**
  - `fableaihelperv2/cuedeck` — earlier snapshot (102 files, commit 2026-07-17 "CueDeck updates: Gemini provider, doc refresh").
  - `finalcallhelp/cuedeck` — same app, later/larger snapshot (258 files, commit 2026-09-23), diverged in most `src/main/**` files (providers, security, settings) — confirmed via `diff -rq`. Extra files present only in the newer copy: `providers/llm/demo.ts`, `providers/probeCache.ts`, `settings/providerSettings.ts`. Treat `finalcallhelp` as the current head and `fableaihelperv2` as a superseded duplicate.

- `aiheartbeat` = hourly `claude -p` heartbeat orchestrator + personal workspace dashboard (unrelated to the call-assistant/CueDeck families).
- `lucasrouter` = RouteIQ, Next.js/Leaflet delivery-route-optimizer demo (unrelated domain, only shares the "recent Astra/Fable upskill-doc" tooling pattern).
- `aiapplybot` = local job-application tracker/CLI/dashboard (unrelated domain).
- `hermes` = a prompt-pack / operating-instructions repo for using the "Hermes" CLI agent (Codex-backed); no application code, docs+prompts only.

| Project | Path | Type | Origin | Stack | Complexity | Docs | Disp |
|---|---|---|---|---|---|---|---|
| ApplyBot (aiapplybot) | Desktop\aiapplybot | CLI + local web dashboard | ORIGINAL | Python stdlib, SQLite, no build | Junior+ | STRONG (astraupskill/, dfableandopus/) | B |
| AI Call Assistant v3 (Tauri/Rust) | Desktop\aicallhelper | desktop (Tauri) | ORIGINAL | Rust core + React/TS/Vite front end | Senior-oriented | EXCELLENT (docs/, docs/learn, docs/adr x17) | A |
| AI Call Assistant v3 (Python) | Desktop\aicallhelper2 | desktop (pywebview) | ORIGINAL | Python (app_core/), pywebview, pytest | Mid+/Senior-oriented | EXCELLENT (docs/learn x14, fabledocs/) | A |
| AI Call Assistant v4 (Tauri) | Desktop\aicallhelper5 | desktop (Tauri) | ORIGINAL | Rust crates (audio/contract/llm/prompt/session/settings/stt/shell) + React/TS | Senior-oriented | STRONG (docs/) | A |
| Pulse (aiheartbeat) | Desktop\aiheartbeat | monorepo(2): CLI/daemon + Next.js dashboard | ORIGINAL | Node/TS core, SQLite, Next.js dashboard | Mid+ | STRONG (playbooks/, astraupskill/, dfableandopus/) | B |
| AI Call Assistant v1 (aihelper) | Desktop\aihelper | desktop (Electron) | ORIGINAL | Electron/vanilla JS | Junior+ | USEFUL (docs/) | D |
| CueDeck (early snapshot) | Desktop\fableaihelperv2\cuedeck | desktop (Electron Forge) | ORIGINAL | Electron/TS/Vite, Playwright | Mid | USEFUL (docs/) | F (superseded by finalcallhelp) |
| AI Call Assistant v2 (fableaihelperv3) | Desktop\fableaihelperv3 | desktop (Electron) | ORIGINAL | Electron/TS, Deepgram WS, SSE | Mid | USEFUL (README, inline) | D |
| CueDeck (current) | Desktop\finalcallhelp\cuedeck | desktop (Electron Forge) | ORIGINAL | Electron/TS/Vite, Playwright | Mid+ | STRONG (fabledocs/, cuedeck/docs) | B |
| Hermes prompt pack | Desktop\hermes | docs/prompts only | ORIGINAL | Markdown + PowerShell cleanup scripts | Tiny/Tutorial | USEFUL (READMEs, prompts/) | G |
| RouteIQ (lucasrouter) | Desktop\lucasrouter | web app (Next.js) | ORIGINAL | Next 16, React 19, Leaflet, Vitest | Mid+ | STRONG (docs/, astraupskill/, dfableandopus/) | B |

---

## AI Call Assistant v3 (Tauri/Rust)
- Path: Desktop\aicallhelper            - Origin: ORIGINAL
- Type: desktop (Tauri 2 app, Rust core + React/TS renderer)
- State: complete/working-looking    - Size: ~2000 files including a `.local-voice/venv` bundled Python venv (excluded from real count); source under `src/`, `src-tauri/core` is sizable (multiple crates worth of Rust). - Last modified: 2026-09-23 (commit "v3.1: call profiles, dock-to-camera, reliability and settings fixes")
- Purpose: push-to-record Windows interview/call copilot — captures system-output audio via WASAPI loopback, streams live transcript, and on Stop produces an LLM-generated suggested answer grounded in resume/job description/call profile; window is excluded from screen capture.
- Stack: FE: React/TS/Vite; Core: Rust (Tauri, `src-tauri/core`); STT/LLM: pluggable providers; local free-voice mode via bundled Python/Ollama (`.local-voice/`); Test: Vitest (renderer, `src/**/*.test.tsx`) + Rust `core/tests`; Docs: `docs/ARCHITECTURE.md`, `docs/SPEC.md`, `docs/TESTING.md`, `docs/adr/` (14+ ADRs).
- Architecture: modular monolith — Rust core crate/module map cited by section number in code comments against `SPEC.md`; renderer/main split typical of Tauri.
- Complexity: Senior-oriented — real-time audio capture, WS streaming, provider abstraction, screen-capture-exclusion Windows API interop, latency-budget engineering.
- Educational material: EXCELLENT — `docs/adr/` (14 architecture decision records covering real tradeoffs like window placement/call profiles), `docs/learn/` guided codebase tour, `fabledocs/` (AUDIT.md, DESIGN.md, multiple dated review/readiness reports through 2026-09-22). Project-specific, not generic; clearly maintained across multiple review passes. Preserve as-is — this is flagship-quality documentation.
- Quality observations:
  - SPEC.md is treated as a load-bearing contract cited by section number in code and tests (`docs/README.md`: "code comments cite its section numbers").
  - Explicit security handling around `WDA_EXCLUDEFROMCAPTURE`: reads the setting back and warns when Windows doesn't confirm it (per aicallhelper2 README describing the same shared design — v3 pair).
  - Dedicated `docs/TROUBLESHOOTING.md` (symptom→cause→fix) and `docs/SECURITY.md`.
  - Test coverage spans core Rust (`core/tests`) and full renderer component/unit suite (`AnswerPanel`, `AskForm`, `HistoryBar`, markdown/XSS, state/bridge/session tests).
  - Multiple independently-dated review passes (fabledocs/PROJECT-REVIEW-2026-09-19.md, READINESS-REPORT-2026-09-22.md) suggest iterative hardening rather than one-shot generation.
- Old-AI-generated smells: none seen — evidence of genuine iterative review (dated audit reports, ADRs revisited).
- Skill tags: fe-react, ts-types, be-rest-design, security-owasp, desktop-electron-tauri, ai-llm-integration, test-unit, test-integration, observability-logs, config-secrets
- Duplicate/overlap: sibling "v3" to `aicallhelper2` (same version, different stack — see lineage note); ancestor of `aicallhelper5` is the *Python* branch, not this one.
- Learning value: Very High — real-time systems design, provider abstraction, Windows capture-exclusion security feature, and a genuinely deep ADR trail are rare and valuable interview material.
- Transformation opportunity: use the ADR set + SPEC.md as a template for teaching "how to document architecture decisions on a real project"; could be stripped of PII/keys and published as a portfolio case study.
- Interview stories it could support: "how I designed for sub-1s latency in a streaming pipeline," "how I handled a Windows API integration with a security guarantee (screen-capture exclusion) and made it testable," "why I wrote ADRs and what changed my mind."
- Proposed disposition: A FLAGSHIP — deepest docs/ADR trail in the batch, senior-complexity real-time system, clean test coverage.

## AI Call Assistant v3 (Python)
- Path: Desktop\aicallhelper2          - Origin: ORIGINAL
- Type: desktop (pywebview-based)
- State: complete/working-looking    - Size: ~130 files excl. `.venv`/caches; `app_core/` split into `audio/`, `bridge/`, `llm/`, `session/`, `store/`, `stt/`. - Last modified: 2026-09-23 (commit "Production-readiness pass: fix review backlog R01-R13 and release-review findings")
- Purpose: same product as the Rust v3 (push-to-record Windows interview copilot, WASAPI loopback capture, live transcript, LLM-suggested answer, screen-capture exclusion) — an independent Python/pywebview implementation built in parallel to the Rust one.
- Stack: BE/core: Python (`app_core/`), pywebview + a `frontend/` (per root listing); Test: pytest (`tests/` — 19+ files: `test_capture.py`, `test_deepgram_client.py`, `test_hotkey.py`, `test_machine.py`, `test_protection.py`, `test_retry.py`, `test_secrets.py`, `test_sse.py`, `test_warm.py`); packaging via `aica.spec` (PyInstaller) + `installer.iss` (Inno Setup) + `build.ps1`; type/lint via mypy/ruff caches present.
- Architecture: modular monolith, state-machine-driven session handling (`test_machine.py`, `test_bridge.py` suggest an explicit state machine + IPC bridge).
- Complexity: Mid+/Senior-oriented — same problem domain as the Rust build (audio capture, streaming STT, provider retry/warm-up logic, secrets handling) implemented with Python's constraints (packaging as a native app via PyInstaller/Inno Setup, no native GUI toolkit).
- Educational material: EXCELLENT — `docs/learn/` (14 files), `fabledocs/` (5 files, review/release material). Consistent with the Rust sibling's documentation discipline.
- Quality observations:
  - Explicit `test_secrets.py`, `test_protection.py`, `test_retry.py` — secrets handling, capture-exclusion protection, and provider retry logic are all directly tested, not just implemented.
  - `test_release_metadata.py` suggests release/version metadata is verified, not hand-maintained.
  - Named commit ("fix review backlog R01-R13") shows a tracked, numbered review-and-fix cycle rather than ad hoc patching.
  - Packaging pipeline (PyInstaller spec + Inno Setup installer script + `build.ps1`) is a complete desktop-distribution story, unusual to see fully wired for a personal project.
- Old-AI-generated smells: none seen.
- Skill tags: be-python, be-async-jobs, be-error-handling, security-owasp, desktop-electron-tauri (closest tag; not literally Electron/Tauri but same desktop-copilot category), ai-llm-integration, test-unit, config-secrets, deploy
- Duplicate/overlap: sibling "v3" to `aicallhelper` (parallel independent rebuild, different stack); direct ancestor of `aicallhelper5` (v4 explicitly rebuilds "the Python/pywebview v3.1.0" per that README).
- Learning value: Very High — packaging/distribution completeness (installer, spec file) plus disciplined numbered-review-cycle fix process is a strong "how we ship desktop software" story.
- Transformation opportunity: pair with the Rust v3 as a "same product, two stacks" case study — good teaching material on tradeoffs between a scripting-language desktop app (fast iteration, packaging overhead) and a native/Tauri one (perf, smaller footprint, different security surface).
- Interview stories it could support: "shipping a native Windows installer for a Python app," "running a numbered review-and-fix backlog to production readiness," "testing a state machine that drives a real-time UI."
- Proposed disposition: A FLAGSHIP — same reasoning as the Rust sibling: deep docs, disciplined review process, complete packaging/distribution pipeline.

## AI Call Assistant v4 (Tauri, React)
- Path: Desktop\aicallhelper5          - Origin: ORIGINAL
- Type: desktop (Tauri 2, React/TS front end)
- State: complete/working-looking    - Size: ~12,569 files (includes `node_modules`? — not excluded from this run's cache-only filter, so treat as UNKNOWN/NEEDS DEEPER INSPECTION for a precise LOC count; source itself is organized into `crates/{audio,contract,llm,prompt,session,settings,shell,stt}` + `src/{app,components,generated,ipc,markdown,state,styles}`). - Last modified: 2026-09-23 (commit "Docs ... and a latency benchmark example")
- Purpose: v4 ground-up rebuild of the Python v3 onto Tauri 2/Rust with a React/TS UI; same push-to-record interview/call-copilot product (record → live transcript → Stop & Answer suggested reply, screen-capture exclusion, ~1s latency target with a measured latency chip).
- Stack: FE: React/TS; Core: Rust workspace split into 8 crates (clean separation of audio, contract/IPC types, llm, prompt, session, settings, shell, stt); Test: Vitest for every major component/state file (`App.test.tsx`, `AppProvider.test.tsx`, `reducer.test.ts`, `select.test.ts`, `ipc/fake.test.ts`, `ipc/tauri.test.ts`) + Rust `crates/*/tests`; Docs: `docs/{ARCHITECTURE,AGENTS,CHANGELOG,RELEASE-CHECKLIST,SPEC,TESTING,TROUBLESHOOTING,USER-GUIDE}.md`.
- Architecture: multi-crate modular monolith (Rust workspace, `Cargo.toml` + `crates/*/Cargo.toml`) — the cleanest crate decomposition of any version in the lineage (contract crate isolates the IPC schema; settings/session/llm/stt are separate crates rather than modules).
- Complexity: Senior-oriented — same real-time streaming problem as v3, plus a genuine multi-crate Rust workspace architecture (harder to get right than a single-crate core) and a fake-vs-real IPC test double (`ipc/fake.test.ts` vs `ipc/tauri.test.ts`) for testing the frontend without Tauri.
- Educational material: STRONG — `docs/` covers architecture, testing, troubleshooting, release checklist, changelog, and a dedicated `docs/testing/` subdir plus a latency-benchmark example (per commit message). No astraupskill/dfableandopus curriculum pack here (unlike aicallhelper/aicallhelper2), so slightly below "EXCELLENT."
- Quality observations:
  - `src/ipc/fake.test.ts` + `src/ipc/tauri.test.ts` — deliberate test-double pattern for the Tauri IPC boundary, letting frontend logic be tested without a real Tauri runtime. This is a genuinely good pattern, worth highlighting.
  - `crates/contract` isolates the cross-language (Rust↔TS) data contract — a real "shared types at the boundary" solution.
  - `docs/CHANGELOG.md` present — versioned history is tracked explicitly, distinguishing it from most other projects in this batch.
  - Latest commit explicitly adds a "latency benchmark example," consistent with the family's stated ~1s latency design target being taken seriously and measured, not just claimed.
- Old-AI-generated smells: none seen from manifest/doc evidence; file count of 12,569 needs verification that this wasn't measured including `node_modules`/`target` (NEEDS DEEPER INSPECTION to confirm true source size, but crate/dir structure itself is legitimate and modest).
- Skill tags: fe-react, ts-types, be-rest-design, arch-modular-monolith, desktop-electron-tauri, ai-llm-integration, test-unit, test-integration, observability-metrics-tracing, backcompat-versioning
- Duplicate/overlap: v4 in the aihelper→fableaihelperv3→{aicallhelper, aicallhelper2}→aicallhelper5 lineage; rebuilds the Python v3, not the Rust v3.
- Learning value: Very High — the multi-crate workspace decomposition and the fake/real IPC test-double pattern are both strong, exportable senior-level patterns.
- Transformation opportunity: extract the `crates/contract` + fake-IPC-test-double pattern into a standalone "testing a Tauri app without Tauri" writeup/example, reusable across future Tauri projects.
- Interview stories it could support: "designing a shared contract crate across a Rust/TS boundary," "testing a desktop app's IPC layer without spinning up the runtime," "iterating a real-time latency budget across four rewrites and measuring it every time."
- Proposed disposition: A FLAGSHIP — most architecturally mature crate decomposition in the lineage; strong test-double pattern; latest/most-polished generation of the family.

## Pulse (aiheartbeat)
- Path: Desktop\aiheartbeat            - Origin: ORIGINAL
- Type: monorepo(2 apps): CLI/daemon orchestrator + Next.js personal workspace dashboard
- State: complete/working-looking    - Size: ~747 files excl. deps/caches; `packages/core` (cli.ts, daemon.ts, scheduler.ts + `src/actions`, `src/claude`, `src/prompt`, `src/pulse`) + `packages/dashboard` (Next.js app dir: applications, approvals, automation, playbooks, projects, pulses, tasks, tickets). - Last modified: 2026-09-09 ("feat: add personal workspace for projects, applications, and daily tasks")
- Purpose: hourly `claude -p` heartbeat orchestrator (scheduled Claude invocations against playbooks like triage-new-issues, stale-PRs, CI-health) plus a local Next.js dashboard that tracks personal tasks/projects/job applications, backed by `workspace.db` (SQLite).
- Stack: BE/core: Node/TS (`packages/core`, scheduler+daemon+CLI); Dashboard: Next.js app router, `app/api`; DB: SQLite (`workspace.db`, path overridable via `PULSE_WORKSPACE_DB`); Test: Vitest-style `*.test.ts` alongside `cli.ts`/`daemon.ts`/`scheduler.ts`, plus `packages/core/test/fixtures`; Docs: `playbooks/` (3 files: triage-new-issues, stale-prs, ci-health), `README.md`.
- Architecture: modular monolith split into two packages (core orchestrator vs. dashboard UI) sharing a `packages/shared`; daemon/scheduler pattern for the hourly heartbeat; approvals workflow suggests a human-in-the-loop gate for automated actions.
- Complexity: Mid+ — scheduling/daemon correctness, an approvals gate for autonomous actions, SQLite-backed dashboard with multiple entity types (projects, tasks, applications, tickets).
- Educational material: STRONG — `astraupskill/` (7 files + evidence/ + snapshots/), `dfableandopus/` (6 files: interview questions, stories/resume, code-reading drill, take-home, system-design followups, flashcards), `playbooks/` (3 real operational runbooks). Per user memory, this project's own review caught a `Bash(gh:*)` injection hole and a stale-pulse wedge — genuine security findings from its own audit trail, valuable interview material.
- Quality observations:
  - `approvals/` app route + an "approvals" concept in the dashboard suggests deliberate human-in-the-loop control over autonomous `claude -p` actions rather than fully unattended execution.
  - `PULSE_WORKSPACE_DB` env override for DB path — basic but correct config-for-testability pattern.
  - Deleting a project explicitly reassigns its tasks to "personal tasks" rather than cascading delete — a real product decision documented in the README, evidence of thought about data lifecycle.
  - Dedicated `daemon.test.ts` and `scheduler.test.ts` — the two riskiest pieces (long-running process, timing) are directly tested.
- Old-AI-generated smells: none seen; per memory, a prior audit found and fixed a Bash(gh:*) command-injection hole — worth noting as a *found-and-fixed* smell, i.e. evidence of a real security review process, not a currently-present flaw (would need re-verification to confirm the fix landed — NEEDS DEEPER INSPECTION if reused).
- Skill tags: be-node-express (closest tag for the core service), fe-next, db-sqlite, be-async-jobs, agentic-engineering, ai-llm-integration, security-owasp, test-unit, observability-logs, config-secrets
- Duplicate/overlap: none within this batch; unrelated domain to the call-assistant/CueDeck families.
- Learning value: Very High — one of the few projects in the archive demonstrating agent scheduling + an approvals/human-in-the-loop gate + a self-caught injection vulnerability, which is excellent "how I found and fixed a security bug" interview material.
- Transformation opportunity: could become a flagship writeup on "building a safe autonomous agent scheduler" (daemon + approvals + fixed injection hole) for a portfolio, since the injection-hole story is rare and concrete.
- Interview stories it could support: "found and fixed a shell-injection vector in an agent that shells out to `gh`," "designed an approvals gate so an autonomous scheduler can't silently take destructive actions," "built a scheduler/daemon and tested its timing logic."
- Proposed disposition: B HIGH-VALUE — strong agentic-engineering + security story, but the app itself (personal task tracker) is lower-stakes domain than the call-assistant systems; not quite flagship without confirming the injection fix is verified in code (would bump to A if re-verified).

## AI Call Assistant v1 (aihelper)
- Path: Desktop\aihelper               - Origin: ORIGINAL
- Type: desktop (Electron, vanilla JS)
- State: complete/working-looking (small)    - Size: ~29 files, `src/main/{ipc,llm,main,prompt,sse,store,stt}.js` + `src/renderer/{app,audio}.js` + `test/` (6 test files: audio, llm, prompt, sse, store, stt). - Last modified: 2026-07-17 ("Initial commit: AI Call Assistant v1 — Electron interview copilot")
- Purpose: first version of the Windows interview/call copilot — push-to-record, SiliconFlow SenseVoice for transcription, DeepSeek for the streamed answer, grounded in resume + job description; screen-share exclusion via Windows 10 2004+ API. "Zero runtime npm dependencies — Electron and electron-builder are the only (dev) dependencies."
- Stack: FE/BE: Electron main + vanilla JS renderer (no framework); STT: SiliconFlow SenseVoice; LLM: DeepSeek; Test: plain `test/*.test.js` per module (audio/llm/prompt/sse/store/stt).
- Architecture: simple monolith, one main process module per concern (ipc/llm/prompt/sse/store/stt) — a clean, minimal baseline architecture for the family's later, larger rewrites.
- Complexity: Junior+ — small, single-package Electron app, no framework, straightforward IPC.
- Educational material: USEFUL — `docs/{ALTERNATIVE_APP_SPEC, ARCHITECTURE, CODE_REVIEW, ONBOARDING, README, TESTING}.md` and a `rewrite.md` (likely the design note that led to v2's rewrite). No astraupskill/dfableandopus curriculum pack.
- Quality observations:
  - "Zero runtime npm dependencies" is a genuine, verifiable minimalism claim (worth confirming against `package.json` if reused, but consistent with the small file count).
  - One test file per main-process module — a clean baseline test layout that the later versions kept and expanded (v2/v3/v4 all still test module-by-module).
  - `docs/CODE_REVIEW.md` and `rewrite.md` document the *reasoning* that led to v2, which is unusually good provenance for a superseded version.
- Old-AI-generated smells: none seen; this is clearly the honest "v1, kept simple" baseline rather than an abandoned draft.
- Skill tags: desktop-electron-tauri, ai-llm-integration, be-node-express (loosely — Electron main process), test-unit, config-secrets
- Duplicate/overlap: superseded by `fableaihelperv3` (v2), which is superseded in turn by `aicallhelper`/`aicallhelper2` (v3 pair) and `aicallhelper5` (v4). Keep for lineage/teaching value, not as a standalone deliverable.
- Learning value: Medium — good "here's the simplest version that worked" baseline to contrast against v2–v4 for a before/after architecture story.
- Interview stories it could support: "started minimal (zero runtime deps), then rewrote for latency" — a good complement to the v2 story about the rewrite's specific perf motivation.
- Proposed disposition: D REFERENCE — valuable only in contrast with its 3 later rewrites; not a deliverable on its own.

## AI Call Assistant v2 (fableaihelperv3)
- Path: Desktop\fableaihelperv3        - Origin: ORIGINAL
- Type: desktop (Electron, TypeScript)
- State: complete/working-looking    - Size: ~35 files; `src/main/{ipc,llm,main,prompt,session,sse,store}.ts` + `src/main/{llm,stt}` subdirs + `src/renderer/{app,markdown}.ts` + `src/shared/{pcm,types}.ts` + `test/` (7 files: deepgram, llm, markdown, pcm, prompt, session, sse, store). - Last modified: 2026-07-17 ("Initial commit: AI Call Assistant v2 — Electron interview copilot")
- Purpose: latency-focused TS rewrite of v1 — parallel session-open + Deepgram WS streaming transcript while the other person is still talking, target ~1s stop-to-first-word.
- Stack: FE: Electron renderer TS + a `markdown.ts` streaming markdown renderer; BE: Electron main TS, Deepgram streaming client, SSE for LLM token streaming; Test: `test/*.test.ts` including a dedicated `pcm.test.ts` (PCM audio framing) and `session.test.ts`.
- Architecture: simple monolith, same per-concern module split as v1 but adds an explicit `session.ts` state coordinator and a `shared/` package for cross-process types (`pcm.ts`, `types.ts`) — a step toward the contract-crate pattern later formalized in v4.
- Complexity: Mid — the README's own architecture diagram (record→parallel session-open/getDisplayMedia, pre-open audio buffering with a ~15s cap, tail-flush on stop with a 5s cap) shows real engineering thought about a specific latency budget, not just wiring an API.
- Educational material: USEFUL — detailed README with an ASCII sequence diagram explaining the exact latency-optimization technique (buffer-before-connect, flush-on-resolve); no dedicated docs/ or curriculum folder found at the root.
- Quality observations:
  - The README explicitly calls out a subtlety: "`DeepgramStream` also has an internal pre-open buffer, but in practice it never fills... Treat that o[ld path as dead/vestigial]" — this kind of "here's a red herring in the code, don't trust it" note is a valuable, honest engineering artifact.
  - Pre-open audio buffering with explicit caps (15s buffer, 5s tail-flush) shows bounded-resource thinking for a real-time pipeline.
  - `pcm.test.ts` and `session.test.ts` test the two riskiest pieces (audio framing correctness, session state transitions) directly.
- Old-AI-generated smells: none seen.
- Skill tags: desktop-electron-tauri, ai-llm-integration, ts-types, realtime-ws, perf-investigation, test-unit
- Duplicate/overlap: middle generation between v1 (`aihelper`) and the v3 pair (`aicallhelper`/`aicallhelper2`); superseded.
- Learning value: Medium-High — the "buffer before the socket opens, flush the instant it does" latency technique with named caps is a genuinely good, specific perf-investigation story independent of it being superseded.
- Interview stories it could support: "shaved N seconds off a streaming pipeline by buffering audio during a WS handshake instead of waiting for it," "identified and left a note about a dead code path other engineers might mistake for load-bearing."
- Proposed disposition: D REFERENCE — good lineage/teaching value and one strong perf story, but fully superseded as a product.

## CueDeck (early snapshot, fableaihelperv2)
- Path: Desktop\fableaihelperv2\cuedeck   - Origin: ORIGINAL
- Type: desktop (Electron Forge + Vite)
- State: working-looking    - Size: 102 files excl. deps. - Last modified: 2026-07-17 ("CueDeck updates: Gemini provider, doc refresh, main-process tweaks")
- Purpose: local-first Electron conversation-practice coach (per user memory: free, no-account rehearsal tool — distinct product from the interview-copilot family, though it shares the "AI-assisted live conversation" domain).
- Stack: FE: Vite/TS renderer; BE: Electron main, `src/main/providers/{llm,stt}` (Cerebras, Gemini, Groq, OpenAI-compatible providers; `geminiAudio`, `localWhisper` STT), `src/main/security/` (captureGrant, http, urlPolicy, windowSecurity), `src/main/settings/` (migrations, publicStore, secretVault), `src/main/sessions/coordinator.ts`; Test: Playwright (`playwright.config.ts`, `test-results/`) + unit `test/`.
- Architecture: modular monolith with a real security layer (URL allowlisting, capture-grant, window-security hardening) and a secret vault for API keys — more security-conscious than most projects in this archive.
- Complexity: Mid — multi-provider LLM/STT abstraction, settings migrations, and a dedicated secrets vault.
- Educational material: USEFUL — `docs/` present (per root listing) plus `IMPLEMENTATION_REPORT.md`, `PRIVACY.md`, `SECURITY.md`, `THIRD_PARTY_NOTICES.md`.
- Quality observations:
  - `security/urlPolicy.ts`, `security/windowSecurity.ts`, `security/captureGrant.ts` and `settings/secretVault.ts` show explicit design for a security surface (outbound URL policy, secret storage) rather than just feature code.
  - `settings/migrations.ts` — settings-schema migrations are handled explicitly, a sign of thinking past v1.
  - Playwright e2e config + `test-results/` present, meaning this app has actual e2e coverage, not just unit tests.
- Old-AI-generated smells: none seen.
- Skill tags: desktop-electron-tauri, ai-llm-integration, security-owasp, config-secrets, test-e2e, test-unit
- Duplicate/overlap: **superseded by `finalcallhelp/cuedeck`** — confirmed via `diff -rq`: most `src/main/**` files differ, and the newer copy adds `providers/llm/demo.ts`, `providers/probeCache.ts`, `settings/providerSettings.ts`. This is the same app, earlier snapshot.
- Learning value: Medium — same value as `finalcallhelp`'s CueDeck but as the superseded copy; keep only for lineage.
- Proposed disposition: F CONSOLIDATE — near-duplicate of `finalcallhelp/cuedeck`; the newer copy should be treated as canonical and this one archived/removed to avoid confusion.

## CueDeck (current, finalcallhelp)
- Path: Desktop\finalcallhelp\cuedeck (product root: Desktop\finalcallhelp)   - Origin: ORIGINAL
- Type: desktop (Electron Forge + Vite)
- State: complete/working-looking    - Size: 258 files excl. deps (product root `finalcallhelp` totals 266). - Last modified: 2026-09-23 ("Add improvement-run final report and close out the handoff")
- Purpose: same product as the earlier CueDeck snapshot — local-first conversation-practice coach — now with a documented multi-pass improvement/review history (per `fabledocs/`: 2026-09-18 improvement report, 2026-09-18 final report, 2026-09-19 project review, 2026-09-22 review + handoff).
- Stack: same as the early snapshot plus additions: `providers/llm/demo.ts` (demo/offline provider mode), `providers/probeCache.ts` (provider capability probing/caching), `settings/providerSettings.ts` (finer-grained provider settings); Test: Playwright e2e + unit `test/`, `test-results/`.
- Architecture: same modular monolith + security-layer design as the early snapshot, extended with a provider-capability probe cache — a real "detect what this API key/model can do and remember it" pattern.
- Complexity: Mid+ — adds provider probing/caching and a demo/offline mode on top of the already-solid security/multi-provider base.
- Educational material: STRONG — `fabledocs/` (4 dated review/handoff docs tracking an explicit improvement run with a fix-status handoff) plus the inherited `cuedeck/docs/{ARCHITECTURE,DEVELOPMENT,TESTING}.md`, `SECURITY.md`, `PRIVACY.md`. The dated review trail (2026-09-18 → 2026-09-22, ending in a handoff doc) is a genuine "here's what we found and what's still open" artifact.
- Quality observations:
  - `README_GROQ_TESTING.md` — a full free-tier-provider testing walkthrough (account/key setup, recording, every app action, troubleshooting) is unusually thorough onboarding documentation for a personal project.
  - `probeCache.ts` — caching provider capability probes avoids repeated slow/expensive capability checks; a real perf/cost consideration for a multi-provider LLM app.
  - Root `README.md` explicitly ranks its own docs by recency ("Dated reports (historical; later reports supersede earlier ones)") — good documentation hygiene, avoids stale-doc confusion.
  - `providers/llm/demo.ts` gives the app a working demo path with no API keys — good for onboarding/demoing without secrets.
- Old-AI-generated smells: none seen.
- Skill tags: desktop-electron-tauri, ai-llm-integration, security-owasp, config-secrets, caching, test-e2e, test-unit, deploy
- Duplicate/overlap: supersedes `fableaihelperv2/cuedeck` (see above); treat this directory as the canonical CueDeck.
- Learning value: High — multi-provider abstraction with capability probing/caching, a documented iterative improvement process, and a genuinely good onboarding doc (Groq testing walkthrough) are all solid, specific interview material.
- Transformation opportunity: the provider-probe-cache pattern and the dated-improvement-run doc trail could both be extracted as reusable templates (one code pattern, one process/documentation pattern) for other multi-provider LLM projects in the archive.
- Interview stories it could support: "built a capability probe cache to avoid re-checking what a provider/model supports on every call," "ran a documented improvement pass with dated reports and a handoff doc instead of silently patching."
- Proposed disposition: B HIGH-VALUE — solid, currently-maintained product with a real security layer and a well-documented improvement process; not flagship-tier only because its domain (practice/rehearsal tool) is lower-stakes than the interview-copilot family's real-time systems engineering.

## Hermes prompt pack
- Path: Desktop\hermes                 - Origin: ORIGINAL
- Type: docs-only (prompt library + PowerShell cleanup scripts; no application source)
- State: docs-only    - Size: 39 files; `prompts/` has 20 `.txt` prompt templates (comms-update, daily-log, debug-plan, design-interview, estimate, impl-plan, inject-bug, map-system, monthly-review, pr-description, pr-ready, quiz-architecture, resume-note, review-diff, task-breakdown, test-design, tradeoffs, weekly-notes-review, weekly-plan, work-item), plus 5 `cleanup-*.ps1` scripts, `FABLEDOCS.md`, `FABLEPROMPTS.md`, and 7 `README-*.md` topic guides. - Last modified: 2026-07-18 ("Initial commit: hermes snapshot")
- Purpose: an "operating pack" of reusable prompts and instructions for driving a Codex-backed CLI agent ("Hermes") through recurring engineering rituals — debugging, planning, PR descriptions, weekly reviews, architecture quizzes, note-taking workflows.
- Stack: N/A (no application code) — Markdown + plain-text prompt templates + PowerShell utility scripts.
- Architecture: N/A.
- Complexity: Tiny/Tutorial — no app to build or run; it's a personal productivity/process artifact.
- Educational material: MINIMAL-to-USEFUL as *content about process*, not as software engineering material — e.g. `prompts/debug-plan.txt` encodes a genuinely good debugging protocol ("critique my hypotheses... order all checks by information gain per minute"), which is a transferable engineering-thinking technique, not code.
- Quality observations:
  - `debug-plan.txt`'s "order checks by information gain per minute" framing is a specific, well-articulated debugging heuristic worth preserving even outside this repo's context.
  - `inject-bug.txt` (a prompt for deliberately planting a bug) mirrors the "planted flaws" teaching pattern used across this user's course repos (per memory: harbor/pulse/atlas all use planted-flaw teaching).
  - No tests, no CI, no app — appropriately so, since this is a prompt/process library, not software.
- Old-AI-generated smells: N/A (not code).
- Skill tags: agentic-engineering, design-docs-adrs, code-review, incident-debugging
- Duplicate/overlap: none in this batch; conceptually related to the `astraupskill`/`dfableandopus`/`fabledocs` documentation patterns seen across nearly every other project in the archive (this user has a recurring habit of generating structured review/teaching docs — Hermes is the "prompt source" for that habit, not a downstream artifact of it).
- Learning value: Medium — useful as a personal-process reference (how to structure a debugging session, a PR description, a weekly review) rather than as a coding/system-design portfolio piece.
- Proposed disposition: G ARCHIVE — valuable personally but out of scope for a software-engineering portfolio; no code to showcase.

## RouteIQ (lucasrouter)
- Path: Desktop\lucasrouter            - Origin: ORIGINAL
- Type: web app (Next.js, deployed to Vercel)
- State: complete    - Size: 204 files excl. deps; `src/app/{dispatch,driver,api}`, `src/components/{dispatch,driver,map,ui}`, `src/data/`, `src/lib/`; `tests/` dir present. - Last modified: 2026-09-06 ("feat: rebuild workspace UI and optimize startup")
- Purpose: mobile-first delivery-route-optimization demo for a fictional Madison, WI package operation — dispatcher view (map of all stops, run optimizer, reassign stops by hand) and driver view (stop-by-stop navigation, delivery proof capture, skip/fail handling, end-of-day report). Routing algorithm is an explicitly swappable placeholder (`nn-2opt-v1`) behind `POST /api/optimize`.
- Stack: FE: Next.js 16 (App Router), React 19, Leaflet/`react-leaflet` for maps, `@dnd-kit` for drag-and-drop stop reassignment; Test: Vitest (7 `.test.*` files) + a custom `scripts/smoke-e2e.mjs` (per memory: 41-check Puppeteer smoke test); Deploy: Vercel free tier, `.vercel/project.json` present; no backend DB — mock JSON data (`src/data/{depot,drivers,paths,stops}.json`).
- Architecture: SPA/SSR hybrid via Next.js App Router; a clearly isolated routing-algorithm boundary (single `/api/optimize` endpoint) designed so a real optimizer can be dropped in without UI changes — documented in `docs/ALGORITHM_INTEGRATION.md`.
- Complexity: Mid+ — real-time-feeling map UI, drag-and-drop stop reassignment, before/after metrics, a documented performance-optimization pass (`docs/REBUILD.md`, `docs/performance-before.json`/`performance-after.json` — measured, not claimed).
- Educational material: STRONG — `astraupskill/` (8 files incl. evidence.json + snapshots/ + images/) and `dfableandopus/` (6 files: interview Qs, stories/resume, code-reading drill, take-home, system-design followups, flashcards); `docs/ALGORITHM_INTEGRATION.md`, `docs/REBUILD.md`, `DECISIONS.md`.
- Quality observations:
  - Explicit before/after performance JSON snapshots (`docs/performance-before.json`, `performance-after.json`) — a measured perf-optimization claim, not just an assertion, tied to a documented rebuild (`docs/REBUILD.md`: "Startup now defers road geometry, drag-and-drop, map popups, and delivery dialogs until they are needed" — real code-splitting/lazy-loading strategy).
  - `DECISIONS.md` at the root is a lightweight ADR-style log.
  - The `/api/optimize` boundary is a genuinely good example of designing an interface for a not-yet-built component (the "real" routing algorithm) — good system-design talking point.
  - `verify` script chains typecheck + lint (max-warnings=0) + test — a real quality gate, not just a `test` script.
- Old-AI-generated smells: none seen; per user memory, "Lighthouse pessimistic on this laptop (dispatch 54/71 calibrated)" — a known measurement caveat already tracked by the user, not a hidden defect.
- Skill tags: fe-react, fe-next, fe-perf, fe-state, ts-types, be-rest-design, test-unit, test-e2e, deploy, design-docs-adrs, perf-investigation
- Duplicate/overlap: none in this batch.
- Learning value: Very High — measured perf-optimization story with before/after data, a clean swappable-algorithm architecture boundary, and drag-and-drop + map real-time UI work are all strong, specific, verifiable portfolio material.
- Transformation opportunity: could be extended with a real routing algorithm behind the existing `/api/optimize` contract as a capstone exercise, since the interface is already documented for exactly that.
- Interview stories it could support: "designed an API boundary so a mock algorithm could later be swapped for a real optimizer with zero UI changes," "measured and fixed a startup-performance regression with before/after Lighthouse-style data," "built a drag-and-drop reassignment UI backed by an undo-safe state model."
- Proposed disposition: A FLAGSHIP — measured performance work, clean architecture boundary, strong curriculum material, deployed and demoable on Vercel.

## ApplyBot (aiapplybot)
- Path: Desktop\aiapplybot             - Origin: ORIGINAL
- Type: CLI + local web dashboard
- State: complete    - Size: 46 files excl. caches; `applybot/{application_store,ats,browser,cli,dashboard,legacy_history,llm,profile,tracker}.py` (~2441 total lines across these), `applybot/web/`, `tests/`. - Last modified: 2026-07-17 ("Initial commit: ApplyBot — AI job-application filler CLI")
- Purpose: local application tracker (SQLite-backed) and Playwright-assisted job-application form filler; dashboard supports create/search/edit/delete with version conflicts and retained change history; CLI history merges SQLite with legacy JSONL records.
- Stack: BE: Python stdlib only for the dashboard (no framework, no JS build — explicit design choice per README); DB: SQLite (`data/applications.sqlite3`) with a JSONL legacy-import path (`import-history --dry-run`); browser automation: `browser.py` (likely Playwright, per user memory of a sibling CLI); Test: `tests/`.
- Architecture: simple monolith; private-token-gated local dashboard (binds to 127.0.0.1, token held in browser memory, regenerated on restart) — a real, if minimal, auth model for a local tool.
- Complexity: Junior+ — CRUD dashboard with version-conflict handling and change history is a step above basic CRUD.
- Educational material: STRONG — `astraupskill/` (11 files incl. codebase map, concepts, worked change, testing/debugging, practice, solutions/review, trace lab, translation, VERIFICATION.md) + `dfableandopus/` (6 files: interview Qs, stories/resume, code-reading drill, take-home, system-design followups, flashcards). README explicitly points learners at `astraupskill/README.md` to "study the actual code as a CRUD web application" — this project is positioned as a teaching artifact first.
- Quality observations:
  - Explicit "version conflicts and retained change history" in the dashboard — optimistic-concurrency-style conflict handling on a CRUD app, called out directly in the README, not left implicit.
  - Local-only auth model (private URL token, 127.0.0.1 bind, in-memory token) is a sensible, correctly-scoped design for a single-user local tool — not over- or under-engineered.
  - Explicit legacy-data migration path (`import-history --dry-run`, SQLite-vs-JSONL coexistence documented) shows real data-migration thinking, not just "start fresh."
- Old-AI-generated smells: none seen.
- Skill tags: crud-basic, db-sqlite, db-concurrency, be-python, authn, test-unit, legacy-codebase-reading
- Duplicate/overlap: none in this batch; separate lineage from the call-assistant family despite the "AI" in its purpose (LLM used for ATS-style content, not the primary teaching focus).
- Learning value: High — this repo is explicitly positioned (by its own README and astraupskill pack) as a "read this CRUD app to learn CRUD done right" teaching artifact, and the version-conflict/legacy-migration handling gives it more depth than a toy CRUD example.
- Interview stories it could support: "designed optimistic-concurrency conflict handling for a local multi-writer CRUD app," "built a legacy-data migration path that coexists with a new SQLite store instead of a risky one-shot conversion."
- Proposed disposition: B HIGH-VALUE — deliberately a teaching-grade CRUD implementation with more depth (conflicts, legacy migration, scoped local auth) than most CRUD exercises in the archive.

## Batch observations
- **Overtrained pattern:** nearly every project in this batch (and per the user's memory index, across the whole archive) carries the same three-tier documentation scaffold — `astraupskill/` (codebase-map → concepts → worked-change → testing/debugging → practice → solutions → trace-lab → translation → VERIFICATION), `dfableandopus/` (interview Qs → stories/resume → code-reading drill → take-home → system-design followups → flashcards), and `fabledocs/` (dated audit/review/readiness reports). This is a strength (consistent, deep teaching material) but also a real duplication risk: identical folder/file names recur project-to-project, and if this portfolio audit is ever consolidated, these packs should be spot-checked for genuinely project-specific content vs. templated boilerplate (this batch's spot-checks — debug-plan.txt in hermes, the ADRs in aicallhelper, the perf JSON in lucasrouter — were project-specific, not generic, but that was not verified for every file in every pack).
- **Version-lineage risk:** the interview-copilot family (aihelper → fableaihelperv3 → {aicallhelper, aicallhelper2} → aicallhelper5) and the CueDeck pair (fableaihelperv2 vs finalcallhelp) are the two clearest duplication clusters in the whole batch. Any portfolio consolidation must decide which generation(s) to feature — likely `aicallhelper` or `aicallhelper2` (v3s) and `aicallhelper5` (v4) as flagships, `aihelper`/`fableaihelperv3` (v1/v2) as "lineage/before-after" reference only, and `finalcallhelp/cuedeck` as canonical over `fableaihelperv2/cuedeck`.
- **Surprising strength:** the call-assistant family is unusually rich in *measured* engineering claims rather than assertions — explicit latency budgets with named caps (v2's 15s/5s buffers), a measured latency chip in v3/v4, before/after performance JSON in lucasrouter, and a provider-capability probe cache in CueDeck. This is a real differentiator versus typical AI-generated portfolio filler.
- **Gap:** no project in this batch has a server-side/multi-tenant backend with a real database beyond SQLite — everything here is local-first desktop or a demo web app with mock/local data. If the portfolio needs a "production backend at scale" story, it won't come from this batch (aiheartbeat's dashboard is the closest, but it's still a personal single-user SQLite tool).
- **hermes is the outlier:** it's the only "project" in this batch with zero application code — pure prompt/process library. Keep it out of any "projects" showcase; it may still be useful as personal tooling documentation.
