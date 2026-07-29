import { render, screen } from "@testing-library/react"
import { describe, expect, it, vi } from "vitest"

vi.mock("@/i18n/navigation", () => ({ Link: "a" }))

import { ShowcaseMedia } from "@/components/sections/showcase-media"

const media = {
  src: "/images/hero.jpg",
  width: 1200,
  height: 800,
  alt: "Aegean arrival",
}

describe("ShowcaseMedia", () => {
  it.each(["hero", "card"] as const)(
    "renders %s media with its stable layout class",
    (variant) => {
      render(<ShowcaseMedia media={media} variant={variant} />)

      const image = screen.getByRole("img", { name: "Aegean arrival" })
      expect(image.classList.contains("showcase-media")).toBe(true)
      expect(image.classList.contains(`showcase-media--${variant}`)).toBe(true)
    }
  )

  it("loads the hero eagerly with high fetch priority", () => {
    render(<ShowcaseMedia priority media={media} variant="hero" />)

    const image = screen.getByRole("img", { name: "Aegean arrival" })
    expect(image.getAttribute("decoding")).toBe("sync")
    expect(image.getAttribute("fetchpriority")).toBe("high")
    expect(image.getAttribute("loading")).toBe("eager")
  })
})
