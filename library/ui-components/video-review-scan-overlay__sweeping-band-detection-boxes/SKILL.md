---
name: video-review-scan-overlay-sweeping-band-detection-boxes
description: "A phone-shaped video frame being read by an AI. A violet band sweeps top to bottom and back, a pink face box and an amber text box snap in with glows and tag labels, and a dark readout bar shows the current stage and the playhead. Use to show an AI analysing a vertical video."
---

# Video review scan overlay

**Code name:** Sweeping band and detection boxes.

## What you see
A 9:16 video in a rounded-3xl frame, black, with a faint violet shadow. Before the run a dim veil holds a violet play button with a glow and a pill reading "Run the reviewer". Press it and the video plays under a readout bar at the bottom: the current stage on the left, `0:06 / 0:23` on the right and a 4px progress line in lilac. Once the third stage starts (reading the file), a 64px-tall band of violet light slides from the top of the frame to the bottom and back, 2.4 seconds per sweep at constant speed, with a 1px lilac line and a 12px glow along its centre. When the fourth stage starts a pink box with a pink glow snaps around the face, 52% of the frame wide, tagged "face". At the sixth stage an amber box does the same around the on-screen text at the top, with its tag underneath. Both scale down onto their subject from 115% and 110% while fading in. When the run ends everything leaves and the bar says "Reviewed".

## When to use it
Explaining that an AI is watching the footage, on a landing page, in an onboarding wait state or in a product demo. Works because the boxes appear one after another, each tied to a stage name. Place the boxes on real content in your video. Wrong for landscape video, where the band and boxes need different proportions.

## How it works
Everything is positioned in percentages inside a relative `aspect-[9/16] overflow-hidden` frame, so it scales with the card. The band is one `motion.div` whose `top` is animated through keyframes; `-translate-y-1/2` centres it on that line.

```tsx
<motion.div key="scan" initial={{ top: '0%' }} animate={{ top: ['0%', '100%', '0%'] }}
  transition={{ duration: 2.4, repeat: Infinity, ease: 'linear' }}
  className="absolute inset-x-0 h-16 -translate-y-1/2 bg-gradient-to-b from-transparent via-rv-purple/35 to-transparent">
  <div className="absolute inset-x-0 top-1/2 h-px bg-rv-purplel shadow-[0_0_12px_#A78BFA]" />
</motion.div>
<motion.div key="face" initial={{ opacity: 0, scale: 1.15 }} animate={{ opacity: 1, scale: 1 }}
  className="absolute left-[24%] top-[30%] h-[22%] w-[52%] rounded-lg border-2 border-pink-400/90 shadow-[0_0_20px_rgba(244,114,182,.5)]">
```
All of it sits inside `AnimatePresence`, so each element has an exit fade when its condition goes false (`scanning && at >= 2`, `at >= 3`, `at >= 5`). `at` is a counter advanced every 1.1s by an interval. The readout bar has `backdrop-blur`; the demo drops it because it sits over moving video. The demo draws a placeholder scene instead of video, with colour changes at fixed cut times so the playhead has something to track, and runs the same stage timings.

## Numbers that matter
| | |
|---|---|
| Frame | 260px wide (`max-w-[260px]`), radius 24px, `shadow-2xl shadow-rv-purple/10` |
| Band | height 64px, centre line 1px `#A78BFA`, glow `0 0 12px #A78BFA`, 2.4s linear loop |
| Face box | left 24%, top 30%, 52% by 22%, `border-pink-400/90`, glow `rgba(244,114,182,.5)`, label `bg-pink-400` |
| Text box | left 8%, top 6%, 84% by 18%, `border-amber-300/90`, glow `rgba(251,191,36,.5)`, label under the box |
| Entrance | opacity 0 to 1, scale 1.15 (face) and 1.1 (text) to 1 |
| Readout | `inset-x-3 bottom-3`, `bg-black/65`, 10px semibold, progress `h-1 bg-rv-purplel` |
| Stage clock | 1.1s per stage, 8 stages |

## Sound
Silent. A rising scan tone while the band moves, and a short blip as each box lands, would fit.

## Adapt it
- Box positions, sizes and labels for your footage.
- The band colour and speed, or two bands for a busier scan.
- Which stage reveals which box.
- The idle veil copy.

## Files
- `code/demo.html` runs on its own and loops in 11s.
