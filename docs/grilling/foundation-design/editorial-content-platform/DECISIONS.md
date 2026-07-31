# Editorial Content Platform Decisions

Accepted by the operator on 2026-07-31 after Foundation Design grilling.

This document defines how Sanity represents, validates, previews, publishes,
withdraws, and evidences Greek Essence's bilingual public editorial content, and
how Next.js renders, searches, caches, and refreshes that published content for
the Public Preview Release.

It does not authorize application implementation, dependency installation,
Sanity project configuration, schema migration, deployment, production access,
or actual content approval. Exact schema field names, Studio configuration,
validation code, document actions, preview routes, cache APIs, webhook secrets,
timing, monitoring, named production owners, provider-plan validation, and
launch evidence remain downstream work.

## Accepted Context

- Sanity owns editable public and catalogue content. Private customer and Request
  data never enters Sanity.
- Next.js owns the public website, authenticated draft preview, server-side
  content queries, route rendering, localized search presentation, and cache
  revalidation endpoint.
- The immutable published Sanity root document ID is the shared identity for a
  public content item. Localized titles, slugs, and URLs remain editable
  attributes rather than identity.
- English and Greek public experiences must be complete, separately authored,
  meaning-equivalent, and approved before publication. Missing content is not
  copied silently from the other language.
- A useful standalone Destination may publish without a published Experience
  when it satisfies the accepted Destination completeness boundary.
- Every published Experience has at least one genuinely valid published
  Destination relationship, one accepted launch type, approved public content
  and media, and an explicit requestability choice.
- All genuinely valid Destination relationships on an Experience are equal.
  There is no required primary Destination or relationship-role taxonomy.
- Requestability means only that Greek Essence is willing to receive a Booking
  Request. It does not assert availability, reservation, or confirmed booking.
- Greek Essence, acting through Giorgos or an authorized agency delegate,
  approves public business meaning. The technical publisher operates the
  technical workflow but does not silently become the business approver.
- Public claims, indicative prices, and media uses must satisfy their accepted
  approval and evidence boundaries. Sensitive source material remains outside
  Sanity.
- Optional withdrawn content disappears from public discovery while its former
  localized URLs provide generic recovery without stale public claims, prices,
  or media.
- Zero new recurring platform spend remains the release boundary until a
  separately approved upgrade is supported by real visitor demand.

## D-001 — One Bilingual Document per Public Content Item

One stable Sanity document represents one public Destination, Experience, Home
page, About page, or other confirmed public content item. Shared identity,
relationships, classifications, lifecycle controls, and other genuinely
language-independent facts are stored once in that document.

Visitor-facing English and Greek values are separately authored within the same
document. Titles, summaries, detail copy, calls to action, labels, image text,
slugs, metadata, and other localized meaning must be natural and complete in
each language. The model must not silently mirror one language into the other,
fall back to incomplete text, or treat literal translation as semantic parity.

Publication is coupled: the document becomes or remains public only when both
language experiences are complete, meaning-equivalent, structurally valid, and
currently approved where approval applies. One language cannot be published as
the finished public Experience while the other remains an incomplete draft.

Separate English and Greek documents were rejected because they would duplicate
identity and shared relationships and permit lifecycle drift. A single-language
record with translation fallback was rejected because it would weaken the
accepted complete bilingual release. A shared core plus separate English and
Greek content documents was rejected because three coordinated records per item
would add joins, validation, and recovery paths without proportionate launch
value.

## D-002 — Explicit Document Types, Controlled Singletons, and Embedded Objects

Destinations and Experiences are explicit repeatable Sanity document types.
Their names and structure reflect the accepted catalogue concepts rather than a
generic page abstraction.

Home, About, and any other page confirmed to be unique are controlled singleton
records. Any confirmed shared site concern that requires one authoritative
editable record may use the same singleton pattern. Singleton behavior must
prevent accidental duplicate records; it does not create a new business concept
or approve additional public content.

Smaller structures that have no independent public identity or lifecycle are
reusable objects embedded in their owning document. Representative examples
include bilingual calls to action, image-use metadata, indicative-price groups,
and approval groups. Embedded objects are validated with their owner and do not
publish, withdraw, or receive public routes independently.

A generic all-purpose Page model was rejected because it would hide accepted
catalogue and page distinctions behind conditional fields. Independently
published section documents and a general page builder were rejected because
they would add references, ordering, permissions, and lifecycle complexity
without a release requirement.

## D-003 — Current Validation and Meaning-Based Approval Gate Publication

Sanity publication requires automated structural validation and current human
approval of material public business meaning. Validation must enforce the
accepted release invariants that can be determined from structured content,
including:

- complete separately authored English and Greek public values;
- valid document structure and required relationships;
- accepted Experience type and explicit requestability choice where applicable;
- current evidence metadata for governed claims and media uses;
- every required indicative-price qualification when a price is present; and
- relationship-aware publication and withdrawal conditions.

Automated validation cannot decide whether an agency claim is true, a price is
commercially approved, media rights are valid, or legal wording is appropriate.
Giorgos or an authorized agency delegate remains responsible for approving that
business meaning.

Business approval and technical operation are separate. The technical publisher
may perform the entire edit, authenticated preview, publish, verification, and
withdrawal pipeline alone; no second technical publisher or technical approver
is required. A specific instruction from the agency approver is sufficient
approval for that exact business change. For example, an instruction to replace
an indicative price with an approved value and publish it does not require the
technical publisher to send the implemented value back for redundant approval.

Meaning-preserving corrections may be published without renewed business
approval. These include spelling, punctuation, formatting, intended internal
links, rendering defects, and technical repair of an already approved asset when
its identity, meaning, and approved use remain unchanged. A material edit to a
claim, price, inclusion, availability statement, service meaning, legal or
payment wording, or media use invalidates the affected prior approval until the
new meaning is approved.

The technical publisher may immediately withdraw misleading, unsafe, expired,
or technically broken public content without waiting for approval. Protective
withdrawal does not authorize invention or publication of replacement business
meaning.

Requestability remains an explicit Experience choice separate from publication.
It functions publicly only while the Experience is published and all applicable
eligibility gates pass.

A required second technical approver was rejected because it would create an
unaccepted staffing bottleneck without improving business authority. Informal
memory alone was rejected because it cannot support reliable publication or
later diagnosis. A combined publisher-owned “ready to publish” state was
rejected because it would blur agency approval of business meaning with
technical execution. Treating every technical correction as new business
approval was rejected because it would add redundant agency work without
protecting meaning.

## D-004 — Compact Item-Level Evidence Metadata

Sanity stores compact evidence metadata beside every governed public claim,
indicative price, and media use. Each governed item records only the information
needed to determine publication readiness:

- approval status and approved scope;
- the responsible approver identity or configured role;
- approval time;
- a short bounded reference to the supporting evidence; and
- a review or expiry date only when one applies.

Document readiness is derived from the current item-level evidence. Missing,
expired, out-of-scope, or materially stale evidence blocks publication or
requires removal of the affected optional content. A material edit stales the
approval associated with the changed item without making unrelated approvals
ambiguous.

Indicative-price metadata preserves the accepted amount or “from” value,
currency, charging basis, key inclusions, review date, confirmation warning, and
approval reference. Media metadata identifies the approved asset, public use
scope, approver, evidence reference, and any applicable expiry. Exact field
layout and change-detection mechanics remain bounded schema design.

Sensitive contracts, identity documents, private correspondence, and unrelated
business files remain in an appropriate agency-controlled location outside
Sanity. Sanity stores only a bounded reference; the metadata does not prove legal
or commercial validity and does not transfer approval responsibility to the
technical publisher.

Ordinary copy that does not contain a governed claim, indicative price, or
media-rights dependency does not receive this additional evidence metadata.

One document-level approval summary was rejected because changing one image,
price, or claim would make the whole approval ambiguous. Separate reusable
Evidence documents were rejected because they would add a record family,
permissions, references, and lifecycle disproportionate to the preview.

## D-005 — Authenticated Draft Preview and Minimal Withdrawn Version

Each content document uses Sanity's normal private draft and published versions.
The technical publisher previews the complete bilingual draft through
authenticated Next.js Draft Mode in the real website layout. Ordinary visitors,
public search, and public discovery read only the published perspective.

Publishing replaces the English and Greek public experience together. The
published source revision is available for the bounded downstream snapshot and
technical diagnosis already required by accepted system-boundary decisions.
Sanity revision history may support comparison or restoration during the
provider's available retention period, but it is not a permanent public archive
or a substitute for immutable accepted Request history. Restored or
reconstructed content returns through a new private draft and current validation
and approval before republication.

Withdrawing optional content publishes a minimal withdrawn version under the
same immutable Sanity root document ID. The published withdrawn version retains
only the lifecycle state and former English and Greek route information needed
to recognize those URLs. Stale detail copy, claims, prices, and media are absent
from the published perspective.

Listings, navigation, filters, search, and Booking Request actions exclude the
withdrawn item. Its former localized routes render the accepted generic
bilingual recovery journey. An unrelated unknown URL keeps normal not-found
behavior.

A minimal withdrawn version cannot replace a required service, request, privacy,
or legal page while a dependent journey remains active. Such a page must be
replaced or redirected, or the dependent journey must be disabled honestly.
Before Destination withdrawal, affected Experience relationships must satisfy
the accepted relationship-aware withdrawal rules.

A separate Withdrawal Route document was rejected because it would create a
second identity, reference, and cleanup lifecycle for every withdrawn item.
Keeping complete stale content in the published perspective behind a status flag
was rejected because an incorrect query or another consumer could expose old
claims, prices, or media.

## D-006 — Cached Published Content with Precise Webhook Revalidation

Public Next.js Server Components read only Sanity's published perspective and
cache editorial data for fast delivery and controlled provider usage. Cached
data is associated with content identity and every affected detail, catalogue,
relationship, route-recovery, and localized-search surface.

After publication or withdrawal, Sanity sends a secured and verified webhook to
a Next.js Route Handler. The handler invalidates all affected cache groups for
both languages. The next request regenerates them from current published Sanity
truth without a website deployment.

A conservative time-based expiry is also required so a missed webhook cannot
leave stale content online indefinitely. Exact Next.js cache APIs, tag names,
webhook signature mechanics, fallback interval, and operational alerting remain
bounded technical design and Runtime Foundations work.

Localized search uses a cached projection containing only published titles and
summaries for the visitor's selected language. It never exposes drafts,
other-language text, or withdrawn items. Publication and withdrawal refresh the
applicable search projections together with detail routes, listings, related
content, and former-URL recovery.

The technical publisher verifies material publications and withdrawals on the
public site after publishing. Launch Readiness must prove that publication,
withdrawal, webhook authentication, cache invalidation, fallback expiry, and
localized-search refresh behave as accepted in the production configuration.

Sanity's Live Content API was rejected because near-real-time behavior exceeds
the editorial need and current first-party guidance identifies additional
Sanity-request and Vercel-write risk with Next.js 16 that conflicts with the
zero-recurring-spend market-validation boundary. Uncached Sanity queries on every
visitor request were rejected because they add latency, runtime dependency, and
quota use. Build-time-only content was rejected because it would make routine
publication and urgent withdrawal depend on a technical deployment.

## Cross-Cutting Invariants

- Drafts, incomplete translations, and unapproved material remain private.
- Shared facts are stored once; English and Greek visitor-facing meaning remains
  separately authored and publishes together.
- Public queries, search, cache regeneration, and route rendering use only the
  published perspective except inside authenticated draft preview.
- Agency approval governs public business meaning; technical publication does
  not silently transfer that authority.
- Meaning-preserving technical correction is not treated as new business
  meaning, while material change stales the affected approval.
- No stale, expired, unapproved, or withdrawn claim, price, or media use remains
  publicly discoverable.
- Sanity withdrawal never deletes or rewrites an accepted Neon Request or its
  bounded immutable snapshot.
- Public content freshness does not depend solely on a successful deployment or
  a single webhook event.
- Required public pages and their dependent journeys remain consistent.
- Provider revision history, caches, evidence references, and email are not
  substitutes for accepted transactional authority.

## Explicit Exclusions

The Public Preview does not include:

- separate English and Greek records for one public content identity;
- language fallback that exposes incomplete or mixed-language content;
- a generic all-purpose page model or independently published section builder;
- private customer or Request data in Sanity;
- a second technical approval role;
- Sanity as a contract, identity-document, or sensitive evidence repository;
- a reusable Evidence-document system;
- complete stale public documents hidden only by query convention;
- a separate withdrawal-record family;
- draft or cross-language content in public search;
- live supplier availability or confirmed-booking meaning;
- automatic public publishing from a content edit;
- a runtime Sanity request for every visitor request;
- required site redeployment for routine editorial publication or withdrawal; or
- near-real-time live-content infrastructure without a separately demonstrated
  need and approved quota or cost boundary.

## Downstream Dependencies

### Bounded Technical Design

Define the exact Sanity schemas, localized field objects, stable-root-ID
handling, reference validation, singleton controls, approval groups,
requestability control, price and media evidence fields, document actions,
minimal withdrawn representation, authenticated preview route, published query
projections, Next.js cache APIs and tags, signed-webhook contract, fallback
interval, and public search implementation without weakening these decisions.

### Transactional Data Platform

Preserve the published root Experience ID and bounded customer-visible snapshot,
including source Sanity revision, without copying the editable catalogue into
Neon or allowing later Sanity changes to mutate accepted Requests.

### Application Architecture

Keep Sanity access, preview authorization, public queries, search projections,
webhook handling, and cache invalidation within explicit server-side boundaries.
Define browser and server entry points and Server or Client Component ownership
without exposing drafts, credentials, or unrestricted CMS access.

### Runtime and Production Foundations

Define environment separation, secrets, webhook verification, provider quotas,
failure monitoring, cache-revalidation recovery, deployment behavior, and
operational diagnostics. Vercel remains the current hosting direction subject to
its accepted commercial gate; Netlify remains only the accepted fallback
direction if that mandatory gate fails.

### Launch Readiness

Confirm named agency approvers, technical publishers, language reviewers,
production account control, actual bilingual content, claims, indicative prices,
media rights, legal and privacy wording, evidence locations, review and expiry
dates, provider-plan facts, and operating procedures. Execute publication,
preview, withdrawal, former-URL recovery, search-isolation, webhook-security,
cache-freshness, accessibility, and production evidence before launch.

External professional review remains required wherever actual package, price,
tax, fee, cancellation, privacy, consumer, media-rights, or travel-industry
wording creates an applicable legal or commercial dependency. That review may
approve or correct actual content; it must not silently weaken the accepted
publication, bilingual, authority, evidence, or truthful-withdrawal boundaries.
