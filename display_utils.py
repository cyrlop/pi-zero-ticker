from PIL import ImageFont
from font_fredoka_one import FredokaOne


def draw_text(display, draw, message, font_size=24, y_align="middle"):
    """Get yfinance ticker object from a symbol

    Args:
        display (Inky): Inky display object
        draw (ImageDraw): ImageDraw object
        message (str): Texr message to display
        font_size (int): Font size
        y_align (str): Y alignment of message: "middle", "top" or "bottom"
    Returns:
        draw (ImageDraw): Updated ImageDraw object
    """
    font = ImageFont.truetype(FredokaOne, font_size)
    w, h = font.getsize(message)

    x = (display.WIDTH / 2) - (w / 2)

    if y_align == "middle":
        y = (display.HEIGHT / 2) - (h / 2)
    elif y_align == "top":
        y = 0
    elif y_align == "bottom":
        y = display.HEIGHT - h
    else:
        raise Exception("y_align parameter not recognised")

    draw.text((x, y), message, display.BLACK, font)
    return draw
