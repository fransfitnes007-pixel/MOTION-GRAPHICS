#!/usr/bin/env python3
"""Word times for a voice take, guided by the exact script, tidied for captions.

Usage: word_times.py <take.wav|mp3> <script.txt> <out words.json> [--drop-last N] [--model small.en]

- Runs faster-whisper with word timestamps and the script as initial_prompt (without it, whisper mishears names).
- Writes [[word, start, end], ...]: punctuation stripped, no zero-length words, no overlaps.
- --drop-last N drops trailing words the end card shows instead of captioning (a site name, a handle).
- Prints the words that differ from the script; fix the take or the script until it prints "mismatch: []".
"""
import argparse, json, re


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('audio'); ap.add_argument('script'); ap.add_argument('out')
    ap.add_argument('--drop-last', type=int, default=0)
    ap.add_argument('--model', default='small.en')
    a = ap.parse_args()
    from faster_whisper import WhisperModel
    script = open(a.script).read().strip()
    model = WhisperModel(a.model, device='cpu', compute_type='int8')
    segs, _ = model.transcribe(a.audio, word_timestamps=True, beam_size=5, initial_prompt=script)
    raw = [w for s in segs for w in (s.words or [])]
    if a.drop_last:
        raw = raw[:-a.drop_last]
    out, prev = [], 0.0
    for w in raw:
        word = w.word.strip().strip('.,!?;:"')
        if not word:
            continue
        s = max(w.start, prev); e = max(w.end, s + 0.06)
        out.append([word, round(s, 2), round(e, 2)]); prev = e
    json.dump(out, open(a.out, 'w'))
    norm = lambda x: re.sub(r'[^a-z0-9]', '', x.lower())
    exp = [x for x in script.split() if norm(x)]
    if a.drop_last:
        exp = exp[:-a.drop_last]
    print(len(out), 'words;', 'mismatch:', [(i, w[0], e) for i, (w, e) in enumerate(zip(out, exp)) if norm(w[0]) != norm(e)])


if __name__ == '__main__':
    main()
