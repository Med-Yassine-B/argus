import pandas as pd
from fx_converter_lab.services.timeseries_service import create_timeseries

def add_daily_percentage_change(curr: str, df: pd.DataFrame) -> pd.DataFrame:
    df = create_timeseries(curr, df)
    df["d_change_rate"] = df["rate"].pct_change() * 100
    return df