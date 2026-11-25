#!/usr/bin/env python3
"""Pin a scene page to a new voice take: write the words, caption groups and beat times into a copy of the last good build.

Usage: fill_beats.py <beats.json> <words.json> <template demo.src.html> <out dir> [--scene scene.js] [--shared shared_ui.js]

beats.json (one per video, written by the agent that wrote the script):
{
  "title": "Account name, video 3: the topic",
  "beats": {"hook": 0, "pain": 11, "turn": 46, "feature": 50, "callback": 89},   # beat name -> word index (0-based)
  "end_pad": 0.5,          # seconds after the last word before the end card
  "end_card": 5,           # end card length in seconds; T.dur = T.end + end_card
  "groups": [[0, 7, 6, 1], [8, 10, -1, 1.3]],   # caption rows: [firstWord, lastWord, lineBreakAfterWord or -1, size]
  "end_lines": ["Line one.", "Line two."],       # optional, written into CONFIG.endLines
  "replace": {"  skin: .*?\\n": "  skin: 0xe8b896, top: 0xe07a2a,\\n"}   # optional extra regex -> text edits
}

The template must contain the lines it rewrites (each on one line):
  <title>...</title>   const WORDS = ...   const GROUPS = ...   const T = ...   endLines: [...],
Optional markers: /*SCENE_START*/ ... /*SCENE_END*/ is replaced by --scene; /*SHARED_UI*/ is inlined from --shared
in demo.html (demo.src.html keeps the marker so the next video can be filled from it).
Writes <out>/demo.src.html, <out>/demo.html and <out>/T.json. Every frame of the page must stay a function of time.
"""
import argparse, json, os, re


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('beats'); ap.add_argument('words'); ap.add_argument('template'); ap.add_argument('out')
    ap.add_argument('--scene'); ap.add_argument('--shared')
    a = ap.parse_args()
    B = json.load(open(a.beats)); W = json.load(open(a.words)); src = open(a.template).read()
    T = {k: W[i][1] for k, i in B['beats'].items()}
    T['end'] = round(W[-1][2] + B.get('end_pad', 0.5), 2)
    T['dur'] = round(T['end'] + B.get('end_card', 5), 2)
    G = B.get('groups') or [[i, i, i, 1] for i in range(len(W))]
    for g in G:
        assert 0 <= g[0] <= g[1] < len(W), f'group out of range: {g}'

    def sub(pat, rep, s, required=True):
        n = re.subn(pat, lambda _: rep, s, count=1)
        if required and n[1] == 0:
            raise SystemExit(f'template has no line matching {pat!r}')
        return n[0]
    src = sub(r'<title>.*?</title>', f'<title>{B.get("title", "")}</title>', src, False)
    src = sub(r'const WORDS = .*?\n', 'const WORDS = ' + json.dumps(W, separators=(',', ':')) + '\n', src)
    src = sub(r'const GROUPS = .*?\n', 'const GROUPS = ' + json.dumps(G) + '\n', src)
    src = sub(r'const T = .*?\n', 'const T = ' + json.dumps(T).replace('"', '') + '\n', src)
    if B.get('end_lines'):
        src = sub(r'endLines: \[.*?\],', 'endLines: ' + json.dumps(B['end_lines']) + ',', src)
    for pat, rep in (B.get('replace') or {}).items():
        src = sub(pat, rep, src)
    if a.scene:
        scene = open(a.scene).read()
        src = sub(r'/\*SCENE_START\*/.*?/\*SCENE_END\*/', '/*SCENE_START*/\n' + scene + '\n/*SCENE_END*/', src)
    os.makedirs(a.out, exist_ok=True)
    open(os.path.join(a.out, 'demo.src.html'), 'w').write(src)
    html = src.replace('/*SHARED_UI*/', open(a.shared).read()) if a.shared else src
    open(os.path.join(a.out, 'demo.html'), 'w').write(html)
    json.dump(T, open(os.path.join(a.out, 'T.json'), 'w'))
    print(T)


if __name__ == '__main__':
    main()
