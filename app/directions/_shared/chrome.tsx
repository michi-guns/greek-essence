import Link from 'next/link'
import { Menu } from 'lucide-react'
import { copy, directions, photos } from './content'

type Slug = (typeof directions)[number]['slug']

/** Says, on every demo page, what is placeholder — and links the three directions. */
export function DemoBar({ current }: { current: Slug }) {
  const here = directions.find((d) => d.slug === current)!
  return (
    <aside className="d-demobar" aria-label="About this demo">
      <p className="d-demobar-long">
        <strong>
          Direction {here.letter} · {here.name}
        </strong>{' '}
        — a design demo. Copy, packages, day counts and photographs are placeholders.
      </p>
      <p className="d-demobar-short">
        <strong>Demo</strong> · placeholders
      </p>
      <nav aria-label="Directions">
        {directions.map((d) => (
          <Link
            key={d.slug}
            href={`/directions/${d.slug}`}
            aria-current={d.slug === current ? 'page' : undefined}
          >
            {d.letter}
          </Link>
        ))}
        <Link href="/directions">All</Link>
      </nav>
    </aside>
  )
}

/** Three things, per 02 §4.4: menu, wordmark centred, one action. */
export function DemoHeader({ actionClass }: { actionClass: string }) {
  return (
    <header className="d-header">
      <button type="button" className="d-menu" aria-label={copy.menu}>
        <Menu size={20} strokeWidth={1.5} />
        <span className="d-menu-label">{copy.menu}</span>
      </button>
      <a href="#" className="d-wordmark">
        {copy.wordmark}
      </a>
      <a href="#" className={actionClass}>
        {copy.action}
      </a>
    </header>
  )
}

/** The pinned action on phones (02 §4.4, after Aman) for directions whose header drops it. */
export function MobileAction() {
  return (
    <a href="#" className="d-btn d-btn-solid d-mobile-action">
      {copy.action}
    </a>
  )
}

export function Credits() {
  const names = [...new Set(Object.values(photos).map((p) => p.author))]
  return (
    <footer className="d-credits">
      <p>
        Placeholder photographs from Unsplash, free under the Unsplash License: {names.join(', ')}.
        They are not of the places named.
      </p>
    </footer>
  )
}
