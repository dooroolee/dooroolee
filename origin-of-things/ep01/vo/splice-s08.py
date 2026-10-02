# -*- coding: utf-8 -*-
"""S08~S09 한 문장 교체 — 리테이크본을 2화 VO 마스터에 끼워 넣는다. (크레딧 0)

  python splice-s08.py [--tempo 1.10]

  구  「노랗게 변한 필터를 세로로 잘라 보면, 색은 바깥쪽에 몰려 있고 안쪽은 아직 하얗습니다.」
  신  「노랗게 변한 필터를 세로로 잘라 보면, 색은 물이 먼저 닿는 쪽에 몰려 있고 반대쪽은 아직 하얗습니다.」
      ← 손잡이형 필터는 물이 «안→밖»으로 흐른다는 설명이 있어 방향과 무관한 문장으로 바꿨다 (2026-09-19)

하는 일
  1. 마스터를 문장 앞 무음(40.95)과 문장 뒤 무음(45.90)에서 자른다 — 앞뒤 쉼은 원본 그대로 남는다
  2. 리테이크본의 앞뒤 무음을 털고 --tempo로 속도를 맞춘다 (음정 보존)
     1.10 = 같은 단어 구간 「노랗게…잘라 보면」 비 1.13 · 전체 음절 속도 비 1.07 의 중간
  3. 음량을 원래 문장 구간(−21.8 LUFS)에 맞춘다 (리테이크 −20.7 → −1.1dB)
  4. 이어 붙여 새 마스터와 이음매 발췌본(앞뒤 5초)을 만든다. 기존 파일은 지우지 않는다
"""
import subprocess, sys, json

MASTER = "MiniMax_2026-09-19_21_11_21_Cheerful_Cool_Junior.wav"
RETAKE = "MiniMax_2026-09-19_22_33_02_Cheerful_Cool_Junior.wav"
OUT = "MiniMax_2026-09-19_splice-s08.wav"
CUT_IN, CUT_OUT = 40.95, 45.90          # 마스터: 문장 앞 무음 · 문장 뒤 무음 안
R_IN, R_OUT = 0.11, 6.10                # 리테이크: 말 시작 0.14 · 끝 6.07 에서 30ms 여유
GAIN_DB = -1.1

def run(*a): subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", *a], check=True)
def dur(f): return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
    "-of", "csv=p=0", f], capture_output=True, text=True, check=True).stdout.strip())

tempo = float(sys.argv[sys.argv.index("--tempo") + 1]) if "--tempo" in sys.argv else 1.10
run("-i", MASTER, "-i", RETAKE, "-filter_complex",
    f"[0:a]atrim=0:{CUT_IN},afade=t=out:st={CUT_IN-0.01}:d=0.01[a];"
    f"[1:a]atrim={R_IN}:{R_OUT},asetpts=PTS-STARTPTS,atempo={tempo},volume={GAIN_DB}dB,"
    f"aresample=32000,afade=t=in:d=0.01[b];"
    f"[0:a]atrim={CUT_OUT},asetpts=PTS-STARTPTS,afade=t=in:d=0.01[c];"
    "[a][b][c]concat=n=3:v=0:a=1[o]", "-map", "[o]", "-ac", "1", "-ar", "32000", "-c:a", "pcm_s16le", OUT)
new_len = (R_OUT - R_IN) / tempo
delta = new_len - (CUT_OUT - CUT_IN)
run("-ss", str(CUT_IN - 5), "-t", str(new_len + 10), "-i", OUT, "seam-s08.wav")
print(json.dumps({"out": OUT, "total": round(dur(OUT), 3), "tempo": tempo,
                  "new_sentence": round(new_len, 3), "delta": round(delta, 3),
                  "shift_from": CUT_OUT}, ensure_ascii=False))
