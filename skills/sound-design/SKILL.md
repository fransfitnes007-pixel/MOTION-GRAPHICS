---
name: sound-design
description: "Add sound effects, a music bed and a final mix to a motion-graphics video, synthesised from scratch (no samples, nothing to license) and placed on the exact frames where things appear. Use when the user asks for sfx, whooshes, clicks, music, \"sound like the original\", or a mix that is too quiet or too loud."
---

# Sound design

`KIT` = the repository root.

## The four families (measured on viral motion-graphics reels)
| Family | Where | Shape |
|---|---|---|
| Click / pop | every tag, bubble, checkmark | 10 to 25 ms rise, 15 to 60 ms fall, bright (6 to 9 kHz) |
| Swish | every scene change, peaking on the cut | 80 to 190 ms rise and fall, band-passed noise sweeping 2 to 8 kHz, panned across |
| Thud | stamps, landings, an X, a title slam | 4 to 12 ms attack, 100 to 300 ms tail, pitch dropping 170 to 60 Hz |
| Boom | the end card, after 0.5 s of silence | 40 to 70 Hz sub plus a 130 Hz tone, about 1.5 s, the loudest moment |
Plus: one key tick per typed character, ticks under every running counter, a riser into big moments, an optional bed (pad or pluck, 55 to 122 bpm) ducked 8 to 12 dB under the voice.

## Place sounds on events, not guesses
For a canvas reel (`pictogram-reel` pipeline):
```bash
python3 build/events.py build/events.json          # plays the reel silently, logs the first frame of every pop-in and typed run
python3 build/sfx.py build/events.json vo/voiceover.wav vo/mix.wav --sfx-only vo/sfx.wav [--level 0.8]
```
`sfx.py` turns logged pills, bubbles, checks, crosses, cards and typing into sounds, adds the hand-placed moments listed per beat, and mixes under the voice. For library scenes, list the event times from the demo's own timing table and reuse the same synth functions. The `KIT/library/sound/` folder has recipes for beds, risers, ducking, cue sheets and the final master.

## Match a reference
Run `KIT/pipelines/reference-analysis/analyze_reference.py` on the reference and on your render. Compare peak levels per family in the side channel, number of effects per second, bed bpm, and the end hit. Effects should sit 15 to 25 dB under the voice peaks, except the final boom.

## Master
Voice about -14 LUFS integrated, true peak -1 dB, soft-clip the sum (`tanh`), fade the last 0.3 s. Check `ffmpeg -af ebur128` and look at a spectrogram of the mix. You cannot hear it: say so and ask the user to listen on a phone speaker and on headphones.
