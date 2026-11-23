---
name: drifting-glow-blobs-blurred-orbs-mood-weights
description: "Three huge blurred colour orbs drifting slowly behind everything on a near-black stage; the scene mood picks which orb is strong (red for danger, gold for warmth, blue for cold). Use it as the base layer of a dark video."
---

# Drifting glow blobs

**Code name:** Blurred orbs with mood weights.

## What you see
Near-black screen with a dull red glow in the lower middle, a faint navy glow at right and a gold-brown one at upper left. The glows wander about 8% of the canvas in each direction, never repeating exactly. When the scene changes, the mood switches: the red orb fades from full strength to 35% while the gold one comes up, and the stage turns from oxblood to amber. In the demo the mood steps red, gold, blue every 3s.

## When to use it
The base under any dark scene with type or cards on it. Pick the mood per scene: red for threat, gold for warmth and payoff, blue for calm. It does not need to be noticed; it stops the black from looking flat.

## How it works
Three absolutely positioned circles, blurred with `filter: blur(120px)`, sized `R * (.55 + .1 i)` with `R = max(W, H)`. `blobs(t, mood)` sets size, opacity and position every frame:

```js
const amp = (m) => (mood === m ? 1 : 0.35)
;[[b1, 0.9 * amp(1), 0.25, 0.3, 0.07], [b2, 0.8 * amp(0), 0.78, 0.7, 0.05], [b3, 0.9 * amp(2), 0.5, 0.95, 0.06]].forEach(([el, a, fx, fy, sp], i) => {
  el.style.opacity = a * 0.9
  el.style.transform = `translate(${fx * W - sz / 2 + Math.sin(t * sp * 6 + i) * 0.08 * W}px, ${fy * H - sz / 2 + Math.cos(t * sp * 5 + i) * 0.08 * H}px)`
})
```
The mood is a hard switch on scene boundaries, not a tween; the cut hides it. A typical mapping: red for the hook, gold for setup and timeline, red for problem events, gold for the payoff and end card. Colours: gold-brown `#3a2a08`, navy `#0f1f3a`, oxblood `#4a1410`.

## Numbers that matter
| | |
|---|---|
| Blur | 120px |
| Orb size | 55%, 65%, 75% of the longer side |
| Anchors (x, y) | gold (.25, .30), navy (.78, .70), red (.50, .95) |
| Drift | 8% of W and H, speeds .07, .05, .06 |
| Weights | active mood 1.0, others .35 |

## Sound
Silent. It pairs well with a low drone (see the sound skills).

## Adapt it
- The three colours.
- The mood mapping per scene.
- `amp(...)` floor (.35) for a stronger switch.
- Drift speed `sp` and amount (.08).

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. 
- `code/fonts/` holds the fonts the demo loads.
