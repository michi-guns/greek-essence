import { ShowcaseCta, ShowcaseMedia } from "./showcase-media"

import type { ShowcaseContent } from "@/content/schemas/showcase"
import type { Locale } from "@/i18n/routing"

export function ParosSections({
  content,
  locale,
  heroMedia,
}: {
  content: ShowcaseContent["paros"]
  locale: Locale
  heroMedia: ShowcaseContent["paros"]["hero"]["media"]
}) {
  return (
    <main id="main-content">
      <section className="hero section-pad">
        <ShowcaseMedia priority media={heroMedia} variant="hero" />
        <div className="shell hero-copy">
          <p className="eyebrow">{content.hero.eyebrow}</p>
          <h1>{content.hero.title}</h1>
          <p className="lead">{content.hero.summary}</p>
          <div className="cta-row">
            <ShowcaseCta
              cta={content.hero.primaryCta}
              locale={locale}
              className="button button-primary"
            />
          </div>
        </div>
      </section>
      <section className="section-pad">
        <div className="shell editorial narrow">
          <p className="eyebrow">{content.introduction.eyebrow}</p>
          <h2>{content.introduction.heading}</h2>
          {content.introduction.body.map((paragraph) => (
            <p key={paragraph}>{paragraph}</p>
          ))}
        </div>
      </section>
      <section className="section-pad surface">
        <div className="shell">
          <h2>{content.travelerFit.heading}</h2>
          <div className="card-grid">
            {content.travelerFit.items.map((item) => (
              <article className="editorial-card" key={item.id}>
                <h3>{item.title}</h3>
                <p>{item.summary}</p>
              </article>
            ))}
          </div>
        </div>
      </section>
      <section className="section-pad">
        <div className="shell">
          <h2>{content.signatureExperiences.heading}</h2>
          <div className="card-grid">
            {content.signatureExperiences.items.map((item) => (
              <article className="editorial-card media-card" key={item.id}>
                <ShowcaseMedia media={item.media} variant="card" />
                <h3>{item.title}</h3>
                <p>{item.summary}</p>
              </article>
            ))}
          </div>
        </div>
      </section>
      <section className="section-pad surface">
        <div className="shell">
          <h2>{content.combinations.heading}</h2>
          <div className="card-grid">
            {content.combinations.items.map((item) => (
              <article className="editorial-card" key={item.id}>
                <h3>{item.title}</h3>
                <p>{item.summary}</p>
              </article>
            ))}
          </div>
        </div>
      </section>
      <section className="section-pad final-cta">
        <div className="shell narrow">
          <h2>{content.finalCta.label}</h2>
          <ShowcaseCta
            cta={content.finalCta}
            locale={locale}
            className="button button-light"
          />
        </div>
      </section>
    </main>
  )
}
