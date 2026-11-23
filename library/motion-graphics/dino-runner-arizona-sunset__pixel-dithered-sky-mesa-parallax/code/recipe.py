#!/usr/bin/env python3
"""Mixes the soundtrack: a voiceover (voiceover.wav, your own recording, sped 1.18x) plus
synthesised game sounds on the demo's timeline (the T block in demo.html).  Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40
PART2 = 19.32; WALL = 35.5
here = os.path.dirname(os.path.abspath(__file__))
vo, sr = sf.read(os.path.join(here, 'voiceover.wav')); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(SR * DUR); mix[:len(vo)] += vo[:len(mix)] / np.abs(vo).max() * 0.9
def add(at, sig, g=1.0):
    i = int(at * SR); sig = sig[:len(mix) - i]; mix[i:i + len(sig)] += sig * g
def blip(f0, f1, d):
    n = int(d * SR); f = np.geomspace(f0, f1, n); return np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * np.exp(-np.linspace(0, 5, n))
def thud():
    n = int(0.3 * SR); r = np.random.default_rng(3).standard_normal(n); return (np.sin(2 * np.pi * np.cumsum(np.geomspace(140, 45, n)) / SR) + 0.4 * r) * np.exp(-np.linspace(0, 7, n))
JUMPS1 = [6.7, 7.92]; HITS = [12.76, 14.95, 16.15, 17.2, 17.54, 17.92, 18.34]
J2 = []; t = PART2 + 0.75; i = 0
while t < WALL - 0.5: J2.append(t); t += 0.74 - 0.012 * min(i, 8); i += 1
for j in JUMPS1: add(j - 0.28, blip(520, 880, 0.12), 0.10)
for h in HITS: add(h, thud(), 0.22); add(h, blip(300, 120, 0.25), 0.07)
n = int(0.8 * SR); sw = np.random.default_rng(5).standard_normal(n) * np.sin(np.linspace(0, np.pi, n)) ** 2
add(PART2 - 0.25, np.convolve(sw, np.ones(40) / 40, 'same'), 0.5)
for k, j in enumerate(J2): add(j - 0.28, blip(620, 1040, 0.09), 0.06); add(j + 0.1, blip(1320 * 2 ** ((k % 5) / 12), 1320 * 2 ** ((k % 5) / 12), 0.12), 0.035)
for k, f in enumerate([261.6, 392, 523.3, 784]): m = int(3.5 * SR); add(WALL + k * 0.03, np.sin(2 * np.pi * f * np.arange(m) / SR) * np.exp(-np.linspace(0, 4, m)), 0.07)
add(WALL, thud(), 0.3)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
