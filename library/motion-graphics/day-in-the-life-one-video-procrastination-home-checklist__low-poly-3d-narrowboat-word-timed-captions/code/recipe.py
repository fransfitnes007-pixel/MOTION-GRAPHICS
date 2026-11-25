#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men), Eleven v4,
take 1, sped 1.1x) plus synthesised sounds on the demo's timeline (the T block in demo.html) inside a
narrowboat: rain on the roof, then water lapping, a kettle, jars, an iron, an accordion. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 39.68
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(138)
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
T = {"part": 2.54, "got": 3.62, "apprHit": 3.76, "huge": 5.4, "kettle0": 6.16, "kettleHit": 8.06, "spice": 8.72, "spiceHit": 9.58, "sock": 10.5, "sockHit": 10.94, "acc": 11.6, "threeHit": 11.86, "accHit": 12.82, "had": 13.58, "oneHit": 13.9, "ideaHit": 15.14, "soI": 16.7, "didnt": 17.34, "found": 18.08, "foundG": 18.92, "home": 19.78, "homeHit": 20.16, "exact": 21.16, "two": 22.72, "next": 24.12, "signHit": 24.7, "oneB": 25.28, "cont": 26.86, "turns": 27.6, "pressHit": 28.36, "no": 29.58, "n1": 29.7, "n2s": 30.34, "n2": 30.42, "nob": 31.18, "nobHit": 31.26, "kept": 32.14, "accHit2": 32.5, "neigh": 33.32, "noteHit": 33.96, "end": 34.68, "dur": 39.68}
def acc_chord(fs, d, trem=6.0, sad=False):
    n = int(d * SR); t = np.arange(n) / SR; s = np.zeros(n)
    for f in fs:
        for k in range(1, 7): s += np.sin(2 * np.pi * f * k * t * (1 + 0.002 * np.sin(2 * np.pi * 5 * t))) / k * (0.6 if k % 2 == 0 else 1)
    e = np.ones(n); r = min(n // 4, int(0.04 * SR)); e[:r] = np.linspace(0, 1, r); e[-r:] = np.linspace(1, 0, r)
    if sad: e *= np.linspace(1, 0.2, n); s *= 1
    return s * e * (0.8 + 0.2 * np.sin(2 * np.pi * trem * t)) / len(fs) / 3
def drip(): return tone(1800 + rng.random() * 900, 0.05, 14)
def hiss(d=0.5): n = int(d * SR); return np.diff(np.concatenate([[0], rng.standard_normal(n)])) * np.sin(np.linspace(0, np.pi, n)) * 0.5
def clink(): return tone(2400 + rng.random() * 600, 0.18, 10, (1, 0.5, 0.2))
def lap(d):
    n = int(d * SR); x = np.convolve(rng.standard_normal(n), np.ones(400) / 400, 'same') * 8; return x * (0.6 + 0.4 * np.sin(np.linspace(0, d * 2.4, n)))
def paper(d=0.4): n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(6) / 6, 'same') * np.exp(-np.linspace(0, 4, n)) * (np.sin(np.linspace(0, 40, n)) > 0)
# rain on the roof until YourBrand, water lapping all through
for i in range(int(T['found'] * 22)): add(rng.random() * T['found'], drip(), 0.006)
add(0, lap(DUR), 0.03)
for i in range(8): add(T['foundG'] + 0.5 + i * 2.9 + (i % 3) * 0.5, chirp(), 0.012)
add(T['part'], thud(120, 0.2), 0.14)
add(T['got'], whoosh(0.3), 0.26); add(T['got'] + 0.1, blip(), 0.06); add(T['apprHit'], ding(1318.5, 0.5), 0.05)
add(T['huge'], thud(140, 0.3), 0.22); add(T['huge'], acc_chord([261.6, 329.6, 392], 0.5), 0.0)
add(T['kettle0'], whoosh(0.3), 0.22)
for i in range(int((T['spice'] - T['kettle0']) / 0.15)): add(T['kettle0'] + 0.1 + i * 0.15, click(), 0.03)
add(T['kettleHit'] - 0.3, hiss(1.2), 0.08); add(T['kettleHit'], pop(520), 0.05)
add(T['spice'], whoosh(0.3), 0.22)
for i in range(6): add(T['spiceHit'] - 0.1 + i * 0.09, clink(), 0.05)
add(T['spiceHit'] + 0.6, pop(620), 0.05)
add(T['sock'], whoosh(0.3), 0.22)
for i in range(4): add(T['sock'] + 0.15 + i * 0.52, slide(300, 200, 0.4), 0.03)
add(T['sockHit'] - 0.2, hiss(0.9), 0.1)
for i in range(6): add(T['sockHit'] + i * 0.18, thud(220, 0.08), 0.06)
add(T['acc'], whoosh(0.3), 0.22)
song = [[261.6, 329.6, 392], [349.2, 440, 523.3], [392, 493.9, 587.3], [261.6, 329.6, 392]]
for i in range(int((T['had'] - T['acc']) / 0.4)): add(T['acc'] + 0.1 + i * 0.4, acc_chord(song[i % 4], 0.38), 0.10)
add(T['had'], whoosh(0.3), 0.26); add(T['had'] + 0.1, blip(), 0.06); add(T['oneHit'], buzz(0.25), 0.05); add(T['ideaHit'], buzz(0.35, 70), 0.07)
add(T['soI'], thud(90, 0.5), 0.3); add(T['soI'] + 0.25, acc_chord([196, 233.1, 293.7], 1.6, 2.0, True), 0.12)
add(T['didnt'], stampS(), 0.3)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['home'], whoosh(0.3), 0.26); add(T['homeHit'], pop(620), 0.06)
for k in range(3): add(T['home'] + 0.3 + k * 0.12, tone(880 + k * 220, 0.15, 10), 0.02)
add(T['two'], ding(1046.5, 0.4), 0.05); add(T['next'], ding(1318.5, 0.4), 0.05); add(T['oneB'], pop(700), 0.06); add(T['cont'], click(), 0.2); add(T['cont'] + 0.02, ding(1568, 0.6), 0.07)
add(T['pressHit'], ding(2093, 0.5), 0.05); add(T['pressHit'], thud(160, 0.2), 0.15)
for at in [T['n1'] + 0.2, T['n2'] + 0.12]: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['n1'] + 0.7, tone(1900, 0.4, 6, (1, 0.6, 0.3)), 0.04)
add(T['nobHit'], thud(130, 0.4), 0.3)
happy = [[261.6, 329.6, 392], [392, 493.9, 587.3], [440, 523.3, 659.3], [349.2, 440, 523.3]]
for i in range(int((T['neigh'] - T['kept']) / 0.28)): add(T['kept'] + i * 0.28, acc_chord(happy[i % 4], 0.26, 9), 0.11)
add(T['neigh'], paper(0.5), 0.12); add(T['noteHit'], thud(150, 0.2), 0.12)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
