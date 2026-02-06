import pandas as pd
from datetime import timedelta

from pipeline.scheduler import get_time_window
from pipeline.ingestion import load_schedule
from pipeline.silence_detection import mark_silence_windows
from pipeline.baseline import compute_silence_baseline
from pipeline.anomaly import detect_shadow_waste
from pipeline.decision import generate_decision

# Load full usage dataset
usage_df = pd.read_csv("data/usage_logs_full.csv")
usage_df["timestamp"] = pd.to_datetime(usage_df["timestamp"])

# Load schedule
schedule = load_schedule("data/demo/schedule.csv")

# Simulate current scheduler time (first 30-min cycle)
current_time = usage_df["timestamp"].min() + timedelta(minutes=30)

print(f"\n=== Scheduled Run At {current_time} ===\n")

# 1️⃣ Extract 30-minute window
window_df = get_time_window(
    usage_df,
    current_time,
    window_minutes=30
)

print("[Window Data]")
print(window_df)

# 2️⃣ Mark silence windows
window_df = mark_silence_windows(window_df, schedule)

# 3️⃣ Prepare historical data for baseline
historical_df = usage_df[usage_df["timestamp"] < current_time]
historical_df = mark_silence_windows(historical_df, schedule)

baseline = compute_silence_baseline(historical_df)

print("\n[Baseline]")
print(baseline)

# 4️⃣ Detect anomalies in this window
result = detect_shadow_waste(window_df, baseline)

print("\n[Anomaly Detection Output]")
print(result)

# 5️⃣ Generate decisions
decisions = []
for _, row in result.iterrows():
    if row["is_anomaly"]:
        decisions.append(generate_decision(row))

print("\n[Generated Decisions]")
for d in decisions:
    print("=" * 80)
    print(f"🏢 Building           : {d['building']}")
    print(f"🔧 Resource           : {d['resource'].capitalize()}")
    print(f"⚠️  Issue              : {d['detected_issue']}")
    print("-" * 80)
    print(f"📊 Observed Usage     : {d['observed_usage']}")
    print(f"📈 Normal (Silence)   : {d['normal_silence_usage']}")
    print(f"🎯 Confidence         : {d['confidence_percent']}%")
    print("-" * 80)
    print(f"🔍 Likely Cause       : {d['likely_cause']}")
    print(f"🛠️  Recommended Action : {d['recommended_action']}")
    print("=" * 80)
    print()
