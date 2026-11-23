---
name: transcribe
description: "Transcribe audio or video locally with faster-whisper and get word-level timestamps. Use for captions, finding cut points in a voiceover, or reading what is said in a reference video."
---

# Transcribe (local, word timestamps)

Local first: no audio leaves the machine and there is no per-minute cost.

## Setup (once)
```bash
python3 -m venv ~/.venvs/transcribe
~/.venvs/transcribe/bin/pip install faster-whisper
brew install ffmpeg        # or your package manager
```
Models download on first use. Sizes: `tiny`/`base` (fast, rough), `small` (good default on CPU), `medium`/`large-v3` (best, wants a GPU or patience).

## Run
```bash
~/.venvs/transcribe/bin/python scripts/transcribe.py <input.mp4|wav|mp3> --model small --out <outdir>
```
Outputs in `<outdir>`:
- `<name>.words.json` : every word with `start`/`end` in seconds
- `<name>.srt` : sentence-level captions
- `<name>.txt` : plain transcript

Options: `--lang en` (skip auto-detect, faster and more accurate), `--device cpu|cuda|auto`, `--max-line 42` (characters per caption line).

## Using the result
- Captions: burn in with ffmpeg (see media-processing skill) or build word-by-word animated captions from `words.json` (highlight the active word using `start`/`end`).
- Cut points: remove silences and filler by cutting between word boundaries, keeping about 80 ms of padding.
- Timing a voiceover to visuals: put each scene's start on a word boundary.
- Reference analysis: feed the transcript to the video-breakdown skill.

## Gotchas
- Music under speech hurts accuracy; if bad, run with `--lang` set and a larger model.
- Whisper can hallucinate text over silence: check any line with no audible speech.
- Always spot-check names, numbers and brand words by ear; fix them in the SRT before burning in.
- Optional cloud route: any hosted Whisper-compatible API works if the user supplies a key through an environment variable (for example `OPENAI_API_KEY`). Say that audio will be uploaded and ask first.
