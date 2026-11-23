# Pictogram parable reel

A faceless black-and-white explainer reel drawn in code: one HTML canvas page where every frame is a function of time, beats pinned to the voiceover's word times, sound effects placed on the frames where things appear, and an App Store end card. The example is a 20-beat, 70-second story ("The best app idea you've ever heard will never get built").

## Files
| File | What it is |
|---|---|
| `script.txt` | The example script, one paragraph per line |
| `cues.map` | Where each beat lands, as words in the script |
| `build/reel.html` | The page: loads `assets/brand.js`, `cues.js`, `kit.js`, `beats.js` |
| `build/kit.js` | Drawing kit: background, glow, text, pills, bubbles, people, bulb, phone, price tag, cards, clock, rocket, dice, App Store listing, sound-event recorder |
| `build/beats.js` | The 20 beats and `renderAt(T)` |
| `build/cues.js` | Beat times (written by `tools/make_cues.py`) |
| `build/render.py` | Frame-by-frame render to MP4 with the audio |
| `build/events.py`, `build/sfx.py` | Log on-screen events, then synthesise and mix the sound effects |
| `tools/make_cues.py` | Voiceover to cue times (faster-whisper) |

## Requirements
Python 3.9+, `pip install playwright numpy scipy faster-whisper && playwright install chromium`, ffmpeg on the PATH.

## Make one
```bash
# 1. voice (see pipelines/voice)
../voice/.venv/bin/python ../voice/reel_vo.py m_smooth script.txt vo/voiceover.wav --f0 130-165
# 2. cues
python3 tools/make_cues.py vo/voiceover.wav cues.map build/cues.js
# 3. look at it
open build/reel.html#play
# 4. sound
python3 build/events.py build/events.json
python3 build/sfx.py build/events.json vo/voiceover.wav vo/mix.wav
# 5. render
python3 build/render.py vo/mix.wav out.mp4
```
To change the story, edit `script.txt`, `cues.map` and the beat functions. To change the brand, edit `brand.config.json` at the repo root and run `engine/tools/apply_brand.py`.
