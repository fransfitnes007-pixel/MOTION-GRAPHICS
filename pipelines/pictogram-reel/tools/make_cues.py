#!/usr/bin/env python3
"""Turn a voiceover into beat times. Every animation in beats.js is pinned to a cue, so a new voice take re-times the reel.
  python3 tools/make_cues.py vo/voiceover.wav cues.map build/cues.js
cues.map has one cue per line, in script order:   name: the words where it lands
  hook: the best app idea
  reason: and the reason why
A cue lands on the start of the first word of its phrase, searching forward from the previous cue.
In a phrase, * matches any one word and @ matches any one word and marks where the cue lands, so a brand name never
has to be spelled the way the transcriber hears it:   brand: open @ on your phone
Needs faster-whisper."""
import json, re, sys
from faster_whisper import WhisperModel
wav, cmap, out = sys.argv[1:4]
segs, _ = WhisperModel("small", compute_type="int8").transcribe(wav, word_timestamps=True)
words = [(w.start, w.end, re.sub(r"[^a-z0-9']", "", w.word.lower())) for s in segs for w in s.words]
json.dump(words, open(wav.rsplit(".", 1)[0] + ".words.json", "w"))
cues, i = {}, 0
for line in open(cmap):
    if ":" not in line or line.strip().startswith("#"): continue
    name, phrase = [x.strip() for x in line.split(":", 1)]
    want = [w if w in ("*", "@") else re.sub(r"[^a-z0-9']", "", w.lower()) for w in phrase.split()]
    land = want.index("@") if "@" in want else 0
    for j in range(i, len(words) - len(want) + 1):
        if all(x in ("*", "@") or x == w[2] for x, w in zip(want, words[j:j + len(want)])): cues[name] = round(words[j + land][0], 2); i = j + 1; break
    else: sys.exit(f"cue '{name}': could not find '{phrase}' after {words[i][0] if i < len(words) else 'the end'} s. Check the transcript in the .words.json file.")
cues["end"] = round(words[-1][1], 2)
open(out, "w").write("const C=" + json.dumps(cues) + ";\nconst HANDLE=(typeof BRAND!=='undefined'&&BRAND.handle)||'';\n")
print(f"{len(cues)} cues -> {out}")
