import argparse
import time

from PIL import Image, ImageDraw

from inkyphat_custom import InkyPHAT_SSD1608_Custom

from stock_utils import (
    get_quote_data,
    get_data,
    get_simple_messages,
    get_error_messages,
)
from display_utils import (
    draw_text,
    draw_simple_messages,
    draw_graph_data,
)


def main(symbol, mode, delay, graph_range, hflip, vflip, *args, **kwargs):
    # Initialize display
    inkyphat = InkyPHAT_SSD1608_Custom(
        colour="black",
        h_flip=hflip,
        v_flip=vflip,
    )
    last_img = None

    font_sizes = {"top": 24, "middle": 58, "bottom": 18}

    while True:
        img = Image.new("P", (inkyphat.WIDTH, inkyphat.HEIGHT))
        draw = ImageDraw.Draw(img)

        if mode == "simple":
            # Gather ticker data
            try:
                quote_data = get_quote_data(symbol)
                messages = get_simple_messages(symbol, quote_data)
            except Exception as e:
                messages = get_error_messages(e)

            draw = draw_simple_messages(inkyphat, draw, messages, font_sizes)

        elif mode == "graph":
            try:
                data = get_data(symbol, days=graph_range * 2)
                quote_data = get_quote_data(symbol)
                messages = get_simple_messages(symbol, quote_data)
                draw = draw_graph_data(inkyphat, draw, data, messages, graph_range)
            except Exception as e:
                messages = get_error_messages(e)
                draw = draw_simple_messages(inkyphat, draw, messages, font_sizes)

        # Show data on display
        if img != last_img:
            inkyphat.set_image(img)
            inkyphat.show()
            last_img = img.copy()

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
        "--mode",
        "-m",
        type=str,
        choices=["simple", "graph"],
        help="Display mode",
        default="simple",
    )
    parser.add_argument(
        "--delay",
        "-d",
        type=int,
        help="Ticker refresh interval (in sec)",
        default=10,
    )
    parser.add_argument(
        "--graph_range",
        "-r",
        type=int,
        help="Graph range in days (x axis)",
        default=60,
    )
    parser.add_argument(
        "--hflip", help="Horizontally flip display", action="store_true"
    )
    parser.add_argument("--vflip", help="Vertically flip display", action="store_true")

    args = parser.parse_args()

    main(**vars(args))
