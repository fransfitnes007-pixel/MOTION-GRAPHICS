#!/usr/bin/env python3
"""Check a voice script against an account's claim rules before any voice is made.

Usage: claim_check.py <script.txt> [--brand NAME] [--chars MIN MAX] [--hold] [--ban REGEX ...] [--by-line]

Checks, in order:
  1. Length in characters (the voice's sweet spot, from the FORMAT LOCK; e.g. 490 550 for a calm voice).
  2. --hold: no product words before the last sentence (organic accounts that hold the product back). The default
     pattern catches "app(s)", "build/built", "made it/this/my/our/us", "download", "link in bio" and the brand name.
  3. --ban: patterns that may never appear anywhere (prices, "free", money promises, results). Some are on by default.
Sentences are split on . ! ? unless --by-line is given (then each line of the file is one unit).
Exit code 0 = clean, 1 = a rule failed (each hit is printed with its sentence).
"""
import argparse, re, sys

DEFAULT_BANS = [
    r'[$€£]\s?\d',                      # a price or an amount of money
    r'\bfree\b',                        # "free" needs the owner's OK per account
    r'\b(guarantee[ds]?|guaranteed)\b',
    r'\b(make|earn|made)\s+(\$|money|\d+k|thousands|a living)\b',  # money promises
    r'\bdramati[sz]ation\b',            # no disclaimer lines
]
HOLD = r"\bapps?\b|\bbuil[dt]\b|\bmade (it|this|my|our|us)\b|\bdownload\b|\blink in (my )?bio\b"


def units(text, by_line):
    if by_line:
        return [l.strip() for l in text.splitlines() if l.strip()]
    return [u.strip() for u in re.split(r'(?<=[.!?])\s+', text.strip()) if u.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('script')
    ap.add_argument('--brand', default='')
    ap.add_argument('--chars', nargs=2, type=int)
    ap.add_argument('--hold', action='store_true')
    ap.add_argument('--ban', action='append', default=[])
    ap.add_argument('--no-default-bans', action='store_true')
    ap.add_argument('--by-line', action='store_true')
    a = ap.parse_args()

    text = open(a.script, encoding='utf-8').read()
    u = units(text, a.by_line)
    bad = 0
    n = len(text.strip())
    if a.chars:
        lo, hi = a.chars
        ok = lo <= n <= hi
        print(f'chars: {n} (target {lo}-{hi})' + ('' if ok else '  <- outside the target'))
        bad += not ok
    else:
        print(f'chars: {n}')

    if a.hold:
        pat = HOLD
        if a.brand:
            b = re.escape(a.brand).replace(r'\ ', r'\s?')
            pat += '|' + b
        for i, s in enumerate(u[:-1]):
            for m in re.finditer(pat, s, re.I):
                print(f'HOLD  sentence {i + 1}: "{m.group(0)}" before the last line -> {s}')
                bad += 1

    bans = ([] if a.no_default_bans else DEFAULT_BANS) + a.ban
    for i, s in enumerate(u):
        for b in bans:
            for m in re.finditer(b, s, re.I):
                print(f'BAN   sentence {i + 1}: "{m.group(0)}" ({b}) -> {s}')
                bad += 1

    print('clean' if not bad else f'{bad} problem(s)')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
