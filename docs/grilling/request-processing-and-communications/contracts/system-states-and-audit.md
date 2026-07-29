# System States and Audit Contract

## Authority and Scope

This contract is normative for Request Processing and Communications D-004. It
defines the system-owned request states and minimum audit history for launch.

It does not create staff workflow states, a staff dashboard, or a
customer-management system. D-005 owns detailed email recovery, and D-006 owns
retention, deletion, logging, and access.

## System-Owned State Domains

The website owns and keeps truthful only these independent domains:

1. **Request acceptance:** not accepted when durable persistence fails; accepted
   after the D-001 durable commit.
2. **Request relationship:** ordinary new request or explicit correction linked
   to the earlier immutable request under D-003.
3. **Agency notification:** the pending, confirmed-handoff, failed, and recovery
   distinctions required by D-001 and refined by D-005.
4. **Visitor acknowledgement:** the equivalent independent delivery and recovery
   distinctions required by D-001 and refined by D-005.

Email-state changes never revoke request acceptance. A correction never replaces
the earlier accepted request.

## Excluded Staff Lifecycle States

The website does not store or publish claims that agency handling is new, in
progress, resolved, closed, cancelled, or otherwise complete. Launch staff
follow-up remains in the agency's accepted email process.

Those states require a separately accepted staff workflow and supported control
surface. They must not be maintained through routine direct database edits.

## Minimum Audit History

For each accepted request, the protected transactional record must preserve:

- opaque request reference and request type;
- durable acceptance time;
- D-002 contact-relationship identity and immutable submitted snapshot;
- D-003 correction relationship when applicable;
- each system-owned state transition and its time;
- whether the transition originated from submission processing, automated
  recovery, or a named authorized recovery action; and
- the minimum provider or failure context needed to investigate delivery without
  placing visitor content in general application logs.

Audit entries are append-only history. Later success does not erase an earlier
failure or uncertain handoff.

## Data-Minimization Boundary

General application, monitoring, and error logs must not copy the request body,
free-text notes, message content, full email address, or other unnecessary
personal data. The private request record remains the source for submitted
content. D-006 must define exact access, retention, deletion, and redaction
rules.