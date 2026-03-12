# viznoir

[English](README.md) | **한국어**

> VTK is all you need. AI 에이전트를 위한 시네마급 과학 시각화.

[![CI](https://github.com/kimimgo/viznoir/actions/workflows/ci.yml/badge.svg)](https://github.com/kimimgo/viznoir/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/mcp-server-viznoir)](https://pypi.org/project/mcp-server-viznoir/)
[![Python](https://img.shields.io/pypi/pyversions/mcp-server-viznoir)](https://pypi.org/project/mcp-server-viznoir/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/kimimgo/viznoir/blob/main/LICENSE)

## 10개 도메인, 하나의 파이프라인

모든 렌더링은 MCP 도구 한 번 호출로 생성 — GUI 없음, 후처리 없음, ParaView 불필요.

| | | |
|:---:|:---:|:---:|
| ![의료](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/01_skull_annotated.webp) | ![연소 CFD](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/02_combustion_annotated.webp) | ![열전달](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/03_heatsink_annotated.webp) |
| **의료** — CT 두개골 볼륨 | **CFD** — 연소 유선 | **열전달** — 방열판 구배 |
| ![지구과학](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/04_seismic_annotated.webp) | ![자동차](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/05_drivaerml_annotated.webp) | ![분자](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/06_h2o_annotated.webp) |
| **지구과학** — 지진파 | **자동차** — DrivAerML Cp 880만 셀 | **분자** — H₂O 전자밀도 |
| ![혈관](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/07_aneurism_annotated.webp) | ![행성](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/08_bennu_annotated.webp) | ![구조](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/09_cantilever_annotated.webp) |
| **혈관** — 뇌동맥류 MRA | **행성** — 베누 소행성 19.6만 삼각형 | **구조** — 캔틸레버 FEA 응력 |

## 물리 기반 애니메이션

슬라이드쇼가 아닙니다 — 모든 효과에 물리적 이유가 있는 실시간 VTK 프레임 렌더링.

| 애니메이션 | 물리 | 기법 |
|-----------|------|------|
| 유선 성장 | 노즐에서 라그랑지안 이류 | `streamline_growth` |
| 클립 스윕 | 압력 구배 방향 단면 | `clip_sweep` |
| 레이어 리빌 | CT 밀도 층별 분류 | `layer_reveal` |
| 등치면 스윕 | 전자 궤도 위상 | `iso_sweep` |
| 변형 진동 | 구조 모드 형상 | `warp_oscillation` |
| 조명 궤도 | 지형학 사광 기법 | `light_orbit` |
| 임계값 리빌 | 볼륨 피처 계층 | `threshold_reveal` |

모든 프리셋은 `viznoir.anim.physics`에서 사용 가능.

## 과학 스토리텔링

물리 인사이트를 추출하고 출판 품질의 스토리로 합성합니다.

```
"캐비티 유동 분석해서 뭐가 일어나는지 보여줘"

→ inspect_physics: 정체점 20개, 와도 범위 [-15.2, +19.6]/s
→ cinematic_render × 4: 속도, 압력, 와도, 온도
→ compose_assets: LaTeX 수식 + 인사이트 라벨 + 스토리 레이아웃
```

![과학 스토리텔링](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/cavity_story.webp)

## 빠른 시작

```bash
pip install mcp-server-viznoir
```

**Claude Code:**

```bash
claude install kimimgo/viznoir
```

**MCP 설정 (Cursor / Windsurf / 기타 클라이언트):**

```json
{
  "mcpServers": {
    "viznoir": {
      "command": "mcp-server-viznoir"
    }
  }
}
```

**Docker (GPU 헤드리스):**

```bash
docker compose up -d
```

## 아키텍처

```
  프롬프트                   "cavity.foam에서 압력장 렌더링해줘"
    │
  MCP 서버                  22개 도구 · 12개 리소스 · 4개 프롬프트
    │
  VTK 엔진                  리더 → 필터 → 렌더러 → 카메라
    │                       EGL/OSMesa 헤드리스 · 시네마틱 조명
  물리 레이어                토폴로지 분석 · 컨텍스트 파싱
    │                       와류 탐지 · 정체점 분류
  애니메이션                 7개 물리 프리셋 · 이징 · 타임라인
    │                       전환 효과 · 합성기 · 비디오 내보내기
  출력                      PNG · WebP · MP4 · GLTF · LaTeX
```

## 수치

| | |
|---|---|
| **22** MCP 도구 | **1489+** 테스트 |
| **12** 리소스 | **97%** 커버리지 |
| **10** 도메인 | **50+** 파일 포맷 |
| **7** 애니메이션 프리셋 | **17** 이징 함수 |

## 라이선스

MIT
