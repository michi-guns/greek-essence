import type { Metadata } from 'next'
import '@fontsource-variable/inter'
import '@fontsource-variable/fraunces'
import './globals.css'

export const metadata: Metadata = {
  title: { default: 'Greek Essence', template: '%s · Greek Essence' },
  description: 'Tailor-made journeys in Greece, planned with you.',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-background text-foreground antialiased">
        <a
          href="#main"
          className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-50 focus:rounded focus:bg-white focus:px-4 focus:py-2"
        >
          Skip to content
        </a>
        <div className="flex min-h-dvh flex-col">
          <main id="main" className="flex-1">
            {children}
          </main>
        </div>
      </body>
    </html>
  )
}
