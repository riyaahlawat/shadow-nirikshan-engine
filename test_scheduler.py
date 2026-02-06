import pandas as pd
from datetime import timedelta

from pipeline.scheduler import get_time_window

# Load full dataset
df = pd.read_csv("data/usage_logs_full.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Start at the first timestamp + 30 mins
current_time = df["timestamp"].min() + timedelta(minutes=30)

# Extract one 30-minute window
window_df = get_time_window(df, current_time, window_minutes=30)

print("Current Time:", current_time)
print("Window Data:")
print(window_df)
