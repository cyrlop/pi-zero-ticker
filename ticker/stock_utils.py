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


def get_messages(symbol, quote_data):
    """Get messages to display depending on market status and other things

    Args:
        quote_data (dict): quote data returned by yahoo_fin

    Returns:
        dict: top, middle en bottom messages to display
    """
    messages = {
        "top": f"${symbol}",
        "middle": f"{quote_data.get('regularMarketPrice')}",
        "bottom": "",
    }

    market_state = quote_data.get("marketState", "UNKNOWN")
    messages["bottom"] = f"Market: {market_state}"

    if market_state == "OPEN":
        pass
    elif market_state == "PRE":
        messages["bottom"] += f" > {quote_data.get('preMarketPrice')}"
    elif market_state in ["POST", "CLOSED"]:
        messages["bottom"] += f" > {quote_data.get('postMarketPrice')}"

    return messages
