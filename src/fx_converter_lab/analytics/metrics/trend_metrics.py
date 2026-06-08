import pandas as pd
from fx_converter_lab.services.timeseries_service import create_timeseries

def add_daily_percentage_change(df: pd.DataFrame) -> pd.DataFrame:
    df["d_change_rate"] = df["rate"].pct_change() * 100
    return df

def add_rolling_average(df: pd.DataFrame) -> pd.DataFrame:
    df["roll_avg"] = df["rate"].rolling(window=3).mean()
    return df

def get_min_max_rates(df: pd.DataFrame) -> dict:
    min_max = {
        "rate":[],
        "date":[]
    }
    min_id = df["rate"].idxmax()
    max_id = df["rate"].idxmin()
    min_max["rate"].append(df.loc[min_id, "rate"])
    min_max["date"].append(df.loc[min_id, "date"])
    min_max["rate"].append(df.loc[max_id, "rate"])
    min_max["date"].append(df.loc[max_id, "date"])
    return min_max