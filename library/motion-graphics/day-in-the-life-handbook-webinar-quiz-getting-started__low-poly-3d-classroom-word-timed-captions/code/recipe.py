#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, sped 1.1x, take 1) plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 37.9
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(47)
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
def bell(d=0.9):                                                                # a school bell, briefly
    n = int(d * SR); t = np.arange(n) / SR; return (np.sin(2 * np.pi * 1870 * t) + 0.6 * np.sin(2 * np.pi * 2490 * t)) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 26 * t))) * np.exp(-t * 2.5)
def scratch(d=0.3):                                                                # a red pen
    n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(6) / 6, 'same') * np.sin(np.linspace(0, np.pi, n)) * (0.6 + 0.4 * np.sin(np.linspace(0, 50, n)))
def slam(): return np.concatenate([thud(90, 0.7) * 1.4])                           # ninety pages meeting a desk
T = dict(part=2.2, sign=3.44, signHit=3.76, pack=5.36, packHit=5.74, book=6.56, bookHit=7.44, web=8.38, webHit=9.0, tues=9.94, tuesHit=11.14, quiz=12.04, quizHit=12.36, onbHit=13.3, scoreHit=14.36, lost=15.68, lostHit=16.48,
         found=17.6, foundG=18.2, levels=19.24, levelsHit=19.94, fiveHit=21.68, finHit=22.96, unlockHit=24.02, links=24.78, linksHit=25.56, pageHit=26.16, n=[27.7, 28.56], nob=29.3, cb=30.2, cbHit=30.3, purposeHit=31.82, end=32.9)
add(0.05, bell(0.8), 0.02)
add(T['part'], thud(120, 0.2), 0.14)
add(T['sign'], whoosh(0.3), 0.25); add(T['signHit'], ding(1318.5, 0.5), 0.07); add(T['signHit'] + 0.1, ding(1760, 0.5), 0.06)
add(T['pack'], whoosh(0.35), 0.3)
for i in range(3): add(T['packHit'] - 0.1 + i * 0.16, pop(480 + i * 70), 0.07)
add(T['book'], slide(900, 200, 0.85), 0.05); add(T['bookHit'], slam(), 0.5); add(T['bookHit'] + 0.02, buzz(0.2), 0.05); add(T['bookHit'] + 0.3, thud(110, 0.2), 0.16)
add(T['web'], whoosh(0.35), 0.3); add(T['webHit'], tone(660, 0.14, 3), 0.06); add(T['webHit'] + 0.25, pop(440), 0.07)
add(T['tues'], whoosh(0.25), 0.2); add(T['tuesHit'], buzz(0.45), 0.11); add(T['tuesHit'], thud(150, 0.4), 0.3)
add(T['quiz'], whoosh(0.35), 0.3)
for i in range(5): add(T['quizHit'] + i * 0.07, click(), 0.14)
add(T['onbHit'] - 0.2, scratch(0.3), 0.14); add(T['onbHit'], thud(130, 0.25), 0.2)
for i in range(4): add(T['scoreHit'] - 0.1 + i * 0.05, scratch(0.1), 0.14)
add(T['scoreHit'], thud(150, 0.45), 0.34); add(T['scoreHit'] + 0.02, buzz(0.4), 0.1); add(T['scoreHit'] + 0.1, slide(520, 240, 0.4), 0.07)
add(T['lost'], whoosh(0.25), 0.2); add(T['lostHit'], slide(500, 260, 0.4), 0.08); add(T['lostHit'], thud(130, 0.3), 0.24)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['levels'], whoosh(0.4), 0.3)
for i in range(3): add(T['levelsHit'] - 0.1 + i * 0.13, whoosh(0.14), 0.14); add(T['levelsHit'] + i * 0.13, ding(1046.5 * 2 ** (i * 2 / 12), 0.4), 0.065)
for i in range(3): add(T['fiveHit'] - 0.1 + i * 0.1, pop(620 + i * 60), 0.06)
add(T['finHit'], click(), 0.4); add(T['finHit'] + 0.03, ding(1568, 0.5), 0.07)
add(T['unlockHit'], click(), 0.35); add(T['unlockHit'] + 0.06, tone(1760, 0.25, 4), 0.07); add(T['unlockHit'] + 0.06, thud(160, 0.15), 0.14)
add(T['links'], whoosh(0.3), 0.25)
for i in range(6): add(T['linksHit'] - 0.1 + i * 0.1, pop(500 + i * 40), 0.055)
add(T['pageHit'], click(), 0.4); add(T['pageHit'] + 0.03, ding(2093, 0.5), 0.07)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['cb'], whoosh(0.35), 0.3); add(T['cbHit'] - 0.05, scratch(0.35), 0.16); add(T['cbHit'], thud(140, 0.3), 0.24)
add(T['purposeHit'] - 0.05, scratch(0.3), 0.14); add(T['purposeHit'], ding(1318.5, 0.4), 0.07); add(T['purposeHit'] + 0.1, ding(1760, 0.5), 0.07)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
