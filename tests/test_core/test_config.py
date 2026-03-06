"""Tests for parapilot.config — PVConfig and helper functions."""

from __future__ import annotations

from unittest.mock import patch


class TestPVConfig:
    def test_default_config(self):
        from parapilot.config import PVConfig
        config = PVConfig()
        assert config.default_resolution == (1920, 1080)
        assert config.default_timeout == 600.0

    def test_data_dir_from_env(self, monkeypatch):
        from importlib import reload

        import parapilot.config
        monkeypatch.setenv("PARAPILOT_DATA_DIR", "/test/data")
        reload(parapilot.config)
        config = parapilot.config.PVConfig()
        assert str(config.data_dir) == "/test/data"

    def test_data_dir_none_when_unset(self, monkeypatch):
        from importlib import reload

        import parapilot.config
        monkeypatch.delenv("PARAPILOT_DATA_DIR", raising=False)
        reload(parapilot.config)
        config = parapilot.config.PVConfig()
        assert config.data_dir is None

    def test_use_gpu_true_for_gpu_backend(self):
        from parapilot.config import PVConfig
        config = PVConfig(render_backend="gpu")
        assert config.use_gpu is True

    def test_use_gpu_false_for_cpu_backend(self):
        from parapilot.config import PVConfig
        config = PVConfig(render_backend="cpu")
        assert config.use_gpu is False

    def test_use_gpu_auto_with_gpu_available(self):
        from parapilot.config import PVConfig
        config = PVConfig(render_backend="auto")
        with patch("parapilot.config._gpu_available", return_value=True):
            assert config.use_gpu is True

    def test_use_gpu_auto_without_gpu(self):
        from parapilot.config import PVConfig
        config = PVConfig(render_backend="auto")
        with patch("parapilot.config._gpu_available", return_value=False):
            assert config.use_gpu is False


class TestParseRenderBackend:
    def test_valid_values(self):
        from parapilot.config import _parse_render_backend
        assert _parse_render_backend("gpu") == "gpu"
        assert _parse_render_backend("cpu") == "cpu"
        assert _parse_render_backend("auto") == "auto"

    def test_case_insensitive(self):
        from parapilot.config import _parse_render_backend
        assert _parse_render_backend("GPU") == "gpu"
        assert _parse_render_backend("  Auto  ") == "auto"

    def test_invalid_falls_back_to_gpu(self):
        from parapilot.config import _parse_render_backend
        assert _parse_render_backend("invalid") == "gpu"


class TestParseVtkBackend:
    def test_valid_values(self):
        from parapilot.config import _parse_vtk_backend
        assert _parse_vtk_backend("egl") == "egl"
        assert _parse_vtk_backend("osmesa") == "osmesa"
        assert _parse_vtk_backend("auto") == "auto"

    def test_invalid_falls_back_to_auto(self):
        from parapilot.config import _parse_vtk_backend
        assert _parse_vtk_backend("invalid") == "auto"


class TestGpuAvailable:
    def test_gpu_available_with_nvidia_smi(self):
        from parapilot.config import _gpu_available
        with patch("shutil.which", return_value="/usr/bin/nvidia-smi"):
            assert _gpu_available() is True

    def test_gpu_unavailable(self):
        from parapilot.config import _gpu_available
        with patch("shutil.which", return_value=None):
            assert _gpu_available() is False
