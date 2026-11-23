---
name: shimmer-page-title-background-clip-sweep
description: "A page heading in white with a soft lilac highlight that sweeps once across the letters, then rests for four seconds before sweeping again, under a small violet eyebrow. Use for the main title of each screen in a dark app."
---

# Shimmer page title

**Code name:** Background clip sweep.

## What you see
A small eyebrow in 11px violet capitals with wide tracking, then a 24 to 30px bold white title with tight tracking, then a grey subtitle, with an actions slot at the right. Every few seconds a soft band of lilac light, about a tenth of the title's width, runs left to right across the letters in 1.5 seconds, leaving them white behind it. Then nothing for four seconds. The text is always readable and the colour change is only on the letters, never the background.

## When to use it
The one title on a screen, in a dark UI, where you want a hint of life without a headline animation. Reads as a rare glint, so only use it on one element per screen. Wrong on light backgrounds, where the lilac highlight on dark text barely shows.

## How it works
The text is `background-clip: text` over a gradient that goes white, lilac, lilac, white, sized to 50% of the text's width and not repeated. Because the gradient image is only half as wide as the text and has a white `currentColor` base behind it, outside the image the letters stay white. Animating `background-position-x` slides the image across.

```css
.shimmer { color: #fff; -webkit-text-fill-color: transparent;
  background: currentColor linear-gradient(to right, currentColor 0%, rgba(167,139,250,.85) 40%,
                                           rgba(167,139,250,.85) 60%, currentColor 100%);
  background-clip: text; background-repeat: no-repeat; background-size: 50% 200%; }
```
```tsx
initial={{ backgroundPositionX: '250%' }}
animate={{ backgroundPositionX: ['-100%', '250%'] }}
transition={{ duration: 1.5, delay: 1.5, repeat: Infinity, repeatDelay: 4, ease: 'linear' }}
```
With a 50% wide image, a position of -100% puts it entirely left of the text and 250% entirely right, so the range covers the full pass with margin. The wrapper is `inline-block overflow-hidden` so descenders and the glow stay clipped. Reduced-motion visitors get plain text. The demo starts the first sweep at 2s instead of 1.5s so the clip loops in 5.5s.

## Numbers that matter
| | |
|---|---|
| Sweep | 1.5s linear, `-100%` to `250%` |
| Rest | `repeatDelay` 4s, first start delayed 1.5s |
| Band | 50% wide image, solid lilac from 40% to 60% so about 10% of the title, `rgba(167,139,250,.85)` |
| Title | `text-2xl sm:text-3xl font-bold tracking-tight text-white` |
| Eyebrow | 11px semibold uppercase, tracking `0.14em`, `rv-purplel` `#A78BFA` |

## Sound
Silent.

## Adapt it
- The highlight colour (a warm gold on black looks like foil).
- `repeatDelay`: shorter for a livelier title, longer for a rare glint.
- Image width: 30% for a thin glint, 80% for a broad wash.
- Use `currentColor` so the same component works with any title colour.

## Files
- `code/demo.html` runs on its own and loops in 5.5s.
