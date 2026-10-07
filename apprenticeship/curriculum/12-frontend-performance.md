# 12 — Measuring and fixing frontend performance honestly

**Measure first, on a production build, with the CPU throttled** (4× is a reasonable mid-range phone). Dev builds and a fast laptop lie.

**Where these repos live now (checked 2026-10-06):** lucasrouter → `elirc/lucasrouter` (`main` @ `b67127f`; incident branches not on GitHub) · perch → `elirc/perch` (`main` @ `94fdb3a`; incident branch not on GitHub) · gitjira-app → `elirc/gitjira` (`main` @ `42abd2c`; incident branches not on GitHub).

| Metric | What it catches | How to see it |
|---|---|---|
| **LCP** | slow first meaningful paint (big JS, late images, blocking CSS) | Lighthouse/Web Vitals, performance panel |
| **INP** | slow reaction to clicks/typing (long tasks, re-render storms) | Web Vitals `onINP`, long-task count while interacting |
| **CLS** | content jumping (late-inserted banners, no reserved space) | Web Vitals `onCLS`, layout-shift regions |
| **JS bytes before interactive** | bundle bloat, bad code-splitting | build output, per-route budgets; watch for prefetch inflating numbers |

**Common causes → fixes**
- **Re-render storm:** state held too high, or a store selector returning new objects. Fix it by moving state down, using narrower selectors and memoization. **Measure again**, because the "obvious" fix often changes nothing (see below).
- **Work on every keystroke:** a debounce that doesn't coalesce, or heavy highlighting or filtering per keypress. Fix with a correct debounce or `useDeferredValue`, and do less work per key.
- **Heavy library in the first-load path** (maps, charts, editors): dynamic `import()` behind interaction, plus a per-route JS budget that fails CI.
- **Layout shift:** reserve space for async UI (skeletons, fixed-height status strips).

**Worked examples in your repos** (all numbers below come from one Windows laptop on 2026-09-24, as recorded in `batch3report/projects/lucasrouter.md` and the training briefs. Compare deltas within a session, never the absolute values.)
- lucasrouter (main lab; `training/tools/frontend-probe.mjs` measures all of the above):
  - INC-001: hydration-critical JS on `/` rises 591 → 619 KB raw (184 → 194 KB gzip). Total JS fetched moved only +6 KB.
  - INC-004: long tasks while typing go from 0–1 to 20–21, taking 1.4–1.9 s (4× CPU, 25 keystrokes, 3 runs).
  - INC-005: `/dispatch` CLS goes 0 → 0.04.
  - M1: marker-click p75 is 224–240 ms at 1×, or about 1.06–1.46 s at 4× CPU. **The obvious selector fix measured as no change**, and that is the lesson.
  - M4: per-route budgets.
- perch: `training/incidents/001-search-debounce-timer-leak` (the debounce never coalesces; the brief's gateway alert shows request rate up about 4×).
- gitjira-app: `training/ladder/M1-board-at-2000-issues.md` and `training/incidents/001-board-cpu-storm.md`.

Interview framing: give numbers, name the device and throttling conditions, and describe one fix that *didn't* work and how you knew.

---

## How the probe measures (read it before trusting it)

`elirc/lucasrouter: training/tools/frontend-probe.mjs` (267 lines) is the measuring instrument for every lucasrouter number above. Read these lines first:
- `:63` observes `longtask` entries. That is the "long tasks while typing" column in INC-004.
- `:69` observes `layout-shift`. That is CLS for INC-005.
- `:72` observes Event Timing with `durationThreshold: 16`. Events shorter than 16 ms are never reported. That is why INC-004 shows about 20 long tasks but only 1 slow keydown.
- `:77` applies `Emulation.setCPUThrottlingRate` when `--cpu` > 1 (the default is 4, `:36`).
- `:38` lets you run one check at a time (`--only=vitals,clicks,typing,toast,sheet`).

The M4 ladder adds the rule that makes these numbers useful: no number in a doc without the command that produced it and the machine it ran on.

## Worked trace: one keystroke in Stop search (lucasrouter `main` @ `b67127f`)

1. The input's `onChange` calls `setQuery`. That is **local** `useState` in `src/components/dispatch/StopSearch.tsx:10`, so only `StopSearch` re-renders urgently.
2. `StopSearch.tsx:12` derives `deferredQuery` with `useDeferredValue`. The filter `useMemo` at `:14-17` depends on the deferred value, so React can render the typed character first and the filtered list later, in an interruptible render.
3. `:27` marks the results `aria-busy` while the deferred value lags the typed one.
4. Nothing above `StopSearch` subscribes to the query. `DispatchScreen` subscribes to seven data slices plus three actions (`src/components/dispatch/DispatchScreen.tsx:64-73`), and the query is not one of them. The map is wrapped in `memo(MapView)` (`:27`), and each marker is `memo(StopMarkerImpl)` (`src/components/map/StopMarker.tsx:250`).

That is a healthy shape: the urgent state sits at the leaf, and the expensive consumers sit behind memo boundaries with stable props.

## Failure mode, step by step: INC-004 ("dim non-matching stops")

The diff is quoted in `training/incidents/004-search-highlight.md`, and the mechanism is in `training/_answers/incident-004.md`.

1. The PR moves `query` from `StopSearch`'s `useState` into the store (`searchQuery`), so the map can read it.
2. It subscribes **`DispatchScreen`** to `searchQuery` and passes `highlightQuery` down to the map.
3. Every keystroke now re-renders `DispatchScreen` and all its non-memoized children (the overview, the panel header, the panel and search results, the legend, the toast).
4. `MemoMapView` gets a new `highlightQuery` prop, so the memo misses. `MapViewInner` passes the string to all 45 `StopMarker`s, so every marker memo misses too. Each marker recomputes `dimmed`, and react-leaflet calls `setOpacity` on it.
5. Because the text now round-trips through an external store (`useSyncExternalStore` renders synchronously), `StopSearch`'s own `useDeferredValue` no longer isolates the work.
6. Result: 20–21 long tasks per 25 keystrokes at 4×, while Event Timing reports almost nothing (the 16 ms floor plus where the work lands). Each hunk of the diff looked tiny. The cost is in **where the subscription sits**, which no single hunk shows.

The chosen fix (option A in the sealed answer) keeps the query local, gives the map a deferred or derived value through a small wrapper, and passes a per-marker `dimmed` boolean so that only markers whose state flips re-render.

## Goal + **Check** ladder

1. **Goal (junior):** say which components re-render on a keystroke today. **Check:** read `StopSearch.tsx:9-17` and `DispatchScreen.tsx:64-73`, and confirm that `searchQuery` does not appear in the grep `grep -n "useAppStore" src/components/dispatch/DispatchScreen.tsx`.
2. **Goal (junior):** fix perch's debounce on paper. **Check:** the sealed answer (`elirc/perch: training/_answers/001-search-debounce-timer-leak.md`) shows the bug: `timer = setTimeout(...)` with no `clearTimeout(timer)`. Your fix adds that one line. Trace the test in your head: three calls inside the window must give `["ada"]`, not `["a","ad","ada"]`. (`apps/web/src/debounce.ts` exists only on the unpushed incident branch. Perch `main` has no debounce file.)
3. **Goal (junior → mid):** find gitjira-app's over-broad invalidation. **Check:** `elirc/gitjira: apps/web/src/lib/useLiveProject.js:20` calls `qc.invalidateQueries({ queryKey: ['projects'] })` on every socket `activity`, which refetches every project-scoped query. M1 asks you to scope it with `queryKeys.issues(key)` and prove the change with a Profiler render count.
4. **Goal (mid):** reproduce M1's "no change" result. **Check (run locally):** with `pnpm build && pnpm start` and `node training/tools/frontend-probe.mjs <url> --only=clicks --cpu=1`, run `main` twice and your change twice in the same session. Your conclusion must survive the recorded spread (±150–200 ms for clicks at 4×, B03 report).
5. **Goal (mid):** write M4's budget so it would catch INC-001. **Check:** the budget measures **hydration-critical** scripts per route (the ones referenced by the built HTML), not total fetched JS, and fails if the store appears in `/`'s critical set. Total JS moved only +6 KB in INC-001, so a total-bytes budget would have passed.

## Verified senior findings

- **The obvious fix didn't move the number.** `training/_answers/ladder-M1.md` records the scratch experiment: moving the selection subscription out of `DispatchScreen` gave p75 272/240 ms at 1× versus 240/224 ms on `main`, which is within noise. The answer says to keep the change only if the Profiler shows a real render saving, and never to claim a latency win. In this case Leaflet's popup and `autoPan` work is a candidate cost that React changes can't touch.
- **Docs mixed a page's own cost with prefetch.** The B03 report found that the per-route "JS KB" table in `docs/REBUILD.md` includes Next's idle `<Link>` prefetch of other routes. On `main` the landing page already downloads a 43 KB store + seed chunk at idle. M4's context gives the probe totals (609 / 802 / 904 KB for `/`, `/dispatch`, `/driver/D1`) and says they include that prefetch.

## Debugging scenario: "typing stutters, but INP looks fine"

(1) Run the probe with `--only=typing` on both builds in one session. Compare long-task count and time, not per-event durations. (2) Record a Performance trace while typing 5 characters at 4×. Click a long task and read its stack: React `performWorkUntilDeadline`/commit frames point at render cost, while Leaflet `setOpacity` or style recalculation points at the map. (3) Open the React Profiler with "why did this render". If `DispatchScreen` says "hook changed", look for a new `useAppStore` selector. (4) Fix, then re-measure in the same session. If the number doesn't move, say so.

**Honesty cap:** no Lighthouse runs and no real mobile hardware were used. The INC-004 sealed answer says no trace was saved; producing one is your job. All lucasrouter incident branches exist only in the original local clone, so reproducing them means re-applying each brief's quoted diff on a scratch branch (the training README's 2026-10-06 status note says the same).
