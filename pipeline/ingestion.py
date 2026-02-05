# pipeline/ingestion.py

import pandas as pd


def load_usage_logs(filepath: str) -> pd.DataFrame:
    """
    Load meter usage logs.
    Expected columns:
    timestamp, building, resource, usage
    """
    df = pd.read_csv(filepath)

    # Parse timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df


def load_schedule(filepath: str) -> pd.DataFrame:
    """
    Load building activity schedules.
    Expected columns:
    building, start_time, end_time, expected_activity
    """
    df = pd.read_csv(filepath)

    # Normalize time columns
    df["start_time"] = pd.to_datetime(df["start_time"], format="%H:%M").dt.time
    df["end_time"] = pd.to_datetime(df["end_time"], format="%H:%M").dt.time

    return df
