import { test, expect } from '@playwright/test'

test('greets user', async ({ page }) => {
  await page.goto('/')
  await expect(page.getByText('SimpleEasy')).toBeVisible()
  await page.getByLabel(/name/i).fill('Alice')
  await page.getByRole('button', { name: /greet|saudar/i }).click()
  await expect(page.getByText(/Alice/)).toBeVisible()
})
