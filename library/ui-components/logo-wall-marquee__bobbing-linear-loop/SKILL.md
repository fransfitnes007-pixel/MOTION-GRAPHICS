---
name: logo-wall-marquee-bobbing-linear-loop
description: "A single row of client logos that scrolls left on a slow linear loop, fades into the page at both edges, and has every logo bobbing on its own phase. Reach for it under a hero as brand proof."
---

# Logo wall marquee

**Code name:** Bobbing linear loop.

## What you see
Under a centred eyebrow, headline and one-line lede, a single row of logos moves steadily left at about 34px a second. Each sits in a 240 by 96px slot with 36px between slots, scaled by its optical area so none dominates. The left and right 8% of the row dissolve into the background. Every logo also floats up and down 6 to 9px on its own 5.8 to 7.6 second cycle, started a little later than its neighbour, so the row never moves as one flat sheet.

## When to use it
A "trusted by" strip: under the hero, above pricing, or at the foot of a case page. Needs at least 8 to 10 logos prepared to the same canvas. Wrong for 3 or 4 logos (it will loop the same ones too visibly) or for logos that must be read, which move too much.

## How it works
Two parts. The `InfiniteSlider` measures its content with `react-use-measure`, renders the children twice, and animates a `translation` motion value from 0 to `-(width + gap) / 2` with `ease: "linear"`, `repeat: Infinity` and `onRepeat` resetting to the start, so the seam is invisible. On hover it re-times to a slower duration (80s becomes 200s) and eases between the two. Second, every logo is a `motion.div` with `animate={{ y: [0, a, 0] }}` on `ease: "easeInOut"`, `repeat: Infinity`, and `delay: (i % 5) * 0.4`, picking one of five amplitude and duration pairs.

```tsx
<InfiniteSlider gap={36} duration={80} durationOnHover={200}>
  {list.map((b, i) => { const f = FLOAT[i % FLOAT.length]; return <motion.div animate={{ y: f.y }} transition={{ duration: f.d, repeat: Infinity, ease: "easeInOut", delay: (i % 5) * 0.4 }} className="flex h-24 w-[210px] shrink-0 ..." /> })}
</InfiniteSlider>
```

Edge fade is a CSS mask: `linear-gradient(to right, transparent, black 8%, black 92%, transparent)`. With reduced motion the slider becomes a scrollable row and the bob stops. In the demo the loop fades at the wrap instead of repeating seamlessly, because the logos are all different and a true seamless wrap would need the whole 80 seconds.

## Numbers that matter
| | |
|---|---|
| Slot | 240 by 96px (210 on phones), gap 36px |
| Speed | half the row width in 80s (about 34px/s with 10 logos); 200s while hovered |
| Bob y | -9, 7, -6, 8, -7.5 px |
| Bob duration | 6.4, 7.2, 5.8, 6.8, 7.6 s; delay (i % 5) x .4 s |
| Edge fade | mask, 8% each side |
| Logo size | max-h-20 (80px) with auto width, pre-rendered on one 440 by 160 canvas |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The logos; keep them on one shared canvas so optical sizes match.
- `duration`: lower for faster; keep it above about 40 so it stays calm.
- Bob amplitudes in `FLOAT`, or set the array to a single zero entry for a flat marquee.
- Reverse direction with the `reverse` prop; stack two rows for a wall.

## Files
- `code/demo.html` runs on its own and loops. Logos are invented CSS wordmarks.
