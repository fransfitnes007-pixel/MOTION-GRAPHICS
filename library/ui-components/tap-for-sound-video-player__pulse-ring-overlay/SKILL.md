---
name: tap-for-sound-video-player-pulse-ring-overlay
description: "A glass-framed video that autoplays muted behind a dim overlay with a frosted \"Tap for sound\" pill inside a pulsing ring, plus a thin progress bar. One tap restarts the video from 0 with sound and native controls. Reach for it for a sales video or reel that must autoplay."
---

# Tap for sound video player

**Code name:** Pulse ring overlay.

## What you see
A 16:9 video sits in a white glass frame with a soft indigo glow behind it. It is playing, muted, under a gradient that darkens the bottom. In the middle is a frosted pill, "Tap for sound" with a speaker icon, and around it a thin white ring that swells to 1.35x and fades out, then comes back, every 2.2 seconds. A 4px progress bar creeps along the bottom edge. When the pointer taps, the pill, ring and bar vanish at once, the video jumps back to 0:00, and the browser's own controls appear.

## When to use it
A video sales page or hero reel that has to autoplay (browsers only allow muted autoplay) and still needs the viewer to hear the opening. Wrong when the video has no spoken hook, or for a player that should keep the viewer's place when they unmute.

## How it works
Three states from two booleans, `muted` and `started`. Muted and started shows the overlay; not started shows a round play button instead; neither shows native controls. The tap handler is the important part: it sets `muted = false` and `currentTime = 0` so the viewer hears the video from the first word.

```tsx
const unmute = () => { v.muted = false; v.currentTime = 0; v.play(); setMuted(false); setStarted(true) }
```

The ring is a Tailwind animation, not framer-motion:

```js
pulse2: { "0%,100%": { transform: "scale(1)", opacity: "0.6" }, "50%": { transform: "scale(1.35)", opacity: "0" } }
animation: { pulse2: "pulse2 2.2s ease-out infinite" }
```

The demo repeats the keyframes with ease-out on each half. The video is a drifting colour field standing in for footage; the loop length, 8.8s, is four pulses so the ring closes cleanly.

## Numbers that matter
| | |
|---|---|
| Frame | glass-strong, rounded-4xl (36px), 12px padding; screen rounded-3xl; glow `-inset-6 bg-accent/20 blur-3xl` |
| Overlay | gradient to top, ink/60 via transparent to ink/10 |
| Pill | rounded-full, border white/40, fill white/20, backdrop-blur-md, px-6 py-3.5, 16px semibold, speaker icon 20px |
| Ring | 96px, 2px white/60 border, scale 1 to 1.35, opacity .6 to 0, 2.2s ease-out, infinite |
| Progress | h-1, track white/20, fill white/80, width follows currentTime, 300ms |
| On tap | muted false, currentTime 0, controls on |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The label ("Tap for sound") and icon.
- Ring size and the 1.35 scale; remove the ring for a quieter overlay.
- The overlay gradient strength if your first frame is bright.
- Set `autoplayMuted` false to get the plain play-button state instead.

## Files
- `code/demo.html` runs on its own and loops. Photos and logos are CSS placeholders; copy is placeholder text.
