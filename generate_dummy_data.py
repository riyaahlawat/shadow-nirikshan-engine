import pandas as pd
from datetime import datetime, timedelta
import random

# --------------------------------------------------
# Configuration
# --------------------------------------------------
START_TIME = datetime(2026, 2, 5, 0, 0)
END_TIME = START_TIME + timedelta(hours=24)
INTERVAL = timedelta(minutes=30)

BUILDINGS = [
    "Lab-A",
    "Library",
    "Admin-Block",
    "Hostel-A",
    "Auditorium",
    "Cafeteria"
]

RESOURCES = ["water", "electricity"]

rows = []
current_time = START_TIME

# --------------------------------------------------
# Generate data
# --------------------------------------------------
while current_time < END_TIME:
    hour = current_time.hour

    for building in BUILDINGS:
        for resource in RESOURCES:

            # -------------------------------
            # Base idle usage
            # -------------------------------
            if resource == "water":
                usage = random.randint(15, 50)
            else:
                usage = random.randint(2, 7)

            # -------------------------------
            # Active hours (9 AM – 6 PM)
            # -------------------------------
            if 9 <= hour < 18:
                if resource == "water":
                    usage = random.randint(200, 600)
                else:
                    usage = random.randint(15, 35)

            # -------------------------------
            # Shadow waste during inactivity
            # -------------------------------
            if hour < 6 or hour >= 22:
                if random.random() < 0.3:  # 30% chance
                    if resource == "water":
                        usage = random.randint(700, 1600)
                    else:
                        usage = random.randint(15, 40)
            
            # Force anomalies for demo: every 5th cycle
            cycle_number = int((current_time - START_TIME) / INTERVAL)
            force_anomaly = (cycle_number % 5 == 0)  # every 5th cycle

            # Inject guaranteed anomaly for first building & water
            if force_anomaly and building == BUILDINGS[0] and resource == "water":
                usage = max(usage, baseline := usage * 2)  # make usage > baseline

            rows.append({
                "timestamp": current_time,
                "building": building,
                "resource": resource,
                "usage": usage
            })

    current_time += INTERVAL


# --------------------------------------------------
# Save CSV
# --------------------------------------------------
df = pd.DataFrame(rows)
df.to_csv("data/usage_logs_full.csv", index=False)

print("✅ Dummy dataset created: data/usage_logs_full.csv")
print(f"📊 Total records generated: {len(df)}")
