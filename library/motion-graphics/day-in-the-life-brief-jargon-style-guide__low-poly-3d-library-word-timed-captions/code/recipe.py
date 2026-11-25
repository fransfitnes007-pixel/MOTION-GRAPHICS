#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, sped 1.29x, take 1)
plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.5
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(37)
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
def page(d=0.22):                                                                # a page turning
    n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(10) / 10, 'same') * np.sin(np.linspace(0, np.pi, n)) ** 0.6 * np.linspace(0.4, 1, n)
def boing(d=0.5, f=180):                                                           # a bobblehead
    n = int(d * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * f * (1 + 0.5 * np.sin(2 * np.pi * 11 * t)) * t) * np.exp(-t * 6)
T = dict(part=2.2, brief=3.58, briefHit=4.22, says=5.26, terms=[6.4, 7.74, 8.74, 9.56], nod=10.56, none=11.46, noneHit=11.92, look=13.0, sites=13.96, sitesHit=14.86, ask=15.78, askHit=16.24, said=16.94, knowHit=17.5, ugcHit=18.12,
         bread=19.32, brollHit=19.7, breadHit=20.64, found=21.64, foundG=22.25, guide=23.22, guideHit=23.62, tenHit=24.7, what=25.56, whatHit=26.0, whenHit=26.88, th2Hit=28.04, best=28.8, bestHit=29.3, me=30.24, meHit=30.4,
         n=[31.32, 32.13], nob=32.76, still=33.72, stillHit=34.92, end=35.5)
add(T['part'], thud(120, 0.2), 0.14)
add(T['brief'], whoosh(0.3), 0.25); add(T['briefHit'], ding(1318.5, 0.5), 0.07); add(T['briefHit'] + 0.1, ding(1760, 0.5), 0.06)
add(T['says'], whoosh(0.35), 0.3); add(T['says'] + 0.2, page(), 0.2)
for i, at in enumerate(T['terms']): add(at, thud(140, 0.25), 0.22 + i * 0.03); add(at, tone([660, 587, 523, 440][i], 0.25, 3, (1, 0.4)), 0.06); add(at + 0.26, slide(420, 640, 0.16), 0.05)                  # each term lands, then a small "?"
for i in range(5): add(T['nod'] + 0.12 + i * 0.16, tone(300 + (i % 2) * 60, 0.07, 3), 0.045)                                       # nod, nod, nod
add(T['none'], whoosh(0.25), 0.2); add(T['noneHit'], slide(520, 240, 0.4), 0.08); add(T['noneHit'], thud(130, 0.35), 0.26)
add(T['look'], whoosh(0.3), 0.28)
for i in range(12): add(T['look'] + 0.03 + i * 0.045, click(), 0.12)
for i in range(3): add(T['sites'] + i * 0.3, whoosh(0.16), 0.16); add(T['sites'] + 0.12 + i * 0.3, pop(480 + i * 90), 0.07)
add(T['sitesHit'], buzz(0.4), 0.09); add(T['sitesHit'], thud(140, 0.3), 0.24)
add(T['ask'], whoosh(0.3), 0.28); add(T['askHit'] - 0.25, pop(620), 0.07); add(T['askHit'], pop(660), 0.08)
for i in range(3): add(T['said'] + 0.1 + i * 0.13, click(), 0.07)
add(T['knowHit'], pop(460), 0.09); add(T['ugcHit'], pop(420), 0.09); add(T['ugcHit'] + 0.05, slide(500, 250, 0.4), 0.07); add(T['ugcHit'], thud(130, 0.3), 0.22)
add(T['bread'], whoosh(0.3), 0.25); add(T['brollHit'], np.convolve(rng.standard_normal(int(0.35 * SR)), np.ones(8) / 8, 'same') * np.linspace(1, 0.3, int(0.35 * SR)), 0.1); add(T['breadHit'], thud(150, 0.4), 0.3); add(T['breadHit'] + 0.05, tone(196, 0.5, 3, (1, 0.5)), 0.07)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['guide'], whoosh(0.4), 0.3)
for i in range(10): add(T['guideHit'] + i * 0.085, pop(480 + i * 34), 0.055)
add(T['tenHit'], ding(1568, 0.6), 0.08); add(T['tenHit'], thud(130, 0.22), 0.18)
add(T['what'], whoosh(0.3), 0.25); add(T['what'] + 0.15, page(), 0.2); add(T['whatHit'], ding(1046.5, 0.5), 0.06); add(T['whenHit'], ding(1318.5, 0.5), 0.06)
add(T['th2Hit'], thud(130, 0.22), 0.18); add(T['th2Hit'], ding(1568, 0.5), 0.06)
add(T['best'], whoosh(0.3), 0.2); add(T['bestHit'], ding(2093, 0.7), 0.08); add(T['bestHit'], thud(130, 0.25), 0.2)
add(T['me'], whoosh(0.2), 0.2); add(T['meHit'], ding(1318.5, 0.4), 0.07); add(T['meHit'] + 0.1, ding(1760, 0.5), 0.07)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['n'][1] - 0.25, boing(0.4), 0.06)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['still'], whoosh(0.3), 0.25); add(T['stillHit'], thud(150, 0.4), 0.3); add(T['stillHit'] + 0.05, tone(196, 0.6, 3, (1, 0.5)), 0.07)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
