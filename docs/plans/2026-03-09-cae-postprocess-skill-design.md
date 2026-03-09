# CAE Postprocess Skill Design

> 도메인 전문가의 개떡 같은 말 → viznoir 도구의 찰떡 같은 호출

## Problem

viznoir는 21개 MCP 도구를 제공하지만, LLM 에이전트가 **"CFD 결과 보여줘"** 같은 전문가 요청을 받았을 때 어떤 도구를 어떤 파라미터로 불러야 하는지 모른다. 도구는 있는데 **통역사**가 없다.

타겟 사용자: **과학 지식이 깊은 전문가** — 워크플로우를 가르칠 필요 없음. 뭉뚱그린 말을 정확한 도구 호출로 번역하고, 데이터에서 시각화 아이디어를 제안하고, 아름다운 asset을 만들어주면 됨.

## Design Decision

**하나의 스킬** `cae-postprocess`가 3가지를 제공:
1. 도메인 용어 → viznoir 도구 매핑 사전
2. inspect_data 결과 기반 시각화 아이디어 생성 룰
3. 미학 가이드 (cinematic 우선, 컬러맵 관례, 카메라)

**안 하는 것**: 고정된 Step 1→2→3→4 워크플로우, 물리 해석 (그건 LLM의 일).

## File Structure

```
.claude-plugin/
├── plugin.json          (기존)
└── skills/
    └── cae-postprocess/
        └── SKILL.md     ← NEW (~300줄)
```

## SKILL.md 구조

### Frontmatter

```yaml
name: cae-postprocess
description: >-
  CAE 시뮬레이션 후처리 통역 스킬. CFD/FEA/SPH 도메인 전문가의
  자연어 요청을 viznoir MCP 도구 호출로 번역한다.
  도메인 용어 사전, 데이터 기반 시각화 아이디어 생성,
  cinematic 우선 미학 가이드를 제공.
  트리거: 시뮬레이션 후처리, CFD, FEA, SPH, 유동, 응력, 입자,
  .foam, .vtu, .vtk, .pvd, render, slice, animate,
  후처리 결과, 시각화, visualization, postprocess,
  streamlines, contour, deformation, pressure drop
```

### Section 1: 도메인 용어 → 도구 매핑 사전

| 전문가가 말하는 것 | viznoir 도구 | 핵심 파라미터 |
|-------------------|-------------|--------------|
| wake, 후류 | `streamlines` | seed: 물체 뒤, field: U |
| 재순환, recirculation | `streamlines` + `clip` | low velocity region |
| 압력강하, pressure drop | `plot_over_line` | inlet→outlet 방향 |
| 자유수면, free surface | `contour` | field: alpha, iso: 0.5 |
| vortex, 와류 | `streamlines` or `contour`(Q-criterion) | field: U or Q |
| 경계층, boundary layer | `slice` + `plot_over_line` | wall-normal 방향 |
| 열전달, heat transfer | `slice` | field: T, colormap: Inferno |
| 응력 집중, stress concentration | `cinematic_render` | field: von_mises |
| 변형, deformation | `execute_pipeline` | WarpByVector + render |
| 항복 초과, yield exceedance | `execute_pipeline` | Threshold(von_mises > σ_y) |
| 입자 분포, particle | `render` | representation: Point Gaussian |
| 시간 변화, transient | `animate` or `split_animate` | timesteps 기반 |
| 비교, compare | `compare` | side-by-side or diff |
| 전체 요약, overview | `batch_render` | 주요 필드 전부 |
| 고품질, 논문용, publication | `cinematic_render` | preset: publication |
| 단면, cross-section | `slice` | bbox 중심 기반 |
| 유선, 유동 패턴 | `streamlines` | auto seed |
| 등치면, isosurface | `pv_isosurface` | field + isovalue |
| 볼륨 렌더링 | `volume_render` | transfer function |
| 3D 미리보기, interactive | `preview_3d` | glTF export |
| 프로브, 모니터링 | `probe_timeseries` | point + field |
| 벽면 힘, wall force | `integrate_surface` | pressure * normals |

### Section 2: inspect_data 기반 시각화 아이디어 생성

```
항상 inspect_data(file_path) 먼저 실행.
결과의 fields, timesteps, bounds를 보고 아이디어를 제안.
```

#### 필드 기반

- velocity(U/Velocity) → streamlines, slice(velocity) 제안
- pressure(p/p_rgh/Pressure) → contour(pressure), plot_over_line 제안
- alpha 필드 → free surface contour (iso=0.5), animate
- temperature(T) → slice(T, colormap=Inferno)
- von_mises/stress → cinematic_render + WarpByVector
- Type 필드 (SPH) → threshold로 fluid/boundary 분리
- vector 필드 2개 이상 → compare로 나란히 비교 제안

#### 시간 기반

- timesteps > 1 → animate 가능 알림, split_animate(render+graph) 추천
- timesteps == 1 → 정적 cinematic_render 추천
- timesteps > 50 → speed_factor 조절 권장

#### 지오메트리 기반

- bounds 비대칭 → 장축 방향으로 slice 제안
- 2D (한 축 thickness ≪ 나머지) → 해당 축 방향 뷰 + empty 축 무시
- cell_count > 1M → "대규모 데이터, slice/clip으로 줄여서 보세요"
- 작은 바운딩박스 → cinematic_render auto-framing이 적합

### Section 3: 미학 가이드

#### 기본 원칙

- `cinematic_render`를 `render`보다 항상 우선 (같은 파라미터에 조명/SSAO/FXAA 추가)
- `viznoir://case-presets` 리소스에서 도메인별 필드/컬러맵/카메라 반드시 참조
- 사용자가 "빨리"/"간단히" 요청 시에만 render 사용

#### 컬러맵 관례

| 물리량 | 컬러맵 | 이유 |
|--------|--------|------|
| 온도 (T) | Inferno / Black-Body Radiation | 열 직관 |
| 압력 (p) | Cool to Warm | diverging, 양/음 구분 |
| 속도 (U) | Viridis | sequential, 지각 균일 |
| 응력 (σ) | Cool to Warm | diverging |
| volume fraction (α) | Blue to Red Rainbow | 상 구분 |
| wall shear | Plasma | high contrast |
| vorticity/Q | Turbo | 구조 강조 |

#### 카메라

- 3D 전체뷰 → isometric
- 유동 방향 분석 → front 또는 top
- wake 분석 → downstream 뷰 (물체 뒤쪽)
- 구조 해석 → isometric (변형 보기 좋음)

#### 배경

- 과학 시각화 기본 → 어두운 배경 `[0.15, 0.15, 0.15]`
- 논문/발표용 → 흰 배경 `[1.0, 1.0, 1.0]`

### Section 4: 실행 패턴

```
1. inspect_data(file_path) → 데이터 파악
2. 사용자 요청 + 필드 정보 → 위 사전에서 적절한 도구 선택
3. viznoir://case-presets에서 해당 도메인 프리셋 참조
4. 도구 실행 (cinematic_render 우선)
5. 결과와 함께 추가 시각화 아이디어 제안
```

### 스킬이 안 하는 것

- 고정 워크플로우 강제 (전문가가 판단)
- 물리 해석 (LLM이 할 일)
- 파일 포맷 제한 (viznoir이 지원하면 다 됨)

## Alternatives Considered

1. **도메인별 3개 스킬** (cfd/fea/sph) — 거부: 전문가는 도메인을 넘나들고, 용어 사전이 중복됨
2. **고정 Phase 1→2→3→4 워크플로우** — 거부: 전문가에게 불필요한 제약
3. **MCP prompt만 사용** — 거부: Claude Code 플러그인 스킬이 더 풍부한 가이드 제공 가능

## Success Criteria

- [ ] 스킬이 viznoir 플러그인 설치 시 자동 로딩
- [ ] "유동 보여줘" 같은 vague 요청 → 적절한 도구 호출로 연결
- [ ] cinematic_render가 기본 렌더링 도구로 선택됨
- [ ] case-presets 리소스가 파라미터 결정에 활용됨
- [ ] body 500줄 이하
