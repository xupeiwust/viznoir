# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.11.0](https://github.com/xupeiwust/viznoir/compare/v0.10.1...v0.11.0) (2026-07-16)


### Features

* --version flag, FileNotFoundError with suggestions, publish verification ([45d21f5](https://github.com/xupeiwust/viznoir/commit/45d21f5402bd4efb04cf03df262a65410442a03b))
* adaptive render resolution — purpose parameter + PNG compression + auto cell-to-point ([#17](https://github.com/xupeiwust/viznoir/issues/17)) ([25ed4e1](https://github.com/xupeiwust/viznoir/commit/25ed4e1dce3858771d6158d4db9aa27bf3836fab))
* add __main__.py for 'python -m parapilot' support (1075 tests) ([ca01de2](https://github.com/xupeiwust/viznoir/commit/ca01de2397d7625585ddf54ee15de30b5c24ee73))
* add 1080p HD video showcase with autoplay orbit renders ([fa2bdc7](https://github.com/xupeiwust/viznoir/commit/fa2bdc77d23d07be0c1d132e7a96c0349c393b62))
* add 13 engineering domain showcase gallery ([3cf2490](https://github.com/xupeiwust/viznoir/commit/3cf24906b34d8e44887d3c4166e7638385461df6))
* add 360° orbit animation showcase with GIF + animated WebP ([1775bf1](https://github.com/xupeiwust/viznoir/commit/1775bf1e415b74fbce2ff1e1da1a52f6720319eb))
* add Blue to Red Rainbow and X Ray colormaps (16 → 18 colormaps, 1073 tests) ([2180fbd](https://github.com/xupeiwust/viznoir/commit/2180fbd464aabd0231ec49eae6cdff9c5367ccf9))
* add cae-postprocess skill — domain expert translator for viznoir plugin ([9b49014](https://github.com/xupeiwust/viznoir/commit/9b490141554d564df8f7934b76585f7b4bfe172b))
* add CI/CD workflows, README, fix lint/type errors ([c8ee93d](https://github.com/xupeiwust/viznoir/commit/c8ee93d0fe25a23a0631c7ac46d44ba2eb962f8e))
* add cividis and twilight colormap presets ([d8db31e](https://github.com/xupeiwust/viznoir/commit/d8db31e415c1f0fa691f2f19f7db0ba8f13d7de6))
* add CVD reactor multi-field analysis to showcase ([82db24d](https://github.com/xupeiwust/viznoir/commit/82db24d1d09ca0b7eda788c5e03b6d2ea3d35240))
* add DATA ANALYSIS showcase section with plot_over_line and extract_stats ([767de1f](https://github.com/xupeiwust/viznoir/commit/767de1f77d3ab86983c35087f1fc618411ad3693))
* add Docker deployment config ([1183a0e](https://github.com/xupeiwust/viznoir/commit/1183a0ee06be60584c681b1bece25a9c4ee735d5))
* add DualSPHysics SPH context parser ([cd93043](https://github.com/xupeiwust/viznoir/commit/cd93043aea9e7b71b70b6dac759af48c4bfd4405))
* add HTTP/SSE transport mode (--transport sse|streamable-http) ([d5a75e7](https://github.com/xupeiwust/viznoir/commit/d5a75e77284f72f8ca0f23b55f8257d64462d2a3))
* add landing page (Astro 5 + Tailwind) ([8319b6a](https://github.com/xupeiwust/viznoir/commit/8319b6a4cb3b2be9eaf12eaca315431adc3a876a))
* add MCP E2E showcase section and honest limitations ([d7fe9b2](https://github.com/xupeiwust/viznoir/commit/d7fe9b23b4b8abc4fb4545f8e4d3968e1ba2f538))
* add MRC/MAP reader for cryoEM electron density maps ([a9af47d](https://github.com/xupeiwust/viznoir/commit/a9af47dedd47fceceac6bb08038ee47645c8a89e))
* add multi-view analysis showcase (CT head + carotid flow composites) ([07c0348](https://github.com/xupeiwust/viznoir/commit/07c034806ed2ae70e887cd516cd633147f102995))
* add OG image for social media sharing ([e1b0158](https://github.com/xupeiwust/viznoir/commit/e1b0158779973e9e8169ac146d0e85c303ba3ef4))
* add OpenFOAM, FEA, kitchen CFD to multi-view showcase ([81ab72d](https://github.com/xupeiwust/viznoir/commit/81ab72d0cf7a2e2d71bafbcffb291683639ef209))
* add parapilot://cinematic resource + auto-camera docs ([399eb87](https://github.com/xupeiwust/viznoir/commit/399eb87046eb85e44d71ebd1f541c01d9d3ba33f))
* add showcase gallery with 6 real VTK renders to landing page ([fb3c5d5](https://github.com/xupeiwust/viznoir/commit/fb3c5d524fcd62334184dfc46994f10cb159e806))
* add streamlines and clip showcases, improve CT skull render ([c08e3f7](https://github.com/xupeiwust/viznoir/commit/c08e3f74724d3e6ed09f06f5a38d6baea62ba285))
* add tasks optional dependency, update CHANGELOG with MCP Tasks + security tests ([19ba370](https://github.com/xupeiwust/viznoir/commit/19ba370ef8a8f1503077808050d31a2d0c674871))
* add terminal animation, comparison chart, client badges ([df1eea2](https://github.com/xupeiwust/viznoir/commit/df1eea2255ada6afdd3a58ef6a415f3c323eb325))
* add volume rendering support (vtkSmartVolumeMapper) ([5f95da4](https://github.com/xupeiwust/viznoir/commit/5f95da453f0db5f4a4c80358668cf8f783bafcdd))
* add WindsorML + DrivAerML automotive CFD to multi-view showcase ([a0c9326](https://github.com/xupeiwust/viznoir/commit/a0c93264c8eeb16eb29b512b0c528de30fcfe9f0))
* agent harness — auto_postprocess meta-tool with MCP sampling ([7aec383](https://github.com/xupeiwust/viznoir/commit/7aec38367327541b375cbb41de6e056ef15f3f0e))
* **api:** add SemVer + deprecation policy with an enforced deprecation helper ([#101](https://github.com/xupeiwust/viznoir/issues/101)) ([3eec38a](https://github.com/xupeiwust/viznoir/commit/3eec38aa6f0321516a972469aeee6cfa396989b8)), closes [#64](https://github.com/xupeiwust/viznoir/issues/64)
* **autoexp:** add modify-&gt;render-&gt;measure-&gt;keep/revert ratchet (pilot) ([#96](https://github.com/xupeiwust/viznoir/issues/96)) ([be7a3ea](https://github.com/xupeiwust/viznoir/commit/be7a3ea5cbde9f51e660e9781c64c36fb0029727)), closes [#61](https://github.com/xupeiwust/viznoir/issues/61)
* batch_render tool — render multiple fields in one call (17 tools) ([5f24d61](https://github.com/xupeiwust/viznoir/commit/5f24d610daa9fed493cc9bf6a442ec7de377f50e))
* CI/CD quality gates + contributor reward system + branch protection ([634a084](https://github.com/xupeiwust/viznoir/commit/634a0848e876a7a08785ee63871b8941382a7b7d))
* cinematic rendering — auto-camera, 3-point lighting, SSAO, FXAA, PBR ([6fbbe1b](https://github.com/xupeiwust/viznoir/commit/6fbbe1b5877dd58142cfac9849766c59f59fe764))
* compare tool, camera paths, PBR materials — 15 tools, 461 tests ([a113630](https://github.com/xupeiwust/viznoir/commit/a11363032529a17ecbce0d8dedf349260889ecde))
* Dockerfile.cpu, server tests 41개, thermal example pipeline ([594f948](https://github.com/xupeiwust/viznoir/commit/594f94897ed685ffb103c6fbae6e0d60092b4453))
* DrivAerML Cp as featured hero — automotive CFD first impression ([4e2f599](https://github.com/xupeiwust/viznoir/commit/4e2f5998503776d40c5f57aa150939524ec1f1af))
* enrich colormaps resource with field-type recommendations, fix colormap count in launch docs ([f67ef08](https://github.com/xupeiwust/viznoir/commit/f67ef0804ece9881ec7340508fc092151a08b8d3))
* expand showcase gallery — 11 new renders (volumetric, cavity CFD, thermal, FEA) ([1112104](https://github.com/xupeiwust/viznoir/commit/11121044df5fb66f6f1e0aa0be9fe623849da5ed))
* **guard:** physics-aware render validation (rules + validator) ([#94](https://github.com/xupeiwust/viznoir/issues/94)) ([9811f9a](https://github.com/xupeiwust/viznoir/commit/9811f9aa325e9580ae2bbffa43b6a5c92a0d4d40))
* MCP compliance tests, dependency review, benchmarks, social preview, social media drafts ([0021d45](https://github.com/xupeiwust/viznoir/commit/0021d45c51c8efd45d2fc99117ad7ef7aafad036))
* MCP Tasks support for long-running tools (FastMCP 3.x, backward-compatible, 1134 tests) ([6980b74](https://github.com/xupeiwust/viznoir/commit/6980b744bf138b9e9eca08d259a95d88d683a3c0))
* migrate pv-agent → parapilot (full MCP server) ([027718b](https://github.com/xupeiwust/viznoir/commit/027718bbda046abd86ce68de57e8996fab5e40b0))
* Phase 1+2 — logging, errors, filters, meshio, glTF, CI, docs ([2eb6a17](https://github.com/xupeiwust/viznoir/commit/2eb6a179c6739e8dc68f56bedd7fe1cb4fba586f))
* Phase 3 P2-3 — per-block styling for multiblock datasets (1048 tests) ([f2309be](https://github.com/xupeiwust/viznoir/commit/f2309bedc61a3f0f172f76c0deb1a7feeee0caf4))
* **plugins:** entry-point plugin system for filters/parsers/presets ([#103](https://github.com/xupeiwust/viznoir/issues/103)) ([e3255c0](https://github.com/xupeiwust/viznoir/commit/e3255c0d2c5bbbc009c56930b889907a026c4bea)), closes [#66](https://github.com/xupeiwust/viznoir/issues/66)
* preview_3d tool + three.js interactive viewer (16 tools) ([08bd3bf](https://github.com/xupeiwust/viznoir/commit/08bd3bfe4d1666bf5b5ea2e027e2250ece698655))
* probe_timeseries tool — sample field at a point over time (18 tools) ([c2c675e](https://github.com/xupeiwust/viznoir/commit/c2c675e4567efbef6e28fde3f265a5a170356885))
* property-based testing (Hypothesis), SECURITY.md, OpenSSF Scorecard, pre-commit config, coverage threshold 80% (1086 tests) ([1463b7e](https://github.com/xupeiwust/viznoir/commit/1463b7e290cf366c1e424584d5fbeb8dd80966e0))
* **quality:** add render quality metrics (contrast, edge entropy, field coverage) ([#93](https://github.com/xupeiwust/viznoir/issues/93)) ([1883692](https://github.com/xupeiwust/viznoir/commit/188369207f1e75270b9e343c61a2b30fe4cf4d15)), closes [#60](https://github.com/xupeiwust/viznoir/issues/60)
* **registry:** publish to MCP Registry via OIDC ([#80](https://github.com/xupeiwust/viznoir/issues/80)) ([2d41b00](https://github.com/xupeiwust/viznoir/commit/2d41b00c573ba42a048c71a7eb599bd4a01f87fb))
* replace synthetic renders with official VTK example data showcase ([e13b913](https://github.com/xupeiwust/viznoir/commit/e13b9135a9c8a60b6a90dd309b6cc7461973b976))
* replace VTK Cow with Iron Protein molecular visualization ([29d617f](https://github.com/xupeiwust/viznoir/commit/29d617f879b069bb0ea1e8b0ccd10fe28217201a))
* replace weak cfd_pressure with office airflow showcase ([9a37053](https://github.com/xupeiwust/viznoir/commit/9a370534cf974ff3057cb63f91ec6a2d83e4b19e))
* Science Storytelling showcase — physics decomposition with LaTeX + compose ([0121614](https://github.com/xupeiwust/viznoir/commit/012161410bb1e36eaca254e0af7879c9a7583902))
* scientific-first showcase redesign ([a5ae483](https://github.com/xupeiwust/viznoir/commit/a5ae483b31acae6d1b6525880d17907e8c7e48fc))
* slim README + landing page, add /docs developer documentation ([1a08ed1](https://github.com/xupeiwust/viznoir/commit/1a08ed18030b12aa9048d3370af92a0c4db3df25))
* **tools:** add validate_render MCP tool (physics guard on render specs) ([#95](https://github.com/xupeiwust/viznoir/issues/95)) ([3353a8d](https://github.com/xupeiwust/viznoir/commit/3353a8d6599e6f800f009ef8b557c55b24f780e5)), closes [#59](https://github.com/xupeiwust/viznoir/issues/59)
* troubleshooting guide + PLY/OBJ/STL integration tests (closes [#37](https://github.com/xupeiwust/viznoir/issues/37), closes [#38](https://github.com/xupeiwust/viznoir/issues/38), 1091 tests) ([020d756](https://github.com/xupeiwust/viznoir/commit/020d756a041b244e6d4d32d81952f6398541cb0b))
* v0.5.0 Science Storyteller — analyze, compose, timeline, transitions ([#12](https://github.com/xupeiwust/viznoir/issues/12)) ([7685fcb](https://github.com/xupeiwust/viznoir/commit/7685fcb7b0b8c19e622d5196e5107cbfd13a1f80))
* v0.6 showcase rebrand — 10 domains, physics animations ([c04b19b](https://github.com/xupeiwust/viznoir/commit/c04b19b9fc32e1fdfde9b69c389afed999a6f007))
* v0.8.0 industrial validation — Fluent reader, CGNS parser, example gallery ([#42](https://github.com/xupeiwust/viznoir/issues/42)) ([a51aeaa](https://github.com/xupeiwust/viznoir/commit/a51aeaac3f3fb0a0d77b180d1eacfb01e11eba60))
* VTK-native annotations + physics-driven animation presets ([a5bee06](https://github.com/xupeiwust/viznoir/commit/a5bee06b103f580c96c12292c50a0fb667609ed0))
* **www:** add GEO content — UseCases, Comparison table, FAQ with schema markup ([ba9c006](https://github.com/xupeiwust/viznoir/commit/ba9c006933baec28efc0c9594b016cf1d1719c7f))
* **www:** add GEO optimization — robots.txt, llms.txt, sitemap.xml, JSON-LD schema, citability block ([528d8ed](https://github.com/xupeiwust/viznoir/commit/528d8ed547cb02a6ede1e2e1d9f973e4181919cf))


### Bug Fixes

* accept snake_case filter names in pipeline DSL ([0e6dd9a](https://github.com/xupeiwust/viznoir/commit/0e6dd9a48dbb5d040d60a206c18e51a74f42d80d))
* add base path to showcase image URLs for GitHub Pages ([8b2a039](https://github.com/xupeiwust/viznoir/commit/8b2a0390b6665671d21306fda3a47ebdb7f21f8f))
* add mcp config to plugin.json, fix asyncio deprecation warning ([c9e8fcc](https://github.com/xupeiwust/viznoir/commit/c9e8fcc1c0b8edcfff5327a3fe87b5bab6a7ce0d))
* add missing vtk import in read_dataset + public API tests ([3adc867](https://github.com/xupeiwust/viznoir/commit/3adc867d6e72d7420dbaf3f453341a62c6b9fd03))
* auto-compute slice/clip origin from dataset center ([caa1bf3](https://github.com/xupeiwust/viznoir/commit/caa1bf36e069f7ec40a83e954059c5942c2d6474))
* centralize VTK rendering skip in conftest.py (root cause fix) ([98c8fbf](https://github.com/xupeiwust/viznoir/commit/98c8fbf090242787609b0966acc73e4e0b1e2cef))
* CI ImportError — _has_mcp_tasks() checks docket availability, tasks extra includes pydocket ([7cc8e11](https://github.com/xupeiwust/viznoir/commit/7cc8e11198edf313de6e54d936f4bb14703aef77))
* **ci:** bump deploy Node 20 -&gt; 22 for Astro 6.4 ([#89](https://github.com/xupeiwust/viznoir/issues/89)) ([d8945ef](https://github.com/xupeiwust/viznoir/commit/d8945effe843249136207c2e9bb291d2173d8bbc))
* **ci:** skip *_vtk.py tests in CI — SIGSEGV on headless runners ([468fe4d](https://github.com/xupeiwust/viznoir/commit/468fe4d61c8e58fca15c8c6c7376cb790ca93921))
* **ci:** skip PR Template check for bot authors ([#79](https://github.com/xupeiwust/viznoir/issues/79)) ([7b0927a](https://github.com/xupeiwust/viznoir/commit/7b0927ada6ad2b34d075d480c91ad2923ec89f87))
* compositor grid labels, auto-cols, list mutation, negative dimension guard ([6e19c20](https://github.com/xupeiwust/viznoir/commit/6e19c20614f814200aefc38f83903dbfff375beb))
* correct domain count, add Gemini CLI, update README showcase ([d59792b](https://github.com/xupeiwust/viznoir/commit/d59792be88a71c7138c68cc560dc143ee0c69ebe))
* correct LLNL/paraview_mcp tools count 8→23 in README and landing page ([3197e40](https://github.com/xupeiwust/viznoir/commit/3197e4097a63e978bbb72a32beaeab0e00f0fbb3))
* flaky CI tests — _registered_instances id() reuse after GC ([b5b1e63](https://github.com/xupeiwust/viznoir/commit/b5b1e63d8851f0b86a7c3e0c6f5c6c4fac1053af))
* guard cols=0 on empty assets, add list mutation regression tests ([1174bf8](https://github.com/xupeiwust/viznoir/commit/1174bf865f81b70e92b9d2a4f3a56dcfd4874b2c))
* handle missing ffmpeg in compile_video test ([dbc30b8](https://github.com/xupeiwust/viznoir/commit/dbc30b89763c2653800585202e42fe11e14dd276))
* improve biomedical render, clean up unused assets ([dac1b2a](https://github.com/xupeiwust/viznoir/commit/dac1b2a59211fd858dde061014538bdb7b48d998))
* MCP compliance tests use .fn for FastMCP version compatibility ([7327eec](https://github.com/xupeiwust/viznoir/commit/7327eecc77e34f780cd07d7a32d9d88a6ebfbdf0))
* module-level resource/prompt registration + mutation-tested config (1116 tests) ([59e3753](https://github.com/xupeiwust/viznoir/commit/59e375350ea058a1746bcfb1352023a50dc9a4a8))
* monitor.sh use --workflow flag instead of --branch ([bf716a6](https://github.com/xupeiwust/viznoir/commit/bf716a60f0e62f0a9de760d75623bb05c4bc2ad6))
* move mcp import to module level in test_story_prompt (flaky CI fix) ([33d0247](https://github.com/xupeiwust/viznoir/commit/33d0247a021774ec9789539fd47a6bfcbe4a0e41))
* narrow exception handling in postfx/readers + security tests for path validation (1128 tests) ([7b008c9](https://github.com/xupeiwust/viznoir/commit/7b008c9f5ee086240ab1ef0a0fd879e07252b19b))
* normalize CamelCase filter names to snake_case in apply_filter ([8f3cdbb](https://github.com/xupeiwust/viznoir/commit/8f3cdbb586c473255f3c11890ec769090711d919))
* pin mcp&lt;1.26 (3.11 regression) + exclude GPU modules from CI coverage ([75904f0](https://github.com/xupeiwust/viznoir/commit/75904f0c943c4319489ba5efd9e6ff163957a791))
* README test count 748→1048, remove empty-PR contributor, awesome-mcp-servers PR [#2807](https://github.com/xupeiwust/viznoir/issues/2807) ([2296242](https://github.com/xupeiwust/viznoir/commit/2296242350762f0dcd4f7d584a7d2374ae679342))
* **registry:** shorten server.json description to &lt;=100 chars ([#82](https://github.com/xupeiwust/viznoir/issues/82)) ([2d8fd16](https://github.com/xupeiwust/viznoir/commit/2d8fd1625fec841b54a2ca46b184a2ccb166d6fb))
* **release:** exclude /tests from sdist (&lt;1MB) + add publish workflow_dispatch ([#76](https://github.com/xupeiwust/viznoir/issues/76)) ([a5d3f61](https://github.com/xupeiwust/viznoir/commit/a5d3f61466e4453889b215219fd65cf8f494d1b2))
* replace O(n) byte-by-byte PNG extraction with numpy bulk copy ([22fbb90](https://github.com/xupeiwust/viznoir/commit/22fbb90567b5ab913a3f6ceb6c9a391fd1d41226))
* replace sparse stellar catalog with brain MRI + globe render ([b1ce550](https://github.com/xupeiwust/viznoir/commit/b1ce550225fb76d9be2c4abe5fee715249788c9e))
* resolve 20 mypy type errors across camera, cinematic, compare modules ([7e8f0b1](https://github.com/xupeiwust/viznoir/commit/7e8f0b1cb7198c7c5c7899cd0185cdb672486852))
* resolve 3 rendering bugs found in E2E testing ([5b7b94e](https://github.com/xupeiwust/viznoir/commit/5b7b94eeb4b41ad2c1b455abba0052218b417072))
* resolve 4 runtime bugs found in E2E testing ([b93f561](https://github.com/xupeiwust/viznoir/commit/b93f561185ecdd7420be880592ba49e1903dea4e))
* resolve CI failures — mypy strict generics + glTF export segfault ([3498c44](https://github.com/xupeiwust/viznoir/commit/3498c443483d3e71aa82172940d156cac00100df))
* resolve CI failures (mypy ndarray type-arg, fail-fast) ([a16bffc](https://github.com/xupeiwust/viznoir/commit/a16bffc835cc9306dae5636ba366ae8f82491167))
* resolve remaining ruff lint errors (unused imports, sort order) ([6a7b3bf](https://github.com/xupeiwust/viznoir/commit/6a7b3bf3f3fd5384b2646eaaef5ef0454d2ace8b))
* resolve ruff E402 import ordering in test files + add release drafter ([f2c7d78](https://github.com/xupeiwust/viznoir/commit/f2c7d786f5a9ec15ef48d2a86424f86832566786))
* resolve ruff lint errors in test files (F401, I001, E501) ([87ea7e8](https://github.com/xupeiwust/viznoir/commit/87ea7e83964665b6ee46a27f11b648e866d0d8ea))
* sdist excludes www/video/docs — 251MB → 192KB package size ([3e3e4d7](https://github.com/xupeiwust/viznoir/commit/3e3e4d72fe1924d86d04ddc8517e399c4b15ff71))
* set PARAPILOT_PYTHON_BIN to /bin/python3 in MCP config ([c8b0ce6](https://github.com/xupeiwust/viznoir/commit/c8b0ce605004278cd4afdc98184327d6b2ebea15))
* skip compile_video timeout test when ffmpeg unavailable (CI fix) ([866b8db](https://github.com/xupeiwust/viznoir/commit/866b8db6e0152de58def99339722352d27e1db2f))
* skip VTK rendering tests in CI + add OSS strategy docs ([7b5f668](https://github.com/xupeiwust/viznoir/commit/7b5f668bffe75eef652090d912602c908f9d4cfc))
* sync COLORMAP_GUIDE with REGISTRY (remove phantom colormaps, add 5 missing), update comparison table with new competitors, bump test count to 1070 ([ff78308](https://github.com/xupeiwust/viznoir/commit/ff7830875bea1f694a3287ea41576a2b77d30771))
* update landing page stats to match actual counts ([ea8ae0f](https://github.com/xupeiwust/viznoir/commit/ea8ae0f78127306ede46180a9a89faab56374154))
* update test count 309 → 310 across all landing page components ([08c5be8](https://github.com/xupeiwust/viznoir/commit/08c5be8907a8328c9d3302915f2e11fb7f240293))
* use absolute URLs for README images (PyPI compatibility) ([529e4af](https://github.com/xupeiwust/viznoir/commit/529e4afe4ddd08f274dd3c3ef916556587652871))
* vtkTrivialProducer GetOutput → GetOutputDataObject fallback ([6944dfd](https://github.com/xupeiwust/viznoir/commit/6944dfd01f8f4e9e9bdc666d8495a2dff9d9c46e))


### Performance Improvements

* add WebP images for 90% showcase size reduction ([1df2778](https://github.com/xupeiwust/viznoir/commit/1df2778240047cc0f5a11605f7ace667e575d8ff))


### Documentation

* adaptive render benchmark report + bench scripts ([#32](https://github.com/xupeiwust/viznoir/issues/32)) ([688f45d](https://github.com/xupeiwust/viznoir/commit/688f45d586f25761df2e592319c5cd908785e1ff))
* adaptive render v2 design spec + implementation plan ([#30](https://github.com/xupeiwust/viznoir/issues/30)) ([8d97a2c](https://github.com/xupeiwust/viznoir/commit/8d97a2c40a915d5260892182e53ddbc90748aa5d))
* add 7-language README translations for viznoir ([8784131](https://github.com/xupeiwust/viznoir/commit/87841315d45fffb89de2828addacb57968364e55))
* add aerodynamics and structural FEA workflow examples ([c63ab2b](https://github.com/xupeiwust/viznoir/commit/c63ab2be859ea565fc7905bd7048d8f46320f881))
* add Awesome AI-CAE featured badge ([879d504](https://github.com/xupeiwust/viznoir/commit/879d50464e7c1b75e9238efbca2ab859f1a04923))
* add Contributor Covenant Code of Conduct v2.1 ([f04fe0a](https://github.com/xupeiwust/viznoir/commit/f04fe0a513f60690c613c606bd59840545f39643))
* add docs, pre-commit, ruff badges to README ([cdb9f0d](https://github.com/xupeiwust/viznoir/commit/cdb9f0d8d1cfbd913ecb766d280ed20a028731e3))
* add Glama MCP server badge ([#20](https://github.com/xupeiwust/viznoir/issues/20)) ([1e89bd7](https://github.com/xupeiwust/viznoir/commit/1e89bd73fc2056bd480a3b0e4ef2e9f6cf31f563))
* add global showcase gallery + country tutorials (14 countries, 22 tools) ([3a03b7a](https://github.com/xupeiwust/viznoir/commit/3a03b7a840064b8a2280a9f2526bef3233081541))
* add Korean README (README.ko.md) with language toggle links (closes [#21](https://github.com/xupeiwust/viznoir/issues/21)) ([7e75881](https://github.com/xupeiwust/viznoir/commit/7e7588198b662f50da0a16bccc96d5bf749139b9))
* add Mentioned in Awesome VTK badge ([#16](https://github.com/xupeiwust/viznoir/issues/16)) ([8576313](https://github.com/xupeiwust/viznoir/commit/8576313679da81c518f3b0a3565767c054b739b4))
* add redesign implementation plan (README + Landing Page v2) ([4be095d](https://github.com/xupeiwust/viznoir/commit/4be095d6724f9534fda716e578bf05a27de5b818))
* add v0.5.0 changelog, sync metrics (1315+ tests, 97% cov), cleanup stale files ([8603bff](https://github.com/xupeiwust/viznoir/commit/8603bffd77ad8e75bb8146dc7f612d5948118869))
* cae-postprocess skill design — domain expert translator for viznoir ([890cea0](https://github.com/xupeiwust/viznoir/commit/890cea0fa25bfd5a82ffb7abaa04c792243a83f4))
* cae-postprocess skill implementation plan (3 tasks) ([f071e48](https://github.com/xupeiwust/viznoir/commit/f071e487699946a5f311d0bbd758ca7001475cde))
* comprehensive OSS strategy with real data + execution checklist ([6e32ca3](https://github.com/xupeiwust/viznoir/commit/6e32ca357611f9a1082abf10687756e319a36aae))
* enhance README — add What it does, Capabilities table, Works with ([d3d8b9d](https://github.com/xupeiwust/viznoir/commit/d3d8b9dcca166184d2ff1512fa25021e01d77bae))
* final metrics sync to 828 tests, 83% coverage ([361a01b](https://github.com/xupeiwust/viznoir/commit/361a01bd52abf053afa4c2e69c7f31ef9d1eab0e))
* fix install commands mcp-server-viznoir -&gt; viznoir + PyPI URLs ([#90](https://github.com/xupeiwust/viznoir/issues/90)) ([4070bee](https://github.com/xupeiwust/viznoir/commit/4070bee4fc6c0306f118a19310a217f2c8bdcd26))
* JOSS paper draft + update CITATION.cff metrics ([83c4f6a](https://github.com/xupeiwust/viznoir/commit/83c4f6aa9773e50834c22e52a904f16819f1cd67))
* ME Autoresearch Harness — README update + implementation plan ([#28](https://github.com/xupeiwust/viznoir/issues/28)) ([b992870](https://github.com/xupeiwust/viznoir/commit/b992870c276ff4d1d0e34654f2519c17d9642c8e))
* MkDocs API documentation site (mkdocs-material) ([4675183](https://github.com/xupeiwust/viznoir/commit/46751838a5b9a9911d567a0b257aadefb6a2cf6a))
* redesign README — benchmark-driven, ~120 lines ([dc2bcb4](https://github.com/xupeiwust/viznoir/commit/dc2bcb4783ee2b5a85eae0a4db262759ca841db0))
* redesign README in Paperclip style — 3-step flow, feature grid, comparison table ([#19](https://github.com/xupeiwust/viznoir/issues/19)) ([d273577](https://github.com/xupeiwust/viznoir/commit/d273577daf8f30bf08a775106b09ec61b51f98cd))
* Science Storyteller v2 design — physics-aware analysis pipeline ([f93e75f](https://github.com/xupeiwust/viznoir/commit/f93e75f56320c9ee3f1c6c0965736d8ae1f9060f))
* Science Storyteller v2 implementation plan (6 tasks) ([08fc8ff](https://github.com/xupeiwust/viznoir/commit/08fc8ff27c38e699a4f1027f1cb7f13563bc8037))
* sync all metrics — 18 tools, 11 resources, 627 tests, 70% coverage ([87220e5](https://github.com/xupeiwust/viznoir/commit/87220e5c23046ff02903ac1ca31f299dc19f7859))
* sync all metrics to 1043 tests, 99% coverage ([2a399bf](https://github.com/xupeiwust/viznoir/commit/2a399bff31b93860d4aa2fb4c8b6bcbcfc55fe8e))
* sync all metrics to 1048 tests, add per-block styling to CHANGELOG ([f2ab1f5](https://github.com/xupeiwust/viznoir/commit/f2ab1f5b5e62e841e58a6bcee292cd59168c0cb5))
* sync all metrics to 1091 tests, expand comparison table, add OpenSSF badge, update CHANGELOG ([8c5b1ea](https://github.com/xupeiwust/viznoir/commit/8c5b1ea6e3fdb03faf9833a095d4af57e060f62a))
* sync all metrics to 1116 tests, add mutation testing to CHANGELOG, awesome-mcp-servers PR draft ([a8f83b8](https://github.com/xupeiwust/viznoir/commit/a8f83b8b70c69dc07878c9c301109337755e88fd))
* sync all metrics to 1128 tests, bump CI guard to 1120 ([f4f76cb](https://github.com/xupeiwust/viznoir/commit/f4f76cb3b0d7c608bc467d818e8e595d97f4c2b1))
* sync all metrics to 846 tests, 84% coverage ([96f39e7](https://github.com/xupeiwust/viznoir/commit/96f39e7bb1c0e68e9193ec9a935c2c215d468d33))
* sync all metrics to 934 tests, 97% coverage ([c2b52f2](https://github.com/xupeiwust/viznoir/commit/c2b52f2f53a6af85c85ab87c1c651631a5d88ad4))
* sync CLAUDE.md metrics to 1134 tests, viznoir branding ([961f721](https://github.com/xupeiwust/viznoir/commit/961f72144ae10ebaf023e9fe68d2fd81a6ca66da))
* sync metrics to 794 tests, 82% coverage across all docs and landing page ([cbe1e87](https://github.com/xupeiwust/viznoir/commit/cbe1e8773ea527a3a7bf34df196af5356efd6e37))
* sync metrics to 826 tests, 83% coverage across all docs and landing page ([c4a9b46](https://github.com/xupeiwust/viznoir/commit/c4a9b466607eb8ec8d348f4cd3e0f676ed7ad25c))
* sync metrics to 836 tests, 84% coverage ([5a1d093](https://github.com/xupeiwust/viznoir/commit/5a1d0930583022718dfa525150b80dae0b985823))
* translate landing page to English, fix metrics, add contributing guide ([d81c6b8](https://github.com/xupeiwust/viznoir/commit/d81c6b8ebd0329228439ec6e7471bacf7a8e4177))
* tutorials, validation, launch prep, cinematic spec, Remotion video ([669f8d6](https://github.com/xupeiwust/viznoir/commit/669f8d64cbb45e121ce40ffbabcc0c4e4352867d))
* update all metrics to 16 tools, 624 tests ([36a2863](https://github.com/xupeiwust/viznoir/commit/36a2863eb13f36ea0bda83160e61202e600b8293))
* update CHANGELOG with all Phase 1+2 changes ([67602ce](https://github.com/xupeiwust/viznoir/commit/67602cea915f68d657d2a24566077756b81a632c))
* update CLAUDE.md architecture with cae-postprocess skill ([cbe877e](https://github.com/xupeiwust/viznoir/commit/cbe877e00ae65be06bb4a6b10da8cf4ecef6782a))
* update MCP server instructions with all 18 tools ([aa52dc6](https://github.com/xupeiwust/viznoir/commit/aa52dc6698b2fa1ef4a0b75b8ce623094457bf11))
* update metrics — 15 tools, 11 resources, 548 tests, 65% coverage ([a34fb52](https://github.com/xupeiwust/viznoir/commit/a34fb525e941a38b58adf1dbf1a8e90e940f3f37))
* update README with 15 tools, 11 resources, Makefile ([8797458](https://github.com/xupeiwust/viznoir/commit/8797458b68c42ff98c6b24700c72b568eb35d20d))
* update redesign plan — release branch model + agent team strategy ([eb5b37e](https://github.com/xupeiwust/viznoir/commit/eb5b37ea6df05a11e07fb861136b85077706c6de))
* update roadmap v0.7.0→v1.0.0 — PyPI at v1.0 only ([e942ce1](https://github.com/xupeiwust/viznoir/commit/e942ce1747f60bf594b606c92d9272bbc9e1a8a3))
* viznoir roadmap v0.6.1 → v1.0.0 ([477ce81](https://github.com/xupeiwust/viznoir/commit/477ce817a7bb94e814357b57131e4edaead8ad4e))

## [0.10.1](https://github.com/kimimgo/viznoir/compare/v0.10.0...v0.10.1) (2026-06-03)


### Bug Fixes

* **ci:** bump deploy Node 20 -&gt; 22 for Astro 6.4 ([#89](https://github.com/kimimgo/viznoir/issues/89)) ([d8945ef](https://github.com/kimimgo/viznoir/commit/d8945effe843249136207c2e9bb291d2173d8bbc))
* **registry:** shorten server.json description to &lt;=100 chars ([#82](https://github.com/kimimgo/viznoir/issues/82)) ([2d8fd16](https://github.com/kimimgo/viznoir/commit/2d8fd1625fec841b54a2ca46b184a2ccb166d6fb))

## [0.10.0](https://github.com/kimimgo/viznoir/compare/v0.9.1...v0.10.0) (2026-06-01)


### Features

* **registry:** publish to MCP Registry via OIDC ([#80](https://github.com/kimimgo/viznoir/issues/80)) ([2d41b00](https://github.com/kimimgo/viznoir/commit/2d41b00c573ba42a048c71a7eb599bd4a01f87fb))

## [0.9.1](https://github.com/kimimgo/viznoir/compare/v0.9.0...v0.9.1) (2026-06-01)


### Bug Fixes

* **release:** exclude /tests from sdist (&lt;1MB) + add publish workflow_dispatch ([#76](https://github.com/kimimgo/viznoir/issues/76)) ([a5d3f61](https://github.com/kimimgo/viznoir/commit/a5d3f61466e4453889b215219fd65cf8f494d1b2))

## [0.9.0](https://github.com/kimimgo/viznoir/compare/v0.8.0...v0.9.0) (2026-06-01)


### Features

* add DualSPHysics SPH context parser ([cd93043](https://github.com/kimimgo/viznoir/commit/cd93043aea9e7b71b70b6dac759af48c4bfd4405))
* add MRC/MAP reader for cryoEM electron density maps ([a9af47d](https://github.com/kimimgo/viznoir/commit/a9af47dedd47fceceac6bb08038ee47645c8a89e))

## [0.8.0](https://github.com/kimimgo/viznoir/compare/v0.7.2...v0.8.0) (2026-04-07)


### Features

* v0.8.0 industrial validation — Fluent reader, CGNS parser, example gallery ([#42](https://github.com/kimimgo/viznoir/issues/42)) ([a51aeaa](https://github.com/kimimgo/viznoir/commit/a51aeaac3f3fb0a0d77b180d1eacfb01e11eba60))

## [0.7.2](https://github.com/kimimgo/viznoir/compare/v0.7.1...v0.7.2) (2026-04-05)


### Documentation

* adaptive render benchmark report + bench scripts ([#32](https://github.com/kimimgo/viznoir/issues/32)) ([688f45d](https://github.com/kimimgo/viznoir/commit/688f45d586f25761df2e592319c5cd908785e1ff))
* adaptive render v2 design spec + implementation plan ([#30](https://github.com/kimimgo/viznoir/issues/30)) ([8d97a2c](https://github.com/kimimgo/viznoir/commit/8d97a2c40a915d5260892182e53ddbc90748aa5d))
* ME Autoresearch Harness — README update + implementation plan ([#28](https://github.com/kimimgo/viznoir/issues/28)) ([b992870](https://github.com/kimimgo/viznoir/commit/b992870c276ff4d1d0e34654f2519c17d9642c8e))

## [0.7.1](https://github.com/kimimgo/viznoir/compare/v0.7.0...v0.7.1) (2026-03-19)


### Documentation

* add Glama MCP server badge ([#20](https://github.com/kimimgo/viznoir/issues/20)) ([1e89bd7](https://github.com/kimimgo/viznoir/commit/1e89bd73fc2056bd480a3b0e4ef2e9f6cf31f563))

## [0.7.0](https://github.com/kimimgo/viznoir/compare/v0.6.0...v0.7.0) (2026-03-18)


### Features

* adaptive render resolution — purpose parameter + PNG compression + auto cell-to-point ([#17](https://github.com/kimimgo/viznoir/issues/17)) ([25ed4e1](https://github.com/kimimgo/viznoir/commit/25ed4e1dce3858771d6158d4db9aa27bf3836fab))
* agent harness — auto_postprocess meta-tool with MCP sampling ([7aec383](https://github.com/kimimgo/viznoir/commit/7aec38367327541b375cbb41de6e056ef15f3f0e))
* slim README + landing page, add /docs developer documentation ([1a08ed1](https://github.com/kimimgo/viznoir/commit/1a08ed18030b12aa9048d3370af92a0c4db3df25))
* v0.6 showcase rebrand — 10 domains, physics animations ([c04b19b](https://github.com/kimimgo/viznoir/commit/c04b19b9fc32e1fdfde9b69c389afed999a6f007))
* VTK-native annotations + physics-driven animation presets ([a5bee06](https://github.com/kimimgo/viznoir/commit/a5bee06b103f580c96c12292c50a0fb667609ed0))
* **www:** add GEO content — UseCases, Comparison table, FAQ with schema markup ([ba9c006](https://github.com/kimimgo/viznoir/commit/ba9c006933baec28efc0c9594b016cf1d1719c7f))
* **www:** add GEO optimization — robots.txt, llms.txt, sitemap.xml, JSON-LD schema, citability block ([528d8ed](https://github.com/kimimgo/viznoir/commit/528d8ed547cb02a6ede1e2e1d9f973e4181919cf))


### Bug Fixes

* compositor grid labels, auto-cols, list mutation, negative dimension guard ([6e19c20](https://github.com/kimimgo/viznoir/commit/6e19c20614f814200aefc38f83903dbfff375beb))
* guard cols=0 on empty assets, add list mutation regression tests ([1174bf8](https://github.com/kimimgo/viznoir/commit/1174bf865f81b70e92b9d2a4f3a56dcfd4874b2c))
* move mcp import to module level in test_story_prompt (flaky CI fix) ([33d0247](https://github.com/kimimgo/viznoir/commit/33d0247a021774ec9789539fd47a6bfcbe4a0e41))
* pin mcp&lt;1.26 (3.11 regression) + exclude GPU modules from CI coverage ([75904f0](https://github.com/kimimgo/viznoir/commit/75904f0c943c4319489ba5efd9e6ff163957a791))
* resolve ruff lint errors in test files (F401, I001, E501) ([87ea7e8](https://github.com/kimimgo/viznoir/commit/87ea7e83964665b6ee46a27f11b648e866d0d8ea))


### Documentation

* add 7-language README translations for viznoir ([8784131](https://github.com/kimimgo/viznoir/commit/87841315d45fffb89de2828addacb57968364e55))
* add Awesome AI-CAE featured badge ([879d504](https://github.com/kimimgo/viznoir/commit/879d50464e7c1b75e9238efbca2ab859f1a04923))
* add global showcase gallery + country tutorials (14 countries, 22 tools) ([3a03b7a](https://github.com/kimimgo/viznoir/commit/3a03b7a840064b8a2280a9f2526bef3233081541))
* add Mentioned in Awesome VTK badge ([#16](https://github.com/kimimgo/viznoir/issues/16)) ([8576313](https://github.com/kimimgo/viznoir/commit/8576313679da81c518f3b0a3565767c054b739b4))
* enhance README — add What it does, Capabilities table, Works with ([d3d8b9d](https://github.com/kimimgo/viznoir/commit/d3d8b9dcca166184d2ff1512fa25021e01d77bae))
* redesign README in Paperclip style — 3-step flow, feature grid, comparison table ([#19](https://github.com/kimimgo/viznoir/issues/19)) ([d273577](https://github.com/kimimgo/viznoir/commit/d273577daf8f30bf08a775106b09ec61b51f98cd))
* update roadmap v0.7.0→v1.0.0 — PyPI at v1.0 only ([e942ce1](https://github.com/kimimgo/viznoir/commit/e942ce1747f60bf594b606c92d9272bbc9e1a8a3))
* viznoir roadmap v0.6.1 → v1.0.0 ([477ce81](https://github.com/kimimgo/viznoir/commit/477ce817a7bb94e814357b57131e4edaead8ad4e))

## [Unreleased]

## [0.6.0] - 2026-03-11

### Added

- `inspect_physics` MCP tool: L2 field topology analysis (vortex detection, stagnation points, gradient statistics) + L3 case context (OpenFOAM BCs, transport properties, Re computation)
- `context/` module: CaseContext data models, ContextParser protocol, GenericContextParser (mesh quality), OpenFOAMContextParser (BCs, solver info, transport properties, derived quantities)
- `engine/topology.py`: L2 field topology analyzer — vortex detection (Q/λ₂ criteria), critical point classification, centerline probe, gradient statistics
- Science Storyteller v2 pipeline: `inspect_physics` → `cinematic_render` → `compose_assets` end-to-end workflow
- CODEOWNERS file for required code review
- PR template validation (CI-enforced): Description + Test Plan sections required
- PR auto-labeling by file path (context, animation labels)

### Changed

- MCP tools: 21 → 22
- Test count: 1315 → 1439+ (97% coverage)
- CI test count guard: 1290 → 1430
- CI: added `ruff format --check` step
- README: Before/After hero section (ParaView GUI vs viznoir), domain-expert gallery with scale metrics
- Gallery captions: generic labels → domain-specific with cell/face counts

### Fixed

- `openfoam.py`: file encoding error on non-UTF8 boundary files (`read_text(errors="replace")`)
- `openfoam.py`: backup/swap files (`.orig`, `.bak`, `.swp`) incorrectly parsed as boundary conditions
- `openfoam.py`: `parse_dataset()` now raises `NotImplementedError` with clear guidance
- `server.py`: path traversal validation for `case_dir` parameter against `VIZNOIR_DATA_DIR`
- `compositor.py`: removed dead `TYPE_CHECKING` import

### Security

- Path traversal prevention strengthened for `inspect_physics` case_dir parameter
- Branch protection: required reviews (CODEOWNERS), dismiss stale reviews, conversation resolution, enforce admins

## [0.5.0] - 2026-03-08

### Added

- **Science Storyteller Pipeline**: analyze → render → compose end-to-end workflow
- `analyze_data` MCP tool: VTK dataset insight extraction (field statistics, anomaly detection, physics context, cross-field analysis, governing equation suggestion)
- `compose_assets` MCP tool: multi-asset composition with 4 layout modes (story, grid, slides, video)
- `engine/analysis.py`: field classification, exact field mapping (OpenFOAM convention), correlation analysis, fitted equations
- `anim/latex.py`: LaTeX → SVG → PNG rendering with body:color:preamble cache (cold 217ms, warm 10ms)
- `anim/compositor.py`: story/grid/slides layout rendering + ffmpeg video export (RGBA → libx264 yuv420p)
- `anim/timeline.py`: scene sequencing with prefix-sum + bisect O(log n) lookup
- `anim/transitions.py`: fade_in, fade_out, dissolve, wipe transitions (Image.blend C-level)
- `anim/easing.py`: 17 easing functions (linear, ease_in/out_quad/cubic/sine/expo/circ/back/elastic/bounce)
- GitHub Pages deployment workflow (Astro landing page)
- Branch protection: force push/delete blocked, required status checks

### Changed

- Test count: 1134 → 1315+ (97% coverage local, ~82% CI)
- MCP tools: 18 → 21
- CI test count guard: 1120 → 1290

### Fixed

- PIL.Image type hint: `from PIL.Image import Image` in TYPE_CHECKING (module vs class)
- np.linalg.norm mypy: explicit `result: np.ndarray` annotation for Any return
- LaTeX SVG cache test: conditional on `LATEX_AVAILABLE` for CI without LaTeX

## [0.3.0] - 2026-03-07

### Changed

- README.md redesigned: 224 → 101 lines, benchmark-driven "proof first" structure
- README.ko.md: matching Korean translation
- Landing page: 9 components → 5 sections (Hero, Proof, Showcase, QuickStart, Footer)
- Removed: Architecture, Features, Stats, Comparison, PluginShowcase components
- New: Proof.astro (unified stats + comparison matrix)
- Showcase: 44 images → 6 curated picks in 2x3 grid
- QuickStart: absorbed PluginShowcase, 3-step install flow

## [0.2.0] - 2026-03-07

### Added

- 5 new MCP tools: `cinematic_render`, `compare`, `probe_timeseries`, `batch_render`, `preview_3d` (total: 18)
- 1 new MCP resource: `capabilities` (total: 11)
- Cinematic rendering engine: PCA auto-camera, PBR materials, SSAO, FXAA, 3-point lighting, 5 quality presets
- `compare` tool: side-by-side, overlay, and difference modes for comparing datasets
- `preview_3d` tool: glTF/glB export with interactive three.js viewer
- `batch_render` tool: render multiple fields/timesteps in one call
- `probe_timeseries` tool: extract field values at a point across all timesteps
- Per-block styling for multiblock datasets (`render_multiblock()`)
- meshio fallback reader for 50+ additional mesh formats
- 5 new VTK filters: SmoothMesh, ProbePoint, CleanPolyData, Shrink, Tube
- HTTP/SSE transport mode (`--transport sse|streamable-http`)
- MCP Tasks support: `animate`, `split_animate`, `execute_pipeline` as async background tasks (FastMCP 3.x, backward-compatible with 2.x)
- `pip install mcp-server-viznoir[tasks]` for FastMCP 3.x with MCP Tasks
- 8 path traversal security tests: symlink escape, null byte injection, prefix attack
- Dockerfile.cpu for CPU-only (OSMesa) deployment without GPU
- MkDocs Material API documentation site (16 pages)
- Thermal analysis workflow example (`examples/thermal_analysis.json`)
- JOSS paper draft (`paper/paper.md`)
- Structured logging framework (`VIZNOIR_LOG_LEVEL` env var)
- Custom exception hierarchy (`ViznoirError`, `FileFormatError`, etc.)
- Render window auto-regeneration (every 100 renders) to prevent GPU memory leaks
- Python 3.11/3.13 CI test matrix
- Codecov coverage reporting
- `smithery.yaml` for MCP registry registration
- Property-based testing with Hypothesis (11 fuzz tests for path traversal, colormaps, Pydantic models)
- SECURITY.md with responsible disclosure policy
- `.pre-commit-config.yaml` (ruff + mypy + pre-commit-hooks)
- OpenSSF Scorecard CI workflow
- PLY/OBJ/STL integration tests (real VTK I/O roundtrip)
- Troubleshooting guide (docs/troubleshooting.md, 10 common issues)
- CODE_OF_CONDUCT.md (Contributor Covenant v2.1)
- `__main__.py` for `python -m viznoir` support
- Blue to Red Rainbow and X Ray colormaps (16 → 18 colormaps)
- Colormap resource enhanced with field-type recommendations

### Changed

- Test count: 310 → 1134 (99% coverage)
- CI coverage threshold: 75% → 80%
- File format support: 26 → 50+ (via meshio fallback)
- CI matrix: Python 3.10/3.12 → 3.10/3.11/3.12/3.13

### Fixed

- postfx.py: narrow exception handling — catch specific VTK errors instead of bare `Exception`
- readers.py: narrow meshio fallback exception to avoid masking `MemoryError`/`KeyboardInterrupt`
- Contour: empty output guard with data range diagnostics
- Streamlines: auto seed points from dataset bounds
- Slice/clip: auto origin from dataset center
- Renderer: reject 0-point datasets in `_resolve_renderable`
- PNG extraction: O(n) byte-by-byte copy replaced with numpy bulk copy
- CI: lint/type check separated into parallel job for faster feedback
- CI: VTK headless test skip mechanism (3-layer defense: conftest set + `*_vtk.py` pattern + env var)

### Added (CI/CD & Quality)

- 5 quality gates: G1 ruff, G2 mypy strict, G3 pytest×4 Python, G4 coverage 75%+, G5 CodeQL+pip-audit
- `security.yml`: CodeQL analysis + pip-audit dependency scanning
- `pr-quality.yml`: auto-labeling by size (XS/S/M/L/XL) and file path
- `dependency-review.yml`: license + vulnerability check on PR dependencies
- `release-drafter.yml`: auto-generated release notes from PR labels
- `stale.yml`: auto-close inactive issues (60d) and PRs (30d)
- `auto-merge.yml`: auto-merge dependabot PRs after CI passes
- `welcome.yml`: welcome message for first-time contributors
- Branch protection: 4 required CI checks, dismiss stale reviews
- `.pre-commit-config.yaml`: ruff, mypy, gitleaks, trailing-whitespace
- `CODEOWNERS`: @kimimgo as default reviewer
- Contributor recognition tiers in CONTRIBUTING.md
- MCP protocol compliance test suite (14 tests)
- Mutation testing framework (mutmut) for test quality verification
- Module-level resource/prompt registration (no `main()` call required)
- Performance benchmark framework (`benchmarks/bench_render.py`)
- Social preview image (1280×640) for GitHub
- Launch posts: HN, Reddit (3 subs), Twitter, LinkedIn, Discord drafts
- Aerodynamics and structural FEA workflow examples
- sdist excludes non-source files (251MB → 192KB package size)
- Dependabot: github-actions ecosystem for automatic action version updates

## [0.1.0] - 2026-03-04

### Added

- 13 MCP tools: `inspect_data`, `render`, `slice`, `contour`, `clip`, `streamlines`, `plot_over_line`, `extract_stats`, `integrate_surface`, `animate`, `split_animate`, `pv_isosurface`, `execute_pipeline`
- 10 MCP resources: formats, filters, colormaps, cameras, case-presets, pipelines (CFD/FEA/split-animate), capabilities, version
- 3 MCP prompts for guided post-processing workflows
- Pipeline DSL with Pydantic models (`SourceDef`, `FilterStep`, `RenderDef`, `OutputDef`)
- VTK direct API engine — no ParaView installation required
- Headless GPU rendering via EGL (`VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow`)
- CPU fallback via OSMesa for non-GPU environments
- 26+ file format support (VTK, VTU, VTP, VTS, VTR, VTI, VTM, STL, OBJ, PLY, OpenFOAM, EnSight, CGNS, Exodus, XDMF, PVD, and more)
- Docker image with GPU EGL support for containerized deployment
- 310 pytest tests with async support (`asyncio_mode = "auto"`)
- CI pipeline: ruff lint + mypy type check + pytest (Python 3.10, 3.12)
- 14 built-in colormaps (plasma, turbo, viridis, inferno, jet, coolwarm, grayscale, etc.)
- Volume rendering support (`representation="volume"` via `vtkSmartVolumeMapper`)
- Automatic seed point generation for streamlines
- Auto-center origin for slice and clip operations
- Empty output guard with data range diagnostics for contour
- `_protect_stdout()` to shield MCP JSON-RPC stream from VTK C-level stdout pollution
- Path traversal prevention when `VIZNOIR_DATA_DIR` is set
- Landing page (Astro 5 + Tailwind) with interactive showcase gallery

[Unreleased]: https://github.com/kimimgo/viznoir/compare/v0.6.0...HEAD
[0.6.0]: https://github.com/kimimgo/viznoir/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/kimimgo/viznoir/compare/v0.3.0...v0.5.0
[0.3.0]: https://github.com/kimimgo/viznoir/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/kimimgo/viznoir/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/kimimgo/viznoir/releases/tag/v0.1.0
