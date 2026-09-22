# -*- coding: utf-8 -*-
"""결론 세 문장 교체 — 리테이크본을 2화 VO 마스터 끝에 붙인다. (크레딧 0)

  python splice-s57.py

  구  「노후 배관의 부스러기를 개인이 차단할 수 있는 마지막 물리적 안전망이라고 볼 수 있지만
       필요 없다고 느낀다면, 쓰지 않아도 괜찮습니다. 선택은, 이제 여러분의 몫입니다.」
  신  「필터가 모든 걸 해결해 주지는 않습니다. 하지만 노후 배관에서 떨어져 나온 부스러기라면
       이야기가 다릅니다. 오래된 집에 산다면, 샤워기에 필터 하나쯤은 달아 두셔도 좋습니다.」
      ← 「선택은 여러분의 몫」이 「쓰라는 거야 말라는 거야?」로 끝나서 판단 기준을 주고 끝낸다 (2026-09-22)

하는 일
  1. 마스터를 「증거입니다.」 뒤 쉼(310.035~310.424) 안 310.36에서 자른다
     — 바꾸는 문장이 파일 끝까지라 뒤쪽은 붙이지 않는다
  2. 리테이크를 말 시작(0.125) 65ms 앞부터 끝까지 붙인다 → 이음매 쉼 0.39초 = 원래 쉼 0.39초
  3. 속도·음량은 손대지 않는다 — S08(tempo 1.10 · −1.1dB)과 달리 실측이 같다
       음절 속도  구 68음절 / 9.65초 = 7.05자/초 · 신 71음절 / 9.98초 = 7.11자/초 (비 1.01)
       음량       구 구간 −20.5 LUFS · 리테이크 −20.5 LUFS
  4. 새 마스터와 이음매 발췌본(이음매 5초 앞 ~ 끝)을 만든다. 기존 파일은 지우지 않는다
"""
import json, os, subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))
MASTER = "MiniMax_2026-09-19_splice-s08.wav"
RETAKE = "MiniMax_2026-09-22_23_43_50_Cheerful_Cool_Junior.wav"
OUT = "MiniMax_2026-09-22_splice-s57.wav"
CUT_IN = 310.36                         # 마스터: 「증거입니다.」 끝 310.035 · 다음 말 시작 310.424
R_IN = 0.06                             # 리테이크: 말 시작 0.125 에서 65ms 여유 · 끝(10.28)까지 쓴다

def run(*a): subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", *a], check=True)
def dur(f): return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
    "-of", "csv=p=0", f], capture_output=True, text=True, check=True).stdout.strip())

run("-i", MASTER, "-i", RETAKE, "-filter_complex",
    f"[0:a]atrim=0:{CUT_IN},afade=t=out:st={CUT_IN-0.01}:d=0.01[a];"
    f"[1:a]atrim={R_IN},asetpts=PTS-STARTPTS,aresample=32000,afade=t=in:d=0.01[b];"
    "[a][b]concat=n=2:v=0:a=1[o]", "-map", "[o]", "-ac", "1", "-ar", "32000", "-c:a", "pcm_s16le", OUT)
run("-ss", str(CUT_IN - 5), "-i", OUT, "seam-s57.wav")
total = dur(OUT)
print(json.dumps({"out": OUT, "total": round(total, 3), "delta": round(total - dur(MASTER), 3),
                  "seam_at": CUT_IN, "retake_offset": round(CUT_IN - R_IN, 3)}, ensure_ascii=False))
