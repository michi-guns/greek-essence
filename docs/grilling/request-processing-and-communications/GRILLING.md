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

## Open Questions

- D-002: How are repeated customers recognized without accounts?
- D-003: How are accidental duplicate submissions handled?
- D-004: What shared request states and audit information are required?
- D-005: How are notification and acknowledgement failures recovered?
- D-006: What retention, deletion, logging, and access rules apply?

## Next Question

ID: D-002

Topic:
Recognizing repeated customer contact without introducing accounts.

Prompt:
When the same person submits another request without an account, how should the
system recognize the relationship without silently merging different people?

Options:

1. (recommended): **Link by the same normalized email while preserving each
   request's submitted contact snapshot.** Give staff the relationship as useful
   context, but do not expose an account, prefill personal details, or overwrite
   what was submitted with an earlier request. Different email addresses remain
   separate unless staff establish the relationship during manual follow-up.
2. **Keep every request completely independent.** Never create a shared customer
   relationship. This minimizes identity assumptions but makes repeated context,
   privacy requests, retention, and staff follow-up harder to reconcile.
3. **Automatically merge using several matching details.** Combine requests
   when email, name, telephone, or similar details appear to identify the same
   person. This may join changed addresses, but risks merging family members,
   shared inboxes, or coincidentally similar visitors.

Why this matters:
Without accounts, an email address is useful contact evidence but not proof of a
unique person. A wrong merge could expose one visitor's request history during
staff follow-up or a privacy request; no linking at all creates avoidable agency
work and fragmented records.

After answer:

- Lock the customer-recognition and request-snapshot boundary.
- Update the shared contract if the answer creates a normative identity rule.
- Store D-003 as the next question.
