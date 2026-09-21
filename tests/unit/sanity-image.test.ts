import { describe, expect, it } from 'vitest'
import sanityImageLoader from '@/lib/sanity/image'

const SRC = 'https://cdn.sanity.io/images/proj/production/abc-1200x800.jpg'

describe('sanityImageLoader', () => {
  it('asks the Sanity CDN for the requested width', () => {
    expect(sanityImageLoader({ src: SRC, width: 640 })).toContain('w=640')
  })

  it('defaults quality to 75 and honours an override', () => {
    expect(sanityImageLoader({ src: SRC, width: 640 })).toContain('q=75')
    expect(sanityImageLoader({ src: SRC, width: 640, quality: 90 })).toContain('q=90')
  })

  it('requests automatic format negotiation so browsers get AVIF or WebP', () => {
    expect(sanityImageLoader({ src: SRC, width: 640 })).toContain('auto=format')
  })

  it('preserves the original asset path', () => {
    expect(sanityImageLoader({ src: SRC, width: 640 })).toContain('abc-1200x800.jpg')
  })
})
