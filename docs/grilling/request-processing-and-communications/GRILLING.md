# Request Processing and Communications Grilling

## Status

Queued as feature 6 of 8. Begin after the three submission-journey grills are
accepted so their shared needs are known.

This grill does not authorize implementation. Use [../DECISIONS.md](../DECISIONS.md)
and [../protocol.md](../protocol.md).

## Locked Project Context

- Accepted requests must be saved in Neon before they are treated as received.
- Agency notification and visitor acknowledgement use Nodemailer through the
  agency's mail service.
- Notification failure must not destroy a saved request.
- Duplicate protection, privacy, monitoring, and honest recovery behavior are
  required.
- There is no staff dashboard or separate customer-management system at launch.

## Scope

Define shared customer identity and reuse, data contracts, validation, storage,
duplicate protection, request states, email delivery, failure recovery,
retention, deletion, logging, and security boundaries.

## Locked Decisions

### D-001 — Accept After Durable Saving and Recover Email Separately

A valid request is accepted when its private transactional record is durably
committed in Neon. Agency-notification and visitor-acknowledgement delivery are
separate outcomes and cannot turn an accepted request back into an unaccepted
one.

After the commit, the website shows an honest received message and the request
reference required by the owning submission journey. It must not claim that an
email was delivered when delivery is failed or unconfirmed, and it must not ask
the visitor to resubmit an already accepted request. If visitor acknowledgement
delivery fails or cannot be confirmed, the website also explains that email
delivery could not be confirmed.

Each required email outcome is recorded against the accepted request. Failed
agency notification must enter a safe recovery path: retry only when doing so
will not deliberately duplicate a confirmed send, or alert the named
operational owner when delivery is uncertain or recovery cannot complete.
Visitor-acknowledgement failure is also recorded and recoverable without losing
or duplicating the request.

Treating email delivery as part of request acceptance is rejected because it
would present a saved request as failed and encourage duplicate submission.
Ignoring delivery failure is also rejected because a real enquiry could remain
unnoticed.

The normative acceptance and delivery-state boundary is defined in
[contracts/request-acceptance-and-delivery.md](contracts/request-acceptance-and-delivery.md).

### D-002 — Email-Based Contact Relationship with Immutable Request Snapshots

The normalized submitted email address is the internal identifier used to group
requests under the same customer-contact relationship. This supports useful
staff context without introducing customer accounts or asking the visitor to
sign in.

Each accepted request preserves the name, email, and other contact details that
were submitted with that request. A later request must not overwrite an earlier
request's snapshot, and the public forms must not prefill or reveal prior
personal details merely because someone enters the same email address.

Email matching is useful contact evidence, not proof that every request came
from one unique person. A shared family or business inbox can therefore group
several people. Different email addresses remain separate unless staff safely
establish the relationship during manual follow-up; the system must not infer a
merge from similar names, telephone numbers, or other approximate details.

The operator identified the related distinction between a visitor correcting a
bad request and making a new request. D-003 owns that submission-intent and
duplicate boundary; D-002 does not authorize overwriting an accepted request.

The normative recognition boundary is defined in
[contracts/customer-contact-recognition.md](contracts/customer-contact-recognition.md).

## Open Questions

- D-003: How are accidental duplicate submissions handled?
- D-004: What shared request states and audit information are required?
- D-005: How are notification and acknowledgement failures recovered?
- D-006: What retention, deletion, logging, and access rules apply?

## Next Question

ID: D-003

Topic:
Distinguishing a new request, a correction, and an accidental duplicate.

Prompt:
When an email address is used again, how should the visitor distinguish a new
request from a correction without letting either case overwrite accepted
history or exposing that the email already has requests?

Options:

1. (recommended): **New by default; explicit correction with the previous
   reference.** An ordinary submission creates a new request. A visitor who
   chooses “correct a previous request” must provide its opaque reference; the
   correction is saved as a linked record and never overwrites the original.
   Exact transport retries are handled idempotently without creating another
   request. The site never reveals prior requests from email alone.
2. **Ask every time an email is reused.** Require “new request” or “correction”
   whenever the email matches existing records. This sounds direct, but revealing
   that a match exists leaks private relationship data, while asking without
   revealing a match adds friction to ordinary new requests.
3. **Infer the intent automatically.** Treat sufficiently similar submissions
   as corrections and different ones as new requests. This reduces questions but
   can overwrite intent, hide a legitimate second booking request, or attach a
   correction to the wrong request.

Why this matters:
The agency needs to know whether to act on both requests, but an accepted
request may already have triggered manual work. Keeping history and requiring
the opaque reference for corrections avoids silent replacement and prevents
email-address probing from exposing prior activity.

After answer:

- Lock new-request, correction, and exact-retry behavior.
- Update the shared contract with the accepted relationship and immutability
  rules.
- Store D-004 as the next question.
