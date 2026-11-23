#!/usr/bin/env node
// Renders media/poster.jpg for every library piece (or those matching a filter) from its own demo.html.
//   node make_posters.cjs [filter] [--force]
const { chromium } = require('playwright-core')
const fs = require('fs'), path = require('path')
const ROOT = path.resolve(__dirname, '../../library')
const CATS = ['motion-graphics', 'ui-components', 'dashboards']
const args = process.argv.slice(2), force = args.includes('--force'), filter = args.find((a) => !a.startsWith('--')) || ''
const launchOpts = (a) => ({ headless: true, args: a, ...(process.env.BROWSER_CHANNEL === 'chromium' ? {} : { channel: process.env.BROWSER_CHANNEL || 'chrome' }) })
;(async () => {
  const browser = await chromium.launch(launchOpts(['--force-color-profile=srgb', '--allow-file-access-from-files']))
  const ctx = await browser.newContext({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 0.5 })
  let made = 0, failed = 0
  for (const cat of CATS) {
    const dir = path.join(ROOT, cat); if (!fs.existsSync(dir)) continue
    for (const slug of fs.readdirSync(dir).sort()) {
      const s = path.join(dir, slug), demo = path.join(s, 'code/demo.html'), out = path.join(s, 'media/poster.jpg')
      if (!fs.existsSync(demo) || !`${cat}/${slug}`.includes(filter) || (fs.existsSync(out) && !force)) continue
      const page = await ctx.newPage()
      const job = (async () => {
        await page.goto('file://' + demo + '?w=1920&h=1080&render=1', { timeout: 20000 })
        await page.evaluate(() => window.READY)
        const dur = await page.evaluate(() => window.DUR)
        await page.evaluate((x) => window.render(x), dur * 0.62)
        await page.waitForTimeout(60)
        fs.mkdirSync(path.dirname(out), { recursive: true })
        await page.screenshot({ path: out, type: 'jpeg', quality: 82, timeout: 20000 })
      })()
      try { await Promise.race([job, new Promise((_, no) => setTimeout(() => no(new Error('timed out after 40 s')), 40000))]); made++; console.log('ok', slug) }
      catch (e) { failed++; console.log('FAIL', `${cat}/${slug}`, e.message.slice(0, 120)) }
      await page.close().catch(() => {})
    }
  }
  await browser.close(); console.log(`posters made ${made}, failed ${failed}`)
})()
