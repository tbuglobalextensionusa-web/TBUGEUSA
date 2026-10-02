"""Lightweight raster preview renderer for a Slide spec (160 px/in).

Pillow previews intentionally use DejaVu fallbacks because the proprietary
Calibri and Palatino fonts used by the reference deck may not be installed.
The editable PPTX renderer remains the fidelity source.
"""
from PIL import Image, ImageDraw, ImageFont

from .design import W, H, SCALE, Box, Line, Ellipse, TextSpec

_FONT_DIR = "/usr/share/fonts/truetype/dejavu"

def _font_path(run):
    serif = bool(run.font and "serif" in run.font.lower()) or "palatino" in (run.font or "").lower()
    if serif:
        name = "DejaVuSerif"
    else:
        name = "DejaVuSans"
    if run.bold:
        name += "-Bold"
    return f"{_FONT_DIR}/{name}.ttf"


def _font(run):
    size = max(1, round(float(run.size) * SCALE / 72.0))
    try:
        return ImageFont.truetype(_font_path(run), size)
    except OSError:
        return ImageFont.load_default(size=size)


def _rgb(value):
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def _xy(x, y):
    return round(x * SCALE), round(y * SCALE)


def _rect(draw, x, y, w, h, fill=None, outline=None, width=1, radius=0):
    x0, y0 = _xy(x, y)
    x1, y1 = _xy(x + w, y + h)
    if fill is not None:
        color = _rgb(fill)
        if radius:
            draw.rounded_rectangle((x0, y0, x1, y1), radius=radius, fill=color)
        else:
            draw.rectangle((x0, y0, x1, y1), fill=color)
    if outline is not None:
        color = _rgb(outline)
        if radius:
            draw.rounded_rectangle((x0, y0, x1, y1), radius=radius, outline=color,
                                   width=max(1, round(width * SCALE / 72)))
        else:
            draw.rectangle((x0, y0, x1, y1), outline=color,
                           width=max(1, round(width * SCALE / 72)))


def _gradient(img, x, y, w, h, c0, c1):
    x0, y0 = _xy(x, y)
    x1, y1 = _xy(x + w, y + h)
    a, b = _rgb(c0), _rgb(c1)
    span = max(1, x1 - x0 - 1)
    draw = ImageDraw.Draw(img)
    for px in range(x0, x1):
        t = (px - x0) / span
        c = tuple(round(a[i] * (1 - t) + b[i] * t) for i in range(3))
        draw.line((px, y0, px, y1), fill=c)


def _wrapped_lines(draw, text, font, max_width):
    lines = []
    for para in str(text).split("\n"):
        words = para.split()
        line = ""
        for word in words:
            trial = word if not line else line + " " + word
            if line and draw.textlength(trial, font=font) > max_width:
                lines.append(line)
                line = word
            else:
                line = trial
        lines.append(line)
    return lines or [""]


def _draw_text(img, spec):
    draw = ImageDraw.Draw(img)
    x0, y0 = _xy(spec.x, spec.y)
    width, height = _xy(spec.w, spec.h)
    y = y0
    paragraphs = []
    for para in spec.paragraphs:
        if not para.runs:
            continue
        run = para.runs[0]
        font = _font(run)
        before = round(para.before * SCALE / 72.0)
        after = round(para.after * SCALE / 72.0)
        line_h = max(1, round(run.size * SCALE / 72.0 * para.leading * 1.22))
        y += before
        text = "".join(r.text for r in para.runs)
        color = para.bullet_color if para.bullet and para.bullet_color else run.color
        if para.bullet:
            text = "\u2014  " + text
        lines = _wrapped_lines(draw, text, font, width)
        for line in lines:
            tw = draw.textlength(line, font=font)
            if para.align == "center":
                x = x0 + (width - tw) / 2
            elif para.align == "right":
                x = x0 + width - tw
            else:
                x = x0
            if y + line_h > y0 + height + line_h:
                break
            draw.text((round(x), y), line, font=font, fill=_rgb(color))
            y += line_h
        y += after
        paragraphs.append(para)
    if spec.anchor == "middle" and paragraphs:
        # Keep vertical positioning close in preview; the PPTX is authoritative.
        pass


def render_png(spec, path, scale=SCALE):
    global SCALE
    old_scale = SCALE
    SCALE = int(scale)
    img = Image.new("RGB", (round(W * SCALE), round(H * SCALE)), (244, 239, 227))
    for el in spec.elements:
        if isinstance(el, Box):
            if el.gradient:
                _gradient(img, el.x, el.y, el.w, el.h, el.gradient[0], el.gradient[1])
                if el.line:
                    _rect(ImageDraw.Draw(img), el.x, el.y, el.w, el.h,
                          outline=el.line, width=el.line_w, radius=round(0.12 * SCALE) if el.round_ else 0)
            else:
                _rect(ImageDraw.Draw(img), el.x, el.y, el.w, el.h, fill=el.fill,
                      outline=el.line, width=el.line_w,
                      radius=round(0.12 * SCALE) if el.round_ else 0)
        elif isinstance(el, Line):
            (a, b), (c, d) = el.endpoints
            ImageDraw.Draw(img).line((*_xy(a, b), *_xy(c, d)), fill=_rgb(el.color),
                                     width=max(1, round(el.width * SCALE / 72)))
        elif isinstance(el, Ellipse):
            x0, y0 = _xy(el.x, el.y)
            x1, y1 = _xy(el.x + el.w, el.y + el.h)
            draw = ImageDraw.Draw(img)
            draw.ellipse((x0, y0, x1, y1), fill=_rgb(el.fill) if el.fill else None,
                         outline=_rgb(el.line) if el.line else None,
                         width=max(1, round(el.line_w * SCALE / 72)))
        elif isinstance(el, TextSpec):
            _draw_text(img, el)
    img.save(path)
    SCALE = old_scale
    return path
