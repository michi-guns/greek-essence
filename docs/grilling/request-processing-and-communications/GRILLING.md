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

None yet. Feature decision IDs begin at D-001.

## Open Questions

- D-001: When is a submitted request considered accepted?
- D-002: How are repeated customers recognized without accounts?
- D-003: How are accidental duplicate submissions handled?
- D-004: What shared request states and audit information are required?
- D-005: How are notification and acknowledgement failures recovered?
- D-006: What retention, deletion, logging, and access rules apply?

## Next Question

ID: D-001

Topic:
The acceptance boundary between database saving and email delivery.

Prompt:
If Neon saves a valid request but the agency email cannot be sent immediately,
what should the website tell the visitor and what must happen next?

Options:

1. (recommended): **Accept after durable saving and record email for recovery.**
   Show an honest received message after the database commit, store notification
   status, retry safely or alert the named owner, and never send a duplicate
   agency email for the same request. Visitor acknowledgement failure is also
   recorded without losing the accepted request.
2. **Treat agency email delivery as part of acceptance.** If the email fails,
   show a retryable failure even though the request remains saved. This makes
   notification central but creates confusing retries and duplicate risk.
3. **Save and ignore delivery failure.** Show success once saved and rely on
   technical staff to discover email problems later. This is simple but can
   leave a real enquiry unnoticed.

Why this matters:
Database saving protects the visitor's information; notification makes the
agency act on it. The product needs an honest rule when only one succeeds.

After answer:

- Lock the acceptance and recovery boundary.
- Create a normative shared request-state and delivery contract if accepted.
- Store D-002 as the next question.
