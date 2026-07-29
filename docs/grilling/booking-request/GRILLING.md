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

## Open Questions

- D-003: How are dates, party size, and special needs represented?
- D-004: What happens if the Experience changes or is unpublished?
- D-005: What does the visitor see after success or failure?

## Next Question

ID: D-003

Topic:
How the request represents dates, party size, and accessibility or other special
needs without collecting unnecessary sensitive information.

Prompt:
How should the booking-request form capture dates, party composition, and
special requirements?

Options:

1. (recommended): **Structured essentials with a bounded optional needs field.**
   Require one preferred date; allow either one alternative date or a flexible
   dates choice; require adult count and, when children are included, child
   count; provide an optional short accessibility or practical-needs field with
   a warning not to include medical, passport, or payment information.
2. **Mostly free text.** Ask for party size and timing in one notes field. This
   is flexible but harder to validate, search, and hand off reliably.
3. **Detailed traveler breakdown.** Collect each traveler’s age, mobility,
   dietary, and health information. This may help later planning but collects
   disproportionate personal and potentially sensitive data too early.

Why this matters:
The agency needs enough structured information to investigate the Experience,
but an initial request should not become a detailed traveler questionnaire or
collect sensitive data before it is necessary.

After answer:

- Lock the date, party, and special-requirements model.
- Record privacy, catalogue, and shared-processing dependencies.
- Store D-004 as the next question.
