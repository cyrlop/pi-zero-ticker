import argparse
import time

from inky import InkyPHAT_SSD1608
from PIL import Image, ImageDraw

from stock_utils import get_quote_data, get_last_price
from display_utils import draw_text


def main(symbol, delay, *args, **kwargs):

    # Initialize display
    inkyphat = InkyPHAT_SSD1608('black')

    while True:
        # Gather ticker data
        quote_data = get_quote_data(symbol)
        price = get_last_price(quote_data)
        print(price)

        # Show data on display
        img = Image.new("P", (inkyphat.WIDTH, inkyphat.HEIGHT))
        draw = ImageDraw.Draw(img)

        draw = draw_text(
            inkyphat,
            draw,
            message=f"${symbol}",
            font_size=24,
            y_align="top",
        )
        draw = draw_text(
            inkyphat,
            draw,
            message=f"{price}",
            font_size=52,
            y_align="middle",
        )
        draw = draw_text(
            inkyphat,
            draw,
            message="Market opened/closed?",
            font_size=18,
            y_align="bottom",
        )

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

