import { defineConfig } from "@playwright/test"

const port = Number(process.env.PLAYWRIGHT_PORT ?? 3100)
const baseURL = `http://127.0.0.1:${port}`

export default defineConfig({
  testDir: "./tests/e2e",
  outputDir: ".artifacts/bootstrap/playwright/test-results",
  timeout: 30_000,
  retries: 0,
  reporter: [
    ["list"],
    [
      "html",
      { outputFolder: ".artifacts/bootstrap/playwright/report", open: "never" },
    ],
  ],
  use: {
    baseURL,
    trace: "retain-on-failure",
    screenshot: "only-on-failure",
    video: "retain-on-failure",
  },
  webServer: {
    command: `pnpm dev --port ${port}`,
    url: baseURL,
    timeout: 120_000,
    reuseExistingServer: !process.env.CI,
  },
  projects: [
    {
      name: "chromium-compact",
      use: { browserName: "chromium", viewport: { width: 390, height: 844 } },
    },
    {
      name: "chromium-medium",
      use: { browserName: "chromium", viewport: { width: 834, height: 1112 } },
    },
    {
      name: "chromium-wide",
      use: { browserName: "chromium", viewport: { width: 1440, height: 1024 } },
    },
  ],
})
