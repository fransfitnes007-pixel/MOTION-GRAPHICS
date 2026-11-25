#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, sped 1.235x, take 1)
plus synthesised sounds on the demo's timeline (the T block in demo.html). No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.65
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(19)
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
def coins(d=0.5):                                                                  # a till: a few bright pings
    out = np.zeros(int(d * SR))
    for k, f in enumerate([2093, 2637, 3136]): s = tone(f, 0.3, 7, (1, 0.3)); i = int(k * 0.06 * SR); out[i:i + len(s)] += s[:len(out) - i]
    return out
def slide(f0, f1, d=0.35):                                                         # a falling or rising whistle
    n = int(d * SR); return np.sin(2 * np.pi * np.cumsum(np.geomspace(f0, f1, n)) / SR) * np.sin(np.linspace(0, np.pi, n))
T = dict(part=2.36, paidHit=3.7, almost=4.78, b1=5.76, appHit=6.92, feeHit=8.06, b2=8.7, invHit=9.72, tmplHit=10.76, b3=11.5, portalHit=12.66, forms=13.56, formsHit=14.02, letterHit=15.14,
         b4=15.78, cardHit=16.86, apps=17.66, appsHit=17.96, head=18.9, headHit=19.46, found=20.22, foundG=20.85, bank=21.88, bankHit=22.58, once=23.4, unlock=24.2, unlockHit=25.02, pressHit=26.24, apprHit=27.88, goesHit=29.34,
         n=[30.14, 31.2], nob=31.98, shampoo=32.78, dogHit=33.56, nodogHit=35.12, end=35.65)
add(T['part'], thud(120, 0.2), 0.14)
add(T['paidHit'], coins(), 0.07); add(T['paidHit'], thud(130, 0.2), 0.14)
add(T['almost'], slide(520, 180, 0.4), 0.08); add(T['almost'] + 0.05, buzz(0.4), 0.1); add(T['almost'], thud(140, 0.4), 0.28)
add(T['b1'], whoosh(0.35), 0.3); add(T['appHit'], coins(0.4), 0.06)
add(T['feeHit'] - 0.1, slide(700, 240, 0.3), 0.07); add(T['feeHit'] + 0.12, thud(150, 0.3), 0.26)
add(T['b2'], whoosh(0.35), 0.3)
for i in range(5): add(T['invHit'] + i * 0.1, click(), 0.16)
add(T['tmplHit'], buzz(0.4), 0.1); add(T['tmplHit'], thud(140, 0.3), 0.22)
add(T['b3'], whoosh(0.35), 0.3); add(T['portalHit'], tone(660, 0.14, 3), 0.06); add(T['portalHit'] + 0.1, tone(523.3, 0.2, 3), 0.06)
for i in range(13): add(T['forms'] + i * 0.07, click(), 0.12 + i * 0.006); add(T['forms'] + i * 0.07, tone(700 + i * 40, 0.05, 3), 0.025)
add(T['formsHit'] + 0.45, thud(120, 0.3), 0.2)
add(T['letterHit'], thud(150, 0.45), 0.34); add(T['letterHit'] + 0.02, buzz(0.5), 0.11)
add(T['b4'], whoosh(0.35), 0.3); add(T['cardHit'] - 0.3, slide(900, 300, 0.3), 0.06); add(T['cardHit'], thud(170, 0.2), 0.2); add(T['cardHit'] + 0.1, tone(392, 0.25, 3), 0.06); add(T['cardHit'] + 0.3, tone(311.1, 0.4, 3), 0.06)
add(T['apps'], whoosh(0.3), 0.3)
for i in range(5): add(T['appsHit'] - 0.05 + i * 0.11, tone(880 * 2 ** (i * 2 / 12), 0.12, 4), 0.06); add(T['appsHit'] - 0.05 + i * 0.11, click(), 0.12)
add(T['head'], whoosh(0.3), 0.25); add(T['headHit'], thud(150, 0.5), 0.34); add(T['headHit'], tone(3200, 1.0, 3), 0.012)      # the ringing in her ears
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
for i in range(8): add(T['bank'] + 0.12 + i * 0.085, click(), 0.14)
add(T['bankHit'] + 0.25, ding(1318.5, 0.5), 0.07)
add(T['once'], thud(130, 0.3), 0.26); add(T['once'], ding(1568, 0.6), 0.07)
add(T['unlock'], whoosh(0.4), 0.3); add(T['unlockHit'], click(), 0.35); add(T['unlockHit'] + 0.06, tone(1760, 0.25, 4), 0.07); add(T['unlockHit'] + 0.06, thud(160, 0.15), 0.14)
add(T['pressHit'], click(), 0.4); add(T['pressHit'] + 0.02, thud(110, 0.18), 0.2)
add(T['apprHit'] - 0.1, whoosh(0.18), 0.18); add(T['apprHit'], ding(1046.5, 0.5), 0.075)
add(T['goesHit'] - 0.1, whoosh(0.18), 0.18); add(T['goesHit'], ding(1318.5, 0.6), 0.075); add(T['goesHit'] + 0.08, coins(), 0.06)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nob'], thud(130, 0.4), 0.3)
add(T['shampoo'], whoosh(0.35), 0.3); add(T['dogHit'], tone(660, 0.1, 3), 0.06); add(T['dogHit'] + 0.1, tone(880, 0.14, 3), 0.06)       # a squeaky toy
add(T['nodogHit'], thud(150, 0.4), 0.3); add(T['nodogHit'] + 0.02, buzz(0.35), 0.09)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
