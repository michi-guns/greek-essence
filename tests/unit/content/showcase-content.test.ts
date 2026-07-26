import { spawnSync } from "node:child_process"
import { createHash } from "node:crypto"
import {
  cpSync,
  mkdtempSync,
  readFileSync,
  rmSync,
  statSync,
  writeFileSync,
} from "node:fs"
import { tmpdir } from "node:os"
import { resolve } from "node:path"

import { describe, expect, it } from "vitest"

import greekFixture from "@/content/el/showcase.json"
import englishFixture from "@/content/en/showcase.json"
import mediaManifest from "@/content/shared/media.json"
import {
  getShowcaseContent,
  resolveMedia,
  resolveMediaFromManifest,
  validateShowcaseContentPair,
  type MediaManifest,
} from "@/lib/content"

const clone = <T>(value: T): T => structuredClone(value)
const showcaseContentPaths = [
  "content/en/showcase.json",
  "content/el/showcase.json",
] as const

function sourceFixtureSnapshot() {
  return showcaseContentPaths.map((path) => {
    const absolutePath = resolve(process.cwd(), path)
    const bytes = readFileSync(absolutePath)
    return {
      path,
      hash: createHash("sha256").update(bytes).digest("hex"),
      mtimeMs: statSync(absolutePath).mtimeMs,
    }
  })
}

function runContentValidationInTemporaryFixtureRoot(
  mutate: (fixture: typeof englishFixture) => void
) {
  const fixtureRoot = mkdtempSync(resolve(tmpdir(), "greek-essence-content-"))
  const contentRoot = resolve(fixtureRoot, "content")

  try {
    cpSync(resolve(process.cwd(), "content"), contentRoot, { recursive: true })
    for (const locale of ["en", "el"] as const) {
      const fixturePath = resolve(contentRoot, locale, "showcase.json")
      const fixture = JSON.parse(readFileSync(fixturePath, "utf8"))
      mutate(fixture)
      writeFileSync(fixturePath, `${JSON.stringify(fixture, null, 2)}\n`)
    }

    return spawnSync(
      process.execPath,
      ["scripts/validate-content.mjs", "--content-root", contentRoot],
      { cwd: process.cwd(), encoding: "utf8" }
    )
  } finally {
    rmSync(fixtureRoot, { force: true, recursive: true })
  }
}

const approvedManifest = (): MediaManifest => ({
  assetRoot: "assets/imgs",
  setStatus: "approved",
  defaults: {
    source: "operator-generated",
    sourceApprovalStatus: "approved",
    rightsStatus: "approved",
    approvalStatus: "approved",
    provisional: false,
    focalPoint: { xPercent: 25, yPercent: 60 },
    alt: { en: "Aegean arrival", el: "Άφιξη στο Αιγαίο" },
  },
  assets: [
    {
      id: "hero",
      files: [{ path: "hero.jpg", width: 1200, height: 800, role: "master" }],
    },
  ],
})

describe("showcase content boundary", () => {
  it("loads structurally equivalent English and Greek Home content", () => {
    const english = getShowcaseContent("en")
    const greek = getShowcaseContent("el")
    expect(Object.keys(greek.home)).toEqual(Object.keys(english.home))
    expect(english.home.howItWorks.steps).toHaveLength(3)
    expect(greek.home.howItWorks.steps).toHaveLength(3)
    expect(greek.home.hero.title).toMatch(/[Α-Ωα-ω]/)
  })

  it("loads a complete six-part Paros editorial structure in both locales", () => {
    const english = getShowcaseContent("en")
    const greek = getShowcaseContent("el")

    expect(english).toHaveProperty("paros")
    expect(greek).toHaveProperty("paros")
  })

  it("rejects an empty editorial field", () => {
    const invalid = clone(englishFixture)
    invalid.home.hero.title = "   "
    expect(() =>
      validateShowcaseContentPair(invalid, greekFixture, [])
    ).toThrow()
  })

  it("rejects an unknown route ID", () => {
    const invalid: unknown = {
      ...clone(englishFixture),
      home: {
        ...clone(englishFixture.home),
        hero: {
          ...clone(englishFixture.home.hero),
          primaryCta: {
            ...clone(englishFixture.home.hero.primaryCta),
            routeId: "unknown",
          },
        },
      },
    }
    expect(() =>
      validateShowcaseContentPair(invalid, greekFixture, [])
    ).toThrow()
  })

  it("rejects an unknown media ID", () => {
    const invalid = clone(englishFixture)
    invalid.home.hero.mediaId = "unknown-media"
    expect(() =>
      validateShowcaseContentPair(invalid, greekFixture, [])
    ).toThrow("Unknown showcase media id")
  })

  it("rejects English/Greek structural drift", () => {
    const promiseWithoutBody: Record<string, unknown> = clone(
      greekFixture.home.promise
    )
    Reflect.deleteProperty(promiseWithoutBody, "body")
    const invalidGreek: unknown = {
      ...clone(greekFixture),
      home: { ...clone(greekFixture.home), promise: promiseWithoutBody },
    }
    expect(() =>
      validateShowcaseContentPair(englishFixture, invalidGreek, [])
    ).toThrow("Showcase locale structure differs")
  })

  it.each([
    ["destination collection ID", "travelerFit", "traveler-fit-drift"],
    [
      "referenced media ID",
      "signatureExperiences",
      "destination-athens-primary-01",
    ],
    ["final CTA route", "finalCta", "home"],
    ["final CTA context", "finalCta", null],
  ])(
    "rejects bilingual Paros stable %s drift",
    (_label, target, replacement) => {
      const invalidGreek = clone(greekFixture)
      if (target === "travelerFit") {
        invalidGreek.paros.travelerFit.items[0]!.id = replacement as string
      } else if (target === "signatureExperiences") {
        invalidGreek.paros.signatureExperiences.items[0]!.mediaId =
          replacement as string
      } else if (target === "finalCta") {
        if (replacement === null) {
          invalidGreek.paros.finalCta.destinationContext = null
        } else {
          invalidGreek.paros.finalCta.routeId = replacement as "home"
        }
      }

      const validate = () =>
        validateShowcaseContentPair(
          englishFixture,
          invalidGreek,
          mediaManifest.assets.map((asset) => asset.id)
        )
      if (target === "finalCta") {
        expect(validate).toThrow()
      } else {
        expect(validate).toThrow("Showcase locale stable values differ")
      }
    }
  )

  it.each([
    ["home route with destination context", "home", "paros-antiparos", false],
    [
      "Plan My Trip route without destination context",
      "plan-my-trip",
      null,
      false,
    ],
    ["context-free Home CTA", "plan-my-trip", null, true],
  ] as const)(
    "validates isolated fixtures without changing authoritative source fixtures: %s",
    (_label, routeId, destinationContext, shouldPass) => {
      const before = sourceFixtureSnapshot()
      const result = runContentValidationInTemporaryFixtureRoot((fixture) => {
        if (shouldPass) {
          fixture.home.finalCta = {
            ...fixture.home.finalCta,
            routeId: "plan-my-trip",
            destinationContext: null,
          }
          return
        }
        fixture.paros.finalCta = {
          ...fixture.paros.finalCta,
          routeId,
          destinationContext,
        }
      })

      expect(result.status === 0).toBe(shouldPass)
      expect(sourceFixtureSnapshot()).toEqual(before)
    }
  )

  it.each([
    ["home route with destination context", "home", "paros-antiparos"],
    ["Plan My Trip route without destination context", "plan-my-trip", null],
  ] as const)(
    "rejects an equally invalid bilingual destination CTA pairing: %s",
    (_label, routeId, destinationContext) => {
      const invalidEnglish = clone(englishFixture)
      const invalidGreek = clone(greekFixture)
      for (const fixture of [invalidEnglish, invalidGreek]) {
        fixture.paros.finalCta = {
          ...fixture.paros.finalCta,
          routeId,
          destinationContext,
        }
      }

      expect(() =>
        validateShowcaseContentPair(
          invalidEnglish,
          invalidGreek,
          mediaManifest.assets.map((asset) => asset.id)
        )
      ).toThrow()
    }
  )

  it("keeps both live Home media records behind the pending approval fallback", () => {
    expect(resolveMedia("home-aegean-human-arrival-01", "en")).toEqual({
      kind: "fallback",
      id: "home-aegean-human-arrival-01",
      reason: "pending-approval",
    })
    expect(
      resolveMedia("destination-paros-antiparos-primary-01", "el")
    ).toEqual({
      kind: "fallback",
      id: "destination-paros-antiparos-primary-01",
      reason: "pending-approval",
    })
  })

  it("fails closed when an approved media file is absent from the build", () => {
    expect(() =>
      resolveMediaFromManifest(approvedManifest(), "hero", "en")
    ).toThrow("Approved media is incomplete")
  })

  it("resolves a controlled fully approved record with localized geometry", () => {
    expect(
      resolveMediaFromManifest(approvedManifest(), "hero", "el", () => true)
    ).toEqual({
      kind: "approved",
      media: {
        id: "hero",
        src: "/assets/imgs/hero.jpg",
        width: 1200,
        height: 800,
        alt: "Άφιξη στο Αιγαίο",
        focalPoint: { xPercent: 25, yPercent: 60 },
      },
    })
  })

  it.each([
    [
      "pending source approval",
      (manifest: MediaManifest) => {
        manifest.defaults.sourceApprovalStatus = "pending"
      },
    ],
    [
      "arbitrary source",
      (manifest: MediaManifest) => {
        manifest.defaults.source = "arbitrary"
      },
    ],
    [
      "provisional manifest",
      (manifest: MediaManifest) => {
        manifest.defaults.provisional = true
      },
    ],
    [
      "incomplete crop role",
      (manifest: MediaManifest) => {
        manifest.assets[0]!.files[0]!.role = ""
      },
    ],
  ])("fails closed for approved media with %s", (_name, mutate) => {
    const manifest = approvedManifest()
    mutate(manifest)
    expect(() =>
      resolveMediaFromManifest(manifest, "hero", "en", () => true)
    ).toThrow("Approved media is incomplete")
  })
})
