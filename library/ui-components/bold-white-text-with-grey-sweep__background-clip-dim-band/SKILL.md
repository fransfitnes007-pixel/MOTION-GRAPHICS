---
name: bold-white-text-with-grey-sweep-background-clip-dim-band
description: A big bold white headline on near-black with a soft grey band that slides across the letters, about every 3 seconds. Reach for it as the main title on a page, or as an AI is thinking label.
---

# Bold white text with grey sweep

**Code name:** Background-clip dim band.

## What you see
Near-black page (`#0a0a0a`), one line of bold white text, Introducing the future, tight letter-spacing, centred. For about half a second nothing moves. Then a soft grey patch, about a third of the text wide, appears at the left edge, so the first letters dim, and slides to the right: the dim spot is on 'Intr' at about 0.95s, on 'ucing the' at 1.25s, and on the final letters at 1.6s, then it is gone off the right edge by about 2s. The text then sits plain white until the next pass, which begins at about 3.5s. In the video the loop is about 3 seconds. The effect dims the letters, it does not light them.

## When to use it
Page titles, hero lines, and status text such as Thinking or Generating where the sweep says work is happening. It is subtle, so it works on a heading people will look at for a while. It dims the text, so keep the base colour well above the background.

## How it works
The text is painted with a `linear-gradient` and `background-clip: text` with a transparent fill colour. The gradient is mostly the base colour with one soft dip to grey in the middle, and the dip's centre position is animated from -30% to 130% of the text width. The original animates `background-position` with a CSS keyframe; the demo recomputes the stops from `t` instead.

```css
span { background-image: linear-gradient(90deg, #fafafa 0%, #fafafa calc(C - 30%), #6c6c6c C, #fafafa calc(C + 30%), #fafafa 100%);
       -webkit-background-clip: text; color: transparent; }
/* C goes -30% to 130% between 0.5s and 2.0s of a 3s loop */
```

The existing `shimmer-page-title__background-clip-sweep` does the same trick with a lilac highlight on a rest-then-sweep schedule; this one is a dark dip on white text.

## Numbers that matter
| | |
|---|---|
| Text | bold, tight tracking (-0.03em), `#fafafa`, 36px in the usage (4xl) |
| Band | centre colour about `#6c6c6c`, half-width about 30% of the text |
| Travel | centre from -30% to 130% of the text width |
| Timing | sweep 0.5s to 2.0s of a 3s loop, speed about 1.1 text widths per second |
| Background | `#0a0a0a` |

## Sound
Silent.

## Adapt it
- `CONFIG.text` and `size`.
- `CONFIG.base` and `dim`: swap for a brand colour, or invert for dark-on-light text.
- `CONFIG.period`, `sweepStart`, `sweepEnd`: how often and how fast.
- `CONFIG.bandWidth`: sharper or wider band.

## Files
- `code/demo.html` runs on its own and loops. Text is placeholder copy; the effect is pure gradient math.
- `media/poster.jpg` is a still of the component.

## Credit
Idea: "Shimmer Text" by tom_ui on 21st.dev (https://21st.dev/@tom_ui/components/shimmer-text), MIT. This demo is an original recreation written from the public preview.
