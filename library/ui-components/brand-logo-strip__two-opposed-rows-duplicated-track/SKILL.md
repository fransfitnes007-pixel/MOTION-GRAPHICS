---
name: brand-logo-strip-two-opposed-rows-duplicated-track
description: "Two rows of client logos drifting in opposite directions at slightly different speeds, wordmarks and icon-plus-name logos mixed, faded out at both edges. Use as a social-proof strip under a hero or between sections."
---

# Brand logo strip

**Code name:** Two opposed rows, duplicated track.

## What you see
Two horizontal lines of logos, one above the other, 28px high with 64px gaps (48px on phones). The top row moves left, the bottom row moves right, and they never stop. Two logo kinds are mixed. A wordmark is shown alone, flattened to a single ink colour at 75% opacity. An app icon is shown in full colour as a 32px rounded square with a 1px ring, with the brand's name in 15px semibold beside it, at 80% opacity. Both ends fade into the page colour over 112px. Hovering a logo lifts it to full opacity.

## When to use it
Proof that real brands are behind the product, right below the first screen. It reads as texture, so keep the logos recognisable and the speed slow. Not for a row you want people to read name by name, since nothing pauses.

## How it works
Each row renders its list twice inside one flex track and animates the track's x from `0%` to `-50%` (the reverse row goes `-50%` to `0%`). `-50%` is exactly one copy's width, so the jump back to 0 lands on identical pixels and the loop has no seam. The edge fades are two absolutely positioned gradients from the page background colour to transparent.

```tsx
<motion.div className="flex items-center gap-12 sm:gap-16 w-max py-3.5"
  animate={{ x: reverse ? ['-50%', '0%'] : ['0%', '-50%'] }}
  transition={{ duration: seconds, repeat: Infinity, ease: 'linear' }}>
  {[...items, ...items].map(b => <Logo key={...} b={b} />)}
</motion.div>
```
Reduced-motion visitors get `animate={undefined}`, a still strip. The demo uses neutral invented brands and sets both rows to an 8s half-width cycle so the loop is short; the source uses 60s and 70s.

## Numbers that matter
| | |
|---|---|
| Row A | 60s per half-width, moving left |
| Row B | 70s per half-width, moving right |
| Gap | `gap-12` (48px), `sm:gap-16` (64px), row padding 14px top and bottom |
| Wordmark | height 28px (some scaled, e.g. 1.35), opacity .75, hover 1 |
| Icon logo | 32px, radius 8px, ring `ink/10`, name 15px semibold `ink/90`, opacity .8 |
| Edge fade | 64px on phones, 112px (`w-28`) on desktop, 160px for the single-row `BrandLine` |

## Sound
Silent.

## Adapt it
- The two lists and their `seconds`.
- Stagger speeds by 10 to 20% so the rows drift out of step.
- Page colour in the fade gradients (they must match the background exactly).
- Gap and logo height for a denser strip.

Sibling: `logo-wall-marquee__bobbing-linear-loop` is a single row where each logo also bobs; this one is two opposed rows with icon-plus-name logos.

## Files
- `code/demo.html` runs on its own and loops in 8s.
