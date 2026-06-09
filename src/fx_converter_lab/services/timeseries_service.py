import pandas as pd
from fx_converter_lab.clients.mock_client import get_mock_timeseries
from fx_converter_lab.analytics.metrics.trend_metrics import add_rolling_average,add_daily_percentage_change,get_min_max_rates

mock_dates = {
    "date": ["2026-06-01","2026-06-02","2026-06-03",
             "2026-06-04","2026-06-05","2026-06-06",
             "2026-06-07","2026-06-08","2026-06-09",
             "2026-06-10","2026-06-11","2026-06-12",
             "2026-06-13","2026-06-14","2026-06-15"
    ]
}

def prepare_trend_analysis() -> tuple[pd.DataFrame,dict]:
    df = pd.DataFrame(mock_dates)
    mock_curr = "USD"
    df["rate"] = 0.0
    # For each date one API call to get the rate
    for i in range(len(df)):
        date = str(df.loc[i,"date"])
        df.loc[i, "rate"] = get_mock_timeseries(mock_curr, date)
    df = add_daily_percentage_change(df)
    df = add_rolling_average(df)
    min_max_rates = get_min_max_rates(df)
    return df,min_max_rates


