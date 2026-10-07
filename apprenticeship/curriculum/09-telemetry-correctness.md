# 09 — Telemetry you can trust (metrics, alerts, logs)

Observability fails in quiet ways: the dashboard is green because the signal is wrong.

| Failure | Example in your repos | Defense |
|---|---|---|
| **Wrong status or route label** | atlas: an anonymous 401 is recorded as 200 in the duration metric; errors lack `X-Correlation-Id` (`training/ladder/M4`) · gitjira-app: `route` is router-relative, so 4 endpoints share `route="/"` (`training/ladder/M2`) | record after the response is final; label by route *template*, never the raw path |
| **Cardinality explosion** | gitjira-app `training/incidents/004-dashboards-flatline`: about 504k series, a 55 MB scrape taking 5.6 s | never put ids, users or raw URLs in labels; cap and alert on series count |
| **Unreachable alert branch** | pulse `training/incidents/001-pipeline-health-severity-inversion`: reordered thresholds mean "critical" never fires | table-test every severity boundary; alert on the symptom (lag) and on the absence of data |
| **Logs as a liability** | atlas `training/incidents/005-payroll-day-log-cap`: the log cap was hit and salary data landed in the SIEM | structured logs with a redaction allow-list; sampling; budgets per level |
| **Claimed but not wired** | netintercom: OTel has no exporter · gitjira-app: queue metrics are documented but missing | verify end to end: emit, then scrape, then query, then alert fires in a drill |

**PromQL SLO traps** (all hit for real in astraspacegameweb during B03, 2026-09-24; reference rules in `training/_answers/ladder/M1-slo-rules.yaml` pass `promtool test rules`). How each trap was caught matters, because promtool did **not** catch all of them:
- **Clipped histograms.** If the top bucket is 60 s, p99 reads "60.0" forever once you're past it. Add buckets beyond your SLO. *Caught live in Lab 0:* the lag histogram's top bucket is `60` (`apps/server/src/metrics.ts:19`).
- **Label format.** Prometheus 3 stores `le="2"` as `"2.0"`, so a selector on `le="2"` silently matches nothing. *Caught live, not by promtool:* the fixtures shared the wrong assumption, so the tests passed (`training/_answers/agentic.md:8`).
- **Zero traffic.** Clamping the denominator (`clamp_min`) makes a ratio alert fire when there are no requests. Guard it with a traffic condition. *Caught by an idle promtool case* (`agentic.md:9`).
- **Silent SLI.** astraspacegameweb `training/incidents/002-lag-panel-flat`: lag p99 sits flat at 2.0 while the oldest event is 137 s old. Measure the *age of the oldest item*, not just a histogram.
- **Nobody receives the alert.** With no Alertmanager, the alert reaches no one. Also alert on "every target down". Still true at HEAD: `infra/prometheus.yaml` has `rule_files` but no `alerting:` block, and `infra/alerts.yaml` has 4 alerts and no `up == 0` rule.

**SLO basics:** pick a user-visible SLI (e.g. p95 latency or success rate of a route), set a target, alert on burn rate, and write the runbook entry *before* the alert exists.
Practice this in gitjira-app `training/ladder/M2` and `S3`.

**Where these repos live now** (checked 2026-10-06):

| Name in this page | GitHub repo | HEAD |
|---|---|---|
| atlas | code at **elirc/atlas** (`19e8c2d`); `training/` at **elirc/gitvg** `atlas/` | gitvg `af91bab` |
| pulse | **elirc/gitvg** `pulse/` (code + `training/`); elirc/pulse has the same code, no `training/` | `af91bab` |
| gitjira-app | **elirc/gitjira** | `42abd2c` |
| netintercom | **elirc/dotnet-intercom** | `74e0a28` |
| astraspacegameweb | **elirc/astraspacegameweb**, incident branches **pushed** | `736b75f` |

Only the astraspacegameweb incident branches exist on GitHub. For atlas, pulse and gitjira, rebuild the branch from the diff in each brief.

## Worked trace: why atlas records a 401 as a 200

All references are to `elirc/atlas` at `19e8c2d`.

**1. Pipeline order** (`src/Atlas.Api/Program.cs`):
- `UseExceptionHandler()` (`:10`) is the **outermost** layer.
- Inside it is `RequestTelemetryMiddleware` (`:15`), whose comment says it's placed "FIRST so every log line — including a 401… — carries the same correlation id" (`:13-14`).
- Inside that are `BearerAuthenticationMiddleware` (`:19`) and `IdempotencyMiddleware` (`:24`).

**2. The telemetry middleware** (`src/Atlas.Api/Observability/RequestTelemetryMiddleware.cs`):
- It sets `X-Correlation-Id` on the response up front (`:31`).
- It calls `next` inside `try` (`:37-40`), and in `finally` records `http.server.request.duration` with tags `method` and `status = http.Response.StatusCode` (`:41-54`). There is no route tag.

**3. The 401** is not written as a response. `BearerAuthenticationMiddleware` **throws** `UnauthenticatedException` (`src/Atlas.Api/Auth/BearerAuthenticationMiddleware.cs:37`, `:63`, `:67`, `:81`). `AtlasExceptionHandler` maps that exception to 401 (`src/Atlas.Api/Errors/AtlasExceptionHandler.cs:54-57`).

### The failure mode, step by step
1. An anonymous `GET /api/v1/payslips/{id}` enters the exception handler, then telemetry, then bearer auth.
2. Bearer auth throws. Nothing has set a status yet, so `Response.StatusCode` is still the default **200**.
3. The exception unwinds through telemetry's `finally`, which records `status="200"` along with the elapsed time.
4. Only then does the outer `UseExceptionHandler` catch the exception and write a 401 problem+json.

The same thing happens to **every thrown** 4xx/5xx: 403, 404 and 500 are all recorded as 200. An error-rate SLI built on this metric reads ~0% during an auth outage.

The correlation header has a matching problem. ASP.NET Core's exception handler clears the response, headers included, before it re-executes, so the header set at `:31` can be lost on error responses. M4's definition of done (item 1) makes you *prove* this with a capturing `IMetrics` in `AtlasApiFactory` before you change anything. Treat the header half as a prediction to test, not a given.

**The fix shape:**
- Record the status *after* the exception handler has run: move telemetry outside it, or register `Response.OnStarting`/`OnCompleted`.
- Re-add the header in the problem-details writer.
- Add a `route` tag from `RoutePattern.RawText`, with `"unmatched"` when there's no endpoint (M4 item 3).

## Two senior findings (verified at HEAD)

**A. atlas metrics are log lines, so they share the log cap.**
- `IMetrics` is bound to `LoggingMetrics` (`elirc/atlas: src/Atlas.Infrastructure/DependencyInjection.cs:122`), which writes every measurement with `logger.LogInformation("metric {Metric}={Value}{Unit} {@Tags}", …)` (`src/Atlas.Infrastructure/Observability/LoggingMetrics.cs:27-28`).
- INC-005's byte breakdown lists that exact template at 1.6% of bytes. When the workspace's daily cap is hit at 09:12, **the metrics stop too**: the incident that blinds the logs also blinds the dashboards.
- ADR-0018 promises a one-file swap to OpenTelemetry (M4's constraints quote this). Until that swap happens, "metrics" and "logs" are one failure domain.

**B. gitjira's route label is ambiguous, not explosive.**
- At HEAD the middleware is cardinality-safe: it uses `req.route?.path ?? (req.baseUrl || 'unmatched')` (`elirc/gitjira: apps/api/src/lib/metrics.js:41`).
- But `req.route.path` is **router-relative**. `issueRoutes.get('/')` (`apps/api/src/routes/issue.routes.js:23`), `projectRoutes.get('/')` (`project.routes.js:14`), `sprintRoutes.get('/')` (`sprint.routes.js:12`) and `healthRoutes.get('/')` (`health.routes.js:7`) all report `route="/"`.
- Health checks run every 15 s (`fly.toml:37-40`) and land in the same series as the board load. That pulls p95 *down* and hides a slow board.
- M2's context paragraph states this; verify it yourself from the four route files.
- INC-004 is the opposite mistake: "fix" the ambiguity with the raw path, and you get 504k series.

**Also verified (pulse):**
- At HEAD, `assessPipeline` checks `lagCrit` before `lagWarn` (`elirc/gitvg: pulse/packages/shared/src/pipeline-health.ts:56-62`), and the boundary test exists (`pipeline-health.test.ts:12-14`). INC-001's branch reorders this.
- netintercom's OTel is tracing-only with **no exporter**: `AddOpenTelemetry().ConfigureResource(…).WithTracing(t => t.AddAspNetCoreInstrumentation())` (`elirc/dotnet-intercom: src/NetIntercom.Api/Program.cs:128-130`).
- gitjira's queue metrics are still missing: `apps/api/src/lib/metrics.js` defines only `http_requests_total` and `http_request_duration_seconds` plus Node defaults, while `docs/RUNBOOK.md:47` tells on-call to check "the queue-depth gauge". That gap is ladder J3.

## Goal + Check ladder

**Goal:** for any metric or alert, state what it would show during the failure it exists to catch, and prove it with a test or a drill.

1. **Junior: read a pipeline.** In atlas `Program.cs:10-24`, write the middleware order outermost-first. **Check:** you can say what `Response.StatusCode` is when telemetry's `finally` runs for a thrown 404 (answer: 200, per the trace above).
2. **Junior: list the labels.** For gitjira `metrics.js:16-31`, list each metric and label, then list four requests that end up in `route="/"`. **Check:** your list matches finding B.
3. **Mid: table-test a severity function.** Using `pipeline-health.ts:45-80`, write a table test with samples at `lagWarn-1`, `lagWarn`, `lagCrit-1`, `lagCrit` and `lagCrit+1`, for lag, DLQ and insert p95. *Run locally:* `pnpm --filter @pulse/shared test`. **Expected:** green at HEAD. Rebuild INC-001's reorder from its brief, and at least the `lagCrit` row turns red.
4. **Mid: atlas M4 spike test.** Capture `IMetrics` in `AtlasApiFactory` (`tests/Atlas.Api.Tests/Infrastructure/AtlasApiFactory.cs`), send an anonymous request and a missing-id request, and assert on `status` and the header. **Check:** write your prediction first. The test should fail at HEAD on the status assertion.
5. **Senior: SLO as code (astraspacegameweb M1).** Write the two SLOs, burn-rate alerts and a guard alert for "work that never commits". **Check:** `promtool test rules` has one must-fire case, one must-not-fire case and one **zero-traffic** case. Then a live drill, *run locally* with `training/ops/LAB0-BRING-UP.md`, confirms the selectors return series. Promtool alone missed `le="2.0"`.

## Debugging scenario: "the lag panel is flat at 2.0 and nothing is firing"

astraspacegameweb INC-002 (branch on GitHub: `training/incidents/002-lag-panel-flat`).
- **Symptom:** during a 150 arrivals/s peak, `lag_p99` = `lag_p50` = 2.0 on every sample, the `oldest_s` column climbs to 136.86, and `GET /api/v1/alerts` returns `{"alerts":[]}`.
- **The trap:** on-call reads "2 s, at the SLO line, under the 5 s page threshold".

**How to work it:**
1. A p50 that equals the p99 exactly is a histogram smell. A real distribution almost never does that.
2. Dump `sum(warband_event_lag_seconds_bucket) by (le)` (the brief already has the raw counters). B03 found 26,998 of 27,000 observations in `+Inf`. When almost everything sits past the top bucket, `histogram_quantile` stops measuring anything useful. Compare the branch's buckets with `main`'s `[0.01 … 60]` at `apps/server/src/metrics.ts:19`.
3. Ask what the SLI *can't* see. The lag metric is observed only for **committed** events (its help text, `metrics.ts:18`: "Delay between event due time and committed resolution"). A backlog that isn't committing yet is invisible to it, which is why M1 requires an age-of-oldest guard alert.

The lesson to take to an interview: "I don't trust a quantile until I've looked at the buckets, and I always pair a latency SLI with an age-of-oldest-work signal."
