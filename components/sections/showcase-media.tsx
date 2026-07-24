import Image from "next/image"

import type { ShowcaseContent } from "@/content/schemas/showcase"
import { Link } from "@/i18n/navigation"
import type { Locale } from "@/i18n/routing"
import type { MediaResolution } from "@/lib/content"
import { getCtaPathname } from "@/lib/routes"

export function ShowcaseMedia({
  resolution,
  variant,
  priority = false,
}: {
  resolution: MediaResolution
  variant: "hero" | "card"
  priority?: boolean
}) {
  if (resolution.kind === "fallback")
    return <div aria-hidden="true" className="media-fallback" />

  const { media } = resolution
  return (
    <Image
      alt={media.alt}
      className={`showcase-media showcase-media--${variant}`}
      height={media.height}
      priority={priority}
      sizes="(max-width: 767px) 100vw, 50vw"
      src={media.src}
      style={{
        objectPosition: `${media.focalPoint.xPercent}% ${media.focalPoint.yPercent}%`,
      }}
      width={media.width}
    />
  )
}

export function ShowcaseCta({
  cta,
  locale,
  className = "text-link",
}: {
  cta: ShowcaseContent["home"]["finalCta"]
  locale: Locale
  className?: string
}) {
  return (
    <Link
      className={className}
      href={getCtaPathname(cta)}
      locale={locale}
      prefetch={cta.routeId === "home" ? undefined : false}
    >
      {cta.label}
    </Link>
  )
}
