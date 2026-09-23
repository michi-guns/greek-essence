/**
 * The one content set all three GE-003.03 directions render. Same words, same photographs,
 * so the directions differ only in layout and image treatment (02-DESIGN-SYSTEM §4.6).
 *
 * Copy is an agent draft (D-035). Package names, day counts and photographs are placeholders:
 * no such packages exist yet, and the photographs are not of the places named. The demo bar
 * says so on every page. Throwaway — app/directions/ is deleted by GE-005.01.
 */

export type DemoPhoto = {
  /** images.unsplash.com base URL; the custom loader in lib/sanity/image.ts adds w/q/auto/fit. */
  src: string
  width: number
  height: number
  alt: string
  /** Credit log (D-034). Every photo is free under the Unsplash License. */
  author: string
  page: string
}

const unsplash = (id: string) => `https://images.unsplash.com/${id}`

export const photos = {
  hero: {
    src: unsplash('photo-1629470036684-cb09761b1b25'),
    width: 6810,
    height: 4540,
    alt: 'A white village on a cliff edge above the sea, in hazy late-afternoon light',
    author: 'Florian Wehde',
    page: 'https://unsplash.com/photos/brown-rocky-mountain-during-daytime-j1vUbDkfmTo',
  },
  steps: {
    src: unsplash('photo-1782179283888-e8674e89ba39'),
    width: 5440,
    height: 8156,
    alt: 'Whitewashed steps climbing between houses in a narrow lane',
    author: 'Anastase Maragos',
    page: 'https://unsplash.com/photos/traditional-white-washed-street-with-steps-in-milos-QMyw76NPpoU',
  },
  lane: {
    src: unsplash('photo-1781442512012-26dc08a50e62'),
    width: 3486,
    height: 5229,
    alt: 'A stone path winding between whitewashed walls',
    author: 'DD GR',
    page: 'https://unsplash.com/photos/winding-stone-pathway-with-white-walls-under-bright-sun-Ue1tJqFRoPI',
  },
  stone: {
    src: unsplash('photo-1789236873618-fdca731494e3'),
    width: 4160,
    height: 6240,
    alt: 'Old stone houses and a prickly pear on a cobbled lane',
    author: 'Nenad Radojčić',
    page: 'https://unsplash.com/photos/stone-buildings-and-cactus-in-monemvasia-XRMU5Cn2ccU',
  },
  chapel: {
    src: unsplash('photo-1757435913829-1aedcf7b55af'),
    width: 4672,
    height: 7008,
    alt: 'A small white chapel on a hillside half lost in mist',
    author: 'Kameron Kincade',
    page: 'https://unsplash.com/photos/white-church-on-a-misty-mountain-peak-aaqPb52xqto',
  },
  door: {
    src: unsplash('photo-1597759539135-3086343979c5'),
    width: 2736,
    height: 3648,
    alt: 'A pale arched wooden door set in an old stone wall',
    author: 'Lieze Neven',
    page: 'https://unsplash.com/photos/blue-wooden-door-on-brown-brick-wall-Hy34GtEUTJQ',
  },
  table: {
    src: unsplash('photo-1773701626594-a601beb3297d'),
    width: 5152,
    height: 7728,
    alt: 'A plate of grilled fish with lime on a wooden table, seen from above',
    author: 'Raelle Cameron',
    page: 'https://unsplash.com/photos/seafood-dish-with-lime-served-on-a-wooden-table-6vKbExUjxWQ',
  },
  grove: {
    src: unsplash('photo-1620417844189-f25b50ee8d48'),
    width: 4692,
    height: 3128,
    alt: 'Old olive trees in a grove, light falling through the leaves',
    author: 'Andreas Weilguny',
    page: 'https://unsplash.com/photos/green-and-brown-trees-on-green-grass-field-during-daytime-vGHQ8yt8lhY',
  },
} satisfies Record<string, DemoPhoto>

export const copy = {
  wordmark: 'Greek Essence',
  menu: 'Menu',
  action: 'Plan your trip',
  eyebrow: 'Tailor-made journeys in Greece',
  headline: { roman: 'Greece, planned with you,', italic: 'one slow day at a time' },
  lede: 'Tell us how you like to travel and we will shape a journey around it — the islands, the villages, the tables worth the detour. Or begin with one of the journeys below and make it yours.',
  body: 'Every journey starts as a conversation. You tell us who is coming, when you can go and what a good day looks like to you; we come back with a route, the places to stay and the few things we would not want you to miss.',
  journeysHeading: 'Journeys to begin from',
  journeyLink: 'See the journey',
  personalLink: 'Or tell us where you would like to go',
  details: [
    { photo: 'door', caption: 'The lanes' },
    { photo: 'table', caption: 'The table' },
    { photo: 'grove', caption: 'The groves' },
  ],
} as const

export type DemoPackage = {
  place: string
  dek: string
  region: string
  days: number
  photo: keyof typeof photos
}

/** Placeholder packages: names and day counts are invented for layout only. */
export const packages: DemoPackage[] = [
  {
    place: 'Paros & Antiparos',
    dek: 'Slow days between two harbours',
    region: 'Cyclades',
    days: 8,
    photo: 'lane',
  },
  {
    place: 'Monemvasia & the Mani',
    dek: 'Stone towns at the southern edge',
    region: 'Peloponnese',
    days: 7,
    photo: 'stone',
  },
  {
    place: 'Amorgos',
    dek: 'Footpaths, chapels and a quiet coast',
    region: 'Cyclades',
    days: 6,
    photo: 'chapel',
  },
]

export const directions = [
  {
    slug: 'type-led',
    letter: 'A',
    name: 'Type-led',
    idea: 'The headline is the hero; the photograph waits underneath it.',
  },
  {
    slug: 'image-led',
    letter: 'B',
    name: 'Image-led',
    idea: 'The photograph is the hero; words step back to the corner.',
  },
  {
    slug: 'editorial-grid',
    letter: 'C',
    name: 'Editorial grid',
    idea: 'A magazine front page: headline, one tall photograph, the journeys already in view.',
  },
] as const
