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

## Open Questions

- D-004: How should claim, price, and media evidence metadata support technical
  publication checks without transferring business approval?
- D-005: How should drafts, preview, revisions, withdrawal, and former-URL
  recovery work together?
- D-006: How should Next.js rendering, caching, revalidation, localized search,
  and freshness preserve published Sanity truth?

## Next Question

ID: D-004

Owning layer: Foundation Design.

Topic:
Claim, indicative-price, and media evidence metadata.

Prompt:
How should Sanity record enough evidence information for the technical publisher
to verify claims, indicative prices, and media before publication without
turning Sanity into a large approval or document-management system?

Options:

1. (recommended): **Keep compact evidence metadata beside each governed claim,
   price, or media use and derive the document's readiness from it.** Record the
   approval status and scope, approving role or identity, approval time, a short
   evidence or source reference, and a review or expiry date only when the item
   requires one. Price metadata also carries its already required currency,
   charging basis, inclusions, review date, and confirmation warning. Media
   metadata identifies the approved asset and use scope. Sensitive contracts,
   identity documents, or unrelated business files remain outside Sanity in an
   appropriate agency-controlled location; Sanity stores only the bounded
   publication reference needed for the check.
2. **Keep one document-level approval summary.** Record who approved the whole
   page, when, and where supporting evidence can be found. This is simpler, but a
   single changed image, price, or claim can make the whole approval ambiguous
   and gives the publisher less help identifying what needs reapproval.
3. **Create separate reusable Evidence documents and reference them from every
   claim, price, and media use.** This supports one evidence record shared across
   several pages, but introduces another independently managed record family,
   reference lifecycle, permissions surface, and withdrawal problem that may be
   disproportionate for the preview.

Why this matters:

The publisher needs to answer a practical question before pressing Publish:
“What proves that this particular claim, price, or image is approved for this
use?” A simple page-level checkbox cannot reliably answer that when one element
changes. At the other extreme, a separate evidence-management application would
add unnecessary work and may place sensitive agency records in the CMS.

For example, the Paros Sailing Tour may show one approved image and an indicative
“from €150 per person” price. The recommended model keeps a small approval and
source record next to the image use and another next to the price. Sanity can
then flag an expired media use or overdue price review without deciding whether
the rights or commercial terms are legally valid. Giorgos or an authorized
delegate still owns that approval; the metadata only helps the technical
publisher verify that the required evidence exists and is current.

After answer:

- Lock the evidence-metadata placement, minimum categories, sensitive-file
  boundary, and publication-readiness relationship.
- Preserve exact field names and Sanity Studio presentation for bounded
  technical design.
- Store D-005 as the next question.
