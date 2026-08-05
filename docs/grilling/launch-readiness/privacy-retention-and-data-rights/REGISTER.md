# Public Preview Privacy, Retention, and Data-Rights Readiness

## Status

Active — LR-P-001 is open.

## Purpose

Confirm the agency-side ownership, approved facts, practical retention and
rights-handling procedure, and evidence needed to operate the accepted private
Request-data boundary before real enquiries are enabled. This register does not
redefine the accepted twelve-month retention, manual backup, or restricted-access
rules; it records the people, approvals, procedures, and proof needed to use
them honestly.

It does not authorize implementation, Neon or Drizzle configuration,
production-data access, migration, deployment, or launch.

## Accepted Inputs

- [Retention, Access, and Deletion Contract](../../request-processing-and-communications/contracts/retention-access-and-deletion.md)
  requires twelve-month database and agency-inbox deletion, one named agency
  owner, manual verified rights handling, restricted production-database access,
  and accurate backup-residue wording.
- [Request Processing and Communications D-009](../../request-processing-and-communications/DECISIONS.md)
  keeps encrypted off-provider exports no more than thirty days and requires
  deletion-safe isolated restore.
- [Runtime and Production Foundations D-005](../../foundation-design/runtime-and-production-foundations/DECISIONS.md)
  requires manual encrypted `pg_dump` exports in controlled local storage outside
  the application and repository.
- [Public Preview Launch Ownership and Escalation](../ownership-and-escalation/REGISTER.md)
  confirms Giorgos as business approver and real-enquiry inbox owner, and Dimitri
  as technical recovery and backup operator. Neither confirmation silently names
  the agency data-rights and retention owner.

## Status Model

- **Open:** the person, fact, approval, procedure, or evidence is not confirmed.
- **Confirmed:** the required boundary and the evidence needed before real
  enquiries are enabled are recorded.
- **Blocked:** progress needs an external fact, qualified review, or an upstream
  product or foundation decision.

## Readiness Register

| ID       | Required readiness item                          | Expected boundary                                                                                                          | Required evidence                                                                           | Status |
| -------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------ |
| LR-P-001 | Agency retention and data-rights owner           | Owns the practical twelve-month database/inbox deletion practice and coordinates verified rights requests                  | Named authorized agency person and escalation boundary                                      | Open   |
| LR-P-002 | Agency approval of the actual retention practice | Approves the agency's real inbox-deletion and manual rights-handling practice without changing the accepted retention rule | Attributable agency approval, with qualified privacy/legal review identified where required | Open   |
| LR-P-003 | Accurate privacy explanation and review          | Explains collection, retention, email copies, backup residue, and contact route without inventing legal claims             | Approved bilingual copy and applicable qualified-review evidence                            | Open   |
| LR-P-004 | Restricted access and deletion evidence          | Limits production database and backup access to named technical roles and proves ordinary deletion practice                | Access-boundary evidence and synthetic or controlled deletion evidence                      | Open   |
| LR-P-005 | Backup-residue and isolated-restore evidence     | Preserves the thirty-day backup limit and reapplies deletion safeguards before a restore can affect production             | Manual export/deletion record and exercised isolated restore using controlled data          | Open   |

## Current Focus

### LR-P-001 — Agency Retention and Data-Rights Owner

The accepted rule is simple: each accepted enquiry and its agency email copies
are deleted after twelve months; requests for earlier deletion, access, or
correction use a verified manual agency process. Someone on the agency side must
own that routine. This is not the technical backup role: Dimitri may operate a
controlled restore, but he cannot decide how Greek Essence handles a visitor's
data-rights request on the agency's behalf.

For example, if a visitor emails Greek Essence asking for their consultation
request to be deleted early, the named agency owner confirms the request through
the approved process, directs the necessary inbox and data handling, and
escalates technical deletion only when needed. The website must not reveal prior
requests or offer an unverified self-service deletion button.

1. **(recommended): Giorgos is the named agency retention and data-rights owner.**
   He owns the agency-side inbox deletion practice and coordinates verified
   earlier deletion, access, and correction requests. He may delegate practical
   tasks within the agency, but remains accountable for the agency decision and
   any required qualified review.
2. **A named authorized agency delegate owns the role.** Giorgos explicitly names
   a person who will run the routine process and coordinate requests. This can
   suit the agency's real staffing, but the person's authority and handoff must
   be confirmed before launch.
3. **Leave the owner unassigned until launch preparation.** This avoids naming a
   person now, but blocks real enquiries because the accepted retention rule has
   no accountable agency-side operator.

## Continuation Rule

Confirm one readiness item at a time before moving to the next. If an external
fact reveals an actual privacy, service, or technical-foundation conflict, mark
the item blocked and route the conflict to its owning layer rather than weakening
an accepted rule.
