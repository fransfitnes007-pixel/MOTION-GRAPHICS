#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, sped 1.1x, take 1) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet
lake at dawn: water lapping, a reel clicking each time a message is pulled up. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 38.3
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(113)
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
def lap(d):                                                                        # water against the dock, slow
    n = int(d * SR); t = np.arange(n) / SR; return np.convolve(rng.standard_normal(n), np.ones(180) / 180, 'same') * 9 * (0.3 + 0.7 * np.sin(2 * np.pi * t / 4.3) ** 2)
def reel(d=0.3):                                                                   # a fishing reel: fast ratchet clicks
    out = np.zeros(int(d * SR)); k = 0
    while k < len(out) - 400: c = click()[:400] * 0.7; out[k:k + 400] += c; k += int(SR * 0.022)
    return out * np.linspace(0.6, 1, len(out))
def plop(): return np.concatenate([slide(700, 260, 0.08), whoosh(0.16) * 0.5])
def fanfare(): return np.concatenate([tone(523.3, 0.12, 2, (1, 0.5, 0.3)), tone(659.3, 0.12, 2, (1, 0.5, 0.3)), tone(784, 0.3, 4, (1, 0.5, 0.3))])   # for a prince
T = dict(part=2.3, dm=3.6, dmHit=4.12, hello=5.62, helloHit=5.92, amb=6.6, ambHit=7.26, ship=8.14, shipHit=8.64, brief=9.4, briefHit=10.16, exe=10.86, exeHit=11.06,
         check=12.32, checkHit=13.06, big=13.66, bigHit=13.94, back=14.56, diffHit=15.0, prince=15.7, p1=16.0, princeHit=16.68, p3=17.08,
         found=17.62, foundG=18.28, inv=19.4, invHit=19.78, placeHit=20.68, read=21.46, dealHit=21.84, yesHit=22.66, sign=23.36, signHit=23.48, dec=24.36, decHit=24.84,
         team=25.4, teamHit=26.26, msgHit=26.88, n=[27.92, 28.88], nobHit=30.2, still=31.18, stillHit=31.7, well=32.36, wellHit=32.64, end=33.3)
bed = lap(T['end'] + 0.6); bed[-SR:] *= np.linspace(1, 0, SR); bed[:SR // 2] *= np.linspace(0, 1, SR // 2); add(0, bed, 0.022)
add(T['part'], thud(120, 0.2), 0.14)
for k in ['dm', 'brief', 'check', 'prince', 'still']: add(T[k], plop(), 0.12); add(T[k] + 0.04, reel(0.3), 0.1)                       # each message reeled in
add(T['helloHit'], pop(420), 0.08); add(T['helloHit'] + 0.03, thud(140, 0.3), 0.2)
add(T['ambHit'] - 0.2, pop(480), 0.07)
for k in range(4): add(T['ambHit'] + k * 0.09, tone(1400 + 300 * (k % 2), 0.07, 2), 0.03)                                             # a tacky jingle
add(T['ship'], pop(440), 0.06); add(T['shipHit'], thud(150, 0.45), 0.32); add(T['shipHit'] + 0.02, buzz(0.4), 0.1); add(T['shipHit'] + 0.08, ding(2093, 0.3), 0.04)
add(T['briefHit'], pop(560), 0.07); add(T['briefHit'] + 0.02, thud(130, 0.2), 0.14)
add(T['exe'], whoosh(0.3), 0.26); add(T['exeHit'], thud(150, 0.45), 0.34); add(T['exeHit'] + 0.02, buzz(0.5), 0.12)
for i in range(3): add(T['exeHit'] + 0.45 + i * 0.13, tone(880, 0.09, 2), 0.05)                                                        # an alarm, three beeps
add(T['checkHit'], whoosh(0.2), 0.16); add(T['checkHit'] + 0.04, ding(1568, 0.4), 0.05)
add(T['bigHit'], thud(150, 0.45), 0.32); add(T['bigHit'] + 0.02, buzz(0.4), 0.1); add(T['back'], pop(460), 0.07); add(T['diffHit'], thud(150, 0.4), 0.3); add(T['diffHit'] + 0.03, slide(520, 240, 0.45), 0.07)
add(T['p1'], pop(480), 0.07); add(T['princeHit'], fanfare(), 0.06); add(T['princeHit'], pop(520), 0.06); add(T['p3'], pop(400), 0.07); add(T['p3'] + 0.03, thud(140, 0.3), 0.2)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['inv'], whoosh(0.35), 0.3); add(T['invHit'], click(), 0.4); add(T['invHit'] + 0.03, ding(1318.5, 0.4), 0.06); add(T['placeHit'] - 0.2, whoosh(0.16), 0.16); add(T['placeHit'] - 0.1, ding(1568, 0.5), 0.07); add(T['placeHit'] - 0.1, thud(130, 0.2), 0.14)
add(T['read'], whoosh(0.35), 0.3)
for i in range(3): add(T['dealHit'] - 0.1 + i * 0.14, pop(520 + i * 60), 0.065)
add(T['yesHit'], ding(1760, 0.5), 0.07); add(T['signHit'], click(), 0.45); add(T['signHit'] + 0.03, ding(1318.5, 0.4), 0.07); add(T['signHit'] + 0.13, ding(1760, 0.5), 0.07)
add(T['decHit'], click(), 0.4); add(T['decHit'] + 0.03, tone(880, 0.3, 5), 0.06)
add(T['team'], whoosh(0.3), 0.26); add(T['team'] + 0.08, pop(620), 0.07); add(T['teamHit'], pop(520), 0.08); add(T['teamHit'] + 0.05, ding(1568, 0.5), 0.06); add(T['msgHit'], pop(560), 0.07)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['still'] + 0.15, pop(480), 0.07); add(T['stillHit'], pop(520), 0.07); add(T['stillHit'] + 0.02, fanfare(), 0.05); add(T['wellHit'] - 0.15, pop(440), 0.07); add(T['wellHit'] + 0.1, ding(1318.5, 0.5), 0.06); add(T['wellHit'] + 0.2, ding(1760, 0.6), 0.06)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
