# Runbook: Sanity Webhook Failure

## Trigger

Published Sanity changes do not appear in the Next.js application after the
expected cache-refresh period.

## Impact

Public content may remain stale. Transactional booking data is not affected.

## Procedure

1. Confirm the content is published in the expected Sanity dataset.
2. Check webhook delivery history and response status.
3. Verify the webhook secret and endpoint configuration.
4. Check application logs for signature, parsing, or revalidation errors.
5. Retry the webhook or trigger the documented cache invalidation path.
6. Confirm the affected page now shows the published content.

## Escalation

If failures repeat, investigate idempotency, monitoring, and whether an ADR or
implementation change is required.

## Note

Replace this placeholder with exact project commands and dashboards after the
integration exists.
