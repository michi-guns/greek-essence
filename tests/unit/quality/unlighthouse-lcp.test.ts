import { describe, expect, it } from "vitest"

import { assertHomeLcpCeiling } from "../../../scripts/assert-unlighthouse-lcp.mjs"

const reports = (en: number, el: number) => [
  { route: "/en", lcp: en },
  { route: "/el", lcp: el },
]

describe("strict Home LCP ceiling", () => {
  it("accepts values below 3000ms", () => {
    expect(() => assertHomeLcpCeiling(reports(2999.999, 2900))).not.toThrow()
  })

  it("accepts values exactly at 3000ms", () => {
    expect(() => assertHomeLcpCeiling(reports(3000, 3000))).not.toThrow()
  })

  it("rejects either locale above 3000ms", () => {
    expect(() => assertHomeLcpCeiling(reports(3000.001, 2900))).toThrow("/en")
    expect(() => assertHomeLcpCeiling(reports(2900, 3000.001))).toThrow("/el")
  })

  it("fails closed when either required locale report is absent", () => {
    expect(() => assertHomeLcpCeiling([{ route: "/en", lcp: 2000 }])).toThrow(
      "/el"
    )
  })
})
