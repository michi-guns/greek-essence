# General Contact Grilling

## Status

Queued as feature 5 of 8. Begin after Booking Request is accepted, unless the
operator changes the sequence.

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

None yet. Feature decision IDs begin at D-001.

## Open Questions

- D-001: What belongs in general contact rather than a travel-request form?
- D-002: Which fields and contact channels are required?
- D-003: How should visitors be redirected to a better journey?
- D-004: What privacy and free-text warnings are needed?

## Next Question

ID: D-001

Topic:
The intended use of the general contact form.

Prompt:
Which messages should the Contact page invite, and how should it handle visitors
who actually want trip planning or a specific Experience?

Options:

1. (recommended): **General questions with clear routes to the two travel
   forms.** Accept ordinary agency, partnership, media, or other questions using
   name, email, optional phone, subject, message, and privacy acknowledgement.
   Show prominent links to consultation and booking-request journeys.
2. **Accept every kind of message in Contact.** Keep the dedicated forms but let
   visitors send trip-planning or Experience requests here too. This feels
   flexible but produces incomplete travel enquiries and inconsistent records.
3. **Restrict Contact to business enquiries.** Travel visitors must use the two
   dedicated journeys; Contact is only for partnerships, suppliers, media, or
   administration. This is clearer operationally but may feel unfriendly to a
   traveler with an unusual question.

Why this matters:
A catch-all form is easy to build but can undermine the structured information
the agency needs from the two accepted travel journeys.

After answer:

- Lock the general-contact purpose and routing rule.
- Store D-002 as the next question.
