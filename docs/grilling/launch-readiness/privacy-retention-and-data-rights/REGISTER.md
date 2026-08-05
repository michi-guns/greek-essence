# Public Preview Privacy, Retention, and Data-Rights Readiness

## Status

Active — LR-P-002 is open.

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

| ID       | Required readiness item                          | Expected boundary                                                                                                          | Required evidence                                                                           | Status    |
| -------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------- |
| LR-P-001 | Agency retention and data-rights owner           | Owns the practical twelve-month database/inbox deletion practice and coordinates verified rights requests                  | Named authorized agency person and escalation boundary                                      | Confirmed |
| LR-P-002 | Agency approval of the actual retention practice | Approves the agency's real inbox-deletion and manual rights-handling practice without changing the accepted retention rule | Attributable agency approval, with qualified privacy/legal review identified where required | Open      |
| LR-P-003 | Accurate privacy explanation and review          | Explains collection, retention, email copies, backup residue, and contact route without inventing legal claims             | Approved bilingual copy and applicable qualified-review evidence                            | Open      |
| LR-P-004 | Restricted access and deletion evidence          | Limits production database and backup access to named technical roles and proves ordinary deletion practice                | Access-boundary evidence and synthetic or controlled deletion evidence                      | Open      |
| LR-P-005 | Backup-residue and isolated-restore evidence     | Preserves the thirty-day backup limit and reapplies deletion safeguards before a restore can affect production             | Manual export/deletion record and exercised isolated restore using controlled data          | Open      |

## Confirmed Readiness

### LR-P-001 — Agency Retention and Data-Rights Owner

- **Named agency owner:** Giorgos.
- **Authority boundary:** Giorgos owns the agency-side practical twelve-month
  inbox-deletion practice and coordinates verified access, correction, and early
  deletion requests. He may delegate practical tasks within Greek Essence, but
  remains accountable for the agency decision and any necessary qualified review.
  Dimitri's technical recovery and backup role does not transfer this agency-side
  authority.
- **Evidence:** the operator selected option 1 on 2026-08-05. Before real
  enquiries are enabled, the agency must approve its actual deletion and
  rights-handling practice, and protected evidence must show that this practice
  can be followed without exposing Request content in repository files or general
  logs.
- **Status:** Confirmed.

## Current Focus

### LR-P-002 — Agency Approval of the Actual Retention Practice

The retention rule is already locked: database records and agency email copies
are deleted twelve months after acceptance, and a verified manual process handles
earlier access, correction, or deletion requests. We now need Giorgos to approve
how Greek Essence will actually carry that rule out in the agency inbox. This is
not a request to write legal language or create a custom privacy-management
system.

For example, a short agency procedure could say: Giorgos periodically identifies
enquiries reaching their retention date, removes the matching agency email copies,
and uses a verified request before asking Dimitri to perform any necessary
technical deletion. The exact verification and legal-response details still need
qualified privacy or legal review before real launch.

1. **(recommended): Prepare a short concrete agency procedure for Giorgos to
   approve and qualified review to validate.** It will implement the accepted
   twelve-month rule and manual rights route, while leaving legal wording and
   identity-verification detail for the appropriate review.
2. **Ask Giorgos to define the operational procedure from scratch.** This gives
   the agency maximum freedom, but risks leaving the accepted retention rule
   impractical or incomplete without a concrete starting point.
3. **Defer the procedure until immediately before launch.** This keeps discovery
   short now, but blocks real enquiries until it is approved and validated.

## Continuation Rule

Confirm one readiness item at a time before moving to the next. If an external
fact reveals an actual privacy, service, or technical-foundation conflict, mark
the item blocked and route the conflict to its owning layer rather than weakening
an accepted rule.
