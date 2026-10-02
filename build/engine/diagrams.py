"""The six module diagrams (M3, M7, M8, M15, M16, M18)."""
from .design import *  # noqa: F401,F403  (palette, fonts, primitives, helpers)


# --------------------------------------------------------------- M3 attributes
def diagram_attributes(num, module_title):
    s = Slide(name="diag-attributes")
    diagram_base(s, "MODULE %02d  \u00b7  %s" % (num, module_title.upper()),
                 "The Attributes of God: One Nature, Two Classes")
    # concentric rings
    s.add(Ellipse(1.25, 2.02, 4.6, 4.6, line=GOLD_D, line_w=0.9))
    s.add(Ellipse(2.0, 2.77, 3.1, 3.1, line=GOLD_D, line_w=0.9))
    s.add(Ellipse(2.6, 3.37, 1.9, 1.9, line=GOLD, line_w=1.6))
    s.add(Ellipse(2.83, 3.6, 1.44, 1.44, fill=NAVY_2))
    s.add(T(2.55, 3.77, 2.0, 1.1,
            [P(R("THE", font=SANS_L, size=8.5, bold=True, color=GOLD_L), align="center", after=1),
             P(R("DIVINE", font=SERIF, size=13, bold=True, color=WHITE), align="center", after=1),
             P(R("NATURE", font=SERIF, size=13, bold=True, color=WHITE), align="center")],
            anchor="middle"))
    # six communicable spokes (inner ring)
    spokes = [
        (3.55, 2.90, 0.0, 0.42, False, True, 3.495, 2.715, 2.80, 2.15, "Omniscience"),
        (4.416, 3.61, 0.364, 0.21, False, True, 4.837, 3.49, 4.142, 2.925, "Omnipotence"),
        (4.416, 4.82, 0.364, 0.21, False, False, 4.837, 5.04, 4.142, 5.375, "Holiness"),
        (3.55, 5.32, 0.0, 0.42, False, False, 3.495, 5.815, 2.80, 6.15, "Love"),
        (2.32, 4.82, 0.364, 0.21, True, False, 2.153, 5.04, 1.458, 5.375, "Faithfulness"),
        (2.32, 3.61, 0.364, 0.21, True, True, 2.153, 3.49, 1.458, 2.925, "Justice"),
    ]
    for lx, ly, lw, lh, fh, fv, dx, dy, tx, ty, name in spokes:
        s.add(Line(lx, ly, lw, lh, GOLD_D, 0.8, fh=fh, fv=fv))
        s.add(Ellipse(dx, dy, 0.11, 0.11, fill=GOLD_L))
        s.add(T(tx, ty, 1.5, 0.3, [P(R(name, font=SANS_L, size=8.8, bold=True, color=GOLD_L), align="center")]))
    # four incommunicable (outer ring)
    outer = [
        (5.121, 2.639, 4.326, 2.034, "Aseity"),
        (1.869, 2.639, 1.074, 2.034, "Eternity"),
        (1.869, 5.891, 1.074, 6.266, "Immutability"),
        (5.121, 5.891, 4.326, 6.266, "Omnipresence"),
    ]
    for dx, dy, tx, ty, name in outer:
        s.add(Ellipse(dx, dy, 0.11, 0.11, fill=GOLD))
        s.add(T(tx, ty, 1.7, 0.3, [P(R(name, font=SANS_L, size=8.8, bold=True, color=PLAT), align="center")]))
    s.add(T(0.95, 6.55, 5.3, 0.3,
            [P(R("Inner ring \u2014 communicable    \u00b7    Outer ring \u2014 incommunicable",
                 font=SANS_L, size=8.8, color=MUTED))]))
    # two panels (right)
    s.add(Box(7.0, 2.25, 5.433, 2.15, fill=NAVY_2, line=GOLD_D, line_w=0.9))
    s.add(Box(7.0, 2.25, 5.433, 0.04, fill=GOLD))
    s.add(T(7.24, 2.44, 4.953, 0.3, [P(R("INCOMMUNICABLE ATTRIBUTES", font=SANS_L, size=9.5, bold=True, color=GOLD_L))]))
    s.add(T(7.24, 2.82, 4.953, 1.5,
            [P(R("Shared with no creature \u2014 they distinguish God absolutely: aseity "
                 "(self-existence), eternity, immutability, omnipresence.", font=SANS, size=10.5, color=PLAT), leading=1.3),
             P(R("Psalm 90:2 \u00b7 1 Timothy 6:16 \u00b7 James 1:17", font=SANS, size=9.5, italic=True, color=MUTED), before=6)]))
    s.add(Box(7.0, 4.62, 5.433, 2.15, fill=NAVY_2, line=GOLD_D, line_w=0.9))
    s.add(Box(7.0, 4.62, 5.433, 0.04, fill=GOLD))
    s.add(T(7.24, 4.81, 4.953, 0.3, [P(R("COMMUNICABLE ATTRIBUTES", font=SANS_L, size=9.5, bold=True, color=GOLD_L))]))
    s.add(T(7.24, 5.19, 4.953, 1.5,
            [P(R("Manifest in creation and redemption, and reflected in creatures in a "
                 "limited degree: omniscience, omnipotence, holiness, love, faithfulness, "
                 "justice.", font=SANS, size=10.5, color=PLAT), leading=1.3),
             P(R("Isaiah 6:3 \u00b7 1 John 4:8 \u00b7 Psalm 8:5-8", font=SANS, size=9.5, italic=True, color=MUTED), before=6)]))
    ticks(s, current=num, dark=True, y=6.98)
    return s


# -------------------------------------------------------------- M7 christology
def diagram_christology(num, module_title):
    s = Slide(name="diag-christology")
    diagram_base(s, "MODULE %02d  \u00b7  %s" % (num, module_title.upper()),
                 "The Course of Christ: Incarnation to Present Session")
    s.add(Line(1.2, 4.0, 10.95, 0.0, GOLD, 1.6))
    nodes = [
        (0.39, "top", "1", "PRE-EXISTENCE", "the eternal Word", "John 1:1; Col. 1:17"),
        (2.58, "bot", "2", "INCARNATION", "the Word became flesh", "John 1:14; Phil. 2:6-8"),
        (4.77, "top", "3", "MINISTRY", "proclamation, miracles", "Luke 4:18; Mark 1:38"),
        (6.96, "bot", "4", "DEATH", "the substitutionary crucifixion", "Rom. 5:8; 1 Pet. 2:24"),
        (9.15, "top", "5", "RESURRECTION", "the firstfruits of the dead", "1 Cor. 15:20"),
        (11.34, "bot", "6", "ASCENSION & SESSION", "heavenly intercession", "Acts 1:9-11; Heb. 7:25"),
    ]
    for cx, pos, n, title, desc, ref in nodes:
        by = 2.10 if pos == "top" else 4.74
        cxx = cx + 0.81
        s.add(Line(cxx, 3.38 if pos == "top" else 4.0, 0.0, 0.62, GOLD_D, 0.9,
                   fv=(pos == "top")))
        s.add(Ellipse(cxx - 0.062, 3.938, 0.124, 0.124, fill=GOLD))
        s.add(Box(cx, by, 1.62, 1.16, fill=NAVY_2, line=GOLD_D, line_w=1.0))
        s.add(Box(cx, by if pos == "top" else by + 1.12, 1.62, 0.04, fill=GOLD))
        s.add(T(cx + 0.12, by + 0.10, 1.38, 0.98,
                [P(R(n, font=SERIF, size=12, bold=True, color=GOLD), after=1),
                 P(R(title, font=SANS_L, size=9.3, bold=True, color=GOLD_L), after=2),
                 P(R(desc, font=SERIF, size=9, italic=True, color=PLAT), leading=1.02, after=2),
                 P(R(ref, font=SANS, size=8.2, color=MUTED))]))
    s.add(T(1.2, 6.4, 11.0, 0.5,
            [P(R("The hypostatic union \u2014 one Person, two natures \u2014 grounds every "
                 "station: Christ acts as God and true man.", font=SERIF, size=11.5,
                 italic=True, color=PLAT), align="center")]))
    ticks(s, current=num, dark=True, y=6.98)
    return s


# -------------------------------------------------------------- M8 soteriology
def diagram_soteriology(num, module_title):
    s = Slide(name="diag-soteriology")
    diagram_base(s, "MODULE %02d  \u00b7  %s" % (num, module_title.upper()),
                 "The Order of Salvation: Redemption to Glorification")
    cards = [
        (0.731, "REDEMPTION", "bought back by a price", "Eph. 1:7"),
        (2.761, "RECONCILIATION", "enmity removed", "2 Cor. 5:18"),
        (4.791, "JUSTIFICATION", "declared righteous", "Rom. 5:1"),
        (6.821, "ADOPTION", "into the family of God", "Rom. 8:15"),
        (8.851, "SANCTIFICATION", "made holy in practice", "1 Thess. 5:23"),
        (10.881, "GLORIFICATION", "perfected in glory", "Rom. 8:30"),
    ]
    for cx, title, desc, ref in cards:
        s.add(Box(cx, 4.15, 1.72, 1.28, fill=NAVY_2, line=GOLD_D, line_w=1.0))
        s.add(Box(cx, 4.15, 1.72, 0.04, fill=GOLD))
        s.add(T(cx + 0.13, 4.27, 1.46, 1.08,
                [P(R(title, font=SANS_L, size=10, bold=True, color=GOLD_L), after=2),
                 P(R(desc, font=SERIF, size=9.3, italic=True, color=PLAT), leading=1.05, after=2),
                 P(R(ref, font=SANS, size=8.3, color=MUTED))]))
        if cx < 10.0:
            s.add(Line(cx + 1.74, 4.79, 0.27, 0.0, GOLD, 1.0))
    # banner + rule (drawn after cards, matching the deck's z-order)
    s.add(T(0.731, 2.35, 11.87, 0.60,
            [P(R("GRACE ALONE THROUGH FAITH \u2014 UNION WITH CHRIST", font=SANS_L, size=10.5,
                 bold=True, color=GOLD), align="center")]))
    s.add(Line(0.731, 3.10, 11.87, 0.0, GOLD_D, 1.0))
    s.add(T(0.731, 5.75, 11.87, 0.70,
            [P(R("Each work is distinct yet inseparable: one salvific act of the Triune God, "
                 "applied progressively to the believer.", font=SERIF, size=11.5, italic=True,
                 color=PLAT), align="center", leading=1.3)]))
    ticks(s, current=num, dark=True, y=6.98)
    return s


# --------------------------------------------------------- M15 church history
def diagram_church_history(num, module_title):
    s = Slide(name="diag-history")
    diagram_base(s, "MODULE %02d  \u00b7  %s" % (num, module_title.upper()),
                 "The Great Periods of Christian History")
    s.add(Line(1.15, 4.35, 11.05, 0.0, GOLD, 1.6))
    nodes = [
        (0.133, "top", "c. 30-100", "APOSTOLIC", "the apostolic church, the New Testament writings"),
        (2.343, "bot", "c. 100-500", "PATRISTIC", "Fathers, councils, the great creeds"),
        (4.553, "top", "c. 500-1500", "MEDIEVAL", "scholasticism, monasticism, the universities"),
        (6.763, "bot", "c. 1500-1650", "REFORMATION", "Luther, Calvin, Zwingli; confessions of faith"),
        (8.973, "top", "c. 1650-1900", "POST-REFORMATION", "Orthodoxy, Pietism, Enlightenment critique"),
        (11.183, "bot", "c. 1900-present", "MODERN & GLOBAL", "missions, ecumenism, postmodern theology"),
    ]
    for cx, pos, period, name, desc in nodes:
        cxx = cx + 1.015
        s.add(Line(cxx, 3.95 if pos == "top" else 4.35, 0.0, 0.40, GOLD_D, 0.9,
                   fv=(pos == "top")))
        s.add(Ellipse(cxx - 0.055, 4.29, 0.11, 0.11, fill=GOLD))
        cy = 2.60 if pos == "top" else 4.85
        s.add(Box(cx, cy, 2.033, 1.30, fill=NAVY_2, line=GOLD_D, line_w=0.9))
        s.add(Box(cx, cy if pos == "top" else cy + 1.26, 2.033, 0.04, fill=GOLD))
        s.add(T(cx + 0.10, cy + 0.10, 1.83, 1.12,
                [P(R(period, font=SANS_L, size=8.6, bold=True, color=MUTED), after=1),
                 P(R(name, font=SANS_L, size=9.6, bold=True, color=GOLD_L), leading=1.02, after=2),
                 P(R(desc, font=SERIF, size=8.8, italic=True, color=PLAT), leading=1.05)]))
    ticks(s, current=num, dark=True, y=6.98)
    return s


# ----------------------------------------------------------- M16 traditions
def diagram_traditions(num, module_title):
    s = Slide(name="diag-traditions")
    diagram_base(s, "MODULE %02d  \u00b7  %s" % (num, module_title.upper()),
                 "A Comparative Framework of Major Theological Traditions")
    cols = [
        (0.900, "REFORMED", [
            "Scripture, tradition, reason and experience in harmony under the magisterium's guidance.",
            "Faith formed by grace working with the sacraments as means of grace.",
            "Papal primacy with an episcopal, sacramental structure."]),
        (3.921, "ROMAN CATHOLIC", [
            "Scripture interpreted within the living tradition of the Church and the teaching office.",
            "Faith and works understood together; the seven sacraments as channels of grace.",
            "Succession from the apostles; the bishop of Rome as visible head."]),
        (6.941, "EASTERN ORTHODOX", [
            "Scripture and the conciliar tradition of the first seven ecumenical councils.",
            "Faith received through the mysteries (myst\u0113ria) of baptism, eucharist and church life.",
            "Conciliar governance; the patriarchal sees and the synodal tradition."]),
        (9.962, "EVANGELICAL / PENTECOSTAL", [
            "Scripture as the supreme authority (sola Scriptura) for faith and practice.",
            "Salvation by grace alone through faith alone; baptism and the Lord's supper as ordinances.",
            "Priesthood of all believers; congregational or connectional polity."]),
    ]
    for cx, header, rows in cols:
        s.add(Box(cx, 2.25, 2.471, 0.62, fill=BURGUNDY))
        s.add(T(cx + 0.16, 2.34, 2.151, 0.48,
                [P(R(header, font=SANS_L, size=10.5, bold=True, color=GOLD_L))]))
        for r, row in enumerate(rows):
            ry = 2.87 + r * 1.06
            s.add(Box(cx, ry, 2.471, 1.06, fill=NAVY_2, line=GOLD_D, line_w=0.8))
            s.add(T(cx + 0.16, ry + 0.09, 2.151, 0.90,
                    [P(R(row, font=SANS, size=9.6, color=PLAT), leading=1.14)]))
    s.add(T(0.90, 6.23, 11.533, 0.40,
            [P(R("Rows compare: scriptural authority  \u00b7  means of grace  \u00b7  "
                 "ecclesial structure. Presentations are idealised summaries "
                 "for academic comparison.", font=SANS, size=9, italic=True, color=MUTED), leading=1.2)]))
    ticks(s, current=num, dark=True, y=6.98)
    return s


# ------------------------------------------------------------ M18 research
def diagram_research(num, module_title):
    s = Slide(name="diag-research")
    diagram_base(s, "MODULE %02d  \u00b7  %s" % (num, module_title.upper()),
                 "The Process of Advanced Theological Research")
    row1 = [
        (0.90, "RESEARCH PROBLEM", "identify and frame a live theological question"),
        (4.22, "LITERATURE REVIEW", "map the field: Scripture, church, academy"),
        (7.54, "THEORETICAL FRAMEWORK", "define doctrine, method and assumptions"),
        (10.86, "METHODOLOGY", "exegesis, history, philosophy or empirical study"),
    ]
    row2 = [
        (0.90, "ANALYSIS & ARGUMENT", "weigh evidence; construct the thesis"),
        (4.22, "DRAFT & REVISION", "write, critique, refine through dialogue"),
        (7.54, "DEFENCE & PUBLICATION", "present the work to the academic community"),
    ]

    def card(cx, cy, title, desc):
        s.add(Box(cx, cy, 2.90, 1.06, fill=NAVY_2, line=GOLD_D, line_w=1.0))
        s.add(Box(cx, cy, 0.045, 1.06, fill=GOLD))
        s.add(T(cx + 0.22, cy + 0.12, 2.50, 0.86,
                [P(R(title, font=SANS_L, size=10.5, bold=True, color=GOLD_L), after=2),
                 P(R(desc, font=SANS, size=9.2, color=PLAT), leading=1.1)]))

    for i, (cx, title, desc) in enumerate(row1):
        card(cx, 2.50, title, desc)
        if i < len(row1) - 1:
            s.add(Line(cx + 2.94, 3.03, 0.34, 0.0, GOLD, 1.5))
    s.add(Line(12.31, 3.62, 0.0, 0.78, GOLD, 1.5))
    for (cx, title, desc) in row2:
        card(cx, 4.46, title, desc)
        s.add(Line(cx + 2.94, 4.99, 0.34, 0.0, GOLD, 1.5))
    # feedback loop
    s.add(Line(2.35, 5.64, 6.64, 0.0, GOLD_D, 1.0, fh=True))
    s.add(Line(2.35, 3.62, 0.0, 2.02, GOLD_D, 1.0, fv=True))
    s.add(T(2.55, 5.54, 4.60, 0.30,
            [P(R("revision loop: findings refine the research question",
                 font=SERIF, size=9, italic=True, color=MUTED))]))
    ticks(s, current=num, dark=True, y=6.98)
    return s


DIAGRAM_BUILDERS = {
    3: diagram_attributes,
    7: diagram_christology,
    8: diagram_soteriology,
    15: diagram_church_history,
    16: diagram_traditions,
    18: diagram_research,
}
