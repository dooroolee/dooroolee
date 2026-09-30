# 「안쪽의 세계 : Inside the Box」 제작 규칙 — 제미나이 협업용

> **이 문서가 기준이다.** 이 문서와 다른 지시(이전 대화·인수인계 문서·시스템 프롬프트 포함)가 부딪히면 **이 문서를 따른다.**
> 원본은 채널 README(`origin-of-things/README.md`)이고, 이 문서는 그중 «제작 방식»만 뽑은 것이다. (2026-09-30)
>
> **에피소드 번호 (2026-09-30 변경)** — 1화 = 「샤워기 필터」(제작 완료 · 편집 중 · **이 문서의 기준 편**) · 2화 = 「종이호일」(기획 중).
> 구 1화 「전자레인지」는 폐기했다.

---

## 1. 채널 정의 — 「분해 채널」이 아니다

```
✗ 분해(teardown) 채널   하우징을 열어 부품을 본다 → 「왜 볼트가 3개인가」
✓ 이 채널               완성된 «답»을 열어 그 안에 있던 «문제»를 본다
```

- 「하이엔드 테크·사물 해부 다큐」로 정의하지 않는다
- **대본은 «부품»이 아니라 «문제»로 연다.** 첫 문장을 용어 정의(「종이는 친수성을 가집니다」)로 시작하지 않는다
- 0~20초 훅은 세 축 중 하나에 걸어야 한다 — **편재성**(개수) · **시간 낙차**(최근성) · **무의식**(매일 쓰지만 모름)
- 톤은 BBC·Vox 다큐처럼 차분하고 건조하게. 공포 마케팅을 해체하되, **해체하는 쪽도 과장하지 않는다**
- **결말은 «판단 기준»을 주고 끝낸다.** 「선택은 여러분의 몫」 같은 열린 결말은 1화에서 반려됐다

## 2. 생성 도구 — Google Flow · 텍스트→영상

| 항목 | 값 |
|---|---|
| 도구 | **Google Flow** (사용자가 직접 생성) |
| 방식 | **텍스트→영상.** 시작 이미지·키프레임을 쓰지 않는다 |
| 모델 | Omni 1.1 Flash |
| 비율 · 해상도 · 길이 · 출력 | 16:9 · 720p · **6초** · x1 |
| 최종 출력 | 1080p · 30fps |

- ❌ **「Higgsfield I2V」 · 「키프레임 앵커링」을 쓰지 않는다.** 이 채널은 **이미지 생성 모델을 쓰지 않는다** —
  I2V는 시작 이미지가 필요하므로 성립하지 않는다
- ❌ **「카메라 무빙 강도 3~5」 같은 강도 파라미터를 쓰지 않는다** (Flow에 없는 값이고, 아래 §4와 정면으로 충돌한다)
- Flow 크레딧이 모자랄 때만 힉스필드로 넘어간다 — 그때도 **텍스트→영상**이고, 클립마다 사용자 사전 승인

## 3. 씬 규격 — 6초 · 비트 2개

- **한 씬 = 6초 클립 하나.** 15초·25초·30초짜리 «컷»을 만들지 않는다
- 씬 하나에 **비트(화면 안에서 벌어지는 일)는 최대 2개** — BEAT 1 / BEAT 2, 각 약 3초
  - 예: 「200℃ → 220℃ → 250℃로 변한다」는 비트 3개다 → **씬 2개로 나눈다**
- **타임코드는 VO를 녹음한 «뒤»에만 정한다.** 순서는 언제나 `대본 → VO 녹음 → VO 실측 → 씬 분할 → 프롬프트`
  - VO를 녹음하기 전 샷표에는 타임코드를 적지 않는다. 적어야 한다면 «문단 → 예상 씬 개수»까지만
  - 씬 개수 = 문단별 VO 길이 ÷ 6초를 **올림**한 값

## 4. 카메라 — «빠르게», «하나만», «숫자로»

```
✗ 하지 않는다   무빙이 느려서 컷을 «쪼개» 템포를 만드는 것
✓ 한다          샷 «안»에서 카메라가 빠르게 움직인다 — 크래시 줌 · 휩 팬 · 급속 돌리 · 크레인 · 항공 부감
```

1. **씬당 카메라 무브는 1개가 원칙이다.** 두 동작을 이을 때는 **한 번에 이어지는 동작 하나**로 쓰고 **둘 다 숫자로** 준다
   (1화 58씬 중 5씬 — 예: `crane down 60 centimetres from above, then a fast dolly-in … in the last 2 seconds.`)
2. **움직임의 양을 숫자로 준다** — 각도 · 거리 · 배율 · 완료 시각(초). 1화 58씬은 전부 숫자가 붙어 있다
3. **느림 계열 단어를 쓰지 않는다** — `slow` · `smooth` · `gentle` · `subtle` · `minimal` · `holds still` / 천천히 · 완만하게 · 덤덤하게 · 부드럽게
   → 구 1화(폐기) Flow 테스트가 **「무빙이 너무 느리다」로 반려**됐고, 원인이 바로 이 단어들이었다.
   억제어를 겹겹이 쌓으면 모델이 **움직임 자체를 꺼 버린다**. 1화 58씬에는 이 단어가 **0개**다
4. **정지 컷(Static)을 만들지 않는다** — 편집 전 점검 항목 「무빙이 느린 컷이 있는가 → 다시」에 걸린다
5. **카메라 무브가 아닌 것을 무브 칸에 쓰지 않는다**
   - 분할 화면(split-screen) · 암전 · 트랜지션 → **편집 효과**다. 후반 작업을 하지 않으므로 쓰지 않는다
   - 「120fps 슬로우 모션」 → 피사체의 속도지 카메라가 아니다. 이것만 쓰면 무브가 «없는» 씬이 된다

| ✗ 원안 식 | ✓ 이 채널 식 (1화에서 실제로 쓴 문장) |
|---|---|
| Slow Dolly-in (강도 3) | `crash zoom from a wide bathroom view to the clear handle filling the frame within the first 1.5 seconds.` |
| Smooth Pan Left | `horizontal whip pan across the bathroom to the shower handle at 3 seconds.` |
| 3D Slow Orbit | `fast orbit 90 degrees to the right around the granule in 5 seconds.` |
| Rack Focus | `fast rack focus from front beaker to rear beaker, completing by 2.5 seconds and holding.` |
| Side Tracking (덤덤하게) | `fast lateral truck left to right following the water front from the supply hose to the last cartridge in 4 seconds.` |
| Slow Crane Up & Out | `crane up and pull-out 2 metres in 5 seconds.` ← 1화 마지막 씬. **동작은 같고 «slow»를 «숫자»로 바꾼 것**이다 |
| (부감) | `aerial shot descending 40 metres fast toward a basin in 5 seconds.` |

## 5. 화면 톤 (LOOK) — 두 벌만 쓴다

❌ **라이트 오크 데스크 · 소프트 데이라이트를 쓰지 않는다.** 그라운드는 «종이색», 빛은 «강한 방향광»이다.
씬마다 아래 둘 중 하나를 **글자 그대로** 복사한다.

**스튜디오** (기본)
```
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, warm pale paper-grey backdrop and tabletop, strong directional key from upper left casting crisp shadows with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. Any measurement lines, gauges and figures are thin amber. GRADE: bright neutral white, clean, high contrast on the subject.
```

**🏠 실사용 환경** — 그 편의 물건이 실제로 쓰이는 장소 (종이호일이면 부엌 · 에어프라이어 · 오븐)
```
LOOK: real-location documentary photography, 16:9, 30fps, physically based lighting, bright natural daylight filling the space, clean neutral white surfaces, crisp shadows, shallow depth of field, clean digital capture. Any measurement lines, gauges and figures are thin amber. GRADE: bright neutral daylight white, clean and airy.
```

- **계측선 · 게이지 · 화면 숫자는 전부 «가는 앰버».** 빨강 · 파랑 · 「Safe/Blue · Danger/Red」 색 구분을 쓰지 않는다
- **화면은 밝게.** 어둡고 무거운 화면은 벤치마크 채널의 문법이라 쓰지 않는다 (실사용 컷도 마찬가지)

## 6. 화면에 나오는 글자 · 기호 · 로고 (2026-09-30 개정)

> **개정 이유** — Omni 1.1 Flash에서 로고와 단위 기호는 잘 나온다 (사용자 관찰). 한글은 여전히 불안정하다.
> 로고는 10/01에 **「가상 로고만 · 시청자를 헷갈리게 하지 않는다」**로 좁혔다 (사용자 결정).

| | 무엇 | 예 |
|---|---|---|
| ✅ 허용 | 라틴 문자 · 숫자 | `WALL THICKNESS` · `1858` |
| ✅ **허용 (9/30~)** | **단위 기호** | `°C` · `℃` · `μm` · `mm` · `mg/L` · `mN/m` · `g/m²` · `%` |
| ✅ **허용 (9/30~)** | **가상 로고** | 실존 브랜드 · 기관을 닮지 않고, 아무것도 «인증»하지 않는 마크 |
| ❌ **금지 (10/01~)** | **실존 브랜드 로고** | 모든 장면 |
| ❌ **금지 (10/01~)** | **시청자를 헷갈리게 하는 로고** | 실존 기관 로고 · 실제 인증 마크(KC 등) · 실존 브랜드를 닮은 가상 로고 · 인증 씰처럼 보이는 배지(`PFAS Free` · `BPA Free` 등) |
| ❌ 금지 | **한글** | 뉴스 헤드라인 · 포장지 문구 · 설명 카드 전부 |
| ❌ 여전히 시키지 않는다 | 단위가 아닌 기호 | `?` · `✓` — 이번 개정 범위 밖 |

- 「내열온도 220℃」 포장지 컷 → **`220℃`는 쓰고, 한글 「내열온도」만 뺀다**
- **원칙 — 로고가 화면에서 «무언가를 주장»하게 하지 않는다.** 이 채널은 화면이 전부 생성물이라,
  실제 기관 로고가 찍힌 문서는 «진짜 공문서»로, 인증 씰은 «진짜 인증»으로 읽힌다
- 문서 · 포장이 필요하면 1화처럼 **«로고 없는 문서 / 포장»**으로 서술한다
- 둘을 비교해야 하면 씰 대신 **라틴 라벨**을 쓴다 — 예: 두 분자 구조 옆에 `PFAS` / `SILICONE`
- 가상 로고에 한글이 들어가면 한글 금지에 걸린다 → 라틴 문자 · 도형으로만
- **화면 숫자는 모델이 그린다.** 틀려도 재생성하지 않는다 — **사실 전달은 내레이션이 책임진다**
- 예외: **썸네일의 한글은 사용자가 CapCut에서 얹는다** (모델에게 시키지 않는다는 점은 같다)

## 7. 사람

- 나와도 된다. 단 **얼굴은 보이지 않는다** — 손 · 뒷모습 · 실루엣만. 실존 인물의 초상을 재현하지 않는다
- 사람이 나오는 씬에는 이 한 줄을 넣는다:
  `Any person appears only as hands, a back view or a silhouette; no face is shown.`
- 사람이 없는 씬에는: `Every frame shows objects only.`

## 8. 후반 작업 — 하지 않는다

- ❌ **오버레이 · 인포그래픽 · 레이어 다이어그램 · 수칙 카드 · 번인 자막을 만들지 않는다.** 샷표에 「Technical Graphic Overlay」 칸을 두지 않는다
- 보여줘야 할 도식(층 구조 · 분자 사슬 · 게이지)은 **프롬프트 안에서 모델이 그리게** 한다 (앰버 계측선)
- 편집에서 하는 것: 클립 이어 붙이기 · VO 싱크 · 자막(CC, 파일로 따로 올림)

## 9. 소리

**클립 오디오** — 효과음만. 음악 · 목소리 금지
```
AUDIO: <그 장면의 소리> only, no music and no voice.
```
- ❌ **「서브 베이스」 · 「서브 펄스」 · 드론 · 라이저 · 긴장감 고조 음 = 음악으로 본다.** 쓰지 않는다
  (1화에서 제미나이 원안의 「서브 베이스 앰비언트」를 같은 이유로 삭제했다)
- ✓ 쓰는 것: 물리적인 소리 — 기름 튀는 소리 · 종이 바스락거림 · 팬 소음 · 불붙는 소리

**내레이션(VO)** — 사용자가 직접 생성한다
- **MiniMax Audio · Cheerful Cool Junior · MiniMax에서 1.2배속으로 생성** (후처리 배속 없음)
- 대본 전체를 **나누지 않고 한 번에** 생성한다
- 1화 실측 속도 **6.63자/초** (한글 음절 기준) → 분량 추정에 쓴다

## 10. 억제어 — 딱 두 개, 네거티브 절 없음

- 프롬프트에 **네거티브 프롬프트 절을 두지 않는다**
- 억제는 두 줄뿐이다 — ① `no music and no voice`(AUDIO 줄) ② `Any lettering that appears in frame is Latin characters, numerals or unit symbols.`
  (②는 2026-09-30 개정판이다. 1화는 `… Latin characters or numerals.`로 생성했다 — 새 문장은 2화 첫 테스트 씬에서 확인한다)
- 이 이상 억제어를 쌓지 않는다 (§4-3의 이유)

## 11. 모델이 잘못 푸는 지시 — 1화에서 배운 것

- **변형(morph · dissolve · transform into)을 지시하지 않는다** — 「A가 B로 변한다」고 쓰면 엉뚱한 곳에 엉뚱한 색으로 나온다.
  처음부터 **B 상태를 찍는다**
- **「줄어든다 · 닳는다」를 지시하지 않는다** — 모델이 수행하지 못한다. BEAT 1 = 가득 / BEAT 2 = 1/3만 남음처럼 **«두 상태»를 박는다**
- **방향이 있는 현상은 방향을 문장에 박는다** — 1화 S04는 「세로로 쌓인 필터 · 위에서 아래로」라는 말 때문에 정수기가 브리타처럼 나와 반려됐다
- 모델이 영양제·다른 물건으로 오해할 단어를 피한다 — 1화에서 `capsule`이 오메가3 캡슐로 나왔다

## 12. 프롬프트 형식

제미나이 쪽 5요소 구조(`[Subject & Material] + [Action & Physical Interaction] + [Camera Movement & Lens] + [Lighting & Environment] + [Render Style & Quality]`)는
**그대로 쓴다.** 다만 아래 줄 순서로 쓴다.

```
<Subject & Material — 무엇이 어디에 어떤 상태로 있는가>
BEAT 1: <처음 3초에 화면 안에서 벌어지는 일>
BEAT 2: <다음 3초에 화면 안에서 벌어지는 일>
CAMERA: <무브 하나 · 양과 시간을 숫자로>
LOOK: <§5 두 벌 중 하나를 글자 그대로>
<§7 사람 줄> Any lettering that appears in frame is Latin characters, numerals or unit symbols.
AUDIO: <소리> only, no music and no voice.
```

**1화 실제 예 (S04)** — 글자 줄은 개정 전 문장이다 (위 템플릿의 새 문장으로 바꿔 쓴다)
```
A countertop water purifier whose housing turns transparent, revealing four cylindrical filter cartridges standing side by side in one horizontal row, linked by short clear tubes. A pressurised tap-water supply hose enters the first cartridge from the left, fitted with a small thin amber pressure gauge.
BEAT 1: the housing becomes glass-clear; the gauge needle stands high and the supply hose is taut.
BEAT 2: mains pressure forces water sideways through the row, left to right, surging up from the bottom of each cartridge and pushing on into the next.
CAMERA: fast lateral truck left to right following the water front from the supply hose to the last cartridge in 4 seconds.
LOOK: tabletop documentary photography, 16:9, 30fps, physically based lighting, warm pale paper-grey backdrop and tabletop, strong directional key from upper left casting crisp shadows with a subtle cool fill, matte non-reflective surfaces, shallow depth of field, clean digital capture. Any measurement lines, gauges and figures are thin amber. GRADE: bright neutral white, clean, high contrast on the subject.
Every frame shows objects only. Any lettering that appears in frame is Latin characters or numerals.
AUDIO: pressurised water rushing through tubing only, no music and no voice.
```

## 13. 분량 · 포맷

- 길이는 **이야기가 정한다.** 길이를 맞추려고 대본을 늘리지 않는다
- **3분 분기** — VO가 3분을 넘으면 롱폼 16:9, 3분 이내면 숏폼 9:16. 2분 40초~3분 20초는 롱폼으로 간다
- **확정은 VO 실측으로만.** 추정치(음절 ÷ 6.63)로 러닝타임을 적지 않는다

## 14. 사실 확인 — 이 채널의 절반

1. 대본을 낼 때 **반드시 두 가지를 함께** 낸다
   - **부족한 점 목록** — 약한 훅, 근거가 빈 주장, 늘어지는 막, 선명하지 않은 딜레마
   - **팩트체크 표** — 대본의 모든 연도 · 수치 · 고유명사 · 인과 주장 × 확신도(확실 / 통설 / 미확인) × **출처**
2. **출처 없는 수치를 대본에 넣지 않는다.** 그럴듯한 값을 «채워 넣지» 않는다 — 모르면 「미확인」으로 표시한다
3. **단정형 표현을 피한다** — 「전혀」 · 「완벽히」 · 「100%」 · 「절대」 · 「정확히 같은 원리」.
   근거가 그만큼 강할 때만 쓴다
4. **출처가 1차 자료인지 확인한다.** 판매사 자료 · 블로그 · 동료심사를 거치지 않은 시험은 «그렇다고 한다» 수준으로만 쓴다
5. **광고의 논리를 그대로 옮기지 않는다** — 「석유 비닐은 위험, 모래 실리콘은 안전」 같은 구도는 이 채널이 해부할 대상이다
6. **업로드 설명글에 넣을 출처 목록**(논문 · 공공기관 발표 · 규격)을 대본과 함께 낸다
7. 화면이 전부 생성물이라 매 편 **합성 콘텐츠 고지**를 한다

## 15. 이번 2화 「종이호일」 초안에서 위 규칙과 어긋난 곳

전체에 걸린 것:

| 원안 | 규칙 |
|---|---|
| 「하이엔드 테크·사물 해부 다큐」 | §1 — 분해 채널이 아니다 |
| Higgsfield I2V · 키프레임 앵커링 · 무빙 강도 3~5 · 네거티브 프롬프트 | §2 · §4 · §10 |
| 컷 12개 × 15~30초 · VO 녹음 전 타임코드 | §3 — 6초 씬 · 타임코드는 VO 실측 뒤 |
| 라이트 오크 데스크 · 소프트 데이라이트 | §5 — 종이색 · 강한 방향광 |
| Technical Graphic Overlay 칸 · 인포그래픽 · 수칙 카드 | §8 — 후반 작업 없음 |
| 서브 베이스 · 서브 펄스 | §9 — 음악으로 본다 |
| 러닝타임 4:30 / 4:35 / 4:45 세 가지 | §13 — 내레이션 1,354음절 ÷ 6.63 = 약 3분 24초 (추정 · 실측으로 확정) |
| #01 훅이 「자연 상태의 종이는 친수성…」 정의로 시작 | §1 — 문제로 연다 |

컷별 카메라:

| 컷 | 원안 | 어긋난 곳 |
|---|---|---|
| #01 | Slow Dolly-in (강도 3) | slow · 강도 제한 · 15초 |
| #02 | Macro Split-screen · 120fps | 무브 없음 · 분할 화면은 편집 효과 |
| #03 | Smooth Pan Left | smooth · 각도 없음 |
| #04 | 3D Cross-section Scan | 수치 없음 · 30초 |
| #05 | 3D Slow Orbit (완만하게) | slow · 완만 |
| #06 | Rack Focus | 완료 시각 없음 |
| #07 | Static Macro Shot | 정지 컷 |
| #08 | Extreme Close-up Push | 배율·시각 없음 · 25초 |
| #09 | Tilt-up with Smoke Track | 비트 3개(200·220·250) · 25초 |
| #10 | High-speed Macro Action · 120fps | 무브 없음 · 비트 4개(와류·들림·접촉·발화) |
| #11 | Side Tracking (덤덤하게 패닝) | 느림 · 수치 없음 · 장소 2곳(비커 → 쓰레기통) = 씬 2개 |
| #12 | Slow Crane Up & Out · 천천히 암전 | slow · 천천히 · 수치 없음 · 암전은 편집 효과 (동작 자체는 1화 마지막 씬과 같아서 OK) |

화면 글자 · 색:

| 컷 | 원안 | 규칙 |
|---|---|---|
| #03 | `Alternative vs Reality` 타이포 | §8 오버레이 |
| #06 | 한글 뉴스 헤드라인 | §6 한글 금지 |
| #07 | `PFAS Free` / `BPA Free` 인증 픽토그램 | §6 — 인증 씰처럼 보이는 배지는 금지. 비교가 필요하면 라틴 라벨(`PFAS` / `SILICONE`)로 |
| #08 | 「내열온도 220℃」 | §6 — `220℃`는 허용. 한글 「내열온도」만 뺀다 |
| #09 | 게이지 Blue / Red | §5 앰버만 |

> ⚠️ 이 문서는 «제작 방식»만 다룬다. 사실관계 검토(오류 · 출처 없는 수치)는 범위 밖이다.
