# 08 — Realtime fan-out (WebSockets / SignalR / Socket.IO) across instances

**Problem.** A socket lives in **one** process. With 2+ instances, an event handled on instance A never reaches clients connected to instance B,
unless a backplane (Redis adapter, Azure SignalR, Postgres LISTEN/NOTIFY) relays it.

**Rules**
1. **Delivery is at-most-once.** Sockets drop and reconnect. Clients must **catch up** on reconnect: refetch, or use `?after=<cursor>`. Treat realtime as a hint and the database as the truth.
2. **Group/room membership is per connection** and is lost on reconnect, so re-join on every (re)connect.
3. **Broadcast after commit**, never inside the transaction. Otherwise clients see data that then rolls back.
4. **Authorize the join**, not just the connection. Room names are guessable.
5. **Scale concerns:** sticky sessions (for long-polling fallback), a backplane, event volume per board, and heartbeats and idle timeouts behind load balancers.

**Where these repos live now** (checked 2026-10-06):
- gitjira-app → **elirc/gitjira** (HEAD `42abd2c`; app code plus `training/`).
- netintercom → **elirc/dotnet-intercom** (HEAD `74e0a28`).
- Neither repo's `training/incidents/*` branches were pushed. The briefs on `main` contain the suspect diffs, so you rebuild each branch from its brief.
- Bonus example: **elirc/astraspacegameweb** (HEAD `736b75f`) *does* have its incident branches on GitHub, including `training/incidents/003-second-tab-silent`, a run-verified realtime incident with a repro script at `training/ops/two-tabs.mjs`.

**Worked examples in your repos**
- gitjira-app (`elirc/gitjira`):
  - `training/incidents/005-live-board-goes-stale`: stops updating after about 15 minutes.
  - `training/incidents/001-board-cpu-storm`: join storm. At B02 this was run-verified: `join-project` fired 25× in 300 ms vs 1× at base.
  - `training/ladder/M4-live-board-across-instances.md`: Socket.IO across 2 machines.
  - Review: no adapter; only create/comment events are broadcast; the broadcast happens before commit. **All three are still true at HEAD.** See the trace below.
- netintercom (`elirc/dotnet-intercom`):
  - `training/incidents/001-widget-note-leak` (what a visitor group may receive) and `002-unassigned-queue-spike` (presence, which is per-connection state).
  - `training/ladder/M3-widget-reconnect-delivery.md` and `S1-scale-out-three-replicas.md`.
  - The widget never re-joins its SignalR group after a reconnect. Still true at HEAD: `frontend/widget/src/Widget.tsx:52-58`.

## Worked trace: one issue update in gitjira, from service to browser

All references are to `elirc/gitjira` at `42abd2c`.

**1. The write.**
- `updateIssue` opens `prisma.$transaction` (`apps/api/src/services/issue.service.js:210`). Inside it, each changed field calls `recordActivity(tx, …)` (`:218`, `:226`).
- `recordActivity` (`apps/api/src/services/activity.service.js:13-30`) inserts an `ActivityEvent` with `tx`, then, **still inside the transaction**, calls `emitToProject` (`:25-27`), but only **if `projectId` was passed**.

**2. Which events broadcast.** Only two call sites pass `projectId`:
- `issue.created` (`issue.service.js:74-80`)
- `comment.added` (`comment.service.js:40-45`)

`priority.changed` (`:218`), `assignee.changed` (`:226`) and `status.changed` (`:298`) don't pass it, so dragging a card between columns is never pushed to other viewers.

**3. The fan-out.**
- `emitToProject` does `io.to(\`project:${projectId}\`).emit(…)` (`apps/api/src/realtime/emit.js:8-12`).
- The server is `new Server(httpServer, { cors })` with **no adapter** (`apps/api/src/realtime/socket-server.js:15-17`). That's the default in-memory adapter, so the room only contains sockets connected to *this* process.
- `fly.toml:35` runs `min_machines_running = 2`. Two people on the same board, routed to different machines, don't see each other's changes.

**4. The join.**
- `join-project` checks `projectMember` before `socket.join` (`socket-server.js:44-54`). That's rule 4 done right.
- On the client, `useLiveProject` emits `join-project` **once per effect run** (`apps/web/src/lib/useLiveProject.js:24`). It has no `socket.on('connect', …)` handler, so after Socket.IO auto-reconnects (`socket.js:7`, "reconnection is on by default"), the new connection is in **no rooms**.

**5. The receive.** `onActivity` invalidates `['projects']` (`useLiveProject.js:18-21`). It's a hint, not a payload, and the refetch reads the truth. That's rule 1 done right.

### The failure mode, step by step (stale board)
1. A user loads the board. The socket connects with `auth: { token: getAccessToken() }`, captured **once** when the socket is created (`apps/web/src/lib/socket.js:12-15`).
2. The access token expires: `ACCESS_TTL = '15m'` (`apps/api/src/services/token.service.js:6`).
3. Any blip (a laptop sleeping, a deploy, a load-balancer idle timeout) triggers an auto-reconnect. The handshake still sends the **expired** token. The `io.use` guard rejects it (`socket-server.js:23-33`: "Invalid token"), and every retry fails the same way.
4. `reconnectSocket()` (`socket.js:20-26`) exists to hand the socket a fresh token, but a repo-wide grep finds **no caller**.
5. Even if the reconnect succeeds, step 4 of the trace applies: no re-join, so no events.
6. Presence goes stale too: `disconnect` only logs (`socket-server.js:61-63`) and never re-broadcasts `presence`. People who left stay listed until somebody else joins or leaves.

INC-005's symptoms ("stops updating about 15 minutes after load", "presence shows people who left") match this HEAD-level analysis. The incident's *planted* change lives only in the brief's diff, so compare the two before you decide which one is the root cause.

## Two senior findings (verified at HEAD)

**A. "Hint-only" doesn't make broadcast-before-commit safe.**
- The comment at `activity.service.js:18-24` argues that emitting inside the transaction is fine because clients only invalidate and refetch. That covers *rollback*. It misses the **race**:
  1. The emit leaves before `COMMIT`.
  2. A fast client refetches under read-committed and gets the **old** row.
  3. No second event ever comes, so the board shows stale data until something else changes.
- The fix is to emit after `$transaction` resolves (collect events in the service and emit them post-commit), or to emit from an outbox relay. See [01](01-transactional-outbox.md).

**B. netintercom's catch-up has a stale closure and a lost-update.**
- `conn.onreconnected` (`frontend/widget/src/Widget.tsx:52-58`) closes over `session.conversation` from the **bootstrap** effect (`:30`).
  - A visitor whose first message created the conversation *after* page load (`send()`, `:84-89`) has `session.conversation === null`, so reconnect catch-up does nothing for them.
  - For everyone else, `setMessages(latest)` (`:56`) **replaces** the list, so a push that arrived during the fetch can vanish.
  - The handler never calls `JoinConversation` again (`:61-63` only runs after the first `start()`).
- Server side, replies go only to group `vconv:{id}` (`src/NetIntercom.Api/Realtime/RealtimeNotifier.cs:20-27`), and group membership is added only in `JoinConversation` after an ownership check (`src/NetIntercom.Api/Realtime/VisitorHub.cs:37-46`). After a reconnect the visitor is silently off the list.
- `AddSignalR()` has no backplane (`src/NetIntercom.Api/Program.cs:37`), so S1's 3 replicas make this worse.
- These are exactly M3's "Explain before touching" Q1–Q3.

## Goal + Check ladder

**Goal:** for any realtime feature, answer "what does a client that was disconnected for 30 s, or connected to the other instance, see?", and prove the answer with a test.

1. **Junior: map the rooms.** List every `join`/`AddToGroupAsync` and every `emit`/`SendAsync` target in both repos. **Check:** gitjira has one room shape (`project:{id}`). The netintercom visitor hub has `visitors` (`VisitorHub.cs:31`) and `vconv:{id}` (`:45`). You can say which code path adds each one.
2. **Junior: which events broadcast.** Grep `recordActivity(` in `apps/api/src/services/`. **Check:** you find 5 call sites and exactly 2 that pass `projectId`.
3. **Mid: reproduce the lost room.** *Run locally* (`npm ci`, `docker compose up -d`, API + web), open a board in two browsers, restart the API, then move an issue's status from browser A. **Expected (derived from the code above):** browser B doesn't update until its own refetch. For an automated version, use a vitest with a fake socket, the pattern B02 used for INC-001 (it's in the *sealed* `training/_answers/incident-001.md`, so open it only after you've done INC-001), and assert that `join-project` is emitted again after a `connect` event.
4. **Mid: fix the widget (M3).** Re-join plus catch-up with `?after=<last CreatedAtUtc>` inside `onreconnected`, reading the conversation from a ref, not the closure. **Check:** your test fails on `Widget.tsx` at HEAD, and a message pushed during the catch-up fetch is not lost or duplicated (dedupe by id, as `addMessage` does at `:19-21`).
5. **Senior: two machines (gitjira M4 / netintercom S1).** Design the backplane, post-commit emit and presence store. **Check:** your doc states the delivery guarantee (at-most-once push + DB catch-up), what happens to presence when a node dies, and how a rolling deploy's mass reconnect is absorbed (jittered backoff, re-join cost: `join-project` does one DB read per join at `socket-server.js:45-47`).

## Debugging scenario: "the dot is green but nothing arrives"

astraspacegameweb INC-003 (branch **on GitHub**: `training/incidents/003-second-tab-silent`).
- **Symptom:** a player with two tabs. One tab stops receiving live hints while its "Connected" dot stays green. Updates arrive only through the 10 s `/api/state` poll.
- **Evidence:** the brief's `two-tabs.mjs` table shows the previous release giving 5/5 hints in both tabs with `warband_ws_connections` = 2. B03 run-verified the broken build: tab B got 0/5 hints, and the gauge read 1 while 2 sockets were open.

**How to work it, the same way for any fan-out bug:**
1. Count the **server's** view of connections (the gauge) against the **client's** view (open sockets). A mismatch means the server dropped or replaced a registration.
2. Find the data structure that maps user → connection(s) and check whether it is keyed per user or per connection.
3. Check whether "connected" in the UI means "socket open" or "subscribed and receiving".

Run it with `elirc/astraspacegameweb: training/ops/two-tabs.mjs` against `main` and the incident branch (*run locally*, using `training/ops/LAB0-BRING-UP.md`). Then write the regression test before you fix anything.
