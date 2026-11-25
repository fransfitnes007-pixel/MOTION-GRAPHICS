#!/usr/bin/env python3
"""Assemble a new episode's code/demo.src.html and code/demo.html from three parts:
  head   = the previous episode's file up to its first scene section ("// ---------- ..."): CONFIG, WORDS, GROUPS, T,
           the renderer, lights, helpers. fill.py rewrites the title, the top comment, endLines, the outfit colours,
           WORDS, GROUPS and T in it.
  middle = your middle.js for this episode: the room, makePerson(), poses, props, drawDoc() sheets, CAM, state(t).
  tail   = the previous episode's file from the /*SHARED_UI*/ line to the end (notes, overlay, render loop).
demo.html = demo.src.html with /*SHARED_UI*/ replaced by code/_shared_ui.js (captions, pill, stamp, coin, endCard).

  python3 fill.py --base <previous episode>/code/demo.src.html --episode <new episode folder> \
                  --words words.json --spec spec.json --middle middle.js

spec.json:
  {"title": "Day in the life of a UGC creator, part N: <name>",
   "comment": "A %s s reel (1080x1920) in low-poly 3D ... Every frame is window.render(t).",   (%s = duration)
   "script": "the script, exactly as voiced",
   "endLines": ["First end-card line.", "YourBrand does the second."],
   "colors": "skin: 0xc8875a, hoodie: 0xffd23a, sweats: 0xd8323a, hair: 0x5a3a20,",
   "beats": {"part": 8, "found": 64, "foundG": 67, "no": 90, ...},        beat name -> word index (start time)
   "endWord": 110,                                                          last spoken word before the URL
   "groups": [[0, 7, 6, 1], [8, 9, -1, 1.3], ...]}                         caption groups: [first, last, line break after, size]
It prints any word that does not match the script, then T. Copy _shared_ui.js, three.min.js and brand-assets.js into
<episode>/code/ first (from the previous episode)."""
import argparse, json, os, re

ap = argparse.ArgumentParser()
for k in ('base', 'episode', 'words', 'spec', 'middle'):
    ap.add_argument('--' + k, required=True)
a = ap.parse_args()
S = json.load(open(a.spec)); W = json.load(open(a.words))
base = open(a.base, encoding='utf-8').read().split('\n')
first = next(i for i, l in enumerate(base) if l.startswith('// ---------- ') and i > 20)
head = '\n'.join(base[:first]); tail = '\n'.join(base[next(i for i, l in enumerate(base) if l.startswith('/*SHARED_UI*/')):])

norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
exp = [w for w in re.split(r'\s+', S['script']) if norm(w)]
bad = [(i, a_[0], b) for i, (a_, b) in enumerate(zip(W, exp)) if norm(a_[0]) != norm(b)]
print(len(W), 'words,', len(exp), 'in the script; mismatches:', bad[:12])

T = {k: W[i][1] for k, i in S['beats'].items()}
T['end'] = round(W[S['endWord']][2] + 0.5, 2); T['dur'] = round(T['end'] + 5, 2)
head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % S['title'], head)
head = re.sub(r'<!-- A .*?-->', '<!-- %s -->' % (S['comment'] % T['dur']), head, flags=re.S)
head = re.sub(r'endLines: \[.*?\],', 'endLines: %s,' % json.dumps(S['endLines']).replace('"', "'"), head)
head = re.sub(r'  skin: .*?\n', '  %s\n' % S['colors'], head)
head = re.sub(r'const WORDS = .*?\n', 'const WORDS = ' + json.dumps(W, separators=(',', ':')) + '\n', head)
head = re.sub(r'const GROUPS = .*?\n', 'const GROUPS = ' + json.dumps(S['groups']) + '\n', head)
head = re.sub(r'const T = \{.*?\}\n', 'const T = ' + json.dumps(T).replace('"', '') + '\n', head, flags=re.S)
src = head + '\n' + open(a.middle, encoding='utf-8').read() + '\n' + tail
code = os.path.join(a.episode, 'code')
open(os.path.join(code, 'demo.src.html'), 'w').write(src)
open(os.path.join(code, 'demo.html'), 'w').write(src.replace('/*SHARED_UI*/', open(os.path.join(code, '_shared_ui.js')).read()))
json.dump(T, open(os.path.join(a.episode, 'T.json'), 'w')); print(T)
