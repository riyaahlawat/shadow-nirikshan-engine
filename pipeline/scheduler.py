from datetime import timedelta

def get_time_window(df, current_time, window_minutes=30):
    """
    Extracts a time window ending at current_time.

    Args:
        df (DataFrame): Full usage dataset
        current_time (datetime): End of window
        window_minutes (int): Window size in minutes

    Returns:
        DataFrame: Filtered window data
    """
    start_time = current_time - timedelta(minutes=window_minutes)

    window_df = df[
        (df["timestamp"] >= start_time) &
        (df["timestamp"] < current_time)
    ]

    return window_df
