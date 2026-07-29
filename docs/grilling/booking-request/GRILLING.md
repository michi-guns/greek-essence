# Booking Request Grilling

## Status

Ready to begin as feature 4 of 8. Consultation Request is accepted and
distilled.

This grill does not authorize implementation. Use [../DECISIONS.md](../DECISIONS.md)
and [../protocol.md](../protocol.md).

## Locked Project Context

- A booking request expresses interest in one eligible Experience.
- It does not reserve availability, confirm a booking, or take payment.
- The agency checks the request and follows up manually.
- Eligibility is defined by the Catalogue Discovery grill.

## Scope

Define the required Experience context, visitor fields, date and party details,
non-confirming wording, agency handoff, and success, failure, and duplicate
behavior for booking requests.

## Locked Decisions

### D-001 — Minimum useful booking-request information

The selected Experience is carried automatically. The visitor provides one
preferred date, with an optional alternative date or flexible-date indication;
party size split into adults and children where relevant; contact details;
preferred contact method; an optional notes field; and privacy acknowledgement.

This gives the agency enough context to begin checking the relevant Experience
and supplier conditions without turning the booking request into a broader trip
consultation or implying availability, reservation, or confirmation.

Dependencies:

- Catalogue Discovery owns whether an Experience is requestable and supplies the
  selected Experience context.
- Request Processing and Communications will define shared contact handling,
  validation, privacy, persistence, notification, and recovery behavior.

Rejected alternatives:

- Contact details alone would create avoidable follow-up before the agency can
  investigate the request.
- Accommodation, transport, budget, and wider itinerary questions belong in the
  separate consultation journey.

### D-002 — Repeated non-confirming wording

The journey must explain at every key decision and confirmation point that a
booking request is only a request, does not reserve the Experience, and does not
confirm availability. The agency will check the request and follow up.

Required placements:

- near the form introduction;
- beside the submit action;
- in the saved-request acknowledgement shown to the visitor; and
- in the verification or acknowledgement email sent to the customer.

Repeating concise wording is intentional: the visitor must receive the correct
expectation before acting and retain it after submission across both on-screen
and email communication.

Dependencies:

- Content Operations owns approved English and Greek wording.
- Request Processing and Communications owns the customer email trigger,
  delivery, failure handling, and recovery behavior.
- Booking Request success messaging must distinguish a safely saved request from
  availability, reservation, or confirmation.

Rejected alternatives:

- A single notice beside the submit action is too easy to miss before and after
  submission.
- Explaining the distinction only after submission allows the visitor to act
  under the wrong expectation.

### D-003 — Structured dates, party composition, and bounded needs

The visitor must provide one preferred date and may provide either one
alternative date or indicate that their dates are flexible. The request must
record the adult count and, when children are included, the child count.

The form may include one short optional field for accessibility or practical
needs. It must carry a persistent warning not to include medical, passport, or
payment information. The initial booking request must not collect individual
traveler ages, health details, or another detailed traveler breakdown.

This structure gives the agency enough consistent information to investigate the
Experience while avoiding an early detailed questionnaire and disproportionate
collection of personal or sensitive information.

Dependencies:

- Privacy and qualified review must validate the field wording, handling, access,
  retention, and later follow-up process.
- Request Processing and Communications owns validation, storage, notification,
  and safe rendering of visitor-provided text.
- Catalogue and Experience rules may later establish when child counts or other
  practical details are relevant, without expanding this initial request into a
  traveler dossier.

Rejected alternatives:

- A mostly free-text representation would be harder to validate and hand off
  reliably.
- A per-traveler age, mobility, dietary, or health breakdown would collect too
  much potentially sensitive information at the initial request stage.

### D-004 — Disable new requests while preserving accepted requests

The server must revalidate the selected Experience when the visitor submits. If
it no longer exists or is no longer requestable, the system must not save a new
booking request. It must explain that the Experience can no longer be requested
and offer appropriate catalogue or consultation paths.

If the request was already safely saved before the agency changed or disabled
the Experience, the request remains intact. Preserve the Experience identifier
and a bounded snapshot of the customer-visible Experience information needed to
understand what the visitor originally requested. Expose that the linked live
Experience is now disabled so the agency can follow up manually, explain the
change, and offer an alternative where appropriate.

Disabling an Experience must not silently rewrite, detach, delete, reject, or
automatically cancel an already accepted request. The original acknowledgement
continues to prove only that a request was received; it never proves
availability, reservation, or confirmation.

Dependencies:

- Catalogue Discovery owns requestability and withdrawal behavior.
- Request Processing and Communications owns persistence, agency visibility,
  customer follow-up, notification, and recovery mechanics.
- The later data contract must define the minimal historical Experience snapshot
  without copying unnecessary mutable catalogue content.

Rejected alternatives:

- Accepting new requests for a disabled Experience creates knowingly impossible
  or misleading work.
- Automatically rejecting, deleting, or detaching existing requests loses
  historical meaning and bypasses appropriate agency review and communication.
- Resolving a saved request only through its live Experience record could rewrite
  what the visitor originally requested.

## Open Questions

- D-005: What does the visitor see after success or failure?

## Next Question

ID: D-005

Topic:
What the visitor sees when validation, persistence, or customer-email delivery
succeeds or fails.

Prompt:
Which success and failure outcomes should the booking-request journey show?

Options:

1. (recommended): **Distinguish validation, saved, email-failure, and unsaved
   outcomes.** Show field-level validation without submission; after a safely
   saved request, show a non-confirming acknowledgement and opaque reference; if
   the customer email fails, keep the saved request and honestly say that email
   delivery could not be confirmed without asking the visitor to resubmit; if
   saving fails, say the request was not received and allow a safe retry.
2. **Use one generic success and one generic error.** This is simpler but cannot
   honestly distinguish a saved request from email delivery or persistence
   failure.
3. **Treat customer-email delivery as the success condition.** Show success only
   when both saving and email complete; otherwise ask the visitor to resubmit.
   This risks duplicate requests when saving succeeded but email failed.

Why this matters:
Saving the request and sending email are separate responsibilities. The visitor
must know whether the agency actually received the request without being given a
false booking confirmation or creating duplicates through unnecessary retries.

After answer:

- Lock the visitor-visible success and failure outcomes.
- Record persistence, duplicate-protection, email, monitoring, and recovery
  dependencies for the shared Request Processing and Communications grill.
- Assess whether any material Booking Request question remains before proposing
  acceptance and distillation.
