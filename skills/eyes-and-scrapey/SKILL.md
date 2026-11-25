---
name: eyes-and-scrapey
description: "The kit's method for reading any reference before rebuilding it: watch it frame by frame in a real browser and screenshot every frame (eyes), read the DOM, CSS, running animations and JS, and scrape static pages politely (scrapey), rebuild as render(t), and run until it matches. Use before recreating a video, a UI component, a site's motion or a brand's style, and before stating any fact about a brand's content or listing."
---

# Eyes and scrapey

`KIT` is the repository root, two folders up from this skill. The full method is `KIT/docs/EYES-AND-SCRAPEY.md`; read it
before the first reference of a session. In short:

1. **Terms first.** Read the site's terms and robots.txt. If they forbid scripted reading or building a library from
   the site, use only your eyes for your own study and put nothing derived from it in a shared library. Never get
   around a paywall, sign-in or quota. Components with no licence shown stay local.
2. **Eyes.** Real browser, pause, step frame by frame, screenshot every frame that changes, write down times,
   distances, overshoots and colours. Contact-sheet videos in the page; download nothing.
3. **Scrapey.** Computed styles, stylesheets (`@keyframes`, `cubic-bezier`, `linear()` springs),
   `document.getAnimations()`, values sampled every 20 to 100 ms, canvas pixels; Scrapling or a public API for static
   pages when the terms allow. Read public code for safety before running anything.
4. **Rebuild** from `engine/templates/demo-template.html` with every number in `CONFIG`; render stills at the same
   moments and compare side by side; fix and repeat until it matches; `verify_library.cjs`.
5. **Output never shrinks** because a quota ran out: change how you read, not how much you deliver, and say what could
   not be read.
6. **Brand facts** (content style, socials, app listing) come from looking and scraping that day, with numbers and the
   date, never from memory.

Credit authors in `meta.json` (`credit`) and `THIRD_PARTY_NOTICES.md`; videos belong to their creators.
