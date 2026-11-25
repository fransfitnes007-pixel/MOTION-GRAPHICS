#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men), Eleven v4,
take 2, sped 1.11x) plus synthesised sounds on the demo's timeline (the T block in demo.html) at a
skate park: birds, distant board clacks and wheels, a cap whoosh, a drop-in roll, a slam, typing-free taps. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.98
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(48)
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
T = {"part": 2.44, "im": 3.62, "fifty": 3.7, "fix": 4.64, "boilers": 4.94, "every": 6.16, "ages": 7.12, "eighteen": 7.48, "twenty": 8.2, "so": 9.14, "wore": 9.7, "backwards": 10.16, "said1": 10.9, "nocap": 11.2, "said2": 12.1, "bussin": 12.32, "about": 13.34, "boiler": 13.7, "bought": 14.46, "skate": 14.84, "the2": 15.62, "won": 16.08, "brand": 16.88, "said3": 17.2, "genz": 17.5, "found": 19.1, "foundG": 19.6, "my": 20.4, "set": 21.32, "forty": 22.4, "find": 23.46, "notfit": 24.66, "age": 26.38, "before": 27.4, "notafter": 28.44, "fall": 29.0, "no": 29.66, "n1": 29.86, "n2s": 30.44, "n2": 30.54, "nob": 31.38, "nobHit": 31.48, "skaters": 32.34, "unc": 33.1, "idk": 33.7, "means": 34.24, "love": 34.96, "end": 35.98, "dur": 40.98}

def bird(): n = int(0.18 * SR); return np.sin(2 * np.pi * np.cumsum(np.linspace(3200, 4200, n) + 300 * np.sin(np.linspace(0, 40, n))) / SR) * np.sin(np.linspace(0, np.pi, n))
def tap(): return np.pad(click()[:400], (0, 1520)) * 0.7 + tone(2400, 0.04, 30) * 0.2
def roll(d, f=70):
    n = int(d * SR); t = np.arange(n) / SR; s = np.convolve(rng.standard_normal(n), np.ones(60) / 60, 'same') * 4 + 0.3 * np.sin(2 * np.pi * f * t) * (1 + 0.3 * np.sin(2 * np.pi * 11 * t))
    e = np.ones(n); r = min(n // 4, int(0.08 * SR)); e[:r] = np.linspace(0, 1, r); e[-r:] = np.linspace(1, 0, r); return s * e
def clack(): return thud(320, 0.09) * 0.8 + np.pad(click()[:900], (0, int(0.09 * SR) - 900)) * 0.6
def crowd(d):
    n = int(d * SR); s = np.zeros(n)
    for k in range(5): s += np.sin(2 * np.pi * np.cumsum(np.full(n, 180 + k * 37) * (1 + 0.04 * np.sin(np.linspace(0, 9 + k, n)))) / SR) * (0.5 + 0.5 * np.sin(np.linspace(k, 6 + k, n)))
    return np.convolve(s, np.ones(200) / 200, 'same') * np.sin(np.linspace(0, np.pi, n)) ** 0.5
# park ambience: birds and far-off skating
for i in range(9): add(0.6 + i * 4.4, bird(), 0.018)
for i in range(14): at = 0.4 + i * 2.6 + (i % 3) * 0.4; add(at, roll(1.1), 0.006); add(at + 1.05, clack(), 0.02)
add(T['part'], thud(120, 0.2), 0.14)
add(T['im'], whoosh(0.3), 0.18); add(T['fifty'], pop(520), 0.04)
add(T['fix'], whoosh(0.3), 0.2); add(T['boilers'], tone(1800, 0.25, 8, (1, 0.5, 0.2)), 0.05); add(T['boilers'], pop(520), 0.04)
add(T['every'], whoosh(0.3), 0.24)
for at in [T['ages'], T['eighteen'] + 0.3, T['twenty']]: add(at, pop(640), 0.05); add(at + 0.04, buzz(0.15, 110), 0.03)
add(T['so'], whoosh(0.3), 0.2); add(T['wore'], pop(420), 0.05); add(T['backwards'], whoosh(0.4), 0.3); add(T['backwards'] + 0.35, ding(1568, 0.3), 0.03)
add(T['said1'], whoosh(0.3), 0.2)
for at in [T['nocap'], T['bussin']]: add(at, pop(600), 0.05)
add(T['boiler'], pop(600), 0.05); add(T['boiler'] + 0.05, buzz(0.2, 98), 0.04)
add(T['bought'], whoosh(0.3), 0.2); add(T['skate'], clack(), 0.12)
D0 = T['the2'] - 0.2; D1 = T['won'] - 0.1; D2 = D1 + 0.36
add(D0, whoosh(0.3), 0.25); add(D0 + 0.05, roll(D1 - D0 + 0.4, 60), 0.05)
add(D1, clack(), 0.2); add(D1 + 0.05, slide(900, 260, 0.35), 0.08)
add(D2, thud(70, 0.5), 0.45); add(D2, squelch(0.25), 0.06); add(D2 + 0.02, stampS(), 0.25)
add(D1 + 0.6, clack(), 0.08); add(D2 + 0.25, crowd(1.3), 0.025)
add(T['brand'], whoosh(0.3), 0.22)
for at in [T['brand'] + 0.05, T['said3'], T['genz']]: add(at, pop(560), 0.05)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['my'], whoosh(0.3), 0.26); add(T['forty'], tap(), 0.06); add(T['forty'] + 0.02, ding(1046.5, 0.4), 0.05)
add(T['find'], whoosh(0.25), 0.18)
for i in range(2): add(T['find'] + 0.1 + i * 0.12, tone(900 + i * 120, 0.06, 14), 0.03)
add(T['notfit'], pop(500), 0.05); add(T['age'], ding(880, 0.4), 0.05)
add(T['before'], ding(1318.5, 0.35), 0.045); add(T['notafter'], ding(1046.5, 0.35), 0.04)
for at in [T['n1'] + 0.15, T['n2'] + 0.12]: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['skaters'] - 0.3, roll(1.9, 75), 0.06); add(T['unc'], pop(700), 0.05)
add(T['idk'], slide(500, 380, 0.3), 0.04); add(T['love'], pop(760), 0.05); add(T['love'] + 0.05, ding(1568, 0.4), 0.03)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
