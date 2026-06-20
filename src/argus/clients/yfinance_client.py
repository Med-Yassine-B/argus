import yfinance as yf
import logging


def get_timeseries(curr_symbol, start, end, interval):
    """
    Fetch historical exchange-rate time series data from Yahoo Finance.

    Args:
        curr_symbol (str): Currency symbol used by Yahoo Finance, for example
            "EURUSD=X".
        start (str): Start date of the requested time range in YYYY-MM-DD format.
        end (str): End date of the requested time range in YYYY-MM-DD format.
        interval (str): Data interval supported by Yahoo Finance, for example
            "1d", "1h", or "15m".

    Returns:
        pandas.DataFrame | None: A DataFrame containing the columns ``date`` and
        ``rate`` if data was successfully fetched. Returns ``None`` if the
        request fails, returns no data, or an exception occurs.
    """
    try:
        yf_logger = logging.getLogger("yfinance")
        yf_logger.disabled = True
        data = yf.download(
            tickers=curr_symbol,
            start=start,
            end=end,
            interval=interval,
            multi_level_index=False,
            progress=False,
        )
        yf_logger.disabled = False
        if data is None:
            return None
        if data.empty:
            return None
        data = data.reset_index()
        data = data[["Date", "Close"]]
        data = data.rename(columns={"Date": "date", "Close": "rate"})
        return data
    except Exception:
        return None
