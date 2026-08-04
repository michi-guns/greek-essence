# Public Preview Launch Ownership and Escalation

## Status

Accepted.

## Purpose

Verify the named people and escalation routes required to operate the accepted
Public Preview safely. This register records assignments, required evidence, and
blockers; it does not redefine accepted product or foundation decisions and does
not authorize implementation, provider configuration, production-data access,
deployment, or launch.

## Scope

This bounded subject covers:

- final agency approval of public business meaning and bilingual content;
- named English and Greek language review;
- technical publication responsibility;
- the monitored agency recipient for real enquiries;
- transactional-email recovery and incident escalation ownership; and
- manual backup, deletion, and authorized restore ownership.

Exact public copy, legal wording, provider accounts, quotas, credentials,
operating procedures, and executable technical evidence remain separate Launch
Readiness subjects.

## Accepted Inputs

- [`PROJECT_ACTORS.md`](../../../PROJECT_ACTORS.md) distinguishes Giorgos's
  agency-side approval authority from Dimitri's technical publishing role.
- [Public Brand Pages decisions](../../public-brand-pages/DECISIONS.md) require
  complete human-reviewed English and Greek experiences with named client
  ownership.
- [Request Processing and Communications decisions](../../request-processing-and-communications/DECISIONS.md)
  require a monitored agency inbox and a named delivery-recovery owner.
- [Editorial Content Platform decisions](../../foundation-design/editorial-content-platform/DECISIONS.md)
  separate approval of business meaning from technical preview and publication.
- [Runtime and Production Foundations decisions](../../foundation-design/runtime-and-production-foundations/DECISIONS.md)
  require named operational ownership before real enquiries are accepted.

## Status Model

- **Open:** the assignment or its evidence is not confirmed.
- **Confirmed:** the named person, authority boundary, and required evidence are
  recorded.
- **Blocked:** confirmation cannot proceed without an external fact or an
  upstream product or foundation decision.

## Readiness Register

| ID       | Required assignment                           | Expected boundary                                                                                                  | Required evidence                                                                                    | Status    |
| -------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | --------- |
| LR-O-001 | Agency business and content approver          | Approves services, claims, prices, media use, and the intended business meaning in both languages                  | Named authorized person and confirmation that technical publication does not transfer this authority | Confirmed |
| LR-O-002 | English and Greek language reviewers          | Check natural language and semantic parity without silently becoming business approvers                            | Named reviewer for each language and the handoff for correcting or escalating changed meaning        | Confirmed |
| LR-O-003 | Technical publisher                           | Performs the Sanity edit, technical preview, validation, publication, withdrawal, and public verification steps    | Named person, production-access boundary, and confirmed handoff from the business approver           | Confirmed |
| LR-O-004 | Real-enquiry inbox recipient                  | Monitors the agency-owned route for Consultation, Booking Request, and General Contact follow-up                   | Named agency owner and protected confirmation that the real-enquiry route reaches that owner         | Confirmed |
| LR-O-005 | Delivery-recovery and incident owner          | Receives data-minimized alerts and handles uncertain or exhausted email delivery without prompting duplicate sends | Named owner, separate alert route, escalation boundary, and exercised recovery evidence              | Confirmed |
| LR-O-006 | Manual backup, deletion, and restore operator | Creates encrypted Neon exports, deletes each no later than thirty days, and restores only with explicit authority  | Named operator, authorization boundary, deletion evidence, and exercised isolated-restore evidence   | Confirmed |

## Confirmed Assignments

### LR-O-001 — agency business and content approver

- **Named approver:** Giorgos.
- **Authority boundary:** Giorgos gives final agency approval for services,
  claims, prices, media use, and intended business meaning in English and Greek.
  He may explicitly delegate approval for affected material to an authorized
  agency person. Technical preparation, preview, validation, or publication does
  not transfer this agency authority to the technical publisher.
- **Evidence:** the operator confirmed Giorgos as the named approver on
  2026-08-04. Each material approval or delegation must remain attributable to
  Giorgos or the explicitly authorized delegate. Qualified legal approval and
  exact legal wording remain separate Launch Readiness evidence.
- **Status:** Confirmed.

### LR-O-002 — English and Greek language reviewers

- **Named English reviewer:** Dimitri.
- **Named Greek reviewer:** Dimitri.
- **Authority boundary and handoff:** Dimitri checks that each language reads
  naturally and that both communicate the same service boundaries. He may make
  wording corrections that preserve the approved meaning, but this review does
  not make him the business approver. Any correction that changes a service,
  claim, price, media use, legal meaning, or other business meaning returns to
  Giorgos for approval before publication.
- **Evidence:** the operator confirmed Dimitri for both language-review roles on
  2026-08-04. Publication evidence must identify the reviewed English and Greek
  material and preserve the Giorgos approval attributable to any changed
  business meaning.
- **Status:** Confirmed.

### LR-O-003 — technical publisher

- **Named technical publisher:** Dimitri.
- **Production-access and authority boundary:** Dimitri is the sole routine
  technical publisher for the Public Preview. He may edit, preview, validate,
  publish, withdraw, and publicly verify content, but may publish business
  meaning only after attributable approval from Giorgos or an explicitly
  authorized delegate. Technical publication does not authorize Dimitri to make
  unapproved business changes.
- **Safety withdrawal:** Dimitri may immediately withdraw content that is clearly
  unsafe, misleading, or subject to uncertain usage rights, then notify Giorgos.
  Republishing that content requires the applicable business approval.
- **Evidence:** the operator confirmed Dimitri and this boundary on 2026-08-04.
  Before production publication, evidence must verify his appropriately bounded
  Sanity access, the attributable approval handoff, successful technical preview
  and validation, and public verification after publication or withdrawal.
- **Status:** Confirmed.

### LR-O-004 — real-enquiry inbox recipient

- **Named owner:** Giorgos.
- **Responsibility boundary:** Giorgos owns monitoring the agency-owned
  real-enquiry route and the agency's manual follow-up. Internal staffing,
  delegation, and absence coverage are agency operations under Giorgos's
  responsibility; the project does not require a named backup delegate.
- **Evidence:** the operator confirmed Giorgos on 2026-08-04. Before real
  enquiries are enabled, protected launch evidence must identify the agency-owned
  inbox and confirm that it reaches Giorgos. The repository does not need the
  exact address, and no response-time promise is introduced. Dimitri's personal
  Gmail remains limited to synthetic controlled tests.
- **Status:** Confirmed.

### LR-O-005 — delivery-recovery and incident owner

- **Named owner:** Dimitri.
- **Authority and escalation boundary:** Dimitri owns technical recovery when
  transactional-email delivery is uncertain or bounded retries are exhausted.
  He receives only data-minimized alert context, checks the recorded delivery
  state, and chooses a safe recovery action without blind duplicate sends or
  asking the visitor to resubmit. If an agency notification failure could leave
  an accepted request unnoticed, he alerts Giorgos through the later validated
  route.
- **Evidence:** the operator confirmed Dimitri on 2026-08-04. Before real
  enquiries are enabled, separate Launch Readiness evidence must verify the alert
  route, retry timing, recovery procedure, access boundary, and an exercised
  recovery outcome.
- **Status:** Confirmed.

### LR-O-006 — manual backup, deletion, and restore operator

- **Named technical operator:** Dimitri.
- **Authorization boundary:** Dimitri owns the manual encrypted Neon export files
  outside the application, deletes each no later than thirty days after creation,
  and performs a restore only through the later approved authorization procedure
  in an isolated environment. This assignment does not itself authorize
  production-data access, backup creation, or restore execution.
- **Evidence:** the operator confirmed Dimitri on 2026-08-04. Before real
  enquiries are enabled, separate Launch Readiness evidence must verify the
  schedule, export and encryption method, key custody, controlled storage,
  deletion record, explicit restore authorization, and an exercised isolated
  restore that reapplies required deletions before production use.
- **Status:** Confirmed.

## Acceptance Review

LR-O-001 through LR-O-006 are Confirmed. A focused accepted-authority audit found
no remaining material ownership or escalation assignment within this bounded
subject.

The named agency retention and data-rights owner, provider-account control, exact
operating procedures, and executable evidence remain separate Launch Readiness
subjects. They are not silently treated as resolved here.

The operator accepted the complete register on 2026-08-04 and authorized
completion of the existing draft pull request, required-check monitoring, squash
merge, merged-branch deletion, and isolated-worktree cleanup. This register
remains the durable Launch Readiness artifact; there is no raw `GRILLING.md` path
to remove.

**Status:** Accepted.

## Accepted Artifact Boundary

These accepted assignments do not authorize implementation, provider
configuration, production-data access, deployment, or launch. Later Launch
Readiness subjects own the unresolved validations identified above. Any future
change to an assignment must be explicit and must preserve or deliberately
reconcile its accepted authority boundary.
