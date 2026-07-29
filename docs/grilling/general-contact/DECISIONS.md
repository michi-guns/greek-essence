# General Contact Decisions

## Status and Authority

Accepted by the operator on 2026-07-29 after feature grilling.

This document defines the Public Preview Release boundary for messages outside
the dedicated Consultation Request and Booking Request journeys, the minimum
contact fields and reply channel, pre-form intent routing, privacy and free-text
safety, and visitor-visible submission outcomes.

It does not authorize application implementation, dependency installation,
schema migration, deployment, or destructive path changes. Those require later
promoted canonical documentation and explicit bounded implementation contracts.

Use the project terms in [../GLOSSARY.md](../GLOSSARY.md). The accepted project
boundary remains in [../DECISIONS.md](../DECISIONS.md).

## Feature Boundary

General Contact is for ordinary agency, partnership, media, unusual traveler,
and other questions that fall outside the two structured travel-request
journeys. It is not an alternative way to submit a trip-planning request or
interest in a specific Experience.

Every accepted message is private transactional data. “Received” means that the
message was safely saved. Customer and agency email delivery are separate
outcomes.

## D-001 — General Questions with Clear Travel-Request Routes

The Contact page accepts ordinary questions that do not require the structured
trip-planning or Experience-specific information collected by the dedicated
request journeys.

It prominently routes trip-planning help to Consultation Request. Interest in a
specific Experience routes through the catalogue to the applicable Booking
Request journey. General Contact remains available for other questions,
including unusual traveler questions that do not fit either structured journey.

Accepting every message type through Contact is excluded because it would
produce incomplete travel enquiries and inconsistent request records.
Restricting Contact to business enquiries is also excluded because it would
remove a welcoming route for legitimate traveler questions outside the two
travel-request journeys.

## D-002 — Email-Only Contact and Follow-Up

General Contact requires:

- one name field;
- email address;
- subject;
- message; and
- the D-004 privacy acknowledgement.

It does not ask for a telephone number or preferred reply channel. Email is used
for both the automated arrival acknowledgement and the agency's personal
follow-up through this journey.

Telephone may remain part of the agency's broader manual process, but General
Contact does not offer it. Optional or required telephone collection is excluded
because no necessary purpose has been established for this journey.

## D-003 — Pre-Form Intent Routing

Before showing the General Contact form, the Contact page asks whether the
visitor wants:

1. trip-planning help;
2. to request a specific Experience; or
3. help with another question.

Trip planning routes to Consultation Request. Specific-Experience interest
routes to the catalogue so the visitor can select a requestable Experience and
use that Experience's Booking Request. Choosing another question reveals the
General Contact form.

Visible text links preserve an accessible route that does not depend on the
intent control or client-side scripting. The interface must not infer intent
after submission or accept travel-request categories inside General Contact for
staff to reroute manually.

## D-004 — Just-in-Time Privacy and Persistent Message Warning

Beside submission, General Contact explains in concise, plain language that
Greek Essence will save and use the submitted details to handle the question
and reply by email. It links to the full privacy notice and requires an
unchecked “I have read the privacy notice” acknowledgement or an approved
bilingual equivalent.

The acknowledgement records that the notice was presented. It is not blanket
consent and must not be treated as consent to unrelated processing. General
Contact includes no marketing consent; newsletter functionality is excluded
from the product.

Beside the message field, a persistent helper—not placeholder-only text—uses
this approved nine-word English warning:

> Please don’t include passport, payment, or medical information here.

The Greek version must preserve the same concise meaning and receive client
review. If a visitor submits sensitive information despite the warning, the
message remains in the protected private-data workflow. Request Processing and
Communications, with qualified privacy review, must define staff access,
notification content, redaction, deletion, retention, and incident handling.

Before public launch, the client and an appropriately qualified reviewer must
confirm the controller identity and contact details, processing purposes,
applicable lawful basis, recipients or recipient categories, retention period,
visitor rights, complaint route, international-transfer facts where relevant,
and final English and Greek wording against the agency's actual processing.
This decision defines product presentation, not legal approval.

## D-005 — Honest Submission Outcomes and Message Reference

General Contact distinguishes these visitor-visible outcomes:

- **Validation failure:** show field-level errors, preserve the entered message
  for correction, and do not claim receipt.
- **Safely saved message:** state that the message was received, show an opaque,
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
delivery is not the success condition. A generic thank-you page that obscures
whether the message was saved is excluded.

Request Processing and Communications owns exact persistence, transaction and
idempotency boundaries, opaque-reference generation, validation, duplicate
protection, customer and agency email delivery, retry, monitoring, and agency
recovery mechanics while preserving these visible distinctions.

## Explicit Exclusions and Deferrals

- General Contact is not a substitute for Consultation Request or Booking
  Request.
- It does not collect structured trip-planning or specific-Experience request
  information.
- It does not collect a telephone number or contact-method preference.
- Telephone follow-up is not offered by this journey.
- Privacy acknowledgement is not blanket or marketing consent.
- Newsletter functionality and marketing signup are excluded.
- The message field must not invite passport, payment, or medical information.
- No response-time promise is allowed without client approval.
- A saved message is not presented as unsaved because an email fails.
- This feature does not define shared schemas, transaction mechanics,
  idempotency, staff tooling, email infrastructure, monitoring, retention,
  deletion, redaction, recovery, or incident handling.

## Dependencies and Unresolved External Validations

- **Client:** validate the real General Contact purposes, final English and Greek
  intent choices, fields, subject and message guidance, acknowledgement and
  warning wording, alternative contact details, response expectation if one is
  published, and success and failure wording.
- **Client and qualified privacy or legal reviewer:** validate controller facts,
  lawful basis, privacy notice, retention, recipients, rights, transfer facts,
  and handling of sensitive information submitted despite the warning.
- **Catalogue Discovery:** provide the requestable Experience route used for
  specific-Experience intent.
- **Content Operations:** provide approved bilingual journey, form, privacy,
  warning, acknowledgement, success, failure, and email wording.
- **Request Processing and Communications:** define private persistence,
  transaction and idempotency boundaries, opaque references, validation,
  duplicate protection, notification content, email delivery, retry, monitoring,
  staff recovery, access, redaction, deletion, retention, and incident handling.
- **Production Operations:** provide secure configuration, monitoring, recovery,
  and operational ownership before accepting real messages.

These validations may refine approved wording, alternative contact details, and
operational ownership. They must not silently turn General Contact into a
catch-all travel-request form, add unnecessary telephone collection, introduce
broad consent or marketing, create false receipt claims, or encourage duplicate
submissions after a safely saved message.
