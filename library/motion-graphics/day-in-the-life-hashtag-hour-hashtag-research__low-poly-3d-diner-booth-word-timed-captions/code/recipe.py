#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, sped 1.1x, take 1) plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 38.95
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(31)
def add(at, sig, g=1.0):
    i = int(at * SR); sig = sig[:len(mix) - i]; mix[i:i + len(sig)] += sig * g
def tone(f, d, dec=5.0, harm=(1.0,)):
    n = int(d * SR); t = np.arange(n) / SR; return sum(a * np.sin(2 * np.pi * f * (k + 1) * t) for k, a in enumerate(harm)) * np.exp(-np.linspace(0, dec, n))
def thud(f0=140, d=0.3):
    n = int(d * SR); return (np.sin(2 * np.pi * np.cumsum(np.geomspace(f0, 45, n)) / SR) + 0.35 * rng.standard_normal(n)) * np.exp(-np.linspace(0, 7, n))
def whoosh(d=0.5):
    n = int(d * SR); return np.convolve(rng.standard_normal(n) * np.sin(np.linspace(0, np.pi, n)) ** 2, np.ones(48) / 48, 'same')
def ding(f=1318.5, d=0.9): return tone(f, d, 6, (1, 0.35, 0.12))
def buzz(d=0.35):
    n = int(d * SR); t = np.arange(n) / SR; return np.sign(np.sin(2 * np.pi * 92 * t)) * np.exp(-np.linspace(0, 3, n)) * 0.6
def click(): n = int(0.03 * SR); return rng.standard_normal(n) * np.exp(-np.linspace(0, 8, n))
def slide(f0, f1, d=0.35):
    n = int(d * SR); return np.sin(2 * np.pi * np.cumsum(np.geomspace(f0, f1, n)) / SR) * np.sin(np.linspace(0, np.pi, n))
def pop(f=520): return slide(f, f * 1.9, 0.09)                                    # a message bubble
def hum(d, f=120):                                                                 # the diner's fridge and neon, low under the first half
    n = int(d * SR); t = np.arange(n) / SR; return (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * f * 2 * t) + 0.4 * np.convolve(rng.standard_normal(n), np.ones(200) / 200, 'same')) * np.minimum(1, np.linspace(0, 8, n)) * np.minimum(1, np.linspace(8, 0, n))
def crackle(d=0.5):                                                                # frost forming
    n = int(d * SR); s = np.zeros(n)
    for _ in range(26): i = rng.integers(0, n - 200); s[i:i + 200] += rng.standard_normal(200) * np.exp(-np.linspace(0, 9, 200)) * rng.uniform(0.3, 1)
    return s
def clink(f=3100): return tone(f, 0.25, 9, (1, 0.5, 0.2))                           # a fork on a plate
T = dict(part=2.32, vid=3.54, vidHit=4.18, tags=5.28, tagsHit=6.3, g=[(7.24, 8.14), (8.84, 9.26), (9.86, 11.04)], fyp=11.82, fypHit=12.22, banHit=15.34, cold=16.32, coldHit=17.1, found=18.08, foundG=18.75,
         niche=19.82, nicheHit=20.34, fifteen=20.94, fifteenHit=21.38, buckets=[22.94, 23.3, 23.98], reason=24.74, reasonHit=25.3, camp=26.05, campHit=27.16, copyHit=28.06, copied=28.36,
         n=[29.38, 30.41], nob=31.34, ate=32.22, ateHit=33.0, end=33.95)
add(0.0, hum(T['found'] + 0.6), 0.035)
add(T['part'], thud(120, 0.2), 0.14)
add(T['vid'], whoosh(0.3), 0.25); add(T['vidHit'], ding(1318.5, 0.5), 0.07); add(T['vidHit'], thud(130, 0.2), 0.16)
add(T['tags'], whoosh(0.35), 0.3)
for i in range(22): add(T['tags'] + 0.05 + (i / 22) * (T['tagsHit'] + 0.4 - T['tags']), click(), 0.1 + (i % 3) * 0.02)
add(T['tagsHit'], thud(150, 0.45), 0.32); add(T['tagsHit'] + 0.02, buzz(0.4), 0.09)
for i, (a, h) in enumerate(T['g']): add(a, whoosh(0.3), 0.28); add(a + 0.12, pop(520 + i * 60), 0.07); add(h, thud(140 + i * 8, 0.3), 0.22 + i * 0.05); add(h, tone([880, 660, 220][i], 0.3, 3, (1, 0.4)), 0.06)
add(T['g'][2][1] + 0.02, buzz(0.45), 0.1)
add(T['fyp'], whoosh(0.3), 0.3)
for i in range(4): add(T['fypHit'] - 0.05 + i * 0.17, pop(560 + i * 70), 0.08)
add(T['banHit'], thud(150, 0.45), 0.34); add(T['banHit'] + 0.02, buzz(0.5), 0.11)
add(T['cold'], whoosh(0.3), 0.25); add(T['coldHit'] - 0.1, crackle(0.55), 0.12); add(T['coldHit'], tone(2637, 0.6, 5), 0.035); add(T['coldHit'], slide(520, 240, 0.35), 0.06)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
for i in range(11): add(T['niche'] + 0.12 + i * 0.065, click(), 0.14)
add(T['nicheHit'] + 0.42, click(), 0.35); add(T['nicheHit'] + 0.44, thud(110, 0.15), 0.16)
add(T['fifteen'], whoosh(0.4), 0.3)
for i in range(15): add(T['fifteenHit'] - 0.15 + i * 0.045, pop(500 + i * 28), 0.05)
add(T['fifteenHit'] + 0.6, ding(1318.5, 0.5), 0.06)
for i, at in enumerate(T['buckets']): add(at, thud(130, 0.22), 0.2); add(at, ding([1046.5, 1318.5, 1568][i], 0.5), 0.075)
add(T['reason'], whoosh(0.2), 0.18); add(T['reasonHit'], ding(1760, 0.5), 0.06)
add(T['camp'], whoosh(0.3), 0.25); add(T['camp'] + 0.3, thud(140, 0.2), 0.16); add(T['campHit'], ding(2093, 0.6), 0.07)
add(T['copyHit'], click(), 0.4); add(T['copyHit'] + 0.02, thud(110, 0.18), 0.2); add(T['copied'], ding(1318.5, 0.4), 0.07); add(T['copied'] + 0.1, ding(1760, 0.5), 0.07)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['ate'], whoosh(0.3), 0.25); add(T['ate'] + 0.3, clink(), 0.05); add(T['ateHit'], clink(2600), 0.06); add(T['ateHit'], ding(1568, 0.6), 0.06); add(T['ateHit'], thud(130, 0.25), 0.2)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
