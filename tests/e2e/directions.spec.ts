import { expect, test } from '@playwright/test'

// GE-003.03 direction demos. Deleted with app/directions/ by GE-005.01.
const slugs = ['type-led', 'image-led', 'editorial-grid']

for (const slug of slugs) {
  for (const width of [320, 390]) {
    test(`${slug} at ${width}px: one h1, no sideways scroll, every visible action fits its button`, async ({
      page,
    }) => {
      await page.setViewportSize({ width, height: 800 })
      await page.goto(`/directions/${slug}`)
      await expect(page.getByRole('heading', { level: 1 })).toHaveCount(1)
      const overflow = await page.evaluate(
        () => document.documentElement.scrollWidth - window.innerWidth,
      )
      expect(overflow).toBeLessThanOrEqual(0)
      // Fixed elements do not count towards page overflow, so check each button's own box:
      // text spilling out of a button (it cannot wrap: white-space nowrap) shows as scrollWidth.
      const actions = page.locator('.d-btn:visible')
      expect(await actions.count()).toBeGreaterThan(0)
      for (const action of await actions.all()) {
        const spill = await action.evaluate((el) => el.scrollWidth - el.clientWidth)
        expect(spill).toBeLessThanOrEqual(0)
        const box = await action.boundingBox()
        expect(box!.x).toBeGreaterThanOrEqual(0)
        expect(box!.x + box!.width).toBeLessThanOrEqual(width)
      }
    })
  }
}

test('the directions are not indexed', async ({ page }) => {
  await page.goto('/directions')
  await expect(page.locator('meta[name="robots"]')).toHaveAttribute('content', /noindex/)
})
