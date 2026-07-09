import os
import pandas as pd


def generate_recommendations():

    input_file = "data/processed/cloud_usage_predictions.csv"
    output_file = "data/processed/cloud_recommendations.csv"

    df = pd.read_csv(input_file)

    recommendations = []

    for _, row in df.iterrows():

        recommendation = "No Action Required"

        if row["prediction"] == "Anomaly":

            if row["cpu_pct"] < 20:
                recommendation = "Resize EC2 Instance"

            elif row["ram_pct"] < 20:
                recommendation = "Reduce Memory Allocation"

            elif row["storage_gb"] > 800:
                recommendation = "Archive or Delete Old Data"

            elif row["monthly_cost"] > 800:
                recommendation = "Review High Cost Resource"

            else:
                recommendation = "Manual Investigation Required"

        recommendations.append(recommendation)

    df["recommendation"] = recommendations

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(output_file, index=False)

    print("\nRecommendation Engine Completed\n")

    print(df["recommendation"].value_counts())

    print("\nSaved Successfully")


if __name__ == "__main__":
    generate_recommendations()