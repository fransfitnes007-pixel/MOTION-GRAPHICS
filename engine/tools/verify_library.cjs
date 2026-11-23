#!/usr/bin/env node
// Checks every skill folder against engine/SKILL-SPEC.md and actually runs each demo.
//   node verify_library.cjs [category-or-slug-filter]
// Fails a demo if it throws, makes a network request, never changes over time, or draws a different picture for the same t.
const { chromium } = require('playwright-core')
const fs = require('fs'), path = require('path'), crypto = require('crypto')
const ROOT = path.resolve(__dirname, '../../library')
const launchOpts = (args) => ({ headless: true, args, ...(process.env.BROWSER_CHANNEL === 'chromium' ? {} : { channel: process.env.BROWSER_CHANNEL || 'chrome' }) })

const CATS = ['motion-graphics', 'ui-components', 'dashboards', 'sound']
const filter = process.argv[2] || ''
const hash = (b) => crypto.createHash('md5').update(b).digest('hex')
// Anti-aliased edges on 3D-transformed layers can raster a few levels differently between identical paints, more so under
// load, and blur filters vary more than that. So a frame is pure if its DOM is identical; a canvas page, which has no DOM
// to compare, is impure only if over 0.1% of its pixels move by more than 12/255.
// The drawing instructions for a frame, or null if the page draws to a canvas, where only pixels can tell.
const snapshot = () => document.querySelector('canvas') ? null : document.getElementById('stage').outerHTML
async function differs(cmp, a, b, sameDom) {
  if (hash(a) === hash(b) || sameDom) return false
  return cmp.evaluate(async ([x, y]) => {
    const load = async (d) => { const i = new Image(); i.src = 'data:image/png;base64,' + d; await i.decode(); const c = document.createElement('canvas'); c.width = i.width; c.height = i.height; const g = c.getContext('2d'); g.drawImage(i, 0, 0); return g.getImageData(0, 0, c.width, c.height).data }
    const A = await load(x), B = await load(y); let n = 0
    for (let k = 0; k < A.length; k += 4) if (Math.abs(A[k] - B[k]) > 12 || Math.abs(A[k + 1] - B[k + 1]) > 12 || Math.abs(A[k + 2] - B[k + 2]) > 12) n++
    return n / (A.length / 4) > .001
  }, [a.toString('base64'), b.toString('base64')])
}

;(async () => {
  const browser = await chromium.launch(launchOpts(['--force-color-profile=srgb', '--allow-file-access-from-files']))
  const ctx = await browser.newContext({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 })
  const cmp = await ctx.newPage()
  let total = 0, bad = 0
  for (const cat of CATS) {
    const dir = path.join(ROOT, cat)
    if (!fs.existsSync(dir)) continue
    for (const slug of fs.readdirSync(dir).sort()) {
      const s = path.join(dir, slug)
      if (!fs.statSync(s).isDirectory() || !(`${cat}/${slug}`.includes(filter))) continue
      total++
      const issues = []
      if (!/^[a-z0-9-]+__[a-z0-9-]+$/.test(slug)) issues.push('bad folder name')
      for (const f of ['SKILL.md', 'meta.json']) if (!fs.existsSync(path.join(s, f))) issues.push('missing ' + f)
      const media = fs.existsSync(path.join(s, 'media')) ? fs.readdirSync(path.join(s, 'media')) : []
      if (cat !== 'sound' && !media.includes('poster.jpg')) issues.push('no poster')
      if (fs.existsSync(path.join(s, 'meta.json'))) {
        try { const m = JSON.parse(fs.readFileSync(path.join(s, 'meta.json'), 'utf8'))
          if (m.slug !== slug) issues.push('meta slug mismatch'); if (m.category !== cat) issues.push('meta category mismatch')
          for (const k of ['visual_name', 'code_name', 'summary', 'tags']) if (!m[k]) issues.push('meta missing ' + k)
        } catch (e) { issues.push('meta.json invalid') }
      }
      if (fs.existsSync(path.join(s, 'SKILL.md')) && !fs.readFileSync(path.join(s, 'SKILL.md'), 'utf8').startsWith('---\nname:')) issues.push('SKILL.md lacks frontmatter')
      const demo = path.join(s, 'code/demo.html')
      if (cat !== 'sound') {
        if (!fs.existsSync(demo)) issues.push('missing code/demo.html')
        else {
          const page = await ctx.newPage()
          page.on('pageerror', (e) => issues.push('throws: ' + e.message.slice(0, 100)))
          page.on('request', (r) => { if (/^https?:/.test(r.url())) issues.push('network: ' + r.url().slice(0, 80)) })
          try {
            await page.goto('file://' + demo + '?w=1920&h=1080&render=1', { timeout: 20000 })
            await page.evaluate(() => window.READY)
            const dur = await page.evaluate(() => window.DUR)
            if (!(dur > 0)) issues.push('no window.DUR')
            const seen = new Set()
            for (const f of [.15, .5, .85]) {
              const t = dur * f
              await page.evaluate((x) => window.render(x), t); const a = await page.screenshot(), da = await page.evaluate(snapshot)
              await page.evaluate(() => window.render(0)); await page.evaluate((x) => window.render(x), t); const b = await page.screenshot(), db = await page.evaluate(snapshot)
              if (await differs(cmp, a, b, da !== null && da === db)) issues.push(`not pure at t=${t.toFixed(2)}`)
              seen.add(hash(a))
            }
            if (seen.size < 2) issues.push('frames do not change over time')
          } catch (e) { issues.push('load failed: ' + e.message.slice(0, 100)) }
          await page.close()
        }
      }
      if (issues.length) { bad++; console.log(`FAIL ${cat}/${slug}\n   ` + [...new Set(issues)].join('\n   ')) }
    }
  }
  await browser.close()
  console.log(`\n${total - bad}/${total} skills pass`)
  process.exit(bad ? 1 : 0)
})().catch((e) => { console.error(e); process.exit(1) })
