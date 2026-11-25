#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4,
take 1, sped 1.26x) plus synthesised sounds on the demo's timeline (the T block in demo.html) at a barn
wedding: crowd murmur, glass clinks, a soft three-four hum under the first dance, camera shutters, a whoosh for the bouquet,
a splat for the cake, notification pings. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.94
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(49)
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
T = {"part": 2.4, "sis": 3.78, "married": 4.28, "im": 5.34, "brides": 5.6, "a1": 6.54, "owes": 6.94, "me1": 7.2, "answer": 7.5, "checked": 8.42, "vows": 9.42, "speeches": 10.2, "speechW": 10.42, "dance": 11.28, "danceW": 11.66, "photo": 12.44, "photoW": 13.0, "then1": 13.82, "threw": 14.16, "bouquet": 14.44, "was": 15.16, "checking": 15.46, "caught": 16.6, "caughtW": 16.7, "face": 17.22, "then2": 18.02, "cake": 18.32, "caughtMe": 18.52, "found": 19.38, "foundG": 20.1, "notif": 21.12, "bell": 22.34, "grouped": 23.2, "camp": 23.98, "content": 24.46, "approved": 25.76, "dmA": 26.58, "dm": 26.94, "tells": 27.72, "dont": 28.56, "check": 28.86, "no": 29.4, "n1": 29.6, "n2s": 30.42, "n2": 30.62, "nob": 31.9, "nobHit": 32.1, "sis2": 33.1, "framed": 33.42, "its": 34.84, "hallway": 35.14, "end": 35.94, "dur": 40.94}
def murmur(d):
    n = int(d * SR); x = np.convolve(rng.standard_normal(n), np.ones(220) / 220, 'same') * 14
    return x * (0.75 + 0.25 * np.sin(2 * np.pi * 0.7 * np.arange(n) / SR))
def clink(): return tone(2637, 0.4, 9, (1, 0.5, 0.2)) + np.pad(tone(3520, 0.3, 12), (0, int(0.4 * SR) - int(0.3 * SR))) * 0.4
def shutter(): return np.concatenate([click()[:900] * 0.8, np.zeros(1600), click()[:700] * 0.6])
def splat(d=0.5):
    n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(60) / 60, 'same') * np.exp(-np.linspace(0, 6, n)) * 7 + thud(70, d) * 0.7
def ping(): return tone(1568, 0.5, 7, (1, 0.3)) + np.pad(tone(2093, 0.42, 8), (int(0.08 * SR), 0))[:int(0.5 * SR)] * 0.7
def waltz(t0, t1):
    for i in range(int((t1 - t0) / 0.42)):
        f = [196, 261.6, 261.6][i % 3] * (1 if (i // 3) % 2 == 0 else 0.89); add(t0 + i * 0.42, tone(f, 0.4, 5, (1, 0.4, 0.15)), 0.035 if i % 3 == 0 else 0.022)
add(0, murmur(T['found']), 0.05)
for at in [0.6, 1.9, 4.5, 9.0]: add(at, clink(), 0.02)
add(T['part'], thud(120, 0.2), 0.14)
add(T['sis'], whoosh(0.3), 0.2); add(T['married'], ding(1046.5, 0.5), 0.03)
add(T['im'], whoosh(0.3), 0.18); add(T['brides'], pop(520), 0.04)
add(T['a1'], whoosh(0.3), 0.24)
for at in [T['a1'] + 0.05, T['owes'], T['me1']]: add(at, pop(600), 0.05)
add(T['answer'], buzz(0.25), 0.05)
for at in [T['checked'], T['speeches'], T['dance'], T['photo']]: add(at, whoosh(0.25), 0.18)
for at in [T['vows'], T['speechW'], T['danceW'], T['photoW']]: add(at, pop(560), 0.05)
add(T['speeches'] + 0.1, slide(900, 2400, 0.25), 0.012)
waltz(T['dance'], T['photo'])
for f in [T['photo'] + 0.08, T['photo'] + 0.5, T['photoW'], T['photoW'] + 0.42]: add(f, shutter(), 0.12)
add(T['then1'], whoosh(0.3), 0.2); add(T['bouquet'], whoosh(0.9), 0.3)
add(T['caught'], whoosh(0.4), 0.2); add(T['caughtW'], thud(160, 0.25), 0.35); add(T['caughtW'], stampS(), 0.22)
add(T['cake'], whoosh(0.4), 0.25); add(T['caughtMe'], splat(0.6), 0.32); add(T['caughtMe'] + 0.02, stampS(), 0.2)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['notif'], whoosh(0.3), 0.26); add(T['bell'], ping(), 0.06)
add(T['grouped'], slide(400, 800, 0.2), 0.04)
for at in [T['camp'], T['content']]: add(at, pop(620), 0.05)
add(T['approved'], ding(1318.5, 0.6), 0.06); add(T['dmA'], ping(), 0.05)
add(T['tells'], whoosh(0.3), 0.2); add(T['tells'] + 0.4, thud(220, 0.1), 0.12)
waltz(T['dont'], T['no'])
for at in [T['n1'] + 0.15, T['n2'] + 0.12]: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['sis2'], whoosh(0.3), 0.22); add(T['framed'], pop(700), 0.05); add(T['framed'] + 0.3, pop(560), 0.04); add(T['its'], pop(700), 0.05); add(T['hallway'], ding(1568, 0.4), 0.03)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
