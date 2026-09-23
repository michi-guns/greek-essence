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
