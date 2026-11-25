#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men), Eleven v4,
take 1, sped 1.1x) plus synthesised sounds on the demo's timeline (the T block in demo.html) in a
basement: a boiler hum, a buzzing bulb, straining at a wall, creaks and falling dust, a wall that talks. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.3
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(142)
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
T = {"part": 2.42, "every": 3.66, "sameHit": 4.86, "talking": 6.56, "wallHit1": 7.8, "forty": 8.72, "videos": 9.08, "oneWall": 10.2, "brand": 10.98, "tryHit": 11.72, "newHit": 12.14, "so": 12.74, "moved": 13.28, "notLit": 14.18, "tried": 15.2, "load": 16.08, "found": 17.04, "foundG": 17.74, "style": 18.6, "ten": 19.44, "when": 20.36, "pov": 22.06, "unbox": 22.68, "tut": 23.7, "skits": 24.52, "so2": 25.06, "skit": 25.78, "chars": 26.9, "wallHit": 28.58, "no": 29.34, "n1": 29.44, "n2s": 30.22, "n2": 30.46, "nob": 31.38, "nobHit": 31.5, "wallS": 32.3, "everyHit": 32.76, "it": 34.0, "royal": 34.32, "end": 35.3, "dur": 40.3}
def creak(d=0.6): n = int(d * SR); t = np.arange(n) / SR; f = 90 + 40 * np.sin(2 * np.pi * 3 * t); return np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * np.convolve(rng.standard_normal(n), np.ones(40) / 40, 'same') * 4 * np.sin(np.linspace(0, np.pi, n))
def grit(d): n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(5) / 5, 'same') * np.exp(-np.linspace(0, 2, n)) * 0.6
def mumble(d=0.5): n = int(d * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * (110 + 30 * np.sin(2 * np.pi * 7 * t)) * t) * (0.5 + 0.5 * np.sin(2 * np.pi * 9 * t)) * np.sin(np.linspace(0, np.pi, n))
add(0, hum(DUR, 55), 0.014)
add(T['part'], thud(120, 0.2), 0.14)
for at in [T['sameHit'], T['talking'], T['wallHit1']]: add(at, pop(520), 0.04)
add(T['forty'], whoosh(0.3), 0.26)
for i in range(9): add(T['forty'] - 0.3 + i * 0.05, tone(700, 0.05, 12), 0.02)
add(T['oneWall'], buzz(0.3, 80), 0.05)
add(T['brand'], whoosh(0.3), 0.22)
for at in [T['brand'] + 0.1, T['tryHit'], T['newHit']]: add(at, pop(560), 0.05)
add(T['so'], whoosh(0.3), 0.2); add(T['moved'], creak(0.8), 0.06); add(T['notLit'], slide(400, 300, 0.3), 0.04); add(T['tried'], creak(0.9), 0.1); add(T['tried'] + 0.2, thud(80, 0.4), 0.15)
add(T['load'], thud(70, 0.6), 0.35); add(T['load'] + 0.05, stampS(), 0.25); add(T['load'], grit(1.0), 0.12); add(T['load'] + 0.3, creak(0.7), 0.1)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['style'], whoosh(0.3), 0.26)
for i in range(10): add(T['ten'] + i * 0.05, tone(880 + i * 60, 0.08, 12), 0.02)
add(T['when'], pop(620), 0.05)
for at in [T['pov'], T['unbox'], T['tut'], T['skits']]: add(at, ding(1046.5 + 130 * [T['pov'], T['unbox'], T['tut'], T['skits']].index(at), 0.35), 0.045)
add(T['skit'], whoosh(0.3), 0.2)
for i in range(6): add(T['chars'] + i * 0.45, pop(400 if i % 2 else 600), 0.03)
add(T['wallHit'], tone(220, 0.3, 4, (1, 0.4)), 0.06); add(T['wallHit'] + 0.2, mumble(0.6), 0.04)
for at in [T['n1'] + 0.2, T['n2'] + 0.12]: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['wallS'], whoosh(0.3), 0.26)
for i in range(9): add(T['wallS'] + 0.1 + i * 0.04, tone(900 + i * 50, 0.06, 12), 0.02)
add(T['royal'], mumble(0.7), 0.06); add(T['royal'] + 0.1, slide(300, 200, 0.4), 0.03)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
