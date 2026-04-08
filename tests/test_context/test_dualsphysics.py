"""Tests for DualSPHysics context parser."""

from __future__ import annotations


def _make_vtk_polydata_with_sph_fields():
    """Create a minimal vtkPolyData dataset with DualSPHysics-typical point fields."""
    import vtkmodules.vtkCommonCore as vtk_core  # noqa: N813
    import vtkmodules.vtkCommonDataModel as vtk_dm  # noqa: N813

    pd = vtk_dm.vtkPolyData()

    # 4 particles in a 2D plane
    points = vtk_core.vtkPoints()
    coords = [(0.0, 0.0, 0.0), (0.1, 0.0, 0.0), (0.0, 0.1, 0.0), (0.1, 0.1, 0.0)]
    for c in coords:
        points.InsertNextPoint(*c)
    pd.SetPoints(points)

    n = len(coords)

    # Idp — particle ID (unsigned int array)
    idp = vtk_core.vtkUnsignedIntArray()
    idp.SetName("Idp")
    idp.SetNumberOfTuples(n)
    for i in range(n):
        idp.SetValue(i, i)
    pd.GetPointData().AddArray(idp)

    # Vel — velocity (3-component float array)
    vel = vtk_core.vtkFloatArray()
    vel.SetName("Vel")
    vel.SetNumberOfComponents(3)
    vel.SetNumberOfTuples(n)
    for i in range(n):
        vel.SetTuple3(i, float(i), 0.0, 0.0)
    pd.GetPointData().AddArray(vel)

    # Rhop — density (float)
    rhop = vtk_core.vtkFloatArray()
    rhop.SetName("Rhop")
    rhop.SetNumberOfTuples(n)
    for i in range(n):
        rhop.SetValue(i, 1000.0)
    pd.GetPointData().AddArray(rhop)

    # Press — pressure (float)
    press = vtk_core.vtkFloatArray()
    press.SetName("Press")
    press.SetNumberOfTuples(n)
    for i in range(n):
        press.SetValue(i, 101325.0)
    pd.GetPointData().AddArray(press)

    return pd


def _make_vtk_polydata_no_sph_fields():
    """Create a vtkPolyData with generic fields (no DualSPHysics-specific names)."""
    import vtkmodules.vtkCommonCore as vtk_core  # noqa: N813
    import vtkmodules.vtkCommonDataModel as vtk_dm  # noqa: N813

    pd = vtk_dm.vtkPolyData()
    points = vtk_core.vtkPoints()
    points.InsertNextPoint(0.0, 0.0, 0.0)
    points.InsertNextPoint(1.0, 0.0, 0.0)
    pd.SetPoints(points)
    return pd


class TestDualSPHysicsContextParserCanParse:
    """Tests for DualSPHysicsContextParser.can_parse()."""

    def test_xml_def_file_returns_true(self, tmp_path):
        """A *_Def.xml file should be recognized as a DualSPHysics case."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        xml = tmp_path / "CasePistons_Def.xml"
        xml.write_text("<casedef><execution/></casedef>")
        parser = DualSPHysicsContextParser()
        assert parser.can_parse(str(xml)) is True

    def test_generic_xml_with_casedef_tag_returns_true(self, tmp_path):
        """A plain .xml file containing <casedef> root element matches."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        xml = tmp_path / "sim.xml"
        xml.write_text("<casedef><geometry/></casedef>")
        parser = DualSPHysicsContextParser()
        assert parser.can_parse(str(xml)) is True

    def test_vtk_file_with_def_xml_in_parent_returns_true(self, tmp_path):
        """A .vtk file whose parent dir contains a *_Def.xml should match."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        (tmp_path / "CaseDam_Def.xml").write_text("<casedef/>")
        vtk_file = tmp_path / "Part_0000.vtk"
        vtk_file.write_text("")
        parser = DualSPHysicsContextParser()
        assert parser.can_parse(str(vtk_file)) is True

    def test_vtp_file_with_def_xml_in_parent_returns_true(self, tmp_path):
        """A .vtp file whose parent dir contains a *_Def.xml should match."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        (tmp_path / "Case_Def.xml").write_text("<casedef/>")
        vtp_file = tmp_path / "Part_0000.vtp"
        vtp_file.write_text("")
        parser = DualSPHysicsContextParser()
        assert parser.can_parse(str(vtp_file)) is True

    def test_vtp_file_with_casedef_xml_in_parent_returns_true(self, tmp_path):
        """A .vtp alongside a plain .xml with <casedef> should match."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        xml = tmp_path / "params.xml"
        xml.write_text("<casedef><execution/></casedef>")
        vtp_file = tmp_path / "particles.vtp"
        vtp_file.write_text("")
        parser = DualSPHysicsContextParser()
        assert parser.can_parse(str(vtp_file)) is True

    def test_vtk_file_without_xml_in_parent_returns_false(self, tmp_path):
        """A .vtk file with no XML in the parent directory should not match."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        vtk_file = tmp_path / "Part_0000.vtk"
        vtk_file.write_text("")
        parser = DualSPHysicsContextParser()
        assert parser.can_parse(str(vtk_file)) is False

    def test_cgns_file_returns_false(self, tmp_path):
        """CGNS files should not match the DualSPHysics parser."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        f = tmp_path / "mesh.cgns"
        f.write_text("")
        parser = DualSPHysicsContextParser()
        assert parser.can_parse(str(f)) is False

    def test_xml_without_casedef_tag_returns_false(self, tmp_path):
        """A plain XML without <casedef> root should not match."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        xml = tmp_path / "config.xml"
        xml.write_text("<configuration><setting/></configuration>")
        parser = DualSPHysicsContextParser()
        assert parser.can_parse(str(xml)) is False

    def test_empty_string_returns_false(self):
        """Empty path should not raise and should return False."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        assert parser.can_parse("") is False

    def test_non_existent_path_returns_false(self):
        """Non-existent path should return False without raising."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        assert parser.can_parse("/no/such/path/file.vtk") is False

    def test_vtu_extension_with_def_xml_returns_false(self, tmp_path):
        """Only .vtk and .vtp extensions should be recognized (not .vtu)."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        (tmp_path / "Case_Def.xml").write_text("<casedef/>")
        vtu_file = tmp_path / "mesh.vtu"
        vtu_file.write_text("")
        parser = DualSPHysicsContextParser()
        assert parser.can_parse(str(vtu_file)) is False


class TestDualSPHysicsContextParserParseDataset:
    """Tests for DualSPHysicsContextParser.parse_dataset() with mock VTK datasets."""

    def test_parse_returns_case_context(self):
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        assert ctx is not None

    def test_parse_mesh_quality_not_none(self):
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        assert ctx.mesh_quality is not None

    def test_parse_point_count_matches_dataset(self):
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        assert ctx.mesh_quality.point_count == ds.GetNumberOfPoints()

    def test_parse_particle_count_equals_point_count(self):
        """For SPH data, particles == points."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        assert ctx.mesh_quality.point_count == 4

    def test_parse_bounding_box_has_correct_structure(self):
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        bb = ctx.mesh_quality.bounding_box
        assert len(bb) == 2
        assert len(bb[0]) == 3
        assert len(bb[1]) == 3

    def test_parse_solver_name_is_dualsphysics(self):
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        assert ctx.solver is not None
        assert ctx.solver.name == "DualSPHysics"

    def test_parse_solver_algorithm_is_sph(self):
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        assert ctx.solver is not None
        assert ctx.solver.algorithm == "SPH"

    def test_parse_detects_idp_field(self):
        """Idp field should be detected and reported in boundary_conditions."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        field_names = {bc.field for bc in ctx.boundary_conditions}
        assert "Idp" in field_names

    def test_parse_detects_vel_field(self):
        """Vel field should be detected and reported in boundary_conditions."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        field_names = {bc.field for bc in ctx.boundary_conditions}
        assert "Vel" in field_names

    def test_parse_detects_rhop_field(self):
        """Rhop field should be detected and reported in boundary_conditions."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        field_names = {bc.field for bc in ctx.boundary_conditions}
        assert "Rhop" in field_names

    def test_parse_detects_press_field(self):
        """Press field should be detected and reported in boundary_conditions."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        field_names = {bc.field for bc in ctx.boundary_conditions}
        assert "Press" in field_names

    def test_parse_no_sph_fields_returns_empty_bc_list(self):
        """Dataset without SPH-specific fields should return empty boundary_conditions."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_no_sph_fields()
        ctx = parser.parse_dataset(ds)
        assert ctx.boundary_conditions == []

    def test_parse_no_transport_properties(self):
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        assert ctx.transport_properties == []

    def test_parse_no_derived_quantities(self):
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        assert ctx.derived_quantities == []

    def test_parse_bounding_box_xmax_gt_xmin(self):
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        bb = ctx.mesh_quality.bounding_box
        assert bb[1][0] > bb[0][0]  # xmax > xmin

    def test_parse_cell_count_uses_point_based_convention(self):
        """SPH datasets are point-based; cell_count should reflect this (0 or == point_count)."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds)
        # cell_count in SPH context is particle count (point_count), cells may be 0
        assert ctx.mesh_quality.cell_count >= 0


class TestDualSPHysicsXMLParsing:
    """Tests for XML case file parameter extraction."""

    def test_parse_with_xml_extracts_transport_properties(self, tmp_path):
        """When an XML with dp/gravity is available alongside the VTK file, extract them."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        xml_content = """<casedef>
  <constantsdef>
    <lattice bound="1" fluid="1"/>
    <gravity x="0" y="0" z="-9.81"/>
    <cflnumber value="0.2"/>
    <dp value="0.01"/>
  </constantsdef>
</casedef>"""
        xml = tmp_path / "CaseDam_Def.xml"
        xml.write_text(xml_content)

        vtp_file = tmp_path / "Part_0000.vtp"
        vtp_file.write_text("")

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        # Set xml_path so the parser knows where to look
        ctx = parser.parse_dataset(ds, xml_path=str(xml))
        assert len(ctx.transport_properties) > 0

    def test_parse_xml_extracts_dp(self, tmp_path):
        """dp (particle spacing) should be extracted as a transport property."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        xml = tmp_path / "Case_Def.xml"
        xml.write_text('<casedef><constantsdef><dp value="0.005"/></constantsdef></casedef>')
        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds, xml_path=str(xml))
        names = {tp.name for tp in ctx.transport_properties}
        assert "dp" in names

    def test_parse_xml_dp_value_correct(self, tmp_path):
        """dp value should be parsed correctly."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        xml = tmp_path / "Case_Def.xml"
        xml.write_text('<casedef><constantsdef><dp value="0.005"/></constantsdef></casedef>')
        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds, xml_path=str(xml))
        dp_props = [tp for tp in ctx.transport_properties if tp.name == "dp"]
        assert len(dp_props) == 1
        assert abs(dp_props[0].value - 0.005) < 1e-9

    def test_parse_xml_extracts_gravity(self, tmp_path):
        """gravity magnitude should be extracted as a transport property."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        xml = tmp_path / "Case_Def.xml"
        xml.write_text('<casedef><constantsdef><gravity x="0" y="0" z="-9.81"/></constantsdef></casedef>')
        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds, xml_path=str(xml))
        names = {tp.name for tp in ctx.transport_properties}
        assert "gravity" in names

    def test_parse_xml_gravity_value_correct(self, tmp_path):
        """gravity magnitude should be approximately 9.81."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        xml = tmp_path / "Case_Def.xml"
        xml.write_text('<casedef><constantsdef><gravity x="0" y="0" z="-9.81"/></constantsdef></casedef>')
        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds, xml_path=str(xml))
        g_props = [tp for tp in ctx.transport_properties if tp.name == "gravity"]
        assert len(g_props) == 1
        assert abs(g_props[0].value - 9.81) < 1e-6

    def test_parse_xml_missing_element_does_not_raise(self, tmp_path):
        """XML without dp or gravity should not raise — just skip."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        xml = tmp_path / "Case_Def.xml"
        xml.write_text("<casedef><geometry/></casedef>")
        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds, xml_path=str(xml))
        assert ctx is not None

    def test_parse_xml_nonexistent_path_does_not_raise(self):
        """Providing a non-existent xml_path should silently fall back."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser

        parser = DualSPHysicsContextParser()
        ds = _make_vtk_polydata_with_sph_fields()
        ctx = parser.parse_dataset(ds, xml_path="/no/such/file.xml")
        assert ctx is not None
        assert ctx.transport_properties == []


class TestDualSPHysicsRegistryIntegration:
    """Tests for DualSPHysics parser registration in the default registry."""

    def test_dualsphysics_registered(self, tmp_path):
        """DualSPHysics parser should be found for a *_Def.xml file."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser
        from viznoir.context.parser import get_default_registry

        xml = tmp_path / "CaseDam_Def.xml"
        xml.write_text("<casedef/>")
        registry = get_default_registry()
        parser = registry.get_parser(str(xml))
        assert isinstance(parser, DualSPHysicsContextParser)

    def test_dualsphysics_precedes_generic(self, tmp_path):
        """DualSPHysics parser should win over GenericContextParser for matching paths."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser
        from viznoir.context.parser import get_default_registry

        (tmp_path / "Case_Def.xml").write_text("<casedef/>")
        vtp_file = tmp_path / "Part_0000.vtp"
        vtp_file.write_text("")
        registry = get_default_registry()
        parser = registry.get_parser(str(vtp_file))
        assert isinstance(parser, DualSPHysicsContextParser)

    def test_openfoam_still_takes_priority(self, tmp_path):
        """OpenFOAM cases should not be matched by DualSPHysics parser."""
        from viznoir.context.openfoam import OpenFOAMContextParser
        from viznoir.context.parser import get_default_registry

        (tmp_path / "system").mkdir()
        (tmp_path / "system" / "controlDict").write_text("application icoFoam;")
        registry = get_default_registry()
        parser = registry.get_parser(str(tmp_path))
        assert isinstance(parser, OpenFOAMContextParser)

    def test_cgns_still_takes_priority_over_dualsphysics(self, tmp_path):
        """CGNS files should be matched by CGNSContextParser, not DualSPHysics."""
        from viznoir.context.cgns import CGNSContextParser
        from viznoir.context.parser import get_default_registry

        f = tmp_path / "mesh.cgns"
        f.write_text("")
        registry = get_default_registry()
        parser = registry.get_parser(str(f))
        assert isinstance(parser, CGNSContextParser)

    def test_non_sph_vtk_falls_to_generic(self, tmp_path):
        """A .vtp file without DualSPHysics XML context should fall back to Generic."""
        from viznoir.context.dualsphysics import DualSPHysicsContextParser
        from viznoir.context.parser import get_default_registry

        vtp_file = tmp_path / "mesh.vtp"
        vtp_file.write_text("")
        registry = get_default_registry()
        parser = registry.get_parser(str(vtp_file))
        assert not isinstance(parser, DualSPHysicsContextParser)
