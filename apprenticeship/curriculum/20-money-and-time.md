# 20 — Money and time in business code

Payroll, billing and scheduling bugs are rarely clever. They are the same two families, over and over.

**Money**
- Store money as **integer minor units** or an exact decimal type (`decimal(19,4)`, `Prisma.Decimal`, C# `decimal`). Never use binary floats.
- Round **once, at a defined point, with a defined mode** (banker's vs away-from-zero), and document it. Truncation (`(long)x`) silently under-reports.
- Decimal libraries in JS are objects. `Decimal(3) + 2` is **string concatenation** (`"32"`); use `.plus()`.
- Test with awkward inputs (0.005, 1/3, 999.995, negatives), not round numbers that hide rounding bugs.

**Time**
- An **instant** (a moment: `DateTimeOffset`, `timestamptz`, UTC) is not a **calendar date** (a business day in a zone: `DateOnly`, `date` + zone).
  Deadlines, start dates and payroll periods are *calendar dates in a specific zone*.
- Never derive "today" from the server's zone. Take a clock abstraction (`TimeProvider`/`IClock`) and the business zone explicitly. Never take "today" from the request body.
- Test at zone boundaries: just before and after midnight in the business zone, DST transitions, and a year boundary. One passing time of day proves nothing.

**Worked examples in your repos**
- **vg:**
  - `training/incidents/002-leave-pending-days-jump`: `Decimal + number` gives `"32"`.
  - `001-completed-run-no-payslips`: an un-awaited Prisma query that silently never runs.
  - Real findings: the year boundary uses the server's zone (live on this UTC-7 laptop); a future-dated raise stops pay; YTD counts unapproved runs.
- **globehire:**
  - `training/incidents/002-start-date-calendar`: wrong at 10:00 New York and 00:30 London summer time. The author's regression test used the one time of day that works.
  - Real finding: the employment-change endpoint takes `Today` from the request body.
- **netstripe:** `training/incidents/002-mrr-rounding-drift` (truncating cast in `Money.Multiply`).
- **atlas:** multi-currency payroll; real finding that approved unpaid leave is never deducted.
