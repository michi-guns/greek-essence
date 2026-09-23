---
id: GE-024
title: Docs use she and he for the same client
status: To Do
assignee: []
created_date: '2026-09-23 19:07'
labels:
  - 'lane:product'
dependencies: []
type: docs
ordinal: 98000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
docs/v1/00-DECISIONS.md refers to the client as she (line 35, lines 213 and 219) and as he (D-032 revised, line 100). Agents copy pronouns from these files into client-facing text, so one of them is wrong in front of the client. Found 2026-09-23 during GE-003.03; which is correct is the operator's knowledge, not something an agent can infer.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The operator confirms how the client is referred to
- [ ] #2 docs/v1/ and AGENTS.md use that form consistently, or neutral wording
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
