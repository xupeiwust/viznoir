"""DualSPHysics context parser — extracts SPH simulation metadata from VTK particle datasets."""

from __future__ import annotations

import math
from pathlib import Path

from viznoir.context.models import BoundaryCondition, CaseContext, MeshQuality, SolverInfo, TransportProperty

# DualSPHysics-specific point field names
_SPH_FIELDS = ("Idp", "Vel", "Rhop", "Press")


class DualSPHysicsContextParser:
    """Parser for DualSPHysics output VTK/VTP files and XML case definition files."""

    def can_parse(self, path: str) -> bool:
        """Return True if the path is a DualSPHysics case file or associated VTK output.

        Matching rules (checked in order):
        1. Path is a *_Def.xml file (DualSPHysics case definition).
        2. Path is any .xml file whose root element is <casedef>.
        3. Path is a .vtk or .vtp file and the parent directory contains
           a *_Def.xml or any .xml file with a <casedef> root element.
        """
        if not path:
            return False

        p = Path(path)

        # Rule 1 & 2: XML files
        if p.suffix == ".xml":
            return _is_dualsphysics_xml(p)

        # Rule 3: VTK particle files
        if p.suffix in (".vtk", ".vtp"):
            return _parent_has_dualsphysics_xml(p.parent)

        return False

    def parse_dataset(self, dataset: object, xml_path: str | None = None) -> CaseContext:
        """Extract CaseContext from a VTK dataset.

        Parameters
        ----------
        dataset:
            A VTK dataset (typically vtkPolyData for SPH particle data).
        xml_path:
            Optional path to the DualSPHysics XML case definition file.
            If provided and the file exists, simulation parameters (dp, gravity)
            are extracted as transport properties.
        """
        point_count: int = dataset.GetNumberOfPoints()  # type: ignore[attr-defined]
        cell_count: int = dataset.GetNumberOfCells()  # type: ignore[attr-defined]

        bounds = list(dataset.GetBounds())  # type: ignore[attr-defined]
        bb = [[bounds[0], bounds[2], bounds[4]], [bounds[1], bounds[3], bounds[5]]]

        mq = MeshQuality(
            cell_count=cell_count,
            point_count=point_count,
            cell_types={},
            bounding_box=bb,
        )

        solver = SolverInfo(name="DualSPHysics", algorithm="SPH", steady=False)

        # Detect SPH-specific fields in point data
        bcs = _detect_sph_fields(dataset)

        # Parse XML case definition if available
        transport: list[TransportProperty] = []
        if xml_path is not None:
            transport = _parse_xml_params(xml_path)

        return CaseContext(
            mesh_quality=mq,
            boundary_conditions=bcs,
            transport_properties=transport,
            solver=solver,
        )


# ------------------------------------------------------------------
# Module-level helpers
# ------------------------------------------------------------------


def _is_dualsphysics_xml(path: Path) -> bool:
    """Return True if the XML file is a DualSPHysics case definition.

    Checks for *_Def.xml naming convention first, then inspects the
    root element for <casedef> regardless of file name.
    """
    if not path.is_file():
        return False

    # Fast check: DualSPHysics naming convention
    if path.stem.endswith("_Def"):
        return True

    # Fallback: inspect root element
    return _xml_has_casedef_root(path)


def _xml_has_casedef_root(path: Path) -> bool:
    """Return True if the XML file's root element is <casedef>."""
    try:
        import xml.etree.ElementTree as ET  # noqa: N814

        tree = ET.parse(str(path))
        root = tree.getroot()
        return root.tag == "casedef"
    except Exception:  # noqa: BLE001
        return False


def _parent_has_dualsphysics_xml(directory: Path) -> bool:
    """Return True if the directory contains at least one DualSPHysics XML file."""
    if not directory.is_dir():
        return False

    for xml_file in directory.glob("*.xml"):
        if _is_dualsphysics_xml(xml_file):
            return True
    return False


def _detect_sph_fields(dataset: object) -> list[BoundaryCondition]:
    """Scan point data arrays for known DualSPHysics field names."""
    bcs: list[BoundaryCondition] = []
    try:
        pd = dataset.GetPointData()  # type: ignore[attr-defined]
        n_arrays: int = pd.GetNumberOfArrays()
        for i in range(n_arrays):
            name: str = pd.GetArrayName(i)
            if name in _SPH_FIELDS:
                bcs.append(BoundaryCondition(patch_name="particles", field=name, type="sph_field"))
    except Exception:  # noqa: BLE001
        pass
    return bcs


def _parse_xml_params(xml_path: str) -> list[TransportProperty]:
    """Extract dp and gravity from a DualSPHysics XML case definition file."""
    transport: list[TransportProperty] = []
    p = Path(xml_path)
    if not p.is_file():
        return transport

    try:
        import xml.etree.ElementTree as ET  # noqa: N814

        tree = ET.parse(str(p))
        root = tree.getroot()

        constants = root.find(".//constantsdef")
        if constants is None:
            return transport

        # dp — particle spacing
        dp_elem = constants.find("dp")
        if dp_elem is not None:
            dp_val = dp_elem.get("value")
            if dp_val is not None:
                transport.append(TransportProperty(name="dp", value=float(dp_val), unit="m"))

        # gravity — vector magnitude
        g_elem = constants.find("gravity")
        if g_elem is not None:
            gx = float(g_elem.get("x", "0"))
            gy = float(g_elem.get("y", "0"))
            gz = float(g_elem.get("z", "0"))
            g_mag = math.sqrt(gx**2 + gy**2 + gz**2)
            transport.append(TransportProperty(name="gravity", value=g_mag, unit="m/s^2"))

    except Exception:  # noqa: BLE001
        pass

    return transport
