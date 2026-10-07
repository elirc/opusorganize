# Batch 05 Report: durable execution, CRDT/offline sync, sagas

> **Status note (added 2026-10-06):** this report is a frozen record of the batch and was not updated afterwards. Not every `training/incidents/*` branch it describes is on GitHub: only 21 of the 92 from B01–B07 were pushed, and several projects now live under different elirc repo names. Before you try to check out an incident, see the incident-branch availability note at the top of [`apprenticeship/PROGRESS.md`](../apprenticeship/PROGRESS.md).

*2026-09-24 · I ran `apprenticeship/BATCH_PROMPT.md` on the three distributed-systems topics no earlier batch covered.
Per-project detail is in `projects/<name>.md`. Shared outputs: `apprenticeship/curriculum/16–18` (new),
`apprenticeship/COMPETENCY_GRAPH.md` (updated), `apprenticeship/PROGRESS.md`.*

## 1. Headline: both labs found that `main` doesn't do its core job
- **relay can't run at all.** Its locked BullMQ 5.79.3 rejects the queue name `relay:runs` (colons aren't allowed). The worker crashes on start, and every enqueue fails *after* the Run row is written. **All 151 tests still pass**, because none of them touches BullMQ, Postgres or `worker.ts`.
- **folio loses offline edits.** Edits made offline, or in the first round trip after opening a doc, never reach the server. A property test through Folio's own provider fails on its first generated case; the reference fix passes 200/200.

Both are now the first ticket of their lab (relay J1, folio M1), and both are strong interview stories: "green CI, broken product".

## 2. Tiers
| Project | What it is | Tier |
|---|---|---|
| **gitvg\relay** | Zapier-style workflow engine: Node + React, Postgres, BullMQ, fake vendor farm | **LAB**: durable execution |
| **gitvg\folio** | Notion-style collaborative docs: Yjs CRDT, offline-first | **LAB**: CRDT and offline sync |
| astra5 (Stockade) | Next.js 16 + .NET "Fulfil" service, inventory/payment sagas | DRILL: sagas and compensation |

## 3. What was created
| Project | Commit | Contents | Incidents | Effort |
|---|---|---|---|---|
| relay | `2cc2ec4` | **runnable `training/lab/`** (Postgres :55442, Redis :56392, fake vendors with failure knobs, the real worker, inspect scripts) · 10 tickets (J1 make it boot, M1 determinism, M2 leases/fencing/heartbeats, M3 versioning in-flight runs, M4 durable timers, S1 multi-day onboarding with compensation, S2 in-flight state migration, S3 50× scale) · review (26) · navigation + CR · agentic (M2) · full interview kit | 5 | ~50 h |
| folio | `da45b9c` | 9 tickets (M1 = the real offline-loss bug with a property test; convergence tests, tombstone GC, protocol versioning, conflict UX; S1 multi-device sync at scale, S2 compaction, S3 schema migration with offline clients) · review (23) · navigation + CR-31 · agentic (M1) · full interview kit | 5 | ~50–60 h |
| astra5 | `bdd63f9` | review (16) · mini kit with a **sagas vs 2PC vs outbox** question set | 1 | ~4 h |

**Git notes**
- Every commit touches only `training/` (checked). No containers or worktrees are left.
- Your 9 uncommitted files in astra5 are untouched.
- **relay deviation:** its incident branches sit on `training/base/engine-boots`, which is main plus a 2-file queue-name fix (the J1 answer), because no durable-execution incident can run on an engine that can't start. Do J1 first; the README says so.

**Incident symptoms** (causes sealed in `_answers/`)

*relay*
1. Duplicate welcome emails and a missing sales alert after a publish + restart.
2. Runs stuck "waiting" after a rate-limit episode, with no errors.
3. Duplicate chat posts after a node rotation.
4. Run history grows by 3M rows overnight, and three runs never end.
5. The run page takes seconds; history grows 20× faster.

*folio*
1. Lab panes show `bc` vs `cb` after reconnecting; CI green.
2. Second-tab edits never reach teammates.
3. Heavily edited docs open in seconds.
4. Every deploy becomes a multi-minute outage.
5. New callout blocks vanish from shared docs.

*astra5*
1. Orders needing 3-D Secure silently drop out of reconciliation forever.

## 4. Verification
| Project | Verified |
|---|---|
| relay | Installed with a private pnpm store; **151 tests + typecheck 11/11**. **All 5 incidents reproduced on the live lab** (Postgres + Redis + worker). Incident 003 compared against base: 1 vs 2 chat posts. Incident 005 measured: the run-detail query takes 17 ms at 10 events and **3.4 s (10 MB JSON) at 50k events**. Each incident branch passes its own typecheck and tests, just as it would pass CI. |
| folio | **195 tests on main**. All 5 incidents reproduced:<br>• 003: state 576 KB → 1,512 KB; cold load ~0.4 s → 5–7 s<br>• 004: each reconnect uploads 274 KB vs 0.04 KB; server CPU per client 4.5 → 43 ms<br>• 005: an old-schema client deletes the callout<br>**Not run:** tsc on the incident branches, browser/e2e. |
| astra5 | The incident builds with `dotnet build` (0 warnings). TS tests were **not run**, deliberately, because your uncommitted refund-health work is in progress in that tree. |

## 5. Real defects found (documented, NOT fixed)

**relay**
- Can't boot (above).
- ADR-0016, the stuck-run runbook and the vendor-hang postmortem describe a circuit breaker, stuck-run detection, heartbeats, metrics and a DLQ; **none of it is wired in**.
- "Safe bulk replay" would re-send emails, because the idempotency keys derive from a new run id.
- Failed runs are never retried.
- `dedupeWindow` is never enforced.
- Nested step config isn't rendered, so SheetLite silently drops rows.
- Event sequence numbers come from `count()` plus fire-and-forget inserts, so events are silently dropped.
- `/auth/dev-login` is always registered, and `/api/runs*` has no auth.
- The dev KEK default is hardcoded (`apps/*/src/env.ts`).

**folio**
- Offline loss (above); a first sync message sent before the room join is dropped; two simultaneous first opens create two rooms.
- **Version restore returns an empty update**, and its test only checks that the replicas are equal.
- Size limits, authorship checks, divergence alerts, telemetry, backup, `drain()` and `setCanEdit` are **all unwired**, and the authorship checker would reject every pure deletion.
- The runbook and postmortem describe infrastructure that doesn't exist; `.env.example` lists an unused `REDIS_URL`.

**astra5**
- `services/Fulfil/Services/Worker.cs:70-78` splits payment capture and compensation across **two committed transactions**. A crash in between leaves a captured order invisible to recovery *and* to the `stuckSagas` health metric.

## 6. Existing learning docs: verdicts
| Repo | Verdict |
|---|---|
| relay | `docs/`: KEEP as the design narrative. Its runbooks, postmortem and ADR-0016 are now review material (they describe unwired features). `docs/sprints/flaw-ledger.md`: KEEP (a spoiler; not reused). `githelp.md`: IGNORE. |
| folio | `docs/curriculum`, `docs/adr`: KEEP · `docs/sprints`: KEEP (spoiler) · runbook and postmortem: CONVERT ("verify each step against the code") · `githelp.md`: IGNORE |
| astra5 | `astraupskill/`, `astradocs/`: KEEP |

## 7. Curriculum
- **New pages:**
  - [16 Sagas vs 2PC vs outbox](../apprenticeship/curriculum/16-sagas-vs-2pc-vs-outbox.md)
  - [17 CRDTs and offline sync](../apprenticeship/curriculum/17-crdt-offline-sync.md)
  - [18 Durable execution](../apprenticeship/curriculum/18-durable-execution.md)
- The curriculum now has **18 pages**.
- Folio's other suggestions are noted for later: fleet schema evolution as a section of 07, and property-testing discipline as a section of 04.

## 8. Totals after five batches
- 23 projects
- **69 incident branches**
- 20 blind reviews
- about 110 ladder tickets
- 10 full + 10 mini interview kits
- 18 curriculum pages

Every distinct engineering topic found in the archive audit is now covered. Remaining gaps can only be closed by *doing*:
- a real cloud deploy (gitjira-app → AWS or atlas → Azure)
- SQL Server on atlas
- a first Outline upstream PR

There's no further batch I'd recommend. The rest of the archive repeats covered skills.

## 9. What to do first from B05 (about 1.5 weeks part-time)
1. **relay J1:** find why the engine can't boot while CI is green, and write the test that would have caught it (curriculum 05).
2. **relay lab + INC-003, then INC-001** (checkpoint read, version pinning). Use curriculum 18.
3. **folio M1:** write the property test that exposes the offline-loss bug, then fix it. This is also the agentic exercise.
4. **folio INC-003 and INC-004** (tombstone growth, reconnect storm), measured with the lab's probes.
5. **astra5:** read the `Worker.cs:70-78` finding, then do INC-001 and the sagas-vs-2PC-vs-outbox questions (curriculum 16).
