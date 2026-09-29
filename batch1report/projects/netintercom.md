# netintercom: B01 report

**Project:** `C:\Users\Owner\Desktop\netintercom` (NetIntercom: .NET 8 API + SignalR + Hangfire + Postgres, React inbox + embeddable widget). Own git repo (`origin` = github.com/elirc/dotnet-intercom, **not pushed** by me).
**Tier:** LAB (Phases 2, 3, 4, 5 done; Phases 1 and 6 skipped per brief).
**Main tree:** it was clean before I started (no user changes). I committed only `training/` with a pathspec commit. No source edits on `main`.

## Commits
| Ref | Hash | Content |
|---|---|---|
| `main` | **467ab4a** | `training: add B01 apprenticeship materials` (50 files, `training/` only) |
| `training/incidents/001-widget-note-leak` | 8a0f386 | incident bug (5 files) |
| `training/incidents/002-unassigned-queue-spike` | 5cc8d8d | incident bug (1 file) |
| `training/incidents/003-sla-escalation-storm` | 0c89976 | incident bug (1 file) |
| `training/incidents/004-widget-transcript-exposure` | e813e94 | incident bug (1 file) |
| `training/incidents/005-inbox-list-latency` | daf7666 | incident bug (5 files) |

All incident branches are based on `f2198dd` (the original HEAD). The worktrees were created in the scratchpad and removed afterwards, and `git worktree list` shows only the main tree.

## Incident symptoms (the cause is sealed in `training/_answers/incident-00N.md`)
1. **001:** A customer saw agent-only text in the preview bubble next to the chat launcher.
2. **002:** New conversations pile up unassigned while the inbox shows agents online. Unassigned ratio went from 1.8% to 11%.
3. **003:** SLA-breach toasts appear 3–4× per breach, and the count grows every day after the move to 3 replicas.
4. **004:** A pen test found a visitor can read support replies in another customer's conversation.
5. **005:** Inbox list p95 went from 180 ms to 3.7 s, DB CPU above 85%, and the Npgsql pool is exhausted during business hours.

## What I created (all under `C:\Users\Owner\Desktop\netintercom\training\`)
- `README.md`: index, branch table, suggested order, time estimate (**about 38–46 h**).
- `ladder/`: J1 409-on-concurrency, J2 transcript cursor pagination, J3 office-hours admin endpoint; M1 inbox query at 400k rows, M2 idempotent visitor send (backward-compatible with cached widgets), M3 widget reconnect delivery, M4 agents logged out by the refresh race; S1 3-replica scale-out, S2 workspace multi-tenancy, S3 SLA escalation outbox with snooze and business-hours clock.
- `review/EXERCISE.md`, `review/COMPARE.md`: 60-min blind review, compared against **two** references (mine and the repo's existing `docs/architecture-review.md`).
- `incidents/001–005`: page/alert, logs, metrics, the suspect PR diff and 5 tasks each. Each fits on one page.
- `navigation/ARCHITECTURE.md` (context, components, 3 flows traced file by file, data model, tests, build), `ONBOARDING.md`, `TRADEOFFS.md` (4 decisions in the "Why?" format), `CHANGE_REQUEST.md` (transfer system messages).
- `agentic/WORKFLOW.md` (M2 through spec → implementer → adversarial reviewer → revision → verification → graded explanation), `agentic/VERIFY_AI_OUTPUT.md`.
- `interview/`: `PROJECT_STORIES.md` (5 STAR skeletons), `TECHNICAL_QUESTIONS.md` (20), `SYSTEM_DESIGN.md`, `MOCK_DEFENSE.md`, `FLASHCARDS.md` (25).
- `_answers/` (20 files): 10 ladder answers, `review.md` (26 ranked findings), 5 incident answers with postmortems, change-request, technical-questions, flashcards, agentic-grading rubric.

## Verification
- **Build:** `dotnet build NetIntercom.sln` succeeded (0 errors, 0 warnings) on **all 5 incident branches** with the machine's .NET SDK 10.0.302. The repo has no `global.json`, so the SDK-pinning workaround wasn't needed.
- **Unit tests:** `DOTNET_ROLL_FORWARD=Major dotnet test tests/NetIntercom.UnitTests` → 27/27 pass on branches 004 and 005. There's no .NET 8 runtime here, so roll-forward to 10 was required. The branches 001–003 changes are in projects the unit tests don't reference (Api) or in code with no coverage, so they pass by construction. The fact that the existing suite doesn't catch any incident is intentional and noted in the lab.
- **UNVERIFIED:** integration tests (they need Docker/Testcontainers; not run). Frontend builds of the incident changes in the widget and inbox (`npm run build` not run; TS changes are small and additive). Runtime reproduction of every incident is untested. The symptoms are reasoned from code, not observed.
- Several ladder answers make EF/Npgsql translation claims (e.g. `Guid.CompareTo` in cursors, the filtered-include SQL shape). These are flagged as "verify" in the answers where they're uncertain.

## Issues found in the project
- **Secret/credential locations (no values):** `src/NetIntercom.Api/appsettings.Development.json` (committed dev JWT signing key, labelled dev-only); `src/NetIntercom.Api/appsettings.json` (DB connection string with the docker-compose password); `docker-compose.yml` (same password). Low risk, since they're all local-dev values.
- **Seeds a known admin password in every environment:** `Seed:Enabled=true` sits in the *base* `appsettings.json:16-18`, and `DbSeeder` creates `admin@…` with the README-documented password and logs it. That's a real security bug, not just dev convenience. The existing docs mention the seeding but don't flag it.
- **Presented as working but isn't:**
  - README:79 says both clients catch up with `?after=`. Neither does.
  - The widget **never rejoins its `vconv:` group after a SignalR reconnect**, so live replies stop after any network blip. Not in the existing review.
  - README claims OpenTelemetry. There's no exporter and only ASP.NET instrumentation.
  - Hangfire dashboard "admin JWT required" is unreachable from a browser.
  - Snooze never wakes.
  - The widget's `messagesRead` handler is an empty stub, and there's an empty `<span />` fake read receipt.
  - `HappyPathTests` routing assertion is weak and depends on the time of day.
- **The existing `docs/architecture-review.md` §2.3 is wrong:** overlapping SLA sweeps don't throw `DomainException`. They silently double-write, because the guard is per-`DbContext` in memory and `SlaTimer` has no concurrency token. The lab uses this as a "don't trust the doc" exercise.
- Other new findings, beyond the existing docs: inbox `conn.on` handler stacking on remount; `LoggingBehavior` logs 4xx at Error; `SlaTimer.MarkMet` ignores the deadline; every `messageCreated` makes every agent refetch the list; the transcript endpoint is unbounded.

## Skill links (for COMPETENCY_GRAPH)
- web/TS/React → `ladder/M3`, `ladder/M4`, `_answers/review.md` R16, `interview/TECHNICAL_QUESTIONS.md` Q12–14
- API design → `ladder/J1`, `ladder/J2`, `ladder/J3`, TQ1–4
- data modeling/SQL/indexes/transactions/concurrency/migrations → `ladder/M1`, `ladder/M2`, `incidents/005`, `incidents/003`, TQ5–8, S1 §schema
- authn/authz/multi-tenancy → `incidents/004`, `ladder/S2`, `ladder/M4`, review R1/R2/R19, TQ15–17
- testing → `ladder/J1–J3` (Testcontainers), review R23, TQ18, `agentic/VERIFY_AI_OUTPUT.md`
- async jobs/queues/idempotency/outbox → `incidents/003`, `ladder/S3`, `ladder/M2`, TQ9–11
- caching → thin: only React Query invalidation strategy (`ladder/M1` multiplier, TQ14)
- observability → `incidents/002`, `incidents/004` (blast radius), review R17, TQ19–20, S3 metrics
- deployment/cloud/config/secrets → `ladder/S1`, review R2/R15/R18
- security (OWASP) → `incidents/001`, `incidents/004`, review R1/R2/R20
- performance → `incidents/005`, `ladder/M1`, `ladder/J2`
- reliability/incidents → `incidents/001–005`, `ladder/S3`
- backward compatibility → `ladder/M2` (cached widget bundles), `ladder/J2`, TRADEOFFS §4, TQ4
- design docs/ADRs → `ladder/S1–S3`, `navigation/TRADEOFFS.md`
- code review → `review/EXERCISE.md` + `COMPARE.md`
- unfamiliar-codebase navigation → `navigation/ARCHITECTURE.md`, `ONBOARDING.md`, `CHANGE_REQUEST.md`
- agentic engineering → `agentic/WORKFLOW.md`, `agentic/VERIFY_AI_OUTPUT.md`, `_answers/agentic-grading.md`
- **realtime/WebSockets (suggest adding as a skill area):** `ladder/M3`, `incidents/001`, `incidents/002`, `ladder/S1`, TQ12–13, MOCK_DEFENSE §2–3

## Curriculum needs (central pages worth writing once; I didn't write them)
1. **SignalR connection lifecycle and groups.** Connection ids, what's lost on reconnect, groups vs users, backplane delivery semantics (at-most-once), and why catch-up is load-bearing.
2. **Optimistic concurrency in EF Core + Postgres.** `xmin`/row versions, `DbUpdateConcurrencyException`, 409 vs 412/ETag, why in-memory domain guards don't protect across `DbContext`s.
3. **Idempotency keys and unique-violation handling.** Insert-then-catch 23505 vs check-then-insert, `ChangeTracker.Clear`, key scoping, retention.
4. **Transactional outbox.** Write-then-publish failure modes, dispatcher with `SKIP LOCKED`, retries/backoff/DLQ, stable idempotency keys downstream.
5. **Adopting EF migrations on an `EnsureCreated` database.** Baseline migration, history insert, `CREATE INDEX CONCURRENTLY`/`suppressTransaction`, migration bundles in a pre-deploy step.
6. **Recurring background jobs in multi-instance deployments.** Hangfire recurring ids, distributed locks, `DisableConcurrentExecution`, set-based idempotent sweeps.
7. **Cursor (keyset) pagination.** Composite cursors and tie-breaks, index support, when offset is acceptable.
8. **Row-level multi-tenancy.** EF global query filters (one-filter-per-entity trap before EF 10), Postgres RLS as a fail-closed backstop, background jobs without an HTTP tenant.

## Existing learning-doc trees
| Tree | Verdict | Why |
|---|---|---|
| `docs/upskill/` (47 files, 8 sections) | **KEEP** | Project-specific and line-anchored. Its ticket lists (G1–G10, M1–M5, S1–S4) overlap with mine only in theme. Link it from the graph as reading material. Note its README calls the repo "no git history". It now has 2 commits. |
| `docs/architecture-review.md` | **CONVERT TO EXERCISE** (done in place: it's now "reference B" in `training/review/COMPARE.md`, gated behind the blind review) | It's effectively an unsealed answer key. It's high quality but §2.3 is wrong. Don't move it. |
| `docs/upskill/08-reference/risk-register.md` | **KEEP** (gated the same way) | Duplicates the review. The learner is told not to read it before the blind review. |

## Honest caveats
- Incident symptoms, metrics and log lines are **simulated** narratives built from the code paths. They're internally consistent, but I haven't reproduced any of them on a running stack.
- Incident 002's magnitude (11% unassigned) depends on synchronized proxy-cut reconnects. The mechanism is real, but the number is illustrative.
- Incident 003's "17 recurring jobs" assumes pod names change per deploy/restart (true for Container Apps/K8s). On a single fixed host the bug would be one extra job, not a growing number.
- There are no tests on the incident branches that demonstrate the bugs. Writing the failing regression test is left to the learner (it's in each incident's tasks).
- Line numbers cite `f2198dd`. The `training/` commit doesn't touch source, so they remain valid on `main`.
