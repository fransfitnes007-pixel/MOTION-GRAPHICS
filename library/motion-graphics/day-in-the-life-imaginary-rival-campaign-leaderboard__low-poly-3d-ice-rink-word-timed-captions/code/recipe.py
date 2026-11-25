#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4,
take 1, sped 1.3x) plus synthesised sounds on the demo's timeline (the T block in demo.html) on an
empty ice rink at night: a big-room hum, skate scrapes, a cardboard thump, a crowd of one. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 41.28
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(141)
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
T = {"part": 2.52, "alone": 3.72, "aloneHit": 3.94, "team": 4.88, "beat": 6.04, "build": 6.82, "rival": 7.74, "name": 8.54, "brendaN": 9.06, "brendaP": 9.96, "five": 10.78, "never": 11.96, "portugal": 14.26, "cardboard0": 15.3, "cardHit": 15.9, "made": 17.22, "winning": 18.6, "found": 19.64, "foundG": 20.32, "campaign": 21.2, "board": 22.06, "real": 23.12, "views": 24.54, "hiHit": 25.98, "fourth": 26.94, "threeHit": 27.96, "iPosted": 29.26, "twice": 29.58, "no": 30.8, "n1": 30.96, "n2s": 31.6, "n2": 31.76, "nob": 32.6, "nobHit": 32.68, "brendaS": 33.74, "firstHit": 35.52, "and": 18.04, "end": 36.28, "dur": 41.28}
def scrape(d=0.6): n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(8) / 8, 'same') * np.sin(np.linspace(0, np.pi, n)) ** 1.5 * 0.8
def marker(d=0.8): n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(3) / 3, 'same') * (0.5 + 0.5 * np.sin(np.linspace(0, d * 40, n))) * 0.4
def flap(): return np.concatenate([thud(200, 0.08), np.zeros(200)]) * 0.8 + 0
add(0, hum(DUR, 60), 0.012)
for i in range(int(DUR / 1.7)): add(0.4 + i * 1.7, scrape(0.6), 0.02)
add(T['part'], thud(120, 0.2), 0.14)
for at in [T['aloneHit'], T['team'], T['beat']]: add(at, pop(520), 0.04)
add(T['beat'] + 0.2, tone(330, 0.6, 3, (1, 0.3)), 0.03)
add(T['build'], marker(0.9), 0.05); add(T['rival'], thud(160, 0.2), 0.12)
add(T['brendaN'], ding(1318.5, 0.4), 0.04)
add(T['brendaP'], whoosh(0.3), 0.26)
for at in [T['five'], T['never'], T['portugal']]: add(at - 0.1, marker(0.45), 0.05)
add(T['cardboard0'], whoosh(0.3), 0.2); add(T['cardHit'], thud(200, 0.12), 0.15); add(T['made'], marker(0.4), 0.05)
add(T['and'], scrape(1.0), 0.12); add(T['and'] + 0.1, whoosh(0.5), 0.15)
add(T['winning'], thud(90, 0.5), 0.3); add(T['winning'] + 0.05, stampS(), 0.25); add(T['winning'] + 0.1, scrape(0.5), 0.1)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['campaign'], whoosh(0.3), 0.26)
for k in range(5): add(T['board'] + 0.1 + k * 0.08, tone(880 + k * 110, 0.12, 10), 0.02)
for at in [T['real'], T['views'], T['hiHit']]: add(at, pop(620), 0.05)
add(T['fourth'], ding(1046.5, 0.4), 0.05); add(T['threeHit'], ding(1318.5, 0.5), 0.05)
add(T['twice'] - 0.1, scrape(1.0), 0.12); add(T['twice'], ding(1568, 0.6), 0.07); add(T['twice'] + 0.08, ding(2093, 0.5), 0.05)
for at in [T['n1'] + 0.2, T['n2'] + 0.12]: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['brendaS'], scrape(0.8), 0.08); add(T['firstHit'], tone(523.3, 0.5, 4, (1, 0.5)), 0.04); add(T['firstHit'] + 0.12, tone(659.3, 0.6, 4, (1, 0.5)), 0.04)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
