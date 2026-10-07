# 11 — Accessibility that actually works (live regions, keyboard, focus)

Automated tools (axe) catch about a third of real problems: contrast, missing names, target size. The rest need a keyboard and a screen reader.

**Where these repos live now (checked 2026-10-06):** lucasrouter → `elirc/lucasrouter` (`main` @ `b67127f`; the five `training/incidents/*` branches were never pushed, so GitHub has only `main`) · Outline → `elirc/masteroutline` (`outline/training/`, `main` @ `3409d2b`) · perch → `elirc/perch` (`main` @ `94fdb3a`).

**Five checks you do on every UI change**
1. **Keyboard only:** can you reach and operate everything with Tab/Shift+Tab/Enter/Space/Escape, in a sensible order? Count the Tab presses to the main action.
2. **Modals and sheets:** focus moves in when opened, is **trapped** while open, **Escape closes**, and focus **returns to the trigger** on close. Mark the background `inert`/`aria-modal`.
3. **Live regions:** the `aria-live` container must **exist in the DOM before** its text changes. Mounting the region together with its message is often not announced. Use `polite` for status and `assertive` only for errors.
4. **Names:** every icon button has an accessible name (`aria-label`); form inputs have `<label>`s; errors are linked with `aria-describedby`.
5. **Visual:** contrast is at least 4.5:1 (text) and 3:1 (UI); targets are at least 24×24 px; nothing conveys meaning by colour alone; timed messages can be paused (WCAG 2.2.1).

**Worked examples in your repos**
- lucasrouter (the main lab):
  - `training/incidents/002-toast-announcements`: the live region is no longer present before the message.
  - `training/incidents/003-driver-sheet-keyboard`: no Escape, no focus return, not modal.
  - `training/ladder/M3`: axe + keyboard + screen-reader audit. The baseline (measured 2026-09-24, recorded in `training/_answers/ladder-M3.md`) is 13–14 contrast failures on the landing page, target-size failures (×13–19) on map markers, and 116 Tabs to reach "Export JSON".
  - The Undo toast disappears after 3.5 s with no pause (`elirc/lucasrouter: src/components/ui/Toast.tsx:9`, `AUTO_DISMISS_MS = 3500`). Since B08 this is its own junior ticket, `training/ladder/J4-actionable-toast-timing.md`.
- Outline: a missing `aria-label` on a `NudeButton` (`elirc/masteroutline: outline/app/components/Collaborators.tsx:167`, re-checked at `3409d2b`), in `outline/training/navigation/02-upstream-contribution-kit.md` ("Candidate A"; a candidate first upstream PR).
- perch: the existing sprint-14 a11y audit (`elirc/perch: docs/accessibility/sprint-14-audit.md`), for reading. Note that it marks "Async announcements" as Pass from roles alone. After this page you should be able to say why a role is not proof.

Interview framing: "I test with the keyboard and a screen reader, not just axe. Here's a live-region bug axe can't see."

---

## Worked trace: the toast that must announce (lucasrouter)

Everything below was read at `elirc/lucasrouter` `main` @ `b67127f`.

1. **The store sets a toast.** Components call `showToast(...)` on the zustand store. `Toast` subscribes with `useAppStore((s) => s.toast)` (`src/components/ui/Toast.tsx:47`).
2. **The live region is the outer container, and it is always mounted.** `Toast.tsx:74-78` renders a `<div role="status" aria-live="polite" aria-atomic="true">` on every render, even when there is nothing to show. The card with the text is a *child* rendered only when `shown` is set (`Toast.tsx:82-121`).
3. **Why that order matters.** A screen reader watches a live region for *changes*. When the empty container is already in the accessibility tree and a card is inserted into it, that is a change inside a known region, so it is announced. When the region and its text appear in the same DOM mutation, many browser and screen-reader pairs never registered the region, so there is nothing to diff against. The B03 report notes this was inferred from live-region semantics plus a DOM check (`regionExistedBefore`); it was **not** tested with NVDA or VoiceOver.
4. **The action lives inside the region.** The "Undo" button (`Toast.tsx:99-109`) is a real `<button>` inside the live region, so the announcement includes it. It dismisses before it runs (`Toast.tsx:101-104`), so it can't fire twice.
5. **The timer.** `useEffect` at `Toast.tsx:60-67` dismisses after `AUTO_DISMISS_MS` (3,500 ms). Nothing pauses it on hover or focus. That is the WCAG 2.2.1 finding that J4 turns into a ticket.
6. **The probe checks the order, not the speech.** `training/tools/frontend-probe.mjs:223` records `regionExistedBefore` (was the region in the DOM before the message?) and `visibleMs` (how long the text stayed). It is a proxy for "will a screen reader speak it", which is why the incident brief still asks you to confirm by ear.

The same file shows the second pattern you need, modality. `src/components/driver/DriverDialog.tsx:114` calls `dialog.showModal()`. That one call gives you the top layer, an inert background and native focus containment (the comment at `:113` says exactly this). Escape arrives as a `cancel` event, handled at `:130-133`. Focus goes into the sheet on the next frame (`:122-124`), and the cleanup returns it to the opener if that element still exists (`:168-170`).

## Failure mode, step by step: INC-002 (live region mounted with its text)

The suspect diff is quoted in full in `training/incidents/002-toast-announcements.md`, so you can study it even though the branch is not on GitHub.

1. A refactor adds `if (!shown) return null;` before the outer `<div>`, and moves `role="status" aria-live="polite" aria-atomic="true"` from the container onto the keyed card.
2. While idle, nothing renders. There is no region in the accessibility tree.
3. A move triggers `showToast`. In one commit React inserts the container *and* the card that carries the role. The region is born holding its message.
4. axe sees a valid `role="status"` and reports nothing. Lighthouse stays at 96. The smoke run clicks with a mouse and looks for visible text. All green (the brief quotes all three).
5. The probe flips `regionExistedBefore` from `true` on `main` to `false` on the branch (B03 report, measured on production builds).
6. An NVDA user hears nothing after moving a stop. They tab through the route list to check that it happened.

The fix is to keep the region persistent and change only its children, and to add a component test that fails on the branch (J2's DOM test project). Then search for the same pattern. One copy is still on `main`: `src/components/dispatch/StopSearch.tsx:27-28` renders `<p role="status">N stops found</p>` *inside* the `filtering ? … : children` branch, so the region mounts with its first count. The M3 sealed answer lists it as finding #3.

INC-003 is the modality version. The brief quotes a one-line change from `dialog.showModal()` to `dialog.show()`, made to keep the Undo toast above the sheet. With `show()` you lose the top layer, the inert background and the native Escape-to-`cancel` path. The probe's `{closedByEscape, focusReturned, modal}` went from true/true/true to false/false/false (B03 report). The probe reads `:modal` at `frontend-probe.mjs:252` and `closedByEscape` at `:256`.

## Goal + **Check** ladder

Every Check is a read or grep you can do on a fresh clone of `elirc/lucasrouter`. Steps marked "run locally" need `pnpm install` and a production build on your machine.

1. **Goal (junior):** list every announcing region in the app. **Check:** `grep -rn 'aria-live\|role="status"\|role="alert"' src` returns about 15 hits, including `Toast.tsx:75`, `StopSearch.tsx:28`, `PanelHeader.tsx:70` and `:90`, and `DriverHeader.tsx:50`. For each hit, write down whether the element is rendered unconditionally. Compare your list with the M3 sealed answer, "Explain-before-touching" #2.
2. **Goal (junior):** explain what `showModal()` gives you that `show()` doesn't. **Check:** read `DriverDialog.tsx:108-172` and name the four things the comments attribute to the native modal: top layer, inert background, focus containment, and Escape via `cancel`. Then map each one to a driver report in `training/incidents/003-driver-sheet-keyboard.md`.
3. **Goal (junior → mid):** fix the StopSearch count so it is announced. **Check:** your diff keeps one `role="status"` element mounted whether or not `filtering` is true, and changes only its text. Run locally: a Testing Library test that types a query and asserts the status node is the *same* node before and after (`toBe`, not just matching text).
4. **Goal (mid):** do J4, which pauses the Undo countdown on focus or hover and gives actionable toasts at least 10 s. **Check:** the four fake-timer tests in the J4 definition of done pass. `Toast.tsx:74-78` is still the outer region (J4's constraints forbid moving it).
5. **Goal (mid):** run the M3 audit yourself. **Check (run locally):** your axe numbers will differ from the recorded ones, because `home.css` has been edited since. Record the axe version, the viewport and the commit. A finding counts only with a WCAG criterion and a repro.

## Verified senior findings

- **The docs claim more than the code delivers.** DECISIONS #44 says landing a11y is 100. The M3 sealed answer measured 13–14 `color-contrast` failures after the rebuild (axe-core 4.10.2, 2026-09-24). A senior's reflex is to put a date and a commit on every quality claim.
- **Keyboard cost scales with data.** 116 Tab presses to reach "Export JSON": 46 marker tab stops (45 stops plus the depot), plus every route polyline, which is focusable and has no name (M3 sealed answer, findings #4 and #9). The fix is architectural: make the map a single tab stop and add a DOM "selected stop" panel. Adding labels alone doesn't fix it.

## Debugging scenario: "the screen reader went quiet, but every gate is green"

A user reports silence after an action. Don't start in the screen reader. (1) In DevTools → Accessibility, find the node with `role="status"` *before* you trigger the action. If it isn't there, you already have your answer. (2) If it is there, check whether the text is replaced inside it or whether a new keyed child appears and disappears too fast. On `main`, M2 measured the "Routes ready" toast visible for only 161–180 ms (training README, "Real bugs on `main`"). (3) Check `aria-atomic` and whether the change happens in the same frame as a focus move, because some readers drop one of the two. (4) Only then confirm by ear with NVDA or VoiceOver, and write down the versions.

**Honesty cap:** the screen-reader outcomes on this page are inferred from DOM and live-region semantics plus the probe. None of the B03 runs used a real screen reader. The incident branches exist only in the original local clone, so reproducing them means re-applying the brief's quoted diff on a scratch branch.
