#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, sped 1.1x, take 1) plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 37.3
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(59)
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
def stampS(): return np.concatenate([thud(170, 0.12) * 1.2, np.zeros(int(0.02 * SR)), thud(110, 0.25)])           # a rubber stamp
def quill(d=0.35):                                                                 # a pen on paper
    n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(5) / 5, 'same') * np.sin(np.linspace(0, np.pi, n)) * (0.55 + 0.45 * np.sin(np.linspace(0, 70, n)))
def bell(): return tone(2093, 0.5, 6, (1, 0.4, 0.2)) + tone(2637, 0.5, 7, (0.6, 0.2))                                # the counter bell
T = dict(part=2.34, apply=3.64, applyHit=4.42, five=5.68, fiveHit=5.82, l=[(6.86, 7.54), (9.32, 9.9), (11.0, 11.66), (13.7, 14.48), (15.54, 16.38)], balmHit=12.76, found=17.56, foundG=18.25, deals=19.3, dealsHit=20.4, pressHit=22.34, revHit=23.4,
         newc=23.96, newHit=24.44, firstHit=25.56, n=[26.74, 27.92], nob=28.84, cb=29.58, cbHit=30.4, beautHit=31.6, end=32.3)
add(0.1, bell(), 0.03)
add(T['part'], thud(120, 0.2), 0.14)
for i in range(22): add(T['apply'] + 0.05 + i * 0.085, click(), 0.11)
add(T['applyHit'], thud(130, 0.2), 0.14)
add(T['five'], whoosh(0.35), 0.3)
for i in range(5): add(T['fiveHit'] - 0.1 + i * 0.09, pop(460 + i * 60), 0.065)
for i, (a, h) in enumerate(T['l']): add(a, whoosh(0.28), 0.3); add(a + 0.14, pop(500), 0.05); add(h, thud(140 + i * 4, 0.35), 0.26 + i * 0.015); add(h + 0.02, buzz(0.3), 0.07 + i * 0.008)
for i in range(14): add(T['l'][0][0] + 0.32 + i * 0.06, tone(700 + i * 50, 0.04, 3), 0.03)                                           # the applicant count climbing
add(T['balmHit'], stampS(), 0.3); add(T['balmHit'] + 0.1, slide(520, 260, 0.35), 0.07)
add(T['l'][3][1] - 0.02, stampS(), 0.3)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['deals'], whoosh(0.35), 0.28); add(T['deals'] + 0.3, ding(1318.5, 0.5), 0.06)
add(T['dealsHit'] - 0.12, whoosh(0.3), 0.25)
for i in range(2): add(T['dealsHit'] - 0.05 + i * 0.15, ding(1046.5 * 2 ** (i * 2 / 12), 0.4), 0.065)
add(T['pressHit'], click(), 0.45); add(T['pressHit'] + 0.02, thud(110, 0.16), 0.18); add(T['pressHit'] + 0.12, ding(1568, 0.5), 0.07)
add(T['revHit'], pop(600), 0.08); add(T['revHit'] + 0.05, ding(1760, 0.5), 0.06)
add(T['newc'], whoosh(0.4), 0.3); add(T['newc'] + 0.38, thud(140, 0.2), 0.16); add(T['newHit'], ding(2093, 0.5), 0.07); add(T['firstHit'], ding(1318.5, 0.5), 0.07); add(T['firstHit'], thud(130, 0.22), 0.18)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['cb'], whoosh(0.35), 0.3)
for i in range(6): add(T['cb'] + 0.15 + i * 0.1, quill(0.3), 0.12)
add(T['cbHit'], quill(0.4), 0.12); add(T['beautHit'] - 0.03, stampS(), 0.32); add(T['beautHit'] + 0.12, ding(1318.5, 0.5), 0.07); add(T['beautHit'] + 0.22, ding(1760, 0.6), 0.07)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
