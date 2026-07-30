# Request Processing and Communications Grilling

## Status

D-001 through D-009 were accepted as the complete feature boundary by the
operator on 2026-07-30. The operator also authorized verified distillation,
removal of this exact raw ledger, automated pull-request delivery, squash merge,
and merged-branch deletion without another routine approval request.

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

A confirmed handoff means only that the configured mail service accepted the
message for delivery. It is not proof that the recipient read or ultimately
received it, and public wording must not overstate that outcome.

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
several people. Different email addresses remain separate at launch; D-008
rejects manual relationship merging without a supported staff tool. The system
must not infer a merge from similar names, telephone numbers, or other
approximate details.

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

Production credentials and records must also remain out of source control,
screenshots, demonstrations, and persistent project memory.

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

### D-008 — Routine Staff Context Stays in the Business Inbox

Routine agency staff use the existing business inbox rather than the production
database to find prior-request context. Every agency notification includes the
current opaque request reference and submitted reply email. An explicit
correction also includes the earlier opaque reference. Staff may use ordinary
inbox search or threading when earlier context is needed.

The D-002 normalized-email relationship remains useful for system integrity,
correction validation, recovery, and privacy work, but it is not exposed as a
routine staff history view. Different email relationships cannot be manually
merged at launch because no supported staff operation exists; a later merge
capability requires a separately accepted interface and verification boundary.

Automatically copying prior-request summaries into every notification is
rejected because it would duplicate more historical personal data in email and
require new summary and redaction rules. A staff request-history interface
remains deferred with the dashboard.

The normative staff-context boundary is defined in
[contracts/customer-contact-recognition.md](contracts/customer-contact-recognition.md).

### D-009 — Zero-Cost Encrypted Rolling Backups with Thirty-Day Expiry

The Public Preview uses encrypted off-provider request-data backups within
zero-cost provider quotas. Each backup copy expires automatically no later than
thirty days after creation. The later technical design may select free scheduled
automation and private object storage but must not require a VPS or paid service
for launch.

Backups are not a history interface and are accessible only to named technical
recovery roles. A restore first enters an isolated, access-restricted
environment, then reapplies the twelve-month cutoff and verified earlier
deletions before any data returns to production. A minimal protected deletion
manifest may be retained only as needed to prevent an eligible backup from
resurrecting a deleted request.

The privacy explanation states that a deleted request may remain in protected
backups for up to thirty additional days. Free-quota use must be monitored.
Visitor-volume pressure on a free allowance is evidence of demand and triggers
an explicit client discussion about a bounded paid upgrade. CI or operational
misuse is not demand evidence and must be corrected separately. Neither case
authorizes silent data loss, an unapproved charge, or weakened safeguards.

If the backup operation cannot complete, the named owner is alerted. If a free
limit prevents durable request acceptance, the website returns an honest
temporary failure rather than claiming receipt. Exact providers, schedules,
quota thresholds, and restore commands belong to Production Operations and the
later technical design.

The normative backup boundary is defined in
[contracts/retention-access-and-deletion.md](contracts/retention-access-and-deletion.md).

## Inherited Cross-Journey Requirements

The owning Consultation Request, Booking Request, and General Contact decisions
remain authoritative beyond visitor wording. Final distillation and later
implementation contracts must preserve these accepted consequences:

- Consultation notes do not enter agency notification emails.
- Visitor-provided text is safely rendered, minimized in notifications, and
  covered by redaction and incident handling.
- A Booking Request stores only the smallest historical Experience snapshot
  needed to identify what the visitor requested without copying unnecessary
  mutable catalogue content.
- Production credentials and records never appear in source control,
  screenshots, demonstrations, general logs, or persistent project memory.

## Open Questions

None. No unresolved feature decision currently appears capable of materially
changing request value, scope, workflow, data, ownership, privacy, recovery,
cost, or implementation boundaries.

## Acceptance and Finalization Authorization

The operator accepted D-001 through D-006 as the complete Request Processing
and Communications feature boundary on 2026-07-30 and separately approved this
raw ledger's removal after verified distillation. The removal did not proceed
because final review found D-007 before the distillation was merged.

On 2026-07-30, the operator accepted D-001 through D-009 as the complete Request
Processing and Communications boundary. The same instruction explicitly
approved removal of
`docs/grilling/request-processing-and-communications/GRILLING.md` after creation
and verification of `DECISIONS.md`, and authorized the commit, push, required
checks, squash merge into `main`, and automatic merged-branch deletion.

Because the repository squash-merges pull requests, this accepted raw state must
first be merged to `main`. A second pull request may then distill the decisions
and remove the approved raw path under the same authorization. No additional
routine approval is required unless semantic review exposes a material conflict
that changes accepted product truth.

This acceptance and delivery authorization does not authorize application
implementation, dependency installation, schema migration, or deployment.
