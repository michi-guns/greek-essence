import { z } from "zod"

const routeIdSchema = z.enum(["home", "paros", "plan-my-trip", "confirmation"])
const ctaBaseSchema = z.object({
  label: z.string().trim().min(1),
})
const ctaSchema = z.union([
  ctaBaseSchema.extend({
    routeId: routeIdSchema,
    destinationContext: z.null(),
  }),
  ctaBaseSchema.extend({
    routeId: z.literal("plan-my-trip"),
    destinationContext: z.literal("paros-antiparos"),
  }),
])
const mediaSchema = z.object({
  src: z.string().trim().startsWith("/images/"),
  width: z.number().int().positive(),
  height: z.number().int().positive(),
  alt: z.string().trim().min(1),
})

export function validateParosFinalCta(cta: z.infer<typeof ctaSchema>): void {
  if (
    cta.routeId !== "plan-my-trip" ||
    cta.destinationContext !== "paros-antiparos"
  ) {
    throw new Error("Paros final CTA requires destination context")
  }
}

const editorialSchema = z.object({
  eyebrow: z.string().trim().min(1).nullable(),
  heading: z.string().trim().min(1),
  body: z.array(z.string().trim().min(1)).min(1),
  media: mediaSchema.nullable(),
})
const cardSchema = z.object({
  id: z.string().trim().min(1),
  title: z.string().trim().min(1),
  summary: z.string().trim().min(1),
  cta: ctaSchema.nullable(),
})
const mediaCardSchema = cardSchema.extend({ media: mediaSchema })

export const showcaseContentSchema = z.object({
  home: z.object({
    metadata: z.object({
      title: z.string().trim().min(1),
      description: z.string().trim().min(1),
    }),
    hero: z.object({
      eyebrow: z.string().trim().min(1).nullable(),
      title: z.string().trim().min(1),
      summary: z.string().trim().min(1),
      media: mediaSchema,
      primaryCta: ctaSchema,
      secondaryCta: ctaSchema.nullable(),
    }),
    promise: editorialSchema,
    parosFeature: cardSchema.extend({ media: mediaSchema }),
    howItWorks: z.object({
      heading: z.string().trim().min(1),
      steps: z.tuple([
        z.object({
          title: z.string().trim().min(1),
          summary: z.string().trim().min(1),
        }),
        z.object({
          title: z.string().trim().min(1),
          summary: z.string().trim().min(1),
        }),
        z.object({
          title: z.string().trim().min(1),
          summary: z.string().trim().min(1),
        }),
      ]),
    }),
    trustStory: editorialSchema,
    finalCta: ctaSchema,
  }),
  paros: z.object({
    metadata: z.object({
      title: z.string().trim().min(1),
      description: z.string().trim().min(1),
    }),
    hero: z.object({
      eyebrow: z.string().trim().min(1).nullable(),
      title: z.string().trim().min(1),
      summary: z.string().trim().min(1),
      media: mediaSchema,
      primaryCta: ctaSchema,
      secondaryCta: ctaSchema.nullable(),
    }),
    introduction: editorialSchema,
    travelerFit: z.object({
      heading: z.string().trim().min(1),
      items: z.array(cardSchema).min(1),
    }),
    signatureExperiences: z.object({
      heading: z.string().trim().min(1),
      items: z.array(mediaCardSchema).min(1),
    }),
    combinations: z.object({
      heading: z.string().trim().min(1),
      items: z.array(cardSchema).min(1),
    }),
    finalCta: ctaSchema,
  }),
})

export type ShowcaseContent = z.infer<typeof showcaseContentSchema>
