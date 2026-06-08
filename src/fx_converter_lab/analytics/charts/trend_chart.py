import matplotlib.pyplot as plt
import pandas as pd
from fx_converter_lab.analytics.metrics.trend_metrics import add_daily_percentage_change,add_rolling_average,get_min_max_rates
from fx_converter_lab.services.timeseries_service import create_timeseries

dates = {
    "date": ["2026-06-01","2026-06-02","2026-06-03",
             "2026-06-04","2026-06-05","2026-06-06",
             "2026-06-07","2026-06-08","2026-06-09",
             "2026-06-10","2026-06-11","2026-06-12",
             "2026-06-13","2026-06-14","2026-06-15"
    ]
}

def create_trendchart() -> None:
    mock_curr = "USD"
    df = pd.DataFrame(dates)
    df = create_timeseries(mock_curr, df)
    df = add_daily_percentage_change(df)
    df = add_rolling_average(df)
    min_max_rates = get_min_max_rates(df)
    
    fig, ax1 = plt.subplots()

    ax1.plot(df["date"], df["rate"], color="red", label="Exchange Rate")
    ax1.plot(df["date"], df["roll_avg"], color="blue", label="Rolling Average")
    ax1.tick_params(axis='x', rotation=45)

    ax2 = ax1.twinx()
    bar_colors = ["green" if x >= 0 else "red" for x in df["d_change_rate"]]
    ax2.bar(df["date"], df["d_change_rate"], color=bar_colors,alpha=0.4)
    ax2.legend(loc="upper left")
    ax2.set_ylabel("Percentage Scale")
    plt.tight_layout()
    plt.show()

create_trendchart()