#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, take 1, sped 1.1x) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet
parked car on a rooftop deck: faint city traffic under everything. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 37.5
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(130)
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
def traffic(d):
    n = int(d * SR); s = np.convolve(rng.standard_normal(n), np.ones(400) / 400, 'same') * 8
    t = np.arange(n) / SR; return s * (0.7 + 0.3 * np.sin(2 * np.pi * 0.11 * t))
def cash(): return tone(2093, 0.25, 9, (1, 0.5, 0.3))
T = dict(part=2.46, make=3.36, oneHit=3.58, pay=4.56, telHit=5.0, hashHit=6.18, scrHit=7.3, pitchHit=9.34, today=10.22, fourHit=11.08, r=[12.64, 13.1, 13.8, 14.56],
         apps=15.22, didHit=17.08, found=17.7, foundG=18.5, tools=19.34, alrHit=19.84, picks=[20.98, 21.66, 22.3], menu=23.2, campHit=23.94, cancel=24.8, threeHit=25.22,
         n=[26.66, 27.56], nobHit=28.36, still=29.0, telHit2=29.92, cant=30.9, btnHit=31.42, end=32.5)
add(0, traffic(T['end'] + 1), 0.012)
add(T['part'], thud(120, 0.2), 0.14); add(T['oneHit'], ding(1318.5, 0.4), 0.05)
for k in ['pay', 'today', 'tools', 'menu', 'cancel', 'cant']: add(T[k], whoosh(0.3), 0.26); add(T[k] + 0.05, pop(540), 0.06)
for k in ['telHit', 'hashHit', 'scrHit', 'pitchHit']: add(T[k], pop(620), 0.06); add(T[k] + 0.05, cash(), 0.04)
add(T['pitchHit'] + 0.12, tone(220, 0.35, 5, (1, 0.5)), 0.07)
add(T['fourHit'], vib(0.4), 0.06)
for i, at in enumerate(T['r']): add(at, stampS(), 0.22); add(at + 0.04, cash(), 0.05); add(at + 0.02, vib(0.25), 0.05)
add(T['apps'], whoosh(0.25), 0.2); add(T['didHit'], slide(500, 160, 0.45), 0.07); add(T['didHit'] + 0.25, thud(120, 0.35), 0.25)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['alrHit'], ding(1318.5, 0.5), 0.05)
for i, at in enumerate(T['picks']): add(at, pop(600 + i * 80), 0.06)
add(T['campHit'], ding(1568, 0.5), 0.05)
for i in range(3): add(T['threeHit'] + i * 0.12, slide(700, 350, 0.15), 0.05)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['still'], whoosh(0.25), 0.2); add(T['telHit2'], cash(), 0.05)
add(T['btnHit'], tone(220, 0.4, 5, (1, 0.5)), 0.08)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
