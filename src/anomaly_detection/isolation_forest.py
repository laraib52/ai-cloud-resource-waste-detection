import os
import joblib
import pandas as pd

from sklearn.ensemble import IsolationForest


def train_model():

    input_file = "data/processed/cloud_usage_featured.csv"

    df = pd.read_csv(input_file)

    features = [
        "cpu_pct",
        "ram_pct",
        "monthly_cost",
        "storage_gb",
        "disk_io",
        "utilization_score",
        "efficiency_score"
    ]

    X = df[features]

    model = IsolationForest(
        contamination=0.10,
        random_state=42
    )

    model.fit(X)

    predictions = model.predict(X)

    df["prediction"] = predictions

    df["prediction"] = df["prediction"].map({
        1: "Normal",
        -1: "Anomaly"
    })

    os.makedirs("models", exist_ok=True)

    joblib.dump(model, "models/isolation_forest.pkl")

    df.to_csv(
        "data/processed/cloud_usage_predictions.csv",
        index=False
    )

    print("\nModel Training Completed")

    print(df["prediction"].value_counts())

    print("\nModel Saved Successfully")


if __name__ == "__main__":
    train_model()