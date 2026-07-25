# K-Reality Check #1 — 조립 인수인계 (새 세션용)

> ⚠️ **이 문서는 대체됨 (superseded).**
> - 채널명이 **KOREASIDER**(`@koreasider`)로 변경됨. 아래의 "K-Reality Check"는 구 명칭.
> - EP1 조립은 **완료됨** (최종 2:55.8 / 1080p24). 아래 "목적/실행" 절은 이미 끝난 작업이다.
> - 현행 정본은 저장소 루트 **`KOREASIDER.md`**. 내용이 어긋나면 그쪽이 우선한다.
> - 이 파일은 조립 설계·에셋 job ID 이력 보존용으로만 남긴다.

## 목적
모든 생성 에셋(클립 8 + VO 8 + 카드 13)은 힉스필드에서 완성됨.
이 세션에서 남은 작업은 **`assemble.py` 실행 → 최종 MP4 + SRT를 사용자에게 전달**뿐이다.

## 전제 조건
- 환경 네트워크 정책이 `d8j0ntlcm91z4.cloudfront.net` 접속을 허용해야 함
  (이전 세션은 "신뢰됨(Trusted)" 정책이라 403으로 차단됐음 — 사용자가 정책 변경 후 새 세션을 시작한 상황)
- ffmpeg: `pip install imageio-ffmpeg` 후
  `/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2`
  (경로가 다르면 `python3 -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"` 로 확인 후 assemble.py 상단 FF 변수 수정)

## 실행
```bash
pip install imageio-ffmpeg
cd k-reality-check && python3 assemble.py
```
- 출력: `out/K-Reality-Check-EP1.mp4` (1080p60, ~2분56초) + `out/K-Reality-Check-EP1.en.srt`
- 완료 후 두 파일을 SendUserFile로 사용자에게 전달할 것 (mp4는 attach, srt도 attach)
- 스크립트가 다운로드(34개 파일) → 세그먼트 인코딩 → 오디오 믹스(VO 1.1배속 + 클립 환경음 22%) → 자막 리본 번인 → SRT 생성까지 전부 수행함

## 조립 설계 요약
- Act 1: 클립 4초 → 데이터카드 (VO 0:00 시작, 23.5초)
- Act 2~7: 제품카드 1초 → 클립 4초 → 데이터카드 (VO는 액트 시작+1초)
- Act 8: 클립 루프 (26.2초)
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

전체 다운로드 URL은 assemble.py 안에 하드코딩되어 있음 (CloudFront).

## 남은 패키징 (조립 후 사용자에게 같이 전달)
- 제목 후보 3종·SEO 설명·챕터 타임스탬프는 조립 완료 후 실제 타임코드 기준으로 갱신해 제공할 것
