#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, sped 1.244x, take 2)
plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.6
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(29)
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
def meow(d=0.42, f=640):                                                            # a short synthetic meow
    n = int(d * SR); u = np.linspace(0, 1, n); fr = f * (1 + 0.45 * np.sin(u * np.pi) - 0.2 * u); ph_ = 2 * np.pi * np.cumsum(fr) / SR
    return (np.sin(ph_) + 0.5 * np.sin(2 * ph_) + 0.25 * np.sin(3 * ph_)) * np.sin(u * np.pi) ** 0.7
def smash(d=0.5):                                                                  # a mug meeting a floor
    n = int(d * SR); t = np.arange(n) / SR; return (rng.standard_normal(n) * np.exp(-t * 14) + 0.5 * sum(np.sin(2 * np.pi * f * t) * np.exp(-t * (9 + i * 3)) for i, f in enumerate([1830, 2710, 3950, 5200])))
T = dict(part=2.26, apply=3.5, q=5.08, qHit=6.26, two=7.9, twoHit=8.02, bigger=8.96, biggerHit=9.58, vids=10.36, vidsHit=10.96, nobody=11.86, nobodyHit=12.76, forms=13.72, kitHit=14.7, countHit=15.88,
         cat=16.98, catHit=17.6, meHit=18.3, buy=18.88, buyHit=19.36, found=20.38, foundG=20.95, lb=21.9, lbHit=22.96, viewsHit=24.24, notFHit=25.1, hook=26.04, hookHit=26.28, bio=27.14, bioHit=27.98,
         n=[29.04, 30.2], nob=31.1, cat2=32.04, stillHit=33.04, notOn=33.92, pushHit=34.44, crash=35.06, end=35.6)
add(T['part'], thud(120, 0.2), 0.14)
add(T['apply'], whoosh(0.35), 0.3)
for i in range(2): add(T['apply'] + 0.25 + i * 0.2, tone(1318.5, 0.1, 3), 0.045)
add(T['q'], thud(130, 0.3), 0.22)
for i in range(14): add(T['qHit'] + i * 0.062, click(), 0.12)
add(T['two'], whoosh(0.25), 0.2); add(T['twoHit'], pop(620), 0.08)
add(T['bigger'], whoosh(0.3), 0.3); add(T['bigger'] + 0.1, pop(480), 0.07); add(T['biggerHit'], thud(150, 0.45), 0.34); add(T['biggerHit'] + 0.02, buzz(0.45), 0.1)
add(T['vids'], whoosh(0.35), 0.3)
for i in range(4): add(T['vidsHit'] - 0.1 + i * 0.08, ding(1046.5 * 2 ** (i * 2 / 12), 0.35), 0.05)
add(T['nobody'], whoosh(0.3), 0.25); add(T['nobodyHit'], slide(520, 260, 0.35), 0.08); add(T['nobodyHit'], thud(130, 0.3), 0.22)
add(T['forms'], whoosh(0.35), 0.3)
for i in range(3): add(T['forms'] + i * 0.14, whoosh(0.14), 0.16); add(T['kitHit'] + i * 0.06, click(), 0.3); add(T['countHit'] + i * 0.06, click(), 0.3)
add(T['kitHit'], buzz(0.3), 0.08); add(T['countHit'], buzz(0.35), 0.1); add(T['countHit'], thud(140, 0.3), 0.24)
add(T['cat'], whoosh(0.3), 0.25); add(T['cat'] + 0.12, meow(), 0.11); add(T['catHit'], ding(1568, 0.5), 0.06); add(T['meHit'], slide(520, 240, 0.35), 0.08); add(T['meHit'], thud(130, 0.3), 0.24)
add(T['buy'], whoosh(0.35), 0.3)
for k in range(4): add(T['buy'] + 0.15 + k * 0.09, tone(1400 + 300 * (k % 2), 0.07, 2), 0.035)                                    # a tacky jingle
add(T['buyHit'], tone(110, 0.6, 3, (1, 0.5, 0.3)), 0.1)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['lb'], whoosh(0.4), 0.3)
for i in range(5): add(T['lbHit'] - 0.1 + i * 0.09, whoosh(0.12), 0.12); add(T['lbHit'] + i * 0.09, ding(1046.5 * 2 ** (i * 2 / 12), 0.35), 0.055)
add(T['viewsHit'], ding(1568, 0.6), 0.08); add(T['viewsHit'], thud(130, 0.25), 0.2)
add(T['notFHit'] - 0.05, whoosh(0.3), 0.3); add(T['notFHit'] + 0.05, thud(150, 0.35), 0.3)
add(T['hook'], whoosh(0.3), 0.25); add(T['hookHit'], ding(1318.5, 0.5), 0.07); add(T['hookHit'], thud(130, 0.2), 0.16)
for i in range(3): add(T['bio'] + 0.1 + i * 0.25, whoosh(0.2), 0.16)
add(T['bioHit'], slide(500, 250, 0.3), 0.07); add(T['bioHit'], thud(130, 0.25), 0.2)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['cat2'], whoosh(0.3), 0.25); add(T['stillHit'], ding(1568, 0.5), 0.05)
add(T['notOn'] + 0.15, slide(300, 420, 0.3), 0.04)                                                                               # the paw comes out
n = int(0.25 * SR); add(T['pushHit'] - 0.1, np.convolve(rng.standard_normal(n), np.ones(20) / 20, 'same') * np.linspace(0.3, 1, n), 0.25)   # ceramic sliding on wood
add(T['crash'], smash(), 0.22); add(T['crash'], thud(160, 0.3), 0.3); add(T['crash'] + 0.25, meow(0.3, 720), 0.07)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
