import os
import pandas as pd


def clean_dataset():

    input_file = "data/raw/cloud_usage.csv"
    output_file = "data/cleaned/cloud_usage_cleaned.csv"

    # Read dataset
    df = pd.read_csv(input_file)

    print("Original Shape :", df.shape)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove missing values
    df = df.dropna()

    # Convert date column
    df["date"] = pd.to_datetime(df["date"])

    # Ensure numeric columns are correct
    numeric_columns = [
        "cpu_pct",
        "ram_pct",
        "disk_io",
        "network_in",
        "network_out",
        "storage_gb",
        "monthly_cost",
        "uptime_hours",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Remove any rows created by conversion errors
    df = df.dropna()

    # Create output folder
    os.makedirs("data/cleaned", exist_ok=True)

    # Save cleaned dataset
    df.to_csv(output_file, index=False)

    print("Cleaned Shape :", df.shape)
    print("Cleaned dataset saved successfully.")
    print(output_file)


if __name__ == "__main__":
    clean_dataset()