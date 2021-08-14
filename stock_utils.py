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
