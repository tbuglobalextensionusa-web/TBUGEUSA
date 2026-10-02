"""Assemble the full deck from the curriculum JSON and render to PPTX."""
import argparse
import json
import os

from . import pptx_render
from .templates import (title_slide, front_purpose, front_objectives, front_progress,
                        overview_slide, divider_slide, intro_slide, lecture_slide,
                        summary_slide, transition_slide, close_review, close_integration,
                        close_reflection, close_final)
from .diagrams import DIAGRAM_BUILDERS

REVIEW_BANDS = [
    ("FOUNDATIONS",
     "The nature and sources of theology; the formation, inspiration and "
     "authority of the Bible.", "Modules 1\u20132"),
    ("SYSTEMATIC DOCTRINES",
     "God and the Trinity, creation and providence, humanity and sin, the "
     "Spirit, Christ, salvation, the Church, last things.", "Modules 3\u201310"),
    ("THE CHRISTIAN LIFE",
     "Spiritual formation and ethics, the mission of the Church, the theology "
     "of the contemporary world.", "Modules 11\u201314"),
    ("HISTORY & CONTEXT",
     "The development of the faith across two millennia; the church in society "
     "and culture.", "Module 15"),
    ("ADVANCED STUDY",
     "Apologetics, comparative traditions, theology and modernity, original "
     "research.", "Modules 16\u201318"),
]

REFLECTION_TEXT = (
    "This programme has carried us from the threshold question \u2014 what is "
    "theology? \u2014 through the great doctrines of the Christian faith, its "
    "history, its practical expression, and finally to the methods of original "
    "research. The student who completes all eighteen modules possesses not a "
    "catalogue of propositions but a living, ordered, defensible understanding "
    "of the faith once delivered to the saints.")

RESEARCH_DIRECTIONS = [
    "The relationship of natural theology and revealed theology in the modern university",
    "Historical Christology: the development of the doctrine from Nicaea to Chalcedon",
    "The doctrine of the Trinity in the early Church fathers and in contemporary theology",
    "Soteriology in the different Christian traditions: an objective comparison",
    "The Church and society: theological perspectives on public life",
    "A critical survey of one major modern or contemporary theologian",
    "Theology and the sciences: historical conflicts and current conversation",
    "The formation of the New Testament canon in the early church",
]


def build_slides(data):
    slides = []
    slides.append(title_slide(data["course_title"], data["subtitle"],
                              data["description"], data["meta"]))
    intro0 = data["introduction"]
    slides.append(front_purpose(intro0["purpose"], intro0["approach"],
                                intro0["scope"]))
    slides.append(front_objectives(intro0["objectives"]))
    slides.append(front_progress())
    modules = data["modules"]
    slides.append(overview_slide(modules))
    for i, m in enumerate(modules):
        num = m["number"]
        mi = m["intro"]
        slides.append(divider_slide(num, m["title"], m["divider_intro"],
                                    m.get("motif", 1)))
        slides.append(intro_slide(num, m["title"], mi["discipline"], mi["context"],
                                  mi["relevance"], mi["focus"]))
        for topic in m["topics"]:
            slides.append(lecture_slide(num, topic["num"], topic))
        if num in DIAGRAM_BUILDERS:
            slides.append(DIAGRAM_BUILDERS[num](num, m["title"]))
        summ = m["summary"]
        next_mod = modules[i + 1] if i + 1 < len(modules) else None
        slides.append(summary_slide(num, m["title"], summ["ideas"],
                                    summ["connections"], summ["progression"],
                                    next_mod))
        if i + 1 < len(modules):
            slides.append(transition_slide(modules[i + 1], summ["progression"]))
    slides.append(close_review(REVIEW_BANDS, modules))
    slides.append(close_integration())
    slides.append(close_reflection(REFLECTION_TEXT, RESEARCH_DIRECTIONS))
    slides.append(close_final())
    return slides


def _default_paths():
    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.abspath(os.path.join(here, "..", ".."))
    cur = os.path.join(repo, "curriculum")
    # Never overwrite the supplied/reference deck in curriculum/ by default.
    out = os.path.join(repo, "reconstructed")
    return out, os.path.join(cur, "curriculum_full.json")


def main(argv=None):
    cur_default, data_default = _default_paths()
    ap = argparse.ArgumentParser(description="Build the Christian Theology deck.")
    ap.add_argument("--data", default=data_default)
    ap.add_argument("--out", default=cur_default, help="output directory")
    ap.add_argument("--pptx", default="Christian_Theology_Curriculum.pptx")
    ap.add_argument("--preview", nargs="*", default=None,
                    help="render sample slides (1-based index) to PNG in --out")
    args = ap.parse_args(argv)

    with open(args.data, encoding="utf-8") as fh:
        data = json.load(fh)
    slides = build_slides(data)

    os.makedirs(args.out, exist_ok=True)
    prs = pptx_render.new_presentation()
    pptx_render.render(prs, slides)
    outp = os.path.join(args.out, args.pptx)
    prs.save(outp)
    print("wrote: %s %d bytes (%d slides)" % (outp, os.path.getsize(outp), len(slides)))

    if args.preview:
        from . import pil_render
        for idx in args.preview:
            i = int(idx)
            p = os.path.join(args.out, "%03d_%s.png" % (i, slides[i - 1].name))
            pil_render.render_png(slides[i - 1], p)
            print("preview: %s" % p)
    return outp


if __name__ == "__main__":
    main()
