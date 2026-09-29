# 11 — Accessibility that actually works (live regions, keyboard, focus)

Automated tools (axe) catch about a third of real problems: contrast, missing names, target size. The rest need a keyboard and a screen reader.

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
  - `training/ladder/M3`: axe + keyboard + screen-reader audit. The baseline is 13–14 contrast failures, target-size failures on map markers, and 116 Tabs to reach "Export JSON".
  - The Undo toast disappears after 3.5 s with no pause.
- Outline: a missing `aria-label` on a `NudeButton` (`Collaborators.tsx:167`), in `training/navigation/02-upstream-contribution-kit.md` (a candidate first upstream PR).
- perch: the existing sprint-14 a11y audit (`docs/`), for reading.

Interview framing: "I test with the keyboard and a screen reader, not just axe. Here's a live-region bug axe can't see."
