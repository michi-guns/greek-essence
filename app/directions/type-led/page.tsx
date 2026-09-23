import type { Metadata } from 'next'
import { Credits, DemoBar, DemoHeader, MobileAction } from '../_shared/chrome'
import { copy, packages } from '../_shared/content'
import { Photo } from '../_shared/photo'

export const metadata: Metadata = { title: 'A · Type-led' }

/** Direction A, after Le Sirenuse, Kinfolk and Openhouse (02 §4.6). */
export default function TypeLedPage() {
  return (
    <div className="d-root d-a">
      <DemoBar current="type-led" />
      <DemoHeader actionClass="d-btn d-btn-solid d-header-action" />

      <section className="d-a-fold" aria-labelledby="a-title">
        <p className="d-eyebrow">{copy.eyebrow}</p>
        <h1 id="a-title" className="d-display">
          <span className="d-roman">{copy.headline.roman}</span>{' '}
          <em className="d-italic">{copy.headline.italic}</em>
        </h1>
        <Photo
          name="hero"
          hero
          className="d-a-hero d-settle"
          sizes="(min-width: 90rem) 90rem, 100vw"
        />
      </section>

      <section className="d-a-intro">
        <p className="d-lede">{copy.lede}</p>
      </section>

      <section className="d-a-journeys" aria-labelledby="a-journeys">
        <h2 id="a-journeys" className="d-section-title">
          {copy.journeysHeading}
        </h2>
        <ol className="d-a-list">
          {packages.map((p) => (
            <li key={p.place} className="d-a-item d-card">
              <Photo
                name={p.photo}
                className="d-portrait"
                sizes="(min-width: 64rem) 34vw, (min-width: 48rem) 45vw, 90vw"
              />
              <div className="d-a-item-copy">
                <p className="d-eyebrow">
                  {p.region} · {p.days} days
                </p>
                <h3 className="d-card-title">
                  {p.place}
                  <em className="d-card-dek">{p.dek}</em>
                </h3>
                <a href="#" className="d-link">
                  {copy.journeyLink}
                </a>
              </div>
            </li>
          ))}
        </ol>
      </section>

      <section className="d-a-close">
        <p className="d-body">{copy.body}</p>
        <a href="#" className="d-link">
          {copy.personalLink}
        </a>
      </section>

      <Credits />
      <MobileAction />
    </div>
  )
}
