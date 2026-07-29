# General Contact Grilling

## Status

Accepted by the operator on 2026-07-29. D-001 through D-005 are locked and ready
for distillation; raw-ledger removal has separate path-specific approval.

This grill does not authorize implementation. Use [../DECISIONS.md](../DECISIONS.md)
and [../protocol.md](../protocol.md).

## Locked Project Context

- A general contact form is required for questions outside consultation and
  booking requests.
- Consultation and booking intent must retain their clearer dedicated journeys.
- The agency follows up through its existing email and telephone process.

## Scope

Define appropriate message purposes, minimum fields, routing to dedicated
travel-request journeys, privacy wording, and success and failure behavior.

## Locked Decisions

### D-001 — General Questions with Clear Travel-Request Routes

The Contact page accepts ordinary questions that fall outside the two dedicated
travel-request journeys. This includes general agency, partnership, media, and
other enquiries that do not require the structured trip-planning or
Experience-specific information collected elsewhere.

The page provides prominent routes to Consultation Request for trip-planning
help and to the applicable Booking Request journey for interest in a specific
Experience. General Contact does not become an alternative catch-all submission
path for those requests.

This preserves a welcoming path for unusual traveler questions while avoiding
incomplete travel enquiries and inconsistent request records. Restricting
Contact to business enquiries was rejected as unnecessarily unfriendly, and
accepting every message type through Contact was rejected because it would
undermine the dedicated journeys.

### D-002 — Email-Only Contact and Follow-Up

General Contact requires one name field, email address, subject, message, and
privacy acknowledgement. It does not ask for a telephone number or a preferred
reply channel.

Email is the sole automated acknowledgement and agency follow-up channel for
this journey. This is the smallest useful field set for an ordinary question,
keeps the reply path clear, and avoids collecting a telephone number without a
necessary purpose. Telephone may remain part of the agency's broader manual
process, but General Contact does not offer it.

Optional telephone collection with or without a reply preference was rejected
as unnecessary personal-data collection for this journey. Requiring both email
and telephone was rejected because it would collect more data and block valid
questions without a demonstrated operational need.

### D-003 — Pre-Form Intent Routing

Before showing the General Contact form, the Contact page asks whether the
visitor wants trip-planning help, wants to request a specific Experience, or
has another question.

Trip-planning intent routes to Consultation Request. Interest in a specific
Experience routes to the catalogue so the visitor can select a requestable
Experience and use that Experience's Booking Request. Choosing another question
shows the General Contact form. Visible text links preserve an accessible route
that does not depend on the intent control or client-side scripting.

An always-visible catch-all form was rejected because visitors could too easily
ignore the better route. Collecting travel intent inside General Contact was
rejected because it would recreate incomplete travel requests and manual staff
sorting. Inferring intent after submission was rejected as late and
unpredictable.

### D-004 — Just-in-Time Privacy and Persistent Message Warning

Beside submission, General Contact explains in concise language that Greek
Essence will save and use the submitted details to handle the question and
reply by email. It links to the full privacy notice and requires an unchecked
“I have read the privacy notice” acknowledgement or an approved bilingual
equivalent.

The acknowledgement records that the notice was presented. It is not blanket
consent and must not be treated as consent to unrelated processing. General
Contact has no marketing consent; newsletter functionality is excluded from the
product.

Beside the message field, a persistent helper—not placeholder-only text—uses the
same approved nine-word English warning as Consultation Request:

> Please don’t include passport, payment, or medical information here.

The Greek wording must preserve the same concise meaning and receive client
review. If a visitor submits sensitive information despite the warning, the
message remains in the protected private-data workflow. Request Processing and
Communications, with qualified privacy review, must define access, notification
content, redaction, deletion, retention, and incident handling.

Omitting the warning was rejected because the free-text field can attract
unnecessary sensitive details. A notice link without acknowledgement was
rejected because it weakens evidence that the notice was presented at
collection. Broad processing and marketing consent was rejected as misleading
and outside the accepted product.

### D-005 — Honest Submission Outcomes and Message Reference

General Contact distinguishes these visitor-visible outcomes:

- **Validation failure:** show field-level errors, preserve the entered message
  for correction, and do not claim receipt.
- **Safely saved message:** state that the message was received, show an opaque
  non-sensitive reference that reveals no personal data or sequential private
  record details, and explain the email-only next step without an unapproved
  response-time promise.
- **Safely saved message with failed or unconfirmed customer-email delivery:**
  preserve the received-message truth and reference, explain honestly that email
  delivery could not be confirmed, and do not ask the visitor to resubmit.
- **Agency-notification failure after saving:** preserve the received message,
  show saved-message success and the reference without claiming staff were
  emailed, and recover through shared monitoring and staff operations.
- **Persistence failure:** state that the message was not received, preserve the
  entered content for safe retry, offer only client-approved alternative contact
  details, and expose no technical error details.

Saving and email delivery are separate responsibilities. Customer-email
delivery is not the success condition because treating it that way could create
duplicates after an already-saved message. A generic thank-you outcome was
rejected because it could falsely claim receipt or hide that no recoverable
message exists.

Request Processing and Communications owns exact persistence, opaque-reference
generation, validation, duplicate protection, email delivery, retry,
monitoring, and agency recovery mechanics while preserving these visible
distinctions.

## Open Questions

None. The operator accepted the feature grill.

## Acceptance

The operator accepted D-001 through D-005 on 2026-07-29. No unresolved
feature-level question remains. Distill the decisions, verify semantic parity,
and remove this raw ledger under the separately granted path-specific approval.
