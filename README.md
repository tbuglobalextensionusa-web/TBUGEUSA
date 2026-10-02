# TBUGEUSA — Christian Theology Curriculum

This repository contains a **reconstructed**, university-level Christian theology curriculum and a reproducible PowerPoint build.

## Deliverables

- `reconstructed/Christian_Theology_Curriculum.pptx` — regenerated 306-slide deck. It is stored separately so a reference copy in `curriculum/` is never overwritten.
- `curriculum/curriculum_full.json` — source content for 18 modules and 220 numbered topics.
- `content_audit.md` — read-only first-pass content findings. No doctrinal edits were made during the audit.

The detailed topic content was reconstructed for this engagement because the official curriculum source was not supplied. It should not be represented as an official TBUGEUSA syllabus; see `curriculum/README.md` for provenance and scope.

## Rebuild

Requires Python 3.10+ with `python-pptx` and Pillow installed:

```bash
python -m pip install python-pptx Pillow
python -m build.engine.build
```

By default, the build writes to `reconstructed/` and **does not overwrite** the reference file in `curriculum/`. To choose another output directory:

```bash
python -m build.engine.build --out /path/to/output
```

To render lightweight PNG previews of selected 1-based slide numbers:

```bash
python -m build.engine.build --out /path/to/output --preview 1 8 56 304
```

To compare a rebuilt deck with an available reference deck (including positions, fills, outlines, normalized text, and paragraph/run styling):

```bash
python -m build.engine.verify /path/to/reference.pptx reconstructed/Christian_Theology_Curriculum.pptx --tol 0.03
```

The current rebuild has **306 slides** and verifies with no detected differences at 0.03-inch geometry tolerance against the reference available in the workspace.
