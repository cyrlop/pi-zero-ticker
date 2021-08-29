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

    # Scale down font if the text is bigger than the screen
    if (w > display.WIDTH):
        font_size = int(font_size*display.WIDTH/w)
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


def draw_simple_messages(
    display,
    draw,
    messages,
    font_sizes={"top": 24, "middle": 52, "bottom": 18},
):
    """Get yfinance ticker object from a symbol

    Args:
        display (Inky): Inky display object
        draw (ImageDraw): ImageDraw object
        messages (dict): messages with the keys "middle", "top" and "bottom"
        font_sizes (dict): Font sizes dict with the keys "middle", "top" and "bottom" 
    Returns:
        draw (ImageDraw): Updated ImageDraw object
    """
    for location, message in messages.items():
        draw = draw_text(
            display,
            draw,
            message=message,
            font_size=font_sizes[location],
            y_align=location,
        )
    return draw