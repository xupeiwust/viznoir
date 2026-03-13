# Country-Specific Tutorials

Quick-start examples tailored to popular CAE domains by region.

## Automotive CFD (🇨🇳 🇩🇪 🇬🇧 🇯🇵 🇰🇷)

```
> Open the DrivAerML car body, render pressure coefficient with cinematic lighting
```

viznoir automatically:
1. Reads the 8.8M-cell surface mesh (`.vtp`)
2. Maps CpMeanTrim field with Cool-to-Warm colormap
3. Applies PCA-based auto-camera framing
4. Renders with 3-point cinematic lighting + SSAO + FXAA

**Output**: Publication-quality car aerodynamics image in ~3 seconds.

## Structural FEA (🇩🇪 🇫🇷 🇺🇸)

```
> Render the cantilever beam Von Mises stress with a ground plane
```

```
> Create an orbit animation of the turbine ring with metallic PBR material
```

**Tips**:
- Use `Plasma` or `Inferno` colormaps for stress concentration
- `metallic=0.7, roughness=0.2` for metallic parts
- `ground_plane=True` adds depth perception

## Medical Imaging (🇺🇸 🇯🇵 🇮🇹)

```
> Volume render the skull CT with ct_bone preset
```

```
> Slice the bonsai CT at z=128 and extract isosurfaces at values 50, 100, 150
```

**Transfer function presets**: ct_bone, ct_tissue, mri_brain, thermal, generic, isosurface_like

## Geoscience & Climate (🇦🇺 🇳🇱)

```
> Render the seismic survey amplitude field and create a P-wave velocity slice
```

**Multi-field workflow**: Use `batch_render` to visualize SeismicAmplitude, PWaveVelocity, Density, and Porosity in one call.

## Space Science (🇨🇭 🇺🇸)

```
> Render the Comet 67P shape with dramatic lighting, no ground plane
```

**Tips**:
- `lighting="dramatic"` for space objects (strong key light, minimal fill)
- `roughness=0.8` for rocky/asteroid surfaces
- `ground_plane=False` for floating objects

## Combustion CFD (🇺🇸 🇫🇷)

```
> Slice the combustion jet at centerplane, show temperature with Inferno colormap,
> then overlay velocity streamlines
```

**Multi-tool workflow**:
1. `slice` — Temperature cross-section at symmetry plane
2. `streamlines` — Velocity field from inlet seed line
3. `contour` — CH4 concentration isosurfaces for flame front

## Biomedical Flow (🇮🇹 🇺🇸)

```
> Create streamlines through the carotid artery to visualize blood flow patterns
```

**Tips**: Seed streamlines along the vessel inlet for best flow visualization.

## Electronics Thermal (🇰🇷 🇯🇵)

```
> Render the heatsink temperature with Inferno colormap and cinematic quality
```

**Multi-field**: Temperature (scalar) + HeatFlux (vector) — combine `cinematic_render` for temperature surface and `streamlines` for heat flux direction.

## Molecular Visualization (🇫🇮 🇨🇭)

```
> Extract electron density isosurfaces at 0.5, 1.0, 2.0, 4.0 e/Å³
```

**Tips**: Use `contour` for orbital visualization, `volume_render` with `generic` preset for density clouds.
