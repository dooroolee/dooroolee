#!/usr/bin/env python3
"""2화 샤워기 필터 — Flow 다운로드 정리 + 조립. 크레딧 0.

  python assemble.py ingest <zip 또는 폴더>   # Flow 다운로드 → clips/S01.mp4 … S58.mp4
  python assemble.py check                     # 58개 중 무엇이 있고 없는지 · 길이 부족 클립
  python assemble.py build [--sfx -20]         # scenes.json 순서로 잘라 붙이고 VO를 얹는다 → out/ep02_draft.mp4

- 클립은 앞에서부터 그 씬의 «쓸길이»만 쓴다. 다른 구간을 쓰려면 OFFSET에 적는다(초).
- 없는 클립은 씬 id를 쓴 검은 화면으로 채운다 — 생성 도중에도 전체 길이·흐름을 볼 수 있다.
- 클립 오디오(효과음)는 --sfx dB로 VO 밑에 깐다. VO는 트루피크 −1dB로 맞춘다(README).
"""
import json, os, re, shutil, subprocess, sys, tempfile, zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
CLIPS = os.path.join(ROOT, "clips")
OUT = os.path.join(ROOT, "out")
SCENES = json.load(open(os.path.join(ROOT, "scenes.json"), encoding="utf-8"))
VO = os.path.join(ROOT, SCENES["source_vo"])
W, H, FPS = 1920, 1080, 30

# 씬별 시작 오프셋(초) — 앞부분이 어색해 뒤쪽을 쓸 때만 적는다. 예: {"S14": 0.5}
OFFSET = {}


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        sys.exit(f"ffmpeg 실패:\n{' '.join(cmd)}\n{r.stderr[-2000:]}")
    return r.stdout


def duration(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                      "-of", "csv=p=0", path]).strip())


def has_audio(path):
    return bool(run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
                     "stream=index", "-of", "csv=p=0", path]).strip())


def ingest(src):
    os.makedirs(CLIPS, exist_ok=True)
    tmp = None
    if zipfile.is_zipfile(src):
        tmp = tempfile.mkdtemp()
        zipfile.ZipFile(src).extractall(tmp)
        src = tmp
    got, unresolved = {}, []
    for dirpath, _, files in os.walk(src):
        for f in sorted(files):
            if not f.lower().endswith(".mp4"):
                continue
            m = re.match(r"S(\d{1,2})(?:[_.\s]|$)", f)
            if not m:
                unresolved.append(f)
                continue
            sid = f"S{int(m.group(1)):02d}"
            got.setdefault(sid, []).append(os.path.join(dirpath, f))
    ids = [s["id"] for s in SCENES["scenes"]]
    for sid, paths in sorted(got.items()):
        dst = os.path.join(CLIPS, f"{sid}.mp4")
        if len(paths) > 1:
            print(f"⚠️ {sid} 후보 {len(paths)}개 — 가장 나중 이름을 쓴다: {[os.path.basename(p) for p in paths]}")
        if os.path.exists(dst):
            print(f"⚠️ {sid}.mp4 이미 있음 — 덮어쓴다")
        shutil.copy2(sorted(paths)[-1], dst)
    print(f"정리됨 {len(got)}개 · 씬 id 없는 파일 {len(unresolved)}개")
    for f in unresolved:
        print(f"  ? {f}")
    if unresolved:
        print("→ 위 파일은 이름에 씬 id가 없다. 어느 씬인지 알려주면 clips/Sxx.mp4로 넣는다")
    if tmp:
        shutil.rmtree(tmp, ignore_errors=True)
    check()


def check():
    missing, short = [], []
    for s in SCENES["scenes"]:
        p = os.path.join(CLIPS, f"{s['id']}.mp4")
        if not os.path.exists(p):
            missing.append(s["id"])
            continue
        need = s["len"] + OFFSET.get(s["id"], 0)
        d = duration(p)
        if d + 0.02 < need:
            short.append(f"{s['id']}({d:.2f}s < {need:.2f}s)")
    n = len(SCENES["scenes"])
    print(f"클립 {n - len(missing)}/{n}")
    if missing:
        print("없음: " + " ".join(missing))
    if short:
        print("길이 부족: " + " ".join(short))
    return missing


def build(sfx_db):
    os.makedirs(OUT, exist_ok=True)
    tmp = tempfile.mkdtemp()
    parts = []
    vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,"
          f"fps={FPS},format=yuv420p,setsar=1")
    for s in SCENES["scenes"]:
        sid, ln = s["id"], s["len"]
        p = os.path.join(CLIPS, f"{sid}.mp4")
        part = os.path.join(tmp, f"{sid}.mp4")
        if os.path.exists(p):
            a_in = ["-i", p] if has_audio(p) else ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
            a_map = "0:a" if has_audio(p) else "1:a"
            cmd = ["ffmpeg", "-y", "-ss", str(OFFSET.get(sid, 0)), "-t", f"{ln:.3f}", "-i", p]
            if a_map == "1:a":
                cmd += a_in
            run(cmd + ["-map", "0:v", "-map", a_map, "-vf", vf, "-af", "aresample=48000,aformat=channel_layouts=stereo",
                       "-t", f"{ln:.3f}", "-c:v", "libx264", "-crf", "18", "-preset", "fast",
                       "-c:a", "aac", "-b:a", "192k", part])
        else:
            run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r={FPS}:d={ln:.3f}",
                 "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                 "-vf", f"drawtext=text='{sid} 미생성':fontfile='C\\:/Windows/Fonts/malgun.ttf':"
                        "fontcolor=white:fontsize=64:x=(w-tw)/2:y=(h-th)/2,format=yuv420p",
                 "-t", f"{ln:.3f}", "-c:v", "libx264", "-crf", "18", "-preset", "fast",
                 "-c:a", "aac", "-b:a", "192k", part])
        parts.append(part)
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w", encoding="utf-8") as f:
        f.writelines(f"file '{p.replace(os.sep, '/')}'\n" for p in parts)
    video = os.path.join(tmp, "video.mp4")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", video])
    out = os.path.join(OUT, "ep02_draft.mp4")
    run(["ffmpeg", "-y", "-i", video, "-i", VO, "-filter_complex",
         f"[0:a]volume={sfx_db}dB[s];[1:a]aresample=48000,alimiter=limit=0.891:level=false[v];"
         "[v][s]amix=inputs=2:duration=first:normalize=0[a]",
         "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", out])
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"→ {out}  ({duration(out):.2f}s · VO {SCENES['total']}s)")
    check()


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] not in ("ingest", "check", "build"):
        sys.exit(__doc__)
    if a[0] == "ingest":
        ingest(a[1])
    elif a[0] == "check":
        check()
    else:
        build(float(a[a.index("--sfx") + 1]) if "--sfx" in a else -20.0)
