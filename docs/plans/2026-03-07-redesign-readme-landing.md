# README + Landing Page Redesign — "Ruff Style" Benchmark-Driven

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** README와 랜딩페이지를 벤치마크 주도("증거 먼저") 구조로 완전 리디자인하여, 개발자가 3초 만에 가치를 파악하고 30초 만에 설치할 수 있게 한다.

**Architecture:** long-lived branch `redesign/v2`에서 작업. 두 개의 Agent Team이 worktree로 분리 병행 — Team A(README + 에셋)와 Team B(Landing Page). Lead(cc)는 main에서 의사결정, 머지, 품질 게이트를 담당.

**Tech Stack:** Astro 5 + Tailwind 3 (www/), Markdown (README), WebP/PNG (showcase assets)

---

## Branch Strategy

```
main (protected)
  └── redesign/v2 (long-lived integration branch)
        ├── redesign/v2-readme    ← Team A worktree
        └── redesign/v2-landing   ← Team B worktree
```

### Rules
- `main`: Lead(cc)만 머지. CI green 필수.
- `redesign/v2`: 통합 브랜치. Team A/B 결과물을 여기로 머지.
- `redesign/v2-readme`: Team A 전용. README.md, README.ko.md, docs/assets/
- `redesign/v2-landing`: Team B 전용. www/ 전체

### Merge Flow
```
Team A (worktree) → PR → redesign/v2
Team B (worktree) → PR → redesign/v2
redesign/v2 → PR → main (Lead 리뷰 + CI green)
```

---

## Agent Team Design

### Lead: cc (Opus, main branch)
- 의사결정, 디자인 방향 설정
- Team A/B 결과물 리뷰 + 머지
- Quality Gate 실행 (lint, build, link check)
- CHANGELOG, CLAUDE.md 업데이트

### Team A: README + Assets (2명)
**Branch:** `redesign/v2-readme` (worktree: `/tmp/parapilot-readme`)

| Role | Model | 담당 |
|------|-------|------|
| **writer** | opus | README.md/README.ko.md 작성, 카피라이팅 |
| **asset-creator** | opus | 터미널 데모 GIF 생성, 벤치마크 차트 SVG, 쇼케이스 큐레이션 |

**File Ownership:**
- `README.md`, `README.ko.md`
- `docs/assets/demo.gif`, `docs/assets/benchmark.svg`
- `www/public/showcase/` (큐레이션만 — 삭제/이동)

### Team B: Landing Page (2명)
**Branch:** `redesign/v2-landing` (worktree: `/tmp/parapilot-landing`)

| Role | Model | 담당 |
|------|-------|------|
| **designer** | opus | 컴포넌트 설계, Tailwind 스타일, 레이아웃 |
| **developer** | opus | Astro 컴포넌트 구현, 빌드 검증, 반응형 |

**File Ownership:**
- `www/src/components/*.astro` (전체)
- `www/src/pages/index.astro`
- `www/src/styles/global.css`
- `www/tailwind.config.mjs`

---

## Design Spec: README.md (Team A)

### Target: ~120줄 (현재 223줄 → 절반)

### Structure (순서 중요)

```markdown
# parapilot

> Headless CAE/CFD post-processing for AI terminals. No ParaView. No GUI.

[배지: CI | Coverage | PyPI | Python | License] (5개만, 현재 9개→5개)

[터미널 데모 GIF — MCP tool call → PNG 결과물, 5초 루프]

## Quick Start

[3가지 설치 방법: Claude plugin / pip / Docker]

## What You Get

[핵심 feature 3개: Headless Rendering / 18 MCP Tools / 50+ Formats]
[각각 1줄 설명 + 아이콘 없이 텍스트만]

## See It In Action

[큐레이션된 6장: 2×3 그리드]
[Full gallery → 랜딩페이지 링크]

## vs Alternatives

[비교표: parapilot / ParaView(pvpython) / PyVista / VTK-direct]
[사실 기반, 존중적 톤, 점수 산식 없음]

## Contributing

[3줄: clone → install → test]

## License

MIT
```

### 핵심 카피

**Tagline (h1 아래):**
> Headless CAE/CFD post-processing for AI terminals. No ParaView. No GUI.

**비교표 포지셔닝:**
> "18 MCP tools that turn natural language into publication-ready renders."

**설치 우선순위:**
1. `claude install kimimgo/parapilot` (Claude Code 사용자)
2. `pip install mcp-server-parapilot` (범용)
3. `docker compose up` (격리 환경)

---

## Design Spec: Landing Page (Team B)

### Target: 5개 섹션 (현재 8개 → 5개)

### Section Flow

```
1. Hero          — 터미널 데모 + tagline + CTA
2. Proof         — 벤치마크 차트 + 핵심 수치 4개
3. Showcase      — 큐레이션 6장 (현재 80장 → 6장)
4. QuickStart    — 3-step 설치
5. Footer        — GitHub / PyPI / Docs / Discord
```

### Section 1: Hero (redesign)

**현재 문제:** 배지 줄, 긴 설명, 터미널 애니메이션 4.5초 딜레이

**새 설계:**
```
┌─────────────────────────────────────────┐
│  [왼쪽 50%]                [오른쪽 50%]  │
│                                         │
│  parapilot                 ┌──────────┐ │
│                            │ Terminal  │ │
│  Post-process              │ Demo GIF │ │
│  simulations from          │ (5s loop)│ │
│  your terminal.            │          │ │
│                            └──────────┘ │
│  No ParaView. No GUI.                   │
│                                         │
│  [pip install ...] [GitHub →]           │
│                                         │
│  Claude Code · Cursor · Gemini CLI      │
└─────────────────────────────────────────┘
```

**변경점:**
- 2-column hero (text left, demo right)
- 배지 제거 (Hero에서), 하단 Stats로 이동
- CTA 2개: install command + GitHub 링크
- 지원 클라이언트는 작은 텍스트로

### Section 2: Proof (신규)

**현재:** Stats + Comparison 분리 → **통합**

```
┌─────────────────────────────────────────┐
│  18 Tools  │  1134 Tests  │  50+ Formats │  99% Coverage │
│            │              │              │               │
│  ─────────────────────────────────────── │
│                                          │
│  [비교표: parapilot vs ParaView vs PyVista] │
│  사실 기반 feature matrix (checkmarks)     │
└──────────────────────────────────────────┘
```

### Section 3: Showcase (축소)

**현재 80장 → 6장 큐레이션**

선정 기준: 도메인 다양성 + 시각적 임팩트
1. DrivAerML 자동차 CFD (외부 공기역학)
2. CT Skull contour (의료)
3. Carotid streamlines (혈류)
4. Office HVAC flow (건축 환기)
5. Structural FEA stress (구조)
6. Stanford Dragon (일반 3D)

```
┌─────────────────────────────────────────┐
│  [img1] [img2] [img3]                   │
│  [img4] [img5] [img6]                   │
│                                         │
│  "All renders from single MCP calls"    │
│  [Full Gallery →] (랜딩페이지 별도 페이지) │
└─────────────────────────────────────────┘
```

### Section 4: QuickStart (간소화)

현재와 동일하지만:
- Step 1: `pip install` (1줄)
- Step 2: `.mcp.json` config (JSON 3줄)
- Step 3: natural language prompt 예시

### Section 5: Footer (확장)

현재 4링크 → 6링크:
- GitHub | PyPI | Docs | Issues | License | Discord(placeholder)

### 삭제 대상
- **Architecture** 섹션 → Docs 사이트로 이동
- **PluginShowcase** (4개 클라이언트 동일 JSON) → QuickStart에 통합
- **Features** 6카드 → Proof 섹션으로 압축

---

## Asset Creation Spec

### 1. Terminal Demo GIF

**내용:**
```
$ # Claude Code에서 MCP tool call
$ > "Render pressure field from cavity.foam with jet colormap"

⠋ Rendering cavity.foam...
✓ Rendered in 0.8s → cavity_pressure.png

[실제 렌더링 결과 PNG 표시]
```

**스펙:**
- 800×500px, 10fps, <3MB
- 5초 루프 (3초 타이핑 + 2초 결과 표시)
- WebP + GIF 동시 제공
- 도구: asciinema + agg 또는 vhs (charmbracelet/vhs)

### 2. Benchmark Comparison (SVG 또는 이미지)

**내용:** 지금은 실제 벤치마크 데이터 없음 → feature matrix로 대체
- 향후 `benchmarks/bench_render.py` 결과로 실제 차트 교체 가능

### 3. Showcase 큐레이션

**기존 88개 → 6개 WebP만 유지 (README용)**
- 나머지는 www/public/showcase/에 그대로 유지 (full gallery 페이지용)

---

## Implementation Tasks

### Phase 0: Branch Setup (Lead)

#### Task 0.1: Create branch structure
```bash
git checkout main
git checkout -b redesign/v2
git push origin redesign/v2

# Team A worktree
git worktree add /tmp/parapilot-readme redesign/v2
cd /tmp/parapilot-readme
git checkout -b redesign/v2-readme
git push origin redesign/v2-readme

# Team B worktree
git worktree add /tmp/parapilot-landing redesign/v2
cd /tmp/parapilot-landing
git checkout -b redesign/v2-landing
git push origin redesign/v2-landing
```

#### Task 0.2: Create team config
```
TeamCreate: Team A (readme-team)
  - writer (opus): README.md, README.ko.md 작성
  - asset-creator (opus): 데모 GIF, 쇼케이스 큐레이션

TeamCreate: Team B (landing-team)
  - designer (opus): 컴포넌트 설계, 스타일
  - developer (opus): Astro 구현, 빌드 검증
```

---

### Phase 1: Team A — README (병렬)

#### Task 1.1: Write new README.md
**Files:** `README.md`
- 위 Design Spec 기반 120줄 README 작성
- 배지 5개만 (CI, Coverage, PyPI, Python, License)
- 터미널 데모 GIF placeholder (`docs/assets/demo.gif`)
- 큐레이션 6장 쇼케이스
- 새 비교표 (사실 기반)
- Commit: `docs: redesign README — benchmark-driven, 120 lines`

#### Task 1.2: Write new README.ko.md
**Files:** `README.ko.md`
- README.md 한국어 번역
- 동일 구조, 동일 이미지
- Commit: `docs: redesign Korean README to match new structure`

#### Task 1.3: Create terminal demo asset
**Files:** `docs/assets/demo.gif`, `docs/assets/demo.webp`
- asciinema/vhs로 터미널 데모 녹화 (또는 수동 제작)
- 대안: 정적 스크린샷 + 코드블록 (GIF 제작이 CI에서 어려우면)
- Commit: `docs: add terminal demo GIF for README hero`

#### Task 1.4: Curate showcase images
**Files:** README에서 참조하는 6장만 확인
- WebP 파일 존재 확인
- alt text 개선 (기술적 설명 추가)
- Commit: `docs: curate 6 showcase images for README`

---

### Phase 2: Team B — Landing Page (병렬)

#### Task 2.1: Redesign Hero component
**Files:** `www/src/components/Hero.astro`
- 2-column layout (text left, demo right)
- 배지 제거
- CTA 2개 (install + GitHub)
- 지원 클라이언트 텍스트 축소
- 터미널 데모: 정적 이미지 또는 GIF
- Commit: `www: redesign Hero — 2-column, demo-right, clean CTA`

#### Task 2.2: Create Proof section (Stats + Comparison 통합)
**Files:**
- Create: `www/src/components/Proof.astro`
- Delete: `www/src/components/Stats.astro`, `www/src/components/Comparison.astro`
- 4개 수치 카드 + feature matrix 테이블
- 바 차트 제거 (불투명한 점수 → 명확한 checkmark)
- Commit: `www: create Proof section — unified stats + comparison`

#### Task 2.3: Slim down Showcase
**Files:** `www/src/components/Showcase.astro`
- 80장 → 6장 큐레이션
- 서브섹션 7개 → 1개 그리드
- "Full Gallery →" 링크 (향후 별도 페이지)
- Commit: `www: slim Showcase to 6 curated renders`

#### Task 2.4: Simplify QuickStart + remove PluginShowcase
**Files:**
- Modify: `www/src/components/QuickStart.astro`
- Delete: `www/src/components/PluginShowcase.astro`
- 3-step만 유지, 클라이언트별 JSON은 QuickStart에 탭으로 통합
- Commit: `www: merge PluginShowcase into QuickStart, 3-step focus`

#### Task 2.5: Update Footer
**Files:** `www/src/components/Footer.astro`
- 4링크 → 6링크 (Docs, Discord placeholder 추가)
- 저작권 연도 추가
- Commit: `www: expand Footer with Docs and Discord links`

#### Task 2.6: Remove Architecture + Features, update page
**Files:**
- Delete: `www/src/components/Architecture.astro`, `www/src/components/Features.astro`
- Modify: `www/src/pages/index.astro`
- 새 섹션 순서: Hero → Proof → Showcase → QuickStart → Footer
- Commit: `www: remove Architecture/Features, 5-section layout`

#### Task 2.7: Build verification
```bash
cd www && npm run build
```
- 빌드 성공 확인
- 깨진 이미지/링크 확인
- Commit: `www: fix build issues from redesign`

---

### Phase 3: Integration (Lead)

#### Task 3.1: Merge Team A → redesign/v2
```bash
git checkout redesign/v2
git merge redesign/v2-readme --no-ff
```

#### Task 3.2: Merge Team B → redesign/v2
```bash
git merge redesign/v2-landing --no-ff
```

#### Task 3.3: Cross-check consistency
- README의 이미지 경로가 www/public/showcase/와 일치하는지
- README의 수치 (tools, tests, coverage)가 랜딩페이지와 일치하는지
- 비교표 내용이 양쪽 동일한지

#### Task 3.4: Quality Gate
```bash
# Lint
ruff check src/ tests/
mypy src/parapilot/ --ignore-missing-imports

# Tests
pytest -q

# www build
cd www && npm run build

# Link check (README)
# markdown-link-check README.md (optional)
```

#### Task 3.5: PR → main
```bash
git checkout main
git merge redesign/v2 --no-ff
git push origin main
```
- CHANGELOG 업데이트
- Commit: `feat: v2 redesign — README + Landing Page (benchmark-driven)`

---

### Phase 4: Cleanup (Lead)

#### Task 4.1: Remove worktrees and branches
```bash
git worktree remove /tmp/parapilot-readme
git worktree remove /tmp/parapilot-landing
git branch -d redesign/v2-readme redesign/v2-landing redesign/v2
git push origin --delete redesign/v2-readme redesign/v2-landing redesign/v2
```

#### Task 4.2: Update CLAUDE.md metrics
- README 줄수, 랜딩페이지 섹션 수 업데이트
- memory/MEMORY.md 업데이트

---

## Quality Checklist

### README
- [ ] 120줄 이하
- [ ] 배지 5개
- [ ] 터미널 데모 (GIF 또는 스크린샷)
- [ ] 쇼케이스 6장
- [ ] 비교표 사실 기반
- [ ] 설치 3가지 방법
- [ ] Contributing 3줄

### Landing Page
- [ ] 5개 섹션 (Hero, Proof, Showcase, QuickStart, Footer)
- [ ] `npm run build` 성공
- [ ] 모바일 반응형 확인
- [ ] 깨진 이미지 0개
- [ ] Lighthouse Performance > 90

### Consistency
- [ ] 수치 일치 (tools, tests, coverage, formats)
- [ ] 이미지 경로 일치
- [ ] 비교표 내용 일치
