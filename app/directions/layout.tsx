import type { Metadata } from 'next'
import { notFound } from 'next/navigation'
// The whole Fraunces family (opsz, SOFT, WONK, true italic) per 02-DESIGN-SYSTEM §4.1.
// The root layout loads only the weight axis; GE-004.02 owns the final import.
import '@fontsource-variable/fraunces/full.css'
import '@fontsource-variable/fraunces/full-italic.css'
import './_shared/directions.css'

export const metadata: Metadata = {
  title: 'Direction demos',
  robots: { index: false, follow: false },
}

/**
 * GE-003.03 direction demos. Throwaway: GE-005.01 deletes app/directions/. Until then they
 * must never reach the live site, so a Netlify production build renders them as 404.
 */
export default function DirectionsLayout({ children }: { children: React.ReactNode }) {
  if (process.env.CONTEXT === 'production') notFound()
  return children
}
