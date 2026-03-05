"""preview_3d tool — export dataset to glTF for interactive 3D viewing."""

from __future__ import annotations

import asyncio
import os
from typing import Any

from parapilot.core.runner import VTKRunner
from parapilot.engine.export import export_gltf
from parapilot.engine.readers import get_timesteps, read_dataset


async def preview_3d_impl(
    file_path: str,
    runner: VTKRunner,
    *,
    field_name: str | None = None,
    timestep: float | str | None = None,
    binary: bool = True,
    output_filename: str = "preview.glb",
) -> dict[str, Any]:
    """Export a dataset to glTF/glB for interactive 3D viewing.

    Returns dict with path, format, size_bytes, and viewer_url.
    """

    def _run() -> dict[str, Any]:
        # Resolve timestep
        ts = timestep
        if ts == "latest":
            steps = get_timesteps(file_path)
            ts = steps[-1] if steps else None
        elif isinstance(ts, str):
            ts = float(ts)

        data = read_dataset(file_path, timestep=ts)

        output_dir = os.environ.get("PARAPILOT_OUTPUT_DIR", "/tmp")
        out_path = os.path.join(output_dir, output_filename)

        result = export_gltf(data, out_path, binary=binary)
        result["viewer_hint"] = (
            "Open the exported file in the parapilot 3D viewer: "
            "https://kimimgo.github.io/parapilot/viewer.html?file=<path_to_glb>"
        )
        return result

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _run)
