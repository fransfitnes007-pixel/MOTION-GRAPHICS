#!/usr/bin/env python3
"""Finds library skills by what you'd call them. Used by the motion-library skill.
  find_skill.py <words>              best matches, ranked
  find_skill.py --alias <word> <slug>   save your own word for a skill"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'library'))
ALIASES = os.path.join(ROOT, 'my-aliases.json')   # your own words; git-ignored


def load_mine():
    return json.load(open(ALIASES)) if os.path.isfile(ALIASES) else {}


def words(s):
    return re.findall(r'[a-z0-9]+', s.lower())


def stem(w):
    return re.sub(r'(ing|ed|es|s)$', '', w) if len(w) > 4 else w


def score(item, q, mine):
    phrase, qw = ' '.join(words(q)), [stem(w) for w in words(q)]
    if q.strip().lower() in mine.get(item['slug'], []):
        return 1000
    fields = [(item.get('aliases', []), 40), ([item['visual_name']], 25), ([item['slug'].replace('__', ' ').replace('-', ' ')], 15),
              (item.get('tags', []), 10), ([item['code_name']], 8), (item.get('tech', []), 4), ([item['summary']], 3)]
    total, hit = 0, set()
    for values, weight in fields:
        for v in values:
            vw = words(v)
            joined = ' '.join(vw)
            if joined == phrase:
                total += weight * 3
            elif phrase and f' {phrase} ' in f' {joined} ':
                total += weight * 2
            vs = {stem(w) for w in vw}
            for w in qw:
                if w in vs:
                    total += weight
                    hit.add(w)
    return total + (20 * len(hit) if len(hit) == len(qw) else 0) if hit or total else 0


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit('usage: find_skill.py <words> | --alias <word> <slug>')
    catalog = json.load(open(os.path.join(ROOT, 'catalog.json')))['skills']
    if args[0] == '--alias':
        word, slug = ' '.join(args[1:-1]).lower(), args[-1]
        if not any(i['slug'] == slug for i in catalog):
            sys.exit('no skill called ' + slug)
        mine = load_mine()
        for k in mine:
            mine[k] = [w for w in mine[k] if w != word]
        mine.setdefault(slug, []).append(word)
        json.dump({k: v for k, v in mine.items() if v}, open(ALIASES, 'w'), indent=1, sort_keys=True)
        print(f'"{word}" now means {slug}')
        return
    q, mine = ' '.join(args), load_mine()
    ranked = sorted(((score(i, q, mine), i) for i in catalog), key=lambda x: -x[0])
    ranked = [(s, i) for s, i in ranked if s > 0][:8]
    if not ranked:
        print('no match')
        return
    for s, i in ranked:
        print(json.dumps({'score': s, 'name': i['visual_name'], 'slug': i['slug'], 'folder': os.path.join(ROOT, i['path']), 'kind': i.get('demo_kind', ''), 'summary': i['summary']}))


if __name__ == '__main__':
    main()
