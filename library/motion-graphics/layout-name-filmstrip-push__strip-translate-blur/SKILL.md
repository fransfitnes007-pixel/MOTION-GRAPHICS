---
name: layout-name-filmstrip-push-strip-translate-blur
description: "A sequence of identical panels, each introduced by a very large title, that slide through one after another on the beat. Use it to step through named options at speed with the same composition every time."
---

# Layout name filmstrip push

**Code name:** Panel groups pushing through on translateX with blur.

## What you see
A panel fills the stage: a small lavender label "LAYOUT 01 / 06", the name in 150px heavy type, a two-line grey description, a laptop on the right and a phone overlapping its bottom right corner. The panel arrives pushed 520px in from the right, blurred 10px and at 96% size, over 0.22s, and leaves 620px to the left, blurred 12px, as the next one arrives. There are six, each at the spoken name, 0.4s to 1.1s apart (they are as long as the voice holds each name). The laptop page scrolls slowly while a panel is on screen.

## When to use it
Walking through a list of named things at the speed of speech, when every item deserves a full-screen identity and a visual. The repeat composition makes it feel like a rhythm. It would be too much for more than six or seven items.

## How it works
Every panel is a group `g` with an `a` (start) and `b` (end) taken from the cut list. One function pushes it through:

```js
function strip(g, t, a, b, din = .45, dout = .4) {
  const pi = eo5(seg(t, a, a + din)), po = eio(seg(t, b - dout, b))
  g.transform = `translateX(${(1 - pi) * 520 - po * 620}px) scale(${.96 + .04 * pi - po * .03})`
  g.opacity = clamp(pi * 1.6) * (1 - po * .9)
  g.filter = (pi < 1 || po > 0) ? `blur(${(1 - pi) * 10 + po * 12}px)` : ''
}
strip(g, t, g.a - .2, g.b, .22, Math.min(.2, (g.b - g.a) * .4))
```

Panels overlap by the length of the entry, so the next one is already arriving as the last leaves. Only the one or two current panels are visible (`display:none` otherwise), so cost does not grow with the count. The same `strip` can be reused for every laptop-and-phone scene.

## Numbers that matter
- Strip: enter 520px right, scale .96, blur 10px (`eo5`); leave 620px left, blur 12px, opacity to 10% (`eio`).
- Enter 0.22s per panel, leave min(0.2s, 40% of its length); panels start 0.2s before their word.
- Name 150px heavy at left 112 top 330; label 24px at top 270; description 30px at top 520.
- Laptop 900px wide at (880, 230); phone 220px at (1620, 450); page scroll y 380 to 620 over the panel.

## Sound

## Adapt it
- Names, labels and descriptions; keep the count equal in the arrays.
- `LCUT`: the time of each name in your voice.
- Push distance (520/620px) and blur for a gentler or harder strip.
- Panel composition: the laptop and phone can be anything.

## Files
- `code/demo.html` runs on its own and loops. The laptops and phones show CSS placeholders. The demo uses the system font stack.
