# 20 — Money and time in business code

Payroll, billing and scheduling bugs are rarely clever. They are the same two families, over and over.

**Where these repos live now (checked 2026-10-06):** vg → `elirc/vg` (HEAD `d87c0a6`); globehire → `elirc/globehire` (HEAD `d38fb14`);
netstripe → `elirc/dotnet-stripe` (HEAD `8f40257`); atlas → source in `elirc/atlas` (HEAD `19e8c2d`), but its `training/` tree is only in
the monorepo `elirc/gitvg` under `atlas/training/` (HEAD `af91bab`). Incident branches: globehire's and dotnet-stripe's are on GitHub;
**vg's two incident branches are not** (only the incident briefs and sealed answers on `main` are).

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
    **All three are still present at `elirc/vg` HEAD `d87c0a6`** (traced below).
- **globehire:**
  - `training/incidents/002-start-date-calendar`: wrong at 10:00 New York and 00:30 London summer time. The author's regression test used the one time of day that works.
  - Real finding: the employment-change endpoint takes `Today` from the request body. **Still present at `d38fb14`**
    (`elirc/globehire: src/GlobeHire.Api/EmploymentLifecycle/EmploymentLifecycleEndpoints.cs:18,30`).
- **netstripe:** `training/incidents/002-mrr-rounding-drift` (truncating cast in `Money.Multiply`).
- **atlas:** multi-currency payroll; real finding that approved unpaid leave is never deducted. **Still true at `elirc/atlas` `19e8c2d`**:
  `src/Atlas.Infrastructure/DependencyInjection.cs:105` registers `NoUnpaidLeaveCalendar`, whose `ApprovedUnpaidDaysAsync` returns
  `Task.FromResult(0)` (`src/Atlas.Infrastructure/Payroll/NoUnpaidLeaveCalendar.cs:16-20`). The fix is ladder rung
  `elirc/gitvg: atlas/training/ladder/J2-unpaid-leave-in-payroll.md`.

---

## Worked trace: one payroll calculation in vg, and three ways it lies

vg is a Next.js + Prisma (plain JS) payroll app. Money is stored correctly as `BigInt` minor units (`amountMinor BigInt`,
`elirc/vg: prisma/schema.prisma:471`), converted by `toMinorUnits`, which does `BigInt(Math.round(numeric * 100))`
(`elirc/vg: src/lib/money.js`). Storage is fine. The bugs are all in **which rows** and **which dates** feed the math.

**Step 1: which salary?** `loadCurrentCompensation` asks for the row with `isCurrent: true` **and** `effectiveDate <= periodEnd`
(`elirc/vg: src/services/payroll.service.js:86-99`).

**Step 2: how is a raise recorded?** `addCompensationRecord` finds the current row, sets `isCurrent: false` on it **immediately**
(`src/services/employee.service.js:341-348`), then creates the new row with `isCurrent: true` and whatever `effectiveDate` HR typed
(`:350-360`). Put steps 1 and 2 together: HR enters a March raise in January. The old row is no longer current, and the new row isn't
effective until March. **No row matches** for February, so the employee is unpayable. Neither file is wrong on its own. This is the
"cross-file reasoning" finding the sealed review (`training/_answers/review.md`, R5) calls the senior signal.

**Step 3: year-to-date.** `loadYtd` computes `const yearStart = new Date(periodStart.getFullYear(), 0, 1)`
(`src/services/payroll.service.js:102`). `getFullYear()` and the `Date(y, m, d)` constructor both use the **server's local zone**.
On a host west of UTC (this laptop is UTC-7), a period starting `2026-01-01T00:00Z` is still 31 Dec 2025 locally, so `yearStart`
becomes 1 Jan **2025** and January's YTD sums all of last year.

**Step 4: which runs count?** The same query filters `status: { in: ["APPROVED", "PAID", "CALCULATED"] }` (`:114-116`).
`CALCULATED` means "someone pressed calculate", not "this was paid". An abandoned test run inflates YTD.

**Step 5: why YTD matters.** `computeTaxForRule` handles a `WAGE_BASE_CAP` rule (e.g. Social Security) as
`remaining = Math.max(0, capMajor - ytdMajor)` and taxes `Math.min(taxableMajor, remaining) * rate` (`:66-71`). Inflate YTD (step 3
or step 4) and `remaining` hits 0: **the tax is silently under-withheld**, with no error anywhere.

Note also *where* the tax is computed: `toMajor` turns minor units into a JS `Number` (`:46-49`), the tax is multiplied out in
floating point, and only then converted back with `toMinorUnits` at `:73`. That is one rounding point with a defined mode
(`Math.round`, half-up for positives), which is acceptable, but it's float math in the middle of a money path. Be able to say why
that works for these magnitudes and when it would stop working.

## Failure mode, step by step: `Decimal + number` (vg INC-002)

Leave balances are *not* integers: `balanceDays`, `usedDays` and `pendingDays` are `Decimal @db.Decimal(10, 2)`
(`elirc/vg: prisma/schema.prisma:770-772`). On `main`, `leave.service.js` defends itself with
`function toDecimal(value) { return Number.parseFloat(String(value || 0)); }` (`src/services/leave.service.js:8-10`) and uses it on both
the availability check (`:163`) and the update (`:190`). The incident brief's PR #517 removes those calls as "dead weight":

1. Prisma returns a `Decimal` column as a **`Prisma.Decimal` object** (decimal.js), not a number. The PR comment says otherwise.
2. JS `+` on an object calls `valueOf()`, which for decimal.js returns a **string**. `Decimal(3) + 2` → `"3" + 2` → `"32"`.
3. Prisma happily accepts the string `"32"` for a Decimal column and stores `32.00`. No error, no log line.
4. The availability line uses `-`, which has no string meaning, so it coerces to numbers and **stays arithmetically correct**. The same
   refactor produced one correct line and one wrong line, which is why review missed it.
5. The next request compares against the corrupted 32: `20 - 32 = -12`, so every request now gets `400 Insufficient leave balance`
   (the brief's 1/day → 60/day error spike).
6. A user's *first* request looks right by accident (`"0" + 4` = `"04"` = 4). "It's the second one that breaks" is the clue.

The sealed answer (`training/_answers/incidents/002-leave-pending-days-jump.md`) records the mechanism as checked against the repo's own
`@prisma/client`: `Decimal(0)+3 === "03"`, `Decimal(3)+2 === "32"`, `Decimal("1.5")+1 === "1.51"`. I did not re-run that for this page
(no installs).

## Goal + Check ladder

**Goal:** given a money or date bug report, find the line where the *type* (object vs number, instant vs date) or the *zone* changed
without anyone deciding it should.

1. **(junior) Read the storage contract.** Open `elirc/vg: prisma/schema.prisma` and list every money field and every `Decimal` field.
   **Check:** money is `BigInt` with a `Minor` suffix (e.g. `:471`, `:596-598`); leave days, exchange rates and hours are `Decimal`
   (`:634`, `:677`, `:770-772`, `:816`). You should be able to say which ones Prisma hands back as objects.
2. **(junior) Predict a concatenation.** Without running anything, write Maya's and Omar's `pendingDays` from the INC-002 brief's SQL.
   **Check:** Maya 0 → 3 → 32; Omar 5 + 1 → 51. Your explanation must name `valueOf()` returning a string.
3. **(junior+) Find the time-of-day bug by reading.** In `elirc/globehire`, open `src/GlobeHire.Infrastructure/Time/SystemClock.cs`.
   **Check:** line 9 is `public DateOnly Today => DateOnly.FromDateTime(UtcNow.UtcDateTime);`, i.e. "today" is the **UTC** date.
   Then grep for `Today` and find the guards that use it: `WorkforcePlan.cs:77`, `Employment.cs:46`, `EmploymentUseCases.cs:21`.
4. **(mid) Hand-evaluate the bad fix.** In globehire INC-002 the PR's `TodayIn` does
   `TimeZoneInfo.ConvertTime(clock.UtcNow.UtcDateTime.Date, zone)`. Work out what it returns at 10:00 New York on 15 July, 21:30
   New York on 15 July, and 00:30 London on 16 July (BST). **Check:** 14 July ✗, 15 July ✓, 15 July ✗. Explain why `.Date` before
   `ConvertTime` converts *UTC midnight*, not *now*. Compare with the table in `training/_answers/incident-002-start-date-calendar.md`.
5. **(mid) Design the test table.** Write the instants you'd put in a table-driven test for "today in country X". **Check:** you have one
   just before and one at local midnight for a zone west of UTC, one between local and UTC midnight for a zone east of UTC, a winter
   case where the zone equals UTC, a DST-switch day, and an unconfigured country. The sealed answer has 8 such rows. Run locally
   (expected from hand-evaluating the branch's `TodayIn`: on `training/incidents/002-start-date-calendar` the 14:00Z-US, 04:00Z-US
   and 23:30Z-GB rows fail and the rest pass; with the sealed fix all pass).

## Verified senior findings

**1. Truncation that only ever errs one way (netstripe).** On `elirc/dotnet-stripe` `main`, `Money.Multiply` rounds then casts:
`decimal.Round(MinorUnits * multiplier, 0, MidpointRounding.AwayFromZero)` then `(long)minor`
(`src/Billing.Api/Domain/Money.cs:43-46`). On the incident branch `training/incidents/002-mrr-rounding-drift` (`bfce8de`) the Round is
deleted with the comment "the cast to long already truncates" (`Money.cs:45-48` on that branch). The dashboard computes an annual plan's
monthly contribution as `plan.BasePrice.Multiply(1m / 12m)` (`src/Billing.Api/Program.cs:270`). For a 299.00 plan: 29,900 × 1/12 =
2,491.67 minor units → truncated to 2,491, rounded to 2,492. **One cent low per annual customer, never high**, which is exactly the
"always in our favour... only moves when we sign an annual customer" pattern in the brief. Round numbers (monthly plans, 12-divisible
prices) agree under both modes, so the existing tests can't see it.

**2. The caller decides what "the past" means (globehire).** `POST /api/v1/clients/{clientId}/employment-changes/validate` builds an
`EmploymentChange` with `request.Today` (`EmploymentLifecycleEndpoints.cs:18`), and `Today` is a field of the request record (`:30`).
The server has an `IClock` (`src/GlobeHire.Application/Abstractions/IClock.cs:3-8`) and ignores it here. Any client can backdate a
salary or termination change by sending an old `today`. The fix is not "validate the field"; it's "delete the field and inject the clock".

## Debugging scenario: "January payslips show $0 Social Security for some employees"

You're on call for vg. Finance says January's run withheld no Social Security for a handful of employees in one org, and only in prod,
not on your laptop. Work it from the code, not from guesses:

1. **Where does SS come from?** The `WAGE_BASE_CAP` branch (`payroll.service.js:66-71`). Zero tax means `remaining` was 0, so
   `ytdMajor >= capMajor`. YTD is wrong, not the rate.
2. **Where does YTD come from?** `loadYtd` (`:101-128`). Two inputs: the date window (`:102`, `:109-112`) and the status filter (`:114-116`).
3. **Why only some employees?** Check for `CALCULATED`-but-never-approved runs earlier in the window. If someone calculated a test run
   for those employees, step 4 of the trace explains it.
4. **Why only prod?** If prod runs in a zone west of UTC (or your laptop and prod disagree), `new Date(periodStart.getFullYear(), 0, 1)`
   resolves to a different year. A `2026-01-01T00:00Z` period start is still 2025 locally, so the window starts 2025-01-01 and swallows
   last year's pay. The bug depends on where it's deployed. Print `process.env.TZ` and `new Date().getTimezoneOffset()` on both hosts.
5. **Fix both**, each with a failing test first: build `yearStart` with `Date.UTC(periodStart.getUTCFullYear(), 0, 1)` (or, better, from
   the org's payroll zone as an explicit input), and restrict YTD to `APPROVED`/`PAID`. Then decide, with finance, what to do about the
   already-issued January payslips; don't silently recompute them.

## Honesty caps

- The vg reference payroll characterization suite (`training/harness/`) has **never been seen passing**: at B07 (2026-09-24) Docker hung
  and the run timed out, so its expected totals were computed by hand (`batch7report/projects/vg.md`). Run `training/harness/README.md`
  before trusting it.
- vg's incident branches (`training/incidents/001-…`, `002-…`) are **not on GitHub** as of 2026-10-06 (`git ls-remote` shows no
  `training/*` refs on `elirc/vg`). The briefs and sealed answers on `main` describe the diffs; you can't check them out from the remote.
- The "live on this UTC-7 laptop" observation and the Decimal REPL results come from B07 runs, not from this revision; this page only
  re-verified them by reading code at the HEADs listed above.
- vg line numbers above are from HEAD `d87c0a6`. The sealed review was written against baseline `99bb8b2`; its cited ranges
  (`employee.service.js:331-360`, `payroll.service.js:86-99`, `:102`, `:114-116`) still match HEAD.
- The globehire test-table outcomes in Check 5 are hand-evaluated from the branch code, not from a run.
