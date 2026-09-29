# 17 — CRDTs & offline sync: what convergence does and doesn't promise

**The promise.** A CRDT (Yjs, Automerge) guarantees that replicas which have received *the same set of updates* end up in the same state, in any order.
It does **not** guarantee that every update *arrives*, that the merged result is what users meant, or that it's cheap.

**Where real systems break** (your transport, not the CRDT)
1. **Delivery:** the sync handshake is two-sided (send your state vector, receive the diff, *and* send your missing updates). Dropping the first message, or offline edits never being sent, means updates are silently lost and the replicas "converge" on different histories.
2. **Identity:** each client needs a unique client ID. Reusing one (two tabs, a restored snapshot) corrupts the merge.
3. **Growth:** deleted content leaves tombstones. Without GC or snapshot compaction, docs grow and load slowly, and server cost per keystroke scales with document size.
4. **Reconnect cost:** resending the whole state on every reconnect turns a deploy into a thundering herd. Sync by state vector instead.
5. **Schema evolution:** old clients keep old code for weeks. A new block type they don't understand may get *deleted* by them. Version the protocol and handshake, and use expand/contract for client bundles ([07](07-zero-downtime-migrations.md)).
6. **Semantics:** "last writer wins" on a field isn't always the right conflict rule. Some fields need explicit conflict UX.

**Testing discipline:** property tests with random operation orders, random disconnects and a random number of clients, run **through your own provider and transport**, not bare library docs. A "chaos" test that only uses raw Yjs proves nothing about your code.

**Worked examples in your repos**
- **folio** (the main lab):
  - `main` itself loses offline edits and first-round-trip edits. A property test through Folio's Provider fails on the first generated case, while the reference fix passes 200/200. This is ladder `M1`.
  - Incidents:
    - 001: lab panes diverge `bc`/`cb`
    - 002: second-tab edits vanish (client identity)
    - 003: docs grow 576 KB → 1,512 KB, and cold load goes from about 0.4 s to 5–7 s (tombstones)
    - 004: a reconnect storm, 274 KB instead of 0.04 KB per reconnect
    - 005: an old-schema client deletes new callouts
- **buildwhiteboard:** Yjs + ws server (not yet a lab).
- **Outline:** Yjs/Hocuspocus save path (`training/navigation/01-collaborative-save-path-trace.md`).
- **Plane vs Teable** (OSS, READ later): CRDT vs OT.
- Realtime delivery: [08](08-realtime-fanout.md).
