# 1화 「전자레인지」 — ★Google Flow 전용 프롬프트 75씬★

생성 도구 **Google Flow** 확정 (2026-09-14 · 사용자 지시) · 힙스필드 크레딧 **0**

원본 `_discarded/ep01_microwave/scene-prompts.md` · 이 파일은 **그것을 Flow 형식으로 변환한 것**이다. 내용은 같고 **형식만 다르다**.


---

## 읽기 전에 — Flow로 옮기면서 뭐가 바뀌었나

```
버린 것   NEGATIVE: 절 전체       ← ★Flow에는 네거티브 입력란이 없다★. 본문에 녹여야 한다
남긴 억제   ★세 개★만 — 무인물 · 음악·목소리 금지 · 한글 금지
          나머지(no whip pan · no drone · no lens flare…)는 ★전부 지웠다★
바뀌 틀   「금지」를 「상태 서술」로 — no people → "The set is unattended"
더한 것   ★GRADE 줄★ — 씬마다 그레이드를 박았다(§0-E)
```

> ### 🔴 억제어를 줄인 것이 이 변환의 핵심이다
> 지난 Flow 6초 훅 테스트가 「무빙이 너무 느리다」로 반려됐고, 원인은 프롬프트였다 —
> `slow` · `holds still` · `no whip pans`를 **겹쳐 넣었다.** 억제어를 쌓으면 모델이
> **움직임 항목 자체를 꺼 버린다.**
> ```
> ✗ 지난판   "slow orbit, camera holds still, no whip pans, gentle, subtle"
> ✓ 이 파일  "CAMERA: orbit 25 degrees to the right across the full 6 seconds"
> ```
> 카메라 무브는 **씬당 하나**고 **양을 숫자로** 준다. 「천천히」는 한 번도 안 쓴다.

> ### ✅ 숫자는 모델이 그린다 — 후반 오버레이 없음
> `no numbers`는 제거됐다. 21씬의 화면값이 프롬프트 안에 들어 있다(원본 §9-D).
> **값이 틀려도 재생성하지 않는다** — 사실은 나레이션이 진다.
> ★기호·글리프는 시키지 않는다★(S08에서 뻐다) — 모양이 불안정해 클립마다 같은 실수를 산다.

> ### ⚠️ 각 씬의 「쓸 길이」는 6초가 아니다
> 표의 **쓸길이**만 타임라인에 올라간다(4.29~5.94초). 6초는 **생성 길이**고,
> 남는 여유는 ★모델이 앞뒤를 망쳤을 때 쓸 구간을 고를 폭★이다. 다 쓰지 않는다.

---


## S01 · 쓸길이 4.71초 · 생성 6초

> VO 「지금 여러분의 부엌에 하나쯤 있을 겁니다. 문을 열고, 그릇을 넣고, 버튼을」


```
A plain white countertop microwave oven sitting on a clean kitchen shelf, shot
straight-on at appliance height. Neutral museum-white wall behind, no props.
BEAT 1: the closed door faces camera, its dark window the only deep tone in frame.
BEAT 2: the interior lamp behind the glass warms up faintly, revealing the mesh.
CAMERA: macro push-in that tightens from full appliance to door-only across the 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral museum white, cool and clean.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S02 · 쓸길이 4.71초 · 생성 6초

> VO 「누르면 끝. 그런데 그 문을 자세히 본 적 있습니까. 유리 안쪽에, 아주 작은 구」


```
Extreme close view of the microwave door glass, filling the frame edge to edge.
BEAT 1: focus sits on the outer glass surface, faint dust and a single fingerprint smear.
BEAT 2: focus travels through the glass onto the perforated metal sheet behind it.
CAMERA: rack focus from glass surface to metal mesh, completing at 4 seconds and holding.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral museum white, cool and clean.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S03 · 쓸길이 4.71초 · 생성 6초

> VO 「멍이 뚫린 금속판이 한 장 들어 있습니다. 저 구멍의 크기는 우연이 아닙니」


```
Macro of the perforated metal shield inside a microwave door, the hole lattice filling
the entire frame, holes roughly 1.5 millimetres across in a regular grid.
BEAT 1: the grid reads as a flat silver field, each hole a dark dot.
BEAT 2: shallow focus sweeps left to right, only a narrow band of holes sharp at a time.
CAMERA: lateral dolly travelling 8 centimetres to the right across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral museum white, cool and clean.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S04 · 쓸길이 4.71초 · 생성 6초

> VO 「다. 저것 하나 때문에, 이 기계가 부엌에 들어오기까지 이십 년이 걸렸습니다.」


```
Ultra-macro on a single perforation in the metal shield, the hole opening into pure
black, the machined burr on its rim catching light.
BEAT 1: the surrounding metal grain is visible, the hole a black circle at centre.
BEAT 2: the frame continues into the hole until black fills two thirds of the image.
ON-SCREEN: the figure 20 in plain white sans-serif, lower left third, fading in at
3 seconds over the black and holding to the end.
CAMERA: macro push-in advancing until the single hole occupies 70 percent of frame.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral museum white, cool and clean.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S05 · 쓸길이 5.86초 · 생성 6초

> VO 「당시, 이 물건의 문제는 한 줄로 요약됩니다. 가두면 보이지 않고, 뚫으면 새어 나온다. 안에서 음식」


```
A clean cutaway model of a sealed metal box on a white tabletop, its near wall removed
so the empty interior cavity is visible. Brushed steel, matte, no markings.
BEAT 1: the cavity sits open, interior walls evenly lit.
BEAT 2: a steel panel swings up and seals the opening, the interior going dark.
CAMERA: orbit 20 degrees to the left across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral museum white, cool and clean.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S06 · 쓸길이 5.86초 · 생성 6초

> VO 「을 익히는 것은 불이 아니라 전파입니다. 전파를 가두려면 상자 전체가 금속이어야 합니다. 그런」


```
Interior of the sealed steel cavity, seen through the cutaway. Thin luminous cyan
traces representing radio waves bounce between the walls, reflecting at hard angles.
BEAT 1: a single trace leaves one wall and strikes the opposite one.
BEAT 2: the traces multiply to a dozen, criss-crossing and never leaving the cavity.
CAMERA: macro push-in tightening 1.4x on the cavity centre.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral museum white, cool and clean.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S07 · 쓸길이 5.86초 · 생성 6초

> VO 「데 사람은 안을 봐야 합니다. 무엇이 얼마나 익었는지 보이지 않는 조리 기구를 쓸 사람은 없으니」


```
The same steel cavity from outside. A thin straight white line representing a line of
sight approaches the outer wall from camera side and stops dead against the metal.
BEAT 1: the white line extends toward the wall and flattens on contact.
BEAT 2: the line retries at three different heights, each stopped at the same surface.
CAMERA: lateral dolly 12 centimetres to the left across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral museum white, cool and clean.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


---

> ## 🔴 S07a · S07b — ★신규 추가 (2026-09-15 · 사용자 지시)★
> 사용자가 준 VO 「그런데 사람은 음식이 익어가는 걸 눈으로 봐야 합니다. 전자레인지 앞의
> 유리문이 없이 안이 새까맣게 보이지 않는 조리 기구를 돈 주고 쓸 사람은 없으니까요.」에
> 맞춰 쓴 프롬프트다. **65음절 · 5.86자/초 기준 약 11.1초라 한 씬에 안 들어간다** → 2클립.
> ```
> ⚠️ 번호를 ★밀지 않았다★ — S07a·S07b로 붙였다. S08~S75는 그대로다
> 🔴 미결   이 두 씬이 기존 S07을 ★대체★하는 것인지 ★추가★인지 (§아래 주의)
> ```
> **S07의 기존 VO 「데 사람은 안을 봐야 합니다…」와 «같은 내용의 다른 문장»이다.**
> 대체라면 **VO 마스터가 바뀌므로 재생성·타임코드 재산출이 걸린다.** 추가라면 총 77클립이 되고
> `flow-order.md`의 「받자마자 75개를 센다」도 함께 고쳐야 한다. **확정 전까지는 뽑지 않는다.**

## S07a · 쓸길이 5.55초 · 생성 6초

> VO 「그런데 사람은 음식이 익어가는 걸 눈으로 봐야 합니다. 전자레인지 앞의 유리문이」


```
A shallow ceramic plate of food sitting on a clean white table, seen from a low three-quarter
angle, the food clearly legible in frame.
BEAT 1: thin steam rises steadily from the plate, the surface of the food plainly visible.
BEAT 2: the steam continues and a slow rack focus settles from the table edge onto the food,
holding it sharp.
CAMERA: lateral dolly travelling 6 centimetres to the left across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral museum white, cool and clean.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S07b · 쓸길이 5.55초 · 생성 6초

> VO 「없이 안이 새까맣게 보이지 않는 조리 기구를 돈 주고 쓸 사람은 없으니까요.」


```
The same plate on the same white table, with a plain matte steel panel standing upright
just in front of it, solid and windowless, filling most of the frame.
BEAT 1: the panel slides across until the plate is entirely hidden behind it, a single
narrow seam left open at its edge, the interior beyond that seam pure black.
BEAT 2: the seam narrows to a hairline and the specular highlight running along the panel
dies out, leaving only flat brushed steel and one black line.
CAMERA: macro push-in of 1.3x on the seam across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral museum white, cool and clean.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```

> ### 이 두 씬에 걸린 기존 규칙 4개
> - **김(steam)으로 「익는 중」을 그렸다.** `heat`·`shimmer`·`glow` 미사용 — §S17 반려 규칙.
>   증기는 S21 v2가 통과시킨 계열이라 불로 번지지 않는다
> - **「안 보인다」를 ★검은 화면★으로 그리지 않았다.** 전면을 강철 질감으로 채우고 ★틈 한 줄★만
>   검게 남겼다 — §S32 「부재는 그 부재가 남긴 물건으로 그린다」
> - **「돈 주고 쓸 사람은 없다」를 가격표로 옮기지 않았다.** 글리프를 시키게 되고, 이 문장의 그림은
>   「비싸다」가 아니라 ★「안이 안 보인다」★다
> - **변형(morph·dissolve) 미사용** — 판이 «미끄러져 들어와» 덮는다. §S51 v1 반려 규칙
>
> 두 씬이 **같은 접시·같은 테이블**이라 A→B가 한 장면으로 이어진다.

---

## S08 · 쓸길이 5.86초 · 생성 6초

> VO 「까요. 그리고 금속은 빛을 통과시키지 않습니다. 이 두 조건은 동시에 만족될 수 없어 보였습니다.」


```
Split composition on white: left, a fully sealed steel box, dark and closed. Right, the
same box with an open rectangular window, cyan wave traces spilling out of it.
BEAT 1: both states sit side by side, equally lit.
BEAT 2: both dim by a third and the gap between them narrows, the two states pressing
toward each other without meeting.
CAMERA: static framing with a 1.05x macro push-in over the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral museum white, cool and clean.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S09 · 쓸길이 5.87초 · 생성 6초

> VO 「이야기는 부엌이 아니라 전쟁터에서 시작합니다. 제이차 세계대전, 영국은 밤하늘로 들」


```
Night sky seen from ground level, heavy overcast cloud lit from below by a faint
unseen source. No aircraft visible, no landmarks, no horizon detail.
BEAT 1: the cloud mass drifts, dense and featureless.
BEAT 2: a thin sweep of pale light passes across the cloud base and fades.
CAMERA: macro push-in of 1.2x on the cloud mass across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: desaturated khaki, cool cast, wartime document tone.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S10 · 쓸길이 5.87초 · 생성 6초

> VO 「어오는 폭격기를 찾아내야 했습니다. 눈으로는 보이지 않으니 다른 감각이 필요했습니」


```
A wartime parabolic radar antenna on a steel mast, shot from ground level looking up at
a 30 degree angle, silhouetted against the overcast night sky.
BEAT 1: the dish sits angled at the sky, its lattice struts readable against cloud.
BEAT 2: the dish rotates on its mount, sweeping through roughly 60 degrees.
CAMERA: orbit 30 degrees to the right around the mast across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: desaturated khaki, cool cast, wartime document tone.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S11 · 쓸길이 5.87초 · 생성 6초

> VO 「다. 그래서 만든 것이 레이더입니다. 전파를 쏘고, 되돌아오는 신호로 물체의 위치를 읽는」


```
A round cathode ray radar scope in a bakelite housing on a steel bench, viewed at a
20 degree tilt. Green phosphor face, a single radial sweep line rotating.
BEAT 1: the sweep line completes one full rotation, phosphor trailing behind it.
BEAT 2: on the second rotation a small bright return appears at the upper left.
CAMERA: macro push-in tightening from full housing to scope face only.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: desaturated khaki, cool cast, wartime document tone.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S12 · 쓸길이 5.87초 · 생성 6초

> VO 「장치. 문제는 출력이었습니다. 멀리 있는 항공기를 잡아내려면 아주 강한 전파가 필요했고,」


```
Extreme macro on the green phosphor face of the radar scope, the individual grain of the
coating visible, one bright return blooming and decaying.
BEAT 1: focus rests on the sweep line as it crosses frame.
BEAT 2: focus shifts to the bright return, which brightens then decays to nothing.
CAMERA: rack focus from sweep line to return, completing at 4 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: desaturated khaki, cool cast, wartime document tone.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S13 · 쓸길이 5.87초 · 생성 6초

> VO 「그걸 만들어내는 부품이 마그네트론이었습니다. 손바닥만 한 금속 덩어리. 그 안에서 전」


```
A cavity magnetron on a plain steel workbench: a heavy copper cylinder with radial
cooling fins, a ceramic insulator collar and two stub terminals. Palm sized, machined,
oxidised copper with tool marks.
BEAT 1: the block sits alone on the bench, fins catching a hard raking light.
BEAT 2: the light shifts and the ceramic collar picks up a cool highlight.
CAMERA: orbit 40 degrees to the right at bench height across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: desaturated khaki, cool cast, wartime document tone.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S14 · 쓸길이 5.87초 · 생성 6초

> VO 「자가 자기장에 밀려 원을 그리며 돌고, 그 회전이 전파를 뿜어냅니다. 전쟁 내내 이 부품은」


```
Cross section of the magnetron interior on white: a central cathode pin ringed by eight
resonant cavities cut into solid copper, shown as a clean machined cutaway.
BEAT 1: the cavity ring sits still, copper surfaces crisp.
BEAT 2: thin luminous traces spiral outward from the centre pin, curving into the cavities.
CAMERA: top-down framing with a 1.3x macro push-in across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: desaturated khaki, cool cast, wartime document tone.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S15 · 쓸길이 5.87초 · 생성 6초

> VO 「가장 중요한 군수품 중 하나였습니다. 그리고 전쟁이 끝났습니다. 생산 설비는 그대로 남」


```
Top-down view of a factory pallet packed with dozens of identical magnetrons in rows,
each seated in a moulded fibre tray, on a concrete floor.
BEAT 1: the full grid of units fills frame, uniform and dense.
BEAT 2: a shadow edge travels across the pallet from left to right.
CAMERA: top-down lateral dolly of 25 centimetres to the right across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: desaturated khaki, cool cast, wartime document tone.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S16 · 쓸길이 5.87초 · 생성 6초

> VO 「았고, 주문은 사라졌습니다. 수천 대를 만들던 라인이 멈춰 섰습니다. 미국의 레이시온이라」


```
A stopped factory conveyor in an empty assembly hall, steel rollers bare, one abandoned
fibre tray left on the belt. Dust suspended in a shaft of window light.
BEAT 1: the belt is motionless, dust drifting through the light shaft.
BEAT 2: the light shaft dims as if cloud passed, the hall flattening to grey.
CAMERA: lateral dolly 40 centimetres along the conveyor across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: desaturated khaki, cool cast, wartime document tone.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S17 · 쓸길이 5.87초 · 생성 6초

> VO 「는 회사에서, 한 기술자가 작동 중인 마그네트론 앞에 서 있었습니다. 퍼시 스펜서. 그날 그」


```
A magnetron mounted in an open test rig on a laboratory bench, cables running to an
off-frame supply. The bench is otherwise empty, the stool beside it unoccupied.
BEAT 1: the rig sits powered, the needle on the bench meter resting at the low end of its dial.
BEAT 2: the needle rises and settles, the copper block and the air around it unchanged.
CAMERA: macro push-in of 1.5x onto the magnetron across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: desaturated khaki, cool cast, wartime document tone.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S18 · 쓸길이 5.87초 · 생성 6초

> VO 「는 주머니에 넣어둔 간식이 녹아 있는 것을 발견합니다. 불도 없었고, 뜨겁다는 느낌도 없」


```
Macro on a paper-wrapped confectionery bar lying on the laboratory bench, the wrapper
torn open along one side, the contents collapsed into a soft glossy pool.
BEAT 1: the melt sits still, surface reflecting the overhead light.
BEAT 2: a slow sag continues at one edge, the pool creeping a few millimetres.
CAMERA: rack focus from the bench grain to the melted surface, completing at 3 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: desaturated khaki, cool cast, wartime document tone.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S19 · 쓸길이 5.87초 · 생성 6초

> VO 「었는데 말이죠. 그는 옥수수 알갱이를 가져와 장치 앞에 놓아봅니다. 팝콘이 튀어 오릅니다.」


```
Macro on a scatter of dried corn kernels on the steel bench in front of the test rig,
shot at kernel height with a wide aperture.
BEAT 1: the kernels sit still, one beginning to split at its hull.
BEAT 2: three kernels burst upward in high speed, white flesh unfurling mid air.
CAMERA: static framing at kernel height, 120fps captured motion played back at 30fps.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: desaturated khaki, cool cast, wartime document tone.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S20 · 쓸길이 4.29초 · 생성 6초

> VO 「보통의 이야기는 여기서 끝납니다. 우연한 발견, 그리고 발명. 그런데 실」


```
A tall commercial cabinet appliance on a neutral grey floor, shot straight-on: a steel
cabinet the height of a wardrobe with a single small door in its upper half, riveted
panels, industrial latch hardware, no markings of any kind.
BEAT 1: the cabinet stands alone, evenly lit, filling most of frame height.
BEAT 2: a soft shadow builds along its left flank.
CAMERA: orbit 15 degrees to the right across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S21 · 쓸길이 4.29초 · 생성 6초

> VO 「제로는 여기서부터가 문제였습니다. 음식을 데우는 데는 성공했습니다.」


```
The same steel cabinet, its small upper door standing open, a plain white plate of food
on the rack inside, shot straight-on at door height on neutral grey.
BEAT 1: the plate sits inside the open cabinet, the interior plain sheet steel.
BEAT 2: steam rises steadily from the plate and keeps rising to the end.
CAMERA: macro push-in of 1.4x from the full cabinet to the open door across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S22 · 쓸길이 4.29초 · 생성 6초

> VO 「그런데 그것을 부엌에 들여놓을 방법이 없었습니다. 이십 년 동안이나요.」


```
The steel cabinet pushed up against a standard domestic doorway frame on neutral grey.
The cabinet is visibly wider and taller than the opening.
BEAT 1: the cabinet meets the frame and stops, the mismatch obvious at both edges.
BEAT 2: the image falls to full black over the last second.
CAMERA: macro push-in of 1.2x on the contact edge, ending in blackout.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S23 · 쓸길이 5.85초 · 생성 6초

> VO 「천구백사십오년 시월 팔일, 레이시온은 특허를 출원합니다. 등록까지는 다시 오 년」


```
Top-down on an aged technical drawing sheet lying on a dark wood desk, showing a sectional
elevation of a cabinet appliance in fine ink linework. Paper is toned, slightly cockled.
BEAT 1: the full sheet fills frame, linework crisp.
BEAT 2: the frame tightens onto the sectional elevation at sheet centre.
CAMERA: top-down macro push-in of 1.6x across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S24 · 쓸길이 5.85초 · 생성 6초

> VO 「이 걸렸습니다. 그사이 회사는 첫 제품을 내놓습니다. 이름은 레이더레인지. 레이더」


```
Extreme macro across the lower corner of the same drawing sheet, where a blank rectangular
title block is ruled in ink. Inside it the date 1945.10.08 is stamped in period
typewriter ink, slightly uneven, paper fibre visible around it.
BEAT 1: focus sits on the paper grain outside the block.
BEAT 2: focus moves onto the stamped date, which fills the right half of frame.
CAMERA: rack focus from paper grain to title block, completing at 4 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S25 · 쓸길이 5.85초 · 생성 6초

> VO 「와 레인지를 합친 말이었습니다. 높이는 성인 남성의 키를 넘었습니다. 무게는 삼백사」


```
The tall steel cabinet appliance on neutral grey, with a plain vertical measuring staff
standing beside it, unmarked, reaching above the cabinet top.
BEAT 1: the cabinet and the staff stand together, cabinet top clearly the taller.
BEAT 2: a shadow sweeps down the staff from top to bottom.
CAMERA: orbit 35 degrees to the left across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S26 · 쓸길이 5.85초 · 생성 6초

> VO 「십 킬로그램이 넘었습니다. 냉장고가 아니라 옷장에 가까운 물건이었죠. 값은 오천」


```
Macro on a large round industrial weighing dial with a white face, engraved graduations
running from 0 to 400 with the unit kg printed below the spindle, and a single black
needle, mounted on a steel plate.
BEAT 1: the needle rests at zero at the bottom of its travel.
BEAT 2: the needle swings clockwise through roughly 300 degrees and settles just past
the 340 graduation.
CAMERA: macro push-in of 1.3x on the dial face across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S27 · 쓸길이 5.85초 · 생성 6초

> VO 「달러. 지금 가치로 환산하면 오천만 원이 넘습니다. 그리고 이 기계는 스스로 너무 뜨거」


```
A white price card standing upright in a small brass easel on a neutral grey surface,
$5,000 printed on it in large plain serif figures, evenly lit.
BEAT 1: the card sits square to camera, its edge shadow soft, the figures in shadow.
BEAT 2: the key light lifts and the figures resolve crisp against near paper white.
CAMERA: macro push-in of 1.25x on the card face across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S28 · 쓸길이 5.85초 · 생성 6초

> VO 「워져서, 물을 순환시켜 식혀야 했습니다. 놓으려면 배관 공사가 필요했다는 뜻입니」


```
Macro on copper cooling pipework running along the underside of a steel appliance chassis,
compression fittings and a short section of clear hose in the run.
BEAT 1: the pipe run sits still, condensation beading on the copper.
BEAT 2: water visibly moves through the clear hose section, carrying a bubble with it.
CAMERA: lateral dolly 20 centimetres along the pipe run across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S29 · 쓸길이 5.85초 · 생성 6초

> VO 「다. 이 조건을 감당할 수 있는 곳은 부엌이 아니었습니다. 대형 식당, 그리고 기내식을」


```
Cutaway of a floor section on neutral grey: tiled surface above, and below it supply and
return pipes turning upward to meet an appliance base plate.
BEAT 1: the cutaway sits still, pipe runs readable through the floor slab.
BEAT 2: the tiled upper layer lifts away a few centimetres, exposing more of the run.
CAMERA: orbit 25 degrees to the right across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S30 · 쓸길이 5.85초 · 생성 6초

> VO 「데우는 항공사 정도만 사용할 수 있었습니다. 십 년 뒤, 가정용이라는 이름을 단 제품이」


```
A commercial stainless kitchen line with empty pass-through shelves, gastronorm pans
stacked and unused, everything scrubbed and vacant.
BEAT 1: the stainless surfaces run away from camera, specular and cold.
BEAT 2: an overhead light bank steps on, lifting the whole line by a stop.
CAMERA: lateral dolly 50 centimetres along the line across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S31 · 쓸길이 5.85초 · 생성 6초

> VO 「처음 나옵니다. 여전히 크고 여전히 비쌌습니다. 거의 팔리지 않았습니다. 기술은 이」


```
A large domestic appliance cabinet on neutral grey, waist height and nearly a metre wide,
enamelled finish with a small viewing door and chrome trim, no markings.
BEAT 1: the unit sits alone, its bulk filling the lower two thirds of frame.
BEAT 2: a counter section slides in beside it, the unit still visibly deeper and taller.
ON-SCREEN: the figure 1955 in plain white sans-serif, lower left third, fading in at
2.5 seconds and holding to the end.
CAMERA: orbit 30 degrees to the right across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S32 · 쓸길이 5.85초 · 생성 6초

> VO 「미 완성되어 있었지만 팔리지 않은 이유는 기술이 아니라 전혀 다른 곳에 있었습니다.」


```
A row of eight identical domestic appliance cabinets standing in a showroom, each draped
with a plain grey dust sheet, receding from foreground to background on a neutral grey
floor. Price tags hang from the handles, the printed side turned away.
BEAT 1: the row stands still, a thin layer of dust visible on the nearest sheet.
BEAT 2: the tag on the nearest unit turns slightly in the still air.
CAMERA: lateral dolly 35 centimetres along the row across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S33 · 쓸길이 5.94초 · 생성 6초

> VO 「가장 큰 벽은 크기도 가격도 아니었습니다. 전파가 새어 나오는 것이었습니다. 그렇다고 상」


```
The sealed steel cavity model on white, cutaway wall still open, cyan wave traces
bouncing inside.
BEAT 1: the traces criss-cross the open cavity, several escaping past the cut edge.
BEAT 2: a steel panel closes the cut face and the escaping traces are cut off, the frame
falling to near black.
CAMERA: macro push-in of 1.3x on the closing face across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S34 · 쓸길이 5.94초 · 생성 6초

> VO 「자를 완전히 막으면 눈으로는 안이 보이지 않습니다. 앞쪽으로 창을 내면 전파가 나옵니다.」


```
The now sealed steel box on white, front face solid.
BEAT 1: a rectangular window opens in the front face, revealing the lit cavity within.
BEAT 2: cyan wave traces pour out through the opening toward camera and past the frame edge.
CAMERA: orbit 20 degrees to the left across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S35 · 쓸길이 5.94초 · 생성 6초

> VO 「막을 것인가, 볼 것인가. 둘 중 하나만 고를 수 있다면 이 기계는 부엌에 들어올 수 없었습니다.」


```
Split composition on white: left half a fully sealed dark steel box, right half the same
box with an open window leaking cyan traces. A hard vertical seam divides them.
BEAT 1: both halves hold, the contrast between dark and leaking plainly readable.
BEAT 2: the vertical seam brightens to a thin white line running the full frame height.
CAMERA: static framing with a 1.05x macro push-in across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S36 · 쓸길이 5.89초 · 생성 6초

> VO 「답은 전파 자체의 성질 안에 있었습니다. 세 단계로 보겠습니다. 첫째, 파장. 이 기」


```
An empty white laboratory table filling frame, seen at table height, nothing on it.
BEAT 1: the bare white surface holds, a soft falloff toward the back edge.
BEAT 2: a single luminous cyan sine wave draws itself across the table from left to right,
about one metre long with four visible crests.
ON-SCREEN: the numeral 1 in plain dark sans-serif, upper left third, fading in at
1 second and holding to the end.
CAMERA: macro push-in of 1.15x across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S37 · 쓸길이 5.89초 · 생성 6초

> VO 「계가 쓰는 전파의 파장은 약 십이 센티미터입니다. 손바닥 하나 크기죠. 전자기파」


```
The cyan sine wave lying on the white table, with a steel rule graduated in centimetres
placed parallel beneath one full crest-to-crest span.
BEAT 1: the rule slides in from the right and aligns under a single wave period.
BEAT 2: that one period brightens while the rest of the wave dims by half, and a thin
dimension line spans it labelled 12 cm in plain dark sans-serif.
CAMERA: top-down framing with a 1.3x macro push-in across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S38 · 쓸길이 5.89초 · 생성 6초

> VO 「에는 규칙이 하나 있습니다. 자기 파장보다 뚜렷하게 작은 구멍은 통과하지 못한」


```
A thin drawn line of luminous cyan light lying on the white table in the shape of a sine
curve, the same line as in the wavelength shot, identical in colour and line weight. An
upright perforated steel plate stands across its path, holes about 1.5 millimetres across.
BEAT 1: the whole drawn line slides to the right along the table until its leading end
reaches the plate face.
BEAT 2: the line rebounds off the plate and slides back to the left, the outgoing and
returning line crossing into a stationary figure of light in front of the plate.
CAMERA: lateral dolly 20 centimetres to the right across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S39 · 쓸길이 5.89초 · 생성 6초

> VO 「다. 구멍이 뚫려 있어도 전파에게는 벽으로 보인다는 뜻입니다. 둘째, 빛. 사람이 보」


```
The perforated steel plate seen straight-on from the wave side, filling frame, its hole
lattice fully visible and lit from behind so each hole shows as a bright point.
BEAT 1: the lattice of bright points reads clearly as open holes.
BEAT 2: a cyan sheet of light washes across the plate face and is entirely turned back,
none of it passing through.
ON-SCREEN: the numeral 2 in plain white sans-serif, upper left third, fading in at
1 second and holding to the end.
CAMERA: macro push-in of 1.4x on the plate centre across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S40 · 쓸길이 5.89초 · 생성 6초

> VO 「는 빛도 같은 전자기파입니다. 다른 것은 파장뿐입니다. 그런데 그 차이가 비교가」


```
The white table with the cyan sine wave still lying along it. A second wave, warm white
and vastly finer, draws itself directly below and parallel to the first.
BEAT 1: the cyan wave holds, its four broad crests spanning the table.
BEAT 2: the white wave completes, so dense its individual crests are not resolvable at
this magnification, reading as a continuous bright line.
CAMERA: top-down framing with a 1.2x macro push-in across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S41 · 쓸길이 5.89초 · 생성 6초

> VO 「되지 않습니다. 빛의 파장은 천 분의 일 밀리미터에도 미치지 못합니다. 전파의 파」


```
Extreme macro diving into the warm white line on the table until its structure resolves
into individual crests, packed impossibly tight.
BEAT 1: the line reads as solid, no structure visible.
BEAT 2: magnification reaches the point where hundreds of individual crests resolve, a
thin dimension line spanning one crest labelled 0.0005 mm in plain white sans-serif.
CAMERA: macro push-in of 40x on the white line across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S42 · 쓸길이 5.89초 · 생성 6초

> VO 「장이 손바닥 하나라면, 빛의 파장은 그 손바닥을 이십만 조각으로 나눈 것 중 하나」


```
Top-down on a plain white rectangular tile on the table, roughly hand sized.
BEAT 1: the tile is whole, a single flat surface.
BEAT 2: a fine grid subdivides it repeatedly, each pass quartering the cells, until the
surface reads as uniform grey texture rather than countable squares.
ON-SCREEN: the figure 200,000 in plain dark sans-serif, lower right third, fading in at
4 seconds and holding to the end.
CAMERA: top-down framing with a 1.5x macro push-in across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S43 · 쓸길이 5.89초 · 생성 6초

> VO 「입니다. 그러니 전파가 막히는 구멍을 빛은 아무 저항 없이 지나갑니다. 같은 구멍」


```
The same perforated steel plate standing on the white table, seen from a three-quarter
angle so both faces are readable.
BEAT 1: warm white light approaches the plate from the far side.
BEAT 2: the light passes straight through every hole, throwing a sharp grid of bright
dots onto the table surface in front of the plate.
CAMERA: orbit 25 degrees to the right across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S44 · 쓸길이 5.89초 · 생성 6초

> VO 「이 하나에게는 벽이고, 하나에게는 활짝 열린 문입니다. 셋째, 그래서 크기. 전파를」


```
The perforated steel plate on the white table, both effects present at once: cyan traces
striking the plate face and bouncing back, warm white light streaming through the holes.
BEAT 1: the cyan reflection and the white transmission both run, clearly separable.
BEAT 2: the cyan brightens on the near side while the transmitted grid of dots sharpens
on the far side.
CAMERA: orbit 30 degrees to the left across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S45 · 쓸길이 5.89초 · 생성 6초

> VO 「막으려면 구멍이 센티미터 단위보다 작아야 합니다. 빛을 통과시키려면 천 분의」


```
Top-down on the white table where a single horizontal measuring scale is laid out, a plain
steel rule engraved in centimetres from 0 to 10. A dark band masks the scale from its
right end inward.
BEAT 1: the full rule is exposed and evenly lit.
BEAT 2: the dark band sweeps in from the right and covers everything above 1 cm.
ON-SCREEN: the numeral 3 in plain dark sans-serif, upper left third, fading in at
1 second and holding to the end.
CAMERA: top-down lateral dolly 15 centimetres to the left across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S46 · 쓸길이 5.89초 · 생성 6초

> VO 「일 밀리미터보다 크기만 하면 됩니다. 그 사이가 통째로 비어 있습니다. 고를 수 있」


```
The same steel rule top-down, now with a second dark band sweeping in from the left end.
BEAT 1: the right-hand band from the previous shot is already in place.
BEAT 2: the left band advances a very short distance and stops, leaving the great majority
of the rule between the two bands uncovered.
CAMERA: top-down macro push-in of 1.25x across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S47 · 쓸길이 5.89초 · 생성 6초

> VO 「는 폭이 이만큼 넓다는 것, 그게 답이었습니다. 그래서 실제로 고른 값은 지름 일 밀」


```
Top-down on the steel rule with both dark bands in place and a wide open gap between them.
BEAT 1: the uncovered middle span holds, plainly the largest region in frame.
BEAT 2: the uncovered span lifts in brightness to near paper white while both bands sink
to deep grey.
CAMERA: top-down framing with a 1.1x macro push-in across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S48 · 쓸길이 5.89초 · 생성 6초

> VO 「리미터에서 이 밀리미터 사이입니다. 막아야 하는 선보다 한참 아래로 잡았습니」


```
Extreme macro on three adjacent perforations in the steel plate, the machined rim burr and
surface grain of the metal fully resolved.
BEAT 1: the three holes sit in a row, focus even across all three.
BEAT 2: focus narrows onto the centre hole, a thin dimension line spanning its diameter
labelled 1-2 mm in plain white sans-serif, the outer two holes falling soft.
CAMERA: rack focus from the outer holes to the centre hole, completing at 4 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S49 · 쓸길이 5.89초 · 생성 6초

> VO 「다. 구멍이 커질수록 새어 나오는 양이 가파르게 늘기 때문에, 여유를 크게 둔 겁니」


```
The perforated plate on the white table, seen three-quarter, cyan traces striking it.
BEAT 1: with small holes, every trace is turned back at the face.
BEAT 2: the holes visibly widen to several millimetres and cyan traces begin streaming
through in growing numbers, the leak accelerating over the last two seconds.
CAMERA: macro push-in of 1.5x on the plate across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S50 · 쓸길이 5.89초 · 생성 6초

> VO 「다. 그렇게 해서 금속판 한 장이 전파에게는 막힌 벽이고 빛에게는 뚫린 창이 됩니」


```
The perforated plate restored to small holes, standing alone on the white table, seen
straight-on and lit from behind.
BEAT 1: the hole lattice glows with transmitted white light, fully open to the eye.
BEAT 2: cyan traces arrive at the near face and are all turned back, the transmitted
white grid unaffected.
CAMERA: macro push-in of 1.3x on the plate centre across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral warm gray, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S51 · 쓸길이 5.89초 · 생성 6초

> VO 「다. 막으면서 동시에 보이는 판. 이게 여러분이 매일 들여다보는 그 금속망입니다.」


```
Macro of the perforated metal shield inside a microwave oven door, seen through the door
glass, the hole lattice filling the entire frame, holes roughly 1.5 millimetres across in
a regular grid, brushed silver steel.
BEAT 1: the door glass surface catches a faint sheen in front of the lattice.
BEAT 2: the sheen fades and focus settles fully on the metal, the lattice filling frame
exactly as in the opening macro.
CAMERA: macro push-in of 1.2x across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, the khaki cast fully gone.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S52 · 쓸길이 5.47초 · 생성 6초

> VO 「그리고 저 십이 센티미터가 정한 것이 하나 더 있습니다. 파장이 이만큼 길」


```
Interior of the steel cavity seen through its cutaway wall, where cyan energy has settled
into a standing pattern: alternating bright and dark horizontal bands across the volume.
BEAT 1: the bands resolve out of the moving traces and lock into place.
BEAT 2: the bright bands intensify while the dark ones deepen to near black.
CAMERA: macro push-in of 1.3x into the cavity across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S53 · 쓸길이 5.47초 · 생성 6초

> VO 「면 상자 안에 전파가 겹쳐 세지는 자리와 약해지는 자리가 생깁니다. 약한 자」


```
Top-down on the cavity floor, the standing wave pattern projected onto it as a regular
grid of bright and dark patches.
BEAT 1: the patch grid holds across the floor plate.
BEAT 2: the pattern drifts by half a cell and settles, bright and dark swapping places.
CAMERA: top-down macro push-in of 1.4x across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S54 · 쓸길이 5.47초 · 생성 6초

> VO 「리에 놓인 음식은 익지 않습니다. 그래서 음식을 돌립니다. 천구백육십육년,」


```
Macro on a ceramic dish of food sitting on the cavity floor across two of the dark
patches, seen at plate height.
BEAT 1: steam rises from one side of the dish only, the other side flat and cold.
BEAT 2: the cold side stays visibly untouched while the steaming side thickens.
CAMERA: lateral dolly 10 centimetres to the right across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S55 · 쓸길이 5.47초 · 생성 6초

> VO 「회전판이 처음 달립니다. 구멍이 저 크기인 것도, 음식이 도는 것도, 디자이너」


```
The glass turntable plate seated on its roller ring on the cavity floor, the standing
wave patches visible on the floor beneath it.
BEAT 1: the plate sits still, one dish riding on it over a dark patch.
BEAT 2: the plate turns through roughly 180 degrees, carrying the dish across several
bright and dark patches in turn.
ON-SCREEN: the figure 1966 in plain white sans-serif, lower left third, fading in at
2.5 seconds and holding to the end.
CAMERA: top-down framing with a 1.2x macro push-in across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S56 · 쓸길이 5.47초 · 생성 6초

> VO 「의 취향이 아닙니다. 전파와 빛 사이에 그만한 틈이 있었고, 그 전파의 파장」


```
Split composition on neutral white: left, extreme macro of the perforated hole lattice.
Right, top-down of the turning glass plate on its roller ring.
BEAT 1: both halves run, the lattice still and the plate turning.
BEAT 2: a thin cyan line traces from the hole lattice across the seam to the turning
plate, connecting the two.
CAMERA: static framing with a 1.08x macro push-in across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S57 · 쓸길이 5.47초 · 생성 6초

> VO 「이 십이 센티미터였다는 것. 안을 확인하는 그 순간에도, 구멍들은 전파를 안」


```
Top-down on the white table with the cyan sine wave laid out beside the perforated steel
plate, one full wave period and the hole spacing in the same frame.
BEAT 1: both sit still, the scale difference between them plainly readable.
BEAT 2: the wave period and the hole lattice each pulse once, in turn, a thin dimension
line spanning the wave period labelled 12 cm in plain dark sans-serif.
CAMERA: top-down macro push-in of 1.3x across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S58 · 쓸길이 5.47초 · 생성 6초

> VO 「쪽으로 되돌려 보내고 있습니다. 이 구조가 자리를 잡자 기계는 빠르게 작아」


```
Extreme macro on the microwave door shield from the cavity side, holes filling frame,
warm interior light behind camera.
BEAT 1: the lattice holds, each hole a bright point of transmitted light.
BEAT 2: cyan traces strike the lattice from the cavity side and reflect back inward,
away from camera.
CAMERA: macro push-in of 1.35x on the lattice across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S59 · 쓸길이 5.47초 · 생성 6초

> VO 「집니다. 냉각용 배관이 사라지고, 부품이 줄고, 가격이 내려갑니다. 천구백육」


```
An exploded assembly of a large appliance chassis on neutral white, its cooling pipework,
transformer, and structural frame floating apart in ordered layers.
BEAT 1: all layers hang in place, the assembly at its largest.
BEAT 2: the pipework layer and two structural layers fade out and the remaining parts
draw together into a body roughly half the original size.
CAMERA: orbit 30 degrees to the right across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S60 · 쓸길이 5.47초 · 생성 6초

> VO 「십칠년, 마침내 조리대 위에 올라가는 제품이 사백구십오 달러에 나옵니다.」


```
A compact countertop microwave oven standing on a domestic kitchen counter, neutral white
surround, enamelled body with a viewing door and a mechanical dial, no markings.
BEAT 1: the unit sits square to camera, the counter running away behind it.
BEAT 2: the interior lamp behind the door glass warms up, the mesh reading through it.
ON-SCREEN: the figures 1967 upper left third and $495 lower right third, both plain white
sans-serif, 1967 fading in at 1.5 seconds and $495 at 3.5 seconds, both holding to the end.
CAMERA: orbit 35 degrees to the right across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S61 · 쓸길이 5.76초 · 생성 6초

> VO 「이후는 빠릅니다. 천구백칠십일년, 미국 가정 백 집 중 한 집. 천구백팔십육년」


```
A line chart rendered as a physical raised ribbon on a neutral white plane, seen at a
25 degree angle. The ribbon runs from the left foreground, flat against the base.
BEAT 1: the flat left section holds, barely lifted off the plane.
BEAT 2: the ribbon begins to climb, still shallow, extending toward the background.
ON-SCREEN: the year 1971 set flat on the base plane beneath the ribbon start, and 1% set
beside the ribbon at that point, both plain dark sans-serif, present from 1 second.
CAMERA: lateral dolly 30 centimetres to the right along the ribbon across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S62 · 쓸길이 5.76초 · 생성 6초

> VO 「에는 네 집 중 한 집. 천구백구십칠년에는 열 집 중 아홉 집이 이 기계를 가지고 있」


```
The same raised ribbon chart, the camera now further along its run where the climb steepens.
BEAT 1: the ribbon rises through the mid range at a moderate slope.
BEAT 2: the slope steepens sharply and the ribbon reaches near the top of the plane.
ON-SCREEN: two labelled stops set flat on the base plane beneath the ribbon, 1986 with 25%
at the mid point and 1997 with 90% near the top, all plain dark sans-serif, the first
present from 1 second and the second appearing at 3.5 seconds.
CAMERA: lateral dolly 40 centimetres to the right along the ribbon across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S63 · 쓸길이 5.76초 · 생성 6초

> VO 「었습니다. 그러는 사이 식탁도 바뀝니다. 얼렸다가 데우기만 하면 되는 음식」


```
Top-down on a domestic dining table, neutral daylight, a single place setting with an
empty plate, cutlery, and a glass.
BEAT 1: the setting sits complete and still.
BEAT 2: a sealed rectangular tray meal is set down onto the plate position, its film lid
taut and reflective.
CAMERA: top-down macro push-in of 1.2x across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S64 · 쓸길이 5.76초 · 생성 6초

> VO 「이라는 산업이 이때 만들어집니다. 한국에서는 천구백칠십팔년에 처음 생산」


```
A supermarket frozen food aisle, upright glass-door freezer cabinets packed with identical
boxed meals, cold blue-white interior lighting, aisle empty.
BEAT 1: the cabinet run recedes down the aisle, doors frosted at their lower edges.
BEAT 2: condensation on one door clears from the centre outward, revealing packed rows.
CAMERA: lateral dolly 60 centimetres down the aisle across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S65 · 쓸길이 5.76초 · 생성 6초

> VO 「됩니다. 가격은 삼십구만 사천 원. 이듬해 팔월까지 전국에 보급된 것은 사백 대」


```
Top-down on a boxy domestic microwave oven of late 1970s design on a neutral surface:
enamelled steel body, mechanical timer dial, a small viewing door, no markings.
BEAT 1: the unit sits centred, its proportions notably deeper than modern units.
BEAT 2: a soft shadow sweeps across the top panel from left to right.
ON-SCREEN: the figure 1978 in plain dark sans-serif, lower left third, fading in at
2.5 seconds and holding to the end.
CAMERA: top-down macro push-in of 1.3x across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S66 · 쓸길이 5.76초 · 생성 6초

> VO 「남짓이었고, 그마저도 가정이 아니라 제과점과 경양식집이 사간 것이었습」


```
Two physical extruded bars standing side by side on a neutral white plane, seen at a
20 degree angle. Both start flush with the base.
BEAT 1: the right bar rises to roughly half the frame height and stops.
BEAT 2: the left bar rises past it to nearly twice that height and stops.
ON-SCREEN: 394,000 set on the base plane at the foot of the left bar and 210,000 at the
foot of the right bar, both plain dark sans-serif, each appearing as its bar finishes rising.
CAMERA: orbit 20 degrees to the right across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S67 · 쓸길이 5.76초 · 생성 6초

> VO 「니다. 그로부터 몇 해 뒤, 한국은 마그네트론을 직접 만들기 시작합니다. 천구백」


```
Macro along a bakery display case, glass front, trays of pastries and bread on stepped
shelves under warm tungsten light, no people.
BEAT 1: focus sits on the glass surface with its faint smears and reflections.
BEAT 2: focus travels through to the pastry trays behind it.
CAMERA: rack focus from glass to trays, completing at 4 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S68 · 쓸길이 5.76초 · 생성 6초

> VO 「팔십삼년, 수원에 세워진 공장은 세계에서 세 번째로 큰 규모였습니다. 전쟁터」


```
Top-down on a factory assembly line, a long conveyor carrying identical magnetron units in
moulded trays, overhead industrial lighting, concrete floor, no people.
BEAT 1: the line runs, trays advancing steadily through frame.
BEAT 2: the framing reveals more of the hall, further parallel lines running alongside.
ON-SCREEN: the figure 1983 in plain white sans-serif, lower left third, fading in at
2.5 seconds and holding to the end.
CAMERA: top-down lateral dolly 80 centimetres along the conveyor across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S69 · 쓸길이 5.76초 · 생성 6초

> VO 「에서 폭격기를 찾아내던 그 부품입니다. 천구백팔십구년에는 한국 회사 두」


```
A cavity magnetron on a plain steel workbench: a heavy copper cylinder with radial cooling
fins, a ceramic insulator collar and two stub terminals. Palm sized, machined copper.
Identical framing, lens and bench to the earlier magnetron shot, but in clean neutral
white grade rather than khaki.
BEAT 1: the block sits alone on the bench, fins catching a hard raking light.
BEAT 2: the light shifts and the ceramic collar picks up a cool highlight.
CAMERA: orbit 40 degrees to the right at bench height across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S70 · 쓸길이 5.76초 · 생성 6초

> VO 「곳이 미국에서 팔리는 전자레인지의 삼분의 일 이상을 대고 있었습니다. 전파」


```
Top-down on a dockside container yard, stacked shipping containers in ordered rows,
overcast daylight, no people or vehicles.
BEAT 1: the container grid fills frame, colours muted and uniform.
BEAT 2: roughly a third of the containers in frame lift in brightness by a stop while the
rest sink slightly.
ON-SCREEN: the fraction 1/3 in plain white sans-serif, lower left third, fading in at
3 seconds and holding to the end.
CAMERA: top-down lateral dolly 70 centimetres across the yard over the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S71 · 쓸길이 5.76초 · 생성 6초

> VO 「를 가두는 문제를 푼 대가로, 인류는 처음으로 불 없이 음식을 익히게 됐습니다.」


```
A plate of food on a neutral white counter beside a conventional gas hob, the hob burners
cold and unlit, no flame anywhere in frame.
BEAT 1: the unlit burner ring sits in the foreground, the plate behind it.
BEAT 2: steam rises steadily from the plate while the burner stays dark and cold.
CAMERA: rack focus from the cold burner to the steaming plate, completing at 4 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral white, even and undramatic.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S72 · 쓸길이 4.96초 · 생성 6초

> VO 「영상 맨 처음에 봤던 그 문을 다시 보겠습니다. 구멍이 촘촘히 뚫」


```
A plain white countertop microwave oven on a clean kitchen shelf, shot straight-on at
appliance height against a neutral museum-white wall. Identical framing, lens and
lighting to the opening shot of the film.
BEAT 1: the closed door faces camera, the interior lamp already warm behind the glass.
BEAT 2: focus travels through the glass onto the perforated metal sheet behind it.
CAMERA: macro push-in that tightens from full appliance to door-only across the 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral museum white, cool and clean, identical to the opening.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S73 · 쓸길이 4.96초 · 생성 6초

> VO 「린 금속판 한 장. 가두는 것과 보는 것을 동시에 해내야 했던 문제」


```
Macro of the perforated shield inside the door, the hole lattice filling frame, matching
the opening macro shot exactly in scale and position.
BEAT 1: the lattice reads as a flat silver field, each hole a dark dot.
BEAT 2: cyan traces appear behind the lattice and strike it from within, every one turned
back, none passing through toward camera.
CAMERA: static framing with a 1.06x macro push-in across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral museum white, cool and clean, identical to the opening.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S74 · 쓸길이 4.96초 · 생성 6초

> VO 「에 대한, 이십 년 만의 답입니다. 누군가 이십 년을 들여 풀었고, 우」


```
The same macro of the perforated shield, cyan traces still striking it from within.
BEAT 1: the traces run at full strength against the lattice.
BEAT 2: the traces fade out completely, leaving only the plain metal lattice, unchanged.
CAMERA: static framing with a 1.06x macro push-in across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral museum white, cool and clean, identical to the opening.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```


## S75 · 쓸길이 4.96초 · 생성 6초

> VO 「리는 답만 받았습니다. 문제는 사라졌고, 답이 부엌에 남았습니다.」


```
Pulling back from the perforated lattice to the full door, then to the whole appliance on
its kitchen shelf, arriving at exactly the opening composition of the film.
BEAT 1: the lattice recedes and the door glass and trim come into frame.
BEAT 2: the full appliance settles into frame, the shelf and wall around it, the interior
lamp switching off in the final second.
CAMERA: macro pull-back from lattice to full appliance across the full 6 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, soft large diffused key from upper left with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. GRADE: neutral museum white, cool and clean, identical to the opening.
The set is unattended: every frame shows objects only, with no person, hand or face present. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: room tone and mechanical sound only, no music and no voice.
```
