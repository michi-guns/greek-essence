# Consultation Scheduling Grilling

## Status

Active — partially complete; D-003 is blocked pending the approved exploratory
technical spike.

## Purpose

Define the public meaning and agency-facing operating boundary of online
consultation scheduling for the Public Preview. This subject changes the accepted
Consultation Request boundary: a visitor may select an offered consultation slot
instead of only asking the agency to propose one by email.

It does not choose a calendar provider, framework, database schema, UI component,
or implementation mechanism. Those are later Foundation Design or bounded
implementation work after the product boundary is settled.

## Inherited Boundaries

- A consultation concerns trip-planning help. It is not a travel reservation,
  supplier commitment, payment, or confirmed Booking.
- The appointment flow uses only agency-offered days and time slots.
- A submitted appointment request remains private transactional data: it is
  durably saved before the site claims success, and agency and visitor emails are
  independent outcomes.
- No customer account, CRM, staff dashboard, or automated post-meeting workflow
  is introduced. Greek Essence handles the consultation after the appointment.
- The existing minimal form privacy presentation remains required: concise
  explanation, full-notice link, and read-only acknowledgement. This subject does
  not replace the later public-launch legal and privacy evidence.

## Locked Decisions

### D-001 — Online Consultation Appointment

A visitor may choose an agency-offered day and time slot to schedule a
consultation meeting online. The resulting appointment is a confirmed
consultation commitment, not a Booking Request, travel reservation, availability
claim about an Experience, supplier commitment, or payment obligation.

The site must make clear what the meeting concerns and must not imply that
selecting a consultation slot confirms travel services. After the appointment is
created, Greek Essence owns the human consultation and all later travel planning.

This replaces the earlier exclusion of automated scheduling only for the
Consultation Request journey. It does not reopen the accepted scope of Booking
Request, General Contact, payments, customer accounts, CRM, or staff dashboards.

### D-002 — Agency-Controlled Calendar Is Authoritative

One agency-controlled calendar is the authoritative availability source. Greek
Essence shows only slots currently offered by that calendar and reserves a
selected slot when scheduling succeeds. The visitor then receives a truthful
consultation-appointment confirmation.

The exact calendar provider, connection, availability query, conflict handling,
and revalidation mechanism remain later technical design.

## Open Questions

- D-003 (blocked): How do agency employees manage the authoritative calendar
  without expanding the Public Preview into a staff dashboard or CRM? The
  operator approved the exploratory custom-scheduling spike before this choice
  is accepted; it is tracked as Trello [WU-41](https://trello.com/c/31Gc85MP).
- D-004: What appointment details are shown and collected before scheduling?
- D-005: What visitor-visible change, cancellation, no-show, and unavailable-slot
  behavior is supported at launch?
- D-006: What meeting format, duration, lead time, timezone, and operating-hours
  rules define an offered slot?

## Next Question

### D-003 — Staff Calendar Management Boundary

Giorgos needs employees to manage availability easily. The currently accepted
Public Preview excludes staff dashboards and CRM, so a new internal management
surface must be chosen deliberately rather than added as an implied "mini"
feature.

The operator approved an exploratory technical spike to test a small
Greek Essence owned scheduling engine before choosing between an external
calendar surface and a limited internal calendar-management surface. No
production implementation is authorized. Resume D-003 after the spike records
an evidence-based verdict.

1. **(recommended): Employees manage availability in the agency-controlled
   calendar itself.** Greek Essence reads and reserves its offered slots but does
   not build a staff management dashboard. This keeps employee work in a familiar
   calendar surface and preserves the Public Preview's no-dashboard boundary.
2. **Build a limited Greek Essence calendar-management dashboard.** Authorized
   employees create, change, and remove slots inside the site. This can be simple
   visually, but it introduces staff authentication, authorization, protected
   admin access, calendar-management audit behavior, and a new operational
   support surface.
3. **Only Dimitri manages availability.** This is technically smallest but does
   not satisfy Giorgos's request for employee-managed availability and creates a
   delivery bottleneck.

## Continuation Rule

Persist each accepted decision before advancing. If an answer reveals an
unaccepted provider, data, privacy, or technical constraint, record the
dependency and route it to the owning layer rather than silently deciding it in
this product ledger.
