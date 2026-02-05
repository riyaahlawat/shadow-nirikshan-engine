# from pipeline.ingestion import load_usage_logs, load_schedule

# usage = load_usage_logs("data/demo/usage_logs.csv")
# schedule = load_schedule("data/demo/schedule.csv")

# print(usage)
# print("\n")
# print(schedule)

# from pipeline.ingestion import load_usage_logs, load_schedule
# from pipeline.silence_detection import mark_silence_windows

# usage = load_usage_logs("data/demo/usage_logs.csv")
# schedule = load_schedule("data/demo/schedule.csv")

# result = mark_silence_windows(usage, schedule)
# print(result)

from pipeline.ingestion import load_usage_logs, load_schedule
from pipeline.silence_detection import mark_silence_windows
from pipeline.baseline import compute_silence_baseline

# Load historical data
historical = load_usage_logs("data/demo/historical_logs.csv")
schedule = load_schedule("data/demo/schedule.csv")

historical = mark_silence_windows(historical, schedule)

baseline = compute_silence_baseline(historical)
print(baseline)

