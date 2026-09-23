import Image from 'next/image'
import { photos } from './content'

type Props = {
  name: keyof typeof photos
  /** Rendered width, widened where cover crops a wider photo (DS-008). */
  sizes: string
  className?: string
  /** The largest paint of the fold: load it first. */
  hero?: boolean
}

/**
 * How much wider than its box a photograph renders under object-fit: cover (DS-008):
 * a 3:2 photo in a 4:5 box is 1.875 x the box width. Multiply `sizes` by it.
 */
export function coverFactor(name: keyof typeof photos, boxRatio: number) {
  const photo = photos[name]
  return Math.max(1, photo.width / photo.height / boxRatio)
}

/** A photograph filling a fixed-ratio frame set by the caller's CSS (DS-007). */
export function Photo({ name, sizes, className, hero }: Props) {
  const photo = photos[name]
  return (
    <div className={['d-frame', className].filter(Boolean).join(' ')}>
      <Image
        src={photo.src}
        alt={photo.alt}
        fill
        sizes={sizes}
        loading={hero ? 'eager' : 'lazy'}
        fetchPriority={hero ? 'high' : undefined}
      />
    </div>
  )
}
