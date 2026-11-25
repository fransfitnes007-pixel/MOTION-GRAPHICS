#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, sped 1.18x) plus
synthesised sounds on the demo's timeline (the T block in demo.html). No music.  Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(SR * DUR); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(4)
def add(at, sig, g=1.0):
    i = int(at * SR); sig = sig[:len(mix) - i]; mix[i:i + len(sig)] += sig * g
def tone(f, d, dec=5.0, harm=(1.0,)):
    n = int(d * SR); t = np.arange(n) / SR; return sum(a * np.sin(2 * np.pi * f * (k + 1) * t) for k, a in enumerate(harm)) * np.exp(-np.linspace(0, dec, n))
def blip(f0, f1, d):
    n = int(d * SR); f = np.geomspace(f0, f1, n); return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-np.linspace(0, 5, n))
def thud(f0=140, d=0.3):
    n = int(d * SR); return (np.sin(2 * np.pi * np.cumsum(np.geomspace(f0, 45, n)) / SR) + 0.35 * rng.standard_normal(n)) * np.exp(-np.linspace(0, 7, n))
def whoosh(d=0.5):
    n = int(d * SR); return np.convolve(rng.standard_normal(n) * np.sin(np.linspace(0, np.pi, n)) ** 2, np.ones(48) / 48, 'same')
def ding(f=1318.5, d=0.9): return tone(f, d, 6, (1, 0.35, 0.12))
def buzz(d=0.35):
    n = int(d * SR); t = np.arange(n) / SR; return np.sign(np.sin(2 * np.pi * 92 * t)) * np.exp(-np.linspace(0, 3, n)) * 0.6
T = dict(wake=2.64, pitch=3.54, zero=4.74, yesHit=7.44, want=8.76, make=9.88, warm=11.04, ban=12.74, film=13.56, rev=[15.07, 15.89, 16.85], ghost=18.04, fuck=19.88,
         found=20.88, foundG=21.6, acctHit=23.06, joinHit=24.04, no=[25.14, 26.12, 27.28], steps=[28.78, 29.64, 30.36, 31.64], doneHit=32.54, nob=33.38, end=35.72)
for k in range(4): add(T['wake'] - 0.5 + k * 0.14, tone(1760, 0.07, 2), 0.05)                      # alarm
for i in range(12): add(T['pitch'] + 0.08 + i * 0.065, whoosh(0.22), 0.10)                         # paper planes
add(T['zero'] + 0.3, buzz(0.3), 0.07)
add(T['yesHit'] - 0.05, ding(1318.5), 0.10); add(T['yesHit'] + 0.07, ding(1760), 0.08)
add(T['want'], thud(110, 0.25), 0.16)
add(T['make'], whoosh(0.35), 0.35)
for i in range(10): add(T['warm'] + i * 0.16, tone(900 + i * 25, 0.04, 3), 0.035)                  # days ticking
add(T['ban'], thud(150, 0.4), 0.32); add(T['ban'] + 0.02, buzz(0.45), 0.10)
add(T['film'] - 0.1, whoosh(0.3), 0.3)
for i, r in enumerate(T['rev']): add(r, thud(150 - i * 15, 0.3), 0.24 + i * 0.04); add(r, tone(2400, 0.03, 2), 0.06)
n = int(1.2 * SR); add(T['ghost'] + 0.15, np.sin(2 * np.pi * np.cumsum(np.linspace(380, 760, n) + 30 * np.sin(np.linspace(0, 40, n))) / SR) * np.sin(np.linspace(0, np.pi, n)) ** 2, 0.045)  # ghost
add(T['fuck'] + 0.08, thud(120, 0.45), 0.36)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.4, 4), 0.055)   # the G arrives
for at in (T['acctHit'], T['joinHit']): add(at, ding(1568, 0.5), 0.07)
for i, at in enumerate(T['no']): add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
for i, at in enumerate(T['steps']): add(at, ding(1046.5 * 2 ** (i * 2 / 12), 0.5), 0.075)
for k, f in enumerate([392, 523.3, 659.3, 784]): add(T['doneHit'] + k * 0.03, tone(f, 1.6, 4), 0.05)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
