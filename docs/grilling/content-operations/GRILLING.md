# Content Operations Grilling

## Status

Paused and preserved as a mixed-layer classification source. Do not continue
from the stored D-002 question. Its approved disposition is recorded in
[`../CLASSIFICATION.md`](../CLASSIFICATION.md); the two remaining upstream gaps
continue under Product and Domain Truth, while technical mechanisms move to the
Editorial Content Platform foundation and named people/evidence move to Launch
Readiness.

This grill does not authorize implementation. Use [../DECISIONS.md](../DECISIONS.md)
and [../protocol.md](../protocol.md).

## Locked Project Context

- Sanity owns editable public and catalogue content.
- Client validation is example-led.
- English/Greek ownership, editors, approval, preview, media rights, and recovery
  require confirmation.
- Private customer and request records must never be stored in Sanity.

## Scope

Define content roles, English/Greek workflow, draft review and publishing,
preview access, required-content validation, media rights, environments,
revisions, and content recovery.

## Locked Decisions

### D-001 — Client-approved content, technically published

The client supplies the public content and explicitly approves it for
publication. A named operator or developer then enters or updates the content,
checks the preview and applicable publication requirements, and publishes it in
Sanity. Technical publication does not make the operator or developer the
approver of agency facts, prices, claims, media rights, or other business
content.

This deliberately avoids requiring the client to learn the publishing system,
but every update depends on technical availability. Before launch, the client
must name who can give publication approval, and the project must name who will
perform publishing and how approved changes are handed over. English and Greek
accuracy ownership remains D-002 rather than being implied by the technical
publisher role.

Direct client publishing and a mandatory separate editor-and-approver workflow
were not selected for the preview release.

## Open Questions

- D-002: Who owns English and Greek accuracy?
- D-003: What must preview show before publishing?
- D-004: Which required fields prevent incomplete public pages?
- D-005: How are licensed media and public claims recorded?
- D-006: How are mistakes, revisions, and deleted content recovered?

## Next Question

ID: D-002

Topic:
English and Greek content accuracy ownership.

Prompt:
Who should be responsible for checking and approving the accuracy of the
English and Greek content before the operator or developer publishes it?

Options:

1. (recommended): **Name one responsible human reviewer for each language.**
   The same bilingual person may own both only if the client confirms they can
   reliably approve both. Each reviewer checks natural wording, factual
   accuracy, service boundaries, and meaning parity before publication.
2. **One client owner approves both languages.** This is the simplest handoff,
   but it is safe only if that person can genuinely judge both English and
   Greek; otherwise translation mistakes may be published as approved content.
3. **Client approves the Greek facts and a named language professional reviews
   English.** This gives English specialist review while keeping business facts
   with the client, but adds an external participant and a recurring handoff.

Why this matters:
Separate storage does not ensure equivalent meaning. A mistranslated price,
service promise, or booking-request boundary could mislead one audience even
when the other language is correct.

After answer:

- Lock English and Greek accuracy ownership.
- Store D-003 as the next question.
