import pandas as pd
from fx_converter_lab.clients.mock_client import get_mock_timeseries
from fx_converter_lab.domain.validation import normalize_input_string,is_valid_curr_code

def check_currency(question:str) -> str:
    resp = normalize_input_string(question)
    """
    if is_valid_curr_code(resp):
        return resp
    return None
    """
    return resp

def create_timeseries(curr: str, dates: pd.DataFrame) -> pd.DataFrame:
    resp = check_currency(curr)
    dates["rate"] = 0.0
    for i in range(len(dates)):
        date = str(dates.loc[i,"date"])
        dates.loc[i, "rate"] = get_mock_timeseries(resp, date)
    return dates


