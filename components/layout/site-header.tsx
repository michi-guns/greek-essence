"use client"

import { useEffect, useRef, useState } from "react"

import { LanguageSwitcher } from "./language-switcher"

import { Link } from "@/i18n/navigation"
import type { Locale } from "@/i18n/routing"
import { getRoutePathname, type ShowcaseRouteId } from "@/lib/routes"

const labels = {
  en: {
    nav: "Primary navigation",
    menu: "Menu",
    home: "Home",
    paros: "Paros & Antiparos",
    plan: "Plan my trip",
  },
  el: {
    nav: "Κύρια πλοήγηση",
    menu: "Μενού",
    home: "Αρχική",
    paros: "Πάρος & Αντίπαρος",
    plan: "Σχεδιάστε το ταξίδι μου",
  },
} as const

export function SiteHeader({
  locale,
  routeId,
}: {
  locale: Locale
  routeId: ShowcaseRouteId
}) {
  const [open, setOpen] = useState(false)
  const trigger = useRef<HTMLButtonElement>(null)
  const nav = useRef<HTMLElement>(null)
  const l = labels[locale]

  useEffect(() => {
    if (!open) return
    const keydown = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        setOpen(false)
        trigger.current?.focus()
      }
    }
    const outside = (event: PointerEvent) => {
      if (!nav.current?.contains(event.target as Node)) {
        setOpen(false)
        window.setTimeout(() => trigger.current?.focus())
      }
    }
    window.addEventListener("keydown", keydown)
    document.addEventListener("pointerdown", outside)
    return () => {
      window.removeEventListener("keydown", keydown)
      document.removeEventListener("pointerdown", outside)
    }
  }, [open])

  const close = () => setOpen(false)
  return (
    <header className="site-header">
      <nav ref={nav} aria-label={l.nav} className="site-nav">
        <Link
          aria-current={routeId === "home" ? "page" : undefined}
          className="brand"
          href="/"
          locale={locale}
        >
          Greek Essence
        </Link>
        <button
          ref={trigger}
          className="menu-trigger"
          type="button"
          aria-expanded={open}
          aria-controls="primary-menu"
          onClick={() => setOpen((value) => !value)}
        >
          {l.menu}
        </button>
        <div
          className={open ? "nav-links is-open" : "nav-links"}
          id="primary-menu"
        >
          <Link
            aria-current={routeId === "home" ? "page" : undefined}
            href="/"
            locale={locale}
            onClick={close}
          >
            {l.home}
          </Link>
          <Link
            aria-current={routeId === "paros" ? "page" : undefined}
            href={getRoutePathname("paros")}
            locale={locale}
            onClick={close}
            prefetch={false}
          >
            {l.paros}
          </Link>
          <Link
            className="nav-cta"
            href={getRoutePathname("plan-my-trip")}
            locale={locale}
            onClick={close}
            prefetch={false}
          >
            {l.plan}
          </Link>
          <LanguageSwitcher locale={locale} routeId={routeId} />
        </div>
      </nav>
    </header>
  )
}
