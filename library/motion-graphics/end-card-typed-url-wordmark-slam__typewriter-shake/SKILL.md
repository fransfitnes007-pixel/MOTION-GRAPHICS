---
name: end-card-typed-url-wordmark-slam-typewriter-shake
description: "On a purple radial field the wordmark drops in from 150 percent with a 20px shake and a white flash, the URL types itself out with a blinking caret, a one-line call to action fades up, and the whole frame fades to black. The last 3 to 5 seconds of a video."
---

# End card with wordmark slam and typed URL

**Code name:** Typewriter reveal with shake.

## What you see
A purple radial field. The wordmark lands from 150 percent, blurred, with a 20px shake over 0.3s and a white flash. From 0.5s a URL types itself out under it with a blinking caret. A call-to-action line fades in at 1.4s. From 3.9s the whole frame fades to black.

## When to use it
The last 3 to 5 seconds of a video. The typed URL is the call to action people can copy. Use it after a colour-fill transition so the field matches.

## How it works
Wordmark entry is `eo5` over 0.3s with a seeded shake; the URL is the full string sliced to a length that grows linearly between 0.5s and 1.3s; the caret blinks at 3 Hz while it types and for 0.9s after.

```js
const n = Math.floor(url.length * seg(lt, .5, 1.3))
endUrl.innerHTML = url.slice(0, n) + (lt > .5 && lt < 2.2 && Math.floor(lt * 3) % 2 === 0 ? '<span style="opacity:.6">|</span>' : '')
stage.style.opacity = 1 - seg(lt, 3.9, 4.35)
```

Simple variant: the field fades in over 0.6s, the wordmark scales from 1.08 to 1 and the URL just fades in. No shake, typing or flash.

## Numbers that matter
| | |
|---|---|
| Wordmark | scale 1.5 to 1, blur 10px to 0, shake 20px decaying over 0.3s |
| URL | 46px weight 700, types 0.5s to 1.3s |
| Sub line | 30px, fades 1.4s to 1.9s |
| Fade out | 3.9s to 4.35s |
| Background | radial-gradient(ellipse at 50% 45%, #7C3AED, #3B1D8F 60%, #12082e) |

## Sound
A suitable soundtrack is a synthesised 128 BPM groove in A minor (Am F C G): kick on every beat, claps on 2 and 4, open hats on the offbeats, sidechained bass. Impacts (a sine boom plus filtered noise crash) land on beats 12, 40, 48 and 60, and a band-passed noise whoosh peaks on each moving transition. The beat-60 impact is on the flash, a held Am chord and a bass note ring under it, and the video fades out with it.

## Adapt it
- The wordmark, URL and call to action.
- Typing window `.5` to `1.3`.
- Background gradient.
- Fade-out time.

## Files
- `code/demo.html` runs on its own with no network. Screens, covers, logos and the wordmark are CSS placeholders.
