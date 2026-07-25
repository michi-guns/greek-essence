import { expect, test, type Page } from "@playwright/test"

import {
  assertNoBrowserFailures,
  installBrowserGuards,
  type BrowserGuards,
} from "./browser-guards"

const localizedRoutes = [
  {
    route: "/en",
    locale: "en",
    canonical: "/en",
    alternates: { en: "/en", el: "/el", "x-default": "/en" },
  },
  {
    route: "/el",
    locale: "el",
    canonical: "/el",
    alternates: { en: "/en", el: "/el", "x-default": "/en" },
  },
  {
    route: "/en/destinations/paros-antiparos",
    locale: "en",
    canonical: "/en/destinations/paros-antiparos",
    alternates: {
      en: "/en/destinations/paros-antiparos",
      el: "/el/destinations/paros-antiparos",
      "x-default": "/en/destinations/paros-antiparos",
    },
  },
  {
    route: "/el/destinations/paros-antiparos",
    locale: "el",
    canonical: "/el/destinations/paros-antiparos",
    alternates: {
      en: "/en/destinations/paros-antiparos",
      el: "/el/destinations/paros-antiparos",
      "x-default": "/en/destinations/paros-antiparos",
    },
  },
  {
    route: "/en/quality-lab",
    locale: "en",
    canonical: "/en/quality-lab",
    alternates: {
      en: "/en/quality-lab",
      el: "/el/quality-lab",
      "x-default": "/en/quality-lab",
    },
  },
  {
    route: "/el/quality-lab",
    locale: "el",
    canonical: "/el/quality-lab",
    alternates: {
      en: "/en/quality-lab",
      el: "/el/quality-lab",
      "x-default": "/en/quality-lab",
    },
  },
] as const

const toggleJourneys = [
  {
    route: "/en/quality-lab",
    initial: "Not selected",
    selected: "Selected",
    status: "Current state",
    activation: "click",
  },
  {
    route: "/el/quality-lab",
    initial: "Δεν έχει επιλεγεί",
    selected: "Επιλεγμένο",
    status: "Τρέχουσα κατάσταση",
    activation: "keyboard",
  },
] as const

async function expectPathname(
  locator: ReturnType<Page["locator"]>,
  path: string
) {
  const href = await locator.getAttribute("href")
  expect(href).not.toBeNull()
  expect(new URL(href!, "http://127.0.0.1:3100").pathname).toBe(path)
}

async function tabTo(page: Page, locator: ReturnType<Page["getByRole"]>) {
  for (let attempt = 0; attempt < 12; attempt += 1) {
    await page.keyboard.press("Tab")
    if (
      await locator.evaluate((element) => element === document.activeElement)
    ) {
      return
    }
  }

  throw new Error("Keyboard focus did not reach the expected control")
}

async function expectNoHorizontalOverflow(page: Page, width: number) {
  expect(
    await page.evaluate(() => ({
      body: {
        clientWidth: document.body.clientWidth,
        scrollWidth: document.body.scrollWidth,
      },
      document: {
        clientWidth: document.documentElement.clientWidth,
        scrollWidth: document.documentElement.scrollWidth,
      },
      overwideElements: [...document.querySelectorAll<HTMLElement>("body *")]
        .filter(
          (element) =>
            element.scrollWidth > element.clientWidth + 1 ||
            element.getBoundingClientRect().right >
              document.documentElement.clientWidth + 1
        )
        .map(
          (element) =>
            `${element.tagName}.${element.className}:scroll=${element.scrollWidth},client=${element.clientWidth},right=${Math.round(element.getBoundingClientRect().right)}`
        ),
    }))
  ).toEqual({
    body: { clientWidth: width, scrollWidth: width },
    document: { clientWidth: width, scrollWidth: width },
    overwideElements: [],
  })
}

async function expectLocalizedMetadata(
  page: Page,
  route: (typeof localizedRoutes)[number]
) {
  await expect(page.locator("html")).toHaveAttribute("lang", route.locale)
  await expect(page).toHaveTitle(/.+/)
  await expect(page.locator('meta[name="description"]')).toHaveAttribute(
    "content",
    /.+/
  )
  await expectPathname(page.locator('link[rel="canonical"]'), route.canonical)

  const alternateLinks = await page
    .locator('link[rel="alternate"][hreflang]')
    .evaluateAll((links) =>
      links.map((link) => ({
        hreflang: link.getAttribute("hreflang"),
        pathname: new URL(link.getAttribute("href")!, "http://127.0.0.1:3100")
          .pathname,
      }))
    )

  expect(alternateLinks).toEqual(
    Object.entries(route.alternates).map(([hreflang, pathname]) => ({
      hreflang,
      pathname,
    }))
  )
  await expect(page.locator('meta[name="robots"]')).toHaveAttribute(
    "content",
    "noindex, nofollow"
  )
}

test.describe("localized prototype shell", () => {
  let browserGuards: BrowserGuards

  test.beforeEach(({ page }) => {
    browserGuards = installBrowserGuards(page)
  })

  test.afterEach(() => {
    assertNoBrowserFailures(browserGuards)
  })

  test("renders exact localized metadata semantics", async ({ page }) => {
    for (const route of localizedRoutes) {
      await page.goto(route.route)
      await expectLocalizedMetadata(page, route)
    }
  })

  test("renders the complete bilingual Home and switches equivalent locale", async ({
    page,
  }) => {
    await page.goto("/en")
    await expect(
      page.getByRole("heading", {
        level: 1,
        name: "Greece, experienced with intention",
      })
    ).toBeVisible()
    await expect(page.locator("main > section")).toHaveCount(6)
    const menuButton = page.getByRole("button", { name: "Menu", exact: true })
    if (await menuButton.isVisible()) await menuButton.click()
    await page.getByRole("link", { name: "Ελληνικά", exact: true }).click()
    await expect(page).toHaveURL(/\/el$/)
    await expect(
      page.getByRole("heading", {
        level: 1,
        name: "Η Ελλάδα, όπως αξίζει να τη ζήσετε",
      })
    ).toBeVisible()
    await expect(page.locator("main > section")).toHaveCount(6)
  })

  test("renders the bilingual Paros editorial journey with route-preserving locale switching", async ({
    page,
  }) => {
    await page.goto("/en/destinations/paros-antiparos")
    await expect(
      page.getByRole("heading", {
        level: 1,
        name: "Paros & Antiparos, in your own rhythm",
      })
    ).toBeVisible()
    await expect(page.locator("main > section")).toHaveCount(6)
    const menuButton = page.getByRole("button", { name: "Menu", exact: true })
    if (await menuButton.isVisible()) await menuButton.click()
    await expect(
      page.getByRole("link", { name: "Paros & Antiparos", exact: true })
    ).toHaveAttribute("aria-current", "page")
    await expectPathname(
      page.getByRole("link", { name: "Plan Paros & Antiparos", exact: true }),
      "/en/plan-my-trip"
    )
    await expect(
      page.getByRole("link", { name: "Plan Paros & Antiparos", exact: true })
    ).toHaveAttribute("href", "/en/plan-my-trip?destination=paros-antiparos")

    await page.getByRole("link", { name: "Ελληνικά", exact: true }).click()
    await expect(page).toHaveURL(/\/el\/destinations\/paros-antiparos$/)
    await expect(
      page.getByRole("heading", {
        level: 1,
        name: "Πάρος & Αντίπαρος, στον δικό σας ρυθμό",
      })
    ).toBeVisible()
    await expect(page.locator("main > section")).toHaveCount(6)
  })

  test("protects both localized Home-to-Paros journeys and destination responsive boundaries", async ({
    page,
    request,
  }) => {
    for (const journey of [
      {
        home: "/en",
        destination: "/en/destinations/paros-antiparos",
        otherDestination: "/el/destinations/paros-antiparos",
        cta: "Plan Paros & Antiparos",
        switcher: "Ελληνικά",
        current: "Paros & Antiparos",
      },
      {
        home: "/el",
        destination: "/el/destinations/paros-antiparos",
        otherDestination: "/en/destinations/paros-antiparos",
        cta: "Σχεδιάστε Πάρο & Αντίπαρο",
        switcher: "English",
        current: "Πάρος & Αντίπαρος",
      },
    ]) {
      await page.emulateMedia({ reducedMotion: "reduce" })
      await page.goto(journey.home)
      const menuButton = page.getByRole("button", {
        name: journey.home === "/en" ? "Menu" : "Μενού",
        exact: true,
      })
      if (await menuButton.isVisible()) await menuButton.click()
      await page.locator(`a[href="${journey.destination}"]`).first().click()
      await expect(page).toHaveURL(journey.destination)
      if (await menuButton.isVisible()) await menuButton.click()
      await expect(
        page.getByRole("link", { name: journey.current, exact: true })
      ).toHaveAttribute("aria-current", "page")
      await expect(
        page.getByRole("link", { name: journey.cta, exact: true })
      ).toHaveAttribute(
        "href",
        `${journey.home.replace(/\/(en|el)$/, "/$1/plan-my-trip")}?destination=paros-antiparos`
      )
      await page
        .getByRole("link", { name: journey.switcher, exact: true })
        .click()
      await expect(page).toHaveURL(journey.otherDestination)

      const response = await request.get(journey.destination)
      expect(response.headers()["content-security-policy"]).toBeTruthy()
      expect(response.headers()["x-content-type-options"]).toBe("nosniff")
      expect(response.headers()["x-frame-options"]).toBe("DENY")

      await page.setViewportSize({ width: 320, height: 844 })
      await expect(page.locator(".button").first()).toBeVisible()
      expect(
        await page.evaluate(
          () =>
            document.documentElement.scrollWidth <=
            document.documentElement.clientWidth + 1
        )
      ).toBe(true)
      expect(
        await page
          .locator(".button")
          .first()
          .evaluate((element) => getComputedStyle(element).transitionDuration)
      ).toBe("0s")
      await page.setViewportSize({ width: 1440, height: 1024 })
      await page.keyboard.press("Tab")
      await expect(page.locator(":focus")).toBeVisible()
    }
  })

  test("protects destination headers and 200% zoom overflow for both locales", async ({
    page,
    request,
  }) => {
    for (const route of [
      "/en/destinations/paros-antiparos",
      "/el/destinations/paros-antiparos",
    ]) {
      const response = await request.get(route)
      expect(response.headers()["content-security-policy"]).toBeTruthy()
      expect(response.headers()["x-content-type-options"]).toBe("nosniff")
      expect(response.headers()["referrer-policy"]).toBe(
        "strict-origin-when-cross-origin"
      )
      expect(response.headers()["permissions-policy"]).toBe(
        "camera=(), microphone=(), geolocation=()"
      )
      expect(response.headers()["x-frame-options"]).toBe("DENY")

      await page.goto(route)
      await page.setViewportSize({ width: 195, height: 844 })
      await expectNoHorizontalOverflow(page, 195)
    }
  })

  test("closes compact destination menus with trigger focus return", async ({
    page,
  }) => {
    test.skip((await page.viewportSize())!.width >= 768, "compact interaction")
    for (const journey of [
      { route: "/en/destinations/paros-antiparos", menu: "Menu" },
      { route: "/el/destinations/paros-antiparos", menu: "Μενού" },
    ]) {
      await page.goto(journey.route)
      const trigger = page.getByRole("button", {
        name: journey.menu,
        exact: true,
      })
      await trigger.click()
      await page.keyboard.press("Escape")
      await expect(trigger).toHaveAttribute("aria-expanded", "false")
      await expect(trigger).toBeFocused()
      await trigger.click()
      await page.locator("main").click({ position: { x: 10, y: 10 } })
      await expect(trigger).toHaveAttribute("aria-expanded", "false")
      await expect(trigger).toBeFocused()
    }
  })

  test("redirects the root route and rejects an invalid locale", async ({
    page,
  }) => {
    await page.goto("/")
    await expect(page).toHaveURL(/\/(en|el)$/)

    const invalidLocaleResponse = await page.goto("/invalid")
    expect(invalidLocaleResponse?.status()).toBe(404)
  })

  test("exercises localized quality-lab toggle interaction", async ({
    page,
  }) => {
    for (const journey of toggleJourneys) {
      await page.goto(journey.route)
      const toggle = page.getByRole("button", {
        name: journey.initial,
        exact: true,
      })

      await expect(toggle).toHaveAttribute("aria-pressed", "false")

      if (journey.activation === "keyboard") {
        await tabTo(page, toggle)
        await page.keyboard.press("Space")
      } else {
        await toggle.click()
      }

      await expect(
        page.getByRole("button", { name: journey.selected, exact: true })
      ).toHaveAttribute("aria-pressed", "true")
      await expect(page.locator('[aria-live="polite"]')).toHaveText(
        `${journey.status}: ${journey.selected}`
      )
    }
  })

  test("provides security headers on both Home locales", async ({
    request,
  }) => {
    for (const route of ["/en", "/el"]) {
      const response = await request.get(route)
      expect(response.headers()["content-security-policy"]).toBeTruthy()
      expect(response.headers()["x-content-type-options"]).toBe("nosniff")
      expect(response.headers()["referrer-policy"]).toBe(
        "strict-origin-when-cross-origin"
      )
      expect(response.headers()["permissions-policy"]).toBe(
        "camera=(), microphone=(), geolocation=()"
      )
      expect(response.headers()["x-frame-options"]).toBe("DENY")
    }
  })

  test("closes the compact menu by Escape, outside activation, and navigation with focus return", async ({
    page,
  }) => {
    test.skip((await page.viewportSize())!.width >= 768, "compact interaction")
    await page.goto("/en")
    const trigger = page.getByRole("button", { name: "Menu", exact: true })
    await trigger.click()
    await page.keyboard.press("Escape")
    await expect(trigger).toHaveAttribute("aria-expanded", "false")
    await expect(trigger).toBeFocused()
    await trigger.click()
    await page.locator("main").click({ position: { x: 10, y: 10 } })
    await expect(trigger).toHaveAttribute("aria-expanded", "false")
    await trigger.click()
    await page.getByRole("link", { name: "Ελληνικά", exact: true }).click()
    await expect(page).toHaveURL(/\/el$/)
  })

  test("preserves focus, current state, reduced motion, responsive layout, and 200% zoom", async ({
    page,
  }) => {
    await page.emulateMedia({ reducedMotion: "reduce" })
    await page.goto("/el")
    const compactMenu = page.getByRole("button", { name: "Μενού", exact: true })
    if (await compactMenu.isVisible()) await compactMenu.click()
    await expect(
      page.getByRole("link", { name: "Αρχική", exact: true })
    ).toHaveAttribute("aria-current", "page")
    if (await compactMenu.isVisible()) await page.keyboard.press("Escape")
    await page.keyboard.press("Tab")
    await expect(page.locator(":focus")).toBeVisible()
    await page.setViewportSize({ width: 195, height: 844 })
    await expectNoHorizontalOverflow(page, 195)
    expect(
      await page
        .locator(".button")
        .first()
        .evaluate((element) => getComputedStyle(element).transitionDuration)
    ).toBe("0s")
    await page.goto("/en")
    await expectNoHorizontalOverflow(page, 195)
  })

  test("provides keyboard focus for interactive navigation", async ({
    page,
  }) => {
    await page.goto("/en")
    await page.keyboard.press("Tab")
    await expect(page.locator(":focus")).toBeVisible()
  })
})
