"""Integration tests for engine/export.py — real VTK execution."""

from __future__ import annotations

import pytest

vtk = pytest.importorskip("vtk")


def _wavelet() -> vtk.vtkImageData:
    src = vtk.vtkRTAnalyticSource()
    src.SetWholeExtent(-5, 5, -5, 5, -5, 5)
    src.Update()
    return src.GetOutput()


def _sphere() -> vtk.vtkPolyData:
    src = vtk.vtkSphereSource()
    src.SetRadius(1.0)
    src.Update()
    return src.GetOutput()


def _multiblock() -> vtk.vtkMultiBlockDataSet:
    mb = vtk.vtkMultiBlockDataSet()
    mb.SetBlock(0, _wavelet())
    mb.GetMetaData(0).Set(vtk.vtkCompositeDataSet.NAME(), "wavelet")
    mb.SetBlock(1, _sphere())
    mb.GetMetaData(1).Set(vtk.vtkCompositeDataSet.NAME(), "sphere")
    return mb


# ---------------------------------------------------------------------------
# inspect_dataset
# ---------------------------------------------------------------------------

class TestInspectDataset:
    def test_inspect_imagedata(self):
        from parapilot.engine.export import inspect_dataset
        info = inspect_dataset(_wavelet())
        assert "ImageData" in info["type"]
        assert info["num_points"] > 0
        assert info["num_cells"] > 0
        assert len(info["bounds"]) == 6
        assert len(info["point_arrays"]) > 0
        assert info["point_arrays"][0]["name"] == "RTData"

    def test_inspect_polydata(self):
        from parapilot.engine.export import inspect_dataset
        info = inspect_dataset(_sphere())
        assert "PolyData" in info["type"]
        assert info["num_points"] > 0

    def test_inspect_multiblock(self):
        from parapilot.engine.export import inspect_dataset
        info = inspect_dataset(_multiblock())
        assert info["multiblock"] is not None
        assert len(info["multiblock"]) == 2
        assert info["multiblock"][0]["name"] == "wavelet"
        assert info["multiblock"][1]["name"] == "sphere"

    def test_inspect_multiblock_nested(self):
        from parapilot.engine.export import inspect_dataset
        outer = vtk.vtkMultiBlockDataSet()
        inner = vtk.vtkMultiBlockDataSet()
        inner.SetBlock(0, _wavelet())
        outer.SetBlock(0, inner)
        info = inspect_dataset(outer)
        assert info["multiblock"][0].get("children") is not None

    def test_inspect_multiblock_with_none_block(self):
        from parapilot.engine.export import inspect_dataset
        mb = vtk.vtkMultiBlockDataSet()
        mb.SetBlock(0, None)
        mb.SetBlock(1, _wavelet())
        info = inspect_dataset(mb)
        assert info["multiblock"][0]["num_points"] == 0
        assert info["multiblock"][0]["type"] == "None"


# ---------------------------------------------------------------------------
# extract_stats
# ---------------------------------------------------------------------------

class TestExtractStats:
    def test_stats_scalar(self):
        from parapilot.engine.export import extract_stats
        stats = extract_stats(_wavelet(), fields=["RTData"])
        assert "RTData" in stats
        s = stats["RTData"]
        assert s["min"] < s["max"]
        assert s["association"] == "point"
        assert s["components"] == 1

    def test_stats_all_fields(self):
        from parapilot.engine.export import extract_stats
        stats = extract_stats(_wavelet())
        assert "RTData" in stats

    def test_stats_vector(self):
        """Test vector field stats with per-component + magnitude."""
        from parapilot.engine.export import extract_stats
        # Create dataset with vector field
        data = _wavelet()
        calc = vtk.vtkArrayCalculator()
        calc.SetInputData(data)
        calc.AddScalarArrayName("RTData")
        calc.SetResultArrayName("velocity")
        calc.SetFunction("RTData*iHat + RTData*0.5*jHat + 0*kHat")
        calc.SetResultArrayType(vtk.VTK_DOUBLE)
        calc.Update()

        stats = extract_stats(calc.GetOutput(), fields=["velocity"])
        assert "velocity" in stats
        s = stats["velocity"]
        assert s["components"] == 3
        assert isinstance(s["min"], list)
        assert "magnitude" in s

    def test_stats_multiblock(self):
        from parapilot.engine.export import extract_stats
        stats = extract_stats(_multiblock())
        # Should extract from first leaf block
        assert "RTData" in stats

    def test_stats_nonexistent_field(self):
        from parapilot.engine.export import extract_stats
        stats = extract_stats(_wavelet(), fields=["nonexistent"])
        assert "nonexistent" not in stats


# ---------------------------------------------------------------------------
# extract_data
# ---------------------------------------------------------------------------

class TestExtractData:
    def test_extract_basic(self):
        from parapilot.engine.export import extract_data
        data = extract_data(_wavelet(), fields=["RTData"])
        assert "RTData" in data
        assert isinstance(data["RTData"], list)
        assert len(data["RTData"]) > 0

    def test_extract_with_coords(self):
        from parapilot.engine.export import extract_data
        data = extract_data(_wavelet(), fields=["RTData"], include_coords=True)
        assert "x" in data
        assert "y" in data
        assert "z" in data
        assert len(data["x"]) == len(data["RTData"])

    def test_extract_all_fields(self):
        from parapilot.engine.export import extract_data
        data = extract_data(_wavelet())
        assert "RTData" in data

    def test_extract_multiblock(self):
        from parapilot.engine.export import extract_data
        data = extract_data(_multiblock())
        assert "RTData" in data


# ---------------------------------------------------------------------------
# export_file
# ---------------------------------------------------------------------------

class TestExportFile:
    def test_export_vtu(self, tmp_path):
        from parapilot.engine.export import export_file
        out = tmp_path / "test.vtu"
        # Need unstructured grid
        conv = vtk.vtkDataSetTriangleFilter()
        conv.SetInputData(_wavelet())
        conv.Update()
        result = export_file(conv.GetOutput(), out)
        assert result["format"] == ".vtu"
        assert result["size_bytes"] > 0
        assert out.exists()

    def test_export_vtp(self, tmp_path):
        from parapilot.engine.export import export_file
        out = tmp_path / "test.vtp"
        result = export_file(_sphere(), out)
        assert result["format"] == ".vtp"
        assert out.exists()

    def test_export_stl(self, tmp_path):
        from parapilot.engine.export import export_file
        out = tmp_path / "test.stl"
        result = export_file(_sphere(), out)
        assert result["format"] == ".stl"
        assert out.exists()

    def test_export_csv(self, tmp_path):
        from parapilot.engine.export import export_file
        out = tmp_path / "test.csv"
        result = export_file(_wavelet(), out)
        assert result["format"] == ".csv"
        assert out.exists()
        content = out.read_text()
        assert "RTData" in content

    def test_export_unsupported_format(self, tmp_path):
        from parapilot.engine.export import export_file
        with pytest.raises(ValueError, match="Unsupported export format"):
            export_file(_wavelet(), tmp_path / "test.xyz")

    def test_export_vtk_generic(self, tmp_path):
        from parapilot.engine.export import export_file
        out = tmp_path / "test.vtk"
        result = export_file(_wavelet(), out)
        assert result["format"] == ".vtk"
        assert out.exists()

    def test_export_stl_auto_convert(self, tmp_path):
        """STL export auto-converts non-polydata to polydata."""
        from parapilot.engine.export import export_file
        out = tmp_path / "converted.stl"
        result = export_file(_wavelet(), out)
        assert result["format"] == ".stl"
        assert out.exists()


# ---------------------------------------------------------------------------
# get_leaf_block
# ---------------------------------------------------------------------------

class TestGetLeafBlock:
    def test_leaf_from_multiblock(self):
        from parapilot.engine.export import get_leaf_block
        leaf = get_leaf_block(_multiblock())
        assert leaf is not None
        assert leaf.GetNumberOfPoints() > 0

    def test_leaf_from_dataset(self):
        from parapilot.engine.export import get_leaf_block
        leaf = get_leaf_block(_wavelet())
        assert leaf is _wavelet() or leaf is not None

    def test_leaf_empty_multiblock(self):
        from parapilot.engine.export import get_leaf_block
        mb = vtk.vtkMultiBlockDataSet()
        leaf = get_leaf_block(mb)
        assert leaf is None
