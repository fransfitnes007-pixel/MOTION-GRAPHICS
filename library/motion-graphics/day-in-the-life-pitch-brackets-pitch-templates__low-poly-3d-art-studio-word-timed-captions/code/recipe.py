#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, sped 1.214x, take 2)
plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.75
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(61)
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
def swoosh_mail(): return np.concatenate([whoosh(0.3) * 0.8, tone(1568, 0.25, 6) * 0.25])                           # an email leaving
def clunk(f=220): return tone(f, 0.12, 6, (1, 0.6, 0.3))                                                              # a bracket landing
def tick(f=1500): return tone(f, 0.035, 3) * 0.8
T = dict(part=2.3, pitch=3.68, pitchHit=4.2, wrote=5.14, hiHit=6.08, hourHit=8.62, tmpl=9.48, tmplHit=10.32, hey=11.5, brandHit=12.08, loved=12.82, prodHit=13.42, yearHit=14.0, sentHit=15.02, brk=15.7, brkHit=15.98, eleven=16.68, elevenHit=16.88,
         found=18.4, foundG=19.0, three=19.98, threeHit=20.28, writes=21.64, writesHit=22.04, give=23.2, g=[23.7, 24.4, 25.2], get=26.02, out=[26.42, 27.32, 28.1, 28.96], n=[30.2, 31.14], nob=31.98, reply=32.96, replyHit=33.66, hi=34.6, nameHit=35.06, end=35.75)
add(T['part'], thud(120, 0.2), 0.14)
add(T['pitch'], whoosh(0.3), 0.25); add(T['pitchHit'], ding(1318.5, 0.5), 0.07)
add(T['wrote'], whoosh(0.35), 0.3)
for i in range(22): add(T['hiHit'] + i * 0.068 + (0.25 if i > 3 else 0) + (0.3 if i > 10 else 0), click(), 0.13)                 # slow, careful typing
for i in range(int((T['hourHit'] - T['hiHit']) / 0.2)): add(T['hiHit'] + i * 0.2, tick(1300 + i * 20), 0.03)
add(T['hourHit'], thud(150, 0.45), 0.32); add(T['hourHit'] + 0.02, buzz(0.4), 0.1)
add(T['tmpl'], whoosh(0.35), 0.3)
for k in range(4): add(T['tmplHit'] + k * 0.09, tone(1400 + 300 * (k % 2), 0.07, 2), 0.035)                                        # a tacky jingle
add(T['hey'], pop(520), 0.07); add(T['brandHit'], clunk(240), 0.14); add(T['loved'], pop(560), 0.07); add(T['prodHit'], clunk(220), 0.14); add(T['yearHit'], clunk(200), 0.15)
add(T['sentHit'], click(), 0.4); add(T['sentHit'] + 0.03, swoosh_mail(), 0.35)
add(T['brk'], whoosh(0.3), 0.28); add(T['brkHit'], thud(150, 0.45), 0.34); add(T['brkHit'] + 0.02, buzz(0.45), 0.11)
for i in range(11): add(T['eleven'] + 0.05 + (i / 11) ** 0.8 * 0.72, swoosh_mail(), 0.12 + i * 0.006)
add(T['elevenHit'] + 0.55, thud(150, 0.4), 0.3); add(T['elevenHit'] + 0.6, slide(520, 240, 0.4), 0.07)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['three'], whoosh(0.4), 0.3)
for i in range(3): add(T['threeHit'] - 0.08 + i * 0.13, whoosh(0.14), 0.14); add(T['threeHit'] + i * 0.13, ding(1046.5 * 2 ** (i * 2 / 12), 0.4), 0.065)
add(T['writes'], pop(600), 0.07); add(T['writesHit'], click(), 0.4); add(T['writesHit'] + 0.03, ding(1760, 0.5), 0.07)
add(T['give'], whoosh(0.3), 0.25)
for i, at in enumerate(T['g']): add(at, pop(500 + i * 70), 0.07); [add(at + 0.04 + j * 0.05, click(), 0.1) for j in range(5)]
add(T['get'], whoosh(0.35), 0.28)
for i, at in enumerate(T['out']): add(at - 0.08, whoosh(0.14), 0.14); add(at, ding([1046.5, 1174.7, 1318.5, 1568][i], 0.45), 0.07); add(at, thud(130, 0.18), 0.12)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['reply'], whoosh(0.35), 0.3); add(T['replyHit'], ding(1318.5, 0.4), 0.07); add(T['replyHit'] + 0.1, ding(1760, 0.5), 0.07)
add(T['hi'], pop(520), 0.07); add(T['nameHit'], clunk(200), 0.18); add(T['nameHit'] + 0.02, thud(150, 0.45), 0.32); add(T['nameHit'] + 0.3, slide(520, 240, 0.45), 0.08)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
