import Link from 'next/link'
import { directions } from './_shared/content'

/** Index of the three GE-003.03 directions. */
export default function DirectionsIndex() {
  return (
    <div className="d-root d-index">
      <p className="d-eyebrow">GE-003.03 · First-fold directions</p>
      <h1 className="d-c-title">Three directions, one content set</h1>
      <ol className="d-index-list">
        {directions.map((d) => (
          <li key={d.slug}>
            <Link href={`/directions/${d.slug}`} className="d-index-link">
              <span className="d-eyebrow">Direction {d.letter}</span>
              <span className="d-card-title">{d.name}</span>
              <span className="d-body">{d.idea}</span>
            </Link>
          </li>
        ))}
      </ol>
    </div>
  )
}
