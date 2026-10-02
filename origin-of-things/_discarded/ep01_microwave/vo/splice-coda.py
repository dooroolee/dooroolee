# -*- coding: utf-8 -*-
"""코다 리테이크본을 1화 VO 마스터에 이어 붙인다. (크레딧 0)

  python splice-coda.py <코다.mp3> [--tempo 0.8202]

  --tempo   새 코다에 먼저 적용할 배속. 1.0이면 무보정.
            ★분할 생성은 템포가 달라진다★ — 짧게 보낸 판이 마스터보다 21.9% 빨랐다.
            0.8202는 동일 문장 2개를 실측해 맞춘 값이다.

하는 일
  1. (--tempo) 새 코다의 속도를 마스터에 맞춘다 (음정 보존)
  2. 기존 마스터를 ★482.25초★(블록 9 마지막 말끝)에서 자른다
  3. 새 코다의 앞뒤 무음을 털어낸다
  4. 사이에 ★1.14초★ 무음을 넣는다 (실측한 블록 경계 쉼과 같은 값)
  5. 이어 붙여 새 마스터 + atempo=1.2 배속본을 만든다
  6. 이음매 앞뒤만 잘라 «귀로 판정할» 발췌본을 뽑는다
기존 파일은 지우지 않는다.
"""
import subprocess, sys, os, re, datetime

SRC_MASTER = "hf_20260914_090931_30aadcfc-07b9-449d-ac19-bb4998a7e184.mp3"
CUT_AT, GAP = 482.25, 1.14
SEAM_PAD = 14.0   # 이음매 발췌본에서 앞뒤로 남길 초

def run(*a): subprocess.run(["ffmpeg","-hide_banner","-v","error","-y",*a], check=True)
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
    "-of","csv=p=0",f], capture_output=True, text=True, check=True).stdout.strip())

def speech_bounds(f, thr="-40dB", d=0.3):
    out = subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",f,"-af",
        f"silencedetect=n={thr}:d={d}","-f","null","-"], capture_output=True, text=True).stderr
    total = dur(f)
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    s = en[0] if en and (not st or en[0] < st[0]) else 0.0
    e = st[-1] if st and st[-1] > s and st[-1] > total - 3 else total
    return s, e

def build(coda, tempo, tag):
    # ★순서가 중요하다★ — 무음 제거는 «늘리기 전»에 한다.
    # 늘린 뒤에 재면 조용한 어미가 무음으로 잡혀 ★실제 말을 잘라낸다★ (2026-09-14에 실제로 겪음)
    s, e = speech_bounds(coda)
    print(f"  [{tag}] 코다 원본 {dur(coda):.2f}s · 발화 {s:.2f}~{e:.2f} ({e-s:.2f}s)")
    work = f"_coda_{tag}.wav"
    af = [] if abs(tempo - 1.0) < 1e-6 else ["-filter:a", f"atempo={tempo:.4f}"]
    run("-ss", str(s), "-to", str(e), "-i", coda, *af,
        "-c:a","pcm_s16le","-ar","44100","-ac","1", work)
    print(f"  [{tag}] 배속 {tempo:.4f} 적용 → {dur(work):.2f}s")

    run("-i", SRC_MASTER, "-t", str(CUT_AT), "-c:a","pcm_s16le","-ar","44100","-ac","1","_head.wav")
    run("-i", work, "-c","copy","_tail.wav")
    run("-f","lavfi","-t",str(GAP),"-i","anullsrc=r=44100:cl=mono","-c:a","pcm_s16le","_gap.wav")
    with open("_list.txt","w",encoding="utf-8") as fh:
        for p in ("_head.wav","_gap.wav","_tail.wav"): fh.write(f"file '{p}'\n")

    stamp  = datetime.date.today().strftime("%Y%m%d")
    master = f"ep01-vo-master-{stamp}-{tag}.mp3"
    run("-f","concat","-safe","0","-i","_list.txt","-c:a","libmp3lame","-b:a","192k", master)
    x120 = f"ep01-vo-x120-{tag}.mp3"
    run("-i", master, "-filter:a","atempo=1.2","-c:a","libmp3lame","-b:a","192k", x120)

    seam_at = CUT_AT / 1.2
    run("-ss", str(round(seam_at - SEAM_PAD, 2)), "-t", str(SEAM_PAD*2 + 4),
        "-i", x120, "-c:a","libmp3lame","-b:a","192k", f"SEAM-{tag}.mp3")

    for p in ("_head.wav","_tail.wav","_gap.wav","_list.txt", work): os.remove(p)
    d = dur(x120)
    print(f"  [{tag}] 마스터 {dur(master):.2f}s → 1.2배속 {d:.2f}s = {int(d//60)}분 {d%60:.1f}초")
    return master, x120

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    coda = sys.argv[1]
    tempo = 0.8202
    if "--tempo" in sys.argv: tempo = float(sys.argv[sys.argv.index("--tempo")+1])
    for f in (SRC_MASTER, coda):
        if not os.path.exists(f): sys.exit(f"없는 파일: {f}")
    print(f"코다 원본 {dur(coda):.2f}s")
    build(coda, tempo, "fit")   # 템포 보정본
    build(coda, 1.0,   "raw")   # 무보정본
    print("\n★ 이음매는 1.2배속본 기준 약 6분 42초 지점 — SEAM-fit.mp3 / SEAM-raw.mp3로 비교한다")
    print("★ 마스터가 496초를 넘는 것은 정상이다 — 천장은 «한 번의 생성»에만 걸린다")

if __name__ == "__main__": main()
