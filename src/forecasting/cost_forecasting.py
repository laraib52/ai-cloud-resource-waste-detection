import os
import pandas as pd
from prophet import Prophet


def forecast_cost():

    input_file = "data/processed/cloud_recommendations.csv"

    df = pd.read_csv(input_file)

    # Daily total cost
    daily_cost = (
        df.groupby("date")["monthly_cost"]
        .sum()
        .reset_index()
    )

    # Prophet format
    daily_cost.columns = ["ds", "y"]

    model = Prophet()

    model.fit(daily_cost)

    future = model.make_future_dataframe(periods=30)

    forecast = model.predict(future)

    os.makedirs("data/forecast", exist_ok=True)

    forecast.to_csv(
        "data/forecast/cost_forecast.csv",
        index=False
    )

    fig = model.plot(forecast)
    fig.savefig("data/forecast/cost_forecast.png")

    print("\nForecast Generated Successfully")
    print(forecast[["ds", "yhat"]].tail())


if __name__ == "__main__":
    forecast_cost()