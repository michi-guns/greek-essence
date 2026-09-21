import { expect, test } from '@playwright/test'

test('home page renders with a single h1 and a skip link', async ({ page }) => {
  await page.goto('/')
  await expect(page.getByRole('heading', { level: 1 })).toHaveCount(1)
  await expect(page.getByRole('link', { name: 'Skip to content' })).toBeAttached()
  await expect(page.locator('main#main')).toBeVisible()
})
