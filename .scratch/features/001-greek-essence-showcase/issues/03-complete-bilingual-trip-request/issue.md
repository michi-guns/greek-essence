Status: ready-for-agent
Method: tdd-solo
Complexity: 5
BlockedBy: none
Milestone: complete-resilient-trip-request

# Complete the accessible bilingual four-step trip request

Add the localized Plan My Trip route and one focused form island so a visitor entering directly or from Paros can complete the exact Trip, Travelers, Preferences, and Contact steps with canonical values, realistic validation, and safe correction behavior. This slice stops at a validated final form state; transport, submission, and confirmation belong to the later submission milestone.

## Acceptance criteria

- [ ] English and Greek Plan My Trip routes render the exact four-step request with every accepted field, option, default, and grouping; direct entry starts with Help me choose while the allow-listed Paros query visibly preselects editable Paros & Antiparos context (FR-004, DEC-003, SUBDEC-001).
- [ ] Continue validates only the active step, then updates affected errors during correction; Back neither validates nor clears values, and the final step can prove a canonical valid form without sending or claiming success (FR-004, SUBDEC-001).
- [ ] Children create one required age control per child, increasing the count preserves existing ages, and reducing a count that would discard populated ages requires explicit confirmation before truncation (FR-005, SUBDEC-001).
- [ ] Date, party, option, contact-method, Unicode-safe text-length, phone, privacy-acknowledgement, unknown-key, and canonical normalization rules match the approved form contract, while optional values normalize predictably and unsupported fields remain absent (FR-004, NFR-004, NFR-005, SUBDEC-001).
- [ ] All form labels, options, progress, helper copy, validation, confirmation-dialog copy, and correction states have complete natural English/Greek message parity with untranslated canonical IDs and no mixed-language fallback (FR-013, DEC-008, SUBDEC-004, NFR-007).
- [ ] Both localized Plan My Trip routes emit non-empty localized metadata, self-canonical URLs, `en`/`el`/`x-default` alternates, and `noindex,nofollow`, while remaining static-first outside the bounded client form island (FR-015, DEC-010, NFR-008).
- [ ] The form is keyboard-completable with persistent labels, associated inline errors, a focusable linked error summary, visible focus, semantic controls, usable targets, reduced-motion behavior, and no horizontal overflow or clipped Greek copy at the required compact and wide viewports plus representative Tier-2 responsive checks (NFR-001, NFR-002, DEC-012).
- [ ] Form routes, URLs, metadata, fixtures, screenshots, console output, and browser artifacts contain no personal data; helper copy warns against sensitive free text, and no server, analytics, or unsupported dynamic boundary is introduced (NFR-003, NFR-004, NFR-005, DEC-010).
- [ ] Focused schema/component tests and guarded compact/wide browser checks prove exact step progression, realistic invalid/correction cases, Back behavior, dependent child ages, direct/contextual entry, bilingual parity, metadata, accessibility, responsiveness, and preserved performance budgets without duplicating exhaustive matrices (NFR-003, NFR-008, DEC-012).

Traces: FR-004, FR-005, FR-013, FR-015; NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-007, NFR-008; DEC-003, DEC-008, DEC-010, DEC-012, SUBDEC-001, SUBDEC-004.
