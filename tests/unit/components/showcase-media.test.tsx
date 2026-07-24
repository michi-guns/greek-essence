import { render, screen } from "@testing-library/react"
import { describe, expect, it, vi } from "vitest"

vi.mock("@/i18n/navigation", () => ({ Link: "a" }))

import { ShowcaseMedia } from "@/components/sections/showcase-media"
import type { MediaResolution } from "@/lib/content"

const approvedMedia: MediaResolution = {
  kind: "approved",
  media: {
    id: "hero",
    src: "/assets/imgs/hero.jpg",
    width: 1200,
    height: 800,
    alt: "Aegean arrival",
    focalPoint: { xPercent: 25, yPercent: 60 },
  },
}

describe("ShowcaseMedia", () => {
  it.each(["hero", "card"] as const)(
    "renders approved %s media with its stable layout class",
    (variant) => {
      render(<ShowcaseMedia resolution={approvedMedia} variant={variant} />)

      const image = screen.getByRole("img", { name: "Aegean arrival" })
      expect(image.classList.contains("showcase-media")).toBe(true)
      expect(image.classList.contains(`showcase-media--${variant}`)).toBe(true)
    }
  )
})
