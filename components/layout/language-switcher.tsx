import { Link } from "@/i18n/navigation"
import type { Locale } from "@/i18n/routing"
import { getRoutePathname, type ShowcaseRouteId } from "@/lib/routes"

const labels = { en: "Ελληνικά", el: "English" } as const

export function LanguageSwitcher({
  locale,
  routeId,
}: {
  locale: Locale
  routeId: ShowcaseRouteId
}) {
  const otherLocale = locale === "en" ? "el" : "en"
  return (
    <Link href={getRoutePathname(routeId)} locale={otherLocale}>
      {labels[locale]}
    </Link>
  )
}
