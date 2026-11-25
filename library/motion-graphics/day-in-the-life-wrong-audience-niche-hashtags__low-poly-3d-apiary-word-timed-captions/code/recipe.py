#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men), Eleven v4,
take 1, sped 1.23x) plus synthesised sounds on the demo's timeline (the T block in demo.html) in an
apiary: birdsong, a bee drone that swells into a swarm, comment pops, a dance beat, typing. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.96
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(46)
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
def thunk(): return thud(260, 0.12) * 0.9 + np.pad(click()[:800], (0, int(0.12 * SR) - 800)) * 0.4
def pock(): return tone(900, 0.07, 12, (1, 0.4)) + np.pad(click()[:600], (0, int(0.07 * SR) - 600)) * 0.5
def blip(): return slide(500, 900, 0.1)
def bark(): n = int(0.16 * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * np.cumsum(np.geomspace(520, 260, n)) / SR) * np.sign(np.sin(2 * np.pi * 90 * t)) * 0.5 * np.exp(-np.linspace(0, 5, n))
T = {"part": 2.24, "i1": 3.36, "bees1": 3.68, "i2": 4.46, "videos": 4.68, "my1": 5.96, "fyp": 6.96, "viral": 8.16, "foryou": 8.76, "my2": 9.5, "first": 10.48, "spaceman": 11.44, "grandma": 12.36, "sweet": 13.34, "the1": 14.08, "asked": 14.54, "audience": 15.1, "so": 16.02, "danced": 16.24, "suit": 17.16, "forA": 17.76, "theBees": 18.88, "enjoy": 19.8, "found": 20.72, "foundG": 21.4, "hashtag": 22.32, "typed": 23.58, "beek": 23.84, "fifteen": 24.9, "broad": 25.58, "niche": 26.7, "micro": 27.04, "reason": 27.8, "niche2": 29.14, "no": 31.14, "n1": 31.24, "n2s": 32.08, "n2": 32.2, "nob": 32.98, "nobHit": 33.04, "grandma2": 33.9, "she": 35.02, "gotbees": 35.24, "end": 35.96, "dur": 40.96}
def buzzD(d, f=220, depth=0.3):
    n = int(d * SR); t = np.arange(n) / SR; ph = 2 * np.pi * np.cumsum(f * (1 + depth * 0.05 * np.sin(2 * np.pi * 6 * t))) / SR
    return (np.sign(np.sin(ph)) * 0.4 + np.sin(2 * ph) * 0.3) * (0.7 + 0.3 * np.sin(2 * np.pi * 3.3 * t))
def bird(): n = int(0.18 * SR); return np.sin(2 * np.pi * np.cumsum(np.linspace(3200, 4200, n) + 300 * np.sin(np.linspace(0, 40, n))) / SR) * np.sin(np.linspace(0, np.pi, n))
def tap(): return np.pad(click()[:400], (0, 1520)) * 0.7 + tone(2400, 0.04, 30) * 0.2
add(0, buzzD(DUR, 210) * np.linspace(1, 1, int(DUR * SR)), 0.004)
for i in range(9): add(0.5 + i * 4.3, bird(), 0.02)
add(T['part'], thud(120, 0.2), 0.14)
add(T['i1'], whoosh(0.3), 0.2); add(T['i1'] + 0.1, buzzD(1.0, 240), 0.02); add(T['bees1'], pop(520), 0.04)
add(T['i2'], whoosh(0.3), 0.18); add(T['videos'], pop(520), 0.04)
add(T['my1'], whoosh(0.3), 0.24)
for at in [T['fyp'], T['viral'], T['foryou']]: add(at, pop(640), 0.05)
add(T['my2'], whoosh(0.3), 0.2)
for at in [T['first'], T['spaceman'], T['grandma']]: add(at, pop(560), 0.05); add(at + 0.05, ding(1318.5, 0.2), 0.015)
add(T['the1'], whoosh(0.3), 0.22)
for at in [T['the1'] + 0.1, T['asked'], T['audience']]: add(at, pop(560), 0.05)
add(T['so'], whoosh(0.3), 0.2)
for i in range(int((T['theBees'] - T['danced']) / 0.21)): add(T['danced'] + i * 0.21, thud(90 if i % 2 == 0 else 160, 0.1), 0.08)
add(T['danced'], buzzD(T['theBees'] - T['danced'], 230), 0.015)
add(T['theBees'], buzzD(T['found'] - T['theBees'], 260, 1), 0.07); add(T['enjoy'], stampS(), 0.25); add(T['enjoy'], thud(80, 0.35), 0.25)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['hashtag'], whoosh(0.3), 0.26)
for i in range(10): add(T['typed'] + i * 0.05, tap(), 0.035)
for i in range(15): add(T['fifteen'] + 0.1 + i * 0.04, tone(800 + i * 40, 0.05, 14), 0.02)
for at, f in [(T['broad'], 880), (T['niche'], 1046.5), (T['micro'], 1318.5)]: add(at, ding(f, 0.35), 0.045)
add(T['reason'], pop(620), 0.05); add(T['niche2'], ding(1046.5, 0.5), 0.05)
for at in [T['n1'] + 0.15, T['n2'] + 0.12]: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['grandma2'], whoosh(0.3), 0.22); add(T['she'], pop(700), 0.05); add(T['she'] + 0.05, ding(1568, 0.4), 0.03)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
