from yahoo_fin import stock_info


def get_quote_data(symbol):
    """Get quote data a ticker symbol

    Args:
        symbol (str): ticker symbol

    Returns:
        dict: quote data
    """
    try:
        return stock_info.get_quote_data(symbol)
    except Exception as e:
        raise Exception(f"get_quote_data() failed: {e}")


def get_error_messages(e):
    """Get messages to display from an Exception

    Args:
        e (Exception): Exception

    Returns:
        dict: top, middle en bottom messages to display
    """
    return {
        "top": "",
        "middle": "ERROR",
        "bottom": str(e)[:min(len(str(e)), 25)] + "..."
    }


def get_rounded(data, key):
    """Get rounded value if value is not None

    Args:
        data (dict): data containing the key
        key (str): key to get the value from the data

    Returns:
        float: rounded value
    """
    value = data.get(key)
    if value is not None:
        value = round(value, 2)
    return value


def get_messages(symbol, quote_data):
    """Get messages to display depending on market status and other things

    Args:
        quote_data (dict): quote data returned by yahoo_fin

    Returns:
        dict: top, middle en bottom messages to display
    """
    price = get_rounded(quote_data, 'regularMarketPrice')

    messages = {
        "top": f"${symbol}",
        "middle": f"{price:,}",
        "bottom": "",
    }

    market_state = quote_data.get("marketState", "UNKNOWN")
    messages["bottom"] = f"Market: {market_state}"

    if market_state == "OPEN":
        pass
    elif market_state == "PRE":
        messages["bottom"] += f" > {get_rounded(quote_data, 'preMarketPrice')}"
    elif market_state in ["POST", "CLOSED", "PREPRE"]:
        messages["bottom"] += f" > {get_rounded(quote_data, 'postMarketPrice')}"

    return messages
