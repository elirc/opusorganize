# 12 — Measuring and fixing frontend performance honestly

**Measure first, on a production build, with the CPU throttled** (4× is a reasonable mid-range phone). Dev builds and a fast laptop lie.

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

**Worked examples in your repos**
- lucasrouter (main lab; `training/tools/frontend-probe.mjs` measures all of the above):
  - INC-001: landing JS rises 591 → 619 KB raw.
  - INC-004: stop-search long tasks go from 0–1 to about 20, taking 1.4–1.9 s.
  - INC-005: CLS goes 0 → 0.04.
  - M1: marker-click INP is 224–240 ms, or 1.06–1.46 s at 4× CPU. **The obvious selector fix measured as no change**, and that is the lesson.
  - M4: per-route budgets.
- perch: `training/incidents/001-search-debounce-timer-leak` (the debounce never coalesces; about 4× API calls).
- gitjira-app: `training/ladder/M1` (board at 2,000 issues) and `training/incidents/001-board-cpu-storm`.

Interview framing: give numbers, name the device and throttling conditions, and describe one fix that *didn't* work and how you knew.
