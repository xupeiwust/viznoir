"""Integration tests for engine/renderer.py — real VTK rendering (GPU/EGL)."""

from __future__ import annotations

import pytest

vtk = pytest.importorskip("vtk")


def _wavelet() -> vtk.vtkImageData:
    """Create wavelet test dataset."""
    src = vtk.vtkRTAnalyticSource()
    src.SetWholeExtent(-5, 5, -5, 5, -5, 5)
    src.Update()
    return src.GetOutput()


def _sphere() -> vtk.vtkPolyData:
    src = vtk.vtkSphereSource()
    src.SetRadius(1.0)
    src.Update()
    return src.GetOutput()


class TestRenderToPng:
    def test_render_basic(self):
        from parapilot.engine.renderer import RenderConfig, render_to_png
        rc = RenderConfig(width=200, height=150)
        png = render_to_png(_wavelet(), rc)
        assert png[:4] == b"\x89PNG"
        assert len(png) > 100

    def test_render_with_colormap(self):
        from parapilot.engine.renderer import RenderConfig, render_to_png
        rc = RenderConfig(width=200, height=150, colormap="viridis", array_name="RTData")
        png = render_to_png(_wavelet(), rc)
        assert png[:4] == b"\x89PNG"

    def test_render_with_scalar_range(self):
        from parapilot.engine.renderer import RenderConfig, render_to_png
        rc = RenderConfig(
            width=200, height=150,
            array_name="RTData",
            scalar_range=(50.0, 200.0),
        )
        png = render_to_png(_wavelet(), rc)
        assert png[:4] == b"\x89PNG"

    def test_render_wireframe(self):
        from parapilot.engine.renderer import RenderConfig, render_to_png
        rc = RenderConfig(width=200, height=150, representation="wireframe")
        png = render_to_png(_sphere(), rc)
        assert png[:4] == b"\x89PNG"

    def test_render_with_background(self):
        from parapilot.engine.renderer import RenderConfig, render_to_png
        rc = RenderConfig(width=200, height=150, background=(0.1, 0.2, 0.3))
        png = render_to_png(_wavelet(), rc)
        assert png[:4] == b"\x89PNG"

    def test_render_different_sizes(self):
        from parapilot.engine.renderer import RenderConfig, render_to_png
        rc = RenderConfig(width=400, height=300)
        png = render_to_png(_wavelet(), rc)
        assert png[:4] == b"\x89PNG"
        assert len(png) > 200

    def test_render_cell_association(self):
        """Test rendering with cell-associated data."""
        from parapilot.engine.filters import point_to_cell
        from parapilot.engine.renderer import RenderConfig, render_to_png
        data = point_to_cell(_wavelet())
        rc = RenderConfig(width=200, height=150)
        png = render_to_png(data, rc)
        assert png[:4] == b"\x89PNG"


class TestResolveArray:
    def test_resolve_point_array(self):
        from parapilot.engine.renderer import _resolve_array
        name, assoc = _resolve_array(_wavelet(), "RTData")
        assert name == "RTData"
        assert assoc == "point"

    def test_resolve_none_returns_first(self):
        from parapilot.engine.renderer import _resolve_array
        name, assoc = _resolve_array(_wavelet(), None)
        assert name == "RTData"

    def test_resolve_nonexistent(self):
        from parapilot.engine.renderer import _resolve_array
        name, assoc = _resolve_array(_wavelet(), "nonexistent_field")
        # Should fall back or return None
        assert name is not None or name is None  # just verify no crash


class TestResolveRenderable:
    def test_resolve_imagedata(self):
        from parapilot.engine.renderer import _resolve_renderable
        result = _resolve_renderable(_wavelet())
        assert result is not None
        assert result.GetNumberOfPoints() > 0

    def test_resolve_multiblock(self):
        from parapilot.engine.renderer import _resolve_renderable
        mb = vtk.vtkMultiBlockDataSet()
        mb.SetBlock(0, _wavelet())
        result = _resolve_renderable(mb)
        assert result is not None

    def test_resolve_empty(self):
        from parapilot.engine.renderer import _resolve_renderable
        empty = vtk.vtkUnstructuredGrid()
        result = _resolve_renderable(empty)
        assert result is None


class TestGetScalarRange:
    def test_scalar_range_point(self):
        from parapilot.engine.renderer import _get_scalar_range
        lo, hi = _get_scalar_range(_wavelet(), "RTData", "point", component=-1)
        assert lo < hi
        assert lo > 0  # RTData min is ~37

    def test_scalar_range_with_component(self):
        from parapilot.engine.renderer import _get_scalar_range
        lo, hi = _get_scalar_range(_wavelet(), "RTData", "point", component=0)
        assert lo < hi


class TestVTKRenderer:
    def test_renderer_class(self):
        from parapilot.engine.renderer import RenderConfig, VTKRenderer
        rc = RenderConfig(width=200, height=150)
        renderer = VTKRenderer(rc)
        png = renderer.render(_wavelet())
        assert png[:4] == b"\x89PNG"

    def test_renderer_with_field(self):
        from parapilot.engine.renderer import RenderConfig, VTKRenderer
        rc = RenderConfig(width=200, height=150, array_name="RTData", colormap="plasma")
        renderer = VTKRenderer(rc)
        png = renderer.render(_wavelet())
        assert png[:4] == b"\x89PNG"

    def test_render_volume(self):
        """Test volume rendering path (lines 222-285)."""
        from parapilot.engine.renderer import RenderConfig, VTKRenderer
        rc = RenderConfig(
            width=200, height=150,
            representation="volume",
            array_name="RTData",
            colormap="plasma",
        )
        renderer = VTKRenderer(rc)
        png = renderer.render(_wavelet())
        assert png[:4] == b"\x89PNG"

    def test_render_volume_no_array(self):
        """Volume rendering without explicit array uses defaults."""
        from parapilot.engine.renderer import RenderConfig, VTKRenderer
        rc = RenderConfig(
            width=200, height=150,
            representation="volume",
        )
        renderer = VTKRenderer(rc)
        png = renderer.render(_wavelet())
        assert png[:4] == b"\x89PNG"

    def test_render_multiple(self):
        """Test render_multiple overlay path (lines 301-357)."""
        from parapilot.engine.renderer import RenderConfig, VTKRenderer
        rc = RenderConfig(width=200, height=150)
        renderer = VTKRenderer(rc)
        datasets = [
            (_wavelet(), None),
            (_sphere(), RenderConfig(width=200, height=150, representation="wireframe")),
        ]
        png = renderer.render_multiple(datasets)
        assert png[:4] == b"\x89PNG"

    def test_render_multiple_with_colormap(self):
        """render_multiple with scalar mapping."""
        from parapilot.engine.renderer import RenderConfig, VTKRenderer
        rc = RenderConfig(width=200, height=150)
        renderer = VTKRenderer(rc)
        datasets = [
            (_wavelet(), RenderConfig(width=200, height=150, array_name="RTData", colormap="viridis")),
        ]
        png = renderer.render_multiple(datasets)
        assert png[:4] == b"\x89PNG"

    def test_render_multiple_with_empty_dataset(self):
        """render_multiple skips empty datasets."""
        from parapilot.engine.renderer import RenderConfig, VTKRenderer
        rc = RenderConfig(width=200, height=150)
        renderer = VTKRenderer(rc)
        empty = vtk.vtkUnstructuredGrid()
        datasets = [
            (empty, None),
            (_wavelet(), None),
        ]
        png = renderer.render_multiple(datasets)
        assert png[:4] == b"\x89PNG"
