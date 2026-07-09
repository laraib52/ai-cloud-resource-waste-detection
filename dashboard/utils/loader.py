import pandas as pd


def load_data():

    anomalies = pd.read_csv(
        "data/processed/cloud_usage_predictions.csv"
    )

    recommendations = pd.read_csv(
        "data/processed/cloud_recommendations.csv"
    )

    forecast = pd.read_csv(
        "data/forecast/cost_forecast.csv"
    )

    return anomalies, recommendations, forecast