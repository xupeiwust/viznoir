# Global Showcase Gallery

> Country-specific visualization examples demonstrating viznoir's capabilities across CAE/CFD/FEA domains worldwide.

## Overview

viznoir supports 50+ file formats and renders cinema-quality visualizations across all major CAE domains. This gallery maps real-world datasets to the countries and research institutions where each domain expertise originated.

---

## 🇺🇸 United States — CFD, Medical Imaging, 3D Scanning

**Strengths**: Sandia National Lab (VTK origin), Kitware (VTK/ParaView maintainer), Stanford 3D Scanning, NIH medical imaging

### Medical CT — Skull Volume Rendering

```
> Render the skull CT dataset with bone transfer function
```

```python
# viznoir MCP tool call
volume_render(
    file_path="skull.vti",
    transfer_preset="ct_bone",
    colormap="bone",
    quality="cinematic"
)
```

**Existing showcase**: `ct_volume.png`, `ct_head_contour.png`, `ct_head_slice.png`, `ct_multiview.png`, `ct_skull_orbit.gif`

### Combustion Jet — Temperature Slice & Streamlines

```
> Slice the combustion jet at the centerplane and show temperature
```

```python
slice(
    file_path="combustion_jet.vts",
    field_name="Temperature",
    origin=[15.75, 0, 0],
    normal=[0, 1, 0],
    colormap="Inferno (matplotlib)"
)

streamlines(
    file_path="combustion_jet.vts",
    vector_field="Velocity",
    seed_point1=[0, -3, -3],
    seed_point2=[0, 3, 3],
    seed_resolution=40,
    max_length=30
)
```

**Fields**: Temperature (300–1800 K), Velocity (0–13 m/s), CH4_Concentration (0–1)

**Physics analysis** (`inspect_physics`):
- **8 vortices detected** in velocity field — counter-clockwise at x=3.96 (strength 4.0), clockwise at x=23.5 (strength 3.9)
- Temperature gradient: dominant direction along jet axis (-x), max gradient 1030 K/unit
- CH4 concentration: linear decay along jet (1.0 at inlet → 0.015 at exit)
- Centerline peak temperature: 817 K at jet center (x=15.75)

**Multi-tool workflow**:
1. `inspect_physics` — Detect vortices, stagnation points, centerline profiles
2. `slice` — Temperature cross-section at Y=0 symmetry plane
3. `streamlines` — Velocity field from seed plane at jet inlet
4. `contour` — CH4 isosurfaces [0.1, 0.3, 0.5, 0.7, 0.9] for flame front visualization
5. `plot_over_line` — Centerline temperature profile (inlet to exit)
6. `extract_stats` — Field statistics for all 3 variables

**Existing showcase**: `02_combustion_annotated.webp`, `10_combustion_annotated.webp`

### Stanford 3D — Bunny & Armadillo

```python
cinematic_render(
    file_path="bunny.ply",
    quality="cinematic",
    lighting="studio",
    ground_plane=True
)
```

**Existing showcase**: `bunny.png`, `armadillo_clip.png`

---

## 🇩🇪 Germany — FEM/Structural, Turbomachinery

**Strengths**: Siemens (NX/Star-CCM+), CalculiX (open-source FEA), DLR aerospace, Fraunhofer institutes

### Cantilever Beam — Von Mises Stress

```python
cinematic_render(
    file_path="cantilever_beam_stress.vts",
    field_name="VonMisesStress",
    colormap="Plasma (matplotlib)",
    quality="cinematic",
    lighting="studio",
    ground_plane=True
)
```

**Existing showcase**: `beam-stress.png`, `beam-stress-pub.png`, `09_cantilever_annotated.webp`

### Turbine Ring — Metallic PBR Rendering

```python
cinematic_render(
    file_path="turbine_stress.vtp",
    quality="cinematic",
    lighting="cinematic",
    metallic=0.7,
    roughness=0.2,
    ground_plane=True
)
```

**Result**: Stunning metallic torus with specular highlights — demonstrates PBR material system.

### LPBF Additive Manufacturing — Laser Thermal

```python
cinematic_render(
    file_path="additive_manufacturing_lpbf.vti",
    field_name="Temperature",
    colormap="Inferno (matplotlib)",
    quality="cinematic",
    lighting="dramatic"
)
```

**Fields**: Temperature (300–3500 K), laser focal point visible

---

## 🇨🇳 China — Automotive Aerodynamics

**Strengths**: BYD/NIO EV development, CAERI wind tunnels, Tsinghua CFD research

### DrivAerML — Pressure Coefficient on Car Body

```python
cinematic_render(
    file_path="drivaerml/run_1/boundary_1.vtp",
    field_name="CpMeanTrim",
    colormap="Cool to Warm",
    quality="cinematic",
    lighting="studio",
    scalar_range=[-2, 1],
    metallic=0.3,
    roughness=0.4,
    ground_plane=True
)
```

**Fields**: CpMeanTrim (-7.9 to 1.0), pMeanTrim, wallShearStressMeanTrim
**Dataset**: 8.8M cells, full car body surface mesh
**Result**: Publication-quality automotive CFD visualization with PBR car paint appearance.
**Existing showcase**: `drivaerml_cp.png`, `drivaerml_multiview.png`, `05_drivaerml_annotated.webp`

---

## 🇬🇧 United Kingdom — External Aerodynamics, CGNS

**Strengths**: Rolls-Royce (turbomachinery), BAE Systems, STFC Daresbury, WindsorML benchmark

### NACA 0012 Airfoil — CGNS Structured Grid

```python
inspect_data(file_path="cgns/naca0012/n0012_897-257.cgns")
# 461K points, 229K cells, structured grid
# Bounds: [-484, 501] × [-1, 0] × [-508, 508]

cinematic_render(
    file_path="cgns/naca0012/n0012_897-257.cgns",
    quality="cinematic",
    lighting="studio"
)
```

**Note**: CGNS multiblock structured grid — classic aerospace validation case from NASA TMR.

### WindsorML — Car Aerodynamics Benchmark

**Existing showcase**: `windsorml_multiview.png`

---

## 🇫🇷 France — Nuclear, Aerospace

**Strengths**: CEA (nuclear), Dassault (CATIA), EDF (Code_Saturne), ONERA aerospace

### Nuclear Pin — Velocity Field

```python
cinematic_render(
    file_path="nuclear_pin.vtp",
    field_name="velocityMagnitude",
    colormap="Viridis",
    quality="cinematic",
    lighting="cinematic"
)
```

### ONERA M6 Wing — Transonic Aerodynamics

```python
inspect_data(file_path="cgns/oneram6/oneram6.cgns")
# Classic transonic wing validation case
```

---

## 🇯🇵 Japan — CT Scanning, PyVista Ecosystem

**Strengths**: tkoyama010 (PyVista/awesome-vtk maintainer), RIKEN, JAXA, Toyota CFD

### Bonsai CT — Isosurface Extraction

```python
contour(
    file_path="bonsai.vti",
    field_name="ImageFile",
    isovalues=[50, 100, 150],
    colormap="Greens"
)
```

**Dataset**: 256³ voxels (16.7M points), CT scan of bonsai tree
**Result**: Nested isosurfaces revealing tree trunk/branch structure — unique cultural dataset.

### PyVista Collection

Japan's tkoyama010 maintains awesome-vtk and contributes to PyVista.
Available datasets: `bonsai.vti`, `aneurism.vti`, `brain.vtk`, `engine.vti`, `carotid.vtk`, `cow.vtp`, `earth.vtp`, `faults.vtk`

---

## 🇮🇹 Italy — Biomedical Flow, SPH

**Strengths**: CINECA HPC, MOX/Politecnico (cardiovascular CFD), DualSPHysics co-development

### Carotid Artery — Flow Streamlines

```python
streamlines(
    file_path="carotid.vtk",
    vector_field="vectors",
    seed_point1=[120, 90, 10],
    seed_point2=[160, 120, 40],
    seed_resolution=30,
    max_length=80
)
```

**Fields**: scalars (0–580), vectors (3-component flow)
**Existing showcase**: `carotid_multiview.png`

---

## 🇦🇺 Australia — Geoscience, Seismic

**Strengths**: CSIRO, Geoscience Australia, mining/resource exploration

### Seismic Survey — Amplitude & P-Wave Velocity

```python
cinematic_render(
    file_path="seismic_survey.vti",
    field_name="SeismicAmplitude",
    colormap="Cool to Warm",
    quality="cinematic",
    lighting="cinematic"
)

slice(
    file_path="seismic_survey.vti",
    field_name="PWaveVelocity",
    colormap="Viridis"
)
```

**Fields**: SeismicAmplitude, PWaveVelocity, SWaveVelocity, Density, Porosity
**Result**: Best volumetric showcase — clear seismic amplitude patterns with good color contrast.
**Existing showcase**: `04_seismic_annotated.webp`

---

## 🇨🇭 Switzerland — Space Science, Molecular

**Strengths**: CERN, ESA (ESTEC), ETH Zürich, Paul Scherrer Institute

### ESA Comet 67P — Rosetta Mission Shape Model

```python
cinematic_render(
    file_path="comet_67p_shape.obj",
    quality="cinematic",
    lighting="dramatic",
    metallic=0.1,
    roughness=0.8,
    ground_plane=False
)
```

**Result**: Iconic dual-lobe comet shape with dramatic lighting — demonstrates OBJ import and surface rendering.
**Existing showcase**: `08_bennu_annotated.webp` (NASA Bennu asteroid)

### Protein Volume — Molecular Density

```python
volume_render(
    file_path="protein_volume.vti",
    transfer_preset="generic",
    colormap="Plasma (matplotlib)",
    quality="cinematic"
)
```

**Existing showcase**: `ironprot.png`, `ironprot_orbit.gif`

---

## 🇰🇷 South Korea — Electronics Thermal, Battery

**Strengths**: Samsung/LG/SK (battery R&D), Hyundai (automotive), KAIST/KIST research

### Heatsink — Thermal Analysis

```python
cinematic_render(
    file_path="heatsink_thermal.vts",
    field_name="Temperature",
    colormap="Inferno (matplotlib)",
    quality="cinematic",
    lighting="cinematic",
    ground_plane=True
)
```

**Fields**: Temperature (250–519 K), HeatFlux (3-component vector)
**Result**: Clear thermal hotspot visualization — demonstrates electronics cooling analysis.
**Existing showcase**: `03_heatsink_annotated.webp`, `elec_cooling.png`

---

## 🇫🇮 Finland — Molecular Simulation

**Strengths**: CSC (national HPC), Helsinki/Aalto research, GROMACS ecosystem

### H₂O Electron Density — Quantum Chemistry

```python
contour(
    file_path="h2o_electron_density.vti",
    field_name="electron_density",
    isovalues=[0.5, 1, 2, 4],
    colormap="Plasma (matplotlib)"
)
```

**Dataset**: 64³ grid, electron density (0 to 8.3 e/Å³)
**Existing showcase**: `06_h2o_annotated.webp`

---

## 🇳🇱 Netherlands — Climate, Ocean

**Strengths**: KNMI (meteorology), Deltares (water), TU Delft (wind energy)

### Ocean Thermohaline — Temperature

```python
cinematic_render(
    file_path="ocean_thermohaline.vti",
    field_name="Temperature",
    colormap="Cool to Warm",
    quality="cinematic"
)
```

**Existing showcase**: `ocean_antarctica.png`

---

## 🇪🇸 Spain — SPH, Coastal Engineering

**Strengths**: DualSPHysics (Universidade de Vigo), Barcelona Supercomputing Center

### DualSPHysics — Smoothed Particle Hydrodynamics

SPH particle data requires VTK conversion via PartVTK tool.
See: [DualSPHysics post-processing guide](tutorials/)

---

## Advanced Multi-Tool Workflows

These workflows demonstrate viznoir's full 22-tool capability by combining multiple tools on the same dataset.

### Clip — Half-Cut Interior Views

```python
# Heatsink half-cut to reveal internal temperature distribution
clip(
    file_path="heatsink_thermal.vts",
    field_name="Temperature",
    origin=[0, 0, 0],
    normal=[0, 1, 0],
    colormap="Inferno (matplotlib)"
)

# Comet 67P cross-section revealing internal structure
clip(
    file_path="comet_67p_shape.obj",
    origin=[0, 0, 0],
    normal=[1, 0, 0]
)
```

### Plot Over Line — Quantitative Profiles

```python
# Heatsink temperature profile from base to fin tip
plot_over_line(
    file_path="heatsink_thermal.vts",
    field_name="Temperature",
    point1=[0, 0, 0],
    point2=[0, 0.05, 0],
    resolution=200
)

# Combustion jet centerline temperature (inlet to exit)
plot_over_line(
    file_path="combustion_jet.vts",
    field_name="Temperature",
    point1=[0, 0, 0],
    point2=[31.5, 0, 0],
    resolution=300
)
```

### Compare — Side-by-Side Field Comparison

```python
# Seismic: Amplitude vs P-Wave Velocity
compare(
    file_path_a="seismic_survey.vti",
    field_name_a="SeismicAmplitude",
    file_path_b="seismic_survey.vti",
    field_name_b="PWaveVelocity",
    mode="side_by_side"
)

# DrivAerML: Pressure coefficient vs Wall shear stress
compare(
    file_path_a="drivaerml/run_1/boundary_1.vtp",
    field_name_a="CpMeanTrim",
    file_path_b="drivaerml/run_1/boundary_1.vtp",
    field_name_b="wallShearStressMeanTrim",
    mode="side_by_side"
)
```

### Animate — Orbit & Time-Series

```python
# Comet 67P orbit animation (dramatic lighting)
animate(
    file_path="comet_67p_shape.obj",
    animation_type="orbit",
    quality="cinematic",
    lighting="dramatic",
    n_frames=60,
    fps=24
)

# Turbine ring metallic PBR orbit
animate(
    file_path="turbine_stress.vtp",
    animation_type="orbit",
    quality="cinematic",
    metallic=0.7,
    roughness=0.2,
    n_frames=60
)
```

### Split Animate — Multi-Pane Synchronized

```python
# Seismic multi-field: 3D render + 3 time-series graphs
split_animate(
    file_path="seismic_survey.vti",
    panes=[
        {"type": "render_3d", "field_name": "SeismicAmplitude"},
        {"type": "graph", "field_name": "PWaveVelocity"},
        {"type": "graph", "field_name": "SWaveVelocity"},
        {"type": "graph", "field_name": "Density"}
    ],
    layout="2x2"
)

# Combustion multi-field: Temperature + CH4 + Velocity
split_animate(
    file_path="combustion_jet.vts",
    panes=[
        {"type": "render_3d", "field_name": "Temperature"},
        {"type": "graph", "field_name": "CH4_Concentration"},
        {"type": "render_3d", "field_name": "Velocity"}
    ],
    layout="1x3"
)
```

### Preview 3D — Interactive glTF Export

```python
# Comet 67P → glTF for web-based 3D viewing
preview_3d(
    file_path="comet_67p_shape.obj",
    output_format="glb"
)

# DrivAerML car body → interactive 3D
preview_3d(
    file_path="drivaerml/run_1/boundary_1.vtp",
    field_name="CpMeanTrim",
    output_format="glb"
)
```

### Compose Assets — Composite Layouts

```python
# 4-panel country showcase composite
compose_assets(
    images=[
        "heatsink_thermal.png",      # Korea
        "drivaerml_cp.png",           # China
        "comet_67p.png",              # Switzerland
        "seismic_amplitude.png"       # Australia
    ],
    layout="2x2",
    title="Global CAE Showcase"
)
```

### Analyze Data — Domain-Specific Insights

```python
# Combustion jet domain analysis
analyze_data(
    file_path="combustion_jet.vts",
    analysis_type="summary"
)

# Seismic survey comprehensive analysis
analyze_data(
    file_path="seismic_survey.vti",
    analysis_type="summary"
)
```

### Isosurface Extraction

```python
# Bonsai CT nested isosurfaces
pv_isosurface(
    file_path="bonsai.vti",
    field_name="ImageFile",
    isovalues=[50, 100, 150, 200],
    colormap="Greens"
)

# H2O electron density orbital shells
pv_isosurface(
    file_path="h2o_electron_density.vti",
    field_name="electron_density",
    isovalues=[0.5, 1.0, 2.0, 4.0],
    colormap="Plasma (matplotlib)"
)
```

### Render — Basic with Custom Camera

```python
# Custom camera angle for Stanford Bunny
render(
    file_path="bunny.ply",
    camera_position=[0, 0.1, 0.3],
    camera_focal_point=[0, 0.1, 0],
    camera_up=[0, 1, 0]
)
```

### Execute Pipeline — Full DSL

```python
# Multi-step combustion analysis pipeline
execute_pipeline(
    pipeline={
        "source": {"file_path": "combustion_jet.vts"},
        "filters": [
            {"type": "Slice", "origin": [15.75, 0, 0], "normal": [0, 1, 0]},
            {"type": "Contour", "field": "CH4_Concentration", "isovalues": [0.1, 0.5, 0.9]}
        ],
        "render": {
            "field_name": "Temperature",
            "colormap": "Inferno (matplotlib)",
            "quality": "cinematic"
        }
    }
)
```

---

## 🌍 Cross-Domain Showcase Summary

| Country | Domain | Best Dataset | Tool | Quality |
|---------|--------|-------------|------|---------|
| 🇺🇸 USA | Medical | skull.vti | `volume_render` (ct_bone) | ★★★★★ |
| 🇺🇸 USA | Combustion | combustion_jet.vts | `slice` + `streamlines` | ★★★★ |
| 🇩🇪 Germany | FEM | cantilever_beam_stress.vts | `cinematic_render` | ★★★ |
| 🇩🇪 Germany | Turbine | turbine_stress.vtp | `cinematic_render` (PBR) | ★★★★★ |
| 🇨🇳 China | Automotive | drivaerml/boundary_1.vtp | `cinematic_render` | ★★★★★ |
| 🇬🇧 UK | Aerospace | naca0012.cgns | `cinematic_render` | ★★★ |
| 🇫🇷 France | Nuclear | nuclear_pin.vtp | `cinematic_render` | ★★★ |
| 🇯🇵 Japan | CT Scan | bonsai.vti | `contour` | ★★★★ |
| 🇮🇹 Italy | Biomedical | carotid.vtk | `streamlines` | ★★★ |
| 🇦🇺 Australia | Geoscience | seismic_survey.vti | `cinematic_render` | ★★★★★ |
| 🇨🇭 Switzerland | Space | comet_67p_shape.obj | `cinematic_render` (dramatic) | ★★★★★ |
| 🇰🇷 Korea | Thermal | heatsink_thermal.vts | `cinematic_render` | ★★★★★ |
| 🇫🇮 Finland | Molecular | h2o_electron_density.vti | `contour` | ★★★ |
| 🇳🇱 Netherlands | Ocean | ocean_thermohaline.vti | `cinematic_render` | ★★★ |
| 🇪🇸 Spain | SPH | (DualSPHysics) | `cinematic_render` | — |

### Rendering Tips by Data Type

| Data Type | Best Tool | Tip |
|-----------|-----------|-----|
| Surface mesh (.vtp, .stl, .obj) | `cinematic_render` | Use PBR metallic/roughness for realism |
| Structured volume (.vti) | `volume_render` or `slice` | Choose transfer_preset matching domain |
| CFD fields (.vts, .vtu) | `slice` + `contour` | Slice at symmetry planes for internal flow |
| Vector fields | `streamlines` | Place seeds at inlet/interesting regions |
| Medical CT | `volume_render` (ct_bone/ct_tissue) | Adjust scalar_range for tissue contrast |
| FEM stress | `cinematic_render` | Plasma/Inferno colormaps show stress concentration |

---

## Dataset Sources

| Dataset | Source | License | Size |
|---------|--------|---------|------|
| skull.vti | Kitware/VTK Examples | BSD | ~50MB |
| combustion_jet.vts | VTK Classic | BSD | ~4MB |
| DrivAerML | ML-CFD Benchmark | CC-BY | ~1.1GB |
| WindsorML | ML-CFD Benchmark | CC-BY | ~394MB |
| NACA 0012 CGNS | NASA TMR | Public | ~140MB |
| seismic_survey.vti | Synthetic | MIT | ~13MB |
| Comet 67P | ESA/Rosetta | CC-BY-SA | ~2MB |
| heatsink_thermal.vts | Synthetic | MIT | ~2MB |
| bonsai.vti | Kitware/PyVista | BSD | ~16MB |
| protein_volume.vti | VTK Classic | BSD | ~4MB |
| h2o_electron_density.vti | Synthetic | MIT | ~1MB |
| carotid.vtk | Kitware/PyVista | BSD | ~3MB |
