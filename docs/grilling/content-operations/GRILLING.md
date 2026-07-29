# Content Operations Grilling

## Status

Queued as feature 7 of 8. Begin after the visitor and request feature grills are
accepted so their content needs are known.

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

None yet. Feature decision IDs begin at D-001.

## Open Questions

- D-001: Who may draft, approve, and publish content?
- D-002: Who owns English and Greek accuracy?
- D-003: What must preview show before publishing?
- D-004: Which required fields prevent incomplete public pages?
- D-005: How are licensed media and public claims recorded?
- D-006: How are mistakes, revisions, and deleted content recovered?

## Next Question

ID: D-001

Topic:
The smallest workable editing and publishing responsibility model.

Prompt:
Who should be able to write, approve, and publish public content in Sanity?

Options:

1. (recommended): **Named client content owner with a simple preview step.** One
   client owner may draft and publish after checking the preview; the operator
   or developer helps with setup and problems but does not silently approve
   business claims. Name separate English/Greek reviewers if the owner cannot
   approve both languages.
2. **Client supplies content; operator or developer publishes it.** This reduces
   client training but makes every update depend on technical availability and
   risks unclear approval responsibility.
3. **Separate editor and approver roles.** One person drafts and another must
   approve before publishing. This improves control but requires at least two
   reliable client participants and a more formal workflow.

Why this matters:
The website can only stay accurate if somebody knows they own each language and
has a practical way to check changes before real visitors see them.

After answer:

- Lock content roles and approval responsibility.
- Store D-002 as the next question.
