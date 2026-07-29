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

None yet. Feature decision IDs begin at D-001.

## Open Questions

- D-001: What information makes a booking request useful to the agency?
- D-002: What wording prevents a confirmation misunderstanding?
- D-003: How are dates, party size, and special needs represented?
- D-004: What happens if the Experience changes or is unpublished?
- D-005: What does the visitor see after success or failure?

## Next Question

ID: D-001

Topic:
The minimum useful request for one Experience.

Prompt:
What should a visitor provide when asking about a specific Experience?

Options:

1. (recommended): **Experience, preferred date, party size, and contact
   details.** Carry the selected Experience automatically; ask for one preferred
   date, an optional alternative or flexible-date indication, adults and
   children where relevant, contact details, optional notes, preferred contact
   method, and privacy acknowledgement.
2. **Contact details only.** Carry the Experience automatically and let the
   agency collect date and party details during follow-up. This is shorter but
   creates more manual exchanges before availability can be checked.
3. **A broader trip request.** Add accommodation, transport, budget, and wider
   itinerary questions. This may help with cross-selling but blurs the boundary
   with the separate consultation journey.

Why this matters:
The agency needs enough information to check the right supplier conditions,
while the form must remain clearly different from a confirmed booking.

After answer:

- Lock the initial booking-request information.
- Record catalogue and shared-processing dependencies.
- Store D-002 as the next question.
