#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men), Eleven v4,
take 1, sped 1.13x) plus synthesised sounds on the demo's timeline (the T block in demo.html) at a
car wash: spray hiss, squeaky sponge, phone taps, a like, the brushes spinning, foam. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.76
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(44)
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
T = {"part": 2.36, "i1": 3.48, "cars": 3.84, "on": 4.66, "brands": 5.86, "every": 6.74, "post": 7.02, "tags": 8.44, "commentI": 9.28, "commented": 9.4, "fire": 9.8, "year": 12.3, "liked0": 13.0, "liked": 13.18, "chair": 14.26, "followed": 14.96, "once": 15.62, "bot": 16.76, "so": 17.32, "filmed": 17.88, "wash": 18.34, "attention": 19.28, "brushes0": 20.16, "won": 20.5, "found": 21.34, "foundG": 22.04, "my": 22.8, "profile": 22.96, "headline": 23.88, "top": 24.76, "switch": 26.22, "disc": 27.1, "browse": 28.64, "invite": 29.48, "no": 30.26, "n1": 30.42, "n2s": 31.14, "n2": 31.52, "nob": 32.28, "nobHit": 32.44, "still": 33.24, "chairC": 34.06, "its": 34.68, "good": 34.86, "end": 35.76, "dur": 40.76}
def hiss(d): n = int(d * SR); return np.convolve(rng.standard_normal(n), [1, -0.9], 'same') * np.sin(np.linspace(0, np.pi, n)) ** 0.3 * 0.5
def squeak(): n = int(0.12 * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * np.cumsum(np.linspace(1400, 2200, n)) / SR) * np.sin(np.linspace(0, np.pi, n)) * 0.6
def tap(): return np.pad(click()[:400], (0, 1520)) * 0.7 + tone(2400, 0.04, 30) * 0.2
def swish(d): n = int(d * SR); t = np.arange(n) / SR; return np.convolve(rng.standard_normal(n), np.ones(12) / 12, 'same') * (0.6 + 0.4 * np.sin(2 * np.pi * 7 * t)) * 3
def blob(): return slide(300, 120, 0.12)
add(0, hiss(DUR) * 0.3, 0.02)
add(T['part'], thud(120, 0.2), 0.14)
add(T['i1'], whoosh(0.3), 0.2)
for i in range(5): add(T['i1'] + 0.1 + i * 0.22, squeak(), 0.03)
add(T['cars'], pop(520), 0.04); add(T['on'], whoosh(0.3), 0.18)
for i in range(10): add(T['on'] + 0.3 + i * 0.12, tap(), 0.05)
add(T['brands'], pop(520), 0.04)
add(T['every'], whoosh(0.3), 0.24)
for i in range(30): add(T['every'] + i * (T['tags'] + 0.4 - T['every']) / 30, tap(), 0.035)
add(T['tags'], buzz(0.25, 90), 0.05)
add(T['commentI'], whoosh(0.3), 0.2)
for i in range(4): add(T['commented'] + i * 0.25, pop(600 + i * 40), 0.04)
add(T['year'], buzz(0.25, 80), 0.04)
add(T['liked0'], whoosh(0.3), 0.2); add(T['liked'], pop(900), 0.06); add(T['liked'] + 0.05, ding(1318.5, 0.3), 0.03)
add(T['followed'], whoosh(0.3), 0.2); add(T['followed'] + 0.05, ding(1046.5, 0.4), 0.04); add(T['bot'], buzz(0.35, 70), 0.06)
add(T['so'], whoosh(0.3), 0.2); add(T['wash'], hiss(1.8), 0.05); add(T['wash'], swish(1.9), 0.03)
add(T['brushes0'], swish(1.2), 0.09); add(T['brushes0'], hiss(1.2), 0.06)
for i in range(8): add(T['brushes0'] + 0.1 + i * 0.13, blob(), 0.04)
add(T['won'], thud(80, 0.4), 0.3); add(T['won'] + 0.05, stampS(), 0.25)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['my'], whoosh(0.3), 0.26)
for i in range(12): add(T['headline'] + i * 0.05, tap(), 0.03)
for i in range(3): add(T['top'] + i * 0.1, pop(700 + i * 80), 0.04)
add(T['switch'] + 0.1, click(), 0.14); add(T['switch'] + 0.12, slide(500, 900, 0.12), 0.04); add(T['disc'], ding(1046.5, 0.5), 0.05)
add(T['browse'], whoosh(0.3), 0.2); add(T['invite'], click(), 0.12); add(T['invite'] + 0.25, ding(1318.5, 0.5), 0.05)
for at in [T['n1'] + 0.15, T['n2'] + 0.12]: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['still'], whoosh(0.3), 0.18)
for i in range(6): add(T['still'] + 0.3 + i * 0.12, tap(), 0.05)
add(T['its'], whoosh(0.3), 0.22)
for i in range(10): add(T['good'] - 0.3 + i * 0.06, tap(), 0.03)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
