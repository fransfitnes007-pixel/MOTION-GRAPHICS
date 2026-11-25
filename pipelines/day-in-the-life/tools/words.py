#!/usr/bin/env python3
"""Word timestamps for a voice take, on this machine (faster-whisper, small.en, CPU).
  python3 words.py take1.wav --script script.txt
The script is passed as the initial prompt so names and odd words come out spelled the way you wrote them.
Writes take1.words.json ([{"w", "s", "e"}, ...]) next to the wav. pip install faster-whisper"""
import sys, json
from faster_whisper import WhisperModel
args = sys.argv[1:]; prompt = None
if '--script' in args:
    i = args.index('--script'); prompt = open(args[i + 1]).read().strip(); del args[i:i + 2]
m = WhisperModel("small.en", device="cpu", compute_type="int8")
for f in args:
    segs, _ = m.transcribe(f, word_timestamps=True, beam_size=5, initial_prompt=prompt)
    words = [{"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2)} for s in segs for w in s.words]
    json.dump(words, open(f.rsplit('.', 1)[0] + '.words.json', 'w'))
    print(f, round(words[-1]['e'], 2), 's'); print(' '.join(f"{x['w']}[{x['s']:.2f}]" for x in words)); print()
