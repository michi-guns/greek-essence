# Booking Request Decisions

## Status and Authority

Accepted by the operator on 2026-07-29 after feature grilling.

This document defines the Public Preview Release boundary for requesting one specific eligible Experience, the minimum visitor information, repeated non-confirming wording, date and party representation, handling of changed or disabled Experiences, and visitor-visible submission outcomes.

It does not authorize application implementation, dependency installation, schema migration, deployment, or destructive path changes. Those require later promoted canonical documentation and explicit bounded implementation contracts.

Use the project terms in [../GLOSSARY.md](../GLOSSARY.md). The accepted project boundary remains in [../DECISIONS.md](../DECISIONS.md), and Experience requestability remains owned by [Catalogue Discovery](../catalogue-discovery/DECISIONS.md).

## Feature Boundary

A Booking Request expresses interest in one requestable Experience. It does not reserve the Experience, prove availability, confirm a booking, or take payment. The agency investigates the request and follows up manually.

Every accepted request is private transactional data. “Received” means that the request was safely saved. Customer and agency email delivery are separate outcomes.

## D-001 — Minimum Useful Booking-Request Information

The selected Experience is carried automatically. The visitor provides:

- one preferred date;
- either one optional alternative date or a flexible-date indication;
- adult count and, when children are included, child count;
- contact details;
- preferred contact method;
- optional notes;
- the bounded optional needs information refined by D-003; and
- privacy acknowledgement.

This gives the agency enough context to begin checking the relevant Experience and supplier conditions without recreating the broader Consultation Request. Contact details alone are insufficient because they create avoidable follow-up. Accommodation, transport, budget, and wider itinerary questions remain in the consultation journey.

Catalogue Discovery owns whether an Experience is requestable and supplies the selected Experience context. Request Processing and Communications owns shared contact handling, validation, privacy, persistence, notification, duplicate protection, and recovery behavior.

## D-002 — Repeated Non-Confirming Wording

The journey must state that a Booking Request is only a request, does not reserve the Experience, and does not confirm availability. It must explain that the agency will check the request and follow up.

Concise non-confirming wording is required:

- near the form introduction;
- beside the submit action;
- in the saved-request acknowledgement shown to the visitor; and
- in the verification or acknowledgement email sent to the customer.

Repeating the distinction is intentional. A notice only at submission or only after submission is insufficient because the visitor could act or retain the acknowledgement under the wrong expectation.

Content Operations owns approved English and Greek wording. Request Processing and Communications owns the customer-email trigger, delivery, failure handling, and recovery behavior.

## D-003 — Structured Dates, Party Composition, and Bounded Needs

The visitor must provide one preferred date and may provide either one alternative date or indicate that dates are flexible. The request records adult count and, when children are included, child count.

The form may include one short optional field for accessibility or practical needs. A persistent warning must tell visitors not to include medical, passport, or payment information. The initial request must not collect individual traveler ages, health details, or a detailed traveler breakdown.

A mostly free-text representation is excluded because it is harder to validate and hand off reliably. Per-traveler age, mobility, dietary, or health collection is excluded because it is disproportionate and potentially sensitive at this stage.

Privacy and qualified review must validate the final field wording, handling, access, retention, and later follow-up. Request Processing and Communications owns validation, storage, notification, and safe rendering of visitor-provided text. Later catalogue rules may identify when child counts or practical details are relevant without expanding the request into a traveler dossier.

## D-004 — Disable New Requests While Preserving Accepted Requests

The server must revalidate the selected Experience when the visitor submits. If it no longer exists or is no longer requestable, the system must not save a new Booking Request. It must explain that the Experience can no longer be requested and offer appropriate catalogue or Consultation Request paths.

If a request was safely saved before the agency changed or disabled the Experience, the request remains intact. Preserve the Experience identifier and a bounded snapshot of the customer-visible information required to understand what the visitor originally requested. Expose that the live Experience is now disabled so the agency can review the request, explain the change, and offer an alternative where appropriate.

Disabling an Experience must not silently rewrite, detach, delete, reject, or automatically cancel an accepted request. The original acknowledgement proves only that a request was received; it never proves availability, reservation, or confirmation.

Catalogue Discovery owns requestability and withdrawal behavior. Request Processing and Communications owns persistence, agency visibility, customer follow-up, notification, and recovery mechanics. A later data contract must define the smallest useful historical snapshot without copying unnecessary mutable catalogue content.

## D-005 — Honest Submission Outcomes and Request Reference

The journey distinguishes these visitor-visible outcomes:

- **Validation failure:** show field-level errors and do not claim submission.
- **Safely saved request:** show a non-confirming acknowledgement and an opaque, non-sensitive reference that reveals no personal data or sequential private-record details.
- **Safely saved request with failed or unconfirmed customer-email delivery:** preserve the accepted request, show the saved-request truth and reference, and honestly explain that email delivery could not be confirmed. Do not ask the visitor to resubmit.
- **Persistence failure:** state that the request was not received and allow a safe retry without exposing technical details.

Saving and email delivery are separate responsibilities. A later email failure must not erase or misrepresent an accepted request. Treating customer-email delivery as the success condition is excluded because it could encourage a duplicate submission after the request was already saved.

Request Processing and Communications owns transaction boundaries, idempotency, duplicate protection, reference generation, customer and agency email delivery, monitoring, retry, recovery, and agency notification behavior. Content Operations owns approved localized wording. Security and privacy review must ensure references and errors reveal no customer data or internal identifiers.

## Explicit Exclusions and Deferrals

- A Booking Request is not a reservation, availability confirmation, confirmed booking, payment, or broader trip-planning consultation.
- It does not collect accommodation, transport, budget, wider itinerary, individual traveler identity, detailed age, medical, passport, payment, or detailed health information.
- New requests are not accepted for a disabled or unrequestable Experience.
- Disabling an Experience does not automatically cancel, reject, rewrite, detach, or delete accepted requests.
- A saved request is not lost or presented as unsaved because an email fails.
- This feature does not define shared schemas, transaction mechanics, idempotency, staff tooling, email infrastructure, monitoring, retention, deletion, redaction, recovery, or incident handling.

## Dependencies and Unresolved External Validations

- **Client:** validate the real booking-request workflow, preferred contact choices, customer communication, practical-needs wording, alternative paths, and final English and Greek form, acknowledgement, email, warning, success, and failure wording.
- **Client and qualified privacy or legal reviewer:** validate privacy-notice and acknowledgement facts, lawful handling and retention, free-text safeguards, and treatment of potentially sensitive information submitted despite the warning.
- **Catalogue Discovery:** provide authoritative Experience identity, requestability, withdrawal behavior, and the customer-visible source for the bounded historical snapshot.
- **Content Operations:** provide approved bilingual Experience and journey wording.
- **Request Processing and Communications:** define private persistence, transaction and idempotency boundaries, opaque references, validation, duplicate protection, email delivery, notification content, retry, monitoring, agency recovery and follow-up, access, redaction, deletion, retention, and incident handling.
- **Production Operations:** provide secure configuration, monitoring, recovery, and operational ownership before accepting real enquiries.

These validations may refine controlled values, approved wording, the minimal historical snapshot, and operational ownership. They must not silently turn a request into a reservation, broaden early personal-data collection, accept new requests for disabled Experiences, destroy historical meaning, or create false receipt and email claims.
