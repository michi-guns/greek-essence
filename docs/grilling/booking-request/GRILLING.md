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

## Open Questions

- D-004: What happens if the Experience changes or is unpublished?
- D-005: What does the visitor see after success or failure?

## Next Question

ID: D-004

Topic:
What happens when the selected Experience changes or becomes unrequestable
before or after the visitor submits the request.

Prompt:
How should the booking-request journey behave if the Experience changes or is
unpublished?

Options:

1. (recommended): **Revalidate before saving and preserve a historical
   snapshot after saving.** At submission, verify that the Experience still
   exists and is requestable. If not, do not save a new booking request; explain
   that it can no longer be requested and offer catalogue or consultation paths.
   Once a request is safely saved, retain the Experience identifier and the
   customer-visible title/details needed to understand the historical request,
   even if the live Experience later changes or is withdrawn.
2. **Always accept against the remembered Experience.** Save the request even if
   the Experience is no longer requestable and let staff resolve it manually.
   This avoids blocking visitors but creates misleading or impossible requests.
3. **Keep only a live Experience link.** Reject unavailable Experiences before
   submission, but let saved requests display whatever the current Experience
   says. This is simpler but can rewrite the meaning of historical requests.

Why this matters:
Catalogue decisions already require withdrawn Experiences to disappear from new
discovery while preserving historical request intelligibility. The booking
journey must prevent stale submissions without losing what an accepted request
originally referred to.

After answer:

- Lock pre-submit revalidation and post-save historical behavior.
- Record catalogue, persistence, and recovery dependencies.
- Store D-005 as the next question.
