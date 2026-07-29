# Consultation Request Grilling

## Status

Ready for operator acceptance as feature 3 of 8. D-001 through D-007 are
locked; Catalogue Discovery is accepted and distilled.

This grill does not authorize implementation. Use [../DECISIONS.md](../DECISIONS.md)
and [../protocol.md](../protocol.md).

## Locked Project Context

- A consultation request asks the agency to help plan a trip.
- The agency follows up manually by email or telephone.
- Online payment, a post-enquiry questionnaire, and automated scheduling are
  deferred.
- Real requests must be saved safely and handled as private personal data.

## Scope

Define the visitor goal, minimum useful information, consent and privacy
language, confirmation wording, manual handoff, and reachable error and retry
behavior for consultation requests.

## Locked Decisions

### D-001: Collect a short structured trip brief initially

The initial consultation request will collect enough structured information for
the agency to understand the broad trip and respond usefully without becoming
the detailed post-enquiry questionnaire that is deferred from this release.

The brief covers contact details, approximate travel timing, party size,
destinations or interests, optional budget guidance, a short notes field,
preferred contact method, and the required privacy acknowledgement. Exact
required and optional field rules remain for D-003; D-001 establishes the
information depth rather than the final field schema or wording.

Detailed accommodation, transport, daily-planning, accessibility, traveler
identity, and other potentially sensitive questions are not part of the
initial brief. If needed, the agency gathers them during appropriate manual
follow-up. This keeps the first contact proportionate while avoiding the extra
back-and-forth likely from a contact-only callback request.

D-002 subsequently establishes email as the only contact method for this
journey, so the D-001 preference field is no longer needed. This narrows the
brief without changing its intended information depth.

Rejected alternatives:

- A contact-only callback request, because it gives the agency too little trip
  context for a useful first response.
- A detailed planning intake, because it recreates the deferred questionnaire,
  increases abandonment risk, and may collect sensitive data too early.

### D-002: Use email only for consultation acknowledgements and follow-up

The consultation request will require an email address and use email both for
the automated arrival acknowledgement and the agency's personal follow-up. The
form will not ask for a telephone number or contact-method preference.

This keeps the journey simple, avoids collecting an additional piece of
personal data, and gives every accepted request the same reliable channel for
the required acknowledgement. Telephone remains part of the agency's broader
manual process where another journey or later direct conversation supports it;
this decision applies specifically to the initial consultation-request journey.

The public journey will show a response window only after the client confirms
one the agency can reliably meet. Until then, it may say that the agency will
follow up by email but must not promise a deadline. The client-confirmed
response expectation remains a launch validation dependency.

Rejected alternatives:

- Requiring email while optionally collecting a telephone number, because the
  operator chose not to offer telephone follow-up in this journey.
- Requiring both email and telephone, because it collects unnecessary personal
  data and may deter visitors who do not want a call.

### D-003: Require routing details and minimum trip context only

An initial consultation request requires the visitor's name, email address,
party size, at least one destination or interest, and the privacy
acknowledgement whose presentation and legal boundary remain for D-004.

Approximate timing is optional and supports a clear “not sure yet” response.
Budget guidance and the short notes field are also optional. Exact destination
and interest controls, budget ranges and currency, and bilingual field wording
need example-led client validation and alignment with the accepted catalogue
content rather than invented taxonomies.

The initial form must not request a telephone number, individual traveler
identities, exact birth dates, passport information, medical details, or
detailed accessibility information. The party-size field asks only for the
group count. If the agency later needs more detailed or sensitive information,
it gathers that information during an appropriate manual follow-up rather than
through this initial request.

Rejected alternatives:

- Requiring every part of the brief, because visitors may not yet know their
  dates or budget and should not need to invent notes merely to submit.
- Requiring only contact details, because that would not provide the minimum
  trip context needed for a useful first agency response.

### D-004: Provide a just-in-time privacy summary and acknowledgement

Beside the submission action, the form will explain in concise, plain language
that Greek Essence will save and use the submitted details to handle the
consultation request and reply by email. It will link to the full privacy notice
and require an unchecked acknowledgement worded as “I have read the privacy
notice” or an approved bilingual equivalent.

The acknowledgement records that the notice was presented; it must not be
described as blanket consent or treated as consent to unrelated processing. No
marketing consent is included, consistent with newsletter functionality being
excluded from the product.

Before public launch, the client and an appropriately qualified reviewer must
confirm the controller identity and contact details, processing purposes,
applicable lawful basis, recipients or recipient categories, retention period,
visitor rights, complaint route, international-transfer facts where relevant,
and the final English and Greek wording against the agency's actual processing.
This decision is a product presentation boundary, not legal approval.

Rejected alternatives:

- A required processing-consent checkbox, because it may incorrectly represent
  consent as the lawful basis for handling the visitor's own request and would
  carry withdrawal and genuine-choice requirements.
- A summary and privacy-notice link without acknowledgement, because D-001 and
  D-003 already require an explicit privacy acknowledgement.

### D-005: Show distinct, honest outcomes with a request reference

Validation errors appear at the relevant fields and preserve the entered brief
on the current form so the visitor can correct it. The interface must not claim
that a request was received before it has been safely saved.

After a successful save, the visitor sees that the consultation request was
received, an opaque non-sensitive reference code, the email-only next step, and
only a response window the client has approved as reliable. The reference must
not encode personal information or expose sequential private-record details.

Saving and email delivery remain separate outcomes:

- If the visitor acknowledgement cannot be sent after saving, the page says
  that the request was received but the confirmation email could not be sent,
  shows the reference, and does not ask the visitor to resubmit.
- If an internal agency notification fails after saving, the request remains
  received. The page shows the saved-request success and reference without
  falsely claiming that staff were emailed; monitoring, retry, and staff
  recovery are dependencies of Request Processing and Communications.
- If saving fails, the page clearly says that the request was not received,
  preserves the entered brief for an immediate retry, and offers only
  client-approved alternative agency contact details. It does not expose
  technical error details.

Exact persistence, acknowledgement, notification, retry, duplicate-protection,
monitoring, and recovery mechanics remain for the shared Request Processing and
Communications grill. This feature requires those mechanics to preserve the
visible distinctions above.

Rejected alternatives:

- Simple messages without a reference or email-delivery distinction, because
  they provide insufficient help when visitors or staff resolve uncertainty.
- Treating any email failure as a failed submission, because asking the visitor
  to retry a saved request can create duplicates and contradicts the accepted
  separation between saving and delivery.

### D-006: Keep optional notes with a short persistent safety warning

The optional notes field remains available for ordinary trip context. A
persistent helper beside the field—not placeholder-only text—will say:

> Please don’t include passport, payment, or medical information here.

The approved English warning is intentionally nine words. Its Greek equivalent
must preserve the same concise meaning and receive client review. Placeholder
text, if used at all, may provide a short example but must not carry the safety
instruction because it disappears during entry and is not a reliable accessible
description.

If a visitor submits sensitive information despite the warning, the request
remains in the protected private-data workflow and the notes must not be echoed
into notification email. Exact staff access, redaction, deletion, retention,
and incident handling belong to Request Processing and Communications and need
privacy review.

Rejected alternatives:

- Removing notes entirely, because it would prevent useful trip context that
  the structured fields do not cover.
- Unrestricted notes without a warning, because unnecessary sensitive-data
  entry would remain reasonably foreseeable.

### D-007: Do not add a special age gate to the consultation form

The Public Preview consultation form will not ask for age or birth date, require
an adult-status checkbox, or introduce a child-specific guardian workflow. The
form is an ordinary initial travel enquiry and is not marketed specifically to
children.

This keeps the journey proportionate to the agency context and avoids encoding
a restriction that the operator does not recognize as normal or necessary for
this agency. If the client or an appropriately qualified reviewer later
identifies a concrete legal or operational requirement for an age boundary, it
must return as an explicit change rather than being assumed now.

Rejected alternatives:

- Adult-only confirmation or helper text, because it adds friction and a
  special restriction without evidence that this consultation journey needs it.
- A child-specific submission workflow, because there is no established agency
  requirement for that additional scope.

## Open Questions

None. The remaining facts are named client, legal, content, or downstream
shared-feature validations rather than unresolved Consultation Request product
choices.

## Next Question

ID: Acceptance check

Topic:
Whether the Consultation Request grill is complete enough to distill into
durable accepted decisions.

Prompt:
Do you accept Consultation Request decisions D-001 through D-007 as the feature
boundary for the Public Preview Release?

Options:

1. (recommended): **Accept and distill the feature decisions.** Create the
   self-contained `DECISIONS.md`, verify that it preserves every accepted
   choice, and then request separate path-specific approval before removing this
   raw ledger.
2. **Continue grilling only if a concrete material gap remains.** Identify the
   traveler or agency workflow that is still undefined; do not add speculative
   edge cases.

Why this matters:
Acceptance makes these decisions feature authority for later canonical
documentation and bounded implementation planning. It does not authorize
implementation, dependency installation, migration, or deployment.

After answer:

- If accepted, distill all durable decisions without changing their meaning.
- Verify the distillation against this raw ledger.
- Ask separately for approval to remove
  `docs/grilling/consultation-request/GRILLING.md`.
