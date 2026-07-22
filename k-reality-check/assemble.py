#!/usr/bin/env python3
"""K-Reality Check #1 — final assembly: download assets, build per-act segments,
align 1.1x VO, burn act captions, encode 1080p60, emit SRT."""
import os, subprocess, sys, json, urllib.request

FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
ROOT = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, "assets"); SEG = os.path.join(ROOT, "seg"); OUT = os.path.join(ROOT, "out")
for d in (A, SEG, OUT): os.makedirs(d, exist_ok=True)
BASE = "https://d8j0ntlcm91z4.cloudfront.net/user_3GnGS9JbBIJNeXrCFvgmip8ViR3/"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

CLIPS = {1:"hf_20260722_064255_d7075287-1415-4a22-8d33-8d1899e045aa.mp4",
         2:"hf_20260722_064332_df3cc451-4ff2-4bdc-b510-f3aab78ec3ce.mp4",
         3:"hf_20260722_064302_bae8b71b-56d3-42d1-902f-e1699a204134.mp4",
         4:"hf_20260722_064305_4f34c10f-525b-406b-a623-0ac19dd09dde.mp4",
         5:"hf_20260722_064309_f682af00-a92e-4ce8-8d21-27ced45c7dca.mp4",
         6:"hf_20260722_064713_c077aa11-e97d-451d-9c59-a05e0b6a3486.mp4",
         7:"hf_20260722_064315_0fa50ae9-7585-4505-9134-632eef0285dd.mp4",
         8:"hf_20260722_064714_b609f420-8da7-46c3-a191-35f68bd53f5b.mp4"}
VOS = {1:"hf_20260722_064744_c62f7814-fbe0-4461-a660-40bd5b0a43f2.wav",
       2:"hf_20260722_064745_be0586c9-99e0-492c-a16b-ef3bd4b5bfb6.wav",
       3:"hf_20260722_064747_96fbaf98-6bd2-4009-972c-a6429f0c7a3c.wav",
       4:"hf_20260722_064750_79cce68d-852b-4575-8a52-c4514b77df4a.wav",
       5:"hf_20260722_064752_f5365edf-bb0a-4884-8020-c1fb42e6f0ae.wav",
       6:"hf_20260722_064754_5e423380-93f2-48b8-a83e-8ec9bbd51833.wav",
       7:"hf_20260722_064902_cb0e2a12-4dcf-4b74-88e8-c825f9db1c47.wav",
       8:"hf_20260722_064904_8a511745-12e7-45a0-a2c8-953185a7884e.wav"}
PCARDS = {2:"hf_20260722_063741_a88dac34-d6b9-4e76-8e58-e55fe623eacb.png",
          3:"hf_20260722_063744_aec56f28-db41-49ec-9e21-066fda013dd1.png",
          4:"hf_20260722_063749_39e04824-5c88-4887-b1f0-f4250f34b8ae.png",
          5:"hf_20260722_063752_be1f6403-c463-434d-af36-d0c5763d93b7.png",
          6:"hf_20260722_063756_78e5f69f-dda3-41b7-b909-d0bc84da620f.png",
          7:"hf_20260722_063759_04b1b046-365b-4a9c-a783-a402b4fed0f6.png"}
DCARDS = {1:"hf_20260722_064356_c2f4b3f3-2a8d-4ff5-a9cd-9bfff54f0e70.png",
          2:"hf_20260722_063804_942baba7-4b53-4ad4-b0b6-e3c68ad78de7.png",
          3:"hf_20260722_064358_80aaba50-22e0-4f7c-84f3-2f28c5a3e076.png",
          4:"hf_20260722_064401_4c7d3900-cbf6-4d76-afee-f216a0e301a1.png",
          5:"hf_20260722_064404_d9ca3a60-089b-4ba8-b96e-98c47b2a196a.png",
          6:"hf_20260722_064407_69a37068-428a-4300-86c9-132d08430956.png",
          7:"hf_20260722_064409_998ec873-592a-44bf-8e14-4521dc320eca.png"}

CAPTIONS = {1:("10,000+ REVIEWS ANALYZED","0x00B4D8"),
            2:("TRAP #1 | BANANA MILK ESPRESSO","0xE63946"),
            3:("TRAP #2 | RICE PAPER BULDAK ROLL","0xE63946"),
            4:("TRAP #3 | GUMMY BEAR ICE CUP","0xE63946"),
            5:("LOCAL PICK #1 | EOL-BAK-SA","0x21A179"),
            6:("LOCAL PICK #2 | GOMTANG + MANDU","0x21A179"),
            7:("LOCAL PICK #3 | BUL-SAM-CHI","0x21A179"),
            8:("3 TRAPS vs 3 REAL HACKS","0x222222")}

SENTS = {
1:["Korea is hotter than ever right now—millions of tourists are flying in for K-pop, K-beauty, and incredible K-food.",
   "And if you've searched K-food on TikTok or Instagram, you've definitely seen those crazy convenience store food hacks.",
   "But as a Seoul local who analyzed over ten thousand posts on Korean forums and sales data—half of them are total aesthetic traps!",
   "Today, I'm exposing three viral hacks locals secretly HATE, and three data-backed hacks we've ACTUALLY eaten for over a decade."],
2:["First trap: Banana Milk Espresso.","Over eighty percent of users on Theqoo, a major Korean community, voted this a complete fail.",
   "Why? The artificial banana syrup clashes with coffee bitterness.",
   "Dozens of Korean food YouTubers tested this, and the consensus was unanimous: looks great on Instagram, tastes terrible in real life.",
   "Rating? Five out of ten."],
3:["Second trap: Buldak Rice Paper Roll.","Great for a fifteen-second ASMR clip, but local food reviewers agree: cold rice paper turns into rubbery leather that ruins the spicy sauce.",
   "Why spend twenty minutes prepping a meal that's supposed to take three minutes?"],
4:["Third trap: Gummy Bear Ice Cup.","Quick chemistry lesson: gelatin freezes instantly in ice-cold soda.",
   "Local SNS reviews call this photo-only trash, because those cute gummies turn into unchewable rubber rocks."],
5:["So what do locals ACTUALLY drink? Meet Eol-Bak-Sa—Bacchus energy drink plus Chilsung Cider over ice.",
   "If you look at Korean PC Cafe menu sales data, this is the undisputed number one drink.",
   "Korean convenience stores even report a massive search spike for this combo at two A.M. during university exam weeks.",
   "It's the official local hangover and fatigue cure!"],
6:["For food? Skip the rice paper gimmick.",
   "According to a survey on Korean university dorm forums, dropping frozen dumplings into hot Sari Gomtang bone broth ramen is the number one dorm survival hack.",
   "Convenience store POS data even shows a high companion purchase rate between these two items.",
   "Five minutes, five dollars, and one hundred percent rich comfort food backed by a decade of student data."],
7:["And the holy grail of Korean convenience store meals? The Bul-Sam-Chi combo—Buldak noodles, a spicy triangle kimbap, and melted string cheese.",
   "This combo has literally ranked number one on Everytime, Korea's largest university app, for over ten consecutive years.",
   "Millions of local students can't be wrong!"],
8:["So today, we looked at three viral convenience store traps and three real hacks that Koreans ACTUALLY eat.",
   "Don't fall for fifteen-second TikTok hype—stick to real, data-backed local secrets!",
   "Which data surprised you the most today?",
   "If there's any real Korean topic or trend you want to learn about next here on K-Reality Check, leave a comment below and don't forget to subscribe!",
   "See you next time with even better content!"]}

def sh(args, **kw):
    r = subprocess.run(args, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        print("CMD FAIL:", " ".join(args[:12]), "...\n", r.stderr[-1500:]); sys.exit(1)
    return r

def dl(fname):
    p = os.path.join(A, fname)
    if not (os.path.exists(p) and os.path.getsize(p) > 1000):
        urllib.request.urlretrieve(BASE + fname, p)
    return p

def probe_dur(path):
    r = sh([FF, "-i", path, "-f", "null", "-"])
    return None

def ffprobe_duration(path):
    import re
    r = subprocess.run([FF, "-i", path], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", r.stderr)
    h, mn, s = int(m.group(1)), int(m.group(2)), float(m.group(3))
    return h*3600 + mn*60 + s

def esc(t):  # drawtext escaping
    return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'").replace(",", "\\,").replace("%","\\%")

def cap_filter(act):
    text, color = CAPTIONS[act]
    return (f"drawtext=fontfile={FONT}:text='{esc(text)}':fontsize=42:fontcolor=white:"
            f"box=1:boxcolor={color}@0.92:boxborderw=16:x=(w-text_w)/2:y=52")

print("== downloading assets ==")
for m in (CLIPS, VOS, PCARDS, DCARDS):
    for k, f in m.items(): dl(f)
print("download ok:", len(os.listdir(A)), "files")

vo_dur = {k: ffprobe_duration(os.path.join(A, f)) for k, f in VOS.items()}
vo_s = {k: v/1.1 for k, v in vo_dur.items()}
print("VO durations (1.1x):", {k: round(v,2) for k,v in vo_s.items()})

TAIL = 0.6; PCARD_D = 1.0; CLIP_D = 4.0
acts, t = [], 0.0
for k in range(1, 9):
    lead = PCARD_D if k in PCARDS else 0.0
    dur = lead + vo_s[k] + TAIL
    acts.append({"act": k, "start": t, "lead": lead, "vo_off": t + lead, "dur": dur})
    t += dur
TOTAL = t
print("act starts:", [(a["act"], round(a["start"],2)) for a in acts], "TOTAL", round(TOTAL,2))

IMG_VF = "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60,format=yuv420p"
CLIP_VF = "scale=1920:1080,setsar=1,fps=60,format=yuv420p"
ENC = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-an"]

print("== building segments ==")
seglist = []
for a in acts:
    k = a["act"]; cap = cap_filter(k)
    if k in PCARDS:
        p = os.path.join(SEG, f"a{k}_p.mp4")
        sh([FF, "-y", "-loop", "1", "-t", f"{PCARD_D:.3f}", "-i", os.path.join(A, PCARDS[k]),
            "-vf", f"{IMG_VF},{cap}", *ENC, p]); seglist.append(p)
    c = os.path.join(SEG, f"a{k}_c.mp4")
    if k == 8:
        loop_d = vo_s[k] + TAIL
        sh([FF, "-y", "-stream_loop", "12", "-i", os.path.join(A, CLIPS[k]), "-t", f"{loop_d:.3f}",
            "-vf", f"{CLIP_VF},{cap}", *ENC, c]); seglist.append(c)
    else:
        sh([FF, "-y", "-i", os.path.join(A, CLIPS[k]), "-t", f"{CLIP_D:.3f}",
            "-vf", f"{CLIP_VF},{cap}", *ENC, c]); seglist.append(c)
    if k in DCARDS:
        d = os.path.join(SEG, f"a{k}_d.mp4")
        dur = vo_s[k] - CLIP_D + TAIL
        sh([FF, "-y", "-loop", "1", "-t", f"{dur:.3f}", "-i", os.path.join(A, DCARDS[k]),
            "-vf", f"{IMG_VF},{cap}", *ENC, d]); seglist.append(d)
    print(f"  act {k} segments done")

concat_txt = os.path.join(SEG, "concat.txt")
with open(concat_txt, "w") as f:
    for s in seglist: f.write(f"file '{s}'\n")
video_only = os.path.join(OUT, "video_only.mp4")
sh([FF, "-y", "-f", "concat", "-safe", "0", "-i", concat_txt, "-c", "copy", video_only])
print("video concat ok:", round(ffprobe_duration(video_only),2), "s")

print("== building audio ==")
inputs, fparts, mix = [], [], []
idx = 0
for a in acts:
    k = a["act"]
    inputs += ["-i", os.path.join(A, VOS[k])]
    ms = int(a["vo_off"] * 1000)
    fparts.append(f"[{idx}:a]atempo=1.1,aformat=sample_rates=48000:channel_layouts=stereo,adelay={ms}|{ms}[v{k}]")
    mix.append(f"[v{k}]"); idx += 1
clip_amb = []
for a in acts:
    k = a["act"]
    r = subprocess.run([FF, "-i", os.path.join(A, CLIPS[k])], capture_output=True, text=True)
    if "Audio:" not in r.stderr: continue
    inputs += ["-i", os.path.join(A, CLIPS[k])]
    ms = int((a["start"] + a["lead"]) * 1000)
    fparts.append(f"[{idx}:a]volume=0.22,aformat=sample_rates=48000:channel_layouts=stereo,adelay={ms}|{ms}[c{k}]")
    mix.append(f"[c{k}]"); idx += 1
fchain = ";".join(fparts) + f";{''.join(mix)}amix=inputs={len(mix)}:duration=longest:normalize=0,alimiter=limit=0.9,apad=whole_dur={TOTAL:.3f}[out]"
audio = os.path.join(OUT, "audio.m4a")
sh([FF, "-y", *inputs, "-filter_complex", fchain, "-map", "[out]", "-t", f"{TOTAL:.3f}", "-c:a", "aac", "-b:a", "192k", audio])
print("audio ok:", round(ffprobe_duration(audio),2), "s")

final = os.path.join(OUT, "K-Reality-Check-EP1.mp4")
sh([FF, "-y", "-i", video_only, "-i", audio, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "copy", "-movflags", "+faststart", final])
print("FINAL:", final, round(ffprobe_duration(final),2), "s", os.path.getsize(final)//1048576, "MB")

print("== SRT ==")
def ts(x):
    h=int(x//3600); m=int(x%3600//60); s=int(x%60); ms=int((x-int(x))*1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
lines, n = [], 1
for a in acts:
    k = a["act"]; sents = SENTS[k]
    total_ch = sum(len(s) for s in sents); cur = a["vo_off"]
    for s in sents:
        d = vo_s[k] * len(s)/total_ch
        lines.append(f"{n}\n{ts(cur)} --> {ts(min(cur+d, a['vo_off']+vo_s[k]))}\n{s}\n")
        cur += d; n += 1
srt = os.path.join(OUT, "K-Reality-Check-EP1.en.srt")
open(srt, "w").write("\n".join(lines))
print("SRT:", srt, n-1, "cues")
print("ALL DONE")
