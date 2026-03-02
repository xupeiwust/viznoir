"""Tests for server-level input validation."""

from __future__ import annotations

import os

import pytest


class TestValidateFilePath:
    """Test _validate_file_path path traversal prevention."""

    def _reload_with_data_dir(self, data_dir: str | None = "/data"):
        """Reload server module with PARAPILOT_DATA_DIR set."""
        import importlib

        import parapilot.config
        import parapilot.server

        if data_dir is not None:
            os.environ["PARAPILOT_DATA_DIR"] = data_dir
        else:
            os.environ.pop("PARAPILOT_DATA_DIR", None)

        importlib.reload(parapilot.config)
        importlib.reload(parapilot.server)
        return parapilot.server._validate_file_path

    def test_valid_path_within_data_dir(self):
        validate = self._reload_with_data_dir("/data")
        result = validate("/data/cavity.vtk")
        assert result == "/data/cavity.vtk"

    def test_valid_nested_path(self):
        validate = self._reload_with_data_dir("/data")
        result = validate("/data/cases/foam/cavity.foam")
        assert result == "/data/cases/foam/cavity.foam"

    def test_rejects_path_traversal(self):
        validate = self._reload_with_data_dir("/data")
        with pytest.raises(ValueError, match="Access denied"):
            validate("/etc/shadow")

    def test_rejects_dotdot_traversal(self):
        validate = self._reload_with_data_dir("/data")
        with pytest.raises(ValueError, match="Access denied"):
            validate("/data/../etc/passwd")

    def test_rejects_absolute_outside(self):
        validate = self._reload_with_data_dir("/data")
        with pytest.raises(ValueError, match="Access denied"):
            validate("/home/user/.ssh/id_rsa")

    def test_data_dir_itself_is_allowed(self):
        validate = self._reload_with_data_dir("/data")
        result = validate("/data")
        assert result == "/data"

    def test_no_data_dir_allows_any_path(self):
        """When PARAPILOT_DATA_DIR is unset, any path is allowed."""
        validate = self._reload_with_data_dir(None)
        result = validate("/tmp/test.vtk")
        assert result == "/tmp/test.vtk"

    def test_no_data_dir_allows_absolute_paths(self):
        """When PARAPILOT_DATA_DIR is unset, absolute paths work."""
        validate = self._reload_with_data_dir(None)
        result = validate("/home/user/sim/case.foam")
        assert result == "/home/user/sim/case.foam"
