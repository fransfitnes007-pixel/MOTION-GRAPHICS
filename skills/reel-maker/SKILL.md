---
name: reel-maker
description: "Make a finished short-form or long-form motion-graphics video end to end (Reels, TikTok, Shorts, X, YouTube, brand films) from an idea, a script or a reference video. Use when the user asks for a reel, a video, an ad, an explainer, a launch film or \"a video like this one\"."
---

# Reel maker, A to Z

`KIT` below is the repository root: two folders up from this skill. Every step has its own skill with the detail; this one is the order and the checks.

## 0. Pin the brief (one message, then go)
Get or decide, without a long interview: the product and the one thing the viewer should feel or do, the platform(s), the length, the look (a palette from `KIT/palettes/PALETTES.md` or the brand's colours in `KIT/brand.config.json`), voice or no voice, and a reference video if there is one. If `brand.config.json` still says `YourBrand`, run the `brand-setup` skill first.

Defaults when the user gives none: 1080x1920 at 30 fps, 35 to 70 s, voiceover at 5.0 syllables a second, captions on, end card with the brand.

## 1. Script
Follow `short-form-principles`. Write the script as one line per beat. Read it aloud at the target pace: `syllables / 5.0` is its length in seconds. Cut until it fits. Put the product where the story earns it, and state why if that is later than 15 s.

## 2. Pick the format
- **A reference video was given:** run `recreate-viral-format` (measure it, map its beats onto the new story).
- **A look from the library fits:** run `motion-library` and build from those pieces (each is a `render(t)` HTML scene).
- **A faceless explainer or parable:** use the `pictogram-reel` pipeline.
- **Talking-head or UGC with demos:** `ugc-video-playbook`.
- **Generated footage or images:** `ai-image-video`.
Several formats can be cut together: every piece renders to MP4 the same way.

## 3. Voice
`voiceover-local` (free, on the machine) or `voiceover-elevenlabs` (bring your own key). Long scripts: line by line so pitch and pace hold. Check pitch with `KIT/pipelines/voice/tools/f0.py`. Then word timestamps with `transcribe`.

## 4. Picture on the voice
Pin every beat to a word time (cues), never to guesses. Rules that hold for every format:
- Something changes at least every 1 to 2 s: a cut, a counter, typing, a pop-in, a camera drift.
- One idea on screen at a time; one glow or accent on the thing the voice is talking about.
- Text inside the safe zone: x 70 to 1010, y 250 to 1480 on 1080x1920 (platform buttons cover the rest).
- Every frame is a pure function of time, so renders are exact and repeatable.

## 5. Sound
`sound-design`: effects placed on logged on-screen events (pop-ins, cuts, typing, stamps), an optional music bed ducked under the voice, a final boom or chord on the end card. Master: voice around -14 LUFS, true peak -1 dB.

## 6. Render and check
- Render: `node KIT/engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` for library scenes, or the pipeline's own `render.py`.
- Check before calling it done: contact sheet of stills every 2 s, a scan for black or frozen frames (`ffmpeg -vf blackdetect`), duration matches the voice, audio peak below 0 dB, text never outside the safe zone. Look at the stills yourself.
- Say plainly what you could not check (you cannot hear the mix; ask the user to listen).

## 7. Export per platform
| Platform | Size | Notes |
|---|---|---|
| Reels, TikTok, Shorts | 1080x1920, H.264, AAC, 30 fps | keep under 90 s for Reels reach; captions inside the safe zone |
| X | 1920x1080 or 1080x1350 | wide version reads best in the timeline |
| YouTube long-form | 1920x1080 or 3840x2160 | chapters from the beat list |
Use `media-processing` for the ffmpeg commands (crop, captions burn-in, loudness, compression).

## 8. Hand-off
Save next to the video: the script, the cue file, the settings used, and one paragraph on what to change for the next variant. Variants are the point: a new script and new tags on the same parts.
