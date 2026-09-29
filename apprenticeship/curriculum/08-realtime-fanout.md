# 08 — Realtime fan-out (WebSockets / SignalR / Socket.IO) across instances

**Problem.** A socket lives in **one** process. With 2+ instances, an event handled on instance A never reaches clients connected to instance B,
unless a backplane (Redis adapter, Azure SignalR, Postgres LISTEN/NOTIFY) relays it.

**Rules**
1. **Delivery is at-most-once.** Sockets drop and reconnect. Clients must **catch up** on reconnect: refetch, or use `?after=<cursor>`. Treat realtime as a hint and the database as the truth.
2. **Group/room membership is per connection** and is lost on reconnect, so re-join on every (re)connect.
3. **Broadcast after commit**, never inside the transaction. Otherwise clients see data that then rolls back.
4. **Authorize the join**, not just the connection. Room names are guessable.
5. **Scale concerns:** sticky sessions (for long-polling fallback), a backplane, event volume per board, and heartbeats and idle timeouts behind load balancers.

**Worked examples in your repos**
- gitjira-app:
  - `training/incidents/005-live-board-goes-stale`: stops updating after about 15 minutes.
  - `training/incidents/001-board-cpu-storm`: join storm.
  - `training/ladder/M4`: Socket.IO across 2 machines.
  - Review: no adapter; only create/comment events are broadcast; the broadcast happens before commit.
- netintercom:
  - `training/incidents/001`, `002`.
  - `training/ladder/M3`, `S1`.
  - The widget never re-joins its SignalR group after a reconnect.
