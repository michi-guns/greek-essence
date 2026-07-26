Status: ready-for-agent
Method: tdd-pingpong
Complexity: 5
BlockedBy: 3
Milestone: complete-resilient-trip-request

# Preserve trip-request progress across refresh, locale switching, and reset

Make the completed four-step request resilient through one silent, locale-neutral, privacy-conscious browser draft. A visitor keeps canonical progress across refresh and equivalent-language navigation, can safely cancel or confirm Start Over, and never sees false persistence or submission claims.

## Acceptance criteria

- [ ] Initialization follows valid draft, then allow-listed route context, then clean direct defaults; one versioned canonical record restores the exact current step, incomplete editable values, entry context, and retry identity fields without translating stored values (FR-003, FR-006, DEC-004, SUBDEC-002, SUBDEC-004).
- [ ] Meaningful changes save after exactly 1000 ms, while blur, step navigation, locale switching, and pagehide synchronously flush pending state; timestamps extend expiry to exactly 72 hours only for meaningful changes (FR-006, DEC-004, SUBDEC-002).
- [ ] Valid incomplete progress restores silently, while corrupt, incompatible, unreadable, future-invalid, expired, or internally inconsistent records are removed through guarded best-effort cleanup and the form continues from safe defaults without storage UI or exceptions (FR-006, NFR-004, NFR-006, SUBDEC-002).
- [ ] Switching between English and Greek preserves the equivalent Plan My Trip route, current step, canonical values, entry provenance, and only the allow-listed destination query/static hash; it flushes first and renders every restored label, option, message, and state in the active locale (FR-003, DEC-008, SUBDEC-004, NFR-007).
- [ ] Start Over cancel leaves values, step, context, and draft intact; confirm clears the draft, returns to Step 1, and restores only route-implied Paros context for destination entry or Help me choose for direct entry (FR-007, DEC-005, SUBDEC-002).
- [ ] A failed storage operation never blocks editing, navigation, or reset; no provider response, rendered email, environment value, analytics data, or extra personal-data copy enters storage, URLs, logs, console output, screenshots, or browser artifacts (NFR-004, NFR-005, NFR-006).
- [ ] The persistence integration remains inside the bounded form client island, keeps static public routes and shallow strict-TypeScript modules, and adds no global store, migration framework, account-style save UI, background retry, or speculative recovery infrastructure (DEC-010, NFR-003, NFR-008).
- [ ] Focused RED-to-GREEN draft/state tests prove debounce and flush timing, exact expiry boundaries, guarded storage failures, structural incomplete restore, submission-identity invalidation rules, and confirmed reset; guarded compact/wide English/Greek browser flows prove refresh and language continuity, silent invalid-draft cleanup, Start Over cancel/confirm, accessibility, and no horizontal overflow (NFR-001, NFR-002, NFR-003, DEC-012).

Traces: FR-003, FR-006, FR-007; NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-006, NFR-007, NFR-008; DEC-004, DEC-005, DEC-008, DEC-010, DEC-012, SUBDEC-002, SUBDEC-004.
