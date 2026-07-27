# 유튜브 채널명 결정 — 인수인계

## ✅ 최종 확정: **KOREASIDER** (2026-07-23)

Korea + Insider 합성어. 검증(인사이더의 팩트체크)과 추천(인사이더의 진짜 리스트)을 한 단어에 담고,
"Korea"라 전국 확장성·SEO도 확보. 아래 후보 검토 이력은 기록용으로 보존.

- 핸들 권장: `@koreasider` (유튜브·인스타·틱톡 동일 확보 권장)
- 표기: KOREASIDER (올캡스 워드마크) / Koreasider (본문용)
- 남은 확인: 3사 핸들 실제 공석 여부 직접 접속 확인

## 지금 상황 (확정 전 기록)
유튜브 채널명을 정하는 중. 첫 영상(EP1)은 편의점 꿀조합 검증 콘텐츠로 이미 완성됨.
현재 임시 채널명은 **"K-Reality Check"** (EP1 아웃트로 나레이션·자막·설명란에 이 이름이 박혀 있음 → 채널명 확정되면 교체 필요).

## 채널 정체성 (이름이 담아야 할 것)
- 두 종류 콘텐츠를 **한 우산**에 담아야 함:
  1. **검증** — 바이럴 꿀조합/트렌드가 진짜인지 데이터로 팩트체크 (TRAP vs LOCAL PICK)
  2. **추천/큐레이션** — 한국 꼭 먹어야 할 베스트10, 진짜 현지인이 가는 맛집 소개 등 (전국 단위)
- 공통 컨셉: **"관광객용 말고, 진짜 한국인이 먹고 사는 것 — 로컬 인사이더의 솔직한 시선"**
- 페르소나: "Min" (서울 로컬), 영어 나레이션, 해외 시청자 타깃

## 이름 고를 때 확정된 기준
1. **검증 + 추천 둘 다** 담을 것 (한쪽만 강조하는 "Reality Check"는 검증에 치우쳐서 탈락)
2. **동음이의·흔한표현 충돌 금지** (예: "Korea IRL" → "Korea Girl"과 겹쳐서 탈락)
3. **전국 확장성** — 콘텐츠가 서울 밖 전국으로 나가므로 "Korea"가 "Seoul"보다 유리
4. **선점 안 된 고유한 이름** (흔한 조합은 이미 다 선점됨)
5. 웹 검색은 참고용 — **최종은 youtube.com/@핸들 직접 확인 필수**

## 검토 이력 (중복 방지)
| 후보 | 결과 |
|---|---|
| K-Reality Check | 검증에만 맞음, 추천 콘텐츠와 톤 불일치 → 채널명으론 부적합 (검증 "시리즈명"으로는 재활용 가능) |
| Korea, Actually | ❌ 이미 있는 채널 |
| K-Insider | ❌ 이미 있는 채널 |
| Korea Unfiltered | ❌ 이미 있는 채널 |
| Real Korea | ⚠️ 비어있지만 너무 흔하고 밋밋, 유사채널 많음 |
| Korea IRL | ❌ "Korea Girl"과 검색 충돌 (치명적) |
| Legit Korea | ❌ 이미 있는 채널 (@LegitKorea) |
| Korea Uncut | ⚠️ 동명은 없으나 "Korea Unfiltered"와 혼동 + "uncut" 성인검색 딸림 |
| Korea Off Menu | ⚠️ 유명 푸드 팟캐스트 "Off Menu"와 카테고리 충돌 |
| Straight Up Korea | ✅ 비어있음·충돌없음 (후보) |
| Korea Decoded | ✅ 비어있음 (후보, 해설 뉘앙스) |
| SEOULCANDID | ✅ 비어있음, 좋음. 단 "Seoul"이 지역 한정 뉘앙스 |
| **KOREACANDID** | ✅ **비어있음. 현재 유력 1순위** |

## 후보 검토 결과 (확정 전 유력했던 안)
### KOREACANDID
- "Candid = 솔직한·꾸밈없는·날것" → 검증(솔직한 팩트체크)과 추천(연출없는 진짜 로컬) 둘 다 담음
- "Korea"라서 전국 확장성·SEO 유리 (SEOULCANDID의 지역한정 문제 해결)
- 붙여쓰기 한 단어 = 고유 워드마크, 로고/핸들로 소유 좋음
- 동음이의 함정 없음
- 웹 검색상 동명 채널 없음 (KoreaChan·Korebap 등 유사하나 다름)
- 차선: SEOULCANDID (더 개인적·서울로컬 밀착이나 확장성 약함), Straight Up Korea

## 다음에 할 일 (KOREASIDER 확정 후)
1. `@koreasider` 핸들 3사(유튜브·인스타·틱톡) 공석 확인 후 즉시 선점
2. 서브 태그라인·시리즈명 구성 — 예: 채널 KOREASIDER / 검증 시리즈 "Reality Check" / 추천 시리즈 "Local's Best 10"
3. **EP1 브랜딩 교체 작업** (아래 상세)

## EP1 "K-Reality Check" → "Koreasider" 교체 대상
| 위치 | 내용 | 비용 |
|---|---|---|
| `assemble.py` 110행 (Act 8 VO 문장) | "...next here on K-Reality Check, leave a comment..." → Koreasider | VO 재생성 필요 ~2.3크레딧 (Leo, seed_audio, voice id `73a45c18-0c56-4642-a61e-f6b303f8ded1`) |
| SRT 자막 | VO 재생성 후 재싱크 스크립트 재실행 | 0 |
| 유튜브 설명란·제목 패키징 | 텍스트 교체 | 0 |
| 출력 파일명 `K-Reality-Check-EP1.mp4` | 원하면 `Koreasider-EP1.mp4`로 변경 | 0 |
| 리본 자막 (화면 내) | 채널명 미표기라 **수정 불필요** | - |
| 썸네일 (job 76e318eb) | 채널명 미표기라 **수정 불필요** | - |

## 참고 (영상 제작 관련은 별도 문서)
- 영상 제작 파이프라인·규칙: `k-reality-check/PRODUCTION-PROMPT.md`
- EP1 조립 상태: `k-reality-check/HANDOVER.md`
