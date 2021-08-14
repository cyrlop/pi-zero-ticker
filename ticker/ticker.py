import argparse
import time

from inky import InkyPHAT_SSD1608
from PIL import Image, ImageDraw

from stock_utils import (
    get_quote_data,
    get_messages,
    get_error_messages,
)
from display_utils import draw_text, draw_messages


def main(symbol, delay, *args, **kwargs):
    # Initialize display
    inkyphat = InkyPHAT_SSD1608("black")

    while True:
        # Gather ticker data
        try:
            quote_data = get_quote_data(symbol)
            messages = get_messages(symbol, quote_data)
        except Exception as e:
            messages = get_error_messages(e)

        # Show data on display
        font_sizes = {"top": 24, "middle": 52, "bottom": 18}

        img = Image.new("P", (inkyphat.WIDTH, inkyphat.HEIGHT))
        draw = ImageDraw.Draw(img)
        draw = draw_messages(inkyphat, draw, messages, font_sizes)

        inkyphat.set_image(img)
        inkyphat.show()

        time.sleep(delay)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script to display stock ticker price on a Inky pHAT display"
    )
    parser.add_argument(
        "--symbol",
        "-s",
        type=str,
        help="Ticker symbol",
        default="GME",
    )
    parser.add_argument(
        "--delay",
        "-d",
        type=int,
        help="Ticker refresh interval (in sec)",
        default=10,
    )

    args = parser.parse_args()

    main(**vars(args))
