# Christian Theology — 18-Module Academic Curriculum

A university-level, eighteen-module academic programme tracing the Christian
faith from its foundations to advanced research.

## Contents

| File | What it is |
|------|-----------|
| `Christian_Theology_Curriculum.pptx` | The full deck — **306 slides**, 16:9. |
| `curriculum_full.json` | The structured content (18 modules / 220 numbered topics) that drives the deck. |

## Structure

- **Front matter** — title, course introduction (purpose / scope / approach),
  learning objectives, the theological-progression map, and a programme overview.
- **18 modules**, each with: a section divider, an introduction to the
  discipline, a sequence of numbered lecture topics (220 in total), — where
  appropriate — a diagram, and a module summary plus a transition to the next stage.
- **Closing** — a course review, the integration of the theological disciplines,
  a reflection with suggested research topics, and a final slide.

Module map:

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

## Provenance

This is a **reconstructed syllabus**: the module themes and the 1–220 topic
numbering follow the standard academic progression, but the detailed topic
titles and lecture content were authored for this engagement because the
official curriculum file was not supplied. The content is swappable — drop the
official file (docx/pdf/txt/md) into the build and run `ingest.py` to parse it
authoritatively and re-emit the deck without re-authoring.

## Quality control

The deck passes a render-based overflow audit: **0 text-overflow issues**
across all 306 slides (conservative DejaVu metrics, 160 px/in).
