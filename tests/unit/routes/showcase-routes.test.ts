import { describe, expect, it } from "vitest"

import { getCtaPathname, getLocalizedHref } from "@/lib/routes"

describe("showcase route identities", () => {
  it.each([
    ["home", "en", "/en"],
    ["home", "el", "/el"],
    ["paros", "en", "/en/destinations/paros-antiparos"],
    ["paros", "el", "/el/destinations/paros-antiparos"],
    ["plan-my-trip", "en", "/en/plan-my-trip"],
    ["plan-my-trip", "el", "/el/plan-my-trip"],
    ["confirmation", "en", "/en/plan-my-trip/confirmation"],
    ["confirmation", "el", "/el/plan-my-trip/confirmation"],
  ] as const)("maps %s independently for %s", (route, locale, href) => {
    expect(getLocalizedHref(route, locale)).toBe(href)
  })

  it("emits contextual CTA paths only for Plan My Trip", () => {
    expect(
      getCtaPathname({
        routeId: "plan-my-trip",
        destinationContext: "paros-antiparos",
      })
    ).toBe("/plan-my-trip?destination=paros-antiparos")
    expect(getCtaPathname({ routeId: "home", destinationContext: null })).toBe(
      "/"
    )
    expect(getCtaPathname({ routeId: "paros", destinationContext: null })).toBe(
      "/destinations/paros-antiparos"
    )
    expect(() =>
      getCtaPathname({
        routeId: "home",
        destinationContext: "paros-antiparos",
      })
    ).toThrow("Destination context requires Plan My Trip")
  })
})
