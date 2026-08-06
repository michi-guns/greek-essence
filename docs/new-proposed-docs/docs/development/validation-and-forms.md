# Validation and Forms

## Zod

Use Zod at runtime boundaries:

- Form data
- Route and search parameters
- Server Actions
- Route Handlers
- Environment variables
- Sanity query results
- External API responses
- Webhooks

Zod validates shape. Domain code validates business meaning.

## Forms

Use native React forms and Server Actions for straightforward forms.

Use React Hook Form when forms have meaningful client complexity:

- Dynamic arrays
- Conditional sections
- Multistep flows
- Nested data
- Autosave
- Immediate interactive validation

Use TanStack Query only when polling, optimistic updates, infinite queries, or
complex client-side cache synchronization justify it.
