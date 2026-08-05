# Consultation Scheduling Grilling

## Status

Active.

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

## Open Questions

- D-002: What is the authoritative availability source and how does the visitor
  receive a truthful slot-confirmation outcome?
- D-003: What appointment details are shown and collected before scheduling?
- D-004: What visitor-visible change, cancellation, no-show, and unavailable-slot
  behavior is supported at launch?
- D-005: What meeting format, duration, lead time, timezone, and operating-hours
  rules define an offered slot?

## Next Question

### D-002 — Availability Authority and Slot Confirmation

Greek Essence needs one truthful source for the days and times displayed as
available. The choice determines whether selecting a slot immediately creates a
meeting commitment or merely records a preference that staff must still confirm.

1. **(recommended): A single agency-controlled calendar is authoritative.** The
   site shows only its currently available slots and reserves the selected slot
   when scheduling succeeds. The visitor receives a truthful appointment
   confirmation; the later calendar-provider and technical implementation remain
   separate work.
2. **The site publishes a small maintained list of slots.** A technical publisher
   or agency operator updates the list manually. This avoids a calendar
   integration initially, but a stale slot can create a conflicting appointment
   and gives the agency extra daily work.
3. **The site records a preferred day and time for agency confirmation.** This is
   operationally simple, but it is not the online scheduler promised to Giorgos:
   the visitor has only made a request, not scheduled a meeting.

A classic date-and-time selector is a presentation choice; it does not itself
make availability truthful. The product decision is which agency-controlled
source is allowed to promise that a displayed slot can be scheduled.

## Continuation Rule

Persist each accepted decision before advancing. If an answer reveals an
unaccepted provider, data, privacy, or technical constraint, record the
dependency and route it to the owning layer rather than silently deciding it in
this product ledger.
