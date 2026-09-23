---
id: GE-021
title: Reconcile the pre-push quality gate with .husky
status: To Do
assignee: []
created_date: '2026-09-23 08:51'
labels: []
dependencies: []
type: chore
ordinal: 95000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
docs/v1/03-WORKFLOW.md §6 promises a pre-push tier (typecheck + lint + test:unit + gitleaks) on every push, but .husky/ has only commit-msg, post-commit and pre-commit. Nothing runs on push, so a local push can reach main with a type error or a leaked secret that only CI (main and PRs only) or nobody catches. Found by the doc-reviewer on 2026-09-23 while fixing the push-authority wording; left out of that change's scope. Decide whether the hook is added (T-00.3 intended it) or the doc tier is dropped, then make code and doc agree.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Either .husky/pre-push runs the tier in 03-WORKFLOW §6, or §6 no longer lists a pre-push tier
- [ ] #2 If the hook is added, a push with a failing typecheck is refused locally
- [ ] #3 03-WORKFLOW §6 and .husky/ describe the same gates
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Acceptance criteria met; final summary records what was checked and what remains
- [ ] #2 typecheck, lint and unit tests pass
- [ ] #3 User-visible change: live walk completed per A-007 with evidence in .local/evidence/ - or state why not applicable
- [ ] #4 Anything odd noticed is filed as a task, not dropped
- [ ] #5 Task branch merged into its phase branch
- [ ] #6 Documentation lifecycle checked (doc-lifecycle): what this work made stale is updated, what it superseded is merged or deleted - or state why not applicable
<!-- DOD:END -->
