---
name: cutting-picture-to-voice-word-timestamp-table
description: "A speech-to-text pass gives the start time of every word; each scene cut is that time minus a small lead, and the sounds follow. When a video is built around a voiceover."
---

# Cutting picture to voice words

**Code name:** Word timestamp table.

## What you hear
A 24 s track with no music or voice: a tiny high tick on the start of every one of the 49 words in the voice take, so you hear the rhythm of the speech, and a whoosh at every scene cut. The whooshes fall just before the words that start a scene. It also prints the cut table.

## When to use it
When a video is built around a voiceover. Record the voice first, get word times from it, and derive every cut and every sound from the table. That keeps the picture, the voice and the sounds on the same grid however the voice is re-recorded. It is wrong for music-led edits (use the beat grid) or silent films.

## How it works
Two steps. First, speech-to-text with word timestamps:

```python
m = WhisperModel("small.en", device="cpu", compute_type="int8")
segs, _ = m.transcribe(path, word_timestamps=True, beam_size=5, initial_prompt="YourBrand. yourbrand dot com.")
```

The `initial_prompt` carries the brand words so the model spells them correctly. The result is saved next to the take as `take1.words.json` with `w`, `s`, `e` and probability `p` (low `p` is printed with a `?`). Second, the page's script names the words it uses and shifts them by the time the voice starts in the final track:

```js
const VO = 0.4
const WT = { w01: 0, w02: .34, w03: .86, ... }          // seconds into the take
for (const k in WT) WT[k] += VO
const C = { cut01: WT.w06 - .16, cut02: WT.w13 - .02, cut04: WT.w16 + .02, cut05: WT.w17 - .02, ... }
```

A scene cut is a word time minus a small lead (0.02 to 0.16 s, usually 0.02 to 0.06) so the new picture is already on screen when the word is heard. The audio script has the same cut and word times typed in (whooshes at `cut - 0.18`, pops on the words), so if the voice take changes, both lists need updating from the table. The recipe has the table copied in and prints the result, and can run the transcription itself with `--transcribe`.

## Numbers that matter
| | |
|---|---|
| Transcription | faster-whisper `small.en`, int8, CPU, beam 5 |
| Voice offset | `VO = 0.4` s |
| Lead before a word | 0.02 to 0.06 s for most cuts, 0.16 s for a slower beat; two cuts land on or just after the word |
| Break cut | `w48 - 0.5` |
| End card | fixed at 25.4 s |
| Whoosh on a cut | `cut - 0.18` |
| Words in the take | 49, from the first word at 0 to the last at 22.42 |

## Sound
The ticks and whooshes in this demo are for listening to the grid only. In a real edit they sit under the voice, which is the reason the grid exists.

## Adapt it
- The word list: re-run the transcription on your own take.
- `VO`, the time the voice starts in the final mix.
- The lead for each cut: shorter for punchy cuts, longer when the picture needs time to settle.
- Which words start scenes.

## Files
- The voice take itself is not bundled.
