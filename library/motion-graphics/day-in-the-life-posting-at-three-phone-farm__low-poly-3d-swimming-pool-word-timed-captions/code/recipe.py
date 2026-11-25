#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men), Eleven v4,
take 1, sped 1.11x) plus synthesised sounds on the demo's timeline (the T block in demo.html) at an
indoor pool: the room's echo and splashes, a clock tick, whistle blasts, the drop and the dive, a muffled
underwater hum with bubbles, UI pops and a rack of phones lighting up. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.84
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(50)
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
T = {"part": 2.42, "im": 3.38, "guard": 3.52, "brand": 4.38, "post": 5.02, "three1": 6.02, "at3": 6.82, "chair": 7.88, "so": 8.66, "whistle": 9.56, "i2": 10.32, "hand": 11.04, "eyes": 11.86, "pool": 12.14, "mostly": 12.94, "then1": 13.66, "dropped": 14.14, "deep": 15.1, "went": 15.92, "thePost": 17.0, "up": 18.16, "neither": 18.82, "found": 19.78, "foundG": 20.52, "farm": 21.24, "film": 22.36, "once": 22.84, "upload": 23.4, "original": 23.94, "gkPosts": 24.82, "phones": 26.36, "notFrom": 27.28, "no": 28.38, "n1": 28.58, "n2s": 29.4, "n2": 29.5, "nob": 30.68, "nobHit": 30.84, "at3b": 31.78, "i3": 32.46, "whistle2": 33.06, "habit": 33.68, "everyone": 34.5, "out": 35.0, "end": 35.84, "dur": 40.84}
def whistle(d=0.45):
    n = int(d * SR); t = np.arange(n) / SR; f = 2900 * (1 + 0.035 * np.sin(2 * np.pi * 28 * t)); s = np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.25 * np.convolve(rng.standard_normal(n), np.ones(6) / 6, 'same')
    e = np.ones(n); a = int(0.02 * SR); e[:a] = np.linspace(0, 1, a); e[-a * 3:] = np.linspace(1, 0, a * 3); return s * e
def splash(d=0.7, big=1.0):
    n = int(d * SR); s = rng.standard_normal(n); s = s - np.convolve(s, np.ones(8) / 8, 'same'); return (s * np.exp(-np.linspace(0, 6 / big, n)) + thud(110, d) * 0.6 * big) * 0.8
def roomtone(d):
    n = int(d * SR); s = np.convolve(rng.standard_normal(n), np.ones(400) / 400, 'same') * 8; return s
def muffled(d):
    n = int(d * SR); t = np.arange(n) / SR; s = np.sin(2 * np.pi * 70 * t) * 0.5 + np.convolve(rng.standard_normal(n), np.ones(300) / 300, 'same') * 10
    e = np.ones(n); r = int(0.2 * SR); e[:r] = np.linspace(0, 1, r); e[-r:] = np.linspace(1, 0, r); return s * e
def bubble(): return slide(300 + rng.random() * 300, 900 + rng.random() * 500, 0.06)
def tick(): return np.pad(click()[:300], (0, 900)) * 0.8 + tone(3200, 0.025, 30) * 0.3
def tap(): return np.pad(click()[:400], (0, 1520)) * 0.7 + tone(2400, 0.04, 30) * 0.2
def echo(sig, delay=0.11, g=0.35, n=4):
    out = np.zeros(len(sig) + int(delay * SR * n)); 
    for k in range(n + 1): i = int(delay * SR * k); out[i:i + len(sig)] += sig * (g ** k)
    return out
pool_on = [(0, T['thePost']), (T['found'], DUR)]
for a, b in pool_on: add(a, roomtone(b - a), 0.012)
for i in range(10): add(0.4 + i * 3.1, echo(splash(0.3, 0.4)), 0.02)
add(T['part'], thud(120, 0.2), 0.14); add(T['guard'], pop(520), 0.04)
add(T['brand'], whoosh(0.3), 0.22)
for at in [T['brand'] + 0.1, T['post'], T['three1']]: add(at, pop(560), 0.05)
add(T['at3'], whoosh(0.3), 0.2)
for i in range(4): add(T['at3'] - 0.3 + i * 0.25, tick(), 0.05)
add(T['at3'] + 0.15, thunk(), 0.2); add(T['at3'] + 0.15, ding(1046.5, 0.5), 0.04)
add(T['chair'], whoosh(0.25), 0.15); add(T['so'], whoosh(0.25), 0.15)
for i in range(6): add(T['so'] + 0.1 + i * 0.09, tap(), 0.03)
add(T['whistle'] - 0.1, echo(whistle(0.55)), 0.09)
add(T['i2'], whoosh(0.25), 0.15)
for i in range(8): add(T['hand'] + i * 0.11, tap(), 0.025)
add(T['mostly'], echo(splash(0.5, 0.6)), 0.12); add(T['mostly'] + 0.5, echo(splash(0.5, 0.6)), 0.1)
add(T['then1'], whoosh(0.3), 0.2); add(T['dropped'] + 0.15, slide(900, 300, 0.5), 0.04); add(T['dropped'] + 0.75, echo(splash(0.6, 0.7)), 0.2)
add(T['went'], whoosh(0.3), 0.2); add(T['went'] + 0.2, whoosh(0.6), 0.25); add(T['went'] + 0.9, echo(splash(0.9, 1.4)), 0.32)
add(T['thePost'], muffled(T['found'] - T['thePost']), 0.05)
for i in range(16): add(T['thePost'] + 0.15 + i * 0.17 + rng.random() * 0.06, bubble(), 0.02)
add(T['up'], stampS(), 0.25); add(T['up'], thud(80, 0.35), 0.2)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['farm'], whoosh(0.3), 0.26); add(T['film'], pop(620), 0.04); add(T['upload'], whoosh(0.25), 0.18); add(T['upload'] + 0.05, pop(560), 0.04)
add(T['original'], click(), 0.15); add(T['original'] + 0.02, ding(1318.5, 0.4), 0.04)
add(T['gkPosts'], whoosh(0.25), 0.18)
for i in range(18): add(T['gkPosts'] + 0.2 + (T['phones'] + 0.4 - T['gkPosts']) * i / 18, tone(700 + i * 45, 0.06, 12), 0.02)
add(T['phones'] - 0.4, ding(1046.5, 0.4), 0.04); add(T['notFrom'], pop(660), 0.05)
for at in [T['n1'] + 0.15, T['n2'] + 0.15]: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['at3b'], whoosh(0.3), 0.2)
for i in range(3): add(T['at3b'] - 0.2 + i * 0.25, tick(), 0.05)
add(T['at3b'] + 0.15, thunk(), 0.2)
add(T['whistle2'] - 0.12, echo(whistle(0.7)), 0.11)
for i in range(4): ts = T['habit'] - 0.15 + i * 0.16; add(ts + 0.1, echo(splash(0.35, 0.5)), 0.06); add(ts + 0.6, thud(200, 0.08), 0.06)
for i in range(6): add(T['everyone'] + i * 0.2, thud(240, 0.06), 0.03)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
