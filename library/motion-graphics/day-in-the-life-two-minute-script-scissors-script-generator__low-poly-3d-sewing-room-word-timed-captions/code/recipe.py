#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, sped 1.1x, take 1)
plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.25
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(53)
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
def snip():                                                                      # scissors: two blades meeting
    n = int(0.09 * SR); a = rng.standard_normal(n) * np.exp(-np.linspace(0, 10, n)); b = tone(3400, 0.09, 8) ; return np.concatenate([a * 0.7 + b * 0.5, np.zeros(int(0.03 * SR)), a[::-1] * 0.3 + tone(2600, 0.09, 6) * 0.6])
def rustle(d=0.3):                                                                 # paper falling
    n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(12) / 12, 'same') * np.sin(np.linspace(0, np.pi, n)) ** 0.7
def tick(f=1500): return tone(f, 0.035, 3) * 0.8
T = dict(part=2.54, brief=4.14, briefHit=4.8, wrote=6.08, read=7.3, twoHit=8.74, cut1=9.56, cut1Hit=10.02, ninetyHit=11.42, cut2Hit=12.46, cut3Hit=13.56, thirty=14.64, thirtyHit=14.9, sense=15.9, senseHit=16.4, never=17.58, neverHit=18.64,
         found=19.58, foundG=20.3, pick=21.5, pickHit=21.94, hook=23.16, blocks=[23.72, 24.4, 25.14, 26.18], fit=27.2, fitHit=27.88, alt=28.6, altHit=28.74, n=[30.8, 31.84], nob=32.6, cb=33.52, cbHit=34.36, end=35.25)
add(T['part'], thud(120, 0.2), 0.14)
add(T['brief'], whoosh(0.3), 0.25); add(T['briefHit'], thud(130, 0.22), 0.18); add(T['briefHit'], tone(880, 0.14, 3), 0.06)
add(T['wrote'], whoosh(0.35), 0.3)
for i in range(18): add(T['wrote'] + 0.05 + i * 0.045, click(), 0.09)
add(T['read'], whoosh(0.3), 0.28)
for i in range(int((T['twoHit'] - T['read'] - 0.15) / 0.055)): add(T['read'] + 0.15 + i * 0.055, tick(1400 + i * 14), 0.035 + i * 0.0012)                    # the stopwatch races
add(T['twoHit'], thud(150, 0.45), 0.34); add(T['twoHit'] + 0.02, buzz(0.45), 0.11)
add(T['cut1'], whoosh(0.35), 0.3)
for at in [T['cut1Hit'], T['cut2Hit'], T['cut3Hit']]: add(at - 0.28, snip(), 0.22); add(at - 0.05, snip(), 0.26); add(at + 0.1, rustle(0.35), 0.2)
add(T['ninetyHit'], pop(520), 0.08); add(T['ninetyHit'], thud(130, 0.22), 0.18)
add(T['thirty'], whoosh(0.3), 0.25); add(T['thirtyHit'], ding(1318.5, 0.5), 0.07); add(T['thirtyHit'] + 0.1, ding(1760, 0.5), 0.07); add(T['thirtyHit'] + 0.25, snip(), 0.14)
add(T['sense'], whoosh(0.3), 0.25); add(T['senseHit'], slide(520, 240, 0.4), 0.08); add(T['senseHit'], thud(140, 0.35), 0.28)
add(T['never'], whoosh(0.25), 0.2); add(T['neverHit'], thud(150, 0.45), 0.34); add(T['neverHit'] + 0.02, buzz(0.4), 0.1)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['pickHit'], click(), 0.4); add(T['pickHit'] + 0.03, ding(1568, 0.5), 0.07); add(T['pickHit'] + 0.5, click(), 0.35); add(T['pickHit'] + 0.52, thud(110, 0.15), 0.16)
add(T['hook'], whoosh(0.4), 0.3)
for i, at in enumerate(T['blocks']): add(at - 0.08, whoosh(0.14), 0.14); add(at, ding([1046.5, 1174.7, 1318.5, 1568][i], 0.45), 0.07); add(at, thud(130, 0.18), 0.12)
add(T['fit'], slide(400, 900, T['fitHit'] - T['fit']), 0.04); add(T['fitHit'], ding(2093, 0.7), 0.08); add(T['fitHit'], thud(130, 0.25), 0.2)
for i in range(3): add(T['altHit'] + i * 0.16, pop(560 + i * 80), 0.07)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['cb'], whoosh(0.35), 0.3)
for i in range(int((T['end'] - T['cb'] - 0.2) / 0.1)): add(T['cb'] + 0.2 + i * 0.1, tick(1500), 0.04)
add(T['cbHit'], thud(150, 0.4), 0.3); add(T['cbHit'] + 0.05, slide(500, 240, 0.45), 0.08)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
