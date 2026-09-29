# 06 — Caching correctness: the four ways a cache lies

A cache is a second copy of the truth with a delay. Every cache bug is one of these four:

| Failure | Mechanism | Defense |
|---|---|---|
| **Stale forever** | The invalidation key doesn't match the read key (e.g. tagged by `handle`, invalidated by `id`), or a write path forgets to invalidate | derive read and invalidate keys from ONE function; test "write → read returns new value" |
| **Stampede** | A hot key expires and N requests recompute at once | single-flight/request coalescing, stale-while-revalidate, jittered TTLs |
| **Wrong audience** | Per-user or per-tenant data stored under a shared key | put every input that changes the output into the key (tenant, user segment, locale); never cache personalized responses at a shared layer |
| **Silent degradation** | Background refresh fails and the error is swallowed; unbounded in-memory caches grow until OOM | log and count refresh failures; set an eviction bound (size/LRU); alert on hit-rate collapse |

**Review questions:** What is the source of truth? Which inputs change the output, and are they all in the key? Which write paths must invalidate? What is the worst-case staleness, and is it acceptable to the business? What happens when the cache is down?

**Worked examples in your repos**
- **bazaar** (`gitvg\bazaar`):
  - `training/incidents/001-storefront-cache-tag-mismatch` (stale forever)
  - `training/incidents/002-personalized-price-shared-cache-key` (wrong audience)
  - `packages/cache/src/index.ts`: SingleFlight/SWR done right, but it was never wired into any app, and it swallows background-refresh errors.
- **pulse** (`gitvg\pulse`): unbounded TTL-only caches in `apps/consumer/src/identity.ts:44` and `packages/auth/src/resolver.ts:53` (review findings).
- **netintercom**: client-side cache invalidation with React Query (`training/ladder/M1`).

Interview framing: "caching is a consistency decision, not a performance tweak." Name the staleness bound and the invalidation owner.
