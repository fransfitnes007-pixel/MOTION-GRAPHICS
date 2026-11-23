---
name: browser-window-focal-camera-zoom-focal-point-transform
description: "A browser window holding a dashboard page, with a virtual camera that eases into one area of the page, then slides across to another, while status pills pop in beside it. Showing a product by guiding the eye over one screenshot instead of cutting between many."
---

# Browser window with focal camera zoom

**Code name:** Focal point transform.

## What you see
A dark browser window with traffic-light dots and a URL pill slides up 80px and fades in. At 1.2s the "camera" pushes in to 1.9x on the stats row, then from 3.4s drifts down and back out slightly to the chart. Two glowing status pills ("views, live" and "items delivered") pop in beside the window at 1.9s and 2.4s and fade at 5.2s.

## When to use it
Showing a product by guiding the eye over one screenshot instead of cutting between many. Use it when you have a full-page capture and want to say "here, then here". It needs a capture at 2x or higher so the zoomed text stays sharp.

## How it works
The page is one element inside a clipped viewport. `cam(win, fx, fy, z)` takes a focal point on the page and a zoom, works out the offset that centres that point, and clamps it so the page edges never show.

```js
function cam(w, fx, fy, z) {                    // fx, fy in page px; z = 1 fits the window width
  const k = w.vw / 1920 * z
  const x = clamp(w.vw / 2 - fx * k, w.vw - 1920 * k, 0)
  const y = clamp(w.vh / 2 - fy * k, Math.min(0, w.vh - capH * k), 0)
  w.pg.style.transform = `translate(${x}px,${y}px) scale(${k})`
}
// two eased legs: k1 = eio(seg(lt,1.2,2.6)), k2 = eio(seg(lt,3.4,4.8))
// focal x .5 -> (.42 -> .48), y .3 -> (.24 -> .45), zoom 1 -> 1.9 -> 1.6
```

Capture the page at 2x (Playwright at deviceScaleFactor 2) and move the capture. The demo builds the page from CSS, so it stays sharp at any zoom.

## Numbers that matter
| | |
|---|---|
| Window | 1520 x 900 at (200, 110), radius 20px, 44px chrome bar |
| Entry | 0 to 0.8s, `eo`: opacity, translateY 80px, scale .92 to 1 |
| Camera legs | 1.2s to 2.6s then 3.4s to 4.8s, both `eio` |
| Pills | pop at 1.9s and 2.4s, out at 5.2s to 5.8s |

## Sound
A suggested soundtrack has a pink-noise whoosh (high-passed at 600 Hz, low-passed at 5.2 kHz, 0.7s long, volume .22) peaking on every scene cut, over a low A-minor drone pad that ducks under the narration. Nothing on the zoom itself; the narration carries it.

## Adapt it
- The page (swap `mkPage` for an `<img>` of your screenshot, same transform).
- Focal points and zoom per leg.
- Pill text and positions.
- Window size and URL text.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.
