# 1화 「전자레인지」 — 씬 분할 + 생성 프롬프트 전량

씬 규칙 **`ceil`** 확정 · **75씬** · 전 씬 **6초 생성 클립** · 화면 길이 4.29~5.94초 · 크레딧 0 (작성만)

원본 데이터 `ep01/scenes.json` — 씬 id·in·out·길이·그 구간 VO. 조립 스크립트는 이 파일을 읽는다.

---

## 0. 전 씬 공통 규칙

### 0-A. 스타일 락 — ★모든 프롬프트 끝에 그대로 붙인다★

```
STYLE: tabletop documentary photography, 16:9, 30fps, physically based lighting,
soft large diffused key from upper left plus subtle cool fill, matte non-reflective
surfaces, shallow depth of field, fine film-free digital cleanliness.
NEGATIVE: no people, no hands, no faces, no subtitles, no Korean text, no sentences,
no paragraphs of text, no logos, no brand marks, no watermark, no music, no singing,
no speech, no voice, no aerial shot, no crane shot, no drone, no whip pan, no lens flare,
no on-screen UI.
AUDIO: diegetic room tone and mechanical sound only.
```

> ✅ **`no numbers`는 제거됐다 (2026-09-14 · 사용자 지시).** ★**후반 오버레이를 쓰지 않는다**★ —
> 화면에 뜨는 숫자는 **모델이 그린다.** 이것은 새 규칙이 아니라 README §확정 사항의
> 「계측선 — 수치와 색상은 모델에 맡긴다. 화면 수치가 틀려도 진행한다」를 따르는 것이다.
> 프롬프트 작성 시 이 확정 사항을 어기고 `no numbers`를 넣었던 것을 되돌렸다.
> ```
> 살아있는 규칙   한글 번인 금지 · 자막 금지 · 로고 금지   ← NEGATIVE에 남겨 둡다
> 폐기된 것     no numbers · no letters · no text · no captions · 후반 오버레이 전체
> 사실의 책임   ★나레이션★이 진다. 화면 숫자가 틀려도 그대로 간다
> ```
> → 씬 표의 **「화면값」 칸**은 이제 「후반에 얹을 것」이 아니라 **「프롬프트가 그리라고 시키는 값」**이다.

### 0-B. 카메라 어휘 — ★이 다섯 가지만 쓴다★

```
허용  orbit (수평 공전) · top-down (수직 부감, 테이블 높이) · macro push-in ·
      rack focus · lateral dolly (횡이동)
금지  항공 부감 · 크레인 · 드론 · 휩팬 · 핸드헬드 흔들림
```

### 0-C. 🔴 움직임은 «한 개»만, 그리고 «수치»로 준다 — Flow 1판 반려의 원인

Flow 훅 테스트가 「무빙이 너무 느리다」로 반려됐고, **원인은 프롬프트였다** —
`slow` · `holds still` · `no whip pans`를 **겹쳐 넣은 것**이다. 억제어를 세 겹 쌓으면
모델이 **움직임 항목 자체를 꺼 버린다**(§모델은 지시를 조용히 잘못 푼다).

```
✗ 금지   "slow orbit, camera holds still, no whip pans, gentle, subtle, minimal movement"
✓ 이렇게  "camera orbits 25 degrees to the right across the full 6 seconds"
```

- **한 씬에 카메라 무브는 1개.** 두 개를 붙이지 않는다
- **양을 숫자로 준다** — 각도·배율·초점 이동 대상. 「천천히」는 쓰지 않는다
- `no whip pans`는 **스타일 락 NEGATIVE에 한 번만** 있고, 본문에 다시 쓰지 않는다

### 0-D. 비트 — 씬당 최대 2개

각 씬은 **BEAT 1 / BEAT 2**로 쓴다(비트당 약 3초). 비트가 하나면 그냥 한 줄로 둔다.
**비트는 «카메라»가 아니라 «화면 안에서 벌어지는 일»이다.** 카메라는 클립 전체에 걸쳐 하나다.

### 0-E. 그레이드 타임라인

```
S01–S08   중성 백색 (neutral museum white)      훅 · 문제 정의
S09–S19   ★탈색 카키★ (desaturated khaki, cool)  1막 · 전쟁
S20–S50   중성 회백 (neutral warm gray)          2막~3막-1 설명부
S51       ★전환★ — 카키 잔향을 털고 중성 백색으로 되돌아온다
S52–S71   중성 백색                              3막-2 · 4막
S72–S75   S01~S03과 ★완전히 동일한 룩★           코다 (수미상관)
```

> ★S72~S75는 S01~S03의 재생이다★ — 같은 프롬프트를 쓰되 코다용 지시만 바꾼다.
> **수미상관이 성립하려면 룩이 «같아 보여야» 한다.** 여기서 그레이드가 틀어지면 구조가 죽는다.

---

## B1 · 훅 (S01–S04 · 0:00.00–0:18.86 · 씬 4.71초)

| 씬 | 시간 | 화면값 | 요지 |
|---|---|---|---|
| S01 | 0:00.00–0:04.71 | — | 부엌 선반 위 전자레인지 정면 |
| S02 | 0:04.71–0:09.43 | — | 문 유리 → 안쪽 금속망 랙포커스 |
| S03 | 0:09.43–0:14.14 | — | 금속망 극매크로 |
| S04 | 0:14.14–0:18.86 | **`20`** | 구멍 하나 속 어둠 |

**S01** — 「지금 여러분의 부엌에 하나쯤 있을 겁니다」
```
A plain white countertop microwave oven sitting on a clean kitchen shelf, shot
straight-on at appliance height. Neutral museum-white wall behind, no props.
BEAT 1: the closed door faces camera, its dark window the only deep tone in frame.
BEAT 2: the interior lamp behind the glass warms up faintly, revealing the mesh.
CAMERA: macro push-in that tightens from full appliance to door-only across the 6 seconds.
```

**S02** — 「그런데 그 문을 자세히 본 적 있습니까」
```
Extreme close view of the microwave door glass, filling the frame edge to edge.
BEAT 1: focus sits on the outer glass surface, faint dust and a single fingerprint smear.
BEAT 2: focus travels through the glass onto the perforated metal sheet behind it.
CAMERA: rack focus from glass surface to metal mesh, completing at 4 seconds and holding.
```

**S03** — 「아주 작은 구멍이 뚫린 금속판이 한 장」
```
Macro of the perforated metal shield inside a microwave door, the hole lattice filling
the entire frame, holes roughly 1.5 millimetres across in a regular grid.
BEAT 1: the grid reads as a flat silver field, each hole a dark dot.
BEAT 2: shallow focus sweeps left to right, only a narrow band of holes sharp at a time.
CAMERA: lateral dolly travelling 8 centimetres to the right across the full 6 seconds.
```

**S04** — 「이 기계가 부엌에 들어오기까지 이십 년이 걸렸습니다」
```
Ultra-macro on a single perforation in the metal shield, the hole opening into pure
black, the machined burr on its rim catching light.
BEAT 1: the surrounding metal grain is visible, the hole a black circle at centre.
BEAT 2: the frame continues into the hole until black fills two thirds of the image.
ON-SCREEN: the figure 20 in plain white sans-serif, lower left third, fading in at
3 seconds over the black and holding to the end.
CAMERA: macro push-in advancing until the single hole occupies 70 percent of frame.
```

---

## B2 · 문제 정의 (S05–S08 · 0:18.86–0:42.30 · 씬 5.86초)

도면 톤. **선으로 그린 단면**이 실물 위에 얹히는 다이어그램 룩.

| 씬 | 시간 | 화면값 | 요지 |
|---|---|---|---|
| S05 | 0:18.86–0:24.72 | — | 금속 상자 단면 도면이 닫힌다 |
| S06 | 0:24.72–0:30.58 | — | 갇힌 전파가 내벽을 반사 |
| S07 | 0:30.58–0:36.44 | — | 시선 궤적이 금속벽에 막힘 |
| S08 | 0:36.44–0:42.30 | — | 두 조건이 겹쳐 교착 |

**S05** — 「가두면 보이지 않고, 뚫으면 새어 나온다」
```
A clean cutaway model of a sealed metal box on a white tabletop, its near wall removed
so the empty interior cavity is visible. Brushed steel, matte, no markings.
BEAT 1: the cavity sits open, interior walls evenly lit.
BEAT 2: a steel panel swings up and seals the opening, the interior going dark.
CAMERA: orbit 20 degrees to the left across the full 6 seconds.
```

**S06** — 「안에서 음식을 익히는 것은 불이 아니라 전파입니다」
```
Interior of the sealed steel cavity, seen through the cutaway. Thin luminous cyan
traces representing radio waves bounce between the walls, reflecting at hard angles.
BEAT 1: a single trace leaves one wall and strikes the opposite one.
BEAT 2: the traces multiply to a dozen, criss-crossing and never leaving the cavity.
CAMERA: macro push-in tightening 1.4x on the cavity centre.
```

**S07** — 「그런데 사람은 안을 봐야 합니다」
```
The same steel cavity from outside. A thin straight white line representing a line of
sight approaches the outer wall from camera side and stops dead against the metal.
BEAT 1: the white line extends toward the wall and flattens on contact.
BEAT 2: the line retries at three different heights, each stopped at the same surface.
CAMERA: lateral dolly 12 centimetres to the left across the full 6 seconds.
```

**S08** — 「이 두 조건은 동시에 만족될 수 없어 보였습니다」
```
Split composition on white: left, a fully sealed steel box, dark and closed. Right, the
same box with an open rectangular window, cyan wave traces spilling out of it.
BEAT 1: both states sit side by side, equally lit.
BEAT 2: both dim by a third and the gap between them narrows, the two states pressing
toward each other without meeting.
CAMERA: static framing with a 1.05x macro push-in over the full 6 seconds.
```

> ⚠️ S08의 「프레임 중앙 여백」은 **후반에 `?`를 얹을 자리**다. 프롬프트에 물음표를 그리게 하지 않는다 —
> 모델이 그리는 기호는 모양이 불안정하고, 그러면 **같은 실수를 클립마다 산다**.

---

## B3 · 1막 — 이게 없던 세상 (S09–S19 · 0:42.30–1:46.82 · 씬 5.87초)

★**탈색 카키 그레이드 구간**★ — `desaturated khaki-olive grade, cool shadows, lifted blacks`
를 각 프롬프트 STYLE 앞에 한 줄 추가한다. **S20에서 중성으로 돌아온다.**

| 씬 | 시간 | 화면값 | 요지 |
|---|---|---|---|
| S09 | 0:42.30–0:48.17 | — | 야간 하늘, 지상에서 올려본 구름 |
| S10 | 0:48.17–0:54.03 | — | 레이더 안테나 회전 |
| S11 | 0:54.03–0:59.90 | — | 레이더 스코프 스윕 |
| S12 | 0:59.90–1:05.76 | — | 스코프 위 블립 매크로 |
| S13 | 1:05.76–1:11.63 | — | ★마그네트론 본체★ (S69와 매치컷) |
| S14 | 1:11.63–1:17.49 | — | 내부 공동 단면, 전자 궤적 |
| S15 | 1:17.49–1:23.36 | — | 전시 생산 라인 탑다운 |
| S16 | 1:23.36–1:29.22 | — | 멈춘 라인, 먼지 |
| S17 | 1:29.22–1:35.09 | — | 작업대 위 작동 중인 마그네트론 |
| S18 | 1:35.09–1:40.95 | — | 녹은 간식 매크로 |
| S19 | 1:40.95–1:46.82 | — | 튀어 오르는 옥수수 알갱이 |

**S09** — 「이야기는 부엌이 아니라 전쟁터에서 시작합니다」
```
Night sky seen from ground level, heavy overcast cloud lit from below by a faint
unseen source. No aircraft visible, no landmarks, no horizon detail.
BEAT 1: the cloud mass drifts, dense and featureless.
BEAT 2: a thin sweep of pale light passes across the cloud base and fades.
CAMERA: macro push-in of 1.2x on the cloud mass across the full 6 seconds.
```

**S10** — 「눈으로는 보이지 않으니 다른 감각이 필요했습니다」
```
A wartime parabolic radar antenna on a steel mast, shot from ground level looking up at
a 30 degree angle, silhouetted against the overcast night sky.
BEAT 1: the dish sits angled at the sky, its lattice struts readable against cloud.
BEAT 2: the dish rotates on its mount, sweeping through roughly 60 degrees.
CAMERA: orbit 30 degrees to the right around the mast across the full 6 seconds.
```

**S11** — 「전파를 쏘고, 되돌아오는 신호로 물체의 위치를 읽는 장치」
```
A round cathode ray radar scope in a bakelite housing on a steel bench, viewed at a
20 degree tilt. Green phosphor face, a single radial sweep line rotating.
BEAT 1: the sweep line completes one full rotation, phosphor trailing behind it.
BEAT 2: on the second rotation a small bright return appears at the upper left.
CAMERA: macro push-in tightening from full housing to scope face only.
```

**S12** — 「멀리 있는 항공기를 잡아내려면 아주 강한 전파가 필요했고」
```
Extreme macro on the green phosphor face of the radar scope, the individual grain of the
coating visible, one bright return blooming and decaying.
BEAT 1: focus rests on the sweep line as it crosses frame.
BEAT 2: focus shifts to the bright return, which brightens then decays to nothing.
CAMERA: rack focus from sweep line to return, completing at 4 seconds.
```

**S13** — 「그걸 만들어내는 부품이 마그네트론이었습니다」  ★S69와 매치컷★
```
A cavity magnetron on a plain steel workbench: a heavy copper cylinder with radial
cooling fins, a ceramic insulator collar and two stub terminals. Palm sized, machined,
oxidised copper with tool marks.
BEAT 1: the block sits alone on the bench, fins catching a hard raking light.
BEAT 2: the light shifts and the ceramic collar picks up a cool highlight.
CAMERA: orbit 40 degrees to the right at bench height across the full 6 seconds.
```

> ★S13과 S69는 같은 세팅·같은 렌즈·같은 오빗 각도로 뽑는다.★ 4막의 「전쟁터에서 폭격기를
> 찾아내던 그 부품입니다」가 **시각적으로 성립하려면 두 컷이 같은 물건으로 보여야 한다.**

**S14** — 「전자가 자기장에 밀려 원을 그리며 돌고」
```
Cross section of the magnetron interior on white: a central cathode pin ringed by eight
resonant cavities cut into solid copper, shown as a clean machined cutaway.
BEAT 1: the cavity ring sits still, copper surfaces crisp.
BEAT 2: thin luminous traces spiral outward from the centre pin, curving into the cavities.
CAMERA: top-down framing with a 1.3x macro push-in across the full 6 seconds.
```

**S15** — 「전쟁 내내 이 부품은 가장 중요한 군수품 중 하나였습니다」
```
Top-down view of a factory pallet packed with dozens of identical magnetrons in rows,
each seated in a moulded fibre tray, on a concrete floor.
BEAT 1: the full grid of units fills frame, uniform and dense.
BEAT 2: a shadow edge travels across the pallet from left to right.
CAMERA: top-down lateral dolly of 25 centimetres to the right across the full 6 seconds.
```

**S16** — 「수천 대를 만들던 라인이 멈춰 섰습니다」
```
A stopped factory conveyor in an empty assembly hall, steel rollers bare, one abandoned
fibre tray left on the belt. Dust suspended in a shaft of window light.
BEAT 1: the belt is motionless, dust drifting through the light shaft.
BEAT 2: the light shaft dims as if cloud passed, the hall flattening to grey.
CAMERA: lateral dolly 40 centimetres along the conveyor across the full 6 seconds.
```

**S17** — 「한 기술자가 작동 중인 마그네트론 앞에 서 있었습니다」
```
A magnetron mounted in an open test rig on a laboratory bench, cables running to an
off-frame supply. The bench is otherwise empty, the stool beside it unoccupied.
BEAT 1: the rig sits powered, the needle on the bench meter resting at the low end of its dial.
BEAT 2: the needle rises and settles, the copper block and the air around it unchanged.
CAMERA: macro push-in of 1.5x onto the magnetron across the full 6 seconds.
```

> ⚠️ **무인물 규칙 — 퍼시 스펜서를 «그리지 않는다».** 사람도 손도 프레임에 없다.
> 그 사람의 존재는 **빈 스툴과 켜진 장비**로만 말한다. 나레이션이 이름을 대고 있으므로
> 화면까지 설명할 필요가 없다.

**S18** — 「주머니에 넣어둔 간식이 녹아 있는 것을 발견합니다」
```
Macro on a paper-wrapped confectionery bar lying on the laboratory bench, the wrapper
torn open along one side, the contents collapsed into a soft glossy pool.
BEAT 1: the melt sits still, surface reflecting the overhead light.
BEAT 2: a slow sag continues at one edge, the pool creeping a few millimetres.
CAMERA: rack focus from the bench grain to the melted surface, completing at 3 seconds.
```

**S19** — 「팝콘이 튀어 오릅니다」
```
Macro on a scatter of dried corn kernels on the steel bench in front of the test rig,
shot at kernel height with a wide aperture.
BEAT 1: the kernels sit still, one beginning to split at its hull.
BEAT 2: three kernels burst upward in high speed, white flesh unfurling mid air.
CAMERA: static framing at kernel height, 120fps captured motion played back at 30fps.
```

---

## B4 · 훅 2 — 1차 딜레마 (S20–S22 · 1:46.82–1:59.68 · 씬 4.29초)

★그레이드 복귀★ — 카키를 털고 중성 회백으로 돌아온다. **S20이 전환점이다.**

| 씬 | 시간 | 화면값 | 요지 |
|---|---|---|---|
| S20 | 1:46.82–1:51.11 | — | 레이더레인지 캐비닛 정면 |
| S21 | 1:51.11–1:55.39 | — | 조리대 높이 눈금과 비교 |
| S22 | 1:55.39–1:59.68 | — | 부엌 문틀에 안 들어감 → 암전 |

**S20** — 「보통의 이야기는 여기서 끝납니다」
```
A tall commercial cabinet appliance on a neutral grey floor, shot straight-on: a steel
cabinet the height of a wardrobe with a single small door in its upper half, riveted
panels, industrial latch hardware, no markings of any kind.
BEAT 1: the cabinet stands alone, evenly lit, filling most of frame height.
BEAT 2: a soft shadow builds along its left flank.
CAMERA: orbit 15 degrees to the right across the full 6 seconds.
```

**S21** — 「음식을 데우는 데는 성공했습니다」
```
The same steel cabinet, its small upper door standing open, a plain white plate of food
on the rack inside, shot straight-on at door height on neutral grey.
BEAT 1: the plate sits inside the open cabinet, the interior plain sheet steel.
BEAT 2: steam rises steadily from the plate and keeps rising to the end.
CAMERA: macro push-in of 1.4x from the full cabinet to the open door across the full 6 seconds.
```

**S22** — 「그것을 부엌에 들여놓을 방법이 없었습니다. 이십 년 동안이나요」
```
The steel cabinet pushed up against a standard domestic doorway frame on neutral grey.
The cabinet is visibly wider and taller than the opening.
BEAT 1: the cabinet meets the frame and stops, the mismatch obvious at both edges.
BEAT 2: the image falls to full black over the last second.
CAMERA: macro push-in of 1.2x on the contact edge, ending in blackout.
```

---

## B5 · 2막 — 1차 해결과 그 대가 (S23–S32 · 1:59.68–2:58.22 · 씬 5.85초)

| 씬 | 시간 | 화면값 | 요지 |
|---|---|---|---|
| S23 | 1:59.68–2:05.53 | — | 특허 도면 탑다운 |
| S24 | 2:05.53–2:11.39 | **`1945.10.08`** | 도면 표제란 |
| S25 | 2:11.39–2:17.24 | — | 레이더레인지 전신 오빗 + 키 눈금 |
| S26 | 2:17.24–2:23.10 | **`340 kg`** | 무게 게이지 상승 |
| S27 | 2:23.10–2:28.95 | **`$5,000`** | 빈 가격 카드 |
| S28 | 2:28.95–2:34.80 | — | 냉각 배관 매크로, 물 흐름 |
| S29 | 2:34.80–2:40.66 | — | 배관이 바닥으로 — 공사 단면 |
| S30 | 2:40.66–2:46.51 | — | 대형 주방 스테인리스 횡이동 |
| S31 | 2:46.51–2:52.37 | **`1955`** | 가정용 모델, 여전히 큼 |
| S32 | 2:52.37–2:58.22 | — | 판매 막대가 바닥에 붙어 있음 |

**S23** — 「레이시온은 특허를 출원합니다」
```
Top-down on an aged technical drawing sheet lying on a dark wood desk, showing a sectional
elevation of a cabinet appliance in fine ink linework. Paper is toned, slightly cockled.
BEAT 1: the full sheet fills frame, linework crisp.
BEAT 2: the frame tightens onto the sectional elevation at sheet centre.
CAMERA: top-down macro push-in of 1.6x across the full 6 seconds.
```

**S24** — 「등록까지는 다시 오 년이 걸렸습니다」
```
Extreme macro across the lower corner of the same drawing sheet, where a blank rectangular
title block is ruled in ink. Inside it the date 1945.10.08 is stamped in period
typewriter ink, slightly uneven, paper fibre visible around it.
BEAT 1: focus sits on the paper grain outside the block.
BEAT 2: focus moves onto the stamped date, which fills the right half of frame.
CAMERA: rack focus from paper grain to title block, completing at 4 seconds.
```

> ⚠️ 표제란은 **비워 둔다.** 날짜는 후반 오버레이다.

**S25** — 「이름은 레이더레인지. 높이는 성인 남성의 키를 넘었습니다」
```
The tall steel cabinet appliance on neutral grey, with a plain vertical measuring staff
standing beside it, unmarked, reaching above the cabinet top.
BEAT 1: the cabinet and the staff stand together, cabinet top clearly the taller.
BEAT 2: a shadow sweeps down the staff from top to bottom.
CAMERA: orbit 35 degrees to the left across the full 6 seconds.
```

**S26** — 「무게는 삼백사십 킬로그램이 넘었습니다」
```
Macro on a large round industrial weighing dial with a white face, engraved graduations
running from 0 to 400 with the unit kg printed below the spindle, and a single black
needle, mounted on a steel plate.
BEAT 1: the needle rests at zero at the bottom of its travel.
BEAT 2: the needle swings clockwise through roughly 300 degrees and settles just past
the 340 graduation.
CAMERA: macro push-in of 1.3x on the dial face across the full 6 seconds.
```

**S27** — 「값은 오천 달러」
```
A white price card standing upright in a small brass easel on a neutral grey surface,
$5,000 printed on it in large plain serif figures, evenly lit.
BEAT 1: the card sits square to camera, its edge shadow soft, the figures in shadow.
BEAT 2: the key light lifts and the figures resolve crisp against near paper white.
CAMERA: macro push-in of 1.25x on the card face across the full 6 seconds.
```

**S28** — 「물을 순환시켜 식혀야 했습니다」
```
Macro on copper cooling pipework running along the underside of a steel appliance chassis,
compression fittings and a short section of clear hose in the run.
BEAT 1: the pipe run sits still, condensation beading on the copper.
BEAT 2: water visibly moves through the clear hose section, carrying a bubble with it.
CAMERA: lateral dolly 20 centimetres along the pipe run across the full 6 seconds.
```

**S29** — 「놓으려면 배관 공사가 필요했다는 뜻입니다」
```
Cutaway of a floor section on neutral grey: tiled surface above, and below it supply and
return pipes turning upward to meet an appliance base plate.
BEAT 1: the cutaway sits still, pipe runs readable through the floor slab.
BEAT 2: the tiled upper layer lifts away a few centimetres, exposing more of the run.
CAMERA: orbit 25 degrees to the right across the full 6 seconds.
```

**S30** — 「대형 식당, 그리고 기내식을 데우는 항공사 정도만」
```
A commercial stainless kitchen line with empty pass-through shelves, gastronorm pans
stacked and unused, everything scrubbed and vacant.
BEAT 1: the stainless surfaces run away from camera, specular and cold.
BEAT 2: an overhead light bank steps on, lifting the whole line by a stop.
CAMERA: lateral dolly 50 centimetres along the line across the full 6 seconds.
```

**S31** — 「가정용이라는 이름을 단 제품이 처음 나옵니다」
```
A large domestic appliance cabinet on neutral grey, waist height and nearly a metre wide,
enamelled finish with a small viewing door and chrome trim, no markings.
BEAT 1: the unit sits alone, its bulk filling the lower two thirds of frame.
BEAT 2: a counter section slides in beside it, the unit still visibly deeper and taller.
ON-SCREEN: the figure 1955 in plain white sans-serif, lower left third, fading in at
2.5 seconds and holding to the end.
CAMERA: orbit 30 degrees to the right across the full 6 seconds.
```

**S32** — 「거의 팔리지 않았습니다」
```
A row of eight identical domestic appliance cabinets standing in a showroom, each draped
with a plain grey dust sheet, receding from foreground to background on a neutral grey
floor. Price tags hang from the handles, the printed side turned away.
BEAT 1: the row stands still, a thin layer of dust visible on the nearest sheet.
BEAT 2: the tag on the nearest unit turns slightly in the still air.
CAMERA: lateral dolly 35 centimetres along the row across the full 6 seconds.
```

---

## B6 · 훅 3 — 2차 딜레마 (S33–S35 · 2:58.22–3:16.04 · 씬 5.94초)

| 씬 | 시간 | 화면값 | 요지 |
|---|---|---|---|
| S33 | 2:58.22–3:04.16 | — | 상자가 완전히 닫히며 암전 |
| S34 | 3:04.16–3:10.10 | — | 창이 뚫리자 전파가 새어 나감 |
| S35 | 3:10.10–3:16.04 | — | 스플릿 — 막을까 볼까 |

**S33** — 「전파가 새어 나오는 것이었습니다」
```
The sealed steel cavity model on white, cutaway wall still open, cyan wave traces
bouncing inside.
BEAT 1: the traces criss-cross the open cavity, several escaping past the cut edge.
BEAT 2: a steel panel closes the cut face and the escaping traces are cut off, the frame
falling to near black.
CAMERA: macro push-in of 1.3x on the closing face across the full 6 seconds.
```

**S34** — 「앞쪽으로 창을 내면 전파가 나옵니다」
```
The now sealed steel box on white, front face solid.
BEAT 1: a rectangular window opens in the front face, revealing the lit cavity within.
BEAT 2: cyan wave traces pour out through the opening toward camera and past the frame edge.
CAMERA: orbit 20 degrees to the left across the full 6 seconds.
```

**S35** — 「막을 것인가, 볼 것인가」
```
Split composition on white: left half a fully sealed dark steel box, right half the same
box with an open window leaking cyan traces. A hard vertical seam divides them.
BEAT 1: both halves hold, the contrast between dark and leaking plainly readable.
BEAT 2: the vertical seam brightens to a thin white line running the full frame height.
CAMERA: static framing with a 1.05x macro push-in across the full 6 seconds.
```

---

## B7 · 3막-1 — 같은 구멍, 다른 파장 (S36–S51 · 3:16.04–4:50.26 · 씬 5.89초)

★**영상 전체의 핵심 설명부 · 16씬**★ — 세 단계(파장 / 빛 / 구멍)가 여기서 다 나온다.

> ### 🔴 이 블록의 설계 원칙 — ★같은 «판»을 계속 쓴다★
> S36~S51은 **하나의 흰 테이블 위에서 벌어지는 한 편의 시연**이다. 씬마다 세트를 바꾸면
> 「같은 구멍이 하나에게는 벽이고 하나에게는 문」이라는 **논증이 시각적으로 안 이어진다.**
> 판·조명·카메라 높이를 **16씬 내내 고정**하고, **판 «위의 것»만 바꾼다.**

| 씬 | 시간 | 화면값 | 요지 |
|---|---|---|---|
| S36 | 3:16.04–3:21.93 | **`1`** | 첫째, 파장 — 파형이 그려진다 |
| S37 | 3:21.93–3:27.82 | **`12 cm`** | 12cm 파형과 눈금 |
| S38 | 3:27.82–3:33.71 | — | 파형이 작은 구멍에 튕긴다 |
| S39 | 3:33.71–3:39.59 | **`2`** | 뚫려 있어도 전파에겐 벽 |
| S40 | 3:39.59–3:45.48 | — | 둘째, 빛 — 촘촘한 파형 등장 |
| S41 | 3:45.48–3:51.37 | **`0.0005 mm`** | 빛 파장 극매크로 |
| S42 | 3:51.37–3:57.26 | **`200,000`** | 손바닥이 20만 조각으로 |
| S43 | 3:57.26–4:03.15 | — | 빛은 구멍을 그냥 지나간다 |
| S44 | 4:03.15–4:09.04 | — | ★같은 구멍, 두 궤적 겹침★ |
| S45 | 4:09.04–4:14.93 | **`3`** | 셋째, 크기 — 상한선 |
| S46 | 4:14.93–4:20.82 | — | 하한선, 사이가 비어 있다 |
| S47 | 4:20.82–4:26.70 | — | 선택 폭이 이만큼 넓다 |
| S48 | 4:26.70–4:32.59 | **`1–2 mm`** | 실제로 고른 값 |
| S49 | 4:32.59–4:38.48 | — | 키우면 새는 양이 급증 |
| S50 | 4:38.48–4:44.37 | — | 막힌 벽이자 뚫린 창 |
| S51 | 4:44.37–4:50.26 | — | ★실제 문 금속망으로 복귀★ |

**S36** — 「답은 전파 자체의 성질 안에 있었습니다. 첫째, 파장」
```
An empty white laboratory table filling frame, seen at table height, nothing on it.
BEAT 1: the bare white surface holds, a soft falloff toward the back edge.
BEAT 2: a single luminous cyan sine wave draws itself across the table from left to right,
about one metre long with four visible crests.
ON-SCREEN: the numeral 1 in plain dark sans-serif, upper left third, fading in at
1 second and holding to the end.
CAMERA: macro push-in of 1.15x across the full 6 seconds.
```

**S37** — 「이 기계가 쓰는 전파의 파장은 약 십이 센티미터입니다」
```
The cyan sine wave lying on the white table, with a steel rule graduated in centimetres
placed parallel beneath one full crest-to-crest span.
BEAT 1: the rule slides in from the right and aligns under a single wave period.
BEAT 2: that one period brightens while the rest of the wave dims by half, and a thin
dimension line spans it labelled 12 cm in plain dark sans-serif.
CAMERA: top-down framing with a 1.3x macro push-in across the full 6 seconds.
```

**S38** — 「자기 파장보다 뚜렷하게 작은 구멍은 통과하지 못한다」
```
A thin drawn line of luminous cyan light lying on the white table in the shape of a sine
curve, the same line as in the wavelength shot, identical in colour and line weight. An
upright perforated steel plate stands across its path, holes about 1.5 millimetres across.
BEAT 1: the whole drawn line slides to the right along the table until its leading end
reaches the plate face.
BEAT 2: the line rebounds off the plate and slides back to the left, the outgoing and
returning line crossing into a stationary figure of light in front of the plate.
CAMERA: lateral dolly 20 centimetres to the right across the full 6 seconds.
```

**S39** — 「구멍이 뚫려 있어도 전파에게는 벽으로 보인다」
```
The perforated steel plate seen straight-on from the wave side, filling frame, its hole
lattice fully visible and lit from behind so each hole shows as a bright point.
BEAT 1: the lattice of bright points reads clearly as open holes.
BEAT 2: a cyan sheet of light washes across the plate face and is entirely turned back,
none of it passing through.
ON-SCREEN: the numeral 2 in plain white sans-serif, upper left third, fading in at
1 second and holding to the end.
CAMERA: macro push-in of 1.4x on the plate centre across the full 6 seconds.
```

**S40** — 「사람이 보는 빛도 같은 전자기파입니다. 다른 것은 파장뿐입니다」
```
The white table with the cyan sine wave still lying along it. A second wave, warm white
and vastly finer, draws itself directly below and parallel to the first.
BEAT 1: the cyan wave holds, its four broad crests spanning the table.
BEAT 2: the white wave completes, so dense its individual crests are not resolvable at
this magnification, reading as a continuous bright line.
CAMERA: top-down framing with a 1.2x macro push-in across the full 6 seconds.
```

**S41** — 「빛의 파장은 천 분의 일 밀리미터에도 미치지 못합니다」
```
Extreme macro diving into the warm white line on the table until its structure resolves
into individual crests, packed impossibly tight.
BEAT 1: the line reads as solid, no structure visible.
BEAT 2: magnification reaches the point where hundreds of individual crests resolve, a
thin dimension line spanning one crest labelled 0.0005 mm in plain white sans-serif.
CAMERA: macro push-in of 40x on the white line across the full 6 seconds.
```

**S42** — 「그 손바닥을 이십만 조각으로 나눈 것 중 하나입니다」
```
Top-down on a plain white rectangular tile on the table, roughly hand sized.
BEAT 1: the tile is whole, a single flat surface.
BEAT 2: a fine grid subdivides it repeatedly, each pass quartering the cells, until the
surface reads as uniform grey texture rather than countable squares.
ON-SCREEN: the figure 200,000 in plain dark sans-serif, lower right third, fading in at
4 seconds and holding to the end.
CAMERA: top-down framing with a 1.5x macro push-in across the full 6 seconds.
```

**S43** — 「전파가 막히는 구멍을 빛은 아무 저항 없이 지나갑니다」
```
The same perforated steel plate standing on the white table, seen from a three-quarter
angle so both faces are readable.
BEAT 1: warm white light approaches the plate from the far side.
BEAT 2: the light passes straight through every hole, throwing a sharp grid of bright
dots onto the table surface in front of the plate.
CAMERA: orbit 25 degrees to the right across the full 6 seconds.
```

**S44** — 「같은 구멍이 하나에게는 벽이고, 하나에게는 활짝 열린 문입니다」
```
The perforated steel plate on the white table, both effects present at once: cyan traces
striking the plate face and bouncing back, warm white light streaming through the holes.
BEAT 1: the cyan reflection and the white transmission both run, clearly separable.
BEAT 2: the cyan brightens on the near side while the transmitted grid of dots sharpens
on the far side.
CAMERA: orbit 30 degrees to the left across the full 6 seconds.
```

**S45** — 「셋째, 그래서 크기. 전파를 막으려면 구멍이 센티미터 단위보다 작아야 합니다」
```
Top-down on the white table where a single horizontal measuring scale is laid out, a plain
steel rule engraved in centimetres from 0 to 10. A dark band masks the scale from its
right end inward.
BEAT 1: the full rule is exposed and evenly lit.
BEAT 2: the dark band sweeps in from the right and covers everything above 1 cm.
ON-SCREEN: the numeral 3 in plain dark sans-serif, upper left third, fading in at
1 second and holding to the end.
CAMERA: top-down lateral dolly 15 centimetres to the left across the full 6 seconds.
```

**S46** — 「빛을 통과시키려면 천 분의 일 밀리미터보다 크기만 하면 됩니다」
```
The same steel rule top-down, now with a second dark band sweeping in from the left end.
BEAT 1: the right-hand band from the previous shot is already in place.
BEAT 2: the left band advances a very short distance and stops, leaving the great majority
of the rule between the two bands uncovered.
CAMERA: top-down macro push-in of 1.25x across the full 6 seconds.
```

**S47** — 「고를 수 있는 폭이 이만큼 넓다는 것, 그게 답이었습니다」
```
Top-down on the steel rule with both dark bands in place and a wide open gap between them.
BEAT 1: the uncovered middle span holds, plainly the largest region in frame.
BEAT 2: the uncovered span lifts in brightness to near paper white while both bands sink
to deep grey.
CAMERA: top-down framing with a 1.1x macro push-in across the full 6 seconds.
```

**S48** — 「실제로 고른 값은 지름 일 밀리미터에서 이 밀리미터 사이입니다」
```
Extreme macro on three adjacent perforations in the steel plate, the machined rim burr and
surface grain of the metal fully resolved.
BEAT 1: the three holes sit in a row, focus even across all three.
BEAT 2: focus narrows onto the centre hole, a thin dimension line spanning its diameter
labelled 1-2 mm in plain white sans-serif, the outer two holes falling soft.
CAMERA: rack focus from the outer holes to the centre hole, completing at 4 seconds.
```

**S49** — 「구멍이 커질수록 새어 나오는 양이 가파르게 늘기 때문에」
```
The perforated plate on the white table, seen three-quarter, cyan traces striking it.
BEAT 1: with small holes, every trace is turned back at the face.
BEAT 2: the holes visibly widen to several millimetres and cyan traces begin streaming
through in growing numbers, the leak accelerating over the last two seconds.
CAMERA: macro push-in of 1.5x on the plate across the full 6 seconds.
```

**S50** — 「금속판 한 장이 전파에게는 막힌 벽이고 빛에게는 뚫린 창이 됩니다」
```
The perforated plate restored to small holes, standing alone on the white table, seen
straight-on and lit from behind.
BEAT 1: the hole lattice glows with transmitted white light, fully open to the eye.
BEAT 2: cyan traces arrive at the near face and are all turned back, the transmitted
white grid unaffected.
CAMERA: macro push-in of 1.3x on the plate centre across the full 6 seconds.
```

**S51** — 「이게 여러분이 매일 들여다보는 그 금속망입니다」  ★그레이드 복귀★
```
Macro of the perforated metal shield inside a microwave oven door, seen through the door
glass, the hole lattice filling the entire frame, holes roughly 1.5 millimetres across in
a regular grid, brushed silver steel.
BEAT 1: the door glass surface catches a faint sheen in front of the lattice.
BEAT 2: the sheen fades and focus settles fully on the metal, the lattice filling frame
exactly as in the opening macro.
CAMERA: macro push-in of 1.2x across the full 6 seconds.
```

> ★S51은 S03과 «같은 구도»여야 한다.★ 훅에서 본 그 망으로 돌아오는 것이 이 블록의 착지점이다.

> ### 🔴 S51 v1 반려 — ★「A가 B로 녹아든다」를 시키지 않는다★ (2026-09-14 · 실측)
> v1은 「흰 테이블 위 시험판이 실물 금속망으로 dissolve」였다. 사용자 판정 —
> **「금속망이 «흰색»이고, 전자레인지 «밖»에 붙어 있는 것처럼 보인다」.**
> **모델이 틀린 게 아니라 프롬프트가 그렇게 시켰다.** 원인 셋 전부 문장에 있었다.
> ```
> ① 흰색      BEAT 1의 `clean laboratory white`
>             ★같은 블록의 S39·S48은 전부 `steel plate`인데 S51만 흰색이라고 썼다★ — 모순
> ② 밖에 붙음  `the surround resolves into …` = ★시험판이 «상수», 기계가 «주위에 생겨남»★
>             그 구조로 쓰면 판이 먼저 있고 기계가 나중에 둘러싸므로 판이 바깥에 얹힌다
> ③ 빠진 말    S03에는 `★inside★ a microwave door`가 있는데 S51에는 없었다.
>             「안에 있다」고 말한 적이 없으니 안에 안 들어간다
> ```
> ★**v2는 모프를 버렸다**★ — 처음부터 실물 문 «안»의 금속망이고, 「복귀」는 **S03과 구도가
> 같다는 것**으로 읽힌다. B7이 흰 테이블 시연을 이미 15씬 쌓아 놨으므로 모프로 다시 설명할 필요가 없다.
>
> ### ★ 일반 규칙으로 승격 — 변형(morph·dissolve) 자체를 지시하지 않는다 ★
> 모델은 **중간 상태**를 못 만든다. 「A가 B가 된다」를 시키면 A도 B도 아닌 것이 나온다.
> ```
> ✗  X dissolves into Y   ·   the surround resolves into Y   ·   X becomes Y
> ✓  ★처음부터 Y를 찍고★, 연결은 «구도 일치»로 읽힌다        ← S51 v2가 이것
> ✓  굳이 변화가 필요하면 ★사라지는 쪽을 «얹는다»★ — Y가 상수, X가 페이드아웃
> ```
> 이건 §모델은 지시를 조용히 잘못 푼다 ⑤ 「빈 상태를 먼저 만들고 «얹는다»」와 같은 규칙이다.

---

## B8 · 3막-2 — 십이 센티미터가 정한 것들 (S52–S60 · 4:50.26–5:39.48 · 씬 5.47초)

| 씬 | 시간 | 화면값 | 요지 |
|---|---|---|---|
| S52 | 4:50.26–4:55.73 | — | 상자 안 정상파, 밝고 어두운 띠 |
| S53 | 4:55.73–5:01.20 | — | 띠 패턴 탑다운 |
| S54 | 5:01.20–5:06.67 | — | 약한 자리의 음식은 안 익는다 |
| S55 | 5:06.67–5:12.14 | **`1966`** | 회전판이 띠를 가로지른다 |
| S56 | 5:12.14–5:17.60 | — | 구멍 격자 + 회전판 — 취향이 아니다 |
| S57 | 5:17.60–5:23.07 | **`12 cm`** | 파장과 구멍 크기를 나란히 |
| S58 | 5:23.07–5:28.54 | — | 구멍이 전파를 되돌려 보낸다 |
| S59 | 5:28.54–5:34.01 | — | 배관이 사라지고 기계가 작아진다 |
| S60 | 5:34.01–5:39.48 | **`1967` `$495`** | 조리대 위 컴팩트 제품 |

**S52** — 「상자 안에 전파가 겹쳐 세지는 자리와 약해지는 자리가 생깁니다」
```
Interior of the steel cavity seen through its cutaway wall, where cyan energy has settled
into a standing pattern: alternating bright and dark horizontal bands across the volume.
BEAT 1: the bands resolve out of the moving traces and lock into place.
BEAT 2: the bright bands intensify while the dark ones deepen to near black.
CAMERA: macro push-in of 1.3x into the cavity across the full 6 seconds.
```

**S53** — 「약한 자리에 놓인 음식은 익지 않습니다」
```
Top-down on the cavity floor, the standing wave pattern projected onto it as a regular
grid of bright and dark patches.
BEAT 1: the patch grid holds across the floor plate.
BEAT 2: the pattern drifts by half a cell and settles, bright and dark swapping places.
CAMERA: top-down macro push-in of 1.4x across the full 6 seconds.
```

**S54** — 「그래서 음식을 돌립니다」
```
Macro on a ceramic dish of food sitting on the cavity floor across two of the dark
patches, seen at plate height.
BEAT 1: steam rises from one side of the dish only, the other side flat and cold.
BEAT 2: the cold side stays visibly untouched while the steaming side thickens.
CAMERA: lateral dolly 10 centimetres to the right across the full 6 seconds.
```

**S55** — 「천구백육십육년, 회전판이 처음 달립니다」
```
The glass turntable plate seated on its roller ring on the cavity floor, the standing
wave patches visible on the floor beneath it.
BEAT 1: the plate sits still, one dish riding on it over a dark patch.
BEAT 2: the plate turns through roughly 180 degrees, carrying the dish across several
bright and dark patches in turn.
ON-SCREEN: the figure 1966 in plain white sans-serif, lower left third, fading in at
2.5 seconds and holding to the end.
CAMERA: top-down framing with a 1.2x macro push-in across the full 6 seconds.
```

**S56** — 「디자이너의 취향이 아닙니다」
```
Split composition on neutral white: left, extreme macro of the perforated hole lattice.
Right, top-down of the turning glass plate on its roller ring.
BEAT 1: both halves run, the lattice still and the plate turning.
BEAT 2: a thin cyan line traces from the hole lattice across the seam to the turning
plate, connecting the two.
CAMERA: static framing with a 1.08x macro push-in across the full 6 seconds.
```

**S57** — 「그 전파의 파장이 십이 센티미터였다는 것」
```
Top-down on the white table with the cyan sine wave laid out beside the perforated steel
plate, one full wave period and the hole spacing in the same frame.
BEAT 1: both sit still, the scale difference between them plainly readable.
BEAT 2: the wave period and the hole lattice each pulse once, in turn, a thin dimension
line spanning the wave period labelled 12 cm in plain dark sans-serif.
CAMERA: top-down macro push-in of 1.3x across the full 6 seconds.
```

**S58** — 「구멍들은 전파를 안쪽으로 되돌려 보내고 있습니다」
```
Extreme macro on the microwave door shield from the cavity side, holes filling frame,
warm interior light behind camera.
BEAT 1: the lattice holds, each hole a bright point of transmitted light.
BEAT 2: cyan traces strike the lattice from the cavity side and reflect back inward,
away from camera.
CAMERA: macro push-in of 1.35x on the lattice across the full 6 seconds.
```

**S59** — 「냉각용 배관이 사라지고, 부품이 줄고, 가격이 내려갑니다」
```
An exploded assembly of a large appliance chassis on neutral white, its cooling pipework,
transformer, and structural frame floating apart in ordered layers.
BEAT 1: all layers hang in place, the assembly at its largest.
BEAT 2: the pipework layer and two structural layers fade out and the remaining parts
draw together into a body roughly half the original size.
CAMERA: orbit 30 degrees to the right across the full 6 seconds.
```

**S60** — 「마침내 조리대 위에 올라가는 제품이 사백구십오 달러에 나옵니다」
```
A compact countertop microwave oven standing on a domestic kitchen counter, neutral white
surround, enamelled body with a viewing door and a mechanical dial, no markings.
BEAT 1: the unit sits square to camera, the counter running away behind it.
BEAT 2: the interior lamp behind the door glass warms up, the mesh reading through it.
ON-SCREEN: the figures 1967 upper left third and $495 lower right third, both plain white
sans-serif, 1967 fading in at 1.5 seconds and $495 at 3.5 seconds, both holding to the end.
CAMERA: orbit 35 degrees to the right across the full 6 seconds.
```

---

## B9 · 4막 — 확산과 유산 (S61–S71 · 5:39.48–6:42.83 · 씬 5.76초)

| 씬 | 시간 | 화면값 | 요지 |
|---|---|---|---|
| S61 | 5:39.48–5:45.24 | **`1971` `1%`** | 보급률 곡선이 바닥에서 출발 |
| S62 | 5:45.24–5:51.00 | **`1986` `25%` / `1997` `90%`** | 곡선이 가파르게 오른다 |
| S63 | 5:51.00–5:56.76 | — | 식탁이 바뀐다 |
| S64 | 5:56.76–6:02.52 | — | 냉동식품 진열대 횡이동 |
| S65 | 6:02.52–6:08.28 | **`1978`** | 한국 첫 생산 제품 탑다운 |
| S66 | 6:08.28–6:14.03 | **`394,000` / `210,000`** | 가격 대 월급 비교 막대 |
| S67 | 6:14.03–6:19.79 | — | 제과점 진열대 매크로 |
| S68 | 6:19.79–6:25.55 | **`1983`** | 수원 공장 생산 라인 탑다운 |
| S69 | 6:25.55–6:31.31 | — | ★마그네트론 — S13과 매치컷★ |
| S70 | 6:31.31–6:37.07 | **`1/3`** | 선적 컨테이너 · 지도 위 분포 |
| S71 | 6:37.07–6:42.83 | — | 불 없이 익는 음식 |

**S61** — 「천구백칠십일년, 미국 가정 백 집 중 한 집」
```
A line chart rendered as a physical raised ribbon on a neutral white plane, seen at a
25 degree angle. The ribbon runs from the left foreground, flat against the base.
BEAT 1: the flat left section holds, barely lifted off the plane.
BEAT 2: the ribbon begins to climb, still shallow, extending toward the background.
ON-SCREEN: the year 1971 set flat on the base plane beneath the ribbon start, and 1% set
beside the ribbon at that point, both plain dark sans-serif, present from 1 second.
CAMERA: lateral dolly 30 centimetres to the right along the ribbon across the full 6 seconds.
```

**S62** — 「천구백구십칠년에는 열 집 중 아홉 집」
```
The same raised ribbon chart, the camera now further along its run where the climb steepens.
BEAT 1: the ribbon rises through the mid range at a moderate slope.
BEAT 2: the slope steepens sharply and the ribbon reaches near the top of the plane.
ON-SCREEN: two labelled stops set flat on the base plane beneath the ribbon, 1986 with 25%
at the mid point and 1997 with 90% near the top, all plain dark sans-serif, the first
present from 1 second and the second appearing at 3.5 seconds.
CAMERA: lateral dolly 40 centimetres to the right along the ribbon across the full 6 seconds.
```

**S63** — 「그러는 사이 식탁도 바뀝니다」
```
Top-down on a domestic dining table, neutral daylight, a single place setting with an
empty plate, cutlery, and a glass.
BEAT 1: the setting sits complete and still.
BEAT 2: a sealed rectangular tray meal is set down onto the plate position, its film lid
taut and reflective.
CAMERA: top-down macro push-in of 1.2x across the full 6 seconds.
```

**S64** — 「얼렸다가 데우기만 하면 되는 음식이라는 산업이 이때 만들어집니다」
```
A supermarket frozen food aisle, upright glass-door freezer cabinets packed with identical
boxed meals, cold blue-white interior lighting, aisle empty.
BEAT 1: the cabinet run recedes down the aisle, doors frosted at their lower edges.
BEAT 2: condensation on one door clears from the centre outward, revealing packed rows.
CAMERA: lateral dolly 60 centimetres down the aisle across the full 6 seconds.
```

**S65** — 「한국에서는 천구백칠십팔년에 처음 생산됩니다」
```
Top-down on a boxy domestic microwave oven of late 1970s design on a neutral surface:
enamelled steel body, mechanical timer dial, a small viewing door, no markings.
BEAT 1: the unit sits centred, its proportions notably deeper than modern units.
BEAT 2: a soft shadow sweeps across the top panel from left to right.
ON-SCREEN: the figure 1978 in plain dark sans-serif, lower left third, fading in at
2.5 seconds and holding to the end.
CAMERA: top-down macro push-in of 1.3x across the full 6 seconds.
```

**S66** — 「가격은 삼십구만 사천 원」
```
Two physical extruded bars standing side by side on a neutral white plane, seen at a
20 degree angle. Both start flush with the base.
BEAT 1: the right bar rises to roughly half the frame height and stops.
BEAT 2: the left bar rises past it to nearly twice that height and stops.
ON-SCREEN: 394,000 set on the base plane at the foot of the left bar and 210,000 at the
foot of the right bar, both plain dark sans-serif, each appearing as its bar finishes rising.
CAMERA: orbit 20 degrees to the right across the full 6 seconds.
```

**S67** — 「그마저도 가정이 아니라 제과점과 경양식집이 사간 것이었습니다」
```
Macro along a bakery display case, glass front, trays of pastries and bread on stepped
shelves under warm tungsten light, no people.
BEAT 1: focus sits on the glass surface with its faint smears and reflections.
BEAT 2: focus travels through to the pastry trays behind it.
CAMERA: rack focus from glass to trays, completing at 4 seconds.
```

**S68** — 「수원에 세워진 공장은 세계에서 세 번째로 큰 규모였습니다」
```
Top-down on a factory assembly line, a long conveyor carrying identical magnetron units in
moulded trays, overhead industrial lighting, concrete floor, no people.
BEAT 1: the line runs, trays advancing steadily through frame.
BEAT 2: the framing reveals more of the hall, further parallel lines running alongside.
ON-SCREEN: the figure 1983 in plain white sans-serif, lower left third, fading in at
2.5 seconds and holding to the end.
CAMERA: top-down lateral dolly 80 centimetres along the conveyor across the full 6 seconds.
```

**S69** — 「전쟁터에서 폭격기를 찾아내던 그 부품입니다」  ★S13과 매치컷★
```
A cavity magnetron on a plain steel workbench: a heavy copper cylinder with radial cooling
fins, a ceramic insulator collar and two stub terminals. Palm sized, machined copper.
Identical framing, lens and bench to the earlier magnetron shot, but in clean neutral
white grade rather than khaki.
BEAT 1: the block sits alone on the bench, fins catching a hard raking light.
BEAT 2: the light shifts and the ceramic collar picks up a cool highlight.
CAMERA: orbit 40 degrees to the right at bench height across the full 6 seconds.
```

> ★S13과 S69는 «그레이드만» 다르다.★ 나머지는 전부 같아야 한다 — 그래야 「그 부품」이 성립한다.

**S70** — 「미국에서 팔리는 전자레인지의 삼분의 일 이상을 대고 있었습니다」
```
Top-down on a dockside container yard, stacked shipping containers in ordered rows,
overcast daylight, no people or vehicles.
BEAT 1: the container grid fills frame, colours muted and uniform.
BEAT 2: roughly a third of the containers in frame lift in brightness by a stop while the
rest sink slightly.
ON-SCREEN: the fraction 1/3 in plain white sans-serif, lower left third, fading in at
3 seconds and holding to the end.
CAMERA: top-down lateral dolly 70 centimetres across the yard over the full 6 seconds.
```

**S71** — 「인류는 처음으로 불 없이 음식을 익히게 됐습니다」
```
A plate of food on a neutral white counter beside a conventional gas hob, the hob burners
cold and unlit, no flame anywhere in frame.
BEAT 1: the unlit burner ring sits in the foreground, the plate behind it.
BEAT 2: steam rises steadily from the plate while the burner stays dark and cold.
CAMERA: rack focus from the cold burner to the steaming plate, completing at 4 seconds.
```

---

## B10 · 수미상관 — 통찰 (S72–S75 · 6:42.83–7:02.66 · 씬 4.96초)

★**S01~S03의 재생이다.**★ 새 세팅을 만들지 않는다. **룩이 같아 보여야 수미상관이 성립한다.**

| 씬 | 시간 | 화면값 | 요지 | 대응 |
|---|---|---|---|---|
| S72 | 6:42.83–6:47.79 | — | 부엌 선반 위 전자레인지 정면 | **= S01** |
| S73 | 6:47.79–6:52.75 | — | 금속망 극매크로 + 전파 궤적 | **= S03 + 궤적** |
| S74 | 6:52.75–6:57.70 | — | 궤적만 사라진다 | **= S03** |
| S75 | 6:57.70–7:02.66 | — | 구멍에서 풀백 → 끝 | **= S01 역방향** |

**S72** — 「영상 맨 처음에 봤던 그 문을 다시 보겠습니다」
```
A plain white countertop microwave oven on a clean kitchen shelf, shot straight-on at
appliance height against a neutral museum-white wall. Identical framing, lens and
lighting to the opening shot of the film.
BEAT 1: the closed door faces camera, the interior lamp already warm behind the glass.
BEAT 2: focus travels through the glass onto the perforated metal sheet behind it.
CAMERA: macro push-in that tightens from full appliance to door-only across the 6 seconds.
```

**S73** — 「구멍이 촘촘히 뚫린 금속판 한 장」
```
Macro of the perforated shield inside the door, the hole lattice filling frame, matching
the opening macro shot exactly in scale and position.
BEAT 1: the lattice reads as a flat silver field, each hole a dark dot.
BEAT 2: cyan traces appear behind the lattice and strike it from within, every one turned
back, none passing through toward camera.
CAMERA: static framing with a 1.06x macro push-in across the full 6 seconds.
```

**S74** — 「이십 년 만의 답입니다」
```
The same macro of the perforated shield, cyan traces still striking it from within.
BEAT 1: the traces run at full strength against the lattice.
BEAT 2: the traces fade out completely, leaving only the plain metal lattice, unchanged.
CAMERA: static framing with a 1.06x macro push-in across the full 6 seconds.
```

**S75** — 「문제는 사라졌고, 답이 부엌에 남았습니다」
```
Pulling back from the perforated lattice to the full door, then to the whole appliance on
its kitchen shelf, arriving at exactly the opening composition of the film.
BEAT 1: the lattice recedes and the door glass and trim come into frame.
BEAT 2: the full appliance settles into frame, the shelf and wall around it, the interior
lamp switching off in the final second.
CAMERA: macro pull-back from lattice to full appliance across the full 6 seconds.
```

---

## 9. 생성 전에 확인할 것

### 9-A. 🔴 아직 «안 정해진» 것 — 생성 도구

```
힉스필드 gemini_omni_flash_1_1   3크레딧/초 × 6초 × 75클립 = ★1,350★  >  잔액 993.41
Google Flow (유료 구글 계정)      힉스필드 크레딧 ★0★ · 6초 훅 테스트 1판 반려 이력
```

**프롬프트는 두 도구에 그대로 쓸 수 있게 썼다** — 도구별 문법이 아니라 **촬영 지시**로 적었다.
도구가 갈리면 STYLE/NEGATIVE 절만 그 도구 형식으로 옮기면 된다.

→ ★**생성 승인은 도구가 정해진 뒤에 받는다.**★ 지금 상태로 힉스필드에 전량을 던지면 잔액이 깨진다.

### 9-B. 매치컷 3쌍 — ★같이 뽑아야 한다★

```
S13 ↔ S69   마그네트론      그레이드만 다르고 나머지 전부 동일
S03 ↔ S51   금속망 극매크로  S51의 착지점이 S03이다
S01 ↔ S72/S75  문 정면      수미상관의 뼈대
```

**세트·렌즈·카메라 높이가 갈리면 이 세 쌍이 전부 죽는다.** 테스트 씬을 고를 때
**S13과 S69를 같이 뽑아 대조**하는 것이 가장 정보량이 크다.

### 9-C. 테스트 씬 추천 (승인 필요 · 6초 × N클립)

| 순위 | 씬 | 무엇을 보는가 |
|---|---|---|
| 1 | **S03** | 극매크로 구멍 격자가 «격자로» 나오는가. 이게 안 되면 이 영상은 성립하지 않는다 |
| 2 | **S44** | 한 프레임에 «반사»와 «투과»를 동시에 그릴 수 있는가 (설명부 전체가 여기 달렸다) |
| 3 | **S13** | 마그네트론 형상 재현 + 카키 그레이드 |
| 4 | **S69** | S13과 붙여 매치컷이 서는지 |

→ 4클립 × 6초 = **힉스필드 기준 72크레딧**. Flow면 0.

### 9-D. 화면값 목록 — ★프롬프트 안에 들어 있다★ (21씬 · 후반 작업 0)

```
S04 20          S24 1945.10.08   S26 340 kg      S27 $5,000     S31 1955
S36 1           S37 12 cm        S39 2           S41 0.0005 mm  S42 200,000
S45 3           S48 1-2 mm       S55 1966        S57 12 cm      S60 1967 / $495
S61 1971 / 1%   S62 1986 / 25% / 1997 / 90%      S65 1978
S66 394,000 / 210,000             S68 1983       S70 1/3
```

**전부 숫자·영문·기호다** — 한글 번인 금지 규칙은 그대로다.

> ### ✅ 이 목록은 「할 일」이 아니라 「이미 박힌 값」이다 (2026-09-14 개정)
> 전에는 CapCut에서 얹을 목록이었다. 지금은 **21씬 전부 해당 씬 프롬프트 안에 들어 있다.**
> ```
> 방식 A  ★장면 «안» 표면이 값을 진다★ (권장)   S24 도면 표제란 · S26 계기판 눈금 ·
>          S27 가격표 · S37·S41·S48·S57 치수선 · S45 자 눈금
> 방식 B  ON-SCREEN 줄로 얹는다                  붙일 표면이 없는 씬 —
>          S04·S31·S36·S39·S42·S55·S60·S65·S68·S70 · S61·S62·S66(차트 라벨)
> ```
> **A가 기본이다** — 표면에 새겨진 값은 그 씬의 조명·초점·카메라 무브를 «같이» 탄다.
> ON-SCREEN은 화면에 덧붙은 것이라 무브를 안 따라간다. 붙일 데가 없을 때만 쓴다.
>
> 🔴 ★**S08은 이 목록에서 빠졌다**★ (2026-09-14 · 사용자 지시). 구 「`?` 오버레이」 자리다 —
> **기호는 모델이 그리면 모양이 불안정하고, 그 실수를 클립마다 산다.** 물음표 지시를 빼고
> 중앙 여백도 없앴다(얹을 게 없으면 빈 화면이다). 교착은 **두 상태가 좁혀지다 안 만나는 것**으로
> 그림이 진다. → ★**기호·글리프는 프롬프트로 시키지 않는다. 숫자는 시킨다**★
> ★**값이 틀려도 재생성하지 않는다**★ — README §확정 사항 「화면 수치가 틀려도 진행한다」.
> 사실은 나레이션이 책임진다. 한 편에 한두 개는 틀리게 나온다고 보고 간다.
