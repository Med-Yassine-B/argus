import matplotlib.pyplot as plt
import pandas as pd
from fx_converter_lab.analytics.metrics.trend_metrics import add_daily_percentage_change

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
    df = add_daily_percentage_change(mock_curr, df)
    
    plt.plot(df["date"],df["rate"],label="Exchange Rate", color="red")
    plt.xlabel("date")
    plt.ylabel("rate")
    plt.bar(df["date"],df["d_change_rate"],label="Daily Percentage Chnage", color="green")
    plt.title("Exchange Rate Over Time")
    plt.legend()
    plt.show()

create_trendchart()