import { z } from 'zod'

/**
 * Fail loudly at startup rather than serving a site that silently behaves wrong.
 * See docs/v1/06-ARCHITECTURE.md §8.
 */
const publicSchema = z.object({
  NEXT_PUBLIC_SANITY_PROJECT_ID: z.string().min(1),
  NEXT_PUBLIC_SANITY_DATASET: z.string().min(1),
  NEXT_PUBLIC_SITE_URL: z.url(),
  NEXT_PUBLIC_UMAMI_WEBSITE_ID: z.string().optional(),
})

const serverSchema = z.object({
  SANITY_API_READ_TOKEN: z.string().min(1),
  SANITY_REVALIDATE_SECRET: z.string().min(1),
})

function parse<T extends z.ZodType>(schema: T, source: unknown, label: string): z.infer<T> {
  const result = schema.safeParse(source)
  if (!result.success) {
    const issues = result.error.issues.map((i) => `  ${i.path.join('.')}: ${i.message}`).join('\n')
    throw new Error(`Invalid ${label} environment:\n${issues}`)
  }
  return result.data
}

export const publicEnv = parse(
  publicSchema,
  {
    NEXT_PUBLIC_SANITY_PROJECT_ID: process.env.NEXT_PUBLIC_SANITY_PROJECT_ID,
    NEXT_PUBLIC_SANITY_DATASET: process.env.NEXT_PUBLIC_SANITY_DATASET,
    NEXT_PUBLIC_SITE_URL: process.env.NEXT_PUBLIC_SITE_URL,
    NEXT_PUBLIC_UMAMI_WEBSITE_ID: process.env.NEXT_PUBLIC_UMAMI_WEBSITE_ID,
  },
  'public',
)

/** Server-only. Never import this from a client component. */
export function serverEnv() {
  return parse(
    serverSchema,
    {
      SANITY_API_READ_TOKEN: process.env.SANITY_API_READ_TOKEN,
      SANITY_REVALIDATE_SECRET: process.env.SANITY_REVALIDATE_SECRET,
    },
    'server',
  )
}
