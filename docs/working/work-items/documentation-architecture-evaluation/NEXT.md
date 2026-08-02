# Documentation Architecture Evaluation

## Status

In Design

## Ownership and Scope

Owner: Codex

Scope: preserve a candidate mature documentation architecture for independent
review and decide how it should relate to the migration already in progress.
This work item evaluates whether to complete the current migration first, pause
and replace it, or transition incrementally. It does not authorize any of those
strategies yet.

## Current State

- Branch `docs/migration-v4` starts at current `origin/main` commit
  `978136091639aa473b8b384b6b9ee8382da040c3`.
- `docs/new-proposed-docs/` contains 41 candidate documents covering a proposed
  documentation system, domain model, architecture, data ownership,
  development guidance, ADRs, assumptions, and runbooks.
- `docs/DAIRY.md` records the operator's creation of the proposal and migration
  idea.
- The proposal is explicitly non-authoritative and does not supersede root
  `AGENTS.md`, accepted grilling decisions, current canonical documentation, or
  the active migration.
- Several candidate ADRs say `Accepted`, and several candidate architecture and
  data documents say `status: active`. These labels remain preserved for review
  but have no current repository authority.
- No matching remote branch or pull request existed before publication.
- Commit `b215a74` preserves the bounded 45-file proposal and work-item scope on
  `origin/docs/migration-v4`.
- Draft pull request
  [#50](https://github.com/michi-guns/greek-essence/pull/50) targets `main` and
  states the evaluation-only status, unresolved migration strategies,
  authority boundaries, and fresh-review task.
- Prettier, redacted Gitleaks, commit and pre-push hooks, and a local Markdown
  link-target audit pass for the published proposal.

## Next Recommended Action

A fresh agent performs a read-only comparison of the current migration, live
documentation authority, and this proposal. The review should recommend one of
three strategies: complete the current migration first, pause and replace it,
or preserve useful completed work and transition incrementally.

Completion condition: the operator chooses a migration strategy after reviewing
the comparison, risks, sequencing, temporary inconsistencies, and treatment of
the proposed documents.

## Done When

- The current and proposed documentation architectures are compared against
  live repository authority and migration state.
- Premature product, domain, architecture, operational, or implementation claims
  in the proposal are identified.
- Migration options include scope, dependencies, risks, rollback implications,
  and a recommended sequence.
- The operator selects and records one strategy before any proposal document is
  promoted into canonical documentation.

## Constraints

- Keep the pull request in draft during evaluation.
- Do not merge, promote, or treat the candidate documents as current authority.
- Do not stop, replace, or continue the active migration solely because this
  proposal exists.
- Do not implement architecture, dependencies, schemas, migrations, operations,
  or product behavior from the proposal.
- Preserve unrelated and concurrent work.
