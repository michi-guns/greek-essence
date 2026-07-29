# Consultation Request Grilling

## Status

Queued as feature 3 of 8. Begin after Catalogue Discovery is accepted, unless
the operator changes the sequence.

This grill does not authorize implementation. Use [../DECISIONS.md](../DECISIONS.md)
and [../protocol.md](../protocol.md).

## Locked Project Context

- A consultation request asks the agency to help plan a trip.
- The agency follows up manually by email or telephone.
- Online payment, a post-enquiry questionnaire, and automated scheduling are
  deferred.
- Real requests must be saved safely and handled as private personal data.

## Scope

Define the visitor goal, minimum useful information, consent and privacy
language, confirmation wording, manual handoff, and reachable error and retry
behavior for consultation requests.

## Locked Decisions

None yet. Feature decision IDs begin at D-001.

## Open Questions

- D-001: How much trip information belongs in the initial request?
- D-002: Which contact method and response expectation are offered?
- D-003: Which fields are required, optional, or avoided?
- D-004: What consent and privacy explanation is needed?
- D-005: What does the visitor see after success or failure?

## Next Question

ID: D-001

Topic:
The amount of information collected before the agency responds.

Prompt:
What should the first consultation form ask so the agency can respond usefully
without turning it into the detailed questionnaire that we postponed?

Options:

1. (recommended): **A short structured trip brief.** Ask for contact details,
   approximate travel timing, party size, destinations or interests, optional
   budget guidance, a short notes field, preferred contact method, and required
   privacy acknowledgement.
2. **A simple callback request.** Ask only for name, contact details, preferred
   contact method, and a short message. The agency gathers all travel details
   during follow-up.
3. **A detailed planning intake.** Ask for accommodation, transport, daily
   preferences, accessibility needs, and other detailed trip information at the
   first contact. This gives the agency more information but approaches the
   deferred questionnaire and increases abandonment and sensitive-data risk.

Why this matters:
Too little information creates extra email exchanges; too much makes the first
contact tiring and may collect personal details before the agency needs them.

After answer:

- Lock the initial information depth.
- Identify sensitive or deferred fields.
- Store D-002 as the next question.
