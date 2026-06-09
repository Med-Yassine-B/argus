import pandas as pd

def add_daily_percentage_change(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["d_change_rate"] = result["rate"].pct_change() * 100
    return result

def add_rolling_average(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["roll_avg"] = result["rate"].rolling(window=3).mean()
    return result

def get_min_max_rates(df: pd.DataFrame) -> dict:
    min_max = {
        "min_date":[],
        "min_rate":[],
        "max_date":[],
        "max_rate":[]
    }
    min_id = df["rate"].idxmin()
    max_id = df["rate"].idxmax()
    min_max["min_date"].append(df.loc[min_id, "date"])
    min_max["min_rate"].append(df.loc[min_id, "rate"])
    min_max["max_date"].append(df.loc[max_id, "date"])
    min_max["max_rate"].append(df.loc[max_id, "rate"])
    return min_max