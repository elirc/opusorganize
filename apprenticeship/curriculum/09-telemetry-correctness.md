# 09 — Telemetry you can trust (metrics, alerts, logs)

Observability fails in quiet ways: the dashboard is green because the signal is wrong.

| Failure | Example in your repos | Defense |
|---|---|---|
| **Wrong status or route label** | atlas: an anonymous 401 is recorded as 200 in the duration metric; errors lack `X-Correlation-Id` (`training/ladder/M4`) | record after the response is final; label by route *template*, never the raw path |
| **Cardinality explosion** | gitjira-app `training/incidents/004-dashboards-flatline`: about 504k series, a 55 MB scrape taking 5.6 s | never put ids, users or raw URLs in labels; cap and alert on series count |
| **Unreachable alert branch** | pulse `training/incidents/001-pipeline-health-severity-inversion`: reordered thresholds mean "critical" never fires | table-test every severity boundary; alert on the symptom (lag) and on the absence of data |
| **Logs as a liability** | atlas `training/incidents/005-payroll-day-log-cap`: the log cap was hit and salary data landed in the SIEM | structured logs with a redaction allow-list; sampling; budgets per level |
| **Claimed but not wired** | netintercom: OTel has no exporter · gitjira-app: queue metrics are documented but missing | verify end to end: emit, then scrape, then query, then alert fires in a drill |

**PromQL SLO traps** (all hit for real in astraspacegameweb `training/ladder/M1` and verified with `promtool test rules`):
- **Clipped histograms.** If the top bucket is 60 s, p99 reads "60.0" forever once you're past it. Add buckets beyond your SLO.
- **Label format.** Prometheus 3 stores `le="2"` as `"2.0"`, so a selector on `le="2"` silently matches nothing.
- **Zero traffic.** Clamping the denominator (`clamp_min`) makes a ratio alert fire when there are no requests. Guard it with a traffic condition.
- **Silent SLI.** astraspacegameweb `training/incidents/002-lag-panel-flat`: lag p99 sits flat at 2.0 while the oldest event is 137 s old. Measure the *age of the oldest item*, not just a histogram.
- **Nobody receives the alert.** With no Alertmanager, the alert reaches no one. Also alert on "every target down".

**SLO basics:** pick a user-visible SLI (e.g. p95 latency or success rate of a route), set a target, alert on burn rate, and write the runbook entry *before* the alert exists.
Practice this in gitjira-app `training/ladder/M2` and `S3`.
