# Request Processing and Communications Grilling

## Status

Accepted through D-006 by the operator on 2026-07-30, then reopened only for
D-007 after distillation review found a material interaction between correction
history and per-request deletion. Do not remove this ledger or finalize
`DECISIONS.md` until D-007 is settled and the complete grill is accepted again.

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

### D-004 — Audit System-Owned States Only

The website records only states it can keep truthful without staff workflow
tooling: durable request acceptance, explicit correction relationships, and the
independent agency-notification and visitor-acknowledgement outcomes. Each state
transition retains its time and whether it came from the submission flow,
automated recovery, or a named authorized recovery action.

The website database does not claim that agency handling is new, in progress,
resolved, or closed. Those lifecycle states remain in the agency's existing
email process for launch because no staff dashboard or customer-management
system is accepted. Direct database maintenance by technical staff is not a
substitute for a supported agency workflow.

The audit must preserve the accepted request's immutable reference, type,
acceptance time, contact relationship, submitted snapshot, correction link, and
delivery history without copying unnecessary personal or free-text data into
logs. D-005 owns detailed delivery recovery; D-006 owns retention, deletion,
access, and logging limits.

Adding even a small staff state-control surface is deferred with the staff
dashboard. Creating lifecycle fields that nobody can reliably maintain is
rejected because inaccurate states would mislead recovery, privacy handling,
and future reporting.

The normative state and audit boundary is defined in
[contracts/system-states-and-audit.md](contracts/system-states-and-audit.md).

### D-005 — Bounded Safe Retry with Out-of-Band Escalation

Definitely failed agency notifications and visitor acknowledgements receive a
bounded number of automatic retries using the stable request-and-purpose
identity established by D-001. A confirmed handoff is not retried. An uncertain
handoff stops blind automatic retry because the mail service may already have
accepted the message.

When retries are exhausted or delivery remains uncertain, the system alerts a
named recovery owner through a separately monitored route that does not depend
solely on the failing agency mail path. The alert contains only the opaque
request reference, email purpose, failure category, and minimum diagnostic
context; it does not copy the visitor's request, message, notes, or contact
details.

The recovery owner decides the bounded next action for uncertain delivery and
ensures that a failed agency notification does not leave an accepted request
unnoticed. Every automated attempt, escalation, authorized recovery action, and
final outcome is appended to the D-004 audit history. Recovery never changes
request acceptance and never asks the visitor to resubmit.

The exact retry count and timing, recovery owner, separately monitored alert
channel, and operational response procedure must be named and tested before
real enquiries are accepted. Immediate manual handling for every definite
failure is rejected as avoidable workload; unbounded retry is rejected because
it can create delayed duplicates and ownerless failures.

The normative delivery contract is updated in
[contracts/request-acceptance-and-delivery.md](contracts/request-acceptance-and-delivery.md).

### D-006 — Simple Twelve-Month Retention and Named Ownership

Accepted enquiries and their protected website audit history are retained for
twelve months from each request's durable acceptance time, then deleted from the
website database. Corresponding agency notification and follow-up email copies
are deleted from the agency inbox on the same twelve-month rule. The product
does not keep enquiry records indefinitely.

One named agency owner is responsible for the routine deletion process and for
handling a verified earlier deletion or data-rights request. Database backups
are not edited record by record; deleted data disappears through the selected
provider's documented normal backup-expiry cycle. That cycle must be known and
consistent with the public privacy explanation before real enquiries are
accepted.

Routine agency access occurs through the named business-inbox recipients.
Production database access is restricted to named technical roles and used only
for authorized recovery, security, or privacy work, not ordinary enquiry
handling. General logs continue to exclude request content, notes, messages,
and full contact details under D-004.

The client must approve the simple twelve-month rule, owner, inbox-deletion
practice, and accurate privacy wording before real launch, with qualified
privacy or legal validation where appropriate. This is a focused launch check,
not a requirement for a custom privacy-management system. Synthetic data may be
used before that approval.

Indefinite retention is rejected as unnecessary exposure. A broader multi-tier
schedule is deferred unless the agency's real workflow or qualified review
proves it necessary.

The normative handling boundary is defined in
[contracts/retention-access-and-deletion.md](contracts/retention-access-and-deletion.md).

### D-007 — Complete Correction Snapshots with Independent Expiry

Every explicit correction stores a complete corrected request rather than only
the changed fields. While both records exist, the correction links to the
earlier request through its opaque reference. The original remains immutable and
the correction remains independently understandable.

Each record continues to expire twelve months after its own durable acceptance.
Deleting the earlier request removes its submitted content and audit history; it
does not extend retention merely because a later correction exists. During the
correction's own retention period, it may preserve the submitted prior opaque
reference and a marker that the target has expired, but it cannot retrieve or
reconstruct the deleted request.

Retaining an entire linked chain until the latest correction expires is rejected
because repeated corrections could silently extend older personal-data
retention. Removing the correction path is also rejected because it would add
agency work and make visitor mistakes harder to resolve clearly.

The normative correction and retention interaction is defined across
[contracts/request-history-and-duplicates.md](contracts/request-history-and-duplicates.md)
and
[contracts/retention-access-and-deletion.md](contracts/retention-access-and-deletion.md).

## Open Questions

- D-008: How can agency staff use email-based request context without a staff
  dashboard or routine database access?

## Prior Acceptance

The operator accepted D-001 through D-006 as the complete Request Processing
and Communications feature boundary on 2026-07-30 and separately approved this
raw ledger's removal after verified distillation. The removal did not proceed
because final review found D-007 before the distillation was merged.

That prior acceptance remains evidence for D-001 through D-006 but is not the
final feature acceptance while D-008 is open. Nothing here authorizes application
implementation, dependency installation, schema migration, or deployment.

## Next Question

ID: D-008

Topic:
Making internal email-based context operational without adding a staff tool.

Prompt:
How should agency staff use prior-request context at launch when their supported
workflow is the business inbox rather than a website dashboard?

Options:

1. (recommended): **Keep routine staff context in the business inbox.** Each
   notification includes the current opaque reference and submitted reply email;
   an explicit correction also identifies the earlier opaque reference. Staff
   use ordinary inbox search or threading when prior context is needed. Database
   grouping supports system integrity, recovery, and privacy work but is not a
   routine staff view. Different emails cannot be manually merged at launch.
2. **Include an automated prior-request summary in each agency notification.**
   This gives immediate context but copies more historical personal data into
   email and requires new summary and redaction rules.
3. **Add a small staff request-history interface.** This makes grouping directly
   usable but introduces authentication, permissions, support, and lifecycle
   work outside the accepted launch boundary.

Why this matters:
Email grouping is not useful routine staff context if it exists only in a
database that agency staff are not allowed to browse. The launch needs either a
simple inbox behavior or a supported staff interface.

After answer:

- Lock the supported staff-context operation and relationship-merge boundary.
- Continue resolving the remaining distillation-review findings.
- Ask the operator to accept or correct the complete grill again before
  distillation.
