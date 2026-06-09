import pandas as pd
from fx_converter_lab.clients.mock_client import get_mock_timeseries
from fx_converter_lab.analytics.metrics.trend_metrics import add_rolling_average,add_daily_percentage_change,get_min_max_rates

def prepare_trend_analysis(mock_curr:str,df:pd.DataFrame) -> tuple[pd.DataFrame,dict]:
    df["rate"] = 0.0
    # For each date one API call to get the rate
    for i in range(len(df)):
        date = str(df.loc[i,"date"])
        df.loc[i, "rate"] = get_mock_timeseries(mock_curr, date)
    df = add_daily_percentage_change(df)
    df = add_rolling_average(df)
    min_max_rates = get_min_max_rates(df)
    return df,min_max_rates


