# Analytics/Metrics Decision Protocol

## Rules and Protocol

1. Ask decisions in batches of exactly five questions unless fewer unresolved decisions remain.
2. Number questions sequentially as `QNN: <Question Title>`.
3. For every question, provide only the question title, a brief description, and one clear recommendation.
4. Keep each description to one short paragraph.
5. Prefer the smallest, fastest implementation that provides useful diagnostic evidence for unattended Ralph runs.
6. Drop or defer metrics that are difficult, unreliable, invasive, or expensive to collect.
7. After the operator answers, record each locked decision in this file before asking the next batch.
8. Preserve prior locked decisions verbatim unless the operator explicitly revises them.
9. Do not begin implementation until the required decisions are locked.

## Chat Response Template

### QNN: <Question Title>

<Brief description of the decision problem.>

**Recommendation: <Recommended decision>**

### QNN: <Question Title>

<Repeat the same structure for five questions per batch, or for every remaining question when fewer than five remain.>

## Locked Decisions

### Q01-AnalyticsStorageLocation
Store generated analytics inside the repository under `.scratch/ralph-loop/analytics/`. Keep the generated analytics files ignored by Git so the implementation stays simple and unattended runs do not dirty the worktree.

### Q02-AnalyticsFileFormat
Use an append-only JSON Lines (`.jsonl`) event log. Record one timestamped event per line so interrupted unattended runs preserve all previously written analytics and Python can process the data without external dependencies.

### Q03-FirstVersionMetricScope
Record directly observable timing plus session counters that Hermes already exposes reliably. Target campaign, task, iteration, implementation, review, and other observable step durations; also collect turns, tool calls, compactions, and final context-window usage when readily available. Omit or explicitly mark unavailable metrics rather than estimating them, and defer invasive instrumentation.

### Q04-RalphCampaignDefinition
A Ralph Campaign is the process of taking a defined list of one or more tasks and implementing them. A campaign may contain only one task, particularly during testing, without changing the campaign definition.

### Q05-AnalyticsFileOrganization
Store one append-only JSON Lines file per campaign at `.scratch/ralph-loop/analytics/<campaign-id>.jsonl`. Identify tasks, steps, and iterations through fields on each event rather than splitting them across additional files.

### Q06-StepBoundaryRecording
Provide a small Python recorder command for explicit campaign, task, and step start/end events. Require the root orchestrator to call it around implementation, review, correction, verification, and closure when those boundaries are under agent control; let the Ralph controller record the lifecycle boundaries it owns directly. Treat missing events as missing data rather than inferring or estimating them.

### Q07-AnalyticsReadingInterface
Create an agent skill that reads the campaign JSONL analytics files and provides a useful human-readable summary. Prefer agent interpretation over a deterministic reporting script so the summary can identify meaningful patterns, anomalies, likely bottlenecks, and missing evidence without building a rigid reporting system.

### Q08-AnalyticsFailurePolicy
Fail open immediately with no retry when an analytics write or collection operation fails. Continue Ralph's primary work and record that the analytic could not be stored or collected; include the error reason when readily available, but do not make obtaining that reason a hard requirement.

### Q09-AnalyticsReaderSkillLocation
Create a repository-local analytics reader skill at `.agents/skills/ralph-analytics/`. Keep it specific to this repository's Ralph paths and analytics schema so it can be implemented quickly and versioned alongside the recorder.

### Q10-TaskStepCategories
Use the recommended standard task-step categories `implementation`, `review`, `correction`, `verification`, and `closure`, while allowing a concise custom step name when genuinely needed. Standard categories support comparisons without making taxonomy validation a blocker.

### Q11-AnalyticsEnabledByDefault
Enable analytics automatically for every normal Ralph run. Do not require an opt-in flag; generated files remain ignored by Git and analytics failures remain fail-open.

### Q12-TimestampStandard
Store UTC ISO 8601 timestamps and measured duration seconds so events remain comparable across long-running sessions and timezone changes.

### Q13-SessionCounterSource
Collect turns, tool calls, compactions, and final context-window usage from Hermes's existing structured session metadata only when access is simple, safe, and straightforward. Skip any counter requiring fragile transcript inference, invasive integration, or material implementation effort.

### Q14-AnalyticsSchemaVersion
Add an integer `schema_version` to every analytics event, starting at `1`, so the event format can evolve without ambiguity.

### Q15-CampaignTerminalStates
Support explicit `completed`, `abandoned`, and `blocked` campaign outcomes. Leave interrupted campaigns without a terminal event rather than inferring an outcome.

### Q16-AnalyticsRetention
Never delete generated analytics automatically in the first version. Retention and cleanup remain manual operator actions.

### Q17-RecordedContentBoundary
Record diagnostic metadata and concise error summaries only. Never store full prompts, model responses, tool arguments, or file contents in analytics events.

### Q18-IncompleteEventPairs
Preserve a start event without its corresponding end event and report it as incomplete. Never invent an end time or calculate a fabricated duration.

### Q19-HistoricalBackfill
Do not backfill analytics from historical Ralph logs or sessions. Begin collecting data only after this feature is enabled.

### Q20-AnalyticsDisableSwitch
Do not add an analytics disable switch in the first version. Analytics remain enabled by default and fail open, so collection failures cannot block Ralph's primary work.

### Q21-FirstVersionDeliveryBoundary
Limit the first version to JSONL event recording, Ralph controller and orchestration integration, focused tests and documentation, and the repository-local analytics reader skill. Defer dashboards, databases, charts, exports, historical backfill, and complex metric extraction.
