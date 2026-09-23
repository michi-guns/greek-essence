import type { Metadata } from 'next'
import { Credits, DemoBar, DemoHeader } from '../_shared/chrome'
import { copy, packages } from '../_shared/content'
import { coverFactor, Photo } from '../_shared/photo'

export const metadata: Metadata = { title: 'B · Image-led' }

/** Direction B, after Dexamenes, Masseria Moroseta and Aman (02 §4.6). */
export default function ImageLedPage() {
  return (
    <div className="d-root d-b">
      <DemoBar current="image-led" />

      <section className="d-b-fold" aria-labelledby="b-title">
        {/* A 3:2 photo in the 4:5 phone frame renders 1.875 x its width (DS-008) */}
        <Photo
          name="hero"
          hero
          className="d-b-hero d-settle"
          sizes="(min-width: 48rem) 100vw, 188vw"
        />
        <div className="d-b-scrim" aria-hidden="true" />
        <DemoHeader actionClass="d-btn d-btn-outline d-header-action" />
        <div className="d-b-caption">
          <h1 id="b-title" className="d-b-title">
            <span className="d-roman">{copy.headline.roman}</span>{' '}
            <em className="d-italic">{copy.headline.italic}</em>
          </h1>
          <a href="#" className="d-btn d-btn-outline d-b-fold-action">
            {copy.action}
          </a>
        </div>
      </section>

      <section className="d-b-story">
        <div className="d-b-text">
          <p className="d-eyebrow">{copy.eyebrow}</p>
          <p className="d-lede">{copy.lede}</p>
        </div>
        <ul className="d-b-cluster">
          {copy.details.map((d) => (
            <li key={d.photo}>
              <figure>
                <Photo
                  name={d.photo}
                  className="d-portrait"
                  sizes={`(min-width: 64rem) ${Math.ceil(30 * coverFactor(d.photo, 0.8))}vw, ${Math.ceil(60 * coverFactor(d.photo, 0.8))}vw`}
                />
                <figcaption className="d-eyebrow">{d.caption}</figcaption>
              </figure>
            </li>
          ))}
        </ul>
      </section>

      <section className="d-b-journeys" aria-labelledby="b-journeys">
        <h2 id="b-journeys" className="d-eyebrow">
          {copy.journeysHeading}
        </h2>
        <ul className="d-b-grid">
          {packages.map((p) => (
            <li key={p.place} className="d-card">
              <Photo
                name={p.photo}
                className="d-portrait"
                sizes={`(min-width: 48rem) ${Math.ceil(30 * coverFactor(p.photo, 0.8))}vw, ${Math.ceil(90 * coverFactor(p.photo, 0.8))}vw`}
              />
              <p className="d-eyebrow">
                {p.region} · {p.days} days
              </p>
              <h3 className="d-b-card-title">
                <a href="#" className="d-link-quiet">
                  {p.place}
                </a>
              </h3>
            </li>
          ))}
        </ul>
      </section>

      <section className="d-b-close">
        <a href="#" className="d-btn d-btn-solid">
          {copy.action}
        </a>
        <a href="#" className="d-link">
          {copy.personalLink}
        </a>
      </section>

      <Credits />
    </div>
  )
}
