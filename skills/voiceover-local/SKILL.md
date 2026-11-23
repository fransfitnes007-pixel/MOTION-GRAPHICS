---
name: voiceover-local
description: "Generate fast, upbeat, natural voiceovers locally on Apple Silicon with open models (Qwen3-TTS presets and voice design, Kokoro), at a set pace and pitch, with no cloud key. Use for any reel or film narration, or when the user wants a new voice, a faster or deeper voice, or more voice options."
---

# Local voiceover

`KIT` = the repository root. Tools live in `KIT/pipelines/voice/`. One-time setup (about 5 GB of models):
```bash
bash KIT/pipelines/voice/setup.sh
```
Not on Apple Silicon: use Kokoro through its own package, or `voiceover-elevenlabs`.

## Make a voiceover
```bash
cd KIT/pipelines/voice
.venv/bin/python voice.py f_heart script.txt out.wav             # short script, one take
.venv/bin/python reel_vo.py m_smooth script.txt out.wav --f0 130-165   # long script: one paragraph per line
```
- `voices/voices.json` lists the voices. `pace.syllables_per_second` (default 5.0) is the target; `--pace 5.5` overrides it.
- What the tools do: cut dead air to 0.08 s, time-stretch to the target pace without changing pitch (capped at 1.3 to 1.5x so it never sounds sped up), optional pitch shift (`"pitch": -2` semitones), loudness -14 LUFS, 48 kHz mono.
- `reel_vo.py` records each line up to four times and keeps the take whose pitch is inside `--f0`, because long single takes drift higher and lose the last word.

## Make new voices
```bash
.venv/bin/python design.py f_new="A woman in her thirties with a low, warm voice, fast and smooth, confident, not breathy"
```
Ready-made descriptions are in `voices/designs.txt`. Describe age, pitch, pace and energy, and say what it must not be ("not girly, not high-pitched").

## Check it (you cannot listen, so measure)
```bash
python3 tools/f0.py out.wav
```
- Adult male narration sits near 95 to 150 Hz, adult female near 165 to 240 Hz. Higher or a very wide range reads as childlike.
- Pace: syllables / seconds of speech. About 3.9 is typical viral narration; most people ask for faster, 5.0 is the default.
- Run `transcribe` on the result and compare with the script to catch swallowed or wrong words.
- Brand names: spell them the way they should sound ("Ky-oo-bee" for an odd name, "shadow banned" as two words). Keep a pronunciation copy of the script separate from the on-screen copy.
- Always tell the user these were chosen by measurement and ask them to listen.
