# Editorial Content Platform Grilling

## Status

Active Foundation Design grill. This ledger does not authorize application
implementation, dependency installation, Sanity project configuration, schema
migration, deployment, or production access.

## Owning Layer and Purpose

Owner: Foundation Design — Editorial Content Platform.

Define the durable Sanity and Next.js foundations for representing, reviewing,
previewing, publishing, withdrawing, rendering, refreshing, and searching Greek
Essence's bilingual public content. Preserve accepted Product and Domain Truth
and the accepted System Boundaries and Domain Representation decisions without
reopening the selected technology stack.

## Accepted Inputs

- Next.js owns the public application and server-side orchestration.
- Sanity owns editable public and catalogue content. Private customer and Request
  data never enters Sanity.
- English and Greek are complete, separately represented, human-approved, and
  meaning-equivalent public experiences. Mixed-language, machine-only, and
  silent-fallback content is not finished public copy.
- Giorgos or an authorized agency delegate approves business content. The
  technical publisher checks technical preview and publication requirements but
  does not become responsible for approving agency facts, claims, prices, media
  rights, or commercial meaning.
- A useful standalone Destination may publish without a published Experience.
  Every published Experience requires at least one genuinely valid published
  Destination relationship, and all valid Destination relationships are equal.
- Every Experience has one immutable published Sanity document ID shared with
  accepted Booking Request records. Localized titles, slugs, and URLs are
  editable attributes rather than identity.
- Experience publication does not enable Booking Requests automatically.
  Requestability is an explicit per-Experience choice and never implies current
  availability or confirmation.
- A published Experience must satisfy its bilingual content, type,
  Destination, claim, media, requestability, and conditional indicative-price
  requirements.
- Withdrawn optional content leaves discovery and provides generic bilingual
  recovery at its former URL without stale claims, prices, or media. Required
  pages must be replaced or redirected, or their dependent journey must be
  disabled honestly.
- Named reviewers, publishers, production access holders, approved launch
  content, provider-account evidence, and completed operational proof remain
  Launch Readiness matters.

## Locked Technical Direction

Do not reopen Next.js or Sanity selection. Exact package versions and provider
configuration are implementation-time work. Current first-party Sanity guidance
recognizes field-level localization in one document and document-level
localization through linked documents as distinct modelling strategies; the
choice here must fit Greek Essence's already accepted identity, bilingual
publication, relationship, and withdrawal invariants.

Reference used for current Sanity capability context:
<https://www.sanity.io/docs/studio/localization>

## Explicit Boundaries

This track may define:

- Sanity document and reference structure;
- English/Greek representation and publication coupling;
- publication, requestability, and relationship validation contracts;
- approval and evidence metadata structure without assigning named people;
- preview, draft, revision, withdrawal, and recovery mechanisms;
- Next.js rendering, caching, revalidation, search, and freshness contracts; and
- durable Sanity roles and permission boundaries without assigning production
  accounts.

This track must not approve actual copy, claims, prices, media rights, legal
wording, named owners, credentials, quotas, account access, or launch evidence.
It must not define private Request storage, Drizzle schemas, application module
layout, deployment topology, or production operations owned by later tracks.

## Locked Decisions

### D-001 — One Bilingual Sanity Document per Public Content Item

Each public content item is represented by one Sanity document containing
separate English and Greek values for visitor-facing content. Shared facts and
relationships—such as Experience type, Destination references, requestability,
and the item's stable identity—exist once in that document rather than being
duplicated per language.

The document may publish only when both complete language experiences and their
applicable human approvals satisfy the publication gate. English and Greek
therefore publish, revise, and withdraw together at the document level rather
than operating on independent public schedules. The localized copy remains
separately written and approved, may be natural rather than literal, must be
meaning-equivalent, and cannot use silent fallback or machine-only text as
finished public content.

This preserves one accepted business item and one immutable published Sanity
document ID across editorial and Request boundaries. It also avoids duplicated
Destination relationships, requestability, withdrawal state, and
cross-language coordination. Exact localized field and object types remain for
the document-structure decision and bounded technical design.

Separate linked documents per language were rejected because they would make
identity, relationships, completeness, requestability, and withdrawal harder to
coordinate without providing a needed independent publication schedule. A
shared core plus separate English and Greek content documents was rejected
because three records per item would add joins, validation, and recovery paths
without proportionate launch value.

### D-002 — Explicit Documents, Controlled Singletons, and Embedded Objects

Greek Essence uses explicit Sanity document types for materially different
public content items. Destinations and Experiences are repeatable document
types. Each confirmed unique public page, including Home and About, has one
controlled singleton record so the publisher cannot create competing copies.
Any confirmed shared site concern that requires one authoritative editable
record may use the same singleton pattern.

Reusable structures—such as localized text, calls to action, media with
approval metadata, and structured page sections—are reusable object definitions
embedded within the document that owns their values. They are not independent
public documents with separate publication, approval, reference, or withdrawal
lifecycles.

This makes Sanity Studio correspond to content items the agency recognizes,
supports type-specific validation, and prevents accidental duplicate one-off
pages. It accepts a modest number of clear schema types instead of one generic
page builder. Only confirmed public surfaces may receive a document or singleton
type; the classification does not invent content, claims, or launch approval.

One generic Page document type was rejected because materially different pages
would depend on conditional fields and editor discipline rather than clear
page-specific structure and publication rules. Independently managed reusable
section documents were rejected because their extra records, references,
approval coordination, and withdrawal paths add complexity without
proportionate preview-release value.

### D-003 — One-Person Technical Publishing with Meaning-Based Approval Gates

Sanity must combine automated publication validation with explicit current
agency approval of material business meaning. Automated errors block publishing
when bilingual completeness, required relationships, conditional fields, or
required claim, media, price, and requestability evidence does not satisfy the
applicable content contract. The technical publisher separately checks the
preview and technical readiness before publishing; no second technical approver
is required.

Giorgos or an authorized agency delegate must approve new or materially changed
business meaning, including prices and inclusions, availability wording,
Experience facts, commercial or trust claims, media rights, and legal or policy
wording. An instruction approving a specific change before implementation is
sufficient approval for that exact change: the technical publisher may then
edit, validate, preview, and publish it without a second post-edit approval.

The technical publisher may independently publish meaning-preserving
corrections to already approved content, such as typography, formatting, an
internal link repaired to its approved intended target, or replacement of a
technically broken asset with the same approved media. These corrections must
not expand or reinterpret the approved claim, offer, obligation, or media use.
A material edit makes the affected approval stale and blocks publication until
the changed meaning is approved.

The technical publisher may also withdraw misleading, stale, unsafe, or
technically broken content immediately to protect visitors. Protective
withdrawal does not approve replacement content or permit materially altered
content to be republished without the normal approval gate.

Requestability remains an explicit shared Experience choice, separate from
publication. It is effective only for a currently published Experience that
satisfies the applicable eligibility and approval gates. Exact evidence fields,
approval identity representation, and change-invalidation mechanics remain
D-004 or bounded technical design.

A combined publisher-owned “ready to publish” state was rejected because it
would blur agency approval of business meaning with technical execution.
Approval kept only in informal external conversation was rejected because it
could become detached from the revision and meaning being published.

### D-004 — Compact Item-Level Evidence Metadata

Each governed claim, indicative price, and media use carries compact evidence
metadata beside that item in its owning Sanity document. The document's
publication readiness is derived from the current state of every applicable
item rather than from one page-level approval checkbox.

The metadata records the approval status and scope, the approving role or
configured identity, approval time, a short evidence or source reference, and a
review or expiry date only when applicable. Exact named production approvers
and access remain Launch Readiness matters. A changed governed item must no
longer inherit metadata that approved materially different meaning or use.

Indicative-price metadata also preserves the already required currency,
charging basis, key inclusions, review date, and confirmation warning. Media
metadata identifies the approved asset and its approved use scope. Ordinary
copy that does not carry a governed claim, price, or media-rights dependency
does not receive this additional evidence record.

Sensitive contracts, identity documents, and unrelated business files remain
outside Sanity in an appropriate agency-controlled location. Sanity stores only
the bounded reference needed for the technical publication check; the metadata
does not assert that the underlying evidence is legally or commercially valid
and does not transfer approval responsibility to the technical publisher.

One document-level approval summary was rejected because changing one image,
price, or claim would make the whole approval ambiguous. Separate reusable
Evidence documents were rejected because their additional record family,
permissions, references, and lifecycle would add disproportionate complexity
for the preview.

## Open Questions

- D-005: How should drafts, preview, revisions, withdrawal, and former-URL
  recovery work together?
- D-006: How should Next.js rendering, caching, revalidation, localized search,
  and freshness preserve published Sanity truth?

## Next Question

ID: D-005

Owning layer: Foundation Design.

Topic:
Drafts, preview, revisions, withdrawal, and former-URL recovery.

Prompt:
How should one Sanity document move from private draft to public revision and
later withdrawal while preserving a truthful generic recovery page at its former
English and Greek URLs?

Options:

1. (recommended): **Use Sanity's normal draft and published versions, an
   authenticated Next.js preview, and a minimal withdrawn version of the same
   document.** Editors preview the complete bilingual draft against the website;
   visitors read only the published version. Publishing replaces both languages
   together and records the source revision. Withdrawal publishes a minimal
   shell under the same stable document ID containing only withdrawal state and
   the former localized route information needed for generic recovery; stale
   detail copy, claims, prices, and media are absent from the public version.
   Discovery excludes the shell, while both former URLs render the accepted
   generic recovery journey. Any later republication starts from private content
   and must pass current validation and approval again.
2. **Unpublish the content document and create a separate Withdrawal Route
   document.** The separate record stores the former localized URLs and generic
   recovery type while the original remains private. This keeps withdrawal data
   isolated but adds another record, reference, identity, and cleanup lifecycle
   for every withdrawn item.
3. **Keep the complete withdrawn document published with a withdrawal flag and
   rely on Next.js queries to hide its stale fields.** This is mechanically
   simple and keeps restoration easy, but stale claims, prices, and media remain
   in the published data and could be exposed by an incorrect query or another
   consumer.

Why this matters:

Sanity can keep a private draft alongside the currently published version.
Next.js can use an authenticated preview mode so the publisher sees that draft
inside the real site layout without exposing it to ordinary visitors. Sanity
also retains revision history for the provider's available retention period,
but that history is not treated as a permanent public archive.

Withdrawal needs more than deleting the document. For example, an old link to
the Paros Sailing Tour must show a generic bilingual “no longer listed” journey,
not a normal not-found page and not the old price and imagery. The recommended
minimal withdrawn shell lets the same immutable document identity and former
localized URLs answer that request without leaving stale visitor content in the
published version or introducing a second withdrawal-record family.

This optional-content mechanism does not satisfy withdrawal of a required
service, request, privacy, or legal page. Such a page must still be replaced or
redirected, or its dependent journey disabled honestly, as already accepted.

After answer:

- Lock the draft/published preview boundary, revision use, withdrawal
  representation, former-route recovery, and republication gate.
- Preserve exact preview integration and field names for bounded technical
  design.
- Store D-006 as the next question.
