---
name: folded-photo-wall-unfurls-flat-3d-tilt-to-flat-column-parallax
description: A grid of portrait photos in four columns that starts folded back and slanted in 3D, then unfurls into a flat full-screen wall while the columns drift into place. Reach for it as a scroll-driven gallery reveal.
---

# Photo wall that unfurls from a tilt to flat

**Code name:** 3D tilt to flat, column parallax.

## What you see
A black rounded frame. The wall of photos is four columns wide, columns 245px wide with 26px gaps, tiles of different heights (260 to 360px) with 4px corners and a couple of dark empty tiles, and the columns start at slightly different heights.

At the start the whole wall is folded: rotated 52 degrees back on X, 24 degrees on Z and shrunk to 62%, seen under 1500px perspective so the near tiles are big and the far ones small and the columns lean to the right. It rests for 0.7s. Then over 3.9s it unfolds with an ease-in-out: the rotation goes to 0, the scale to 100%, the wall shifts to its place, and the columns, which started staggered up and down by different amounts, slide into alignment (that is the parallax). It ends flat and filling the frame, edges cropped by the frame, and holds 1.6s. The demo then folds it back so the loop closes; the video only shows the unfurl.

In the original the unfurl is probably driven by scroll; the 21st.dev usage shows a bare component, so the trigger is not visible here. A small pointer rests at the left while the wall is folded.

## When to use it
A photography, model-agency or lookbook page where the first screen is a dramatic tilted view and scrolling flattens it into the working gallery. It needs many strong portrait images. It is heavy on small phones; consider showing the flat grid only there.

## How it works
One group holds the columns; the transform runs from folded to flat as a single progress value `p` (0 to 1):
```js
grid.transform = `translate3d(${lerp(60, 0, p)}px, ${lerp(-20, 0, p)}px, 0)
                  rotateX(${52 * (1 - p)}deg) rotateY(${-4 * (1 - p)}deg) rotateZ(${24 * (1 - p)}deg)
                  scale(${lerp(.62, 1, p)})`           // parent: perspective 1500px
column[i].transform = translateY((i - 1.5) * 117 * (1 - p) + sin(i * 1.7) * 30 * (1 - p))   // parallax lag
```
Because each column has its own offset that shrinks to zero with `p`, the columns slide past each other while rotating, which gives the unfurl its depth. In the original, `p` presumably comes from scroll; here `prog(t)` is a timed ease-in-out. Photo tiles are SVG portraits standing in for real photos.

## Numbers that matter
| | |
|---|---|
| Canvas | 1066 x 716, frame radius 26 |
| Grid | 4 columns of 245px, gap 26, tiles 260 to 360px tall |
| Folded pose | rotateX 52, rotateZ 24, rotateY -4, scale .62, perspective 1500px |
| Timing | rest .7s, unfurl 3.9s, flat 1.6s, fold back 1.4s |
| Column lag | up to about 175px of vertical offset when folded |

## Sound
Silent.

## Adapt it
- Replace the `portrait()` SVGs with `<img>` tags; `CONFIG.heights` sets each tile's height, `empty` marks blank tiles.
- `CONFIG.tilt` and `startScale` for how folded it starts; `parallax` for how much the columns lag.
- `CONFIG.tUnfurl` and `tFlat` for timing; connect `prog(t)` to scroll position for real scrolling.
- `CONFIG.cols`, `colW` and `gap` change the grid shape.

## Files
- `code/demo.html` runs on its own and loops. Placeholder art is CSS and SVG only.
- `media/poster.jpg` is one frame.

## Credit
Idea: "3D Parallax Unfurling Gallery" by piyushxdev on 21st.dev (https://21st.dev/@piyushxdev/components/3d-parallax-unfurling-gallery), MIT. This demo is an original recreation written from the public preview.
