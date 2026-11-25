#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4,
take 1, sped 1.3x) plus synthesised sounds on the demo's timeline (the T block in demo.html) in an
empty cinema: a projector whirr, a torch click, popcorn, slide clicks, a folding seat. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.82
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(43)
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
T = {"part": 2.34, "im": 3.66, "usher": 3.82, "between": 4.82, "briefs": 5.82, "this": 6.66, "sixty": 7.08, "s1": 8.54, "s2": 10.16, "bigger": 10.98, "s9": 11.98, "journey": 13.02, "filmed": 14.84, "cheap": 15.98, "good": 16.7, "they": 17.4, "did": 18.34, "fifty8": 19.04, "grey": 19.98, "never": 20.96, "neverCheap": 21.4, "found": 22.36, "foundG": 23.04, "brief": 23.84, "app": 24.4, "numbered": 25.08, "one": 25.7, "section": 26.12, "tap": 26.96, "rules": 27.1, "opens": 27.78, "no": 28.6, "n1": 29.02, "n2s": 29.7, "n2": 30.2, "nob": 30.92, "nobHit": 31.06, "still": 32.12, "teal": 34.02, "nobody": 34.72, "asked": 35.02, "end": 35.82, "dur": 40.82}
def creak(d=0.6): n = int(d * SR); t = np.arange(n) / SR; f = 90 + 40 * np.sin(2 * np.pi * 3 * t); return np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * np.convolve(rng.standard_normal(n), np.ones(40) / 40, 'same') * 4 * np.sin(np.linspace(0, np.pi, n))
def whirr(d): n = int(d * SR); t = np.arange(n) / SR; return (np.sin(2 * np.pi * 24 * t) * 0.5 + 0.5) * np.convolve(rng.standard_normal(n), np.ones(30) / 30, 'same') * 3
def crunch(): n = int(0.12 * SR); return np.convolve(rng.standard_normal(n), np.ones(3) / 3, 'same') * (rng.random(n) > 0.7) * np.exp(-np.linspace(0, 4, n))
def sclick(): return tone(1800, 0.04, 20, (1, 0.5)) + np.pad(click()[:500], (0, int(0.04 * SR) - 500)) * 0.6
add(0, whirr(DUR), 0.006)
for i in range(6): add(0.4 + i * 0.35, crunch(), 0.05)
add(T['part'], thud(120, 0.2), 0.14)
add(T['im'], whoosh(0.3), 0.2); add(T['im'] + 0.1, click(), 0.12); add(T['usher'], pop(520), 0.04)
add(T['between'], whoosh(0.3), 0.18); add(T['briefs'], pop(520), 0.04)
add(T['this'], whoosh(0.4), 0.24); add(T['this'] + 0.05, click(), 0.08); add(T['sixty'], buzz(0.25, 90), 0.05)
for at in [T['s1'], T['s2'], T['s9']]: add(at, sclick(), 0.1); add(at, whoosh(0.2), 0.08)
add(T['bigger'], thud(90, 0.3), 0.18)
for i in range(6): add(T['journey'] + i * 0.18, tone(600 + i * 40, 0.05, 12), 0.02)
for i in range(5): add(T['s9'] + 0.6 + i * 0.4, crunch(), 0.05)
add(T['filmed'], whoosh(0.3), 0.2); add(T['filmed'] + 0.1, tone(1200, 0.08, 12), 0.04); add(T['cheap'], pop(600), 0.05); add(T['good'], pop(500), 0.04)
add(T['they'], whoosh(0.3), 0.22)
for at in [T['they'] + 0.1, T['did'], T['fifty8']]: add(at, pop(560), 0.05)
add(T['grey'], sclick(), 0.1); add(T['grey'], slide(300, 200, 0.9), 0.025)
add(T['never'], creak(0.5), 0.1); add(T['never'] + 0.35, thud(80, 0.35), 0.3); add(T['neverCheap'], stampS(), 0.25)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['brief'], whoosh(0.3), 0.26)
for i in range(4): add(T['numbered'] + i * 0.07, tone(880 + i * 90, 0.07, 12), 0.025)
for i in range(4): add(T['one'] + i * 0.1, tone(700 + i * 60, 0.06, 12), 0.02)
add(T['tap'], click(), 0.12); add(T['opens'], slide(400, 800, 0.2), 0.04)
for i in range(3): add(T['opens'] + i * 0.15, ding(1046.5 + 130 * i, 0.35), 0.04)
for at in [T['n1'] + 0.15, T['n2'] + 0.12]: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['still'], whoosh(0.3), 0.2); add(T['still'] + 0.05, sclick(), 0.08)
for i in range(4): add(T['still'] + 0.5 + i * 0.4, crunch(), 0.05)
add(T['teal'], ding(784, 0.6), 0.06); add(T['teal'], whoosh(0.3), 0.15)
add(T['nobody'], whoosh(0.4), 0.2); add(T['asked'] + 0.3, crunch(), 0.05)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
