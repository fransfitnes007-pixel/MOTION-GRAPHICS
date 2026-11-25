#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4,
take 1, sped 1.19x) plus synthesised sounds on the demo's timeline (the T block in demo.html) in a
karaoke booth: a backing track, off-key singing, a booth hum, a ring light, a score fanfare. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.98
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(139)
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
T = {"part": 2.58, "sing": 3.92, "singHit": 4.06, "badly": 5.74, "loudly": 6.78, "but": 7.54, "camHit": 8.26, "forget": 9.06, "engHit": 9.5, "take1": 10.62, "umHit": 11.88, "take2": 12.54, "cousinHit": 14.14, "minHit": 15.06, "take17": 15.98, "s17Hit": 16.1, "brandHit": 17.56, "wrongHit": 17.94, "twice": 18.9, "found": 19.78, "foundG": 20.6, "gen": 21.54, "hookHit": 22.84, "beatsHit": 23.42, "prodHit": 24.2, "know": 25.2, "exact": 25.44, "said": 26.52, "first": 27.88, "firstHit": 28.0, "no": 28.74, "n1": 28.88, "n2s": 29.52, "n2": 29.74, "nob": 30.48, "nobHit": 30.62, "karaoke": 31.4, "scoreHit": 33.24, "my": 34.38, "twelveHit": 35.22, "end": 35.98, "dur": 40.98}
def note(f, d, wob=0.0):
    n = int(d * SR); t = np.arange(n) / SR; ff = f * (1 + wob * np.sin(2 * np.pi * 3.1 * t)); ph = 2 * np.pi * np.cumsum(ff) / SR
    s = np.sin(ph) + 0.4 * np.sin(2 * ph) + 0.2 * np.sin(3 * ph); e = np.ones(n); r = min(n // 4, int(0.02 * SR)); e[:r] = np.linspace(0, 1, r); e[-r:] = np.linspace(1, 0, r); return s * e / 1.6
def backing(t0, t1, g):
    prog = [[130.8, 164.8, 196], [174.6, 220, 261.6], [196, 246.9, 293.7], [130.8, 164.8, 196]]; i = 0; t = t0
    while t < t1:
        for f in prog[i % 4]: add(t, note(f, 0.5), g / 3)
        add(t, thud(90, 0.15), g * 1.5); add(t + 0.25, click(), g * 0.6); t += 0.5; i += 1
def offkey(t0, t1, g):
    mel = [392, 440, 523.3, 494, 392, 349.2]; t = t0; i = 0
    while t < t1: add(t, note(mel[i % 6] * (1 + 0.06 * np.sin(i * 2.3)), 0.32, 0.03), g); t += 0.34; i += 1
add(0, hum(DUR, 50), 0.01)
add(T['part'], thud(120, 0.2), 0.14)
backing(T['sing'] - 0.1, T['but'], 0.05); offkey(T['sing'], T['but'], 0.05)
add(T['badly'], buzz(0.35, 70), 0.06)
for i in range(3): add(T['loudly'] + 0.05 + i * 0.12, note(587.3 * (1 + 0.08 * i), 0.3, 0.05), 0.09)
add(T['but'], whoosh(0.3), 0.2); add(T['camHit'], tone(1760, 0.15, 10), 0.05); add(T['camHit'] + 0.05, hum(0.6, 120), 0.03)
add(T['engHit'], slide(500, 200, 0.5), 0.05)
add(T['take1'], whoosh(0.3), 0.26); add(T['take1'] + 0.1, blip(), 0.06)
for k, at in enumerate([T['take1'], T['take2'], T['take17']]): add(at + 0.05, stampS(), 0.12)
add(T['umHit'], buzz(0.3, 80), 0.05)
for i in range(8): add(T['cousinHit'] + i * 0.12, click(), 0.03)
add(T['brandHit'], tone(220, 0.3, 4, (1, 0.5)), 0.05); add(T['wrongHit'], buzz(0.35, 70), 0.07)
add(T['twice'], thud(90, 0.5), 0.3); add(T['twice'] + 0.1, stampS(), 0.25)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['gen'], whoosh(0.3), 0.26)
for k in range(3): add(T['gen'] + 0.3 + k * 0.12, tone(880 + k * 220, 0.15, 10), 0.02)
for at in [T['hookHit'], T['beatsHit'], T['prodHit']]: add(at - 0.1, pop(620), 0.06)
add(T['know'], whoosh(0.3), 0.2); add(T['exact'], ding(1318.5, 0.4), 0.05); add(T['firstHit'], ding(1568, 0.6), 0.07); add(T['firstHit'] + 0.08, ding(2093, 0.5), 0.05)
for at in [T['n1'] + 0.2, T['n2'] + 0.12]: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['karaoke'], whoosh(0.3), 0.26)
for i in range(int((T['scoreHit'] - T['karaoke'] - 0.3) / 0.06)): add(T['karaoke'] + 0.3 + i * 0.06, tone(1200 + i * 15, 0.04, 12), 0.015)
for k, f in enumerate([523.3, 659.3, 784, 1046.5]): add(T['scoreHit'] + k * 0.09, note(f, 0.5), 0.08)
for i in range(12): add(T['scoreHit'] + 0.1 + rng.random() * 0.8, click(), 0.06)
backing(T['my'] - 0.1, T['end'], 0.05); offkey(T['my'], T['end'], 0.06); add(T['twelveHit'], buzz(0.35, 70), 0.06)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
