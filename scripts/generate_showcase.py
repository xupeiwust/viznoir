#!/usr/bin/env python3
"""Generate showcase renders for the landing page.

Uses official VTK example datasets from pyvista/vtk-data repository.
Each render runs in a separate subprocess to ensure clean VTK state.
"""

from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
OUT_DIR = PROJECT_ROOT / "www" / "public" / "showcase"
DATA_DIR = Path("/tmp/vtk-showcase")

# Base URL for pyvista/vtk-data
VTK_DATA_URL = "https://raw.githubusercontent.com/pyvista/vtk-data/master/Data"

# Files to download
DATA_FILES = [
    "cow.vtp",
    "bunny.ply",
    "dragon.ply",
    "head.vti",
    "disk_out_ref_surface.vtp",
    "Human.vtp",
]

# Each render is a standalone Python snippet executed in its own process.

RENDERS: dict[str, str] = {
    # 1. CFD: disk_out_ref temperature field
    "cfd_temperature": textwrap.dedent("""\
        import vtk
        from parapilot.engine.filters import apply_filter
        from parapilot.engine.renderer import RenderConfig, render_to_png
        from parapilot.engine.camera import CameraConfig

        reader = vtk.vtkXMLPolyDataReader()
        reader.SetFileName(DATA_DIR + '/disk_out_ref_surface.vtp')
        reader.Update()
        data = reader.GetOutput()

        cam = CameraConfig(position=(25.0, 20.0, 28.0), focal_point=(0, 0, 0), view_up=(0, 0, 1))
        cfg = RenderConfig(
            width=1920, height=1080, background=(0.04, 0.04, 0.06),
            colormap='cool to warm', array_name='Temp',
            show_scalar_bar=True, scalar_bar_title='Temperature',
        )
        PNG = render_to_png(data, cfg, cam)
    """),

    # 2. CFD: disk_out_ref pressure field
    "cfd_pressure": textwrap.dedent("""\
        import vtk
        from parapilot.engine.filters import apply_filter
        from parapilot.engine.renderer import RenderConfig, render_to_png
        from parapilot.engine.camera import CameraConfig

        reader = vtk.vtkXMLPolyDataReader()
        reader.SetFileName(DATA_DIR + '/disk_out_ref_surface.vtp')
        reader.Update()
        data = reader.GetOutput()

        cam = CameraConfig(position=(-22.0, 24.0, 22.0), focal_point=(0, 0, 0), view_up=(0, 0, 1))
        cfg = RenderConfig(
            width=1920, height=1080, background=(0.04, 0.04, 0.06),
            colormap='viridis', array_name='Pres',
            show_scalar_bar=True, scalar_bar_title='Pressure',
        )
        PNG = render_to_png(data, cfg, cam)
    """),

    # 3. Medical: head CT slice
    "ct_head_slice": textwrap.dedent("""\
        import vtk
        from parapilot.engine.filters import apply_filter
        from parapilot.engine.renderer import RenderConfig, render_to_png
        from parapilot.engine.camera import CameraConfig

        reader = vtk.vtkXMLImageDataReader()
        reader.SetFileName(DATA_DIR + '/head.vti')
        reader.Update()
        data = reader.GetOutput()

        sliced = apply_filter(data, 'slice', origin=[128, 128, 93], normal=[0, 0, 1])
        cam = CameraConfig(position=(128, 128, 400), focal_point=(128, 128, 93), view_up=(0, 1, 0))
        cfg = RenderConfig(
            width=1920, height=1080, background=(0.04, 0.04, 0.06),
            colormap='grayscale', array_name='Scalars_',
            show_scalar_bar=True, scalar_bar_title='CT Density',
        )
        PNG = render_to_png(sliced, cfg, cam)
    """),

    # 4. Medical: head CT contour (skull isosurface)
    "ct_head_contour": textwrap.dedent("""\
        import vtk
        from parapilot.engine.filters import apply_filter
        from parapilot.engine.renderer import RenderConfig, render_to_png
        from parapilot.engine.camera import CameraConfig

        reader = vtk.vtkXMLImageDataReader()
        reader.SetFileName(DATA_DIR + '/head.vti')
        reader.Update()
        data = reader.GetOutput()

        contoured = apply_filter(data, 'contour', array_name='Scalars_', values=[1200])
        cam = CameraConfig(position=(350, 200, 250), focal_point=(128, 128, 93), view_up=(0, 0, 1))
        cfg = RenderConfig(
            width=1920, height=1080, background=(0.04, 0.04, 0.06),
            colormap='turbo', array_name='Scalars_',
            show_scalar_bar=True, scalar_bar_title='CT Density',
        )
        PNG = render_to_png(contoured, cfg, cam)
    """),

    # 5. Geometry: Stanford Dragon with Elevation
    "dragon": textwrap.dedent("""\
        import vtk
        from parapilot.engine.renderer import RenderConfig, render_to_png
        from parapilot.engine.camera import CameraConfig

        reader = vtk.vtkPLYReader()
        reader.SetFileName(DATA_DIR + '/dragon.ply')
        reader.Update()

        norms = vtk.vtkPolyDataNormals()
        norms.SetInputData(reader.GetOutput())
        norms.ComputePointNormalsOn()
        norms.Update()

        elev = vtk.vtkElevationFilter()
        elev.SetInputConnection(norms.GetOutputPort())
        b = reader.GetOutput().GetBounds()
        elev.SetLowPoint(0, b[2], 0)
        elev.SetHighPoint(0, b[3], 0)
        elev.Update()

        cam = CameraConfig(position=(0.15, 0.18, 0.15), focal_point=(0, 0.15, -0.04), view_up=(0, 1, 0))
        cfg = RenderConfig(
            width=1920, height=1080, background=(0.04, 0.04, 0.06),
            colormap='plasma', array_name='Elevation',
            show_scalar_bar=True, scalar_bar_title='Elevation',
        )
        PNG = render_to_png(elev.GetOutput(), cfg, cam)
    """),

    # 6. Geometry: Cow with Elevation
    "cow": textwrap.dedent("""\
        import vtk
        from parapilot.engine.renderer import RenderConfig, render_to_png
        from parapilot.engine.camera import CameraConfig

        reader = vtk.vtkXMLPolyDataReader()
        reader.SetFileName(DATA_DIR + '/cow.vtp')
        reader.Update()

        norms = vtk.vtkPolyDataNormals()
        norms.SetInputData(reader.GetOutput())
        norms.ComputePointNormalsOn()
        norms.Update()

        elev = vtk.vtkElevationFilter()
        elev.SetInputConnection(norms.GetOutputPort())
        b = reader.GetOutput().GetBounds()
        elev.SetLowPoint(0, b[2], 0)
        elev.SetHighPoint(0, b[3], 0)
        elev.Update()

        cam = CameraConfig(position=(10, 5, 8), focal_point=(0.5, -0.5, 0), view_up=(0, 1, 0))
        cfg = RenderConfig(
            width=1920, height=1080, background=(0.04, 0.04, 0.06),
            colormap='magma', array_name='Elevation',
            show_scalar_bar=True, scalar_bar_title='Elevation',
        )
        PNG = render_to_png(elev.GetOutput(), cfg, cam)
    """),
}


def download_data() -> bool:
    """Download example data files from pyvista/vtk-data."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    all_ok = True
    for fname in DATA_FILES:
        target = DATA_DIR / fname
        if target.exists() and target.stat().st_size > 0:
            print(f"  {fname}: cached ({target.stat().st_size // 1024}KB)")
            continue
        url = f"{VTK_DATA_URL}/{fname}"
        print(f"  {fname}: downloading...", end=" ", flush=True)
        result = subprocess.run(
            ["curl", "-sLo", str(target), url],
            capture_output=True, text=True, timeout=120,
        )
        if result.returncode != 0 or not target.exists():
            print("FAIL")
            all_ok = False
        else:
            print(f"OK ({target.stat().st_size // 1024}KB)")
    return all_ok


def run_render(name: str, code: str) -> bool:
    """Run a render in an isolated subprocess."""
    import os

    preamble = (
        f"import sys, io, os\n"
        f"os.environ['VTK_DEFAULT_OPENGL_WINDOW'] = 'vtkEGLRenderWindow'\n"
        f"sys.path.insert(0, {str(PROJECT_ROOT / 'src')!r})\n"
        f"DATA_DIR = {str(DATA_DIR)!r}\n\n"
    )
    postamble = (
        "\n# Save optimized 960x540\n"
        "from PIL import Image\n"
        f"out_path = {str(OUT_DIR)!r} + '/{name}.png'\n"
        "img = Image.open(io.BytesIO(PNG))\n"
        "resized = img.resize((960, 540), Image.LANCZOS)\n"
        "resized.save(out_path, 'PNG', optimize=True)\n"
        "import os\n"
        "print(f'{os.path.getsize(out_path) // 1024}KB')\n"
    )
    wrapper = preamble + code + postamble

    env = {**os.environ, "VTK_DEFAULT_OPENGL_WINDOW": "vtkEGLRenderWindow"}
    env.pop("DISPLAY", None)  # Force EGL, avoid GLX attempts

    result = subprocess.run(
        [sys.executable, "-c", wrapper],
        capture_output=True, text=True, timeout=120,
        env=env,
    )

    if result.returncode != 0:
        err = result.stderr.strip().splitlines()[-1] if result.stderr else "unknown"
        print(f"  FAIL: {err}")
        if result.stderr:
            # Print last 5 lines for debugging
            for line in result.stderr.strip().splitlines()[-5:]:
                print(f"    {line}")
        return False

    size = result.stdout.strip()
    print(f"  {name}.png: {size}")
    return True


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Downloading {len(DATA_FILES)} example datasets...\n")
    download_data()

    print(f"\nGenerating {len(RENDERS)} showcase renders (isolated subprocess per render)...\n")

    success = 0
    for i, (name, code) in enumerate(RENDERS.items(), 1):
        print(f"[{i}/{len(RENDERS)}] {name}")
        if run_render(name, code):
            success += 1

    print(f"\nDone: {success}/{len(RENDERS)} renders saved to {OUT_DIR}")


if __name__ == "__main__":
    main()
