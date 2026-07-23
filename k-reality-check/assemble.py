#!/usr/bin/env python3
"""K-Reality Check #1 — final assembly: download assets, build per-act segments,
align 1.1x VO, burn act captions, encode 1080p60, emit SRT."""
import os, subprocess, sys, json, urllib.request

FF = "/usr/bin/ffmpeg"
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
       7:"hf_20260723_083216_20359a83-0d5a-4258-b21e-66a69a7885f5.wav",
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

# extra montage footage per act, cycled with the primary clip under the VO.
# .mp4 entries are cut in as 4s chunks; .png/.jpg entries get a 4s Ken Burns pan.
EXTRAS = {
 1:["real_9abd6444.png",                                              # CU 매장 (실사)
    "hf_20260722_072916_fc98b83b-a714-4ac7-b367-55202f21af7b.mp4",
    "hf_20260722_072941_a982d52b-8003-448b-808a-6023d7c1515e.mp4",
    "hf_20260723_083541_330dbecd-e25c-4c25-96ef-ca215d9cad3d.mp4"],   # N1 데이터 분석
 2:["real_2d_banana_coffee.png",                                      # 바나나우유+커피 (실사)
    "hf_20260722_072942_194f8b8e-e88b-47b2-9385-19cc3c9653f5.mp4",
    "hf_20260722_072943_21d38021-8ba4-4e26-a967-1494678b0c5e.mp4",
    "up6_1af8c3d6.png"],                                              # 진열대 (실사)
 3:["hf_20260722_072945_1a72b8b4-b8fe-4aa0-b7be-316c47b3829f.mp4",
    "hf_20260723_090602_eff13ea2-0a4d-4de7-b212-a8d71fe51ae2.mp4"],  # R1 불닭 롤 재생성
 4:["hf_20260722_073335_819cec96-25d4-4e9b-9ad0-60095ad04cf6.mp4",
    "hf_20260722_073337_9780c1e4-63c6-430a-92f0-173c4d2ad249.mp4"],
 5:["real_5d_bacchus.png",                                            # 박카스+사이다 (실사)
    "hf_20260722_073338_0eefc5c6-58d4-4d60-a153-ad61a8d7f18e.mp4",
    "hf_20260722_073340_33b59d17-a114-4c6b-bb8d-1d054518fc66.mp4"],
 6:["hf_20260723_083332_e5136cb6-6678-4bcc-b841-f0baac0ec0c3.mp4",   # R2 컵라면 만두 투하
    "real_mandu_4s.mp4",                                              # 냉동고 만두 (실사 영상)
    "hf_20260723_083415_371cb2aa-b395-4aa6-a0f4-b43a32e5c85a.mp4"],  # R3 기숙사 컵라면
 7:["up1_256bfc13.png",                                               # 불닭 치즈 리조또 (실사)
    "hf_20260723_083449_48225d04-5fc7-4616-b9c8-dde0dfe0921b.mp4"],  # R4 삼각김밥 온전
 8:["hf_20260723_083646_b8f34996-9a77-4fe3-999c-21c4c838878b.mp4",   # 8D TRAP 나열
    "hf_20260723_084255_a76cff71-6021-42bd-ad33-648834d9fe2d.mp4",   # 8E LOCAL 나열
    "real_d328dd4f.png",                                              # 세븐일레븐 (실사)
    "hf_20260722_073624_b1ae0da8-a75f-4e76-9653-5a1254c3ce2f.mp4",
    "hf_20260722_073625_41f7d7ca-3762-48dc-8384-f6729508ddb2.mp4",
    "hf_20260723_085821_3137f75f-cec6-4bbd-a517-0c2c50c6d307.mp4"],  # 8G 인사
}

CAPTIONS = {1:("10,000+ REVIEWS ANALYZED","0x00B4D8"),
            2:("TRAP #1 | BANANA MILK ESPRESSO","0xE63946"),
            3:("TRAP #2 | RICE PAPER BULDAK ROLL","0xE63946"),
            4:("TRAP #3 | GUMMY BEAR ICE CUP","0xE63946"),
            5:("LOCAL PICK #1 | EOL-BAK-SA","0x21A179"),
            6:("LOCAL PICK #2 | GOMTANG + MANDU","0x21A179"),
            7:("LOCAL PICK #3 | BULDAK CHEESE RISOTTO","0x21A179"),
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
7:["And the holy grail of Korean convenience store meals? Tear triangle kimbap and string cheese right into hot Buldak noodles and mix—locals call it the Buldak cheese risotto.",
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

# product card shows for PCARD_D but VO still enters at VO_LEAD so the card
# overlaps the act's opening line instead of adding dead air (total length unchanged)
TAIL = 0.6; VO_LEAD = 1.0; PCARD_D = 3.0; CLIP_D = 4.0; DCARD_D = 5.0
acts, t = [], 0.0
for k in range(1, 9):
    lead = VO_LEAD if k in PCARDS else 0.0
    dur = lead + vo_s[k] + TAIL
    acts.append({"act": k, "start": t, "lead": lead, "vo_off": t + lead, "dur": dur})
    t += dur
TOTAL = t
print("act starts:", [(a["act"], round(a["start"],2)) for a in acts], "TOTAL", round(TOTAL,2))

IMG_VF = "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=24,format=yuv420p"
CLIP_VF = "scale=1920:1080,setsar=1,fps=24,format=yuv420p"
ENC = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-an"]

print("== building segments ==")
seglist = []
for a in acts:
    k = a["act"]; cap = cap_filter(k)
    if k in PCARDS:
        p = os.path.join(SEG, f"a{k}_p.mp4")
        sh([FF, "-y", "-loop", "1", "-t", f"{PCARD_D:.3f}", "-i", os.path.join(A, PCARDS[k]),
            "-vf", f"{IMG_VF},{cap}", *ENC, p]); seglist.append(p)
    # montage: unique clips only (no repeats), body split evenly so every chunk fits in one clip
    playlist = [CLIPS[k]] + EXTRAS.get(k, [])
    body = a["dur"] - (PCARD_D if k in PCARDS else 0.0) - (DCARD_D if k in DCARDS else 0.0)
    n = max(1, -(-int(body*1000) // int(CLIP_D*1000)))
    if len(playlist) < n:
        print(f"FATAL: act {k} needs {n} unique clips for {body:.2f}s but has {len(playlist)}"); sys.exit(1)
    d = body / n
    for i in range(n):
        src = os.path.join(A, playlist[i])
        c = os.path.join(SEG, f"a{k}_m{i}.mp4")
        if src.lower().endswith((".png", ".jpg", ".jpeg")):
            fr = max(int(d*24), 6)
            kb = (f"scale=4224:2376:force_original_aspect_ratio=increase,crop=4224:2376,"
                  f"zoompan=z='min(zoom+{0.1/fr:.6f},1.1)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
                  f"d={fr}:s=3840x2160:fps=24,scale=1920:1080,setsar=1,format=yuv420p")
            sh([FF, "-y", "-i", src, "-vf", f"{kb},{cap}", *ENC, c])
        else:
            sh([FF, "-y", "-i", src, "-t", f"{d:.3f}",
                "-vf", f"{CLIP_VF},{cap}", *ENC, c])
        seglist.append(c)
    if k in DCARDS:
        d = os.path.join(SEG, f"a{k}_d.mp4")
        frames = int(DCARD_D * 24)
        kb = (f"scale=4224:2376:force_original_aspect_ratio=increase,crop=4224:2376,"
              f"zoompan=z='min(zoom+{0.1/frames:.6f},1.1)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
              f"d={frames}:s=3840x2160:fps=24,scale=1920:1080,setsar=1,format=yuv420p")
        sh([FF, "-y", "-i", os.path.join(A, DCARDS[k]),
            "-vf", f"{kb},{cap}", *ENC, d]); seglist.append(d)
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
    # ambience plays once, only while the primary clip is on screen (no looping)
    inputs += ["-i", os.path.join(A, CLIPS[k])]
    ms = int((a["start"] + (PCARD_D if k in PCARDS else 0.0)) * 1000)
    body = a["dur"] - (PCARD_D if k in PCARDS else 0.0) - (DCARD_D if k in DCARDS else 0.0)
    amb_d = body / (1 + len(EXTRAS.get(k, [])))
    fparts.append(f"[{idx}:a]atrim=0:{amb_d:.3f},afade=t=out:st={max(amb_d-0.4,0):.3f}:d=0.4,"
                  f"volume=0.22,aformat=sample_rates=48000:channel_layouts=stereo,adelay={ms}|{ms}[c{k}]")
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
