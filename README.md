# parapilot

Headless CAE post-processing MCP server for AI coding assistants.

```
pip install mcp-server-parapilot
```

## What it does

parapilot lets AI assistants (Claude Code, Cursor, Gemini CLI) render CFD/FEA simulation results without a GUI. It talks to ParaView headless or uses VTK directly to produce PNG screenshots, statistics, and animations from OpenFOAM, VTK, CGNS, and 30+ other formats.

## Quick Start

### Claude Code (plugin)

```bash
claude install kimimgo/parapilot
```

Then in a conversation:

> "Render the pressure field from cavity/cavity.foam with a jet colormap"

### Standalone MCP server

```json
{
  "mcpServers": {
    "parapilot": {
      "command": "mcp-server-parapilot"
    }
  }
}
```

### Docker (GPU headless)

```bash
docker compose up -d
```

Requires NVIDIA Container Toolkit for GPU rendering.

## Tools (13)

| Tool | Description |
|------|-------------|
| `inspect_data` | File metadata — fields, timesteps, bounds |
| `render` | Single-field PNG screenshot |
| `slice` | Cut-plane visualization |
| `contour` | Iso-surface visualization |
| `clip` | Clipped region visualization |
| `streamlines` | Vector field flow visualization |
| `extract_stats` | Min/max/mean/std for fields |
| `plot_over_line` | Sample values along a line |
| `integrate_surface` | Force/flux integration over surfaces |
| `animate` | Time series or camera orbit animation |
| `split_animate` | Multi-pane synchronized animation (GIF) |
| `execute_pipeline` | Full pipeline DSL for advanced workflows |
| `pv_isosurface` | DualSPHysics bi4 → VTK surface mesh |

## Resources (10)

| URI | Content |
|-----|---------|
| `parapilot://formats` | Supported file formats and readers |
| `parapilot://filters` | Available filter parameters |
| `parapilot://colormaps` | Colormap presets |
| `parapilot://cameras` | Camera angle presets |
| `parapilot://representations` | Render representations |
| `parapilot://case-presets` | Domain-specific case presets |
| `parapilot://physics-defaults` | Physics-aware rendering defaults |
| `parapilot://pipelines/cfd` | CFD pipeline examples |
| `parapilot://pipelines/fea` | FEA pipeline examples |
| `parapilot://pipelines/split-animate` | Split animation examples |

## Architecture

```
┌─────────────────────────────────────────────┐
│  AI Assistant (Claude / Cursor / Gemini)    │
│  ↕ MCP protocol (stdio)                    │
├─────────────────────────────────────────────┤
│  parapilot MCP Server (FastMCP)             │
│  ├── tools/     13 MCP tools                │
│  ├── resources/ 10 MCP resources            │
│  └── prompts/   3 MCP prompts               │
├─────────────────────────────────────────────┤
│  Engine Layer (VTK direct API)              │
│  ├── readers    OpenFOAM, VTK, CGNS, ...    │
│  ├── filters    Slice, Contour, Clip, ...   │
│  ├── renderer   Off-screen VTK rendering    │
│  ├── camera     Preset + custom positions   │
│  ├── colormaps  Scientific color schemes    │
│  ├── overlay    Scalar bars, labels, text   │
│  ├── physics    Auto-detect field types     │
│  └── export     PNG, VTK, CSV output        │
├─────────────────────────────────────────────┤
│  Core Layer                                 │
│  ├── compiler   Pipeline → VTK script       │
│  ├── runner     Local / Docker execution    │
│  ├── registry   Filter & format schemas     │
│  └── output     Result collection           │
└─────────────────────────────────────────────┘
```

## Workflow

```
inspect_data → render / slice / contour → extract_stats → animate
```

1. **Inspect** — discover fields, timesteps, bounds
2. **Visualize** — render, slice, contour, clip, streamlines
3. **Extract** — statistics, line plots, surface integrals
4. **Animate** — time series or multi-pane comparison

## Supported Formats

OpenFOAM (.foam), VTK (.vti/.vtp/.vtu/.vtm), CGNS (.cgns), Ensight (.case), Exodus (.exo), STL (.stl), PLY (.ply), OBJ (.obj), and 30+ more via VTK readers.

## Development

```bash
git clone https://github.com/kimimgo/parapilot
cd parapilot
pip install -e ".[dev]"
pytest                     # 295 tests
ruff check src/ tests/     # lint
mypy src/parapilot/        # type check
```

## vs Alternatives

| | parapilot | LLNL/paraview_mcp | Kitware/vtk-mcp |
|---|---|---|---|
| Rendering | Headless VTK + ParaView | GUI-attached only | None (docs search) |
| Tests | 295 | 0 | 0 |
| Docker | GPU (EGL) | No | No |
| MCP Tools | 13 | 5 | 3 |
| Plugin | Claude Code plugin | No | No |

## License

MIT
