# Request Processing and Communications Decisions

## Status and Authority

Accepted by the operator on 2026-07-30 after feature grilling and a reopened
semantic review. D-001 through D-009 form the complete accepted feature
boundary.
The operator amended the mail-provider realization on 2026-08-04 through Runtime
and Production Foundations D-004 without changing this feature's accepted
delivery semantics.

This document defines the Public Preview Release behavior shared by Consultation
Requests, Booking Requests, and General Contact messages: durable acceptance,
customer-contact recognition, immutable request history, explicit corrections,
exact-retry behavior, truthful system states, email recovery, staff context,
retention, access, deletion, logging, and off-provider recovery.

It does not authorize application implementation, dependency installation,
schema migration, deployment, or production-data handling. Those require later
promoted canonical documentation, accepted technical and Production Operations
decisions, and explicit bounded implementation contracts.

Use the project terms in [../GLOSSARY.md](../GLOSSARY.md). The accepted project
boundary remains in [../DECISIONS.md](../DECISIONS.md). The three owning
submission journeys remain authoritative for their fields, visitor wording,
content minimization, and visible outcomes.

## Feature Boundary

Every accepted submission is private transactional data. The website validates
and durably saves it in Neon before claiming receipt. Agency notification and
visitor acknowledgement use one provider-neutral transactional-email interface,
with Resend primary and Brevo as the single launch fallback, but remain
independent outcomes after acceptance.

The launch has no customer accounts, public request history, staff dashboard,
staff request-history interface, or separate customer-management system.
Agency staff handle routine follow-up and prior-request context through the
existing business inbox. The production database owns protected request records
and only those system states the website can keep truthful.

The Public Preview is a zero-new-recurring-platform-spend market-validation
release. This feature uses compliant free quotas at launch without weakening
privacy, security, durability, recovery, or truthful failure behavior. Real
visitor-driven quota pressure is evidence for a later client-funded upgrade;
CI or operational exhaustion is not.

The normative contracts are:

- [Request acceptance and delivery](contracts/request-acceptance-and-delivery.md)
- [Customer contact recognition](contracts/customer-contact-recognition.md)
- [Request history and duplicates](contracts/request-history-and-duplicates.md)
- [System states and audit](contracts/system-states-and-audit.md)
- [Retention, access, and deletion](contracts/retention-access-and-deletion.md)

## D-001 — Accept After Durable Saving and Recover Email Separately

A valid request is accepted when its complete private transactional record is
durably committed in Neon. If persistence fails, the request is not accepted.
Agency-notification and visitor-acknowledgement work starts only for an accepted
request. Later email outcomes cannot revoke, delete, or rewrite acceptance.
The submission handler waits for the required initial delivery work to finish
before returning the visitor-visible outcome; later bounded recovery remains
separate.

After the commit, the website shows the owning journey's honest received message
and opaque, non-sensitive reference. It does not claim that staff or the visitor
were emailed when the corresponding delivery is failed or unconfirmed. If the
visitor acknowledgement fails or cannot be confirmed during submission, the
website explains that the request was received but email delivery could not be
confirmed. It never asks the visitor to resubmit an accepted request to repair
email delivery.

A confirmed handoff means only that the configured mail service accepted the
message for delivery. It is not proof that the recipient read or ultimately
received it, and public wording must not overstate that outcome.

Agency-notification and visitor-acknowledgement outcomes are recorded
independently. Failed agency notification enters operational recovery rather
than being ignored. Treating email delivery as the acceptance condition is
rejected because it would present saved data as failed and encourage duplicate
submission.

## D-002 — Email-Based Contact Relationship with Immutable Snapshots

The normalized submitted email address identifies the internal
customer-contact relationship used to group accepted requests across all three
submission journeys.

Each accepted request preserves the name, email, and other contact values
submitted with that request. Later submissions append current information but
do not overwrite, rewrite, or detach an earlier request's snapshot.

The relationship is not an account, login, verified identity, or proof that all
grouped requests came from one unique person. Shared family or business inboxes
may represent several people. Different email addresses remain separate at
launch. Manual cross-email merging is unavailable because no supported staff
operation exists. Names, telephone numbers, and approximate matching must not
merge relationships automatically.

Public forms must not use email alone to reveal whether earlier requests exist,
list or summarize them, prefill earlier personal information, or claim that the
visitor is recognized or verified. Exact normalization mechanics belong to a
later implementation contract and must not apply provider-specific mailbox
transformations that could merge distinct addresses.

## D-003 — Immutable Chronology, Explicit Corrections, and Exact Retries

Every accepted new submission has one immutable record and opaque reference in
the D-002 relationship's chronological history. Later records append; they do
not overwrite, rewrite, or detach earlier records. Similar content, close
timing, or reused contact details do not by themselves prove that a later
submission is a correction or duplicate.

A submission is a correction only when the visitor explicitly selects that
intent and supplies the earlier request's opaque reference. The submitted
normalized email must belong to the same contact relationship as the referenced
request. A failed reference-and-email match must not reveal whether either value
exists or identify prior activity.

A valid correction creates a new immutable request linked to the earlier
request. It never overwrites, deletes, or detaches the original because staff may
already have received or acted upon it. An ordinary submission remains a new
request by default.

Repeated transport of the same technical submission resolves idempotently to
the same accepted request and reference. It does not create another
chronological record, correction, or intentional email dispatch. The later
implementation contract must use a bounded, non-sensitive idempotency identity
and must not reuse it for a visitor's later intentional request.

The chronology is private system context. It does not introduce a customer
account, visitor-visible history, or routine staff database-browsing workflow.

## D-004 — Audit Only Truthful System-Owned States

The website owns and records these independent state domains:

1. request acceptance after durable persistence;
2. ordinary-new or explicit-correction relationship;
3. agency-notification delivery and recovery; and
4. visitor-acknowledgement delivery and recovery.

Each transition preserves its time and whether it originated from submission
processing, automated recovery, or a named authorized recovery action. Each
email purpose distinguishes work still pending or unconfirmed, confirmed
handoff to the mail service, and failed work requiring retry, escalation, or
owner attention. Audit history is append-only: later success does not erase an
earlier failure or uncertain handoff.

For each accepted request, the protected transactional record preserves the
opaque reference, request type, acceptance time, contact relationship,
immutable submitted snapshot, correction link where applicable, delivery
transitions, and minimum provider or failure context needed for investigation.

The website does not store or publish staff lifecycle claims such as new, in
progress, resolved, closed, or cancelled. Those states remain in the agency's
existing email process because no supported staff control surface is accepted.
Technical staff must not maintain invented staff lifecycle fields through
routine direct database work.

General application, monitoring, and error logs do not copy request bodies,
notes, messages, full email addresses, or other unnecessary visitor data. The
protected request and audit records remain the authoritative private sources.

## D-005 — Bounded Safe Retry with Out-of-Band Escalation

A definitely failed agency notification or visitor acknowledgement receives a
bounded number of automatic retries using a stable request-and-purpose identity.
A confirmed mail-service handoff is not deliberately redispatched. An uncertain
handoff stops blind automatic retry because the provider may already have
accepted the message.

When retries are exhausted or delivery remains uncertain, the system alerts a
named recovery owner through a separately monitored route that does not depend
solely on the failing transactional-email provider path. The alert contains only
the opaque request reference, email purpose, failure category, and minimum
diagnostic context. It excludes the visitor's request, message, notes, and contact
details.

The recovery owner makes the bounded decision for uncertain delivery and ensures
that a failed agency notification does not leave an accepted request unnoticed.
Every automated attempt, escalation, authorized recovery action, and final
outcome is appended to the D-004 audit history. Recovery does not change request
acceptance and does not ask the visitor to resubmit.

Before real enquiries are accepted, name and test the retry count and timing,
recovery owner, separately monitored alert route, and response procedure.
Immediate manual handling of every definitely failed send is rejected as
avoidable workload. Unbounded retry is rejected because it can create delayed
duplicates and leave failures without a human owner.

## D-006 — Twelve-Month Retention and Named Ownership

Each accepted enquiry and its protected website audit history is retained for
twelve months from that request's durable acceptance time and then deleted from
the production database. Corresponding agency notification and follow-up email
copies follow the same twelve-month deletion rule in the agency inbox. Enquiry
records are not retained indefinitely.

One named agency owner is responsible for routine deletion and the corresponding
inbox practice. The same owner coordinates verified earlier deletion, access,
correction, or other applicable data-rights requests through a client-approved
manual process. The public website does not expose request history or provide an
unverified self-service deletion mechanism.

Named business-inbox recipients may access operationally necessary email copies
for manual follow-up. Production database access is restricted to named
technical roles for authorized recovery, security, or privacy work and is not
the routine agency workflow.

Provider-managed backups are not edited record by record. Their documented
expiry cycle and restore behavior must be known and represented accurately in
the approved privacy explanation. D-009 adds the separate off-provider recovery
boundary.

A broader or longer retention schedule is deferred unless the agency's real
workflow or qualified review proves it necessary. This decision requires a
simple, testable launch practice rather than a custom privacy-management system.

## D-007 — Complete Correction Snapshots with Independent Expiry

Every explicit correction stores a complete corrected request rather than only
the changed fields. While both records exist, the correction links to the
earlier request through its submitted opaque reference. The original remains
immutable and the correction remains independently understandable.

Every request, including a correction, expires twelve months after its own
durable acceptance. A later correction does not extend the earlier request's
retention. Deleting the earlier request removes its submitted content and audit
history.

During the correction's remaining retention period, it may preserve the
submitted prior opaque reference and an expired-target marker. It cannot retrieve
or reconstruct the deleted earlier request. Keeping an entire correction chain
until its newest record expires is rejected because repeated corrections could
silently extend older personal-data retention.

## D-008 — Routine Staff Context Stays in the Business Inbox

Routine agency staff use the existing business inbox rather than the production
database to find prior-request context. Every agency notification includes the
current opaque request reference and submitted reply email. An explicit
correction also includes the submitted earlier opaque reference. Staff may use
ordinary inbox search or threading when earlier context is needed.

The D-002 normalized-email relationship remains useful for system integrity,
correction validation, technical recovery, security, and privacy work, but it is
not exposed as a routine staff history view. Different email relationships
cannot be manually merged at launch. A later merge capability requires a
separately accepted staff interface and verification boundary.

Notifications do not automatically include summaries of prior requests. Such
summaries would duplicate more historical personal data in email and require new
summary and redaction rules. A staff request-history interface remains deferred
with the dashboard.

## D-009 — Zero-Cost Encrypted Rolling Backups with Thirty-Day Expiry

The Public Preview uses encrypted off-provider request-data backups within
zero-cost provider quotas. Each copy expires automatically no later than thirty
days after creation. The later technical design may select free scheduled
automation and private object storage but must not require a VPS or paid service
for launch.

Backups are not a history interface and are accessible only to named technical
recovery roles. A restore first enters an isolated, access-restricted
environment. Before any data returns to production, the recovery procedure
reapplies the twelve-month cutoff and every verified earlier deletion that could
be present in the selected copy.

A minimal protected deletion manifest may be retained only as long as needed to
prevent an eligible backup from resurrecting a deleted request. The approved
privacy explanation states that a deleted request may remain in protected
backups for up to thirty additional days.

Free-quota use is monitored. Visitor-volume pressure is evidence of demand and
triggers an explicit client discussion about a bounded paid upgrade. CI or
operational exhaustion is corrected separately and is not demand evidence.
Neither case authorizes silent data loss, an unapproved charge, or weakened
safeguards.

If backup creation cannot complete, the named owner is alerted. If a free limit
prevents durable request acceptance, the website returns an honest temporary
failure rather than claiming receipt. Exact providers, schedules, quota
thresholds, and restore commands belong to Production Operations and the later
technical design.

## Inherited Journey and Security Boundaries

This shared feature preserves the owning Consultation Request, Booking Request,
and General Contact decisions rather than broadening their collection,
notifications, or visitor promises:

- Consultation notes remain in the protected private-data workflow and are not
  copied into agency notification emails.
- Visitor-provided text is safely rendered and minimized in notifications. Its
  access, redaction, deletion, retention, and incident handling require the
  accepted protected-data workflow and applicable qualified review.
- A Booking Request stores the smallest bounded historical Experience snapshot
  needed to identify what the visitor requested without copying unnecessary
  mutable catalogue content. Disabling an Experience does not rewrite, detach,
  delete, reject, or automatically cancel an already accepted request.
- Booking Request acknowledgement emails retain the owning journey's required
  non-confirming wording: the request does not reserve the Experience or confirm
  availability.
- Persistence failures preserve the owning journey's accepted recovery
  behavior: no receipt claim, safe retry with entered data preserved where
  specified, no exposed technical details, and only client-approved alternative
  contact routes where specified.
- Opaque references and public errors reveal no personal data or sequential
  private-record details.
- Production credentials and records never appear in source control,
  screenshots, demonstrations, general logs, or persistent project memory.
- Content Operations owns approved, semantically equivalent English and Greek
  receipt, failure, correction, privacy, and recovery wording.

## Explicit Exclusions and Deferrals

- Email delivery is not the request-acceptance condition.
- An accepted request is never presented as unreceived because email failed.
- A mail-service handoff is not represented as final receipt or reading.
- Email matching does not authenticate a person, expose prior activity, prefill
  history, or provide public history access.
- Different-email relationships cannot be manually or approximately merged at
  launch.
- A correction never overwrites or deletes the earlier request.
- Similar submissions are not automatically classified as corrections or
  duplicates.
- Linked corrections do not extend earlier records' retention.
- Customer accounts and visitor-visible request history remain deferred.
- A staff dashboard, staff history interface, customer-management system, and
  website-owned staff lifecycle states remain deferred.
- Direct database editing or browsing is not routine agency request handling.
- Notifications do not automatically summarize historical requests.
- Confirmed or uncertain email handoffs are not blindly retried.
- Recovery alerts do not copy private visitor submissions or contact details.
- General logs do not contain request content or unnecessary personal data.
- Enquiries and off-provider recovery copies are not retained indefinitely.
- Backups are not routine staff history or reporting surfaces.
- No VPS, paid launch backup service, or custom privacy-management system is
  required.

## Dependencies and Unresolved External Validations

Before Greek Essence accepts real enquiries, the applicable owners must confirm
and test:

- **Client:** the production business inbox, recipients, ordinary follow-up
  process, recovery owner, separately monitored alert route, and operational
  response procedure.
- **Development team with the client mail-provider owner:** Resend and Brevo
  account control, narrow API credentials, authorized sender domain, provider
  terms and limits, confirmed handoff behavior, and the exact bounded retry count
  and timing.
- **Client:** the named agency deletion and data-rights owner, twelve-month
  database and inbox rule, and practical inbox-deletion process.
- **Client and qualified privacy or legal reviewer:** accurate controller facts,
  lawful basis, privacy wording, twelve-month active retention, possible
  thirty-day protected-backup residue, recipients, rights, transfer facts where
  relevant, and identity verification for manual data-rights handling.
- **Development team with the client account owner:** Neon access, suitable
  region and privacy agreement, durable transaction behavior, restricted
  production roles, provider-managed backup expiry, and restore behavior.
- **Production Operations:** commercially eligible free-plan validation, quota
  monitoring and alerts, encrypted off-provider backup ownership and automatic
  expiry, deletion-safe isolated restore evidence, secrets, incidents, and named
  operational access.
- **Catalogue Discovery:** the authoritative Experience identifier,
  requestability state, withdrawal behavior, and source for the smallest useful
  historical snapshot.
- **Content Operations:** approved, semantically equivalent English and Greek
  receipt, email-failure, correction, privacy, and recovery wording.
- **Later implementation contracts:** exact email normalization, opaque-reference
  generation, idempotency identity, request validation, schema and transaction
  boundaries, safe free-text rendering, notification payloads, retry scheduling,
  audit fields, deletion execution, deletion-manifest behavior, backup commands,
  bounded Experience snapshot, and focused tests.

These validations may refine mechanics, named owners, approved wording, provider
selection, and qualified handling. They must not silently change durable
acceptance; expose prior activity; overwrite or indefinitely extend request
history; add unsupported staff lifecycle states; allow ownerless email failures;
place private content in general logs; resurrect expired records; introduce an
unapproved paid service; or weaken the zero-cost Public Preview's mandatory
safeguards.
