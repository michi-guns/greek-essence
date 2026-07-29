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

## Open Questions

- D-002: What wording prevents a confirmation misunderstanding?
- D-003: How are dates, party size, and special needs represented?
- D-004: What happens if the Experience changes or is unpublished?
- D-005: What does the visitor see after success or failure?

## Next Question

ID: D-002

Topic:
Clear wording that prevents a booking request from being mistaken for a
reservation or confirmed booking.

Prompt:
Where and how should the journey explain that submitting the request does not
reserve the Experience or confirm availability?

Options:

1. (recommended): **Repeat concise non-confirming wording at the key decision
   points.** Explain it near the form introduction, beside the submit action,
   and in the saved-request acknowledgement: this is a request only, nothing is
   reserved or confirmed, and the agency will check and follow up.
2. **Use one detailed notice beside the submit action.** This reduces repetition
   but makes the distinction easier to miss earlier in the journey and after
   submission.
3. **Explain it only in the acknowledgement.** This keeps the form visually
   lighter but allows visitors to submit under the wrong expectation.

Why this matters:
A visitor may otherwise interpret “booking request” or a successful submission
as a reservation. The wording must set the correct expectation before the
visitor acts and preserve it after the request is saved.

After answer:

- Lock the non-confirming wording and its required placements.
- Record catalogue, content, and shared-communications dependencies.
- Store D-003 as the next question.
