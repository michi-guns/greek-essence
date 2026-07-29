# Consultation Request Decisions

## Status and Authority

Accepted by the operator on 2026-07-29 after feature grilling.

This document defines the Public Preview Release boundary for the initial trip
planning brief, contact channel, required and optional information, privacy
presentation, visitor-visible submission outcomes, free-text safety, and age
handling in the Consultation Request journey.

It does not authorize application implementation, dependency installation,
schema migration, deployment, or destructive path changes. Those require later
promoted canonical documentation and explicit bounded implementation contracts.

Use the project terms in [../GLOSSARY.md](../GLOSSARY.md). The accepted project
boundary remains in [../DECISIONS.md](../DECISIONS.md).

## Feature Boundary

A Consultation Request asks Greek Essence to help plan a trip. It is a short
initial enquiry, not a detailed questionnaire, offer, reservation, or confirmed
booking. The agency follows up manually by email. Online payment, automated
scheduling, and the deferred post-enquiry questionnaire are outside this
feature.

Every accepted request is private transactional data. “Received” means the
request was safely saved; email delivery is a separate outcome.

## D-001 — Short Structured Trip Brief

The initial request collects enough structured context for a useful first
agency response without becoming a detailed planning intake.

It covers the visitor's contact and core trip context, with optional timing,
budget guidance, and notes as refined by D-002 and D-003. Detailed
accommodation, transport, daily planning, traveler identity, and sensitive
planning information are gathered only during appropriate manual follow-up if
needed.

A contact-only callback request is insufficient because it creates avoidable
back-and-forth. A detailed first-contact questionnaire is excluded because it
increases abandonment and sensitive-data collection before the agency needs
that information.

## D-002 — Email-Only Acknowledgement and Follow-Up

The form requires an email address. Email is used for both the automated
arrival acknowledgement and the agency's personal follow-up. The form does not
ask for a telephone number or contact-method preference.

Telephone may remain part of the agency's broader manual process, but it is not
offered by this initial Consultation Request journey.

The public journey shows a response window only after the client confirms one
the agency can meet reliably. Until then, it may promise follow-up by email but
must not promise a deadline.

## D-003 — Required, Optional, and Excluded Information

The initial request requires:

- one name field;
- email address;
- party size as a group count;
- at least one destination or interest; and
- the D-004 privacy acknowledgement.

Approximate timing is optional and supports “not sure yet.” Budget guidance and
the short notes field are also optional.

The form does not request:

- a telephone number;
- individual traveler identities;
- exact birth dates;
- passport or identity-document information;
- payment or bank details;
- medical details; or
- detailed accessibility information.

Exact destination and interest controls must align with accepted catalogue
content. Budget ranges and currency and all English and Greek field wording
require example-led client validation rather than invented taxonomies or
commercial assumptions.

## D-004 — Just-in-Time Privacy Explanation

Beside the submission action, the form explains in concise, plain language that
Greek Essence will save and use the submitted details to handle the request and
reply by email. It links to the full privacy notice and requires an unchecked “I
have read the privacy notice” acknowledgement or an approved bilingual
equivalent.

The acknowledgement records that the notice was presented. It is not blanket
consent and must not be treated as consent to unrelated processing. The form
includes no marketing consent; newsletter functionality is excluded from the
product.

Before public launch, the client and an appropriately qualified reviewer must
confirm the controller identity and contact details, processing purposes,
applicable lawful basis, recipients or recipient categories, retention period,
visitor rights, complaint route, international-transfer facts where relevant,
and final English and Greek wording against the agency's actual processing.
This decision defines product presentation, not legal approval.

## D-005 — Honest Submission Outcomes and Request Reference

Validation errors appear at the relevant fields and preserve the entered brief
on the current form for correction. The interface does not claim receipt before
the request is safely saved.

After a successful save, the visitor sees:

- that the Consultation Request was received;
- an opaque, non-sensitive reference code that encodes no personal information
  or sequential private-record details;
- the email-only next step; and
- only a client-approved response window.

Saving and email delivery remain separate:

- If the visitor acknowledgement fails after saving, the page says the request
  was received but the confirmation email could not be sent, shows the
  reference, and does not ask the visitor to resubmit.
- If the internal agency notification fails after saving, the request remains
  received. The page shows saved-request success and the reference without
  falsely claiming staff were emailed. Monitoring, retry, and staff recovery
  handle the operational failure.
- If saving fails, the page clearly says the request was not received,
  preserves the entered brief for immediate retry, and offers only
  client-approved alternative agency contact details. It exposes no technical
  error details.

Request Processing and Communications owns exact persistence, acknowledgement,
notification, retry, duplicate protection, monitoring, and recovery mechanics
while preserving these visible distinctions.

## D-006 — Optional Notes with a Short Persistent Warning

The optional notes field remains available for ordinary trip context. A
persistent helper beside the field—not placeholder-only text—uses this approved
nine-word English warning:

> Please don’t include passport, payment, or medical information here.

The Greek version must preserve the same concise meaning and receive client
review. Placeholder text may provide a short example but must not carry the
safety instruction.

If a visitor submits sensitive information despite the warning, the request
stays in the protected private-data workflow and the notes are not echoed into
notification email. Request Processing and Communications, with privacy review,
must define staff access, redaction, deletion, retention, and incident handling.

## D-007 — No Special Age Gate

The Consultation Request form does not ask for age or birth date, require an
adult-status checkbox, or introduce a child-specific guardian workflow. It is
an ordinary initial travel enquiry and is not marketed specifically to children.

This avoids adding an unsupported restriction or special workflow. If the
client or an appropriately qualified reviewer later identifies a concrete legal
or operational age requirement, it must return as an explicit change.

## Explicit Exclusions and Deferrals

- The initial request is not a detailed planning questionnaire.
- Telephone contact and contact-method preference are not part of this journey.
- A public response-time promise is not allowed without client approval.
- The form does not collect the excluded identity, payment, medical, or detailed
  accessibility information listed in D-003.
- Privacy acknowledgement is not blanket or marketing consent.
- Notes are not copied into notification email.
- The form has no speculative age gate or child-specific workflow.
- Online payment, automated scheduling, confirmed booking, and detailed
  post-enquiry intake remain deferred.
- This feature does not define shared persistence, email, duplicate protection,
  staff tooling, monitoring, recovery, retention, redaction, or incident
  mechanics.

## Dependencies and Unresolved External Validations

- **Client:** approve destination and interest choices, budget presentation,
  alternative contact details, a reliable response window if one is published,
  and final English and Greek form, acknowledgement, warning, success, and
  failure wording.
- **Client and qualified privacy or legal reviewer:** validate the actual
  controller facts, lawful basis, privacy notice, retention, recipients, rights,
  transfer facts, age boundary if evidence later requires one, and handling of
  sensitive information submitted despite the warning.
- **Catalogue Discovery and Content Operations:** provide approved bilingual
  destination and any Interest vocabulary used by the form.
- **Request Processing and Communications:** define private persistence,
  opaque references, validation, duplicate protection, email delivery,
  notification content that excludes notes, retry, monitoring, staff recovery,
  access, redaction, deletion, retention, and incident handling.
- **Production Operations:** provide secure configuration, monitoring, recovery,
  and operational ownership before accepting real enquiries.

These validations may refine approved wording, controlled values, and
operational ownership. They must not silently add a detailed questionnaire,
telephone collection, unsupported response promise, false receipt claim, broad
consent, or unnecessary sensitive-data collection.
