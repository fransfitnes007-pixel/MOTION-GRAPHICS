---
name: wordmark-clip-path-reveal-inset-wipe-shrink-away
description: "A logo reveal using a sliding clip-path edge, then a quick scale-down and lift. Use it on a dark stage when the name should appear like a curtain opening, and the scene should continue straight after."
---

# Wordmark wipe reveal

**Code name:** Clip-path inset wipe, then shrink and rise.

## What you see
Nothing is on the stage. As the name is spoken, the wordmark appears from its left edge as if a curtain were being pulled right: a hard vertical edge sweeps from 0 to 100% of its width over 0.6s with a steep ease in and out, and the letters behind it are already at full size and full brightness. After a short hold it shrinks to 42% while rising 260px, and fades by 1.55s, ready for the next scene to take over the middle of the frame.

## When to use it
A dark-themed video where the name should arrive with authority but without a bounce: on the spoken name, before the product scene. It is quieter than the slam and does not need a stage of its own. Avoid it if the logo is not wider than it is tall; the sweep needs width.

## How it works
`clip-path: inset(top right bottom left)` with only the right value animated reveals the element from the left.

```js
const r = eio5(seg(t, MEET, GK + .35))
wm.style.clipPath = `inset(-10% ${(1 - r) * 100}% -10% 0)`    // negative top/bottom stops the clip cutting glow or spikes
wm.transform = `translateY(${-go * 260}px) scale(${lerp(1, .42, go)})`   // go = eio5(seg(t, 1.05, 1.45))
```

The -10% top and bottom let tall parts of the logo (a logo with long spikes, say) stay visible; only the right edge cuts.

## Numbers that matter
- Wipe: `eio5` from the word "meet" to 0.35s after the name (0.59s).
- Exit: `eio5` over 0.4s, up 260px, scale 1 to 0.42; fade over 0.2s.
- Wordmark box 800 by 382 centred; clip `inset(-10% X% -10% 0)`.

## Sound
None.

## Adapt it
- The logo artwork: use a wide PNG.
- `MEET` and `GK`: the start and end of the sweep.
- Exit direction and size (260px, 0.42).
- Sweep from the right by animating the left inset instead.

## Files
- `code/demo.html` runs on its own and loops. The wordmark is a CSS placeholder.
