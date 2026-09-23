import type { Metadata } from 'next'
import { Credits, DemoBar, DemoHeader, MobileAction } from '../_shared/chrome'
import { copy, packages } from '../_shared/content'
import { Photo } from '../_shared/photo'

export const metadata: Metadata = { title: 'C · Editorial grid' }

/** Direction C, after Cereal, Monocle and The Newt (02 §4.6). */
export default function EditorialGridPage() {
  return (
    <div className="d-root d-c">
      <DemoBar current="editorial-grid" />
      <DemoHeader actionClass="d-btn d-btn-solid d-header-action" />

      <section className="d-c-fold" aria-labelledby="c-title">
        <div className="d-c-lead">
          <p className="d-eyebrow">{copy.eyebrow}</p>
          <h1 id="c-title" className="d-c-title">
            <span className="d-roman">{copy.headline.roman}</span>{' '}
            <em className="d-italic">{copy.headline.italic}</em>
          </h1>
          <p className="d-c-dek">{copy.lede}</p>
          <a href="#" className="d-link">
            {copy.personalLink}
          </a>
        </div>
        <Photo
          name="steps"
          hero
          className="d-portrait d-c-photo d-settle"
          sizes="(min-width: 64rem) 30vw, (min-width: 48rem) 40vw, 100vw"
        />
      </section>

      <section className="d-c-journeys" aria-labelledby="c-journeys">
        <div className="d-c-rule">
          <h2 id="c-journeys" className="d-eyebrow">
            {copy.journeysHeading}
          </h2>
          <span className="d-eyebrow d-c-count">{packages.length} journeys</span>
        </div>
        <ol className="d-c-grid">
          {packages.map((p, i) => (
            <li key={p.place} className="d-card">
              <Photo
                name={p.photo}
                className="d-portrait"
                sizes="(min-width: 64rem) 30vw, (min-width: 48rem) 45vw, 90vw"
              />
              <p className="d-eyebrow">
                ({String(i + 1).padStart(2, '0')}) {p.region} · {p.days} days
              </p>
              <h3 className="d-card-title">
                {p.place}
                <em className="d-card-dek">{p.dek}</em>
              </h3>
              <a href="#" className="d-link">
                {copy.journeyLink}
              </a>
            </li>
          ))}
        </ol>
      </section>

      <section className="d-c-close">
        <p className="d-body">{copy.body}</p>
      </section>

      <Credits />
      <MobileAction />
    </div>
  )
}
