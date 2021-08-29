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
    if w > display.WIDTH:
        font_size = int(font_size * display.WIDTH / w)
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
    """Draw three text messages

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


def draw_graph_data(display, draw, data, simple_messages):
    """Draw graph mode data

    Args:
        display (Inky): Inky display object
        draw (ImageDraw): ImageDraw object
        data (DataFrame): DataFrame given by get_data
        simple_messages (dict): output of draw_simple_messages()
    Returns:
        draw (ImageDraw): Updated ImageDraw object
    """
    # Display text
    message = f"{simple_messages['top']}: {simple_messages['middle']}"
    font = ImageFont.truetype(FredokaOne, 25)
    w, h = font.getsize(message)
    x = (display.WIDTH / 2) - (w / 2)
    draw.text((x, 0), message, display.BLACK, font)
    message = f"{simple_messages['bottom']}"
    font = ImageFont.truetype(FredokaOne, 15)
    w, h = font.getsize(message)
    x = (display.WIDTH / 2) - (w / 2)
    draw.text((x, 25), message, display.BLACK, font)

    # Display graph
    x_steps = 30
    x_margin_right = 50

    y_margin_top = 50
    y_margin_bot = 5
    y_range = display.HEIGHT - y_margin_top - y_margin_bot

    price_data = list(data["close"])[-x_steps:]
    max_price = round(max(price_data), 2)
    min_price = round(min(price_data), 2)

    x_list = []
    y_list = []

    # y: change scale from [max_price, max_price] to [0, display.HEIGHT]
    y_data = [
        (display.HEIGHT * (y - min_price)) / (max_price - min_price) for y in price_data
    ]
    for i in range(x_steps):
        x = i * (display.WIDTH - x_margin_right) / x_steps
        y = y_data[i]
        y = display.HEIGHT - y  # 0 on bottom
        y = y / display.HEIGHT * y_range + y_margin_top  # apply limited range (y_range)

        x_list.append(x)
        y_list.append(y)

    draw.line(list(zip(x_list, y_list)), fill=display.BLACK, width=2)

    # Display min price and max price on right side
    draw.text(
        (display.WIDTH - x_margin_right + 2, y_margin_top - 3),
        str(max_price),
        display.BLACK,
        ImageFont.truetype(FredokaOne, 15),
    )
    draw.text(
        (display.WIDTH - x_margin_right + 2, display.HEIGHT - 15),
        str(min_price),
        display.BLACK,
        ImageFont.truetype(FredokaOne, 15),
    )
    return draw
