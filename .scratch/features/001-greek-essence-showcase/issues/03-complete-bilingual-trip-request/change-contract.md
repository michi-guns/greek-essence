# Change Contract — Complete the accessible bilingual four-step trip request

Issue: `03-complete-bilingual-trip-request` · Method: `tdd-solo` · Milestone: `complete-resilient-trip-request`

## Goal / postcondition

After this slice, an English- or Greek-language visitor can open the static Plan My Trip route directly or from the allow-listed Paros context, complete the exact Trip, Travelers, Preferences, and Contact steps with accessible active-step validation and safe child-age correction, and produce a canonical valid `TripRequestValues` result without sending data, persisting a draft, navigating to confirmation, or claiming submission success.

## Traces

FR-004, FR-005, FR-013, FR-015; NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-007, NFR-008; DEC-003, DEC-008, DEC-010, DEC-012, SUBDEC-001, SUBDEC-004.

## Soft scope — edit freely

| Path | Create / edit | Reason & pattern to match |
| --- | --- | --- |
| `app/[locale]/plan-my-trip/page.tsx` | create | Add the static localized route, allow-listed public destination context, and metadata; mirror locale validation, `setRequestLocale`, canonical/alternate metadata, `noindex,nofollow`, and skip-link mechanics in `app/[locale]/destinations/paros-antiparos/page.tsx`, but compose the SPEC §5.4 minimal form shell rather than the destination page's full navigation. |
| `components/layout/trip-request-header.tsx` | create | Provide only the localized Home/safe-exit action and route-preserving language control required by the minimal Plan My Trip shell in SPEC §5.4; reuse `i18n/navigation.ts`, `lib/routes.ts`, and the visual/accessibility conventions of `components/layout/site-header.tsx` without changing that full shared header. |
| `components/forms/trip-request-form.tsx` | create | Own the one client form island, four-step progression, active-step validation, error-summary focus, correction behavior, Back behavior, and validated final state; use the existing shallow `components/*` organization and semantic token classes from `app/globals.css`. |
| `components/forms/steps/trip-step.tsx` | create | Render only the Step 1 destination and date controls from SPEC §6.1 using persistent labels and React Hook Form context supplied by `TripRequestForm`. |
| `components/forms/steps/travelers-step.tsx` | create | Render only Step 2 party, child-age, and trip-type controls, including the explicit destructive-reduction confirmation observed through the form UI. |
| `components/forms/steps/preferences-step.tsx` | create | Render only Step 3 interest, pace, and privacy-conscious notes controls with canonical untranslated IDs. |
| `components/forms/steps/contact-step.tsx` | create | Render only Step 4 contact controls and required privacy acknowledgement, including phone-dependent contact-method availability. |
| `lib/trip-request-schema.ts` | create | Define strict editable/canonical types, defaults, allow-listed IDs, `validateStep`, and final normalization from SPEC §6.1; follow the repository's strict Zod/type pattern in `content/schemas/showcase.ts`. |
| `messages/en.json` | edit | Add complete English form, option, progress, helper, validation, dialog, and correction messages while retaining keys still consumed by the quality-lab fixture. |
| `messages/el.json` | edit | Add the structurally identical natural Greek message namespace, preserving the recursive parity pattern in `tests/unit/messages/parity.test.ts`. |
| `app/globals.css` | edit | Add only the form-route layout, control, progress, error, selected, dialog, and responsive styles consumed by this issue; reuse the existing Greek Essence semantic token/focus/reduced-motion foundation. |
| `package.json` | edit | Add only an exact-version `react-hook-form` runtime dependency required by the accepted design; preserve standalone pnpm `11.17.0`, existing scripts, and the dependency policy. |
| `pnpm-lock.yaml` | edit | Record only the package-manager-generated lockfile change for the exact `react-hook-form` addition; do not hand-edit unrelated resolution state. |
| `unlighthouse.config.ts` | edit | Add representative English and Greek Plan My Trip paths to the existing scan include list so the new substantial form island is measured without lowering any score or route budget; preserve the current Home/Paros/quality-lab samples. |
| `tests/unit/forms/trip-request-schema.test.ts` | create | Focused RED→GREEN tests for the public editable/step/final validation and normalization seam using known-good literals from SPEC §6.1. |
| `tests/unit/forms/trip-request-form.test.tsx` | create | Focused component tests for progression, correction, Back, dependent child ages, confirmation, and final valid state through labels/roles rather than component internals; follow `tests/unit/setup.ts`. |
| `tests/unit/messages/parity.test.ts` | edit | Retain recursive key-set parity and update the fixture-only description to cover the bilingual showcase messages. |
| `tests/e2e/showcase-journey.spec.ts` | create | Add the compact/wide form-only critical journeys for direct/contextual entry, keyboard validation/correction, child-age handling, and EN/GR presentation, reusing `tests/e2e/browser-guards.ts`. |
| `tests/e2e/localization-and-quality.spec.ts` | edit | Extend the existing localized metadata and responsive route matrix only for the two Plan My Trip routes; preserve existing Home, Paros, quality-lab, security-header, and browser-guard coverage. |
| `tests/e2e/accessibility.spec.ts` | edit | Add representative EN/GR Plan My Trip states to the existing axe A/AA route/state gate without duplicating the full form matrix. |

## Hard walls — STOP if hit

- **Issue 04 persistence/reset boundary** — do not create `lib/form-draft.ts`, access `localStorage`, implement debounce/expiry/restore/flush behavior, preserve form values across locale navigation, or add Start Over persistence semantics. Those are explicitly assigned to `04-preserve-trip-request-progress`; this issue may render only correction confirmation required to prevent child-age loss.
- **Submission and confirmation boundary** — do not create or call `POST /api/trip-request`, email/Resend modules, confirmation pages, submission IDs, pending/retry/success behavior, or network transport. The final step validates canonical values only and must not send or claim success; these belong to `submit-safely-and-confirm`.
- **Locale and route identity** — preserve `routing.locales`, always-prefixed English/Greek routes, `/` → `/en`, invalid-locale 404 behavior, and the public route IDs/signatures in `lib/routes.ts`; changing `i18n/routing.ts`, `proxy.ts`, or those route identities requires a ScopeExpansionRequest.
- **Canonical form contract** — preserve the exact four step names/order, accepted fields/defaults/options/grouping, canonical untranslated IDs, normalization, date/party/child-age/contact/privacy rules, and explicit omissions in SPEC §6.1 and SUBDEC-001. Adding budget, residence, accommodation, marketing consent, another notes field, or any unsupported field is out of scope.
- **Static-first and bounded client boundary** — the route shell and metadata remain statically renderable and `TripRequestForm` is the only substantial client island for this slice; no server action, runtime content API, global state library, generalized form framework, analytics, database, or new dynamic server boundary is allowed.
- **Privacy and artifact boundary** — no personal data may enter URLs beyond the allow-listed public destination ID, metadata, logs, console output, fixtures, screenshots, or browser artifacts; synthetic test data and the sensitive-free-text warning are mandatory.
- **Existing quality budgets and viewports** — do not lower Unlighthouse budgets, remove browser guards, weaken axe rules, or change the 390 × 844 and 1440 × 1024 sign-off viewports. The inherited English Home LCP exception remains technically failing and is not converted to a pass by this issue.
- **Unrelated accepted showcase work** — preserve Home, Paros, shared media/content, headers/footers, security headers, and quality-lab behavior except for ordinary integration needed to link the already-existing Plan My Trip route identity.

## Seams to test

- **`validateStep(step, editableValues)` and final normalization in `lib/trip-request-schema.ts`** — public validation boundaries expose active-step errors and either canonical `TripRequestValues` or safe field/form errors without accepting unknown keys or unsupported values.
- **Rendered `TripRequestForm` progression and correction** — labels, controls, linked error summary, focus, Continue/Back behavior, progress, and the final validated state are observable through accessible roles and text, not component internals.
- **Rendered dependent child-age controls and destructive-reduction dialog** — the public form UI preserves existing ages on increase and requires an explicit cancel/confirm decision before populated ages are discarded.
- **Localized Plan My Trip route and metadata** — HTTP/rendered output exposes direct/contextual defaults, English/Greek message parity, static route metadata, canonical/alternate links, robots policy, responsive layout, and browser health.

## Triangulating acceptance cases

**Seam: `validateStep(step, editableValues)` and final normalization**

- [ ] Clean direct defaults validate Step 1 because flexible dates are enabled and `help-me-choose` is selected, but Step 2 reports required `tripType`; validation is active-step-only (SPEC §6.1 defaults/rules and FR-004).
- [ ] A complete known-good family request with `paros-antiparos`, exact `2026-05-03`/`2026-05-03` dates, adults `"2"`, children `"2"`, ages `"4"`/`"11"`, trip type `family`, interests `culture`/`gastronomy`, pace `balanced`, trimmed Greek name, lowercased email, optional phone whitespace, email contact, and acknowledged privacy produces canonical numbers, same-day dates, display-order arrays, preserved Unicode text, and `phone: null` (SPEC §6.1 known-good literals and ASM-003).
- [ ] An editable object with an unknown key is rejected structurally; a final request with a reversed date range, over-limit Unicode notes, an invalid phone character/digit count, phone contact without usable phone, or `privacyAcknowledged: false` returns only the approved safe field/form error codes and no canonical data (SPEC §6.1 rules, NFR-004/005). Use focused representative assertions rather than a combinatorial matrix.

**Seam: rendered `TripRequestForm` progression and correction**

- [ ] From direct English entry, Step 1 shows “Step 1 of 4” and Help me choose; Continue advances only after the active step is valid, and later-step invalid fields are not announced early (DEC-003, FR-004).
- [ ] On an invalid active step with multiple errors, Continue keeps the step, focuses a linked error summary, and associates inline errors; correcting an affected control updates that error, while Back returns to the previous step without validation or value loss (SPEC §§6.6–7.1, NFR-002).
- [ ] Completing all four steps in Greek reaches a localized, neutral “details ready” validation state backed by canonical `TripRequestValues`, with Greek progress, labels, options, helper/error/dialog copy and no mixed-language fallback, network request, confirmation navigation, or submitted/success claim (DEC-008, SUBDEC-004, issue slice boundary).

**Seam: rendered dependent child-age controls and destructive-reduction dialog**

- [ ] Changing Children from `0` to `2` renders exactly two required localized age controls; Continue cannot advance while either is empty (FR-005, SPEC §6.1).
- [ ] After entering ages `4` and `11`, increasing Children to `3` preserves both values and adds one empty required age control (FR-005).
- [ ] Reducing populated ages from three children to one opens localized confirmation; Cancel preserves count and every age, while Confirm commits count `1` and retains only the first age, with no silent truncation (SUBDEC-001).

**Seam: localized Plan My Trip route and metadata**

- [ ] `/en/plan-my-trip` renders the English title and direct `help-me-choose` default, a non-empty English title/description, self-canonical `/en/plan-my-trip`, `en`/`el`/`x-default` alternates, and `noindex,nofollow` (FR-015, SPEC §§5.3 and 6.2).
- [ ] `/el/plan-my-trip?destination=paros-antiparos` renders natural Greek interface copy with editable `paros-antiparos` selected while canonical IDs remain untranslated; an unknown destination query falls back safely to clean direct defaults and introduces no PII or extra query-derived text (FR-013, SUBDEC-004, NFR-004/005/007).
- [ ] At 390 × 844 and 1440 × 1024, representative EN/GR keyboard journeys have visible focus, usable semantic controls, linked errors, reduced-motion behavior, zero axe A/AA violations, no horizontal overflow/clipped Greek copy, and no unexpected console/page/request/HTTP failures; a focused 320 px check is representative robustness, not a duplicated full matrix (NFR-001/002/003, DEC-012, Tier 2).
- [ ] The existing Unlighthouse command scans representative `/en/plan-my-trip` and `/el/plan-my-trip` routes in addition to preserved earlier routes, applies the unchanged score budgets, and reports the inherited English Home LCP failure truthfully under its existing operator exception rather than calling that command a pass (SPEC §§12.2 and 13.4; project exception record).

## Method / risk

`tdd-solo` — routine but stateful form logic has clear public schema and rendered-UI seams; one fresh implementation agent must preserve the exact failing RED and passing GREEN evidence while avoiding persistence and submission work assigned to later slices.

## Escalation — what forces a ScopeExpansionRequest

- Delivering the accepted form requires persistence, server submission, confirmation, a new route identity, a server action, or another hard-walled capability.
- The correct implementation requires editing a source or test file outside soft scope for more than a small directly related neighbor.
- A test implies different fields, options, defaults, step order, canonical values, normalization, or success behavior than the issue/SPEC/SUBDEC-001.
- The static route cannot remain statically renderable with only the bounded client form island.
- A privacy, security, accessibility, bilingual-parity, or existing-budget requirement cannot be met inside this cage.

Small in-scope neighbor additions do NOT need a request.

## ScopeExpansionRequest (fill only if a hard wall is hit)

- **What was discovered:** <the file/interface/invariant the plan did not anticipate>
- **Why the current contract is insufficient:** <what cannot be done inside it>
- **Proposed change:** <files to add to soft scope, or wall to renegotiate>
- **Risk if ignored:** <low | medium | high>
