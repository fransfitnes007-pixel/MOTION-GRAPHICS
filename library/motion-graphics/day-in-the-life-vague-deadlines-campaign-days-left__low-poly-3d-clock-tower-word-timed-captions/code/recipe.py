#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men), Eleven v4,
take 1, sped 1.13x) plus synthesised sounds on the demo's timeline (the T block in demo.html) inside a
clock tower: ticking, turning gears, a pendulum, a chiming bell, chat pops. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.8
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(140)
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
T = {"part": 2.42, "brand": 3.34, "weekHit": 4.9, "whose": 5.74, "which": 6.4, "asked": 7.1, "asap": 8.26, "rush": 10.06, "eod": 10.98, "whoseDay": 12.12, "clockHit": 13.54, "knowHit": 14.88, "posted": 15.52, "friday": 15.82, "meant": 16.82, "tuesday": 17.0, "found": 17.94, "foundG": 18.58, "campaign": 19.28, "dates": 20.36, "four": 21.76, "threeHit": 23.66, "counts": 25.22, "iPosted": 26.16, "monday": 26.48, "early": 27.54, "firstHit": 28.14, "no": 29.5, "n1": 29.72, "n2s": 30.68, "n2": 30.82, "nob": 31.7, "nobHit": 31.84, "still": 32.72, "saysHit": 34.0, "just": 34.64, "numberHit": 35.1, "end": 35.8, "dur": 40.8}
def tick(f=2600): n = int(0.025 * SR); return np.sin(2 * np.pi * f * np.arange(n) / SR) * np.exp(-np.linspace(0, 9, n))
def bell(f=392, d=2.5): return tone(f, d, 3, (1, 0.6, 0.35, 0.2, 0.12))
def grind(d): n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(120) / 120, 'same') * 6 * (0.6 + 0.4 * np.sin(np.linspace(0, d * 18, n)))
# the tower ticks all the way through; faster while the hands spin
for i in range(int(DUR * 2)): at = i * 0.5; add(at, tick(2600 if i % 2 else 2200), 0.03 if not (T['whoseDay'] < at < T['posted']) else 0.0)
for i in range(int((T['posted'] - T['clockHit']) / 0.06)): add(T['clockHit'] + i * 0.06, tick(3000), 0.03)
add(0, grind(DUR), 0.008)
add(T['part'], thud(120, 0.2), 0.14)
for at in [T['brand'], T['asked'], T['posted'], T['still']]: add(at, whoosh(0.3), 0.22)
for at in [T['brand'] + 0.15, T['asap'], T['rush'], T['eod'], T['meant'], T['still'] - 0.1, T['saysHit']]: add(at, pop(560), 0.05)
add(T['asked'], pop(760), 0.04); add(T['posted'] + 0.1, pop(760), 0.04)
add(T['weekHit'], buzz(0.3, 80), 0.05)
for at in [T['whose'], T['which']]: add(at, slide(300, 520, 0.3), 0.05)
add(T['whoseDay'], whoosh(0.5), 0.25); add(T['clockHit'], bell(392, 2.2), 0.08); add(T['knowHit'], buzz(0.35, 70), 0.05)
add(T['tuesday'], thud(90, 0.5), 0.3); add(T['tuesday'] + 0.05, stampS(), 0.25); add(T['tuesday'], grind(0.9), 0.05)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['campaign'], whoosh(0.3), 0.26)
for k in range(3): add(T['campaign'] + 0.3 + k * 0.12, tone(880 + k * 220, 0.15, 10), 0.02)
add(T['dates'], pop(620), 0.06); add(T['four'], ding(1046.5, 0.4), 0.05); add(T['threeHit'], ding(1318.5, 0.4), 0.05); add(T['counts'] + 0.45, click(), 0.15); add(T['counts'] + 0.45, tick(1800), 0.1)
add(T['monday'], ding(1318.5, 0.5), 0.05); add(T['early'], ding(1568, 0.6), 0.07); add(T['early'] + 0.08, ding(2093, 0.5), 0.05); add(T['firstHit'], bell(523.3, 1.6), 0.05)
for at in [T['n1'] + 0.2, T['n2'] + 0.12]: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['just'] + 0.2, slide(300, 260, 0.3), 0.03); add(T['numberHit'], ding(1318.5, 0.4), 0.05)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
add(T['end'] + 0.1, bell(261.6, 3.5), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
