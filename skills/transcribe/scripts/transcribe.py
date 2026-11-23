#!/usr/bin/env python3
"""Local transcription with faster-whisper. Writes word-level JSON, SRT and TXT."""
import argparse, json, subprocess, sys, tempfile
from pathlib import Path


def srt_time(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--model", default="small")
    ap.add_argument("--lang", default=None)
    ap.add_argument("--device", default="auto")
    ap.add_argument("--out", default=".")
    a = ap.parse_args()

    from faster_whisper import WhisperModel

    src = Path(a.input)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as td:
        wav = Path(td) / "a.wav"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
                        "-vn", "-ac", "1", "-ar", "16000", str(wav)], check=True)
        model = WhisperModel(a.model, device=a.device, compute_type="int8" if a.device in ("cpu", "auto") else "float16")
        segs, info = model.transcribe(str(wav), language=a.lang, word_timestamps=True, vad_filter=True)
        words, srt, txt = [], [], []
        for i, s in enumerate(segs, 1):
            for w in (s.words or []):
                words.append({"word": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3)})
            srt.append(f"{i}\n{srt_time(s.start)} --> {srt_time(s.end)}\n{s.text.strip()}\n")
            txt.append(s.text.strip())

    (out / f"{src.stem}.words.json").write_text(json.dumps({"language": info.language, "words": words}, indent=2))
    (out / f"{src.stem}.srt").write_text("\n".join(srt))
    (out / f"{src.stem}.txt").write_text("\n".join(txt))
    print(f"language={info.language} words={len(words)} -> {out}")


if __name__ == "__main__":
    sys.exit(main())
