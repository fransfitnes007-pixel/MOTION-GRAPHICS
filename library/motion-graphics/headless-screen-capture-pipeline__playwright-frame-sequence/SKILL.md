---
name: headless-screen-capture-pipeline-playwright-frame-sequence
description: "A method, not a look: drive a real web app in headless Chrome with Playwright, screenshot each screen at 2x, and record a running interaction as a numbered PNG sequence that a video plays back as a flip book, so real product screens can be zoomed and panned in a frame-accurate render."
---

# Headless screen capture pipeline

**Code name:** Playwright frame sequence.

## What you see
The demo is a diagram of the method, played as three steps over 9s: a headless browser window taking a screenshot per section (thumbnails drop into a strip, each named `shot-<section>.png`), then 70 numbered frames filling a strip at about 120ms each while a scan runs, then a playhead moving across those frames by time. It is a method diagram, not a scene to reuse as-is.

## When to use it
Whenever a video must show a real product, not a mock-up: dashboards, analytics, a running AI process, a live device wall. A recorded screen video cannot be zoomed into without going soft and cannot be driven by a frame-exact render. Stills at 2x and short PNG sequences can. Use it when the app runs locally and its state can be set up by URL or a click.

## How it works
Three scripts, three jobs.

1. **Section stills (`capture.cjs`).** Launch Chrome through `playwright-core` with `channel: 'chrome'`, a 1920x1080 viewport and `deviceScaleFactor: 2` (so every capture is 3840x2160 and survives a 3.4x zoom). Load each section by URL, wait for the network to be idle plus a fixed 3.5s for charts to settle, hide any fixed dev chrome, and `page.screenshot`.
2. **Crops and a run (`capture-run.cjs`).** Rewrite on-screen words in the DOM with a `TreeWalker` (product names swapped to your brand, capture only), replace missing media with cover images by injecting `data:` URLs, take element crops with `getBoundingClientRect()` for close-ups, then click the button that starts a process and screenshot the card every ~120ms (60ms wait plus screenshot time) into `f000.png` to `f069.png`.
3. **Live devices (`capture-devices.cjs`).** Same method on a local dashboard that mirrors real devices, then click through tabs by text.

The frames are consumed with no video decode: stack all 70 `<img>` elements and show one by index.

```js
const rebrand = () => { /* walk text nodes, replace product names, hide fixed tab bars */ }
await page.click('button[aria-label="Run the scan"]')
for (let i = 0; i < 70; i++) { await page.evaluate(rebrand); await page.screenshot({ path: `f${String(i).padStart(3,'0')}.png`, clip: card }); await page.waitForTimeout(60) }
```
Pitfalls found in the scripts: media files may not load headless (give each `<video>` a `poster` instead); re-run the text swap every frame because the app re-renders; hide any floating tab list so it is not in the shot.

## Numbers that matter
| | |
|---|---|
| Viewport | 1920x1080, `deviceScaleFactor: 2`, Chrome via `channel: 'chrome'`, `--force-color-profile=srgb` |
| Settle | `waitUntil: 'networkidle'` then 3,500ms (4,000ms before the run) |
| Frame rate | 70 frames, `waitForTimeout(60)` between, about 120ms apart in practice |
| Playback | frames 0-29 over 2.75s, frames 30+ at 6 per second |
| Sections | home, start, projects, team, items, reviews, analytics, billing, chat (list in `capture.cjs`) |

## Sound
Silent (a tool, not a moment).

## Adapt it
- `BASE`, the `?s=` query and the section list for your app.
- The `rebrand` function: your replacements.
- Number of frames and wait time to match how fast the app animates.
- Output folder: your video reads `shots/` and `shots/run/`.

## Files
- `code/demo.html`: the animated diagram (a standalone rebuild).
