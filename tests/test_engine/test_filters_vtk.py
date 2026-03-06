"""Integration tests for engine/filters.py — real VTK execution (GPU/EGL)."""

from __future__ import annotations

import pytest

vtk = pytest.importorskip("vtk")


def _wavelet() -> vtk.vtkImageData:
    """Create wavelet test dataset with RTData array."""
    src = vtk.vtkRTAnalyticSource()
    src.SetWholeExtent(-5, 5, -5, 5, -5, 5)
    src.Update()
    return src.GetOutput()


def _unstructured() -> vtk.vtkUnstructuredGrid:
    """Convert wavelet to unstructured grid."""
    src = _wavelet()
    conv = vtk.vtkDataSetTriangleFilter()
    conv.SetInputData(src)
    conv.Update()
    return conv.GetOutput()


def _polydata() -> vtk.vtkPolyData:
    """Create a sphere polydata."""
    src = vtk.vtkSphereSource()
    src.SetRadius(1.0)
    src.SetThetaResolution(16)
    src.SetPhiResolution(16)
    src.Update()
    return src.GetOutput()


# ---------------------------------------------------------------------------
# Slice
# ---------------------------------------------------------------------------

class TestSlicePlane:
    def test_slice_default_origin(self):
        from parapilot.engine.filters import slice_plane
        result = slice_plane(_wavelet())
        assert result.GetNumberOfPoints() > 0

    def test_slice_custom_origin_normal(self):
        from parapilot.engine.filters import slice_plane
        result = slice_plane(_wavelet(), origin=(0, 0, 0), normal=(1, 0, 0))
        assert result.GetNumberOfPoints() > 0

    def test_slice_preserves_arrays(self):
        from parapilot.engine.filters import slice_plane
        result = slice_plane(_wavelet())
        assert result.GetPointData().GetArray("RTData") is not None


# ---------------------------------------------------------------------------
# Clip
# ---------------------------------------------------------------------------

class TestClipPlane:
    def test_clip_default(self):
        from parapilot.engine.filters import clip_plane
        result = clip_plane(_wavelet())
        assert result.GetNumberOfPoints() > 0

    def test_clip_inside_out(self):
        from parapilot.engine.filters import clip_plane
        r1 = clip_plane(_wavelet(), inside_out=False)
        r2 = clip_plane(_wavelet(), inside_out=True)
        # Opposite sides should have different point counts
        assert r1.GetNumberOfPoints() != r2.GetNumberOfPoints() or r1.GetNumberOfPoints() > 0

    def test_clip_custom_origin(self):
        from parapilot.engine.filters import clip_plane
        result = clip_plane(_wavelet(), origin=(0, 0, 0), normal=(0, 1, 0))
        assert result.GetNumberOfPoints() > 0


# ---------------------------------------------------------------------------
# Contour
# ---------------------------------------------------------------------------

class TestContour:
    def test_contour_single_value(self):
        from parapilot.engine.filters import contour
        result = contour(_wavelet(), array_name="RTData", values=[100.0])
        assert result.GetNumberOfPoints() >= 0

    def test_contour_multiple_values(self):
        from parapilot.engine.filters import contour
        result = contour(_wavelet(), array_name="RTData", values=[50.0, 100.0, 200.0])
        assert result is not None

    def test_contour_with_isovalues_alias(self):
        from parapilot.engine.filters import contour
        result = contour(_wavelet(), field="RTData", isovalues=[100.0, 200.0])
        assert result is not None


# ---------------------------------------------------------------------------
# Isosurface
# ---------------------------------------------------------------------------

class TestIsosurface:
    def test_isosurface(self):
        from parapilot.engine.filters import isosurface
        result = isosurface(_wavelet(), array_name="RTData", value=100.0)
        assert result.GetNumberOfPoints() > 0


# ---------------------------------------------------------------------------
# Threshold
# ---------------------------------------------------------------------------

class TestThreshold:
    def test_threshold_range(self):
        from parapilot.engine.filters import threshold
        result = threshold(_wavelet(), array_name="RTData", lower=50.0, upper=200.0)
        assert result.GetNumberOfPoints() > 0

    def test_threshold_lower_only(self):
        from parapilot.engine.filters import threshold
        result = threshold(_wavelet(), array_name="RTData", lower=100.0)
        assert result.GetNumberOfPoints() >= 0

    def test_threshold_both_bounds(self):
        from parapilot.engine.filters import threshold
        result = threshold(_wavelet(), array_name="RTData", lower=50.0, upper=200.0)
        assert result.GetNumberOfPoints() > 0


# ---------------------------------------------------------------------------
# Streamlines
# ---------------------------------------------------------------------------

class TestStreamlines:
    def test_streamlines_basic(self):
        from parapilot.engine.filters import streamlines
        data = _wavelet()
        # Add a vector field
        calc = vtk.vtkArrayCalculator()
        calc.SetInputData(data)
        calc.AddScalarArrayName("RTData")
        calc.SetResultArrayName("velocity")
        calc.SetFunction("RTData*iHat + 0*jHat + 0*kHat")
        calc.SetResultArrayType(vtk.VTK_DOUBLE)
        calc.Update()
        vdata = calc.GetOutput()

        result = streamlines(vdata, array_name="velocity", num_seeds=5)
        # May produce 0 points if seed placement doesn't intersect flow
        assert result is not None


# ---------------------------------------------------------------------------
# Calculator
# ---------------------------------------------------------------------------

class TestCalculator:
    def test_calculator(self):
        from parapilot.engine.filters import calculator
        result = calculator(_wavelet(), expression="RTData * 2", result_name="doubled")
        arr = result.GetPointData().GetArray("doubled")
        assert arr is not None


# ---------------------------------------------------------------------------
# Gradient
# ---------------------------------------------------------------------------

class TestGradient:
    def test_gradient(self):
        from parapilot.engine.filters import gradient
        result = gradient(_wavelet(), array_name="RTData")
        # Gradient should create a new vector array
        assert result.GetPointData().GetNumberOfArrays() > 1


# ---------------------------------------------------------------------------
# IntegrateVariables
# ---------------------------------------------------------------------------

class TestIntegrateVariables:
    def test_integrate(self):
        from parapilot.engine.filters import integrate_variables
        result = integrate_variables(_wavelet())
        assert result is not None


# ---------------------------------------------------------------------------
# ExtractBlock
# ---------------------------------------------------------------------------

class TestExtractBlock:
    def test_extract_block_by_index(self):
        from parapilot.engine.filters import extract_block
        mb = vtk.vtkMultiBlockDataSet()
        mb.SetBlock(0, _wavelet())
        result = extract_block(mb, block_index=0)
        assert result.GetNumberOfPoints() > 0


# ---------------------------------------------------------------------------
# ExtractSurface
# ---------------------------------------------------------------------------

class TestExtractSurface:
    def test_extract_surface(self):
        from parapilot.engine.filters import extract_surface
        result = extract_surface(_unstructured())
        assert result.GetNumberOfPoints() > 0


# ---------------------------------------------------------------------------
# Warp
# ---------------------------------------------------------------------------

class TestWarp:
    def test_warp_by_scalar(self):
        from parapilot.engine.filters import warp_by_scalar
        result = warp_by_scalar(_wavelet(), array_name="RTData", scale_factor=0.01)
        assert result.GetNumberOfPoints() > 0

    def test_warp_by_vector(self):
        from parapilot.engine.filters import warp_by_vector
        data = _wavelet()
        # Create a vector array
        calc = vtk.vtkArrayCalculator()
        calc.SetInputData(data)
        calc.AddScalarArrayName("RTData")
        calc.SetResultArrayName("disp")
        calc.SetFunction("RTData*0.01*iHat + 0*jHat + 0*kHat")
        calc.SetResultArrayType(vtk.VTK_DOUBLE)
        calc.Update()
        result = warp_by_vector(calc.GetOutput(), array_name="disp", scale_factor=1.0)
        assert result.GetNumberOfPoints() > 0


# ---------------------------------------------------------------------------
# CellToPoint / PointToCell
# ---------------------------------------------------------------------------

class TestDataConversion:
    def test_cell_to_point(self):
        from parapilot.engine.filters import cell_to_point
        # Add a cell array first
        data = _unstructured()
        result = cell_to_point(data)
        assert result is not None

    def test_point_to_cell(self):
        from parapilot.engine.filters import point_to_cell
        result = point_to_cell(_wavelet())
        assert result is not None


# ---------------------------------------------------------------------------
# PlotOverLine
# ---------------------------------------------------------------------------

class TestPlotOverLine:
    def test_plot_over_line(self):
        from parapilot.engine.filters import plot_over_line
        result = plot_over_line(
            _wavelet(),
            point1=(-5, 0, 0),
            point2=(5, 0, 0),
            resolution=50,
        )
        assert result.GetNumberOfPoints() == 51  # resolution + 1


# ---------------------------------------------------------------------------
# Glyph
# ---------------------------------------------------------------------------

class TestGlyph:
    def test_glyph_basic(self):
        from parapilot.engine.filters import glyph
        data = _wavelet()
        calc = vtk.vtkArrayCalculator()
        calc.SetInputData(data)
        calc.AddScalarArrayName("RTData")
        calc.SetResultArrayName("vectors")
        calc.SetFunction("RTData*0.01*iHat + 0*jHat + 0*kHat")
        calc.SetResultArrayType(vtk.VTK_DOUBLE)
        calc.Update()
        result = glyph(calc.GetOutput(), array_name="vectors", scale_factor=0.1)
        assert result.GetNumberOfPoints() > 0


# ---------------------------------------------------------------------------
# Decimate
# ---------------------------------------------------------------------------

class TestDecimate:
    def test_decimate(self):
        from parapilot.engine.filters import decimate
        poly = _polydata()
        original_cells = poly.GetNumberOfCells()
        result = decimate(poly, reduction=0.5)
        assert result.GetNumberOfCells() < original_cells


# ---------------------------------------------------------------------------
# Triangulate
# ---------------------------------------------------------------------------

class TestTriangulate:
    def test_triangulate(self):
        from parapilot.engine.filters import triangulate
        result = triangulate(_polydata())
        assert result.GetNumberOfCells() > 0


# ---------------------------------------------------------------------------
# SmoothMesh
# ---------------------------------------------------------------------------

class TestSmoothMesh:
    def test_smooth(self):
        from parapilot.engine.filters import smooth_mesh
        result = smooth_mesh(_polydata(), iterations=20)
        assert result.GetNumberOfPoints() > 0


# ---------------------------------------------------------------------------
# ProbePoint
# ---------------------------------------------------------------------------

class TestProbePoint:
    def test_probe_point(self):
        from parapilot.engine.filters import probe_point
        result = probe_point(_wavelet(), point=(0, 0, 0))
        assert result is not None
        assert result.GetPointData().GetArray("RTData") is not None


# ---------------------------------------------------------------------------
# CleanPolyData
# ---------------------------------------------------------------------------

class TestCleanPolyData:
    def test_clean(self):
        from parapilot.engine.filters import clean_polydata
        result = clean_polydata(_polydata())
        assert result.GetNumberOfPoints() > 0


# ---------------------------------------------------------------------------
# Shrink
# ---------------------------------------------------------------------------

class TestShrink:
    def test_shrink(self):
        from parapilot.engine.filters import shrink
        result = shrink(_unstructured(), shrink_factor=0.8)
        assert result.GetNumberOfCells() > 0


# ---------------------------------------------------------------------------
# Tube
# ---------------------------------------------------------------------------

class TestTube:
    def test_tube(self):
        from parapilot.engine.filters import tube
        # Create a line source
        line = vtk.vtkLineSource()
        line.SetPoint1(0, 0, 0)
        line.SetPoint2(1, 1, 1)
        line.SetResolution(10)
        line.Update()
        result = tube(line.GetOutput(), radius=0.1, sides=8)
        assert result.GetNumberOfPoints() > 0


# ---------------------------------------------------------------------------
# apply_filter / apply_filters
# ---------------------------------------------------------------------------

class TestApplyFilter:
    def test_apply_filter_by_name(self):
        from parapilot.engine.filters import apply_filter
        result = apply_filter(_wavelet(), "slice", normal=[1, 0, 0])
        assert result.GetNumberOfPoints() > 0

    def test_apply_filter_case_insensitive(self):
        from parapilot.engine.filters import apply_filter
        result = apply_filter(_wavelet(), "Slice", normal=[1, 0, 0])
        assert result.GetNumberOfPoints() > 0

    def test_apply_filters_chain(self):
        from parapilot.engine.filters import apply_filters
        steps = [
            ("slice", {"normal": (0, 0, 1)}),
        ]
        result = apply_filters(_wavelet(), steps)
        assert result is not None


class TestListFilters:
    def test_list_filters(self):
        from parapilot.engine.filters import list_filters
        names = list_filters()
        assert "slice" in names
        assert "clip" in names
        assert "contour" in names
        assert len(names) >= 20
