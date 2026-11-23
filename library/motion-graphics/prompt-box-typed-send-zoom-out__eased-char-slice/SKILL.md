---
name: prompt-box-typed-send-zoom-out-eased-char-slice
description: "A glowing prompt box types a sentence on an eased curve, a cursor slides to the send button and clicks, then the box swells and blurs away. The opening beat of a product video where the idea is \"type what you want, get it\": an AI tool, a builder, a launch planner."
---

# Typed prompt box with send click

**Code name:** Eased char slice.

## What you see
A dark blueprint field with a faint purple grid. A rounded prompt box fades up from 30px below at 0 to 0.6s, with a small spaced lilac label above it. A sentence types itself into the box from 0.5s to 3.2s, fast in the middle and slow at both ends, with a lilac caret. At 3.1s a white arrow cursor slides in from the lower right to the purple send button, and at 3.9s it presses (the cursor shrinks to 85 percent, the button to 90 percent) while a thin ring expands from it. From 4.3s the box swells to 2.6x while blurring to 14px, and the label has already faded out. The original cuts to a logo at 5.2s; the demo fades the last 0.3s so the loop does not pop.

## When to use it
The opening beat of a product video where the idea is "type what you want, get it": an AI tool, a builder, a launch planner. The swell-and-blur exit hands over to a logo or a hard cut. It is wrong for anything that is not a text-to-result story, and the typed sentence needs to be short enough to finish in under three seconds.

## How it works
The text is the full string sliced to a length that follows an ease-in-out curve over the typing window, so the typing speeds up and slows down like a person rather than ticking at a fixed rate. The caret blinks at 2.5 Hz, but stays solid while typing.

```js
const n = Math.floor(txt.length * eio(seg(lt, .5, 3.2)))
ptext.innerHTML = txt.slice(0, n) + (Math.floor(lt * 2.5) % 2 === 0 || lt < 3.2 ? '<span style="color:#A78BFA">|</span>' : '')
// exit: the box scales up on an exponential ease while the blur grows
S(box, { transform: `translateY(${(1-inK)*30}px) scale(${1 + ex(seg(lt, 4.3, 5.2)) * 1.6})`, filter: `blur(${seg(lt, 4.5, 5.2) * 14}px)` })
```

The cursor path is two `eio` lerps from (1500,760) to (1386,590) between 3.1 and 3.8s. The click ring is `r = 10 + 60 * eo(k)` over 0.45s with opacity `1 - k`.

## Numbers that matter
| | |
|---|---|
| Box | 1000 x 200 at (460, 440), radius 28px, fill rgba(16,14,28,.92), 1px lilac border, 80px purple glow |
| Typing | 0.5s to 3.2s, `eio`, 50 characters |
| Cursor | travels 3.1s to 3.8s, press at 3.9s, ring over 0.45s |
| Exit | scale 1 to 2.6 on `ex` (exponential), blur 0 to 14px, 4.3s to 5.2s |
| Colours | purple #8B5CF6 send button, lilac #A78BFA caret, label #C4B5FD at .3em tracking |

## Sound
Suggested sound: a pink-noise whoosh (high-passed at 600 Hz, low-passed at 5.2 kHz, 0.7s long, volume .22) peaking on every scene cut, over a low A-minor drone pad that ducks under the narration. On this scene specifically: key clicks follow the same typing curve (one click per new non-space character, at least 35ms apart, volume .45) and a mouse click lands at 3.9s.

## Adapt it
- The sentence, the label above it and the footer text in the box.
- Typing window (`.5` to `3.2`) to match a voice line.
- Accent colour: the send button, caret and glow.
- Click time `3.9` and the exit window `4.3` to `5.2`.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.
