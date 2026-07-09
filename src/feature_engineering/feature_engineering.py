import os
import pandas as pd


def create_features():

    input_file = "data/cleaned/cloud_usage_cleaned.csv"
    output_file = "data/processed/cloud_usage_featured.csv"

    df = pd.read_csv(input_file)

    print("Original Shape :", df.shape)

    # CPU and RAM utilization score
    df["utilization_score"] = (
        df["cpu_pct"] + df["ram_pct"]
    ) / 2

    # Cost per CPU usage
    df["cost_per_cpu"] = (
        df["monthly_cost"] / (df["cpu_pct"] + 1)
    ).round(2)

    # Cost per RAM usage
    df["cost_per_ram"] = (
        df["monthly_cost"] / (df["ram_pct"] + 1)
    ).round(2)

    # Network traffic
    df["total_network"] = (
        df["network_in"] +
        df["network_out"]
    )

    # Resource efficiency
    df["efficiency_score"] = (
        df["utilization_score"] /
        (df["monthly_cost"] + 1)
    ).round(3)

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(output_file, index=False)

    print("Feature Engineering Completed")
    print("New Shape :", df.shape)
    print(output_file)


if __name__ == "__main__":
    create_features()