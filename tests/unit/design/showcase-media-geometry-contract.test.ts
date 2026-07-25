import { readFileSync } from "node:fs"
import { resolve } from "node:path"

import { describe, expect, it } from "vitest"

const stylesheet = readFileSync(
  resolve(process.cwd(), "app/globals.css"),
  "utf8"
)

function declarations(selector: string) {
  const match = stylesheet.match(new RegExp(`${selector}\\s*\\{([^}]*)\\}`))
  expect(match, `Missing ${selector} CSS rule`).not.toBeNull()
  return match![1]
}

describe("approved showcase media geometry contract", () => {
  it("keeps approved hero media filling and cropping its hero slot", () => {
    const hero = declarations("\\.hero \\.showcase-media--hero")
    expect(hero).toContain("position: absolute")
    expect(hero).toContain("inset: 0")
    expect(hero).toContain("width: 100%")
    expect(hero).toContain("height: 100%")
    expect(hero).toContain("object-fit: cover")
  })

  it("keeps approved card media width, aspect, and crop declarations", () => {
    const card = declarations("\\.media-card \\.showcase-media--card")
    expect(card).toContain("display: block")
    expect(card).toContain("width: calc(100% + 0.5rem)")
    expect(card).toContain("aspect-ratio: 4 / 3")
    expect(card).toContain("height: auto")
    expect(card).toContain("object-fit: cover")
  })
})
