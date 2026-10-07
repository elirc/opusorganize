# 17 — CRDTs & offline sync: what convergence does and doesn't promise

**The promise.** A CRDT (Yjs, Automerge) guarantees that replicas which have received *the same set of updates* end up in the same state, in any order.
It does **not** guarantee that every update *arrives*, that the merged result is what users meant, or that it's cheap.

**Where these repos live now (checked 2026-10-06):**
- **folio**: code is at `elirc/folio` (main @ `b81e960`). Its `training/` tree is **not** on that repo's main. It is in the monorepo, at `elirc/gitvg: folio/training/` (@ `af91bab`).
  The five `training/incidents/00N-*` branches were never pushed to `elirc/folio` or `elirc/gitvg`; `git ls-remote` shows no `training/*` refs on either. They existed only in the local `Desktop\gitvg\folio` clone at B05 (2026-09-24).
- **buildwhiteboard**: `elirc/buildwhiteboard` (main @ `e8f70e2`). It has `astraupskill/` notes, but no `training/` lab.
- **Outline**: `elirc/masteroutline`, path `outline/training/` (main @ `3409d2b`).

**Where real systems break** (your transport, not the CRDT)
1. **Delivery:** the sync handshake is two-sided (send your state vector, receive the diff, *and* send your missing updates). Dropping the first message, or offline edits never being sent, means updates are silently lost and the replicas "converge" on different histories.
2. **Identity:** each client needs a unique client ID. Reusing one (two tabs, a restored snapshot) corrupts the merge.
3. **Growth:** deleted content leaves tombstones. Without GC or snapshot compaction, docs grow and load slowly, and server cost per keystroke scales with document size.
4. **Reconnect cost:** resending the whole state on every reconnect turns a deploy into a thundering herd. Sync by state vector instead.
5. **Schema evolution:** old clients keep old code for weeks. A new block type they don't understand may get *deleted* by them. Version the protocol and handshake, and use expand/contract for client bundles ([07](07-zero-downtime-migrations.md)).
6. **Semantics:** "last writer wins" on a field isn't always the right conflict rule. Some fields need explicit conflict UX.

**Testing discipline:** property tests with random operation orders, random disconnects and a random number of clients, run **through your own provider and transport**, not bare library docs. A "chaos" test that only uses raw Yjs proves nothing about your code.

**Quick reference: the Yjs sync handshake (v1)**

| Message | Sent by | Carries | Meaning |
|---|---|---|---|
| `sync1` | **both** peers, on connect | state vector | "Here's what I have; send what I lack." |
| `sync2` | reply to `sync1` | delta for that state vector | "Here is exactly what you're missing." |
| `update` | either peer, steady state | one incremental update | "Here is a new change." |

If only one side sends `sync1`, only one side learns what it's missing. The other side's unsent edits (offline work, edits typed during the handshake) stay stranded.

**Worked examples in your repos**
- **folio** (the main lab):
  - `main` itself loses offline edits and first-round-trip edits. At B05 (2026-09-24, base `af51546`), a property test through Folio's Provider failed on the first generated case, while the reference fix passed 200/200. This is ladder `M1`.
    At `elirc/folio` HEAD `b81e960`, the code that causes it is unchanged (traced below). The 200/200 run was not repeated in this pass.
  - Incidents (briefs in `elirc/gitvg: folio/training/incidents/`; the bug branches are local-only, see above):
    - 001: lab panes diverge `bc`/`cb`
    - 002: second-tab edits vanish (client identity)
    - 003: docs grow 576 KB → 1,512 KB, and cold load goes from about 0.4 s to 5–7 s (tombstones)
    - 004: a reconnect storm, 274 KB instead of 0.04 KB per reconnect
    - 005: an old-schema client deletes new callouts
  - All of these numbers come from vitest probes on the user's laptop at B05. `folio/training/README.md` says to compare ratios, not absolutes. The incident briefs present them as production telemetry that Folio doesn't actually emit.
- **buildwhiteboard:** Yjs + ws server (not yet a lab). It's a useful **contrast**: its server sends its own `sync1` (below).
- **Outline:** Yjs/Hocuspocus save path (`elirc/masteroutline: outline/training/navigation/01-collaborative-save-path-trace.md`, 1,547 words). That trace cites Outline file:lines against its own baseline `37ca0d5`. I confirmed the trace file exists, but not the Outline source lines it cites.
- **Plane vs Teable** (OSS, READ later): CRDT vs OT. Not re-verified in this pass.
- Realtime delivery: [08](08-realtime-fanout.md).

## Worked trace: an offline edit in folio, keystroke to nowhere

All lines are `elirc/folio` @ `b81e960`.

1. **The protocol core is correct.** `elirc/folio: packages/collab/src/protocol.ts:70-79` (`readSyncMessage`): a `sync1` is answered with `writeSyncStep2` (the delta), and a `sync2`/`update` is applied to the doc. The comment block at `protocol.ts:15-18` even says `sync1` is sent by "both peers". So does `docs/sync-protocol.md:10` ("both, on connect").
2. **The client starts the handshake.** `elirc/folio: packages/collab/src/provider.ts:43-47` (`startSync`) sets `synced = false`, calls `detachLocal()` and sends the client's `sync1`. From now on the local `doc.on("update")` relay is **off**.
3. **The server replies, but only half.** `elirc/folio: apps/api/src/yroom.ts:119-120` passes the client's `sync1` to `readSyncMessage` and sends back the `sync2`. Grep `writeSyncStep1` in `apps/api/src`: the only hits are `yroom.test.ts:3` (an import) and `:71`, a test that sends a *client* `sync1`. **The server never sends its own `sync1`**, so the client is never asked "what do you have that I lack?"
4. **The client finishes and re-attaches.** `provider.ts:57` → `finishSync` (`:60-66`) applies buffered remote updates, sets `synced = true`, and only then calls `attachLocal()` (`:68-73`).
5. **Where the edit is lost.** The offline paragraph was already in the local `Y.Doc` before step 2. `attachLocal` only relays updates that happen *after* it attaches, and nobody ever sends the client's pre-existing state. Any keystroke typed between steps 2 and 4 is lost the same way: it fires `doc.on("update")` while the listener is detached.
   The edit survives only in the user's own tab or IndexedDB. The server, teammates and exports never see it.
6. **Why it never gets another chance.** The next live keystroke *does* arrive at the server (step 4 onward). It's a Yjs update whose dependencies (the stranded offline items) the server doesn't have, so Yjs parks it as pending instead of integrating it. The M1 hints point at `Y.Doc.store.pendingStructs`.
   That's how the system "converges" on two different histories with no error anywhere.

The fix (M1's reference answer) is O(delta): the server also sends `sync1` with its state vector, and the client answers with a `sync2` containing exactly what the server lacks. Note that the client side already handles this: `provider.ts:55-56` replies to any incoming `sync1`.
The fix has to keep old clients working for a release (M1's constraint list), and must **not** resend whole state. Incident 004 is exactly that naive fix: 274 KB per reconnect.

### Contrast: buildwhiteboard does the handshake both ways

`elirc/buildwhiteboard @ e8f70e2: server/index.js:300-303` sends the server's own `writeSyncStep1` to every new socket, and `:208-214` answers the client's `sync1` with `writeSyncStep2`. The client uses the stock `y-websocket` `WebsocketProvider` (`client/src/App.tsx:3, 122`).
Same library, different transport, and this one doesn't have folio's stranded-edit bug. That's the whole point of "test your transport, not the CRDT".
buildwhiteboard pays elsewhere: `server/store.js:90-107` (`applyUpdate`) copies the entire document into a candidate `Y.Doc` and re-encodes it twice on **every** update (`:94`, `:96`, `:98`). That's correct and size-limited (413 at `:97`), but per-keystroke cost scales with document size. This is the same family as folio's R10 finding below.

## Failure mode, step by step: the cold-join race (folio review R2/R3)

This is a second delivery bug on folio main, independent of M1. Lines are @ `b81e960`.
1. A socket connects. `elirc/folio: apps/api/src/ws.ts:45-52` starts an **un-awaited** async IIFE: it looks up the member role, then `await rooms.join(...)`.
2. The message handler is registered synchronously at `ws.ts:54-57`, so the client's `sync1` can arrive **before** `join` resolves.
3. `yroom.ts:102-103`: `handle()` looks up `socketDoc`. That entry is only set at the end of `join` (`:54`), so the early `sync1` returns silently. The client waits for a `sync2` that never comes, so `synced` stays false and every local edit stays unrelayed.
4. Two sockets cold-open the same doc. Both reach `yroom.ts:40` with no room, both `await this.load(docId)` at `:43`, and each `rooms.set` at `:51` overwrites the other. Now there are **two authoritative Y.Docs** for one document, and sockets in different rooms never see each other's edits.
5. Nothing logs and CI stays green, because the room tests join sequentially.

A senior fix is a per-docId in-flight join promise (`Map<string, Promise<Room>>`), plus buffering messages per socket until join resolves. That's the same "buffer, don't drop" rule `provider.ts:50-53` already applies on the client.

## Goal + Check ladder

**Goal:** you can explain, from code, why a CRDT app can "converge" and still lose user data. You can point to the exact line where it happens.

1. **(Junior) Read the protocol table against the code.** Open `elirc/folio: docs/sync-protocol.md:10` and `apps/api/src/yroom.ts`.
   **Check:** grep `writeSyncStep1` under `apps/api/src`. You should get exactly two hits, both in `yroom.test.ts` (`:3` import, `:71` a client-side `sync1`), and none in a server send path. In one sentence, say which half of the handshake is missing.
2. **(Junior) Find the detached window.** **Check:** in `provider.ts`, name the line that turns the local relay off (`:45`) and the line that turns it back on (`:65`). List which user actions in between are never sent.
3. **(Junior→mid) Explain the "proves OUR transport" claim.** Open `elirc/folio: packages/collab/src/chaos.convergence.test.ts`. Its header (lines 7-11) claims to prove "OUR transport".
   **Check:** confirm that `runChaos` builds bare `new Y.Doc()` replicas and shuffles their updates by hand. It never imports `Provider` or `YRooms`, so it can't catch step 5 of the trace.
4. **(Mid) Run locally: write the failing property test.** Follow `elirc/gitvg: folio/training/ladder/M1-offline-edits-never-arrive.md` (in-memory socket, ≥200 runs, 3 clients, edit/disconnect/reconnect/deliver steps).
   **Expected outcome (from the B05 report):** it fails on `main` on the first generated case, and the reference fix in `_answers/ladder-M1.md` passes 200/200.
5. **(Mid→senior) Design the backward-compatible fix.** **Check:** your design (a) sends only the delta, (b) handles an old client that never answers a server `sync1` (it already does: `provider.ts:55-56` replies to any `sync1`, so verify that and say why it matters), and (c) says what happens to users whose lost edits are still in IndexedDB.
   Compare it with incident 004's naive full-state fix and its 274 KB per-reconnect cost.

## Verified senior findings (folio @ `b81e960`)

- **Version restore is a no-op, and its test can't notice.** `elirc/folio: packages/collab/src/history.ts:60-66`, `restoreAsUpdate`, returns `Y.encodeStateAsUpdate(oldDoc, currentSv)`. The current doc already contains every item the old snapshot has (deleted ones survive as tombstones), so that diff is empty. B05 measured 2 bytes.
  The web applies it with origin `"remote"` (`apps/web/src/editor/ProseMirrorView.tsx:49`), which the provider never relays (`provider.ts:70`). The test at `history.test.ts:80-96` asserts only that two replicas are **equal** (`:96`), not that the content went back.
  Lesson: "converged" is not "correct". A CRDT test needs a content oracle.
- **Authorship check rejects every pure deletion, and it isn't called anyway.** `elirc/folio: packages/collab/src/security.ts:41-50` (`updateClientIds`) collects client ids only from `structs`. A delete-only update has no structs (just a delete set), so `verifyUpdateAuthorship` (`:57-62`) hits `clients.size === 0` → `false`.
  A grep of non-test files shows no caller of `verifyUpdateAuthorship` or `safeApplyUpdate`, and `setCanEdit` (`yroom.ts:96`) is mentioned only in a comment at `ws.ts:43`. In addition, `ws.ts:51` grants edit (`: true`) when no `member` is on the URL, and the web's `WS_URL` (`apps/web/src/lib/api.ts:4`) is `.../ws` with no member.
  "Hardening" that exists as exported functions is not hardening. Grep for callers.

## Debugging scenario: "my second tab's edits vanish"

This scenario uses `elirc/gitvg: folio/training/incidents/002-second-tab-edits-vanish.md`. The bug branch `7cfb4ff` is local-only, so read the diff from the brief.
- **Symptom:** single-tab users are fine. A user with two tabs open sees that tab 2's text never reaches anyone. No errors anywhere.
- **First clue, from the triage log in the brief:** `socket=s-18 … handled=ok room_update_emitted=false relayed_to=0`. The server accepted the update, but the room doc emitted **no** update. In other words, Yjs treated it as already known.
- **Hypothesis:** the suspect PR sets `ydoc.clientID = clientIdForUser(user.id)` (an FNV hash of the user id). Two tabs of one user now share a client ID. Each tab numbers its own items from clock 0 under that same `(client, clock)` identity, so the server sees tab 2's items as duplicates of tab 1's and drops them. This is rule 2 ("Identity") above.
- **Confirm (run locally, on the incident branch if you have it):** give two `Y.Doc`s the same `clientID`, insert different text in each, and sync both to a third doc. One tab's text is missing, and the replicas still "converge" without it (that's what the B05 probe recorded).
- **Fix direction:** keep `clientID` random per session (Yjs's default). Bind authorship server-side to the authenticated socket instead of the payload, and set `clientID` before any IndexedDB load.
  The sealed answer is `folio/training/_answers/incident-002.md`.

**Honesty cap:** every number on this page (200/200, 576→1,512 KB, 274 KB, 0.4→5–7 s) is from B05 laptop probes on 2026-09-24. None were re-run on 2026-10-06; this pass only re-read code at the SHAs above. No browser or e2e run was ever done for folio, and incident 005's browser path is inferred.
