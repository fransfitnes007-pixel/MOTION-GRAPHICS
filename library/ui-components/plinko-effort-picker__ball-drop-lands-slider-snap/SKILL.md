---
name: plinko-effort-picker-ball-drop-lands-slider-snap
description: A dark settings panel where a glowing ball drops through a plinko board to choose one of six levels (Auto, Light, Medium, High, Extra High, Ultra), then the purple slider thumb and the label under it move to the result. Reach for it as a playful way to pick a setting or tier at random.
---

# Plinko effort picker

**Code name:** Ball drop that lands on a level and snaps the slider.

## What you see
A dark panel (684 by 540 in the clip, 30px radius, `#1f1f23` to `#17171a`). Header: "Reasoning effort" in 22px semibold with a grey sub line, a purple-tinted pill button on the right ("Again" with a white dot and a bolt, or "Dropping" dimmed while the ball is in play), and a close X. Under it a plinko board 636 by 284 holding five rows of grey pegs (5, 6, 5, 6, 5 pegs, 106px apart, rows 39px apart) and six empty bins along the bottom. Below the board are six labels (Auto, Light, Medium, High, "Extra High" on two lines, Ultra); the active one is bold white with a small purple bar above and below it. Then a 48px slider track with a purple gradient fill ending at a 54px white thumb, with a dot at each of the six stops. A dark pill under the panel reads "5.6 Sol" and either "Choosing..." or the level name.

In the 4.5s clip the ball rests in High. A click on Again sets the sub line to "Ball in play..." and the button to "Dropping". A small glowing purple-white ball appears at the top, bounces down through the pegs in about 2.7s, lands in Medium with a glow, and the thumb slides to Medium. The sub line becomes "Landed on Medium. Thinking eff...".

The demo runs 8s with two drops (Medium, then High) so it returns to its starting state.

## When to use it
A playful chooser where the result may be random or the picker wants a moment of suspense, such as selecting a plan, a model effort, or a reward. It also doubles as a progress indicator because the ball's fall takes a couple of seconds. Not for settings that people change often; waiting 2.7s each time would annoy.

## How it works
The ball's route is scripted, not simulated, so the result is fixed by `pegs` and `bin` in `CONFIG.drops`. A path is the list of peg x positions it hits in each row, always moving 53px left or right between rows, then the bin centre.

```js
{ click: .7, pegs: [638, 585, 532, 585, 638], bin: 2 }     // ends on Medium
```

Each leg between pegs takes 0.4s. The ball's y is a quadratic fall with a small hop (`y = ya + (yb - ya) * u * u - 16 * 4u(1-u)(1-u)`), x eases between pegs, and a peg lights up for 0.3s when it is hit. Four faint ghost copies of the ball at earlier times make the trail. When the last leg ends, the thumb moves to the bin's stop with a spring (k=6, f=9) and the underline bars, label weight, sub line and model pill update. The page's usage shows only `<BallModelPicker className="w-[min(408px,...)]" />`, so levels and copy are built in.

## Numbers that matter
| | |
|---|---|
| Panel | 684 x 540, 30px radius, border `#2a2a2f` |
| Board | 636 x 284 at 24px inset, `#141416`, 20px radius |
| Pegs | 15px, `#5a5a5e`, rows at y 281, 320, 359, 399, 438 (clip px), 106px apart |
| Bins | 6 x 106px, divider `#242427` |
| Ball | 30px, white core, `#8f6bff` halo |
| Slider | track 48px `#2a2a2d`, fill `#6a4fc6` to `#8f74ee`, thumb 54px white |
| Button | 186 x 56, Again `#4a3d7d`, Dropping rgba(90,70,170,.28) |
| Drop timing | legs 0.5, 0.4, 0.4, 0.4, 0.4, 0.5s, about 2.6s total |
| Demo loop | 8s, clicks at 0.7s and 5.0s |

## Sound
Silent.

## Adapt it
- `CONFIG.levels` and `model` for your own six options.
- `drops`: click times, peg routes and target bins (keep each step to a neighbouring peg).
- `hitSec`: faster legs for a quicker drop.
- `accent` and the purple values in the CSS for another brand colour.

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Ball Model Picker" by zanwei on 21st.dev (https://21st.dev/@zanwei/components/ball-model-picker), MIT. This demo is an original recreation written from the public preview.
