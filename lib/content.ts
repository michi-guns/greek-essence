import greekContent from "@/content/el/showcase.json"
import englishContent from "@/content/en/showcase.json"
import {
  showcaseContentSchema,
  validateParosFinalCta,
  type ShowcaseContent,
} from "@/content/schemas/showcase"
import type { Locale } from "@/i18n/routing"

function shape(value: unknown): unknown {
  if (Array.isArray(value)) return value.map(shape)
  if (value && typeof value === "object") {
    return Object.fromEntries(
      Object.keys(value as Record<string, unknown>)
        .sort()
        .map((key) => [key, shape((value as Record<string, unknown>)[key])])
    )
  }
  return "scalar"
}

const stableValueKeys = new Set([
  "id",
  "routeId",
  "destinationContext",
  "src",
  "width",
  "height",
])

function stableValues(value: unknown): unknown {
  if (Array.isArray(value)) return value.map(stableValues)
  if (!value || typeof value !== "object") return undefined

  return Object.fromEntries(
    Object.entries(value as Record<string, unknown>).flatMap(([key, child]) => {
      if (stableValueKeys.has(key)) return [[key, child]]
      const nested = stableValues(child)
      return nested === undefined ? [] : [[key, nested]]
    })
  )
}

export function validateShowcaseContentPair(
  englishInput: unknown,
  greekInput: unknown
): { en: ShowcaseContent; el: ShowcaseContent } {
  if (
    JSON.stringify(shape(englishInput)) !== JSON.stringify(shape(greekInput))
  ) {
    throw new Error("Showcase locale structure differs")
  }
  const en = showcaseContentSchema.parse(englishInput)
  const el = showcaseContentSchema.parse(greekInput)
  validateParosFinalCta(en.paros.finalCta)
  validateParosFinalCta(el.paros.finalCta)
  if (JSON.stringify(stableValues(en)) !== JSON.stringify(stableValues(el))) {
    throw new Error("Showcase locale stable values differ")
  }
  return { en, el }
}

const validated = validateShowcaseContentPair(englishContent, greekContent)
const contentByLocale: Record<Locale, ShowcaseContent> = validated

export function getShowcaseContent(locale: Locale): ShowcaseContent {
  return contentByLocale[locale]
}
