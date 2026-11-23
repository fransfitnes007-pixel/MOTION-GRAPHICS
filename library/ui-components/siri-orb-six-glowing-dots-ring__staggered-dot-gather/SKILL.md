---
name: siri-orb-six-glowing-dots-ring-staggered-dot-gather
description: A small black square with a few white glowing dots that gather from a loose triangle into a ring of six, like a voice assistant listening. Reach for it as a voice mode, AI thinking or listening indicator.
---

# Siri orb of six glowing dots

**Code name:** Staggered dot gather.

## What you see
A near-black page (`#0a0a0c`) with a 360px black rounded square and a deep soft shadow. Nothing else. At the start of the clip three bright dots about 15px across sit in a loose triangle around the centre with a smaller one in the middle. Over the next 1.6 seconds the middle dot moves out, two more dots bud from the centre one after another (at about 0.45s and 0.75s in my timing; the clip shows five dots around 0.9s and six by 1.1s), and the dots spread into a ring of six, about 32px radius, with soft halos. The ring then turns slowly, the dots swell and shrink a little at different rates. The sizes are uneven, the way blobs would be. The clip is only 1.8s long, so the 'fluid' motion after that is not on view; the demo carries on with a slow turn and breathing, then folds back to three dots so the 4.8s loop closes.

## When to use it
Voice assistant listening states, AI is thinking indicators, microphone-on screens, a loader on a dark app. It is tiny and quiet, so it works as a centrepiece with lots of empty space. It is not a loading bar: it says nothing about progress.

## How it works
Each dot has a target on a circle: `angle = -90 + 60 * k + spin`, radius 32 breathing about 6%. The first three dots start at the triangle positions and ease to their targets with `eo5`; the other three start at the centre at 0.5 scale, with staggered delays, and ease out to their targets while growing to full size and fading in. Each dot is a white radial gradient with a larger faint halo behind it.

```js
const ringA = -90 + 60 * k + rot * eo(u)       // u: 0 loose, 1 ring
x = lerp(startX, Math.cos(ringA) * R, eo5(u))
r = DOT_R * (1 + .12 * Math.sin(t * 3 + k))     // uneven breathing
```

The original is named Siri Wave with a fluid-dots variant, so it likely has other variants and a shader or canvas inside. The demo is a plain DOM rebuild of what the clip shows; the exact dot paths are by eye.

## Numbers that matter
| | |
|---|---|
| Square | 360px, radius 18, `#000`, shadow `0 20px 60px rgba(0,0,0,.6)`, page `#0a0a0c` |
| Dots | 6, radius about 7.6px, white with a soft halo |
| Ring | radius 32px, turns 20 degrees per second |
| Start | triangle at 44 to 52px from the centre, small centre dot |
| Gather | 1.6s, extra dots at 0.0, 0.45 and 0.75s |
| Loop | in 0 to 1.6s, hold to 3.4s, fold back to 4.6s, 4.8s total |

## Sound
Silent.

## Adapt it
- `CONFIG.size`, `radius`: the container.
- `CONFIG.ring` and `dotR`: how big the cluster is; make them larger to fill the square.
- `CONFIG.count`: number of dots (the even ones start as the triangle; keep the count even).
- `CONFIG.spin`: turn speed; `glow`: halo size.
- To drive it from audio, scale `rr` and `r` by a volume value.

## Files
- `code/demo.html` runs on its own and loops. Dot paths are read by eye from a 1.8 second clip.
- `media/poster.jpg` is a still of the component.

## Credit
Idea: "Siri Wave" by 40973894 on 21st.dev (https://21st.dev/@40973894/components/siri-wave/fluid-dots), MIT. This demo is an original recreation written from the public preview.
