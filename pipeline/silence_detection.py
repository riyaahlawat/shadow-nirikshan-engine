from datetime import time
import pandas as pd


def is_time_in_window(check_time: time, start: time, end: time) -> bool:
    """
    Handles both normal and overnight time windows.
    """
    if start <= end:
        return start <= check_time <= end
    else:
        # Overnight window (e.g., 22:00 - 06:00)
        return check_time >= start or check_time <= end


def mark_silence_windows(
    usage_df: pd.DataFrame,
    schedule_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Adds an 'is_silence' column to usage_df.
    """

    usage_df = usage_df.copy()
    usage_df["is_silence"] = False

    for idx, row in usage_df.iterrows():
        building = row["building"]
        record_time = row["timestamp"].time()

        building_schedule = schedule_df[schedule_df["building"] == building]

        for _, sched in building_schedule.iterrows():
            if sched["expected_activity"] == "NO":
                if is_time_in_window(
                    record_time,
                    sched["start_time"],
                    sched["end_time"]
                ):
                    usage_df.at[idx, "is_silence"] = True

    return usage_df