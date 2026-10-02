# -*- coding: utf-8 -*-
"""결론 구간 재교체 v5 — 「필터가 모든 걸」부터 끝까지를 새 리테이크로 바꾼다. (크레딧 0)

  python splice-s57v5.py

  구  「…오래된 집에 산다면, 샤워기에 필터 하나쯤은 달아 두셔도 좋습니다.」 (retake 2026-09-22)
  신  「…오래된 집에 살거나 녹물이 자주 나오는 곳이라면, 녹을 거르기 위한 필터 하나쯤은 달아 두셔도 좋습니다.
       그리고 염소가 아토피 피부의 수분 보유 능력을 떨어뜨렸다는 실험이 있습니다. 피부가 예민해서 수돗물의
       염소를 줄이고 싶다면, 시험 성적이 있는 비타민 씨 필터를 고르시길 권합니다.」  (retake-s57-v5.txt)

  마스터(구 splice-s57)를 310.36에서 자른다 — s57과 같은 지점(「증거입니다.」 뒤 쉼 310.035~310.424 안).
  리테이크는 말 시작(0.122) 65ms 앞부터 → 이음매 쉼 0.39초 = 원래 쉼 0.39초.

  두 판을 만든다 (사용자가 이음매를 듣고 고른다)
    raw  보정 없음
    fit  속도 보정 atempo 0.906 + 음량 −1.0dB  — 리테이크가 본문보다 빨라서(7.78 vs 7.05자/초 · 비 1.10) 맞춘 것
         (S08에서 tempo 1.10을 건 것과 같은 크기의 차이)
"""
import json, os, subprocess
os.chdir(os.path.dirname(os.path.abspath(__file__)))
MASTER = "MiniMax_2026-09-22_splice-s57.wav"
RETAKE = "MiniMax_2026-10-01_12_35_17_Cheerful_Cool_Junior.wav"
CUT_IN = 310.36
R_IN = 0.057                       # 말 시작 0.122 − 65ms

def run(*a): subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", *a], check=True)
def dur(f): return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
    "-of", "csv=p=0", f], capture_output=True, text=True, check=True).stdout.strip())

res = {}
for tag, rt_filter in (("raw", ""), ("fit", ",atempo=0.906,volume=-1.0dB")):
    out = f"MiniMax_2026-10-01_splice-v5-{tag}.wav"
    run("-i", MASTER, "-i", RETAKE, "-filter_complex",
        f"[0:a]atrim=0:{CUT_IN},afade=t=out:st={CUT_IN-0.01}:d=0.01[a];"
        f"[1:a]atrim={R_IN},asetpts=PTS-STARTPTS{rt_filter},aresample=32000,afade=t=in:d=0.01[b];"
        "[a][b]concat=n=2:v=0:a=1[o]", "-map", "[o]", "-ac", "1", "-ar", "32000", "-c:a", "pcm_s16le", out)
    run("-ss", str(CUT_IN - 5), "-i", out, f"seam-v5-{tag}.wav")
    res[tag] = {"out": out, "total": round(dur(out), 3), "delta": round(dur(out) - dur(MASTER), 3)}
print(json.dumps(res, ensure_ascii=False, indent=1))
