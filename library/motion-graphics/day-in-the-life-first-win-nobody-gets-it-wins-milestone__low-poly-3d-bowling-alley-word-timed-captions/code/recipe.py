#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice B (men),
Eleven v4, sped 1.1x, take 1) plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet
bowling alley: a low room tone, a ball rolling now and then, pins a long way off. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 38.7
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(97)
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
def tick(f=1500): return tone(f, 0.035, 3) * 0.8
def room(d): n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(300) / 300, 'same') * 12
def roll(d=2.4):                                                                   # a ball going down a lane, far away
    n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(220) / 220, 'same') * 10 * np.sin(np.linspace(0, np.pi, n)) ** 0.6 * np.linspace(1, 0.5, n)
def pins():                                                                        # and what it hits
    out = np.zeros(int(0.7 * SR))
    for i in range(9): k = int((0.02 + rng.random() * 0.3) * SR); c = tone(700 + rng.random() * 900, 0.14, 7, (1, 0.5)); out[k:k + len(c)] += c * (0.5 + rng.random() * 0.5)
    return out
def horn(d=0.42):                                                                  # a party horn
    n = int(d * SR); t = np.arange(n) / SR; f = np.linspace(360, 520, n); return (np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * 0.5 + np.sin(2 * np.pi * np.cumsum(f * 2.01) / SR) * 0.4) * np.sin(np.linspace(0, np.pi, n)) ** 0.4
T = dict(part=2.3, hit=3.6, hitHit=4.44, kHit=5.2, first=6.1, firstHit=6.22, chat=7.12, chatHit=7.88, nice=8.66, niceHit=9.0, park=9.94, parkHit=10.66,
         room=11.4, roomHit=11.84, he=12.48, ofHit=12.82, whatHit=13.2, plant=13.88, plantHit=14.28, gets=14.88, getsHit=15.24, party=16.06, partyHit=16.4, att=17.24, meHit=17.96,
         found=18.66, foundG=19.2, mile=20.24, mileHit=21.0, wins=21.46, winsHit=22.26, handle=22.92, handleHit=23.46, net=24.2, seesHit=24.98, ppl=25.52, getHit=26.64,
         n=[27.72, 28.58], nobHit=29.68, still=30.44, stillHit=31.08, there=32.0, dayHit=32.84, end=33.7)
bed = room(T['end'] + 0.6); bed[-SR:] *= np.linspace(1, 0, SR); bed[:SR // 2] *= np.linspace(0, 1, SR // 2); add(0, bed, 0.02)
for at in [0.4, 6.9, 13.6, 21.8, 29.9]: add(at, roll(), 0.018); add(at + 2.3, pins(), 0.02)
add(T['part'], thud(120, 0.2), 0.14)
add(T['hit'], whoosh(0.35), 0.3)
for i in range(22): add(T['hit'] + 0.25 + (i / 22) ** 0.75 * (T['kHit'] - T['hit'] - 0.3), tick(900 + i * 40), 0.045)            # the counter climbing
add(T['kHit'], ding(1318.5, 0.6), 0.08); add(T['kHit'] + 0.08, ding(1760, 0.7), 0.08); add(T['kHit'] + 0.16, ding(2093, 0.8), 0.07); add(T['kHit'], thud(130, 0.3), 0.22)
add(T['first'], whoosh(0.3), 0.26); add(T['firstHit'], ding(1568, 0.5), 0.06)
add(T['chat'], whoosh(0.35), 0.3); add(T['chatHit'], pop(620), 0.08); add(T['niceHit'], pop(360), 0.07); add(T['niceHit'] + 0.03, thud(140, 0.3), 0.2)
add(T['park'], pop(420), 0.06); add(T['parkHit'], pop(440), 0.06); add(T['parkHit'] + 0.3, pop(460), 0.06); add(T['parkHit'] + 0.5, slide(520, 240, 0.45), 0.07)
add(T['room'], whoosh(0.35), 0.3); add(T['roomHit'], pop(620), 0.08); add(T['ofHit'], pop(380), 0.07); add(T['whatHit'], thud(150, 0.45), 0.34); add(T['whatHit'] + 0.02, buzz(0.45), 0.11); add(T['whatHit'] + 0.35, pop(420), 0.05)
add(T['plant'], whoosh(0.3), 0.26); add(T['plantHit'], pop(560), 0.06)
for i in range(4): add(T['gets'] + 0.1 + i * 0.12, whoosh(0.1), 0.1)                                                                   # leaves nodding
add(T['getsHit'], ding(1318.5, 0.5), 0.07)
add(T['party'], whoosh(0.3), 0.26); add(T['partyHit'], horn(0.45), 0.05); add(T['partyHit'] + 0.5, horn(0.36), 0.04); add(T['partyHit'], pop(700), 0.06)
add(T['meHit'], thud(150, 0.45), 0.32); add(T['meHit'] + 0.03, slide(480, 200, 0.6), 0.07)                                            # the horn giving up
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['mile'], whoosh(0.35), 0.3); add(T['mileHit'] - 0.06, pop(600), 0.07); add(T['mileHit'], ding(1318.5, 0.5), 0.07); add(T['mileHit'] + 0.1, ding(1760, 0.6), 0.07); add(T['mileHit'], thud(130, 0.2), 0.14)
add(T['winsHit'], ding(1568, 0.45), 0.07); add(T['winsHit'], thud(130, 0.18), 0.14); add(T['handleHit'], ding(2093, 0.5), 0.07); add(T['handleHit'], thud(130, 0.18), 0.16)
for i in range(5): add(T['seesHit'] - 0.06 + i * 0.09, pop(520 + i * 70), 0.065)
add(T['ppl'] + 0.15, pop(600), 0.07); add(T['getHit'] - 0.1, pop(660), 0.07); add(T['getHit'] + 0.15, ding(1760, 0.5), 0.07)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['still'], whoosh(0.3), 0.26); add(T['stillHit'], ding(1318.5, 0.5), 0.07)
add(T['there'], whoosh(0.3), 0.26)
for i in range(4): add(T['there'] + 0.2 + i * 0.17, whoosh(0.1), 0.09)
add(T['dayHit'], ding(1046.5, 0.6), 0.07); add(T['dayHit'] + 0.1, ding(1318.5, 0.6), 0.07); add(T['dayHit'] + 0.2, ding(1568, 0.8), 0.07)
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
