"""Design system: palette, fonts, and the slide-spec primitives.

A slide is a named collection of elements (Box / Line / Ellipse / TextSpec).
Both renderers (python-pptx and PIL) consume these specs, so the layout is
defined exactly once. All coordinates are inches; the slide is 13.333 x 7.5.
"""

# ---------------------------------------------------------------- palette ---
IVORY     = "F4EFE3"
PAPER     = "FBFAF4"
INK       = "232A38"
INK_SOFT  = "4C566B"
BURGUNDY  = "77212E"
GOLD      = "C9A45C"
GOLD_D    = "A67F3B"
GOLD_L    = "E6D3A3"
NAVY      = "122A4E"
MIDNIGHT  = "0B1526"
NAVY_2    = "1B3A66"
PLAT      = "C9CDD6"
MUTED     = "9AA5BC"
TICK_ON_D = "C9A45C"
TICK_OFF_D= "6E7A93"
TICK_ON_L = "77212E"
TICK_OFF_L= "A8AAAD"
LINE_L    = "D6D3CB"
LINE_OVER = "DAD7CE"
RULE_OBJ  = "D8D0BE"
WHITE     = "FFFFFF"

# ------------------------------------------------------------------ fonts ---
SERIF  = "Palatino Linotype"
SANS   = "Calibri"
SANS_L = "Calibri Light"

# --------------------------------------------------------------- geometry ---
W = 13.333
H = 7.5
MARGIN = 0.9
SCALE = 160            # px per inch (fit-check / preview baseline)


# ---------------------------------------------------------- spec primitives ---
class Box:
    """A (rounded) rectangle. Fill or a 2-stop horizontal gradient."""
    def __init__(self, x, y, w, h, fill=None, line=None, line_w=1.0,
                 gradient=None, round_=False):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.fill = fill
        self.line = line
        self.line_w = line_w
        self.gradient = gradient          # (c0, c1, angle_deg) or None
        self.round_ = round_


class Line:
    """A straight connector. (x, y) is the box origin; flips set the diagonal."""
    def __init__(self, x, y, w, h, color, width=1.0, fh=False, fv=False):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.color = color
        self.width = width
        self.fh, self.fv = fh, fv
    @property
    def endpoints(self):
        x, y, w, h = self.x, self.y, self.w, self.h
        if self.fh and self.fv:  return (x + w, y + h), (x, y)
        if self.fh:              return (x + w, y), (x, y + h)
        if self.fv:              return (x, y + h), (x + w, y)
        return (x, y), (x + w, y + h)


class Ellipse:
    def __init__(self, x, y, w, h, fill=None, line=None, line_w=1.0):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.fill = fill
        self.line = line
        self.line_w = line_w


class Run:
    def __init__(self, text, font=None, size=12, bold=False, italic=False,
                 color=INK):
        self.text = text
        self.font = font
        self.size = size
        self.bold = bold
        self.italic = italic
        self.color = color


class P:
    """A paragraph: a run or list of runs plus spacing / alignment / bullet."""
    def __init__(self, *runs, align="left", before=0, after=0, leading=1.0,
                 bullet=None, bullet_color=None):
        if len(runs) == 1 and isinstance(runs[0], (list, tuple)):
            runs = tuple(runs[0])
        self.runs = list(runs)
        self.align = align
        self.before = before
        self.after = after
        self.leading = leading
        self.bullet = bullet
        self.bullet_color = bullet_color


class TextSpec:
    def __init__(self, x, y, w, h, paragraphs, anchor="top", tag=None):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.paragraphs = (paragraphs if isinstance(paragraphs, (list, tuple))
                           else [paragraphs])
        self.anchor = anchor
        self.tag = tag


class Slide:
    def __init__(self, name=""):
        self.name = name
        self.elements = []
        self.bg = None          # solid background hex, or None
        self.bg_grad = None     # (top, bottom, angle)
    def add(self, el):
        self.elements.append(el)
        return el


# convenience aliases (match the historical authoring style)
T = TextSpec
R = Run


# --------------------------------------------------------------- helpers -----
def dark_bg(s, inverted=False):
    """Full-slide horizontal gradient rectangle (navy->midnight, ang=0)."""
    top, bottom = (MIDNIGHT, NAVY) if inverted else (NAVY, MIDNIGHT)
    s.add(Box(0, 0, W, H, gradient=(top, bottom, 0)))


def label_par(text, color, size):
    return P(R(text, font=SANS_L, size=size, bold=True, color=color))


def gold_rule(x, y, w, color=GOLD_D, width=1.0):
    return Line(x, y, w, 0.0, color, width)


def ticks(s, current, dark=True, y=6.72, x0=0.9):
    """Style A: 18 small ticks; the first `current` are lit. Dark/light palette."""
    on, off = (TICK_ON_D, TICK_OFF_D) if dark else (TICK_ON_L, TICK_OFF_L)
    for i in range(18):
        s.add(Box(x0 + i * 0.215, y, 0.16, 0.035,
                 fill=(on if i < current else off)))


def transition_ticks(s, target):
    """Style B: 18 wider ticks; modules 1..target-1 gold, module target
    gold-light, the rest dim. Used on the inter-module transition slides."""
    for i in range(18):
        col = (GOLD if i < target - 1 else
               GOLD_L if i == target - 1 else TICK_OFF_D)
        s.add(Box(2.969 + i * 0.415, 6.35, 0.34, 0.05, fill=col))


def diagram_head(s, label, title):
    """Common header for the dark diagram slides."""
    s.add(T(0.9, 0.78, 10.5, 0.3,
            [P(R(label, font=SANS_L, size=10, bold=True, color=GOLD_L))]))
    s.add(T(0.9, 1.12, 11.6, 0.7,
            [P(R(title, font=SERIF, size=24, bold=True, color=WHITE))]))
    s.add(Line(0.9, 1.86, 11.533, 0.0, GOLD_D, 1.0))


def diagram_base(s, label, title):
    """Dark gradient + frame + header, shared by all six diagrams."""
    dark_bg(s)
    s.add(Box(0.4, 0.4, 12.533, 6.7, line=GOLD_D, line_w=0.9))
    diagram_head(s, label, title)
    return s
