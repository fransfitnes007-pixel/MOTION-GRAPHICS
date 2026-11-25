#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4,
take 1, sped 1.14x) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet
airport gate: a hall hum and a boarding chime. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.7
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(135)
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
def hall(d): n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(500) / 500, 'same') * 9
def chime(): return np.concatenate([tone(784, 0.5, 3, (1, 0.3)), tone(988, 0.5, 3, (1, 0.3)), tone(1175, 0.9, 3, (1, 0.3))])
def trash(): return np.concatenate([slide(900, 300, 0.18) * 0.6, click()[:900] * 0.8])
T = dict(part=2.68, airport=4.0, phone=5.08, fullHit=6.18, so=6.96, dels=[9.26, 11.32, 12.67], owe=13.74, todayHit=14.6, empt=15.44, binHit=16.0, backup=16.92, thumbHit=19.64,
         lie=20.09, found=20.5, foundG=21.26, now=22.16, contentHit=23.38, versionHit=24.74, reviewHit=26.24, phone2=26.9, playHit=28.16, still=29.06, n=[30.2, 31.24], nobHit=32.12,
         again=33.02, fullHit2=33.52, catsHit=34.82, end=35.7)
add(0, hall(T['end'] + 1), 0.01)
add(T['part'], thud(120, 0.2), 0.14); add(T['airport'] + 0.1, chime(), 0.035)
add(T['phone'], whoosh(0.3), 0.26); add(T['fullHit'], buzz(0.3, 70), 0.06); add(T['fullHit'] + 0.02, stampS(), 0.25)
add(T['so'], whoosh(0.3), 0.26)
for at in T['dels']: add(at, trash(), 0.12)
add(T['dels'][2] + 0.1, tone(196, 0.6, 4, (1, 0.5)), 0.08)
add(T['todayHit'], tone(330, 0.4, 5, (1, 0.4)), 0.06)
add(T['empt'], whoosh(0.3), 0.26); add(T['binHit'], trash(), 0.14); add(T['binHit'] + 0.02, stampS(), 0.25)
add(T['backup'], whoosh(0.3), 0.26); add(T['thumbHit'], stampS(), 0.28); add(T['lie'], thud(110, 0.4), 0.25)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['now'], whoosh(0.3), 0.26)
for i in range(3): add(T['contentHit'] + i * 0.18, pop(560 + i * 50), 0.05)
add(T['versionHit'], ding(1318.5, 0.5), 0.05); add(T['reviewHit'], ding(1568, 0.5), 0.05)
add(T['phone2'], whoosh(0.3), 0.26); add(T['playHit'], click(), 0.25); add(T['still'], ding(1046.5, 0.6), 0.07); add(T['still'] + 0.08, ding(1568, 0.5), 0.05)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['again'], whoosh(0.3), 0.26)
for i in range(12): add(T['again'] + 0.1 + i * 0.12, pop(700 + (i % 4) * 80), 0.03)
add(T['catsHit'], slide(700, 1400, 0.3), 0.05)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
