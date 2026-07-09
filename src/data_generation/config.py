"""
Project Configuration File
Cloud Resource Waste Optimization System

This file contains all configurable parameters for
synthetic cloud data generation.
"""

import random

# ==========================
# General Configuration
# ==========================

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

NUM_RESOURCES = 100
NUM_DAYS = 180

# ==========================
# Cloud Regions
# ==========================

REGIONS = [
    "us-east-1",
    "us-west-2",
    "eu-west-1",
    "ap-south-1",
    "eu-central-1"
]

# ==========================
# Cloud Services
# ==========================

SERVICES = [
    "EC2",
    "S3",
    "RDS",
    "Lambda",
    "EBS"
]

# ==========================
# EC2 Instance Types
# ==========================

INSTANCE_TYPES = [
    "t3.micro",
    "t3.small",
    "t3.medium",
    "m5.large",
    "c5.large"
]

# ==========================
# Environment Types
# ==========================

ENVIRONMENTS = [
    "Production",
    "Development",
    "Testing"
]

# ==========================
# Usage Limits
# ==========================

CPU_MIN = 2
CPU_MAX = 95

RAM_MIN = 5
RAM_MAX = 98

DISK_IO_MIN = 10
DISK_IO_MAX = 500

NETWORK_MIN = 1
NETWORK_MAX = 300

STORAGE_MIN = 10
STORAGE_MAX = 1000

MONTHLY_COST_MIN = 15
MONTHLY_COST_MAX = 1500

UPTIME_MIN = 1
UPTIME_MAX = 24

# ==========================
# Waste Simulation
# ==========================

ANOMALY_PERCENTAGE = 0.05
UNDERUTILIZED_CPU = 15
UNDERUTILIZED_RAM = 20