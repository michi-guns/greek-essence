import { expect, test } from '@playwright/test'

// GE-003.03 direction demos. Deleted with app/directions/ by GE-005.01.
const slugs = ['type-led', 'image-led', 'editorial-grid']

for (const slug of slugs) {
  for (const width of [320, 390]) {
    test(`${slug} at ${width}px: one h1, no sideways scroll, the action on one line`, async ({
      page,
    }) => {
      await page.setViewportSize({ width, height: 800 })
      await page.goto(`/directions/${slug}`)
      await expect(page.getByRole('heading', { level: 1 })).toHaveCount(1)
      const overflow = await page.evaluate(
        () => document.documentElement.scrollWidth - window.innerWidth,
      )
      expect(overflow).toBeLessThanOrEqual(0)
      const action = page.locator('.d-btn:visible').first()
      await expect(action).toBeVisible()
      const box = await action.boundingBox()
      expect(box!.height).toBeLessThan(60)
    })
  }
}

test('the directions are not indexed', async ({ page }) => {
  await page.goto('/directions')
  await expect(page.locator('meta[name="robots"]')).toHaveAttribute('content', /noindex/)
})
