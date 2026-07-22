# K-Reality Check #1 — 조립 인수인계

## 상태 (2026-07-22 갱신)
- 조립 완료·전달됨. 에셋: 클립 24(원본 8 + 몽타주용 추가 16) + VO 8 + 카드 13.
- 각 액트 본문은 [기존 클립 → 추가 클립 B → C] 4초 청크 순환 몽타주, 데이터카드는 액트 끝 5초만(켄 번즈 줌인).
- 추가 클립 매니페스트는 assemble.py의 EXTRAS에 하드코딩됨(.png/.jpg를 넣으면 켄 번즈 스틸로 삽입 가능 — 사용자가 실제 편의점 사진을 주면 여기 추가).

## 전제 조건
- 환경 네트워크 정책이 `d8j0ntlcm91z4.cloudfront.net` 접속을 허용해야 함
- ffmpeg: **apt의 시스템 ffmpeg 사용** (`apt-get update && apt-get install -y ffmpeg`) —
  imageio-ffmpeg 번들 바이너리는 drawtext 필터가 없어 자막 리본 번인이 실패함

## 실행
```bash
cd k-reality-check && python3 assemble.py
```
- 출력: `out/K-Reality-Check-EP1.mp4` (1080p60, ~2분56초) + `out/K-Reality-Check-EP1.en.srt`
- 스크립트가 다운로드(50개 파일) → 세그먼트 인코딩 → 오디오 믹스(VO 1.1배속 + 클립 환경음 22%) → 자막 리본 번인 → SRT 생성까지 전부 수행함
- 전달 제약: 채팅 첨부 한도 30MiB(→ 720p 프리뷰로 전달), GitHub 파일 한도 100MB
  (→ 마스터는 2-pass 4Mbps 재인코딩본을 out/에 커밋; crf18 원본은 세션 로컬에만 존재)

## 조립 설계 요약
- Act 1: 클립 몽타주 (VO 0:00 시작, 23.5초) → 데이터카드 5초
- Act 2~7: 제품카드 1초 → 클립 몽타주 → 데이터카드 5초 (VO는 액트 시작+1초)
- Act 8: 클립 몽타주 (26.2초)
- 상단 리본 자막: TRAP=빨강, LOCAL PICK=초록, Act1=시안, Act8=검정
- BGM 없음 — 사용자가 유튜브 오디오 라이브러리에서 직접 추가 예정
  (추천 검색어: "upbeat lo-fi hip hop", "hyperpop energetic" / 밝음·활기참 필터)

## 프로젝트 컨텍스트 (요약)
- 유튜브 채널 "K-Reality Check" 1화. 콘셉트: 바이럴 편의점 꿀조합 3개(TRAP) vs 현지인 검증 3개(LOCAL PICK)
- 페르소나 "Min" — VO는 힉스필드 seed_audio, 프리셋 보이스 **Leo**(남성, id 73a45c18-0c56-4642-a61e-f6b303f8ded1)
- 비주얼: "Vivid Pop" (네온 옐로/크림슨/네온 그린/시안), 밝은 하이키 — 다크 톤 금지
- 썸네일 확정: 힉스필드 job `76e318eb-2478-4eaf-9f32-2668d7f2ec1b` (노맛/극혐/DAEBAK/존맛 4스티커 VS 구도)
- 힉스필드 워크스페이스: ff57adad-ada3-4e61-8da6-c62b9f4a4f09 (Plus)

## 에셋 매니페스트 (힉스필드 job ID)
| Act | 클립(Seedance 4s) | VO(Leo, wav) | 제품카드 | 데이터카드 |
|---|---|---|---|---|
| 1 | d7075287 | c62f7814 | — | c2f4b3f3 |
| 2 | df3cc451 | be0586c9 | a88dac34 | 942baba7 |
| 3 | bae8b71b | 96fbaf98 | aec56f28 | 80aaba50 |
| 4 | 4f34c10f | 79cce68d | 39e04824 | 4c7d3900 |
| 5 | f682af00 | f5365edf | be1f6403 | d9ca3a60 |
| 6 | c077aa11 | 5e423380 | 78e5f69f | 69a37068 |
| 7 | 0fa50ae9 | cb0e2a12 | 04b1b046 | 998ec873 |
| 8 | b609f420 | 8a511745 | — | — |

추가 몽타주 클립 16개(액트당 2개, Seedance 720p): assemble.py의 EXTRAS 참조.
(7B 치즈 풀링은 콘텐츠 필터 오탐으로 1회 재생성 — 3cd4f796)
전체 다운로드 URL은 assemble.py 안에 하드코딩되어 있음 (CloudFront).

## 남은 패키징 (조립 후 사용자에게 같이 전달)
- 제목 후보 3종·SEO 설명·챕터 타임스탬프는 조립 완료 후 실제 타임코드 기준으로 갱신해 제공할 것
