#!/usr/bin/env python3
"""Mixes the reel's soundtrack: the TTS voiceover (voiceover.wav, voice A (women), Eleven v4, sped 1.244x, take 1)
plus synthesised sounds on the demo's timeline (the T block in demo.html) over a quiet train: a low rumble and the
da-dum of wheels on rail joints. No music.
Usage: python3 recipe.py out.wav"""
import sys, os
import numpy as np, soundfile as sf
SR = 48000; DUR = 40.75
here = os.path.dirname(os.path.abspath(__file__))
vp = os.path.join(here, 'voiceover.wav')  # your own take, 48 kHz; effects only without it
vo, sr = sf.read(vp) if os.path.exists(vp) else (np.zeros(SR), SR); assert sr == SR
if vo.ndim > 1: vo = vo.mean(1)
mix = np.zeros(int(SR * DUR)); mix[:len(vo)] += vo[:len(mix)] / max(np.abs(vo).max(), 1e-9) * 0.9
rng = np.random.default_rng(83)
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
def clunk(f=220): return tone(f, 0.12, 6, (1, 0.6, 0.3))
def tick(f=1500): return tone(f, 0.035, 3) * 0.8
def shutter(): return np.concatenate([click() * 1.2, np.zeros(int(0.045 * SR)), click() * 0.9])        # a camera
def rumble(d):                                                                     # the carriage, a long way under the voice
    n = int(d * SR); return np.convolve(rng.standard_normal(n), np.ones(420) / 420, 'same') * 14
T = dict(part=2.28, kit=3.5, kitHit=4.3, none=5.24, noneHit=5.7, make=6.48, makeHit=6.86, hours=7.72, hoursHit=7.88, font=8.5, fontHit=8.88,
         p1=9.7, p1Hit=9.94, me=10.6, laugh=10.85, saladHit=11.44, p2=12.18, statsHit=13.06, shots=14.06, stale=14.7, staleHit=15.38,
         pages=16.28, pagesHit=16.58, reply=17.3, replyHit=17.5, just=18.2, threeHit=18.7,
         found=19.96, foundG=20.62, prof=21.62, profHit=21.76, line=23.6, lineHit=23.76, top=24.7, topHit=25.02, views=25.9, viewsHit=26.12, tracked=26.86,
         disc=27.44, discHit=27.98, inv=29.02, invHit=29.74, n=[30.98, 31.7], nobHit=32.44, rec=33.2, that=34.16, notHit=34.8, funnyHit=35.06, end=35.75)
bed = rumble(T['end'] + 0.6); bed[-SR:] *= np.linspace(1, 0, SR); bed[:SR // 2] *= np.linspace(0, 1, SR // 2); add(0, bed, 0.022)
at = 0.35
while at < T['end']:                                                              # da-dum ... da-dum over the rail joints
    add(at, thud(95, 0.12), 0.035); add(at + 0.16, thud(85, 0.12), 0.03); at += 1.37
add(T['part'], thud(120, 0.2), 0.14)
add(T['kit'], whoosh(0.35), 0.3); add(T['kit'] + 0.1, ding(1568, 0.4), 0.05); add(T['kitHit'], thud(140, 0.3), 0.26); add(T['kitHit'] + 0.02, pop(600), 0.07)
add(T['none'], whoosh(0.3), 0.25); add(T['noneHit'], thud(150, 0.4), 0.3); add(T['noneHit'] + 0.03, slide(520, 250, 0.4), 0.06)
add(T['make'], whoosh(0.3), 0.25); add(T['makeHit'], ding(1046.5, 0.4), 0.06); add(T['makeHit'] + 0.1, ding(1318.5, 0.5), 0.06)
add(T['hours'], whoosh(0.35), 0.3)
for i in range(int((T['fontHit'] - T['hours']) / 0.083)): add(T['hours'] + 0.05 + i * 0.083, tick(900 + (i * 137) % 700), 0.04)   # a font per tick
add(T['hoursHit'], thud(140, 0.3), 0.22); add(T['fontHit'], thud(150, 0.45), 0.32); add(T['fontHit'] + 0.02, buzz(0.4), 0.1)
add(T['p1'], whoosh(0.35), 0.3); add(T['p1Hit'], pop(560), 0.07)
for i in range(5): add(T['laugh'] + i * 0.1, pop(700 + (i % 2) * 160), 0.045)                                                        # ha ha ha
add(T['saladHit'], shutter(), 0.4); add(T['saladHit'] + 0.03, ding(1760, 0.5), 0.06); add(T['saladHit'] + 0.3, thud(140, 0.3), 0.2)
add(T['p2'], whoosh(0.35), 0.3)
for k in ['statsHit', 'shots']: add(T[k], shutter(), 0.36)
add(T['shots'] + 0.18, shutter(), 0.36)
for i in range(3): add(T['stale'] + i * 0.14, clunk(240 - i * 20), 0.14)
add(T['staleHit'], thud(150, 0.45), 0.32); add(T['staleHit'] + 0.02, buzz(0.45), 0.11)
add(T['pages'], whoosh(0.35), 0.3)
for i in range(14): add(T['pages'] + 0.02 + i * 0.045, whoosh(0.08), 0.13)                                                           # pages landing
add(T['pagesHit'] + 0.25, thud(140, 0.3), 0.24)
add(T['reply'], whoosh(0.3), 0.26); add(T['replyHit'], ding(1318.5, 0.4), 0.06); add(T['just'], pop(520), 0.07)
add(T['threeHit'], thud(150, 0.45), 0.34); add(T['threeHit'] + 0.02, buzz(0.45), 0.11); add(T['threeHit'] + 0.35, slide(520, 240, 0.45), 0.07)
add(T['found'], whoosh(0.7), 0.4)
for k, f in enumerate([261.6, 329.6, 392, 523.3, 659.3]): add(T['foundG'] + k * 0.035, tone(f, 2.0, 4), 0.055)
add(T['prof'], whoosh(0.35), 0.3); add(T['profHit'], ding(1046.5, 0.45), 0.07); add(T['profHit'], thud(130, 0.18), 0.12)
for i in range(13): add(T['lineHit'] - 0.08 + i * 0.058 + (0.015 if i % 3 else 0), click(), 0.12)
for i in range(3): add(T['topHit'] - 0.08 + i * 0.12, whoosh(0.14), 0.14); add(T['topHit'] + i * 0.12, ding(1046.5 * 2 ** (i * 2 / 12), 0.4), 0.065)
add(T['viewsHit'], pop(560), 0.07); add(T['viewsHit'] + 0.05, slide(420, 1100, 0.6), 0.04); add(T['tracked'], ding(1760, 0.5), 0.07)
add(T['disc'], whoosh(0.3), 0.26); add(T['discHit'], click(), 0.45); add(T['discHit'] + 0.04, ding(1318.5, 0.4), 0.07); add(T['discHit'] + 0.14, ding(1760, 0.5), 0.07)
add(T['inv'], whoosh(0.3), 0.26); add(T['inv'] + 0.1, ding(1568, 0.45), 0.06); add(T['invHit'], click(), 0.4); add(T['invHit'] + 0.03, ding(2093, 0.5), 0.06)
for at in T['n']: add(at, whoosh(0.3), 0.35); add(at, thud(130, 0.22), 0.2)
add(T['nobHit'], thud(130, 0.4), 0.3)
add(T['rec'], whoosh(0.3), 0.26); add(T['that'], whoosh(0.3), 0.26); add(T['notHit'], thud(150, 0.45), 0.32); add(T['notHit'] + 0.02, buzz(0.4), 0.1)
add(T['funnyHit'] + 0.26, tone(2400, 0.3, 7, (1, 0.5)), 0.09); add(T['funnyHit'] + 0.3, click(), 0.25)                               # the fork tips over
add(T['end'] - 0.2, whoosh(0.5), 0.35)
for k, f in enumerate([261.6, 392, 523.3, 784]): add(T['end'] + 0.1 + k * 0.03, tone(f, 3.4, 4), 0.06)
mix = np.tanh(mix * 1.05); mix *= 0.89 / np.abs(mix).max(); mix[-SR // 2:] *= np.linspace(1, 0, SR // 2)
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'sound.wav', np.stack([mix, mix], 1), SR, subtype='PCM_16')
