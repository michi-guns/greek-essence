# Request Acceptance and Delivery Contract

## Authority and Scope

This contract is normative for Request Processing and Communications D-001. It
defines the shared acceptance boundary and the minimum delivery-state behavior
for Consultation Requests, Booking Requests, and General Contact messages.

It does not authorize implementation or choose a database schema, queue,
scheduler, mail provider, retry count, or monitoring product. Later decisions
own detailed shared states, recovery operations, retention, access, and
production monitoring.

## Acceptance Boundary

1. A submission is not accepted until all data required for its private request
   record is durably committed in Neon.
2. The successful commit is the acceptance event. Later email outcomes cannot
   revoke, delete, or rewrite that accepted state.
3. If the commit fails, the request is not accepted and no email outcome may be
   presented as proof of receipt.
4. Agency notification and visitor acknowledgement begin only for an accepted
   request and remain traceable to that request's opaque reference.

## Required Delivery Records

For each accepted request, independently record the outcome of:

- the agency notification; and
- the visitor acknowledgement.

Each outcome must distinguish at least:

- delivery work still pending or not yet confirmed;
- a confirmed handoff to the configured mail service; and
- failed delivery work requiring retry, owner attention, or later recovery.

A mail-service handoff is not proof that the recipient read or ultimately
received the message. Customer-facing wording must not overstate that fact.

## Visitor-Visible Outcomes

- After the durable commit, show that the request was received and show the
  owning journey's opaque request reference.
- Never describe an accepted request as unreceived merely because either email
  outcome failed or remains unconfirmed.
- Never ask the visitor to resubmit an accepted request to repair email
  delivery.
- Do not claim that staff or the visitor were emailed when the corresponding
  delivery is failed or unconfirmed.
- When visitor-acknowledgement delivery fails or cannot be confirmed during the
  submission outcome, explain that the request was received but email delivery
  could not be confirmed.

## Recovery and Duplicate-Send Boundary

- A failed or pending agency notification must remain visible to operational
  recovery until it is resolved or explicitly handed to the named owner.
- A definitely failed send receives a bounded number of automatic retries using
  a stable request-and-purpose identity.
- A confirmed handoff must not be deliberately redispatched.
- An uncertain mail handoff stops blind automatic retry because the provider may
  already have accepted the message.
- Exhausted or uncertain delivery alerts a named recovery owner through a
  separately monitored route that does not depend solely on the failing agency
  mail path.
- The alert contains only the opaque request reference, email purpose, failure
  category, and minimum diagnostic context. It excludes request content, notes,
  messages, and visitor contact details.
- Every attempt, escalation, authorized recovery action, and outcome is appended
  to the D-004 audit history.
- Visitor-acknowledgement failure follows the same recorded recovery principle
  but never changes request acceptance or prompts resubmission.

Before real enquiries are accepted, name and test the retry count and timing,
recovery owner, separate alert route, and response procedure. D-006 owns
retention and access to the resulting delivery history.