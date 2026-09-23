---
id: GE-023
title: 'DS-006: focus ring colour on photographs and filled bars'
status: To Do
assignee: []
created_date: '2026-09-23 19:07'
labels:
  - 'lane:product'
dependencies: []
type: docs
ordinal: 97000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
DS-006 (docs/v1/02-DESIGN-SYSTEM.md §6) says the focus ring is teal everywhere. In the GE-003.03 direction demos the teal ring nearly vanished on a dark photograph (image-led outline button) and was clipped at the screen edge on the pinned blue phone bar, so the demos use a white ring there (app/directions/_shared/directions.css). Found 2026-09-23; round-1 visual review judged the deviation justified. The rule should say what happens on photographs and on filled blue surfaces before GE-004.01 builds the tokens.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 DS-006 states the focus ring colour and offset on a photograph and on a filled blue button or bar
- [ ] #2 The chosen ring passes 3:1 non-text contrast against both surfaces, checked by screenshot
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
