# Retention, Access, and Deletion Contract

## Authority and Scope

This contract is normative for Request Processing and Communications D-006,
D-007, and D-009. It defines the proportional launch rule for private enquiry
retention, correction expiry, access, deletion, backups, restore, and logging.

It does not provide legal advice or authorize real-data launch by itself. The
client must approve the actual practice and public wording, with qualified
privacy or legal validation where appropriate.

## Twelve-Month Rule

1. Each accepted Consultation Request, Booking Request, or General Contact
   message and its protected website audit history is retained for twelve months
   from that request's durable acceptance time.
2. At the end of that period, the request and its protected website audit are
   deleted from the production database.
3. Agency notification and follow-up email copies for that enquiry follow the
   same twelve-month deletion rule in the agency inbox.
4. Enquiries are not retained indefinitely.
5. A broader or longer schedule requires later evidence from the agency's real
   workflow or qualified review; it must not be introduced silently.
6. Linked corrections do not extend the earlier request's expiry. Every
   correction stores a complete corrected snapshot and expires twelve months
   after its own acceptance. After the target expires, the correction may retain
   its submitted prior opaque reference and an expired-target marker during the
   correction's remaining retention period, but not the deleted target's
   content or audit history.

## Ownership and Earlier Requests

One named agency owner is responsible for the routine deletion process and the
corresponding agency-inbox practice. The same owner coordinates verified earlier
deletion, access, correction, or other applicable data-rights requests through a
client-approved manual process.

The exact identity-verification and legal-response procedure requires client and
qualified review before real launch. The public website does not expose request
history or provide an unverified self-service deletion mechanism.

## Access Boundary

- Named business-inbox recipients may access the operationally necessary email
  copies for manual agency follow-up.
- Production database access is restricted to named technical roles for
  authorized recovery, security, or privacy work.
- Direct database access is not the routine agency enquiry workflow.
- Access credentials and production records must not appear in source control,
  screenshots, demonstrations, general logs, or persistent project memory.

## Backups and Logs

Deleted records disappear from backups through the selected provider's
documented normal backup-expiry cycle; backups are not edited record by record.
The cycle and recovery behavior must be known and reflected accurately in the
approved privacy explanation before real enquiries are accepted.

Off-provider request-data backups are encrypted and use a rolling expiry of no
more than thirty days from each copy's creation. They are stored outside Neon,
remain unavailable to routine agency staff, and are accessible only to named
technical recovery roles. Launch uses zero-cost provider quotas; the exact free
scheduler and private storage provider belong to later technical and Production
Operations decisions.

A restore first enters an isolated, access-restricted environment. Before any
data returns to production, the recovery procedure reapplies the twelve-month
cutoff and every verified earlier deletion that could be present in the selected
backup. A minimal protected deletion manifest may remain only as long as needed
to prevent an eligible backup from resurrecting the deleted request.

The public privacy explanation states that deleted requests may remain in
protected backups for up to thirty additional days. Free quotas are monitored.
Visitor-volume pressure triggers an alert and evidence-led client review;
non-traffic exhaustion is corrected as an operational constraint. Neither case
causes an automatic paid upgrade or weakened safeguard.

General application, monitoring, and error logs must not contain request bodies,
notes, messages, full email addresses, or other unnecessary visitor details.
The protected request record and audit remain the authoritative private sources
during their retention period.

## Launch Validation

Before accepting real enquiries, confirm and test:

- client approval of the twelve-month database and inbox rule;
- the named agency deletion and data-rights owner;
- the agency-inbox deletion practice;
- provider backup expiry and recovery behavior; and
- encrypted off-provider backup creation, automatic thirty-day expiry,
  restricted access, deletion-safe isolated restore, free-quota monitoring, and
  alert ownership;
- accurate privacy wording and any qualified review required for the actual
  processing.

Synthetic test data may be used before these validations are complete.