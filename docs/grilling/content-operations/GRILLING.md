# Content Operations Grilling

## Status

Active as feature 7 of 8 after the visitor and request feature grills were
accepted and established their content needs.

This grill does not authorize implementation. Use [../DECISIONS.md](../DECISIONS.md)
and [../protocol.md](../protocol.md).

## Locked Project Context

- Sanity owns editable public and catalogue content.
- Client validation is example-led.
- English/Greek ownership, editors, approval, preview, media rights, and recovery
  require confirmation.
- Private customer and request records must never be stored in Sanity.

## Scope

Define how Sanity is used: the editorial domain entities and relationships,
English/Greek content model, draft and publication states, preview and
application integration, required-content validation, media and claim evidence
records, revisions, and recovery. Easily changed staffing assignments remain
launch validations rather than architecture decisions.

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
perform publishing and how approved changes are handed over. Those named people
are launch validations, not additional architecture decisions.

Direct client publishing and a mandatory separate editor-and-approver workflow
were not selected for the preview release.

## Open Questions

- D-002: Which editorial entities and relationships does Sanity own?
- D-003: How are English and Greek variants modeled in Sanity?
- D-004: What draft, validation, and publication state model is required?
- D-005: How do preview, rendering, caching, and invalidation integrate with
  Next.js?
- D-006: How are media rights and public-claim evidence modeled?
- D-007: How are revisions, deletions, migration, and content recovery handled?

## Next Question

ID: D-002

Topic:
The core Sanity domain model.

Prompt:
Which foundational content model should Sanity use for Greek Essence?

Options:

1. (recommended): **A typed domain model with constrained supporting content.**
   Destination and Experience are first-class document types; an Experience
   references one Destination and uses the accepted type values, with Interest
   added only if its taxonomy is approved. Home, About, Contact, legal content,
   site settings, and navigation use bounded singleton or supporting document
   types. This preserves meaningful relationships and validation without
   creating a general-purpose page builder.
2. **A generic page-and-block model.** Most public content is assembled from one
   flexible Page type and reusable blocks. This allows broad layout changes but
   weakens domain constraints, makes catalogue queries harder, and introduces a
   page-builder system before the preview needs one.
3. **A separate document type for every page and catalogue variation.** Home,
   About, each legal surface, Destinations, Tours, Activities, and Travel
   packages all get distinct schemas. Validation is explicit, but shared fields
   and behavior are duplicated and schema maintenance grows quickly.

Why this matters:
This decides the CMS entities, their relationships, the shape of queries and
validation, and whether the application is built around stable travel-domain
concepts or a generic page-building abstraction.

After answer:

- Lock the core Sanity entities and relationship strategy.
- Store D-003 as the next foundational question.
