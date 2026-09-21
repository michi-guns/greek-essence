import { defineConfig, globalIgnores } from 'eslint/config'
import nextVitals from 'eslint-config-next/core-web-vitals'
import nextTs from 'eslint-config-next/typescript'

/**
 * Dependency rules from docs/v1/06-ARCHITECTURE.md §4, enforced rather than reviewed (D-041).
 * Direction: app -> sections -> patterns -> ui. lib and types are free for all to use.
 *
 * NOTE: flat config REPLACES a rule when a later block matches the same file, it does not
 * merge. So each group below must list every restriction that applies to it -- do not factor
 * the shared lib/sanity rule out into a `components/**` block, or the more specific blocks
 * will silently drop it. Verified by deliberate violation in T-00.3.
 */
const NO_SANITY = {
  group: ['@/lib/sanity/*', '**/lib/sanity/*'],
  message: 'Components take domain DTOs, never Sanity documents (D-040). Map in lib/sanity/map.ts.',
}
const NO_SECTIONS = {
  group: ['@/components/sections/*'],
  message: 'Wrong direction: the flow is app -> sections -> patterns -> ui.',
}
const NO_PATTERNS = {
  group: ['@/components/patterns/*'],
  message: 'Primitives are leaves: ui must not import patterns or sections.',
}
const restrict = (...patterns) => ({
  'no-restricted-imports': ['error', { patterns }],
})

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  globalIgnores(['.next/**', 'out/**', 'build/**', 'next-env.d.ts']),
  { files: ['components/sections/**/*.{ts,tsx}'], rules: restrict(NO_SANITY) },
  { files: ['components/patterns/**/*.{ts,tsx}'], rules: restrict(NO_SANITY, NO_SECTIONS) },
  { files: ['components/ui/**/*.{ts,tsx}'], rules: restrict(NO_SANITY, NO_SECTIONS, NO_PATTERNS) },
  {
    files: ['lib/**/*.{ts,tsx}'],
    rules: restrict({
      group: ['@/components/*', '@/app/*'],
      message: 'lib must stay testable without React. It never imports components or routes.',
    }),
  },
])

export default eslintConfig
