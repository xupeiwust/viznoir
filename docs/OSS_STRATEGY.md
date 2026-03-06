# parapilot OSS Strategy

> Last updated: 2026-03-06

## 1. KPI Dashboard

| Metric | Current | 1-month | 3-month | 6-month |
|--------|---------|---------|---------|---------|
| GitHub Stars | 0 | 30+ | 100+ | 200+ |
| Forks | 4 | 10+ | 25+ | 50+ |
| Contributors | 2 | 5+ | 10+ | 20+ |
| PyPI Downloads/month | ~0 | 200+ | 1,000+ | 5,000+ |
| Open Issues | 15 | 20+ | 15 (managed) | 10 (managed) |
| Closed Issues | 0 | 10+ | 30+ | 60+ |
| Clones (14d) | 604 | 300+ | 500+ | 1,000+ |
| Views (14d) | 2 | 100+ | 500+ | 2,000+ |
| MCP Registry listings | 0 | 3+ | 5+ | 5+ |
| JOSS Paper | - | - | submitted | accepted |

## 2. Automation Inventory

### Active

| Automation | Status | File |
|-----------|--------|------|
| CI (lint + type + test) | `.github/workflows/ci.yml` | Python 3.10/3.12 |
| GitHub Pages deploy | `.github/workflows/deploy.yml` | Astro landing page |
| PyPI publish | `.github/workflows/publish.yml` | Trusted publisher |
| Auto-merge (dependabot) | `.github/workflows/auto-merge.yml` | Minor/patch |
| Stale bot | `.github/workflows/stale.yml` | 60d stale, 14d close |
| Welcome bot | `.github/workflows/welcome.yml` | First-time contributors |
| Dependabot | `.github/dependabot.yml` | pip + npm weekly |
| All Contributors | `.all-contributorsrc` | README contributor table |

### Recommended (P1)

| Automation | Priority | Description |
|-----------|----------|-------------|
| Release Drafter | P1 | Auto-generate release notes from PR labels |
| CodeQL | P1 | Security scanning on PRs |
| Semantic PR title check | P2 | Enforce conventional commits in PR titles |
| Auto-label | P2 | Label PRs by file paths changed |

## 3. Promotion Strategy

### Phase A: Foundation (Week 1-2)

1. **MCP Registry Registration** (5 targets)
   - Smithery.ai (`smithery.yaml` ready)
   - Anthropic official registry
   - awesome-mcp-servers (GitHub PR)
   - Glama.ai
   - mcp.run

2. **GitHub Topics Optimization**
   Current: `cae, cfd, claude-code, headless-rendering, mcp, model-context-protocol, paraview, post-processing, simulation, vtk`
   Add: `openfoam, fea, scientific-visualization, ai-tools, engineering`

3. **PyPI Metadata**
   - Keywords, classifiers, project URLs all set
   - Trusted Publisher configured

### Phase B: Community Launch (Week 3-4)

4. **Reddit Posts**
   - r/CFD: "I built a headless CAE post-processing tool that talks to AI assistants"
   - r/OpenFOAM: "Render OpenFOAM results from your terminal with AI"
   - r/MachineLearning: "MCP server for scientific visualization"
   - r/Python: "VTK-based headless CAE rendering as an MCP server"

5. **Hacker News**
   - "Show HN: parapilot — Headless CAE post-processing via AI coding assistants"
   - Best time: Tuesday-Thursday, 9-11am EST

6. **CFD Community**
   - CFD-Online Forum tool listing
   - SimScale community post
   - OpenFOAM Wiki mention

### Phase C: Academic & Industry (Month 2-3)

7. **JOSS Paper**
   - `paper/paper.md` + `paper/paper.bib`
   - Zenodo DOI from GitHub release
   - Title: "parapilot: Headless CAE Post-Processing through AI Coding Assistants"

8. **Conference Talks**
   - OpenFOAM Workshop abstract
   - SciPy Conference poster

## 4. SEO Keywords

### Primary (search volume + relevance)
- `mcp server cad` / `mcp server cfd`
- `headless vtk rendering`
- `openfoam ai post-processing`
- `claude code simulation`
- `paraview alternative python`

### Secondary
- `vtk headless docker`
- `cfd visualization api`
- `scientific visualization mcp`
- `ai-assisted engineering`
- `model context protocol scientific`

### Long-tail
- `how to render openfoam results without gui`
- `vtk offscreen rendering python`
- `claude code cfd workflow`
- `mcp server for engineering simulation`

## 5. Branding

### Identity

| Element | Value |
|---------|-------|
| **Name** | parapilot |
| **Tagline** | "Headless CAE post-processing for AI assistants" |
| **Short** | "Ask your AI to render your simulation" |
| **Color** | `#00d4ff` (accent), `#0a0a0a` (dark bg) |
| **Font** | Inter (body) + JetBrains Mono (code) |
| **Tone** | Technical, confident, concise. No hype. |

### Positioning

**What we are**: The only headless scientific visualization server that speaks MCP.

**What we are NOT**:
- Not a ParaView replacement
- Not a complete CAE platform
- Not a simulation runner

### Messaging Framework

| Audience | Key Message |
|----------|-------------|
| **CFD Engineers** | "Render your OpenFOAM/CGNS results with a single prompt. No GUI, no boilerplate." |
| **AI Developers** | "Give your LLM eyes for simulation data. 18 tools, 627 tests, plug and play." |
| **Researchers** | "Reproducible visualization pipelines. JSON DSL + version control = auditable science." |
| **OSS Contributors** | "Well-tested (70% coverage), well-documented, good-first-issues ready. Ship real impact." |

### Logo Direction
- Abstract: wireframe mesh + pilot/compass motif
- Colors: gradient from `#00d4ff` to `#0066ff`
- Style: minimal, geometric, works at 16px favicon size
- Format: SVG primary, PNG fallback

### Social Preview
- 1280x640px, dark background (`#0a0a0a`)
- DrivAerML showcase image + tagline overlay
- Badge strip: "18 Tools | 627 Tests | MIT License"

## 6. Contributor Growth Strategy

### Good First Issues Pipeline
Always maintain 5-8 open `good first issue` tags covering:
- Documentation improvements
- Colormap/preset additions
- Type hint additions
- Test coverage gaps
- Small feature enhancements

### Contribution Recognition
- All Contributors bot (README table)
- Release notes credit
- CONTRIBUTORS.md with detailed roles

### Mentorship
- Clear CONTRIBUTING.md with architecture guide
- Issue templates with expected difficulty + estimated time
- PR review within 24-48h
- Welcoming bot for first-time contributors

### Incentives
- "Hacktoberfest" label for October
- GSoC project ideas (already labeled)
- JOSS paper co-authorship for significant contributions

## 7. Competitive Moat

Features competitors cannot easily replicate:

1. **Pipeline DSL** — Declarative JSON filter chains with code generation
2. **Physics-aware defaults** — Auto-detect field types from names
3. **Split-pane animation** — Synchronized multi-view + graph GIF
4. **627 tests** — Most tested MCP server in the scientific viz space
5. **Dual execution** — Local VTK + Docker GPU (EGL) transparent switching
6. **Claude Code plugin** — One-line install: `claude install kimimgo/parapilot`
