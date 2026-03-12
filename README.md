# viznoir

**English** | [한국어](README.ko.md)

> VTK is all you need. Cinema-quality science visualization for AI agents.

[![CI](https://github.com/kimimgo/viznoir/actions/workflows/ci.yml/badge.svg)](https://github.com/kimimgo/viznoir/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/mcp-server-viznoir)](https://pypi.org/project/mcp-server-viznoir/)
[![Python](https://img.shields.io/pypi/pyversions/mcp-server-viznoir)](https://pypi.org/project/mcp-server-viznoir/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/kimimgo/viznoir/blob/main/LICENSE)

## 10 Domains, One Pipeline

Every render below is a single MCP tool call — no GUI, no post-processing, no ParaView.

| | | |
|:---:|:---:|:---:|
| ![Medical](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/01_skull_annotated.webp) | ![Combustion CFD](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/02_combustion_annotated.webp) | ![Thermal](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/03_heatsink_annotated.webp) |
| **Medical** — CT skull volume | **CFD** — Combustion streamlines | **Thermal** — Heatsink gradient |
| ![Geoscience](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/04_seismic_annotated.webp) | ![Automotive](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/05_drivaerml_annotated.webp) | ![Molecular](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/06_h2o_annotated.webp) |
| **Geoscience** — Seismic wavefield | **Automotive** — DrivAerML Cp 8.8M cells | **Molecular** — H₂O electron density |
| ![Vascular](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/07_aneurism_annotated.webp) | ![Planetary](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/08_bennu_annotated.webp) | ![Structural](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/09_cantilever_annotated.webp) |
| **Vascular** — Cerebral aneurysm MRA | **Planetary** — Bennu asteroid 196K tri | **Structural** — Cantilever FEA stress |

## Physics-Driven Animations

Not slideshows — real VTK frame-by-frame rendering where every effect has a physical reason.

| Animation | Physics | Technique |
|-----------|---------|-----------|
| Streamline Growth | Lagrangian advection from nozzle | `streamline_growth` |
| Clip Sweep | Cross-section along pressure gradient | `clip_sweep` |
| Layer Reveal | CT density layer classification | `layer_reveal` |
| Iso Sweep | Electron orbital topology | `iso_sweep` |
| Warp Oscillation | Structural mode shape | `warp_oscillation` |
| Light Orbit | Geomorphology oblique illumination | `light_orbit` |
| Threshold Reveal | Volume feature hierarchy | `threshold_reveal` |

All presets available in `viznoir.anim.physics`.

## Science Storytelling

Extract physics insights and compose them into publication-ready stories.

```
"Analyze the cavity flow and show me what's happening"

→ inspect_physics: 20 stagnation points, ω range [-15.2, +19.6]/s
→ cinematic_render × 4: velocity, pressure, vorticity, temperature
→ compose_assets: LaTeX equations + insight labels + story layout
```

![Science Storytelling](https://raw.githubusercontent.com/kimimgo/viznoir/main/www/public/showcase/cavity_story.webp)

## Quick Start

```bash
pip install mcp-server-viznoir
```

**Claude Code:**

```bash
claude install kimimgo/viznoir
```

**MCP config (Cursor / Windsurf / any client):**

```json
{
  "mcpServers": {
    "viznoir": {
      "command": "mcp-server-viznoir"
    }
  }
}
```

**Docker (GPU headless):**

```bash
docker compose up -d
```

## Architecture

```
  prompt                    "Render pressure from cavity.foam"
    │
  MCP Server                22 tools · 12 resources · 4 prompts
    │
  VTK Engine                readers → filters → renderer → camera
    │                       EGL/OSMesa headless · cinematic lighting
  Physics Layer             topology analysis · context parsing
    │                       vortex detection · stagnation points
  Animation                 7 physics presets · easing · timeline
    │                       transitions · compositor · video export
  Output                    PNG · WebP · MP4 · GLTF · LaTeX
```

## Numbers

| | |
|---|---|
| **22** MCP tools | **1489+** tests |
| **12** resources | **97%** coverage |
| **10** domains | **50+** file formats |
| **7** animation presets | **17** easing functions |

## License

MIT
