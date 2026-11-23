---
name: cover-wall-tight-crop-pull-back-scale-rotatex-pull
description: "A grid of video covers starts at 3.2x so one tile fills the screen, pulls back to the whole wall tilted 16 degrees, approval stamps slam on, a title rises, and the wall whips upward out of frame. A match cut out of a zoom: the previous scene ends zoomed into a tile and this one opens on that tile and reveals it was one of many."
---

# Cover wall pull-back from a tight crop

**Code name:** Scale and rotateX pull.

## What you see
The scene starts so tight that one video cover fills the frame (3.2x), then pulls back in 0.7s to the whole wall of covers, tilted back 16 degrees, while a slow scroll runs underneath. From 1.2s, six pills reading Approved or Live slam onto covers every 234ms. A title rises into the bottom at 0.9s. At the end the whole wall whips upward off the top with a 40px vertical motion blur.

## When to use it
A match cut out of a zoom: the previous scene ends zoomed into a tile and this one opens on that tile and reveals it was one of many. Good for "there are lots of these". Needs a grid of images dense enough to look like a wall.

## How it works
Three eased values on one element: `pull` (`eo5`, 0.7s) drives scale from 3.2 to 1.06 and rotateX from 0 to 16 degrees; `scroll` (`eio`, whole scene) moves the camera focal point down the page; `wipeOut` (`ei`, last 0.3s) throws the element up 1300px with an SVG vertical blur.

```js
S(pw, { transform: `perspective(2000px) rotateX(${lerp(0, 16, pull)}deg) translateY(${-wipeOut * 1300}px) scale(${lerp(3.2, 1.06, pull)})`, transformOrigin: '540px 400px' })
blur(pw, wipeOut * 40, 'y')
cam(pw, 960, lerp(300, 760, scroll), lerp(1.5, 1.15, pull))
```

`blur()` is the directional blur from the whip pan skill.

Variant: the wall is rotateX 24 to 10 degrees and translateY 120 to -40px over 4.8s with scale 1.05 to 1.12, and the stamps pop from 60 percent with a back ease.

## Numbers that matter
| | |
|---|---|
| Pull | 0 to 0.7s, `eo5`, scale 3.2 to 1.06, rotateX 0 to 16 |
| Stamps | start 1.2s, one every 234ms (half a beat at 128 BPM) |
| Exit | last 0.3s, translateY -1300px, 40px y blur |
| Wall | 9 columns x 4 rows of 9:16 covers |

## Sound
A suggested soundtrack is a synthesised 128 BPM groove in A minor (Am F C G): kick on every beat, claps on 2 and 4, open hats on the offbeats, sidechained bass. Impacts (a sine boom plus filtered noise crash) land on beats 12, 40, 48 and 60, and a band-passed noise whoosh peaks on each moving transition. The pull-back lands on a beat; stamps are on the half beats.

## Adapt it
- The grid of covers (use your own thumbnails).
- Start zoom (3.2) to match the tile you were zoomed into.
- Stamp text and positions.
- Title.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.
