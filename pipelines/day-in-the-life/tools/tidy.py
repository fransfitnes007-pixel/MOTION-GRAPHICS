#!/usr/bin/env python3
"""Clean faster-whisper word times so captions can sit on them.
  python3 tidy.py take.words.json words.json [--drop-last 3]
Joins split tokens ("follow", "-up"), drops the spoken URL at the end (the end card shows it; whisper usually gives it as
three tokens, e.g. "YourBrand dot com"), strips punctuation, gives every word at least 0.08 s, and makes sure no word
starts before the previous one ends. Prints the words with their index: use those indexes for beats and caption groups."""
import json, re, sys
src, dst = sys.argv[1], sys.argv[2]
drop = int(sys.argv[sys.argv.index('--drop-last') + 1]) if '--drop-last' in sys.argv else 3
R = json.load(open(src)); W = []
for x in R:
    w = x['w']
    if w.startswith('-') and W: W[-1][0] += w; W[-1][2] = x['e']; continue
    W.append([w, x['s'], x['e']])
if drop: W = W[:-drop]
for a in W: a[0] = re.sub(r"[^A-Za-z0-9'\-]", '', a[0])
for i in range(len(W)):
    if W[i][2] - W[i][1] < 0.08: W[i][2] = round(W[i][1] + 0.1, 2)
    if i and W[i][1] < W[i-1][2]: W[i][1] = W[i-1][2]
    if W[i][2] <= W[i][1]: W[i][2] = round(W[i][1] + 0.08, 2)
json.dump(W, open(dst, 'w')); print(len(W), W[-1]); print(' '.join(f'{i}:{a[0]}' for i, a in enumerate(W)))
