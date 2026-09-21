/**
 * Custom next/image loader. Sanity's CDN performs the transformation, which keeps
 * image bytes off the host entirely — see docs/v1/06-ARCHITECTURE.md §14.
 */
type LoaderArgs = { src: string; width: number; quality?: number }

export default function sanityImageLoader({ src, width, quality }: LoaderArgs): string {
  const url = new URL(src)
  url.searchParams.set('w', String(width))
  url.searchParams.set('q', String(quality ?? 75))
  url.searchParams.set('auto', 'format')
  url.searchParams.set('fit', 'max')
  return url.toString()
}
