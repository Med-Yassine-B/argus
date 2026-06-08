import pandas as pd
from fx_converter_lab.clients.mock_client import get_mock_timeseries

def create_timeseries(curr: str, dates: pd.DataFrame) -> pd.DataFrame:
    dates["rate"] = 0.0
    for i in range(len(dates)):
        date = str(dates.loc[i,"date"])
        dates.loc[i, "rate"] = get_mock_timeseries(curr, date)
    return dates


