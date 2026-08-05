# Public Preview Privacy, Retention, and Data-Rights Readiness

## Status

Active — LR-P-003 is open.

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
| LR-P-002 | Agency approval of the actual retention practice | Approves the agency's real inbox-deletion and manual rights-handling practice without changing the accepted retention rule | Attributable agency approval, with qualified privacy/legal review identified where required | Confirmed |
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

### LR-P-003 — Accurate Privacy Explanation and Review

The website's privacy explanation must truthfully describe what it collects, how
long it is retained, who receives enquiry emails, how visitors contact Greek
Essence about their data, and the limited backup-residue period. The accepted
product does not yet supply the exact controller details, inbox route, legal
wording, or qualified-review outcome, so public copy cannot safely be invented.

Before a bilingual draft is written, the agency needs a compact factual input
pack: the legal/controller identity and contact route it wants visitors to use;
the approved inbox recipient boundary; the actual provider and backup facts once
configured; and the qualified reviewer who will validate the final wording.

Giorgos's visible coordination task is [WU-42](https://trello.com/c/f73YL73G),
**GIORGOS ACTION: confirm public privacy-notice facts and reviewer**. Its Inbox
description includes a copy-and-complete response template and a clearly
fictional completed example. The card is a request for factual input and review
ownership; it does not approve public wording or enable real enquiries.

1. **(recommended): Giorgos supplies the agency facts and nominates the qualified
   privacy/legal reviewer; Dimitri prepares an English/Greek draft only from those
   confirmed inputs.** This keeps agency legal and business facts with the agency,
   while Dimitri can prepare meaning-equivalent public copy for review.
2. **Giorgos supplies the facts but no qualified reviewer is identified yet.** A
   draft could be prepared as internal review material, but it cannot be approved
   as launch-ready privacy wording.
3. **Defer all privacy-copy work until after technical configuration.** This avoids
   provisional copy but delays agency review even for facts already independent of
   the final provider setup.

## Confirmed Readiness

### LR-P-002 — Agency Approval of the Actual Retention Practice

- **Selected direction:** Prepare a short concrete agency procedure for Giorgos
  to approve, with qualified privacy or legal review validating applicable
  details.
- **Draft review input:**
  [Draft Agency Retention and Data-Rights Procedure](procedures/draft-agency-retention-and-data-rights-procedure.md).
  It preserves the accepted twelve-month database and inbox rule, verified manual
  rights route, restricted technical access, and limited backup-residue boundary
  without claiming approval or legal completeness.
- **Evidence:** the operator selected option 1 on 2026-08-05. Before real
  enquiries are enabled, Giorgos must approve or correct the procedure against
  actual agency practice, and applicable qualified review must validate the
  verification, response, documentation, and public-wording details.
- **Status:** Confirmed.

## Continuation Rule

Confirm one readiness item at a time before moving to the next. If an external
fact reveals an actual privacy, service, or technical-foundation conflict, mark
the item blocked and route the conflict to its owning layer rather than weakening
an accepted rule.
