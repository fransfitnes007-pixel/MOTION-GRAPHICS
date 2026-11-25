# Eyes and scrapey: how to read a reference and rebuild it

Every reference in this kit (a viral video, a UI component, a site's motion, a brand's style) is read the same way:
**eyes** (a real browser, looked at like a person, screenshot by screenshot) and **scrapey** (reading the page's DOM,
CSS, JS and network, plus a scraper such as [Scrapling](https://github.com/D4Vinci/Scrapling) for static pages). Then
the piece is rebuilt as a `render(t)` page and run until it matches. Numbers come from that reading, that day, never
from memory.

## 1. Before anything: the terms
- Read the site's terms of use and robots.txt first. If they forbid scripted reading, bulk copying, mirroring or
  building a reference library from the site, stop scripted reading at once and use only your eyes in the browser,
  for your own study. Never put anything derived from such a site into a shared library.
- Respect paywalls, sign-ins and per-person licences: do not sign in for someone, buy, or redistribute paid prompts,
  skills or code. A free daily quota that runs out is not permission to get around it.
- Licences: MIT, ISC, Apache and your own builds can go into a shared library with credit. If a component page shows
  no licence, keep your rebuild local; do not publish it.
- Videos belong to their creators. Watch them, rebuild the motion by eye in your own code, credit the creator when a
  piece is recognisably theirs, never download, re-post or remix their files.

## 2. Eyes: watch it frame by frame
1. Open the reference in a real browser tab (the built-in browser, or Playwright with Chrome when the pane does not run
   `requestAnimationFrame` in the background).
2. Pause it and step through. Screenshot every frame that changes; for video, seek in small steps (1/30 s around the
   moment, 0.25 s elsewhere) and make a contact sheet in the page (draw the `<video>` into a canvas at each time) so
   nothing is downloaded.
3. Write down what you see with times: what enters, from where, how far, how long, what it overshoots, what colour.
4. Screenshots at 0.3 to 0.5 scale are too small to read motion; zoom into the region instead.

## 3. Scrapey: read how it is made
- **DOM and computed styles:** sizes, radii, colours, fonts, shadows (`getComputedStyle`).
- **Stylesheets:** every `@keyframes`, `transition`, `cubic-bezier(...)` and `linear(...)` spring string.
- **Running animations:** `document.getAnimations()` gives keyframes, duration, delay and easing of what is playing.
- **Sample over time:** read a transform, a width or an SVG path every 20 to 100 ms with `requestAnimationFrame` or a
  `MutationObserver`; canvas pixels with `getImageData`. Fit springs and curves to the samples.
- **Static pages:** Scrapling (or any polite scraper) for the HTML and CSS when the terms allow it; public JSON APIs
  when the site offers them.
- **Code that is public** (a GitHub repo, a published package): read it, note the licence, never run it before reading
  it for safety.

## 4. Rebuild, then run until it matches
1. Start from `engine/templates/demo-template.html`. Every frame is `window.render(t)`: no timers, no CSS transitions
   or keyframes, no unseeded random.
2. Put every number you measured into a `CONFIG` block.
3. Render stills at the same moments as your screenshots (`node engine/tools/render_demo.cjs still ...`) and put them
   side by side with the reference.
4. Fix what differs, render again. Repeat until a viewer could not tell which is which at a glance. Typical: three to
   six rounds.
5. Run `node engine/tools/verify_library.cjs <slug>` and write the SKILL.md with the real numbers and what is yours
   rather than seen (say so: "tooltip wording is a placeholder", "dismiss timing is an estimate").

## 5. Output never shrinks
A quota running out, a paywall or a blocked page changes *how* you read (eyes instead of source, a second site instead
of the first), not *how much* you deliver. If the source is locked, rebuild by eye with measurements and mark the
piece `rebuilt-by-eye`. Say plainly what could not be read.

## 6. Brands and stats
Any statement about a brand's content style, social accounts or app listing comes from looking (screenshots) and
reading (scraper, the public App Store lookup `https://itunes.apple.com/lookup?id=<id>`) on the day, with the numbers
and the date. Never from memory.
