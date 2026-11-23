---
name: caption-word-reveal-highlight-ceil-word-count
description: "A centred 40px caption at the bottom of the frame writes itself word by word across the length of the spoken line, with one chosen word bold and lilac, then fades out .4s after the line ends. Voiceover videos that are watched muted."
---

# Bottom caption with word-by-word reveal and one highlighted word

**Code name:** Ceil word count.

## What you see
A line of subtitle-style text at the bottom, centred, 40px and weight 600 with a soft dark shadow. Words appear one at a time, spread across the length of the spoken line, so the text writes itself in time with the voice. One word is bold lilac (#C4B5FD). The line fades out 0.4s after the voice stops.

## When to use it
Voiceover videos that are watched muted. The highlighted word is the one the line is about, so pick it by meaning, not by position.

## How it works
Every frame finds the current line (the last one whose start has passed), works out how many words to show from time since the start, and sets the HTML. Hidden words stay in the layout as transparent spans so the line does not re-centre as it grows.

```js
const shown = Math.ceil(words.length * clamp((t - cur.t) / dur)) || 1
cap.innerHTML = words.map((w, i) => i < shown ? (w.replace(/[.,?]/g, '') === cur.hi ? `<b>${w}</b>` : w) : `<span style="opacity:0">${w}</span>`).join(' ')
cap.style.opacity = t > end ? 1 - seg(t, end, end + .4) : 1
```
`dur` is the real voice length for the line (fill `t` and `end` from the timings your speech generator reports), falling back to 0.32s per word.

## Numbers that matter
| | |
|---|---|
| Text | 40px weight 600, tracking -.01em, shadow 0 2px 20px rgba(0,0,0,.85), 70px from the bottom |
| Highlight | weight 700, #C4B5FD |
| Reveal | `ceil(words * progress)` across the voice length |
| Fade | 0.4s after the line ends |

## Sound
This is the visual of the voiceover; the voice comes from a speech track with the music ducked under it.

## Adapt it
- Lines, start and end times, highlight words.
- Font size and position.
- Highlight colour.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.
