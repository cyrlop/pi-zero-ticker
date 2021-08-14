from yahoo_fin import stock_info



def get_quote_data(symbol):
    """Get quote data a ticker symbol

    Args:
        symbol (str): ticker symbol

    Returns:
        dict: quote data
    """
    return stock_info.get_quote_data(symbol)



def get_last_price(quote_data):
    """Get last ticker price

    Args:
        quote_data (dict): quote data returned by yahoo_fin

    Returns:
        float: last ticker price
    """
    last_price = quote_data["regularMarketPrice"]
    return round(last_price, 2)

