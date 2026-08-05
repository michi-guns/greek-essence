# System Boundaries and Domain Representation Grill

## Status and Authority

Active — D-001 is open.

This Foundation Design grill realizes accepted product behavior without changing
what Greek Essence promises visitors. It does not authorize implementation,
Neon/Drizzle configuration, schema migration, dependency installation, or real
data processing.

The locked stack is Next.js, Sanity for editable public and catalogue content,
and Neon PostgreSQL with Drizzle for private request data. The open questions are
technical boundaries, not provider selection.

## Accepted Inputs

- Booking Request is an expression of interest in one requestable Experience; it
  neither reserves nor confirms availability.
- Catalogue Discovery owns whether an Experience is requestable.
- A new Booking Request must be rejected if the selected Experience no longer
  exists or is no longer requestable when submitted.
- A request safely accepted before a later Experience withdrawal remains intact
  and retains a bounded customer-visible snapshot sufficient to explain what was
  originally requested.
- Public editable Experience content belongs in Sanity; private accepted requests
  belong in Neon.

## Decision Sequence

1. D-001 — authoritative Experience eligibility at Booking Request acceptance.
2. D-002 — immutable accepted-request context and bounded snapshot principle.
3. D-003 — request-family identity and typed-detail boundary.
4. D-004 — cross-service identity and withdrawal-safe relationships.

## D-001 — Authoritative Experience Eligibility at Booking Request Acceptance

### Problem

A visitor can open an Experience page while it is requestable, but staff can
withdraw that Experience before the visitor submits the Booking Request. Greek
Essence must decide which source is trusted at the acceptance moment so it never
saves a new request for something the agency has withdrawn, while still keeping
previously accepted requests meaningful.

### Concrete workflow

A visitor opens “Naxos food walk” and starts a request. Before submission, the
agency withdraws the Experience in Sanity. On submission, the trusted server
checks the current Sanity Experience record. If it is absent or no longer
requestable, the request is not saved and the visitor is told honestly that it
can no longer be requested. If it remains requestable, Greek Essence accepts the
private request in Neon and later preserves the original customer-visible context
needed for agency follow-up.

### Options

1. **(recommended): Sanity remains the live authority at submission.** The server
   reads the current selected Experience from Sanity at acceptance and permits a
   new Booking Request only when that record exists and is requestable. Neon holds
   private accepted requests, not a competing eligibility flag. This follows the
   accepted ownership boundary and avoids a second source that could drift.
2. **Copy eligibility into Neon and check that copy at submission.** This permits
   request acceptance without a live Sanity check, but requires a reliable
   synchronization rule and a clear answer for what happens when Sanity and Neon
   disagree.
3. **Trust the Experience details sent by the browser.** This avoids a server-side
   content read but could accept a request after withdrawal. It conflicts with
   the accepted requirement to revalidate selected Experiences at submission and
   is included only to make the unsafe boundary explicit.

### After Answer

Record the accepted authority and failure behavior, then ask D-002. Exact cache,
query, token, transaction, schema, and module mechanics remain downstream.
