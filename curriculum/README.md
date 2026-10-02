# Christian Theology — 18-Module Academic Curriculum

A reconstructed university-level academic programme tracing the Christian faith from its foundations to advanced research.

## Files

| File | What it is |
|------|-----------|
| `curriculum_full.json` | Structured source content: 18 modules and 220 numbered topics. |
| `../reconstructed/Christian_Theology_Curriculum.pptx` | Rebuilt, editable PowerPoint: 306 slides, 16:9. |
| `../content_audit.md` | Read-only first-pass audit findings; doctrinal wording was not changed. |

The original/reference PPTX, when present in this workspace as `Christian_Theology_Curriculum.pptx`, is left untouched. The rebuild writes to `reconstructed/` by default.

## Structure

- **Front matter** — title, course introduction (purpose / scope / approach), learning objectives, theological-progression map, and programme overview.
- **18 modules** — each has a divider, module introduction, numbered lecture topics, an optional diagram, a summary, and (except the last module) a transition.
- **Closing** — course review, integration of theological disciplines, reflection with suggested research topics, and final slide.

## Module map

1. Foundations of Christian Theology
2. The Bible: The Book of Theology
3. Theology Proper: The Doctrine of God
4. Creation, Providence and Angels
5. The Doctrine of Man
6. The Holy Spirit: The Doctrine of the Spirit
7. Christology: The Person and Work of Christ
8. Soteriology: The Doctrine of Salvation
9. Ecclesiology: The Doctrine of the Church
10. Eschatology: The Doctrine of Last Things
11. The Christian Life and Spiritual Formation
12. Christian Ethics
13. Missiology: The Mission of the Church
14. Theology and the Contemporary World
15. Church History
16. Advanced Christian Theology
17. Apologetics and Theology in Dialogue
18. Advanced Theological Research

## Provenance and scope

This is a **reconstructed syllabus**, not an official TBUGEUSA curriculum. The module themes and 1–220 numbering follow a standard academic progression; detailed titles and lecture content were authored for this engagement because the official curriculum file was not supplied. If an official source arrives, replace/update the JSON and rebuild rather than treating this reconstruction as authoritative.

Some content is explicitly or implicitly Reformed/evangelical, while other passages read as broadly Christian. See `../content_audit.md` for historical, citation, and tradition-framing issues identified in a read-only pass.

## Build and verification

From the repository root:

```bash
python -m pip install python-pptx Pillow
python -m build.engine.build
python -m build.engine.verify /path/to/reference.pptx reconstructed/Christian_Theology_Curriculum.pptx --tol 0.03
```

The build emits a 306-slide deck into `reconstructed/` and does not overwrite the reference PPTX.
