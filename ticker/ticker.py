import argparse
import time

from PIL import Image, ImageDraw

from inkyphat_custom import InkyPHAT_SSD1608_Custom

from stock_utils import (
    get_quote_data,
    get_messages,
    get_error_messages,
)
from display_utils import draw_text, draw_messages


def main(symbol, delay, hflip, vflip, *args, **kwargs):
    # Initialize display
    inkyphat = InkyPHAT_SSD1608_Custom(
        colour="black",
        h_flip=hflip,
        v_flip=vflip,
    )

    messages = None
    while True:
        # Gather ticker data
        try:
            quote_data = get_quote_data(symbol)
            new_messages = get_messages(symbol, quote_data)
        except Exception as e:
            new_messages = get_error_messages(e)

        if messages == new_messages:
            time.sleep(delay)
            continue
        else:
            messages = new_messages

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
    parser.add_argument(
        "--hflip",
        help="Horizontally flip display",
        action="store_true"
    )
    parser.add_argument(
        "--vflip",
        help="Vertically flip display",
        action="store_true"
    )

    args = parser.parse_args()

    main(**vars(args))
