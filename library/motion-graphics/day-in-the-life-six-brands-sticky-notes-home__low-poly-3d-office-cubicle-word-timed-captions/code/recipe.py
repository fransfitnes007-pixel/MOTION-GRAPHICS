#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, sped 1.1x, take 1) plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 39.1
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(41)
def add(at, sig, g=1.0):
    i = int(at * SR); sig = sig[:len(mix) - i]; mix[i:i + len(sig)] += sig * g
def tone(f, d, dec=5.0, harm=(1.0,)):
    n = int(d * SR); t = np.arange(n) / SR; return sum(a * np.sin(2 * np.pi * f * (k + 1) * t) for k, a in enumerate(harm)) * np.exp(-np.linspace(0, dec, n))
def thud(f0=140, d=0.3):
    n = int(d * SR); return (np.sin(2 * np.pi * np.cumsum(np.geomspace(f0, 45, n)) / SR) + 0.35 * rng.standard_normal(n)) * np.exp(-np.linspace(0, 7, n))
def whoosh(d=0.5):
    n = int(d * SR); return np.convolve(rng.standard_normal(n) * np.sin(np.linspace(0, np.pi, n)) ** 2, np.ones(48) / 48, 'same')
def ding(f=1318.5, d=0.9): return tone(f, d, 6, (1, 0.35, 0.12))
def buzz(d=0.35):
    n = int(d * SR); t = np.arange(n) / SR; return np.sign(np.sin(2 * np.pi * 92 * t)) * np.exp(-np.linspace(0, 3, n)) * 0.6
def click(): n = int(0.03 * SR); return rng.standard_normal(n) * np.exp(-np.linspace(0, 8, n))
def slide(f0, f1, d=0.35):
    n = int(d * SR); return np.sin(2 * np.pi * np.cumsum(np.geomspace(f0, f1, n)) / SR) * np.sin(np.linspace(0, np.pi, n))
def pop(f=520): return slide(f, f * 1.9, 0.09)                                    # a message bubble
def slap(g=1.0):                                                                # a sticky note going on
    n = int(0.07 * SR); return (rng.standard_normal(n) * np.exp(-np.linspace(0, 9, n)) + 0.6 * np.sin(2 * np.pi * 240 * np.arange(n) / SR) * np.exp(-np.linspace(0, 12, n))) * g
def flutter(d=1.2):                                                                # forty notes letting go at once
    n = int(d * SR); s = np.convolve(rng.standard_normal(n), np.ones(14) / 14, 'same') * np.sin(np.linspace(0, np.pi, n)) ** 0.5 * (0.5 + 0.5 * np.sin(np.linspace(0, 90, n)) ** 2); return s
def hum(d, f=100):
    n = int(d * SR); t = np.arange(n) / SR; return (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * f * 3 * t) + 0.4 * np.convolve(rng.standard_normal(n), np.ones(220) / 220, 'same')) * np.minimum(1, np.linspace(0, 8, n)) * np.minimum(1, np.linspace(8, 0, n))
T = dict(part=2.24, six=3.56, sixHit=4.04, each=5.22, eachHit=5.9, think=7.0, thinkHit=7.1, note=8.02, some=9.38, a=[(10.26, 10.68), (11.86, 12.38), (13.4, 14.34)], neverHit=15.12, miss=15.9, missHit=16.38, forgot=17.16, forgotHit=17.84,
         found=19.16, foundG=19.85, home=20.74, homeHit=21.16, next=21.8, nextHit=22.3, live=23.12, liveHit=23.5, ppdHit=24.86, cardHit=25.68, today=26.28, todayHit=26.8, n=[28.0, 29.08], nob=29.98,
         cb=31.02, cbHit=31.48, checkHit=32.58, notesHit=33.16, end=34.1)
add(0.0, hum(T['found'] + 0.6), 0.03)
add(T['part'], thud(120, 0.2), 0.14)
add(T['six'], whoosh(0.3), 0.25); add(T['sixHit'], thud(130, 0.22), 0.18)
for i in range(6): add(T['sixHit'] - 0.2 + i * 0.07, pop(440 + i * 50), 0.045)
add(T['each'], whoosh(0.35), 0.3)
for i in range(6): add(T['each'] + 0.08 + i * 0.07, click(), 0.14); add(T['eachHit'] + i * 0.06, slide(420, 560, 0.08), 0.04)
add(T['think'], whoosh(0.25), 0.2); add(T['thinkHit'], slide(520, 300, 0.35), 0.07); add(T['thinkHit'], thud(130, 0.25), 0.2)
add(T['note'], whoosh(0.3), 0.25)
for i in range(15): add(T['note'] + 0.08 + i * 0.086, slap(), 0.1 + (i % 3) * 0.02)
add(T['some'] + 0.13, slap(1.4), 0.3); add(T['some'] + 0.15, thud(150, 0.3), 0.26)
for i, (a, h) in enumerate(T['a']): add(a, whoosh(0.25), 0.25); add(a + 0.14, slap(), 0.22); add(h, thud(140, 0.25), 0.2); add(h, tone([660, 587, 494][i], 0.25, 3, (1, 0.4)), 0.06)
add(T['neverHit'], thud(150, 0.45), 0.32); add(T['neverHit'] + 0.02, buzz(0.4), 0.1)
add(T['miss'], whoosh(0.35), 0.3); add(T['missHit'], tone(880, 0.12, 3), 0.08); add(T['missHit'] + 0.1, tone(880, 0.12, 3), 0.08); add(T['missHit'], thud(150, 0.4), 0.3); add(T['missHit'] + 0.45, tone(660, 0.12, 3), 0.07); add(T['missHit'] + 0.55, tone(660, 0.12, 3), 0.07)
add(T['forgot'], whoosh(0.25), 0.2); add(T['forgotHit'], slide(500, 220, 0.45), 0.09); add(T['forgotHit'], thud(130, 0.4), 0.3)
add(T['found'], whoosh(0.7), 0.4); add(T['found'] + 0.4, slap(0.8), 0.12)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
for i in range(4): add(T['home'] + 0.1 + i * 0.07, pop(520 + i * 60), 0.05)
add(T['homeHit'], ding(1318.5, 0.5), 0.07)
add(T['next'], whoosh(0.35), 0.3)
for i in range(2): add(T['nextHit'] + i * 0.16, ding(1046.5 * 2 ** (i * 2 / 12), 0.35), 0.06)
add(T['nextHit'] + 0.4, ding(1568, 0.6), 0.07); add(T['nextHit'] + 0.4, thud(130, 0.2), 0.16)
add(T['live'], whoosh(0.25), 0.2)
for i in range(2): add(T['liveHit'] - 0.05 + i * 0.14, pop(560 + i * 80), 0.07)
add(T['ppdHit'], ding(1318.5, 0.5), 0.07); add(T['cardHit'], ding(2093, 0.6), 0.07); add(T['cardHit'], thud(130, 0.22), 0.18)
add(T['today'], whoosh(0.3), 0.25); add(T['today'] + 0.05, flutter(1.3), 0.2); add(T['todayHit'], ding(1568, 0.6), 0.07)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['cb'], whoosh(0.35), 0.3); add(T['cb'] + 0.2, slap(1.2), 0.22); add(T['cbHit'], ding(1318.5, 0.4), 0.06)
add(T['checkHit'], thud(140, 0.3), 0.24); add(T['notesHit'], thud(150, 0.4), 0.3); add(T['notesHit'] + 0.3, thud(150, 0.4), 0.32); add(T['notesHit'] + 0.32, slide(500, 240, 0.45), 0.08)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
