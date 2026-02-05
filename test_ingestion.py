# from pipeline.ingestion import load_usage_logs, load_schedule

# usage = load_usage_logs("data/demo/usage_logs.csv")
# schedule = load_schedule("data/demo/schedule.csv")

# print(usage)
# print("\n")
# print(schedule)

from pipeline.ingestion import load_usage_logs, load_schedule
from pipeline.silence_detection import mark_silence_windows

usage = load_usage_logs("data/demo/usage_logs.csv")
schedule = load_schedule("data/demo/schedule.csv")

result = mark_silence_windows(usage, schedule)
print(result)
