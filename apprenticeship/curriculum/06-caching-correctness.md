# 06 — Caching correctness: the four ways a cache lies

A cache is a second copy of the truth with a delay. Every cache bug is one of these four:

| Failure | Mechanism | Defense |
|---|---|---|
| **Stale forever** | The invalidation key doesn't match the read key (e.g. tagged by `handle`, invalidated by `id`), or a write path forgets to invalidate | derive read and invalidate keys from ONE function; test "write → read returns new value" |
| **Stampede** | A hot key expires and N requests recompute at once | single-flight/request coalescing, stale-while-revalidate, jittered TTLs |
| **Wrong audience** | Per-user or per-tenant data stored under a shared key | put every input that changes the output into the key (tenant, user segment, locale); never cache personalized responses at a shared layer |
| **Silent degradation** | Background refresh fails and the error is swallowed; unbounded in-memory caches grow until OOM | log and count refresh failures; set an eviction bound (size/LRU); alert on hit-rate collapse |

**Review questions:** What is the source of truth? Which inputs change the output, and are they all in the key? Which write paths must invalidate? What is the worst-case staleness, and is it acceptable to the business? What happens when the cache is down?

**Where these repos live now** (checked 2026-10-06): the old Desktop folders are gone.
- bazaar and pulse: code **and** `training/` are in the monorepo **elirc/gitvg** (`bazaar/`, `pulse/`, HEAD `af91bab`). The standalone repos elirc/bazaar (HEAD `5dc2dd6`) and elirc/pulse (HEAD `0b6d520`) have byte-identical copies of every file cited below, but no `training/` folder.
- netintercom → **elirc/dotnet-intercom** (HEAD `74e0a28`).
- The bazaar incident **branches** (`training/incidents/001-…`, `002-…`) were never pushed to any GitHub repo. Only the briefs and sealed answers are on GitHub, so you have to recreate the buggy code yourself from the brief.

**Worked examples in your repos**
- **bazaar** (`elirc/gitvg: bazaar/`):
  - `training/incidents/001-storefront-cache-tag-mismatch` (stale forever)
  - `training/incidents/002-personalized-price-shared-cache-key` (wrong audience)
  - `packages/cache/src/index.ts`: SingleFlight/SWR done right, but it was never wired into any app, and it swallows background-refresh errors. Still true at HEAD `af91bab`: a repo-wide grep for `@bazaar/cache`, `TaggedCache` and `SingleFlight` outside `packages/cache/` finds only its own `package.json` and `docs/curriculum/sprint-06.md`.
- **pulse** (`elirc/gitvg: pulse/`): TTL-only caches with no size bound and no sweep of expired entries in `apps/consumer/src/identity.ts:44` and `packages/auth/src/resolver.ts:53` (review findings; both line numbers still match at HEAD).
- **netintercom** (`elirc/dotnet-intercom`): client-side cache invalidation with React Query lives in `training/ladder/M5-cache-routing-rules.md` (added in B08), **not** `M1` as this page said at B02. M1 is the inbox query at scale. M5's "Explain before touching" links back to this page.

Interview framing: "caching is a consistency decision, not a performance tweak." Name the staleness bound and the invalidation owner.

## Worked trace: the bazaar cache library, line by line

All references are to `elirc/gitvg: bazaar/` at `af91bab`.

**1. The read path.**
- `ReadThroughCache.read` (`packages/cache/src/index.ts:16-26`) does the classic get → miss → `load()` → `set` sequence.
- `TaggedCache.read` (`:65-69`) wraps it, and **only after** the value comes back does it call `tags.attach(key, entryTags)` (`:67`).
- A tag is a string built by `entityTag(resource, id)` (`:153-155`), which returns `` `${resource}:${id}` ``. The function accepts any string as the id.

**2. The invalidate path.**
- `TaggedCache.invalidate` (`:71-82`) asks the tag index for every key under each tag, deletes those keys, and records `metrics.record("invalidation", keys.size)` (`:80`).
- If no key carries that tag, `keys.size` is 0 and the call still returns successfully. No error is thrown and nothing is logged.

**3. Who calls invalidate.**
- `CatalogPublisher.productPublished` (`apps/api/src/catalog-publisher.ts:8-14`) invalidates `` `product:${productId}` `` (`:10`), then revalidates the path `/products/${handle}` (`:13`).
- So the write side speaks in **product ids**. Anything on the read side that tags by **handle** builds a different string, and the invalidation becomes a no-op. That is the exact shape of incident 001: "the publisher *did* fire at 14:03:11Z with no thrown error".
- At HEAD, nothing implements the `StorefrontRevalidator` interface (`catalog-publisher.ts:1-4`). A grep for `invalidateTags` finds only this file.

**4. What the storefront actually does today.**
- `apps/storefront/app/products/[handle]/page.tsx:11` sets `export const revalidate = 60`, which is Next.js ISR with a documented 60-second tolerance (comment at `:9-10`).
- The catalog is a hard-coded array (`:14-21`). The live storefront's staleness bound is therefore the ISR timer, not the tag cache.

**5. The policy table.**
- `packages/cache/src/policy.ts:3-10` gives `product` 300 s, `collection` 120 s and `search` 30 s, and deliberately turns caching **off** for `admin` (`:7-9`: "consistency-sensitive"). That bypass is why the merchant in incident 001 sees the right price while shoppers don't.

### The failure mode, step by step (stale forever)
1. A shopper reads `canvas-market-tote`. The read path stores the value under `bazaar:v1:store:s1:product:canvas-market-tote` and attaches tag `product:canvas-market-tote`.
2. The merchant edits the price. `productPublished("p_…", "canvas-market-tote")` invalidates tag `product:p_…`.
3. `keysFor("product:p_…")` returns `[]` (`index.ts:52`). Nothing is deleted, and `CacheMetrics` adds 0 invalidations.
4. Every warm process keeps serving the old price. A freshly started pod has an empty `Map`, so it shows the right price. That matches the brief's "cold process is correct" clue.

## Two senior findings (verified in the code, not in the incident briefs)

**A. The in-memory store ignores its TTL.**
- `InMemoryCacheStore.set` (`index.ts:33`) is declared `async set<T>(key: string, value: T)`. It drops the `ttlSeconds` argument and never expires anything.
- The incident 001 brief reasons that "22 minutes is 8x [the 300 s] TTL… a plain TTL expiry would have self-healed". That reasoning holds only if the backing store honors TTLs. If the in-memory store is the one wired, a mismatched tag means stale **until restart**, and the `Map` grows without bound.
- So the same line is also a "silent degradation" bug: it makes the cache unbounded.
- The existing test `"loads once across sequential reads"` (`index.test.ts:17-23`) passes either way, because it never advances a clock.

**B. Invalidate can lose a race with a slow load.**
- In `TaggedCache.read`, the tag is attached **after** the load finishes (`:66-67`). Picture this sequence:
  1. Request A misses and starts loading the old price.
  2. The merchant saves, and `invalidate` runs. `keysFor` finds nothing yet, because A hasn't attached its tag.
  3. A finishes, stores the old price (`:24`) and attaches the tag.
- The invalidation happened, and the stale value survives it anyway. Standard defenses:
  - version-stamp entries and reject writes older than the last invalidation;
  - delete again after a short delay ("double delete");
  - attach tags before loading.
- No test in `index.test.ts` covers concurrent invalidate + load.

**Also: background refresh errors are swallowed.** `StaleWhileRevalidateCache.read` (`:135-138`) fires `void this.singleFlight.run(key, refresh).catch(() => undefined)` (`:136`). If the origin is down, readers keep getting stale data until `staleUntil`. Then they block on a load that fails, and nothing ever counted the failures.

**Second senior example (pulse, wrong-scope invalidation):**
- `IdentityResolver.identify` (`pulse/apps/consumer/src/identity.ts:100-119`) merges two persons and then re-primes the cache for the moved ids (`:116`, via `prime` at `:137-139`).
- The cache is a per-process `Map` (`:44`) with a 60 s default TTL (`:53`).
- If you run more than one consumer, every *other* process keeps mapping the moved `distinctId` to the **deleted** loser for up to 60 s. That's the "events mis-attribute for the TTL window" that the header comment (`:9-10`) warns about, now across processes. A local invalidation is only correct when the cache is local to the only writer.
- `CachedKeyResolver` (`pulse/packages/auth/src/resolver.ts:52-97`) is honest about the same trade-off: its TTL comment at `:38` calls the TTL "the maximum revocation lag ('undead key' window)". It does not cache unknown or revoked keys (`:84-85`), so its size is bounded by the number of live keys. The identity cache has no such bound.

## Goal + Check ladder

**Goal:** given any cache in your repos, name its key, its invalidation owner and its worst-case staleness, and prove "write → read returns the new value" with a test.

1. **Junior: read the key.** Open `bazaar/packages/cache/src/index.ts:149-155` and `policy.ts:12-15`. **Check:** you can say which three inputs make up a product key (store id, resource, id), and why `normalizedQueryKey` sorts the query params (so that `?a=1&b=2` and `?b=2&a=1` share one entry; see the test at `index.test.ts:83`).
2. **Junior: find the owner.** Grep for who calls `invalidate` / `invalidateTags`. **Check:** the only caller is `CatalogPublisher` (`catalog-publisher.ts:9`), and nothing implements `StorefrontRevalidator` at HEAD.
3. **Mid: reproduce incident 001 without the branch.** Write a vitest that reads through `TaggedCache` with tag `entityTag("product", handle)`, then invalidates `entityTag("product", id)`. *Run locally*: `pnpm --filter @bazaar/cache test`. **Expected:** `invalidate` returns `[]` and the second read does not call `load` again. Compare with the passing tag test at `index.test.ts:25-33`, which uses the same tag on both sides.
4. **Mid: fix the TTL.** Make `InMemoryCacheStore` store `expiresAt` and treat expired entries as misses. **Check:** a test with an injected clock shows a miss after `ttlSeconds`, and `"loads once across sequential reads"` still passes.
5. **Senior: the race and the fleet.** Write the interleaving test from finding B (use a deferred promise as `load`), and decide on a cross-process invalidation scheme for pulse's `IdentityResolver`. **Check:** your write-up names the staleness bound per replica, and compares that with what dotnet-intercom M5 asks for ("every replica routes by the new rule within a bound you choose").

## Debugging scenario: "the inbox refetches everything when Wi-Fi blips"

In dotnet-intercom, the inbox's React Query client sets `staleTime: 10_000` (`frontend/inbox/src/main.tsx:10`). Each hub event invalidates a precise key (`frontend/inbox/src/pages/Inbox.tsx:40-52`). On reconnect, though, `conn.onreconnected` calls `queryClient.invalidateQueries()` **with no filter** (`:73-76`). Every cached query in the app refetches at once.

**Symptom:** after a network blip, the browser's network tab shows a burst of requests. On a big support team, the API sees a request spike after every load-balancer idle timeout.

**Diagnosis:**
1. This is a stampede created by over-invalidation, not a cache that lies. The data is correct; the cost is the problem.
2. Correctness actually *depends* on this refetch. Messages missed while disconnected only arrive through it (rule 1 of [08](08-realtime-fanout.md)), and the 30 s `refetchInterval` on the conversation list (`:32`) is the safety net.

**Fix shape:** narrow the reconnect invalidation to the queries that can miss events (`["conversations"]`, `["messages", openId]`) and jitter it, instead of removing it. Before shipping, answer M5's question 5 in `training/ladder/M5-cache-routing-rules.md`.
