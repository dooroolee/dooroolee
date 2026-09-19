#!/usr/bin/env python3
"""「안쪽의 세계 : Inside the Box」 브랜드 자산 생성기 — Pillow만 있으면 동작한다. 크레딧 0.

    pip install pillow
    python build.py

색상·문구·서체는 아래 설정 블록만 고치면 된다.
한글은 Pretendard(사용자 설치), 영문·숫자는 Bahnschrift(윈도우 기본).
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

# ─────────── 설정 ───────────
NAME_KR = "안쪽의 세계"
NAME_EN = "INSIDE THE BOX"
HANDLE = "@insidethebox_kr"
TAGLINE = "겉모습 너머를 매크로 렌즈로 해부합니다"

PAPER = (239, 236, 229)      # 밝은 중성 — 비주얼 시스템 「어두우면 밝게 다시」
PAPER_D = (226, 222, 213)    # 배경 그라데이션 하단
INK = (22, 24, 26)
STEEL = (138, 144, 153)
AMBER = (216, 135, 31)       # 계측선 강조 — 「빨간 계측선 → 앰버로」

# Pretendard는 웨이트마다 파일이 따로다. 사용자 폰트 폴더에 설치돼 있다.
PRE_DIR = os.path.join(os.path.expanduser("~"),
                       "AppData", "Local", "Microsoft", "Windows", "Fonts")
EN = "C:/Windows/Fonts/bahnschrift.ttf"
OUT = os.path.dirname(os.path.abspath(__file__))
ALT = os.path.join(OUT, "_alt")

SAFE_W, SAFE_H = 1235, 338   # 유튜브 배너 모바일 안전영역
W, H = 2048, 1152
# ────────────────────────────


def kr(size, weight="Medium"):
    """Pretendard. 없으면 Noto Sans KR로 떨어진다."""
    p = os.path.join(PRE_DIR, f"Pretendard-{weight}.otf")
    if not os.path.exists(p):
        f = ImageFont.truetype("C:/Windows/Fonts/NotoSansKR-VF.ttf", size)
        try:
            f.set_variation_by_name(weight)
        except Exception:
            pass
        return f
    return ImageFont.truetype(p, size)


def en(size, style="SemiBold"):
    f = ImageFont.truetype(EN, size)
    try:
        f.set_variation_by_name(style)
    except Exception:
        pass
    return f


def _w(f, text, track):
    return sum(f.getlength(c) + track for c in text) - track


def tracked(d, xy, text, f, fill, track, halo=None, halo_w=0):
    """자간 있는 가운데 정렬 텍스트. PIL은 트래킹을 지원하지 않아 한 글자씩 찍는다.

    halo를 주면 글자 둘레에 테두리를 깐다 — 투명 배경 번인이 어두운 화면에서도 읽히게."""
    x = xy[0] - _w(f, text, track) / 2
    for c in text:
        d.text((x, xy[1]), c, font=f, fill=fill, anchor="lm",
               stroke_width=halo_w, stroke_fill=halo)
        x += f.getlength(c) + track
    return _w(f, text, track)


def paper_bg():
    im = Image.new("RGB", (W, H), PAPER)
    g = Image.new("L", (1, H))
    for y in range(H):
        g.putpixel((0, y), int(255 * (y / H) ** 1.6))
    return Image.composite(Image.new("RGB", (W, H), PAPER_D), im, g.resize((W, H)))


# ─────────── 배너 C 「분해도」 — 타이포 3안 ───────────
def iso_box_line(d, cx, cy, w, dp, hgt, color, width=3):
    """아이소메트릭 상자 라인아트. 윗면은 마름모."""
    L, T, R, B = ((cx - w / 2, cy), (cx, cy - dp / 2), (cx + w / 2, cy), (cx, cy + dp / 2))
    d.line([L, T, R, B, L], fill=color, width=width, joint="curve")
    for p in (L, B, R):
        d.line([p, (p[0], p[1] + hgt)], fill=color, width=width)
    d.line([(L[0], L[1] + hgt), (B[0], B[1] + hgt), (R[0], R[1] + hgt)],
           fill=color, width=width, joint="curve")


def banner_C(weight="Bold", size=126, track=4, variant="1"):
    """C 「분해도」 — 상자가 세 겹으로 열린다. 분해선은 안전영역 밖, 안엔 글자만."""
    im = paper_bg()
    d = ImageDraw.Draw(im)
    cx, cy = W / 2, H / 2

    for side in (-1, 1):                       # 데스크톱·TV에서만 보이는 분해도
        bx = cx + side * 720
        for dy, col in [(-190, (206, 202, 193)), (0, (184, 180, 171)), (190, (206, 202, 193))]:
            iso_box_line(d, bx, cy + dy, 230, 112, 62, col)
        d.line([(bx, cy - 240), (bx, cy + 260)], fill=(222, 197, 160), width=2)

    f_kr = kr(size, weight)
    f_en = en(42, "SemiBold")
    f_h = en(28, "Light")
    f_tg = kr(30, "Light")

    tracked(d, (cx, cy - 78), NAME_KR, f_kr, INK, track)
    tracked(d, (cx, cy + 8), NAME_EN, f_en, AMBER, 22)
    d.line([(cx - 420, cy + 60), (cx + 420, cy + 60)], fill=(200, 196, 187), width=2)
    tracked(d, (cx, cy + 104), TAGLINE, f_tg, (86, 90, 96), 2)
    tracked(d, (cx, cy + 154), HANDLE, f_h, STEEL, 6)
    return im


# ─────────── 심볼 — 3안(열린 상자) 계열 6종 ───────────
S = 800          # 마스터 해상도. 150·60은 여기서 축소한다


def _canvas():
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    return im, ImageDraw.Draw(im)


def _body(d, cx, cy, w, dp, hgt, t, color=INK):
    """상자 몸통 — 윗면 마름모 + 앞쪽 세 모서리."""
    L, T, R, B = ((cx - w / 2, cy), (cx, cy - dp / 2), (cx + w / 2, cy), (cx, cy + dp / 2))
    d.line([L, T, R, B, L], fill=color + (255,), width=t, joint="curve")
    for p in (L, B, R):
        d.line([p, (p[0], p[1] + hgt)], fill=color + (255,), width=t)
    d.line([(L[0], L[1] + hgt), (B[0], B[1] + hgt), (R[0], R[1] + hgt)],
           fill=color + (255,), width=t, joint="curve")
    return L, T, R, B


def _lid(d, cx, cy, w, dp, t, lift, squash=1.0, color=AMBER):
    """뚜껑 — 몸통과 같은 마름모를 들어 올리고 필요하면 납작하게."""
    y = cy - lift
    dd = dp * squash
    L, T, R, B = ((cx - w / 2, y), (cx, y - dd / 2), (cx + w / 2, y), (cx, y + dd / 2))
    d.line([L, T, R, B, L], fill=color + (255,), width=t, joint="curve")
    return L, T, R, B


def m_a():
    """A 젖힌 뚜껑 — 1차 시안의 그 형태."""
    im, d = _canvas()
    c = S / 2
    t = int(S * 0.048)
    _body(d, c, c + S * 0.06, S * 0.46, S * 0.24, S * 0.24, t)
    _lid(d, c + S * 0.04, c + S * 0.06, S * 0.46, S * 0.24, t, S * 0.20, squash=0.55)
    return im


def m_b():
    """B 분해 — 뚜껑이 수평으로 떠 있다. 배너 C의 분해도와 결이 같다."""
    im, d = _canvas()
    c = S / 2
    t = int(S * 0.048)
    _body(d, c, c + S * 0.09, S * 0.46, S * 0.24, S * 0.22, t)
    _lid(d, c, c + S * 0.09, S * 0.46, S * 0.24, t, S * 0.26)
    return im


def m_c():
    """C 빛 — 열린 상자 안쪽에서 빛이 세 줄 뻗어 나온다."""
    im, d = _canvas()
    c = S / 2
    t = int(S * 0.048)
    L, T, R, B = _body(d, c, c + S * 0.12, S * 0.46, S * 0.24, S * 0.22, t)
    for k, dx in enumerate((-0.13, 0.0, 0.13)):
        x0 = c + dx * S
        d.line([(x0, c + S * 0.06), (x0 + dx * S * 0.9, c - S * 0.26)],
               fill=AMBER + (255,), width=int(S * 0.036))
    return im


def m_d():
    """D 단면 — 앞면을 잘라내 내부 한 겹이 드러난다."""
    im, d = _canvas()
    c = S / 2
    t = int(S * 0.048)
    w, dp, hgt = S * 0.46, S * 0.24, S * 0.26
    cy = c + S * 0.04
    _body(d, c, cy, w, dp, hgt, t)
    d.line([(c - w / 2 + t, cy + hgt * 0.52), (c, cy + dp / 2 + hgt * 0.52),
            (c + w / 2 - t, cy + hgt * 0.52)],
           fill=AMBER + (255,), width=int(S * 0.036), joint="curve")
    return im


def m_e():
    """E 점 — 상자와 안쪽의 점 하나. 60px에서 가장 강하다."""
    im, d = _canvas()
    c = S / 2
    t = int(S * 0.052)
    w, dp = S * 0.46, S * 0.24
    cy = c + S * 0.10
    _body(d, c, cy, w, dp, S * 0.22, t)
    r = S * 0.062
    d.ellipse([c - r, cy - S * 0.19 - r, c + r, cy - S * 0.19 + r], fill=AMBER + (255,))
    return im


def m_f():
    """F 배지 — 원 안의 상자. 프로필 원형 크롭과 궁합이 좋다."""
    im, d = _canvas()
    c, R = S / 2, S * 0.40
    d.ellipse([c - R, c - R, c + R, c + R], outline=INK + (255,), width=int(S * 0.040))
    t = int(S * 0.044)
    _body(d, c, c + S * 0.05, S * 0.34, S * 0.17, S * 0.17, t)
    _lid(d, c, c + S * 0.05, S * 0.34, S * 0.17, t, S * 0.19)
    return im


MARKS = [("A", "젖힌 뚜껑", m_a), ("B", "분해", m_b), ("C", "빛", m_c),
         ("D", "단면", m_d), ("E", "점", m_e), ("F", "배지", m_f)]


def marks_sheet():
    """심볼 비교 시트 — 큰 형태 · 프로필 원형 · 플레이어 실표시 60px."""
    CW, CH = 1800, 1180
    im = Image.new("RGB", (CW, CH), (250, 249, 246))
    d = ImageDraw.Draw(im)
    tracked(d, (CW / 2, 54), "심볼 — 「열린 상자」 계열 6종", kr(34, "SemiBold"), INK, 2)
    tracked(d, (CW / 2, 96), "판정은 맨 아래 60px 칸부터. 워터마크는 그 크기에서 살아남는 것만 답이다",
            kr(21, "Light"), (120, 124, 130), 1)

    f_lb = kr(24, "SemiBold")
    for k, (key, label, fn) in enumerate(MARKS):
        col, row = k % 3, k // 3
        cx = 300 + col * 600
        top = 150 + row * 500

        card = Image.new("RGB", (300, 300), PAPER)
        big = fn().resize((300, 300), Image.LANCZOS)
        card.paste(big, (0, 0), big)
        im.paste(card, (int(cx - 150), top))
        d.rectangle([cx - 150, top, cx + 150, top + 300], outline=(216, 212, 203), width=2)
        tracked(d, (cx, top + 338), f"{key}. {label}", f_lb, INK, 2)

        prof = Image.new("RGB", (120, 120), PAPER)          # 프로필 원형 크롭
        m = fn().resize((120, 120), Image.LANCZOS)
        prof.paste(m, (0, 0), m)
        mask = Image.new("L", (120, 120), 0)
        ImageDraw.Draw(mask).ellipse([0, 0, 119, 119], fill=255)
        im.paste(prof, (int(cx - 190), top + 366), mask)

        play = Image.new("RGB", (180, 120), (26, 26, 26))    # 플레이어 우하단 60px
        small = fn().resize((60, 60), Image.LANCZOS)
        play.paste(small, (108, 48), small)
        im.paste(play, (int(cx + 10), top + 366))
    return im


# ─────────── 확정본 (배너 C1 · 심볼 B) ───────────
def mark_B(halo=True, bg=None, ink=INK, lid=AMBER):
    """확정 심볼 — B 「분해」. 뚜껑이 수평으로 떠 있다.

    halo=True면 획 둘레에 종이색 테두리를 깐다. 투명 배경 워터마크가
    어두운 화면(전쟁·야간 씬) 위에 얹혀도 윤곽이 죽지 않게 하는 장치다."""
    im = Image.new("RGBA", (S, S), bg or (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c = S / 2
    cy = c + S * 0.09
    t = int(S * 0.048)
    w, dp, hgt, lift = S * 0.46, S * 0.24, S * 0.22, S * 0.26
    if halo:
        ht = int(t * 2.4)
        _body(d, c, cy, w, dp, hgt, ht, PAPER)
        _lid(d, c, cy, w, dp, ht, lift, color=PAPER)
    _body(d, c, cy, w, dp, hgt, t, ink)
    _lid(d, c, cy, w, dp, t, lift, color=lid)
    return im


def profile(px=800):
    """프로필 800×800 — 원형 크롭되므로 모서리 여백을 크게 둔다. 배경은 종이색."""
    im = Image.new("RGB", (px, px), PAPER)
    m = mark_B(halo=False).resize((int(px * 0.78), int(px * 0.78)), Image.LANCZOS)
    off = (px - m.width) // 2
    im.paste(m, (off, off), m)
    return im


def lockup(with_handle=True, w=1600, h=360):
    """CapCut 번인용 가로 락업. 투명 배경 + 종이색 테두리(어두운 화면 대비)."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    sym = mark_B(halo=True).resize((int(h * 0.92), int(h * 0.92)), Image.LANCZOS)
    im.paste(sym, (40, (h - sym.height) // 2), sym)

    x0 = 40 + sym.width + 46
    f_kr = kr(int(h * 0.40), "Bold")
    cy = h / 2 - (int(h * 0.13) if with_handle else 0)
    tx = x0 + _w(f_kr, NAME_KR, 2) / 2
    tracked(d, (tx, cy), NAME_KR, f_kr, INK + (255,), 2, halo=PAPER + (255,), halo_w=6)
    if with_handle:
        f_s = en(int(h * 0.145), "SemiBold")
        sub = f"{NAME_EN}   {HANDLE}"
        tracked(d, (x0 + _w(f_s, sub, 8) / 2, cy + h * 0.30), sub, f_s,
                STEEL + (255,), 8, halo=PAPER + (255,), halo_w=4)
    return im.crop(im.getbbox())


def build_final():
    banner_C("Bold", 126, 4).save(os.path.join(OUT, "banner_2048x1152.png"))
    profile().save(os.path.join(OUT, "profile_800x800.png"))
    mark_B(halo=True).resize((150, 150), Image.LANCZOS).save(
        os.path.join(OUT, "watermark_youtube_150x150.png"))
    lockup(True).save(os.path.join(OUT, "watermark_capcut_wordmark.png"))
    lockup(False, 1300, 320).save(os.path.join(OUT, "watermark_capcut_plain.png"))
    # 대안 — 밝은 화면 전용(테두리 없음) · 어두운 화면 전용(아이보리 선)
    mark_B(halo=False).resize((150, 150), Image.LANCZOS).save(
        os.path.join(ALT, "wm_150_no_halo.png"))
    mark_B(halo=False, ink=PAPER).resize((150, 150), Image.LANCZOS).save(
        os.path.join(ALT, "wm_150_ivory.png"))


def final_sheet():
    """확정본 점검 시트 — 밝은 화면·어두운 화면·플레이어 60px를 나란히."""
    CW, CH = 1500, 620
    im = Image.new("RGB", (CW, CH), (250, 249, 246))
    d = ImageDraw.Draw(im)
    tracked(d, (CW / 2, 50), "확정본 점검 — 워터마크(투명 배경)", kr(30, "SemiBold"), INK, 2)
    wm = mark_B(halo=True)
    for k, (label, bg) in enumerate([("밝은 화면", (236, 233, 226)), ("중간", (128, 130, 132)),
                                     ("어두운 화면", (24, 25, 27))]):
        x = 130 + k * 420
        plate = Image.new("RGB", (360, 300), bg)
        big = wm.resize((220, 220), Image.LANCZOS)
        plate.paste(big, (20, 40), big)
        small = wm.resize((60, 60), Image.LANCZOS)
        plate.paste(small, (270, 200), small)
        im.paste(plate, (x, 110))
        tracked(d, (x + 180, 450), label, kr(24, "Medium"), INK, 2)
    tracked(d, (CW / 2, 530), "오른쪽 아래 작은 것이 플레이어 실표시 60px", kr(21, "Light"),
            (120, 124, 130), 1)
    tracked(d, (CW / 2, 572), "프로필·배너는 파일로 따로 보냅니다", kr(21, "Light"),
            (120, 124, 130), 1)
    return im


if __name__ == "__main__":
    os.makedirs(ALT, exist_ok=True)
    build_final()
    final_sheet().save(os.path.join(ALT, "final_check_sheet.png"))
    banner_C("Bold", 126, 4).save(os.path.join(ALT, "banner_C1_pretendard_bold.png"))
    banner_C("SemiBold", 130, 10).save(os.path.join(ALT, "banner_C2_pretendard_semibold.png"))
    banner_C("Medium", 122, 20).save(os.path.join(ALT, "banner_C3_pretendard_medium_wide.png"))
    marks_sheet().save(os.path.join(ALT, "marks_box_family.png"))
    for key, _, fn in MARKS:
        fn().resize((150, 150), Image.LANCZOS).save(os.path.join(ALT, f"wm_box_{key}_150.png"))
    print("saved ->", ALT)
