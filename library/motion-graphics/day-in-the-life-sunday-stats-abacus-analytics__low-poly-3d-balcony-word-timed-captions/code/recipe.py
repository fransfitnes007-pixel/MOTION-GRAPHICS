#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4,
take 2, sped 1.12x) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet
city balcony: soft birdsong and far-off traffic. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.7
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(133)
def add(at, sig, g=1.0):
    i = int(at * SR); sig = sig[:len(mix) - i]; mix[i:i + len(sig)] += sig * g
def tone(f, d, dec=5.0, harm=(1.0,)):
    n = int(d * SR); t = np.arange(n) / SR; return sum(a * np.sin(2 * np.pi * f * (k + 1) * t) for k, a in enumerate(harm)) * np.exp(-np.linspace(0, dec, n))
def thud(f0=140, d=0.3):
    n = int(d * SR); return (np.sin(2 * np.pi * np.cumsum(np.geomspace(f0, 45, n)) / SR) + 0.35 * rng.standard_normal(n)) * np.exp(-np.linspace(0, 7, n))
def whoosh(d=0.5):
    n = int(d * SR); return np.convolve(rng.standard_normal(n) * np.sin(np.linspace(0, np.pi, n)) ** 2, np.ones(48) / 48, 'same')
def ding(f=1318.5, d=0.9): return tone(f, d, 6, (1, 0.35, 0.12))
def buzz(d=0.35, f=92):
    n = int(d * SR); t = np.arange(n) / SR; return np.sign(np.sin(2 * np.pi * f * t)) * np.exp(-np.linspace(0, 3, n)) * 0.6
def click(): n = int(0.03 * SR); return rng.standard_normal(n) * np.exp(-np.linspace(0, 8, n))
def slide(f0, f1, d=0.35):
    n = int(d * SR); return np.sin(2 * np.pi * np.cumsum(np.geomspace(f0, f1, n)) / SR) * np.sin(np.linspace(0, np.pi, n))
def pop(f=520): return slide(f, f * 1.9, 0.09)
def stampS(): return np.concatenate([thud(170, 0.12) * 0.8, click()[:800] * 0.6])
def squelch(d=0.35):
    n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(90) / 90, 'same') * np.exp(-np.linspace(0, 5, n)) * 6 + thud(90, d) * 0.5
def hum(d, f=58):
    n = int(d * SR); t = np.arange(n) / SR; s = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t) + 0.08 * np.convolve(rng.standard_normal(n), np.ones(30) / 30, 'same')
    e = np.ones(n); r = min(n // 4, int(0.3 * SR)); e[:r] = np.linspace(0, 1, r); e[-r:] = np.linspace(1, 0, r); return s * e
def vib(d=0.6):
    n = int(d * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * 150 * t) * (np.sin(2 * np.pi * 9 * t) > 0) * np.exp(-np.linspace(0, 1.5, n))
def chirp(): n = int(0.12 * SR); return np.sin(2 * np.pi * np.cumsum(np.geomspace(2600, 3800, n)) / SR) * np.sin(np.linspace(0, np.pi, n))
def bead(): return tone(1800, 0.08, 9, (1, 0.3)) + np.pad(click()[:400], (0, int(0.08 * SR) - 400)) * 0.3
def shutter(): return np.concatenate([click()[:600] * 1.2, np.zeros(1200), click()[:500] * 0.8])
def pencil(d=0.5): n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(3) / 3, 'same') * 0.4 * (0.5 + 0.5 * np.sign(np.sin(np.linspace(0, 20 * np.pi, n))))
def traffic(d): n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(400) / 400, 'same') * 8
T = dict(part=2.78, sunday=4.24, numHit=4.8, threeHit=6.56, one=[7.78, 8.98, 10.32], hits=[8.2, 9.42, 10.94], shot=12.16, add=13.9, handHit=14.56, takes=15.36, mornHit=16.08,
         abaHit=17.92, found=18.96, foundG=19.62, handles=20.62, handHit2=21.24, tracked=22.42, pageHit=23.5, cards=[24.5, 25.18, 25.68], updHit=26.64, mineHit=28.48,
         n=[29.72, 30.72], nobHit=31.6, kept=32.7, keptHit=33.16, lovelyHit=34.3, end=35.7)
add(0, traffic(T['end'] + 1), 0.008)
for i in range(14): add(1.0 + i * 2.6 + (i % 3) * 0.4, chirp(), 0.012)
add(T['part'], thud(120, 0.2), 0.14); add(T['numHit'], tone(330, 0.4, 5, (1, 0.4)), 0.06); add(T['threeHit'], pop(600), 0.05)
for at in T['one']: add(at, pop(560), 0.06)
for at in T['hits']: add(at, tone(220, 0.3, 5, (1, 0.5)), 0.06)
for i in range(16): add(T['shot'] + 0.1 + i * 0.1, shutter(), 0.05)
add(T['add'], whoosh(0.25), 0.2); add(T['add'] + 0.1, pencil(0.8), 0.04); add(T['handHit'], pencil(0.6), 0.05)
add(T['mornHit'], tone(196, 0.6, 4, (1, 0.5)), 0.07)
add(T['abaHit'] - 0.02, thud(150, 0.3), 0.25)
for i in range(5): add(T['abaHit'] + 0.25 + i * 0.2, bead(), 0.06)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['handles'], whoosh(0.3), 0.24)
for i in range(3): add(T['handHit2'] + i * 0.1, ding(1318.5 + i * 100, 0.35), 0.04)
add(T['tracked'], whoosh(0.3), 0.24); add(T['pageHit'], ding(1046.5, 0.5), 0.05)
for at in T['cards']: add(at, pop(620), 0.05)
add(T['updHit'], slide(600, 1200, 0.25), 0.05); add(T['mineHit'], ding(1568, 0.6), 0.06)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['kept'], whoosh(0.25), 0.2)
for i in range(6): add(T['kept'] + 0.3 + i * 0.33, bead(), 0.05)
add(T['lovelyHit'], ding(1318.5, 0.5), 0.05)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
