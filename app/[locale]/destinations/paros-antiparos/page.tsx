import type { Metadata } from "next"
import { notFound } from "next/navigation"
import { setRequestLocale } from "next-intl/server"

import { SiteFooter } from "@/components/layout/site-footer"
import { SiteHeader } from "@/components/layout/site-header"
import { ParosSections } from "@/components/sections/paros-sections"
import { routing, type Locale } from "@/i18n/routing"
import { getShowcaseContent } from "@/lib/content"
import { getLocalizedHref } from "@/lib/routes"

type LocalePageProps = { params: Promise<{ locale: string }> }

function getLocale(rawLocale: string): Locale {
  if (!routing.locales.includes(rawLocale as Locale)) notFound()
  return rawLocale as Locale
}

export async function generateMetadata({
  params,
}: LocalePageProps): Promise<Metadata> {
  const { locale: rawLocale } = await params
  const locale = getLocale(rawLocale)
  const { metadata } = getShowcaseContent(locale).paros
  return {
    title: metadata.title,
    description: metadata.description,
    alternates: {
      canonical: getLocalizedHref("paros", locale),
      languages: {
        en: getLocalizedHref("paros", "en"),
        el: getLocalizedHref("paros", "el"),
        "x-default": getLocalizedHref("paros", "en"),
      },
    },
    robots: { index: false, follow: false },
  }
}

export default async function ParosPage({ params }: LocalePageProps) {
  const { locale: rawLocale } = await params
  const locale = getLocale(rawLocale)
  setRequestLocale(locale)
  const content = getShowcaseContent(locale).paros
  return (
    <>
      <a className="skip-link" href="#main-content">
        {locale === "en" ? "Skip to content" : "Μετάβαση στο περιεχόμενο"}
      </a>
      <SiteHeader locale={locale} routeId="paros" />
      <ParosSections
        content={content}
        heroMedia={content.hero.media}
        locale={locale}
      />
      <SiteFooter locale={locale} />
    </>
  )
}
