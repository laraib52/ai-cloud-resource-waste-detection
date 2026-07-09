import os
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from faker import Faker

from config import *

fake = Faker()

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)


def generate_resource_id():
    return f"RES-{random.randint(10000, 99999)}"


def generate_date(day):
    start_date = datetime(2025, 1, 1)
    return start_date + timedelta(days=day)


def generate_record(resource_id, day):

    cpu = round(random.uniform(CPU_MIN, CPU_MAX), 2)
    ram = round(random.uniform(RAM_MIN, RAM_MAX), 2)
    disk = round(random.uniform(DISK_IO_MIN, DISK_IO_MAX), 2)
    network_in = round(random.uniform(NETWORK_MIN, NETWORK_MAX), 2)
    network_out = round(random.uniform(NETWORK_MIN, NETWORK_MAX), 2)
    storage = round(random.uniform(STORAGE_MIN, STORAGE_MAX), 2)
    cost = round(random.uniform(MONTHLY_COST_MIN, MONTHLY_COST_MAX), 2)
    uptime = round(random.uniform(UPTIME_MIN, UPTIME_MAX), 2)

    anomaly = 0

    if random.random() < ANOMALY_PERCENTAGE:
        cpu = round(random.uniform(0, UNDERUTILIZED_CPU), 2)
        ram = round(random.uniform(0, UNDERUTILIZED_RAM), 2)
        anomaly = 1

    return {
        "resource_id": resource_id,
        "date": generate_date(day),
        "region": random.choice(REGIONS),
        "service": random.choice(SERVICES),
        "instance_type": random.choice(INSTANCE_TYPES),
        "environment": random.choice(ENVIRONMENTS),
        "cpu_pct": cpu,
        "ram_pct": ram,
        "disk_io": disk,
        "network_in": network_in,
        "network_out": network_out,
        "storage_gb": storage,
        "monthly_cost": cost,
        "uptime_hours": uptime,
        "anomaly": anomaly,
    }


def generate_dataset():

    data = []

    resources = [generate_resource_id() for _ in range(NUM_RESOURCES)]

    for resource in resources:
        for day in range(NUM_DAYS):
            data.append(generate_record(resource, day))

    df = pd.DataFrame(data)

    # Create folder if it doesn't exist
    os.makedirs("data/raw", exist_ok=True)

    # Save CSV
    output_path = "data/raw/cloud_usage.csv"
    df.to_csv(output_path, index=False)

    print(df.head())
    print()
    print("Dataset Generated Successfully")
    print(f"Total Records : {len(df)}")
    print(f"Saved to : {output_path}")


if __name__ == "__main__":
    generate_dataset()