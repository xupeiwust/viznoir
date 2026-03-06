"""Shared test fixtures."""

from __future__ import annotations

import os

import pytest

from parapilot.config import PVConfig
from parapilot.core.compiler import ScriptCompiler


def _can_vtk_render() -> bool:
    """Check if VTK can create an offscreen render window without segfault."""
    if os.environ.get("CI"):
        return False  # GitHub Actions has no GPU/OpenGL
    try:
        import vtk
        rw = vtk.vtkRenderWindow()
        rw.SetOffScreenRendering(True)
        rw.SetSize(64, 64)
        rw.Render()
        rw.Finalize()
        return True
    except Exception:
        return False


CAN_RENDER = _can_vtk_render()

requires_rendering = pytest.mark.skipif(
    not CAN_RENDER,
    reason="VTK offscreen rendering not available (CI or no GPU)",
)


@pytest.fixture
def compiler() -> ScriptCompiler:
    return ScriptCompiler()


@pytest.fixture
def config() -> PVConfig:
    return PVConfig(data_dir="/data", output_dir="/output")
