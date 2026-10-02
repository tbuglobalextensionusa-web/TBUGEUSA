"""Slide builders for the non-diagram layouts. Each returns a design.Slide."""
from .design import *  # noqa: F401,F403  (palette, fonts, primitives, helpers)
from .motifs import MOTIFS

_DIV_CAPTION = "Christian Theology \u00b7 A Comprehensive Academic Study"
# overview row y-positions (both columns share them)
_OVER_Y = [2.080, 2.665, 3.250, 3.835, 4.420, 5.005, 5.590, 6.175, 6.760]


# ---------------------------------------------------------------- front -----
def title_slide(title, subtitle, description, meta):
    s = Slide(name="title")
    dark_bg(s)
    s.add(Box(0.45, 0.45, 12.433, 6.6, line=GOLD, line_w=1.1))
    s.add(Box(0.56, 0.56, 12.213, 6.38, line=GOLD_D, line_w=0.4))
    s.add(T(0.9, 1.02, 11.533, 0.3,
            [P(R("UNIVERSITY-LEVEL THEOLOGICAL EDUCATION", font=SANS_L, size=10,
                 bold=True, color=GOLD_L))]))
    s.add(Line(6.116, 1.42, 0.35, 0.0, GOLD_D, 0.8))
    s.add(Line(6.866, 1.42, 0.35, 0.0, GOLD_D, 0.8))
    s.add(T(1.0, 2.05, 11.333, 1.35,
            [P(R(title, font=SERIF, size=56, bold=True, color=WHITE), align="center")]))
    s.add(Line(4.566, 3.62, 1.9, 0.0, GOLD, 1.1))
    s.add(Line(6.866, 3.62, 1.9, 0.0, GOLD, 1.1))
    s.add(Ellipse(6.626, 3.58, 0.08, 0.08, fill=GOLD))
    s.add(T(1.0, 3.86, 11.333, 0.5,
            [P(R(subtitle.upper(), font=SANS_L, size=15, bold=True, color=GOLD_L),
               align="center")]))
    s.add(T(2.4, 4.72, 8.533, 0.95,
            [P(R(description, font=SERIF, size=13, italic=True, color=PLAT),
               align="center", leading=1.4)]))
    s.add(T(0.9, 6.28, 11.533, 0.35,
            [P(R(meta, font=SANS_L, size=10, bold=True, color=MUTED), align="center")]))
    return s


def _light_head(s, label, title):
    s.bg = IVORY
    s.add(Box(0, 0, W, 0.14, fill=BURGUNDY))
    s.add(T(0.9, 0.62, 11.5, 0.3,
            [P(R(label, font=SANS_L, size=10, bold=True, color=GOLD_D))]))
    s.add(T(0.9, 1.0, 11.5, 0.7,
            [P(R(title, font=SERIF, size=26, bold=True, color=INK))]))
    s.add(Line(0.9, 1.78, 11.53, 0.0, GOLD_D, 1.0))


def front_purpose(purpose, approach, scope):
    s = Slide(name="front-purpose")
    _light_head(s, "COURSE INTRODUCTION", "Why Study Theology, and How This Course Proceeds")
    sections = [
        (2.08, GOLD, "ACADEMIC PURPOSE", purpose),
        (3.72, BURGUNDY, "METHOD & APPROACH", approach),
        (5.36, GOLD, "SCOPE OF STUDY", scope),
    ]
    for y, bar, head, body in sections:
        s.add(Box(0.9, y, 0.035, 1.42, fill=bar))
        s.add(T(1.18, y, 11.0, 0.28, [P(R(head, font=SANS_L, size=9, bold=True, color=BURGUNDY))]))
        s.add(T(1.18, y + 0.32, 11.0, 1.06,
                [P(R(body, font=SERIF, size=12.5, color=INK), leading=1.3)]))
    return s


def front_objectives(objectives):
    s = Slide(name="front-objectives")
    _light_head(s, "LEARNING OBJECTIVES", "What the Student Will Be Able to Do")
    for i, obj in enumerate(objectives):
        y = 2.17 + i * 0.83
        s.add(Box(0.9, y, 0.42, 0.42, fill=PAPER, line=GOLD_D, line_w=1.0))
        s.add(T(0.9, y, 0.42, 0.42, [P(R(str(i + 1), font=SERIF, size=15,
               bold=True, color=BURGUNDY), align="center")], anchor="middle"))
        s.add(T(1.55, y - 0.02, 10.8, 0.62,
                [P(R(obj, font=SANS, size=12.5, color=INK), leading=1.18)]))
        if i < len(objectives) - 1:
            s.add(Line(1.55, y + 0.62, 10.85, 0.0, RULE_OBJ, 0.5))
    return s


_PROG = [
    ("I", "Foundations", "the nature, sources and method of theology; the Bible as the rule of faith"),
    ("II", "Systematic Theology", "God, the Trinity, Christ, the Spirit, humanity, salvation, the Church and last things"),
    ("III", "Applied Theology", "the Christian life, ethics and the theology of the world's great questions"),
    ("IV", "Historical Theology", "the faith as confessed and lived from the apostles to the present"),
    ("V", "Advanced Theology", "apologetics, comparative traditions and the method of original research"),
]


def front_progress():
    s = Slide(name="front-progress")
    dark_bg(s)
    s.add(Box(0.4, 0.4, 12.533, 6.7, line=GOLD_D, line_w=0.9))
    s.add(T(0.9, 0.8, 11.5, 0.35,
            [P(R("THEOLOGICAL PROGRESSION", font=SANS_L, size=10.5, bold=True, color=GOLD_L))]))
    s.add(T(0.9, 1.2, 11.5, 0.7,
            [P(R("From Foundation to Advanced Research", font=SERIF, size=26, bold=True, color=WHITE))]))
    s.add(Line(0.9, 1.98, 11.53, 0.0, GOLD_D, 1.0))
    for i, (num, head, desc) in enumerate(_PROG):
        y = 2.40 + i * 0.97
        s.add(Ellipse(0.9, y, 0.78, 0.78, line=GOLD, line_w=1.2))
        s.add(T(0.9, y, 0.78, 0.78, [P(R(num, font=SERIF, size=20, bold=True,
               color=GOLD_L), align="center")], anchor="middle"))
        s.add(T(2.0, y + 0.02, 10.2, 0.35,
                [P(R(head, font=SANS_L, size=13, bold=True, color=WHITE))]))
        s.add(T(2.0, y + 0.40, 10.2, 0.35,
                [P(R(desc, font=SANS, size=10, color=MUTED))]))
        if i < len(_PROG) - 1:
            s.add(Line(1.29, y + 0.78, 0.0, 0.19, GOLD_D, 1.0))
    return s


def overview_slide(modules):
    s = Slide(name="overview")
    s.bg = IVORY
    s.add(Box(0, 0, W, 0.14, fill=BURGUNDY))
    s.add(Line(0.9, 0.62, 11.533, 0.0, GOLD_D, 1.0))
    s.add(T(0.9, 0.78, 11.533, 0.3,
            [P(R("COURSE OVERVIEW", font=SANS_L, size=10, bold=True, color=GOLD_D))]))
    s.add(T(0.9, 1.1, 11.533, 0.6,
            [P(R("The Structure of the Programme", font=SERIF, size=27, bold=True, color=INK))]))
    for i, m in enumerate(modules):
        col = 0 if i < 9 else 1
        row = i % 9
        x = 0.9 if col == 0 else 7.016
        colw = 5.066 if col == 0 else 5.067
        y = _OVER_Y[row]
        s.add(Box(x, y, 0.022, 0.30, fill=GOLD_D))
        s.add(T(x + 0.18, y - 0.13, 0.62, 0.585,
                [P(R("%02d" % m["number"], font=SERIF, size=15, bold=True, color=BURGUNDY))]))
        s.add(T(x + 0.85, y - 0.13, 4.316, 0.585,
                [P(R(m["title"], font=SANS, size=11, color=INK), leading=1.05)]))
        if row < 8:
            s.add(Line(x, y + 0.41, colw, 0.0, LINE_OVER, 0.5))
    return s


# ---------------------------------------------------------- module parts -----
def _divider_motif(s, num):
    for el in MOTIFS.get(num, MOTIFS[1]):
        s.add(el)


def divider_slide(num, title, intro, motif=1):
    s = Slide(name="divider-%02d" % num)
    dark_bg(s)
    s.add(Box(0.4, 0.4, 12.533, 6.7, line=GOLD_D, line_w=0.9))
    _divider_motif(s, num)
    s.add(Line(8.35, 1.7, 0.0, 3.9, GOLD_D, 0.8))
    s.add(T(0.9, 1.28, 7.2, 0.35,
            [P(R("MODULE %02d" % num, font=SANS_L, size=11.5, bold=True, color=GOLD))]))
    s.add(T(0.84, 1.62, 7.0, 2.5,
            [P(R("%02d" % num, font=SERIF, size=132, bold=True, color=GOLD))]))
    s.add(T(0.9, 4.28, 7.2, 1.05,
            [P(R(title.upper(), font=SERIF, size=27, bold=True, color=WHITE), leading=1.08)]))
    s.add(Line(0.9, 5.42, 1.15, 0.0, GOLD, 1.2))
    s.add(T(0.9, 5.62, 7.1, 0.95,
            [P(R(intro, font=SERIF, size=12.5, italic=True, color=GOLD_L), leading=1.3)]))
    ticks(s, current=num, dark=True, y=6.72)
    s.add(T(6.933, 6.68, 5.5, 0.3,
            [P(R(_DIV_CAPTION, font=SANS_L, size=8.5, bold=True, color=TICK_OFF_D),
               align="right")]))
    return s


def intro_slide(num, title, discipline, context, relevance, focus):
    s = Slide(name="intro-%02d" % num)
    s.bg = IVORY
    s.add(Box(0, 0, 3.35, H, fill=BURGUNDY))
    s.add(Box(3.35, 0, 0.035, H, fill=GOLD))
    s.add(T(0.55, 0.85, 2.5, 0.3,
            [P(R("MODULE", font=SANS_L, size=9.5, bold=True, color=GOLD_L))]))
    s.add(T(0.5, 1.25, 2.6, 1.6,
            [P(R("%02d" % num, font=SERIF, size=84, bold=True, color=GOLD_L))]))
    s.add(Line(0.55, 2.72, 0.9, 0.0, GOLD, 1.2))
    s.add(T(0.55, 2.95, 2.55, 2.2,
            [P(R(title.upper(), font=SERIF, size=15.5, bold=True, color=WHITE), leading=1.15)]))
    ticks(s, current=num, dark=False, y=6.85, x0=0.55)
    s.add(T(3.95, 0.82, 8.483, 0.3,
            [P(R("INTRODUCTION TO THIS MODULE", font=SANS_L, size=10, bold=True, color=GOLD_D))]))
    s.add(T(3.95, 1.16, 8.483, 1.0,
            [P(R(title, font=SERIF, size=24, bold=True, color=INK), leading=1.04)]))
    s.add(Line(3.95, 2.28, 8.483, 0.0, GOLD_D, 0.8))
    for y, head, body in [
        (2.60, "THE DISCIPLINE", discipline),
        (3.64, "BIBLICAL & HISTORICAL CONTEXT", context),
        (4.68, "RELEVANCE TO CHRISTIAN THEOLOGY", relevance),
    ]:
        s.add(T(3.95, y, 8.483, 0.28, [P(R(head, font=SANS_L, size=9, bold=True, color=BURGUNDY))]))
        s.add(T(3.95, y + 0.30, 8.483, 0.72,
                [P(R(body, font=SANS, size=11.2, color=INK_SOFT), leading=1.18)]))
    s.add(Box(3.95, 5.74, 8.483, 1.22, fill=PAPER, line=LINE_L, line_w=0.75))
    s.add(Box(3.95, 5.74, 0.04, 1.22, fill=BURGUNDY))
    s.add(T(4.25, 5.92, 7.883, 0.3, [P(R("LEARNING FOCUS", font=SANS_L, size=9, bold=True, color=BURGUNDY))]))
    s.add(T(4.25, 6.24, 7.883, 0.62,
            [P(R(focus, font=SERIF, size=12, italic=True, color=INK), leading=1.22)]))
    return s


def lecture_slide(mod, num, topic):
    title = topic["title"]
    expl = topic.get("explanation", "")
    concepts = topic.get("concepts", [])
    refs = topic.get("references", [])
    context = topic.get("context", "")
    takeaway = topic.get("takeaway", "")
    s = Slide(name="lec-%03d" % num)
    s.bg = IVORY
    s.add(T(0.9, 0.52, 10.0, 0.3,
            [P(R("MODULE %02d  \u00b7  LECTURE TOPIC" % mod, font=SANS_L, size=9.5, bold=True, color=GOLD_D))]))
    s.add(T(0.9, 0.84, 11.1, 0.82,
            [P(R(title, font=SERIF, size=23, bold=True, color=INK), leading=1.02)]))
    s.add(Box(12.28, 0.55, 0.62, 0.62, fill=PAPER, line=GOLD_D, line_w=1.0))
    s.add(T(12.28, 0.55, 0.62, 0.62,
            [P(R("%03d" % num, font=SERIF, size=15, bold=True, color=BURGUNDY), align="center")],
            anchor="middle"))
    s.add(Line(0.9, 1.72, 11.533, 0.0, GOLD_D, 1.0))
    s.add(Box(0.9, 1.98, 0.035, 4.42, fill=GOLD))
    s.add(T(1.18, 2.02, 7.05, 4.42,
            [P(R(expl, font=SERIF, size=13, color=INK), leading=1.34)]))
    px, pw = 8.72, 3.713
    s.add(Box(px, 1.98, pw, 2.26, fill=PAPER, line=LINE_L, line_w=0.75))
    s.add(Box(px, 1.98, pw, 0.045, fill=GOLD))
    s.add(T(px + 0.26, 2.16, pw - 0.5, 0.3, [P(R("KEY CONCEPTS", font=SANS_L, size=9, bold=True, color=BURGUNDY))]))
    paras = [P(R(c, font=SANS, size=10, color=INK_SOFT), bullet="\u2014",
               bullet_color=GOLD_D, after=4, leading=1.1) for c in concepts]
    s.add(T(px + 0.26, 2.5, pw - 0.5, 1.68, paras))
    s.add(Box(px, 4.34, pw, 2.2, fill=PAPER, line=LINE_L, line_w=0.75))
    s.add(Box(px, 4.34, pw, 0.045, fill=BURGUNDY))
    s.add(T(px + 0.26, 4.52, pw - 0.5, 0.3, [P(R("SCRIPTURE & CONTEXT", font=SANS_L, size=9, bold=True, color=BURGUNDY))]))
    paras = [P(R(r, font=SANS, size=10, italic=True, color=INK), after=2.5, leading=1.08) for r in refs]
    if context:
        paras.append(P(R(context, font=SANS, size=9.5, color=INK_SOFT), before=4, leading=1.1))
    s.add(T(px + 0.26, 4.86, pw - 0.5, 1.6, paras))
    s.add(Box(0.9, 6.62, 11.533, 0.02, fill=GOLD_D))
    s.add(T(0.95, 6.82, 1.35, 0.3, [P(R("TAKEAWAY", font=SANS_L, size=9, bold=True, color=BURGUNDY))]))
    s.add(T(2.4, 6.79, 9.933, 0.42,
            [P(R(takeaway, font=SANS, size=11.5, bold=True, color=INK), leading=1.05)]))
    ticks(s, current=mod, dark=False, y=7.18)
    return s


def summary_slide(num, title, ideas, connections, progression, next_mod=None):
    s = Slide(name="summary-%02d" % num)
    s.bg = IVORY
    s.add(Box(0, 0, W, 0.14, fill=BURGUNDY))
    s.add(T(0.9, 0.62, 10.5, 0.3,
            [P(R("MODULE %02d  \u00b7  SUMMARY" % num, font=SANS_L, size=10, bold=True, color=GOLD_D))]))
    s.add(T(0.9, 0.96, 11.5, 0.7,
            [P(R("Consolidating " + title, font=SERIF, size=25, bold=True, color=INK))]))
    s.add(Line(0.9, 1.74, 11.533, 0.0, GOLD_D, 1.0))
    s.add(T(0.9, 2.05, 6.4, 0.3, [P(R("MAJOR THEOLOGICAL IDEAS", font=SANS_L, size=9.5, bold=True, color=BURGUNDY))]))
    paras = [P(R(i, font=SANS, size=11.5, color=INK), bullet="\u2014",
               bullet_color=GOLD_D, after=7, leading=1.2) for i in ideas]
    s.add(T(0.9, 2.42, 6.45, 4.2, paras))
    s.add(Box(8.05, 2.05, 4.383, 2.35, fill=PAPER, line=LINE_L, line_w=0.75))
    s.add(Box(8.05, 2.05, 4.383, 0.045, fill=GOLD))
    s.add(T(8.31, 2.26, 3.883, 0.3, [P(R("KEY CONNECTIONS", font=SANS_L, size=9, bold=True, color=BURGUNDY))]))
    s.add(T(8.31, 2.62, 3.883, 1.6,
            [P(R(connections, font=SANS, size=11, color=INK_SOFT), leading=1.25)]))
    s.add(Box(8.05, 4.62, 4.383, 2.0, fill=BURGUNDY))
    s.add(Box(8.05, 4.62, 4.383, 0.045, fill=GOLD))
    s.add(T(8.31, 4.84, 3.883, 0.3, [P(R("ACADEMIC PROGRESSION", font=SANS_L, size=9, bold=True, color=GOLD_L))]))
    s.add(T(8.31, 5.14, 3.863, 0.92,
            [P(R(progression, font=SANS, size=10.6, color=IVORY), leading=1.2)]))
    if next_mod is not None:
        s.add(T(8.31, 6.14, 3.883, 0.4,
                [P(R("NEXT  \u2192  MODULE %02d \u00b7 %s" % (next_mod["number"], next_mod["title"]),
                     font=SANS_L, size=8.6, bold=True, color=GOLD_L), leading=1.12)]))
    ticks(s, current=num, dark=False, y=7.08)
    return s


def transition_slide(next_mod, progression):
    s = Slide(name="trans-%02d" % next_mod["number"])
    dark_bg(s, inverted=True)
    s.add(Line(6.666, 0.75, 0.0, 0.8, GOLD_D, 1.0))
    s.add(Ellipse(6.631, 1.585, 0.07, 0.07, fill=GOLD))
    s.add(T(0.9, 2.0, 11.533, 0.35,
            [P(R("PROCEEDING TO THE NEXT MODULE", font=SANS_L, size=10, bold=True, color=MUTED), align="center")]))
    s.add(T(0.9, 2.5, 11.533, 0.9,
            [P(R("MODULE %02d" % next_mod["number"], font=SERIF, size=38, bold=True, color=GOLD), align="center")]))
    s.add(T(0.9, 3.55, 11.533, 0.85,
            [P(R(next_mod["title"].upper(), font=SERIF, size=21, bold=True, color=WHITE),
               align="center", leading=1.1)]))
    s.add(Line(5.666, 4.62, 0.85, 0.0, GOLD_D, 0.9))
    s.add(Line(6.816, 4.62, 0.85, 0.0, GOLD_D, 0.9))
    s.add(T(2.6, 4.95, 8.133, 0.9,
            [P(R(progression, font=SERIF, size=12.5, italic=True, color=PLAT), align="center", leading=1.35)]))
    transition_ticks(s, target=next_mod["number"])
    return s


# ---------------------------------------------------------------- close -----
def close_head(s, title, title_y, rule_y):
    s.bg = None
    dark_bg(s)
    s.add(Box(0.4, 0.4, 12.533, 6.7, line=GOLD_D, line_w=0.9))
    s.add(T(0.9, 0.85, 11.533, 0.35,
            [P(R("COURSE CONCLUSION", font=SANS_L, size=10.5, bold=True, color=GOLD_L))]))
    s.add(T(0.9, title_y, 11.533, 0.7,
            [P(R(title, font=SERIF, size=26, bold=True, color=WHITE))]))
    s.add(Line(0.9, rule_y, 11.533, 0.0, GOLD_D, 1.0))


def close_review(bands, modules):
    s = Slide(name="close-review")
    close_head(s, "Comprehensive Review of the Theological Curriculum", 1.25, 2.05)
    xs = [0.900, 3.277, 5.653, 8.030, 10.406]
    for x, (name, desc, mods) in zip(xs, bands):
        s.add(Box(x, 2.5, 2.027, 3.5, fill=NAVY_2, line=GOLD_D, line_w=0.8))
        s.add(Box(x, 2.5, 2.027, 0.045, fill=GOLD))
        s.add(T(x + 0.25, 2.78, 1.527, 0.62,
                [P(R(name, font=SANS_L, size=10.5, bold=True, color=GOLD_L), leading=1.15)]))
        s.add(T(x + 0.25, 3.5, 1.527, 1.85,
                [P(R(desc, font=SANS, size=10, color=PLAT), leading=1.25)]))
        s.add(T(x + 0.25, 5.5, 1.527, 0.35, [P(R(mods, font=SANS_L, size=8.5, bold=True, color=MUTED))]))
    ticks(s, current=18, dark=True, y=6.75)
    return s


def close_integration():
    s = Slide(name="close-integration")
    close_head(s, "The Integration of the Theological Disciplines", 1.22, 2.0)
    rows = [
        (2.42, "BIBLICAL THEOLOGY", "the Scriptures as the norm of all doctrine"),
        (3.26, "SYSTEMATIC THEOLOGY", "doctrine ordered into coherent dogmatics"),
        (4.10, "HISTORICAL THEOLOGY", "the faith as confessed across the centuries"),
        (4.94, "PRACTICAL THEOLOGY", "doctrine embodied in life and ministry"),
        (5.78, "ADVANCED THEOLOGY", "critique, context and original research"),
    ]
    for y, name, desc in rows:
        s.add(Box(1.2, y, 5.7, 0.64, fill=NAVY_2, line=GOLD_D, line_w=0.9))
        s.add(Box(1.2, y, 0.045, 0.64, fill=GOLD))
        s.add(T(1.5, y + 0.09, 5.15, 0.48,
                [P(R(name, font=SANS_L, size=10.5, bold=True, color=GOLD_L), after=1),
                 P(R(desc, font=SERIF, size=9.5, italic=True, color=PLAT))]))
    # connectors + dots to the hub
    for (cx, cy, cw, ch), dy in [
        ((7.02, 2.74, 2.75, 1.35), 2.70), ((7.02, 3.58, 2.668, 0.725), 3.54),
        ((7.02, 4.42, 2.628, 0.137), 4.38), ((7.02, 4.818, 2.643, 0.442), 5.22),
        ((7.02, 5.054, 2.707, 1.046), 6.06)]:
        s.add(Line(cx, cy, cw, ch, GOLD_D, 1.0))
        s.add(Ellipse(6.98, dy, 0.08, 0.08, fill=GOLD))
    # hub: three concentric ellipses + label
    s.add(Ellipse(9.45, 3.22, 2.8, 2.8, line=GOLD_D, line_w=0.9))
    s.add(Ellipse(9.67, 3.44, 2.36, 2.36, line=GOLD, line_w=1.6))
    s.add(Ellipse(9.87, 3.64, 1.96, 1.96, fill=NAVY_2))
    s.add(T(9.8, 4.07, 2.1, 1.1,
            [P(R("THE", font=SANS_L, size=9, bold=True, color=GOLD_L), align="center", after=1),
             P(R("CHRISTIAN", font=SERIF, size=13.5, bold=True, color=WHITE), align="center", after=1),
             P(R("FAITH", font=SERIF, size=13.5, bold=True, color=WHITE), align="center")],
            anchor="middle"))
    s.add(T(6.2, 6.62, 6.2, 0.6,
            [P(R("Every discipline converges on the person and work of Christ \u2014 the centre "
                 "of the Christian faith.", font=SERIF, size=11,
                 italic=True, color=MUTED), align="right", leading=1.3)]))
    return s


def close_reflection(reflection, research):
    s = Slide(name="close-reflection")
    s.bg = IVORY
    s.add(Box(0, 0, W, 0.14, fill=BURGUNDY))
    s.add(T(0.9, 0.66, 10.5, 0.3, [P(R("COURSE CONCLUSION", font=SANS_L, size=10, bold=True, color=GOLD_D))]))
    s.add(T(0.9, 1.0, 11.533, 0.7,
            [P(R("Final Reflection and Paths of Further Study", font=SERIF, size=25, bold=True, color=INK))]))
    s.add(Line(0.9, 1.78, 11.533, 0.0, GOLD_D, 1.0))
    s.add(Box(0.9, 2.1, 0.035, 1.55, fill=GOLD))
    s.add(T(1.18, 2.14, 11.033, 1.6, [P(R(reflection, font=SERIF, size=13.5, color=INK), leading=1.4)]))
    s.add(T(0.9, 3.95, 6.3, 0.3, [P(R("SUGGESTED RESEARCH DIRECTIONS", font=SANS_L, size=9.5, bold=True, color=BURGUNDY))]))
    ys = [4.44, 5.06, 5.68, 6.30]
    for i, item in enumerate(research):
        col = 0 if i < 4 else 1
        row = i % 4
        x = 0.9 if col == 0 else 6.916
        y = ys[row]
        s.add(Box(x, y, 0.022, 0.3, fill=GOLD_D))
        s.add(T(x + 0.2, y - 0.09, 5.216, 0.6, [P(R(item, font=SANS, size=11.3, color=INK_SOFT), leading=1.12)]))
    ticks(s, current=18, dark=False, y=7.12)
    return s


def close_final():
    s = Slide(name="close-final")
    dark_bg(s)
    s.add(Box(0.45, 0.45, 12.433, 6.6, line=GOLD, line_w=1.1))
    s.add(Box(0.56, 0.56, 12.213, 6.38, line=GOLD_D, line_w=0.4))
    s.add(T(0.9, 1.5, 11.533, 0.4,
            [P(R("THE END OF THE CURRICULUM", font=SANS_L, size=10.5, bold=True, color=GOLD_L))]))
    s.add(Line(5.916, 2.05, 0.55, 0.0, GOLD_D, 0.9))
    s.add(Line(6.866, 2.05, 0.55, 0.0, GOLD_D, 0.9))
    s.add(T(1.0, 2.6, 11.333, 1.3,
            [P(R("CHRISTIAN THEOLOGY", font=SERIF, size=48, bold=True, color=WHITE), align="center")]))
    s.add(T(1.0, 3.95, 11.333, 0.5,
            [P(R("A COMPREHENSIVE ACADEMIC STUDY", font=SANS_L, size=13.5, bold=True, color=GOLD_L), align="center")]))
    s.add(Ellipse(6.626, 4.71, 0.08, 0.08, fill=GOLD))
    s.add(T(1.0, 5.15, 11.333, 0.4,
            [P(R("Eighteen Modules  \u00b7  Two Hundred and Twenty Lecture Topics", font=SERIF, size=12.5, italic=True, color=PLAT), align="center")]))
    s.add(T(1.0, 6.15, 11.333, 0.4,
            [P(R("Soli Deo Gloria", font=SERIF, size=13, italic=True, color=GOLD_L), align="center")]))
    return s
