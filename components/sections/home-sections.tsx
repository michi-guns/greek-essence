import { ShowcaseCta, ShowcaseMedia } from "./showcase-media"

import type { ShowcaseContent } from "@/content/schemas/showcase"
import type { Locale } from "@/i18n/routing"
import type { MediaResolution } from "@/lib/content"

export function HomeSections({
  content,
  locale,
  heroMedia,
  parosMedia,
}: {
  content: ShowcaseContent["home"]
  locale: Locale
  heroMedia: MediaResolution
  parosMedia: MediaResolution
}) {
  return (
    <main id="main-content">
      <section className="hero section-pad">
        <ShowcaseMedia priority resolution={heroMedia} variant="hero" />
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
            {content.hero.secondaryCta ? (
              <ShowcaseCta
                cta={content.hero.secondaryCta}
                locale={locale}
                className="button button-secondary"
              />
            ) : null}
          </div>
        </div>
      </section>
      <section className="section-pad">
        <div className="shell editorial narrow">
          <p className="eyebrow">{content.promise.eyebrow}</p>
          <h2>{content.promise.heading}</h2>
          {content.promise.body.map((paragraph) => (
            <p key={paragraph}>{paragraph}</p>
          ))}
        </div>
      </section>
      <section className="section-pad surface">
        <div className="shell split">
          <ShowcaseMedia resolution={parosMedia} variant="card" />
          <div>
            <p className="eyebrow">
              {locale === "en" ? "An island pairing" : "Δύο νησιά μαζί"}
            </p>
            <h2>{content.parosFeature.title}</h2>
            <p>{content.parosFeature.summary}</p>
            {content.parosFeature.cta ? (
              <ShowcaseCta cta={content.parosFeature.cta} locale={locale} />
            ) : null}
          </div>
        </div>
      </section>
      <section className="section-pad">
        <div className="shell">
          <h2>{content.howItWorks.heading}</h2>
          <ol className="steps">
            {content.howItWorks.steps.map((step, index) => (
              <li key={step.title}>
                <span>{index + 1}</span>
                <h3>{step.title}</h3>
                <p>{step.summary}</p>
              </li>
            ))}
          </ol>
        </div>
      </section>
      <section className="section-pad story">
        <div className="shell narrow">
          <p className="eyebrow">{content.trustStory.eyebrow}</p>
          <h2>{content.trustStory.heading}</h2>
          {content.trustStory.body.map((paragraph) => (
            <p key={paragraph}>{paragraph}</p>
          ))}
        </div>
      </section>
      <section className="section-pad final-cta">
        <div className="shell narrow">
          <h2>
            {locale === "en"
              ? "Your journey can begin here"
              : "Το ταξίδι σας μπορεί να ξεκινήσει εδώ"}
          </h2>
          <p>
            {locale === "en"
              ? "Tell us what you imagine, and take the first step towards a journey with your own rhythm."
              : "Μοιραστείτε όσα φαντάζεστε και κάντε το πρώτο βήμα για ένα ταξίδι στον δικό σας ρυθμό."}
          </p>
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
