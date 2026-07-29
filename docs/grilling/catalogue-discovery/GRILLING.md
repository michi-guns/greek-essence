# Catalogue Discovery Grilling

## Status

Ready to begin as feature 2 of 8. Public Brand Pages is accepted and distilled.

This grill does not authorize implementation. Use [../DECISIONS.md](../DECISIONS.md)
and [../protocol.md](../protocol.md).

## Locked Project Context

- Visitors browse destination and Experience lists and detail pages.
- Catalogue text search and useful filters are required.
- A booking request expresses interest and never confirms a booking.
- Articles, Accommodation pages, and Attraction pages are deferred unless
  client validation proves a launch need.
- Live supplier availability and confirmed online booking are deferred.

## Scope

Define catalogue concepts, requestable entries, search and filters, detail-page
truthfulness, content relationships, empty or unavailable states, and the
boundary with booking requests.

## Locked Decisions

None yet. Feature decision IDs begin at D-001.

## Open Questions

- D-001: Which published Experiences may receive a booking request?
- D-002: Which Experience types are required at launch?
- D-003: Which search targets and filters are genuinely useful?
- D-004: What price and availability wording is permitted?
- D-005: What happens when content is unpublished or incomplete?

## Next Question

ID: D-001

Topic:
Which Experiences can show a request-to-book action.

Prompt:
How should the catalogue decide whether a visitor may send a booking request
for a particular Experience?

Options:

1. (recommended): **The editor marks each eligible Experience as requestable.**
   Published content may be useful inspiration without accepting booking
   requests. Eligible entries show a clearly non-confirming request action.
2. **Every published Experience is requestable.** Publishing automatically
   enables a booking request, so editors must never publish inspiration-only or
   unavailable entries as Experiences.
3. **Eligibility follows the Experience type.** For example, all Tours and
   Activities accept requests while other types never do. This is easy to
   explain but cannot handle exceptions within a type.

Why this matters:
An editor may want to publish useful inspiration before the agency is ready to
handle requests for it. A wrong request button creates visitor expectations and
manual work the agency may be unable to fulfill.

After answer:

- Lock the eligibility rule.
- Record its content and booking-request dependency.
- Store D-002 as the next question.
