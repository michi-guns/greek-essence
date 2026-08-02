---
status: active
owner: engineering
---

# Next.js Boundaries

Next.js is the delivery and composition framework.

## Server Components

Use for server-side reads, public pages, dashboard pages, and view composition.

## Server Actions

Use for UI-triggered mutations.

Every Server Action must:

1. Authenticate.
2. Authorize.
3. Validate input.
4. Call an application use case.
5. Translate expected errors.
6. Revalidate, refresh, or redirect deliberately.

Treat Server Actions as untrusted public POST entry points.

## Route Handlers

Use for webhooks, public APIs, callbacks, integration endpoints, and file
responses.

## Client Components

Use only when browser state, browser APIs, event handlers, or rich interactive
behavior require them.

Business rules do not belong in components, actions, or route handlers.
