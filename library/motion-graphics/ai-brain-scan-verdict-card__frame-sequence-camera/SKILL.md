---
name: ai-brain-scan-verdict-card-frame-sequence-camera
description: "A dark scanning window tilts up from below and the camera starts tight on a glowing 3D brain made of strands while callouts light up, then at the verdict the view jumps to a result card and pulls back to show the whole thing. Two lines of type sit above it: \"Checked for you. Before it goes live.\""
---

# AI brain scan with verdict card

**Code name:** Frame-sequence camera.

## What you see
Over the dark stage, a 1600x824 window pops up with a 16-degree forward tilt (`rotateX`) and 120px of travel, reaching full size at 9.0s. Its content is a screen capture of a scanning tool: a violet wireframe brain turning slowly with data callouts in small dark tooltips ("Score A - 8/10", "Score B - 9/10"). The camera starts 2.05x tight on the brain and eases to 1.75x. At 11.25s the content switches to the result: a card with "Yes, good to go", four score tiles and a thumbnail. At 11.15 to 11.75s the camera pulls back to 1.08x so the whole verdict is readable. The window then slides up and blurs out at 12.15s. Words appear above: "Checked for you." at 9.38s, then "Before it goes live." at 10.8s.

## When to use it
Any "the software judges the work" beat: a score, an audit, a scan. The brain is the spectacle; the verdict is the payoff, and the pull-back lets viewers read it. It works best with a real product capture; the brain art in the demo is a stand-in.

## How it works
The page is rendered headless and screenshotted every ~180ms into a 70-frame PNG sequence (see `headless-screen-capture-pipeline__playwright-frame-sequence`). Stack all 70 `<img>` elements in a window and shows exactly one per frame; the frame index is a function of `t`:

```js
const fi = t < 11.25 ? Math.floor(lerp(0, 29, seg(t, 8.5, 11.25))) : Math.min(69, 30 + Math.floor((t - 11.25) * 6))
```
That is a flip book: a pure function of time, so renders are repeatable. The camera is the same pan-zoom as the dashboard window skill, applied to whichever frame is showing:

```js
const pull = eio5(seg(t, 11.15, 11.75))
const z = lerp(lerp(2.05, 1.75, eio(seg(t, 8.6, 11.1))), 1.08, pull)
const fx = lerp(lerp(640, 600, seg(t, 8.6, 11)), 760, pull), fy = lerp(370, 330, pull)
```
The small thumbnail is a separate element placed in capture space at (321,391), because the headless browser could not load the video. The demo swaps the PNG sequence for two drawn layers (strands and a verdict card), and `fi` for a single switch at 11.25s.

## Numbers that matter
| | |
|---|---|
| Window | 1600 wide, aspect of the 1336x688 capture, 46px bar, at (160,210) |
| Entry | 8.35s to 9.0s `eo5`: 120px up, rotateX 16 to 0, scale .9 to 1 |
| Frames | 70 PNGs; 0-29 played over 8.5s to 11.25s; 30-69 at 6 fps after |
| Camera | z 2.05 to 1.75 (8.6s to 11.1s) then to 1.08 (11.15s to 11.75s); focal (640,370) to (760,330) |
| Exit | 12.15s to 12.6s: slides up 60px, shrinks 12%, blurs 12px |
| Type | 118px white, `Checked for you.` out at 10.62s, `Before it goes live.` in at 10.8s |

## Sound
Music drops its clap and half its hats for this section (a dark breath before the next scene); a low impact lands at 8.62s as the window arrives, and a soft pop at 11.68s on "live" with the verdict chip.

## Adapt it
- Replace `runCap`/`verdictCap` with a folder of frames: `frames[i].src = 'frames/f000.png'`.
- `T_*` times and the camera numbers to frame your own capture.
- The type lines.
- The window width and the dark colours.

## Files
- `code/demo.html` (strands drawn with seeded random).
- Related: `verdict-chip-pop__spring-scale-rise`, `dark-stage-circle-reveal__clip-path-circle-wipe`.
