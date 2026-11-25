#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, take 1, sped 1.3x)
plus synthesised sounds on the demo's timeline (the T block in demo.html) in a yoga studio: room tone, birds outside,
a singing bowl, sent-mail swooshes, a breathing voice note, creaks for the knot, typing. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 43.36
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
T = {"part": 2.38, "teach": 3.6, "yoga": 3.8, "monday": 4.96, "pitched": 5.46, "noreply": 6.54, "lunch": 7.64, "bump1": 8.5, "night": 9.78, "bump2": 10.6, "tue": 11.9, "per": 12.5, "wed": 13.76, "hello": 14.52, "thu": 15.38, "vnote": 16.28, "breath": 16.94, "replied": 17.72, "who": 18.6, "so": 19.6, "hardest": 20.44, "still": 21.5, "found": 22.48, "foundG": 23.22, "brand": 24.4, "personal": 25.14, "ai": 26.06, "fBrand": 27.22, "fNiche": 27.38, "fDeliv": 27.92, "email": 28.8, "dm": 29.58, "fu": 30.36, "four": 31.38, "later": 31.74, "notf": 32.4, "hours": 32.72, "no": 33.38, "n1": 33.56, "n2s": 34.2, "n2": 34.3, "nob": 34.98, "nobHit": 35.06, "teach2": 35.8, "knot": 36.28, "nobody": 37.16, "out": 37.56, "end": 38.36, "dur": 43.36}
def bird(): n = int(0.18 * SR); return np.sin(2 * np.pi * np.cumsum(np.linspace(3200, 4200, n) + 300 * np.sin(np.linspace(0, 40, n))) / SR) * np.sin(np.linspace(0, np.pi, n))
def tap(): return np.pad(click()[:400], (0, 1520)) * 0.7 + tone(2400, 0.04, 30) * 0.2
def bowl(d=3.0): return tone(392, d, 2.2, (1, 0.5, 0.25, 0.12)) + tone(394.5, d, 2.4) * 0.6
def sent(): return np.concatenate([whoosh(0.25) * 0.8, slide(700, 1400, 0.12)])
def breath(d=1.0):
    n = int(d * SR); s = np.convolve(rng.standard_normal(n), np.ones(60) / 60, 'same'); return s * np.sin(np.linspace(0, np.pi, n)) ** 2 * 4
def creak(d=0.4):
    n = int(d * SR); t = np.arange(n) / SR; return np.sign(np.sin(2 * np.pi * (40 + 30 * np.sin(2 * np.pi * 3 * t)) * t)) * np.exp(-np.linspace(0, 2, n)) * 0.3
add(0, hum(DUR, 55), 0.006)
for i in range(8): add(0.8 + i * 5.1, bird(), 0.018)
add(0.3, bowl(3.5), 0.05)
add(T['part'], thud(120, 0.2), 0.14)
add(T['teach'], whoosh(0.3), 0.2); add(T['yoga'], bowl(1.6), 0.035)
add(T['monday'], whoosh(0.3), 0.22); add(T['pitched'], sent(), 0.12); add(T['noreply'], buzz(0.25, 110), 0.05)
add(T['lunch'], whoosh(0.3), 0.2)
for k in ['bump1', 'bump2', 'per', 'hello']: add(T[k], sent(), 0.1)
add(T['vnote'], pop(600), 0.05)
for i in range(3): add(T['breath'] + i * 0.25, breath(0.5), 0.05)
add(T['replied'], whoosh(0.3), 0.2); add(T['replied'] + 0.1, ding(1318.5, 0.4), 0.04); add(T['who'], pop(500), 0.06)
add(T['so'], whoosh(0.4), 0.2); add(T['hardest'], creak(0.5), 0.12); add(T['hardest'] + 0.3, thud(110, 0.25), 0.18)
add(T['still'], stampS(), 0.25); add(T['still'], thud(80, 0.35), 0.22); add(T['still'] + 0.3, creak(0.6), 0.1)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['brand'], whoosh(0.3), 0.26); add(T['personal'], pop(620), 0.05)
for k in ['fBrand', 'fNiche', 'fDeliv']:
    for i in range(6): add(T[k] + i * 0.06, tap(), 0.03)
for k, f in [('email', 880), ('dm', 1046.5), ('fu', 1318.5)]: add(T[k], ding(f, 0.35), 0.045)
add(T['four'], ding(1568, 0.5), 0.045); add(T['notf'], pop(520), 0.04)
for at in [T['n1'] + 0.15, T['n2'] + 0.12]: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['teach2'], whoosh(0.3), 0.22); add(T['knot'], bowl(2.0), 0.05)
for i in range(5): add(T['nobody'] + i * 0.17, creak(0.2), 0.06)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
