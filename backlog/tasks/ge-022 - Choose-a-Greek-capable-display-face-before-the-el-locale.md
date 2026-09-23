---
id: GE-022
title: Choose a Greek-capable display face before the /el/ locale
status: To Do
assignee: []
created_date: '2026-09-23 09:20'
labels:
  - 'lane:product'
dependencies: []
type: chore
ordinal: 96000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Fraunces, the heading face chosen in S-005 (docs/v1/05-STACK.md), has no Greek glyphs: @fontsource-variable/fraunces 5.3.0 ships only latin, latin-ext and vietnamese subsets. Inter ships Greek. v1 is English-only (D-005), so nothing breaks now, but every heading on the planned /el/ site would fall back to a system serif, and no Greek-script display moment (a place name in Greek, a Greek wordmark) is possible in Fraunces even in v1. Found during GE-003.01 visual research on 2026-09-23. Decide before Greek content is scheduled: keep Fraunces for Latin and pair a Greek-capable serif for /el/, or replace Fraunces site-wide. Not urgent for v1.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A Greek-capable display face is chosen and recorded in 05-STACK.md next to S-005, with the reason
- [ ] #2 A Greek sample headline renders in the chosen face with no fallback glyphs, checked by screenshot
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
