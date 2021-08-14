import argparse
import time

import yfinance

from inky import InkyPHAT_SSD1608
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne


def get_ticker(ticker_symbol):
    """Get yfinance ticker object from a symbol

    Args:
        ticker_symbol (str): ticker symbol

    Returns:
        Ticker: yfinance ticker object
    """
    return yfinance.Ticker(ticker_symbol)


def get_last_price(ticker):
    """Get last ticker price

    Args:
        ticker (Ticker): yfinance ticker object

    Returns:
        float: last ticker price
    """
    last_price = ticker.history().tail(1)["Close"].iloc[0]
    return round(last_price, 2)


def main(symbol, delay, *args, **kwargs):

    # Initialize display
    inkyphat = InkyPHAT_SSD1608('black')


    while True:
        # Gather ticker data
        ticker = get_ticker(symbol)
        price = get_last_price(ticker)
        print(price)

        # Show data on display
        img = Image.new("P", (inkyphat.WIDTH, inkyphat.HEIGHT))
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype(FredokaOne, 52)
        message = f"{price}"
        w, h = font.getsize(message)
        x = (inkyphat.WIDTH / 2) - (w / 2)
        y = (inkyphat.HEIGHT / 2) - (h / 2)
        draw.text((x, y), message, inkyphat.BLACK, font)

        font = ImageFont.truetype(FredokaOne, 24)
        message = f"${symbol}"
        w, h = font.getsize(message)
        x = (inkyphat.WIDTH / 2) - (w / 2)
        y = 0
        draw.text((x, y), message, inkyphat.BLACK, font)

        font = ImageFont.truetype(FredokaOne, 18)
        message = "Market opened/closed?"
        w, h = font.getsize(message)
        x = (inkyphat.WIDTH / 2) - (w / 2)
        y = inkyphat.HEIGHT - h
        draw.text((x, y), message, inkyphat.BLACK, font)

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

