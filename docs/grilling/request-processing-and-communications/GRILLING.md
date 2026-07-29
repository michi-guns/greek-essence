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

### D-003 — Immutable Chronological History with Explicit Corrections

Every accepted submission creates or resolves to one immutable request record
in the chronological history grouped by the D-002 normalized email
relationship. An ordinary submission is a new request by default. Similar
content, timing, or contact details must not silently turn it into a correction
or replacement.

A visitor who intends to correct a previous request explicitly chooses the
correction path and supplies that request's opaque reference. The submitted
email must resolve to the same contact relationship without revealing whether a
different email or reference exists. A valid correction creates a new record
linked to the earlier request; it never overwrites, deletes, or detaches the
original record.

The chronology preserves each request's reference, type, submitted snapshot,
acceptance time, explicit correction relationship when applicable, and the
processing and delivery-state history defined by later decisions. Exact
technical retries of one submission resolve idempotently to the same accepted
request rather than creating another history entry.

The chronology is internal agency context, not a customer account or public
request-history page. Automatic intent inference and email-reuse prompts are
rejected because they could hide a legitimate additional request, attach a
correction incorrectly, add friction, or expose prior activity.

The normative chronology, correction, and exact-retry boundary is defined in
[contracts/request-history-and-duplicates.md](contracts/request-history-and-duplicates.md).

## Open Questions

- D-004: What shared request states and audit information are required?
- D-005: How are notification and acknowledgement failures recovered?
- D-006: What retention, deletion, logging, and access rules apply?

## Next Question

ID: D-004

Topic:
Shared request states and audit information without a staff dashboard.

Prompt:
Since launch has no staff dashboard or customer-management system, which states
should the website own and audit while the agency follows up through its
existing email process?

Options:

1. (recommended): **Audit system-owned states only; keep manual handling in the
   agency inbox.** Record durable acceptance, correction links, and independent
   agency-notification and visitor-acknowledgement outcomes with timestamps and
   source. Do not claim “in progress,” “resolved,” or “closed” in the website
   database when staff have no supported way to maintain those states.
2. **Add a small secure staff state-control surface.** Let staff mark requests
   as new, in progress, resolved, or closed while retaining the system-delivery
   audit. This gives stronger operational visibility but introduces the staff
   tooling explicitly deferred from launch.
3. **Create staff lifecycle states without a supported interface.** Store new,
   in-progress, resolved, and closed states and expect technical staff or direct
   database work to maintain them. This appears complete but creates hidden,
   unsafe agency work and will quickly become inaccurate.

Why this matters:
An audit field is useful only if a named process keeps it truthful. The accepted
release sends requests into the agency's existing mailbox and explicitly defers
a staff dashboard, so invented staff lifecycle states could mislead recovery,
privacy handling, and future reporting.

After answer:

- Lock system-owned request and delivery states plus minimum audit history.
- Update the shared request contract if accepted.
- Store D-005 as the next question.
