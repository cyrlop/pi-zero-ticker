import argparse
import time

import yfinance


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

    while True:
        # Gather ticker data
        ticker = get_ticker(symbol)
        price = get_last_price(ticker)
        print(price)

        # Show data on display
        # TODO

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
