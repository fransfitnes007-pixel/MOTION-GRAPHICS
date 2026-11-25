---
name: ui-state-morph-chain-sum-of-springs-rounded-rect
description: One black rounded shape never cuts: a button becomes a loader, a tick, a toast and a tab bar whose indicator stretches between tabs, then the button again. Rebuilt by eye from a public motion video (see Credit); use it in app promos and launch reels.
---

# UI state morph chain

**Code name:** Sum of springs on one rounded rect. Rebuilt by eye from a public motion video; original code, credited below.

## What you see
Warm grey (#ecede8). A black "Generate" pill; the cursor clicks it at 0.48s. It springs into an 88px circle with a spinning white arc (0.62s), the arc becomes a drawn tick (1.55s), the circle stretches into a 520px toast "Saved to your library" (2.15s), then into a 600px tab bar with four tabs and a white indicator on Home (3.05s). The cursor clicks Library then Search: the indicator's leading edge shoots ahead and the trailing edge catches up, so it stretches and then settles. At 4.4s the bar springs back into the Generate pill. Contents swap with a short blur (out .12s, in .2s). A camera zoom follows each state (2.1x for the small circle, 1.22x for the bar).

## When to use it
Feature beats in a product film where you want continuity instead of cuts: generate, wait, done, saved, navigate. It is the standard "Dribbble-level UI motion" move in the gallery. Wrong when the states are real screens with lots of content; use a camera move over real UI instead.

## How it works
Every property with several targets is the first value plus one spring per change, so it is still a pure function of time even with 6 changes queued (rule from @twoclipping's public prompt):
```js
const sumSpring = (t, keys, col) => keys.reduce((v, k, i) => i ? v + (k[col] - keys[i-1][col]) * sstep(t - k[0], 2.3, .78) : k[col], 0)
// width, height, radius and camera zoom each read their own column of CONFIG.states
```
The tab indicator is two values, its left and right edge. On a move to the right the right edge uses the fast spring (3.4 Hz) and the left the slow one (1.7 Hz), and the reverse when moving left. That is the whole stretch. The cursor is placed in camera space so it scales with the zoom.

## Numbers that matter
| | |
|---|---|
| Shape spring | f 2.3 Hz, zeta .78 (about 2% overshoot) |
| Camera | same sum, f 1.4 zeta .9; 1.55 / 2.1 / 1.3 / 1.22 |
| Indicator edges | lead 3.4 Hz, trail 1.7 Hz, zeta .8 |
| Content swap | out .12s ease-in, in .2s ease-out, blur 8px |
| Beat | states land on .5s multiples (120 BPM) |

## Sound
UI clicks on each press, a tiny tick when the tick draws, a soft swish under the toast stretch. Place each by its measured peak. The demo is silent.

## Adapt it
- `states`: add or remove rows `[time, w, h, radius, zoom]` and a matching content layer and `win` range.
- `button`, `toast`, `tabs` text.
- `bg` and `ink` (it works inverted: white shape on black).

## Files
- `code/demo.html` runs on its own; every value to change is in the `CONFIG` block at the top of the skill script.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "motionvideo.xyz gallery: Shape morphing through UI states" by @twoclipping (https://x.com/twoclipping/status/2103273003555402193), Video belongs to its creator; not included. "revid.ai Claude Opus 5.5 wall #58: Habitify: a UI micro-animation" by @thednyx (https://x.com/thednyx/status/2102653181146575329), Video belongs to its creator; not included. Recreated by eye from watching the public video; this demo is original code and contains none of the video. Full notices: `THIRD_PARTY_NOTICES.md`.
