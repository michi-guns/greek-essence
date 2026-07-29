import Image from "next/image"

import type { ShowcaseContent } from "@/content/schemas/showcase"
import { Link } from "@/i18n/navigation"
import type { Locale } from "@/i18n/routing"
import { getCtaPathname } from "@/lib/routes"

type ShowcaseMediaContent = ShowcaseContent["home"]["hero"]["media"]

export function ShowcaseMedia({
  media,
  variant,
  priority = false,
}: {
  media: ShowcaseMediaContent
  variant: "hero" | "card"
  priority?: boolean
}) {
  return (
    <Image
      alt={media.alt}
      className={`showcase-media showcase-media--${variant}`}
      decoding={priority ? "sync" : "async"}
      fetchPriority={priority ? "high" : undefined}
      height={media.height}
      loading={priority ? "eager" : "lazy"}
      quality={priority ? 60 : 75}
      sizes="(max-width: 767px) 100vw, 50vw"
      src={media.src}
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
