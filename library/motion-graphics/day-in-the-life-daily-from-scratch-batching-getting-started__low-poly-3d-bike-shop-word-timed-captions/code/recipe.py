#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4,
take 1, sped 1.25x) plus synthesised sounds on the demo's timeline (the T block in demo.html) in a
bike repair shop: a ratchet, a freewheel ticking, a ring light clicking on and off, typing, a snore. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.84
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(45)
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
T = {"part": 2.36, "i1": 3.52, "bikes": 3.82, "post": 5.06, "set": 7.3, "film": 8.42, "edit": 9.08, "postC": 9.72, "pack": 10.34, "mon": 11.36, "tue": 12.12, "wed": 12.86, "by": 13.66, "sunday": 13.76, "editing": 14.52, "sleep": 15.12, "literally": 16.02, "posted": 16.78, "wheel1": 17.34, "just": 17.98, "spinning": 18.86, "found": 19.68, "foundG": 20.32, "getting": 21.24, "level": 22.1, "batch": 23.08, "filmW": 23.78, "edit2": 25.24, "caption": 26.0, "three": 27.78, "ones": 29.34, "no": 30.02, "n1": 30.4, "n2s": 31.08, "n2": 31.44, "nob": 32.14, "nobHit": 32.3, "the": 33.18, "wheel2": 33.32, "im": 35.0, "fine": 35.1, "and": 4.58, "from": 6.26, "end": 35.84, "dur": 40.84}
def tick(): return np.pad(click()[:300], (0, 900)) * 0.6
def ratchet(d=0.6, rate=18):
    n = int(d * SR); out = np.zeros(n); k = int(SR / rate)
    for i in range(0, n - 1200, k): out[i:i + 1200] += tick()
    return out
def tap(): return np.pad(click()[:400], (0, 1520)) * 0.7 + tone(2400, 0.04, 30) * 0.2
def snore(d=0.9): n = int(d * SR); t = np.arange(n) / SR; return np.convolve(rng.standard_normal(n), np.ones(60) / 60, 'same') * np.sin(np.linspace(0, np.pi, n)) * (0.6 + 0.4 * np.sin(2 * np.pi * 30 * t)) * 6
def on(): return thud(300, 0.08) * 0.5 + np.pad(click()[:600], (0, int(0.08 * SR) - 600))
add(0, hum(DUR, 60), 0.01)
add(T['part'], thud(120, 0.2), 0.14)
add(T['i1'], whoosh(0.3), 0.2); add(T['i1'] + 0.1, ratchet(1.0, 14), 0.05)
add(T['and'], whoosh(0.3), 0.18); add(T['post'], pop(520), 0.04); add(T['from'], buzz(0.25, 90), 0.04)
add(T['set'], whoosh(0.3), 0.2); add(T['set'] + 0.25, on(), 0.12)
for i in range(6): add(T['edit'] + i * 0.08, tap(), 0.04)
add(T['postC'], pop(700), 0.05); add(T['pack'] + 0.3, slide(500, 200, 0.4), 0.04); add(T['pack'] + 0.7, on(), 0.1)
for d in range(3):
    t0 = T['mon'] + d * (T['by'] - T['mon']) / 3; add(t0, whoosh(0.2), 0.12); add(t0 + 0.05, on(), 0.08)
    for i in range(4): add(t0 + 0.35 + i * 0.05, tap(), 0.03)
add(T['by'], slide(400, 250, 0.5), 0.03)
for i in range(8): add(T['by'] + 0.4 + i * 0.12, tap(), 0.03 * (1 - i / 9))
add(T['sleep'], snore(0.8), 0.08)
add(T['literally'], thud(90, 0.35), 0.28); add(T['literally'] + 0.04, stampS(), 0.25); add(T['literally'] + 0.4, snore(0.6), 0.06)
add(T['posted'], whoosh(0.3), 0.22); add(T['posted'] + 0.2, ratchet(2.4, 22), 0.03); add(T['spinning'], pop(600), 0.04)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['getting'], whoosh(0.3), 0.26); add(T['level'], slide(400, 800, 0.2), 0.04); add(T['batch'], ding(1046.5, 0.4), 0.05)
add(T['filmW'], whoosh(0.3), 0.2); add(T['filmW'] + 0.05, on(), 0.08)
for i in range(7): add(T['filmW'] + i * (T['edit2'] - T['filmW']) / 7, pop(500 + i * 50), 0.035)
add(T['edit2'], whoosh(0.2), 0.12)
for i in range(8): add(T['edit2'] + 0.1 + i * 0.08, tap(), 0.035)
add(T['caption'], pop(700), 0.04)
for i in range(6): add(T['caption'] + 0.2 + i * 0.1, tap(), 0.03)
add(T['three'], whoosh(0.3), 0.2); add(T['three'] + 0.6, slide(300, 600, 0.5), 0.04); add(T['ones'], ding(1318.5, 0.5), 0.05)
for at in [T['n1'] + 0.15, T['n2'] + 0.12]: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['the'], whoosh(0.3), 0.22); add(T['wheel2'] + 0.2, slide(300, 900, 0.5), 0.04)
add(T['im'], whoosh(0.2), 0.12); add(T['im'] + 0.1, ratchet(0.7, 20), 0.03)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
