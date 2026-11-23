#!/usr/bin/env node
// Renders a library demo.html to an MP4 or PNG stills. Same frame-by-frame method as the films (every frame = render(t)).
//   node render_demo.cjs video <demo.html> <out.mp4> [w] [h] [layout]
//   node render_demo.cjs still <demo.html> <outDir> <t1,t2,...> [w] [h] [layout]
const { chromium } = require('playwright-core')
const { spawn } = require('child_process')
const path = require('path'), fs = require('fs')
const FFMPEG = process.env.FFMPEG || 'ffmpeg'
const launchOpts = (args) => ({ headless: true, args, ...(process.env.BROWSER_CHANNEL === 'chromium' ? {} : { channel: process.env.BROWSER_CHANNEL || 'chrome' }) })
const FPS = +(process.env.FPS || 30)
const [mode, demo, out] = process.argv.slice(2)
const rest = process.argv.slice(5)
const times = mode === 'still' ? rest.shift().split(',').map(Number) : null
const W = +(rest[0] || 1920), H = +(rest[1] || 1080), layout = rest[2] || (H > W ? 'tall' : 'wide')

;(async () => {
  const browser = await chromium.launch(launchOpts(['--force-color-profile=srgb', '--font-render-hinting=none', '--allow-file-access-from-files']))
  const page = await (await browser.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: 1 })).newPage()
  let errors = 0
  page.on('pageerror', (e) => { errors++; console.error('PAGE ERROR', e.message) })
  page.on('console', (m) => { if (m.type() === 'error') { errors++; console.error('PAGE', m.text()) } })
  await page.goto('file://' + path.resolve(demo) + `?w=${W}&h=${H}&layout=${layout}&render=1`)
  await page.evaluate(() => window.READY)
  const dur = await page.evaluate(() => window.DUR)
  if (mode === 'still') {
    fs.mkdirSync(out, { recursive: true })
    for (const t of times) {
      await page.evaluate((x) => window.render(x), t)
      await page.screenshot({ path: path.join(out, `t-${t.toFixed(2)}.png`) })
    }
  } else {
    fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true })
    const n = Math.round(dur * FPS)
    const ff = spawn(FFMPEG, ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-vf', 'scale=in_range=pc:out_range=tv,format=yuv420p', '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] })
    for (let i = 0; i < n; i++) {
      await page.evaluate((x) => window.render(x), i / FPS)
      const buf = await page.screenshot({ type: 'jpeg', quality: 94 })
      if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once('drain', r))
    }
    ff.stdin.end()
    await new Promise((r) => ff.on('close', r))
    console.log('wrote', out, `${n} frames`)
  }
  await browser.close()
  if (errors) { console.error(`${errors} page errors`); process.exit(2) }
})().catch((e) => { console.error(e); process.exit(1) })
