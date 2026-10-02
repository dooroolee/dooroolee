# -*- coding: utf-8 -*-
"""숫자 오독 두 구간을 리테이크로 바꾼다. (크레딧 0)

  python splice-numbers.py

  마스터    MiniMax_2026-10-02_12_42_58_Cheerful_Cool_Junior.wav (272.86초 · 사용자 생성 · 1.2배속)
  리테이크  MiniMax_2026-10-02_12_48_21_Cheerful_Cool_Junior.wav (18.81초) — 두 문장 묶음
    A  「피자 가게에서 1,700번 가까이 … 검출되지 않았습니다.」   마스터 전사 「일 700번」 ← 천칠백을 「일 칠백」으로 읽었다
    B  「올해 7월, 국가기술표준원과 … 관련됐다고 발표했습니다.」  사용자 청취로 지적

  경계는 전부 silencedetect(−40dB · 0.1초) 쉼 안에서 자른다. 쉼 길이는 «원래 마스터의 쉼»을 그대로 둔다
    앞 쉼  마스터를 쉼 끝 65ms 앞에서 자르고 · 리테이크를 말 시작 65ms 앞부터  → 앞 쉼 = 원래 길이
    뒤 쉼  리테이크를 말 끝 150ms 뒤까지 · 마스터를 쉼 시작 150ms 뒤부터       → 뒤 쉼 = 원래 길이
  보정 없음 — 음량 차 0.3~0.4 LU(A −20.5/−20.8 · B −21.0/−21.4) · 속도 A 1.01 · B 1.04 (ep01은 1.10에서 보정했다)
"""
import json, os, subprocess
os.chdir(os.path.dirname(os.path.abspath(__file__)))
MASTER = "MiniMax_2026-10-02_12_42_58_Cheerful_Cool_Junior.wav"
RETAKE = "MiniMax_2026-10-02_12_48_21_Cheerful_Cool_Junior.wav"
OUT = "MiniMax_2026-10-02_splice-numbers.wav"
PRE, POST = 0.065, 0.150

# (마스터 앞 쉼 끝, 마스터 뒤 쉼 시작, 리테이크 말 시작, 리테이크 말 끝)
BLOCKS = {
    "A": (96.163, 101.906, 0.119, 5.917),
    "B": (200.878, 212.638, 6.343, 18.616),
}

def run(*a): subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", *a], check=True)
def dur(f): return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
    "-of", "csv=p=0", f], capture_output=True, text=True, check=True).stdout.strip())

# 마스터 조각과 리테이크 조각을 번갈아 잇는다
pieces, t = [], 0.0
for k, (m_in, m_out, r_in, r_out) in BLOCKS.items():
    pieces.append((0, t, m_in - PRE))
    pieces.append((1, r_in - PRE, r_out + POST))
    t = m_out + POST
pieces.append((0, t, None))

fc, labels = [], []
for i, (src, a, b) in enumerate(pieces):
    trim = f"atrim={a}" + (f":{b}" if b is not None else "")
    fade_out = f",afade=t=out:st={b - a - 0.01}:d=0.01" if b is not None else ""
    fc.append(f"[{src}:a]{trim},asetpts=PTS-STARTPTS,afade=t=in:d=0.01{fade_out}[p{i}]")
    labels.append(f"[p{i}]")
fc.append("".join(labels) + f"concat=n={len(pieces)}:v=0:a=1[o]")
run("-i", MASTER, "-i", RETAKE, "-filter_complex", ";".join(fc),
    "-map", "[o]", "-ac", "1", "-ar", "32000", "-c:a", "pcm_s16le", OUT)

# 이음매 청취용 발췌 — 각 블록 앞 3초 ~ 뒤 3초
res, shift = {"out": OUT, "total": round(dur(OUT), 3), "delta": round(dur(OUT) - dur(MASTER), 3)}, 0.0
for k, (m_in, m_out, r_in, r_out) in BLOCKS.items():
    s = m_in + shift
    shift += (r_out - r_in) - (m_out - m_in)
    e = m_out + shift
    run("-ss", str(s - 3), "-to", str(e + 3), "-i", OUT, f"seam-{k}.wav")
    res[k] = {"new_in": round(s, 3), "new_out": round(e, 3), "len_change": round((r_out - r_in) - (m_out - m_in), 3)}
print(json.dumps(res, ensure_ascii=False, indent=1))
