# Ralph/JZ Controller — Operator Exception 08

**Date:** 2026-07-24
**Resolved depth:** Tier 2 — Prototype
**Decision:** Accepted residual risk for overnight activation after the final bounded review.

## Technical verdict preserved

Immutable review 07 remains **FAIL**. Its finding is not reclassified as passing:

- controller/preflight do not reject a missing or mismatched `feature.id` when `feature.slug` resolves to a contained feature directory;
- an explicit `artifactPath: null` is treated like omission.

## Evidence and impact

The pinned stable `features-cli` 0.3.0 emits valid feature identity (`feature.id: 1`, `feature.slug: "greek-essence-showcase"`) and either omits `artifactPath` or emits a string. The residual finding requires malformed or internally inconsistent CLI JSON that the pinned normal path does not produce.

Normal overnight behavior is verified:

- artifact-less `review-issue` and resumed `implement-issue` route to the correct issue owner;
- artifact-less feature-level frontiers route to the feature owner;
- same-owner later iterations reuse one invocation-owned run directory;
- separate controller invocations cannot overwrite one another;
- Windows junction/reparse escapes are rejected;
- exact-PID ownership persistence and ambiguous-cleanup blocking remain green;
- full Ralph suite passed with 67 tests and one environment-only file-symlink skip.

## Operator authorization

Dimitris explicitly accepted bounded Tier-2 edge-case residuals to enable overnight feature implementation. This exception authorizes activation using the pinned stable CLI and current repository only. It does not authorize claiming review 07 passed, changing provider/model configuration, deployment, push, history rewriting, or weakening runtime ownership safeguards.

If live `features-cli` returns missing/mismatched feature identity or explicit `artifactPath: null`, stop the campaign and preserve evidence rather than treating that payload as trusted.
