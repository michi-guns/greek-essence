import type { KnipConfig } from "knip"

const config = {
  entry: ["unlighthouse.config.ts"],
  ignoreDependencies: [
    // Installed for the repository-approved interactive browser workflow.
    "@playwright/cli",
    // Invoked as a nested binary by quality:unlighthouse.
    "@unlighthouse/cli",
    // Supplies Chromium to Unlighthouse at runtime.
    "puppeteer",
  ],
} satisfies KnipConfig

export default config
