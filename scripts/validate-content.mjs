import { existsSync, readFileSync } from "node:fs"
import { resolve } from "node:path"

import {
  showcaseContentSchema,
  validateParosFinalCta,
} from "../content/schemas/showcase.ts"

const root = process.cwd()
const contentRootFlagIndex = process.argv.indexOf("--content-root")
const contentRoot =
  contentRootFlagIndex === -1
    ? resolve(root, "content")
    : resolve(root, process.argv[contentRootFlagIndex + 1] ?? "")
const locales = ["en", "el"]
const contents = Object.fromEntries(
  locales.map((locale) => [
    locale,
    showcaseContentSchema.parse(
      JSON.parse(
        readFileSync(resolve(contentRoot, locale, "showcase.json"), "utf8")
      )
    ),
  ])
)
function shape(value) {
  if (Array.isArray(value)) return value.map(shape)
  if (value && typeof value === "object")
    return Object.fromEntries(
      Object.keys(value)
        .sort()
        .map((key) => [key, shape(value[key])])
    )
  return typeof value
}
if (JSON.stringify(shape(contents.en)) !== JSON.stringify(shape(contents.el)))
  throw new Error("Showcase locale structure differs")

validateParosFinalCta(contents.en.paros.finalCta)
validateParosFinalCta(contents.el.paros.finalCta)

function stableValues(value) {
  if (Array.isArray(value)) return value.map(stableValues)
  if (!value || typeof value !== "object") return undefined

  return Object.fromEntries(
    Object.entries(value).flatMap(([key, child]) => {
      if (
        [
          "id",
          "routeId",
          "destinationContext",
          "src",
          "width",
          "height",
        ].includes(key)
      )
        return [[key, child]]
      const nested = stableValues(child)
      return nested === undefined ? [] : [[key, nested]]
    })
  )
}
if (
  JSON.stringify(stableValues(contents.en)) !==
  JSON.stringify(stableValues(contents.el))
)
  throw new Error("Showcase locale stable values differ")

for (const [locale, content] of Object.entries(contents)) {
  if (locale === "el" && !/[Α-Ωα-ω]/.test(JSON.stringify(content)))
    throw new Error("Greek showcase content lacks Greek prose")
  const media = [
    content.home.hero.media,
    content.home.promise.media,
    content.home.parosFeature.media,
    content.home.trustStory.media,
    content.paros.hero.media,
    content.paros.introduction.media,
    ...content.paros.signatureExperiences.items.map((item) => item.media),
  ].filter(Boolean)
  for (const item of media) {
    const publicPath = resolve(root, "public", item.src.slice(1))
    if (!existsSync(publicPath))
      throw new Error(`Showcase media file is missing: ${item.src}`)
  }
}
console.log("Showcase content validation passed for en/el with public media")
