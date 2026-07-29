# Project and Public Preview Release Grilling

## Status

Active project-level grilling. This ledger establishes the preview release's
product boundary and feature map before feature-specific grilling begins.

## Protocol

- Ask one decision question at a time.
- Offer two to four reasonable numbered options.
- Prefix the recommended option exactly with `(recommended):`.
- After each answer, persist the accepted decision, rejected alternatives,
  consequences, and next question before continuing.
- When the high-level grill is accepted, replace this file with a refined
  `DECISIONS.md` and create feature workspaces only for confirmed features.

## Operator Preferences

- Use multiple grilling sessions where useful rather than forcing premature
  closure.
- Begin with a general understanding of the public preview release, then grill
  each confirmed feature independently.
- Keep all durable grilling state under `docs/grilling/`.
- Use `GRILLING.md` only while a grill is active; replace it with distilled
  `DECISIONS.md` when complete.
- Do not use the removed engineering-depth concept.

## Current Design Target

- Product: Greek Essence public platform.
- Release: Public Preview Release, targeted for the end of August in the current
  working roadmap.
- Goal: Establish the smallest coherent production-facing release boundary and
  its real business features before choosing final module boundaries or
  implementation tasks.

## Evidence Base

- The full former documentation baseline is preserved under
  `docs/archive/showcase-prototype-v0/`; every document there is historical
  reference and has no current authority.
- The operator-authored, agent-assisted roadmap, domain architecture, and Layer
  2 migration brief are provisional working drafts not yet reviewed by the
  client.
- The release is operator-confirmed as publicly accessible and expected to
  receive real visitors and enquiries.
- Sanity, Supabase, and Drizzle are strong candidate platform directions, not
  yet approved implementation contracts.
- Requirements Batch 01 currently contains 27 reported requirements and 15
  conflicts or clarification needs.

## Established Context

- The stateful workflow and file lifecycle are defined in `protocol.md`.
- Grilling combines software-engineering analysis with product-management and
  travel-agency operations coaching as defined in `AGENTS.md` and
  `protocol.md`.
- The preview release will be public and is expected to receive real visitors
  and enquiries.
- The removed engineering-depth concept must not return through grilling,
  requirements, contracts, or implementation planning. State concrete quality
  and risk controls instead.

## Locked Decisions

None yet. Project decision-question numbering begins with D-001 below.

## Rejected or Superseded Options

### R-001: Private Prototype Framing

Rejected because the release will be public and accept real enquiries.

### R-002: Engineering-Depth Tiers

Rejected because the project removed the abstraction in favor of explicit
requirements and risk controls.

### R-003: Immediate Feature Folder Creation

Rejected because feature boundaries must follow accepted product capabilities,
not provisional architecture drafts.

## Candidate Feature Areas

These are prompts for the high-level grill, not accepted feature boundaries:

- editorial website and brand content;
- catalogue and search;
- consultation request;
- booking request;
- contact and newsletter capture;
- customer identity and reuse;
- notifications and communications;
- content operations and preview;
- production platform and operations.

## Open Questions

- D-001: What is the primary product promise of the Public Preview Release?
- D-002: Which user-visible capabilities are required at launch?
- D-003: Which operational capabilities must the agency have at launch?
- D-004: What are the accepted product feature boundaries and dependencies?
- D-005: Which candidate platforms are mandates versus implementation choices?
- D-006: Which decisions require client validation before scope freeze?
- D-007: What is explicitly deferred beyond the Public Preview Release?

## Next Question

ID: D-001

Topic:
Primary product promise of the Public Preview Release.

Prompt:
When the public preview succeeds, what is the core thing a real visitor must be
able to accomplish—and what must the agency reliably receive or do in response?

Options:

1. (recommended): **Editorial catalogue plus two managed enquiry paths.**
   Visitors discover destinations and Experiences, then submit either a
   consultation request or a clearly non-confirming booking request. The agency
   receives reliable records and notifications and handles follow-up manually.
2. **Editorial catalogue plus consultation only.** Visitors browse the same
   content, but all intent routes through one consultation request; booking
   requests are deferred.
3. **Catalogue and broader lead capture.** Include consultation, booking request,
   contact, and newsletter acquisition as equal launch workflows.
4. **Early operational platform.** Include the public catalogue and enquiry
   paths plus a custom agency dashboard for reviewing and managing requests.

Why this matters:
This decision determines the initial product promise, the minimum transactional
domain, the operational burden, and which feature grills must exist. It also
protects the deadline from quietly expanding into payments, scheduling,
questionnaires, confirmed bookings, or a custom back office.

After answer:

- Lock the accepted preview-release promise.
- Record rejected or deferred alternatives.
- Refine the candidate feature areas.
- Replace this section with D-002.

## Notes

- The current roadmap proposes Option 1, with contact also present as a public
  page and submission journey.
- Newsletter remains explicitly conditional in the working drafts.
- Payments, questionnaires, automated scheduling, and confirmed bookings are
  currently deferred beyond the preview release.
