---
name: spring-draw-wobble-icon-kit__seekable-css-keyframes-svg
description: 40 line icons whose hover animations (Lucide Animated, MIT) were rebuilt as plain SVG plus CSS keyframes that auto-play and loop, with every frame reproducible from a time. Reach for it when an app-promo video needs a heart that beats, a bell that swings, a tick that draws, a send arrow that flies, with no hover and no React.
---

# Spring, draw and wobble icon kit

**Code name:** Seekable CSS keyframes SVG.

## What you see
Dark page, heading "Animated icon kit", then a grid of 40 tiles (10 across wide, 5 across tall). Each tile has one line icon in one of four accents, with its name under it. The tiles spring in one after another over the first 0.6 s. After that every icon plays its own motion on a loop, each shifted 0.11 s from the one before so the grid ripples instead of pulsing in unison: ticks, X and dollar strokes draw themselves in, the heart beats three times, the bell swings, the phone rings, the clock hand spins, the arrows on download and upload spring down and up, the send plane flies off with a dashed trail, the battery bars fade out and refill one by one, party-popper confetti pops. 6 s loop with no seam.

## When to use it
Icon beats in short app-promo videos: a like, a notification, a payment tick, a download, a send, a streak flame, a lock closing. Pick this kit for motion that is quick and physical (0.3 to 1.2 s), then rests until the next loop. If you want slower, softer wobbles use `gentle-wobble-icon-kit__seekable-css-keyframes-svg`; to put an icon inside a chip, tab bar or notification use `icon-in-context-scenes__chips-tab-bar-notification-9x16`. Wrong for a long continuous spinner: use the line-md loaders in `animated-and-static-icon-pack__line-md-smil-plus-lucide`.

## How it works
Each icon is an `<svg viewBox="0 0 24 24">` with `currentColor` strokes. Every moving part has a class and its own `@keyframes`. All keyframes of one icon span the same loop length `L` (percent = seconds / L) and the animation is `L s infinite`, so the motion plays once near the start of the loop and rests for the remainder.

Original hover variant to CSS:

| motion library | CSS |
|---|---|
| `rotate`, `scale`, `x`, `y`, `skewY` arrays | one `transform` track, same numbers (px = viewBox units) |
| `pathLength` 0 to 1 | `pathLength="1"` on the element and `stroke-dasharray: p 1` |
| `pathOffset` | `stroke-dashoffset: -offset` |
| `d` morph (rocket flame) | `d: path("...")` keyframes |
| `transformOrigin`, `originX/Y` | `transform-box: view-box; transform-origin: 12px 12px` (children default to `fill-box` centre) |
| `ease: "easeInOut"` | `cubic-bezier(.42,0,.58,1)` on each keyframe interval |
| spring `{stiffness, damping, mass}` | `linear(...)` easing sampled from the spring equation, duration = time to settle |

To make a frame a pure function of time, `render(t)` does this to every icon:

```js
for (const a of svg.getAnimations({ subtree: true })) { a.pause(); a.currentTime = (t + offset) * 1000 }
```

Same t, same frame, so a recorder can step it at any fps and a tool can scrub it. Loop lengths: 2 s for most, 3 s for battery-full, download, upload, refresh-cw, settings, sparkles; 1.5 s for brain; 6 s for rocket. All divide the demo's `DUR = 6`.

Where the original only moves on hover and snaps back on leave, the loop here goes there and back by itself. Where the original waited on hover-leave, the return is timed (lock shackle, send plane, refresh-cw, settings gear). The rocket's original 6 s shake plays forward once per loop. The sparkles' blink (a 2 s spring in the original) is compressed to 1.6 s so it fits a 3 s loop.

## Numbers that matter
| | |
|---|---|
| Icons | 40, 24 x 24 viewBox, stroke 2, round caps, `currentColor` |
| Start of motion | 0.15 s into each loop, so t = 0 is the plain icon |
| Bell | rotate 0, -10, 10, -10, 0 deg over 0.5 s easeInOut (checked on the live site) |
| Heart | scale 1, 1.08, 1 over 0.45 s, three beats |
| Check / zap / x / flame | pathLength 0 to 1 over 0.4 to 0.6 s, opacity 0 to 1 over 0.1 s |
| Download / upload | arrow y +2 / -2 px, spring stiffness 200 damping 10 |
| Send | plane x +3, y -3, scale 0.8 over 0.5 s; dashed trail draws over 0.55 s |
| Clock | hour hand 360 deg in 0.6 s (cubic-bezier .4,0,.2,1), minute hand 45 deg in 0.5 s |
| Battery | bars fade out 0.4 s, then back in 0.6 s each, 0.4 s apart |
| Grid | stagger 0.11 s, tile spring(7, 11), 4 accents |
| Size of one svg | about 0.6 to 1.8 KB plus its CSS |

## Sound
Silent. Pair with a soft pop for check and heart, a short bell for bell, a swoosh for send.

## Adapt it
- Colour: `CONFIG.accents` (or set `color` on any svg; strokes are `currentColor`).
- Which icons: `CONFIG.only = ['heart','bell','send']`; columns in `CONFIG.cols`.
- One icon alone for a hero beat: inline one file from `code/svg/` at 400 px, set `a.currentTime` as above, or just let it auto-play (each file carries its own `<style>`).
- Speed: change the `L` seconds in `animation:` of that icon's classes (the motion keeps its shape, the rest gets longer or shorter).
- New icon: add its Lucide children and a spec to `code/generator/la_specs.py` (`A(start, dur, ease, key=[values...])`), run `gen.py`. The generator reads the original `.tsx` from the upstream repo.

## The 40 icons
battery-full, bell, bookmark, brain, calendar-check, cart, chart-column-increasing, check, check-check, clock, dollar-sign, download, droplet, eye, flame, heart, home, lock, message-circle, mic, moon, party-popper, phone, play, plus, refresh-cw, rocket, search, send, settings, shield-check, sparkles, trending-up, upload, user, users, wallet, wifi, x, zap.

Not here (they are in the sibling kit): camera, star, trophy, gift, gamepad, dumbbell, book-open, music, video, thumbs-up, crown, target.

## Files
- `code/demo.html` runs the grid and loops; `CONFIG` at the top.
- `code/svg/<name>.svg` 40 standalone auto-playing icons (CSS inside each file).
- `code/generator/` the Python that turned the variants into CSS (`core.py`, `la_specs.py`, `gen.py`).
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Lucide Animated" by pqoqubbw (shown as dmytro on 21st.dev) (https://21st.dev/community/icons), MIT. "Lucide" by Lucide Contributors (https://lucide.dev/), ISC. Rebuilt as render(t) from the published code. Full notices: `THIRD_PARTY_NOTICES.md`.
