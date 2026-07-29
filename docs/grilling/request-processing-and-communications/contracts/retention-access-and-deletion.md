# Retention, Access, and Deletion Contract

## Authority and Scope

This contract is normative for Request Processing and Communications D-006. It
defines the proportional launch rule for private enquiry retention, access,
deletion, backups, and logging.

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
- accurate privacy wording and any qualified review required for the actual
  processing.

Synthetic test data may be used before these validations are complete.