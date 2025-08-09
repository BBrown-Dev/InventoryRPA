# Generates 10,000 synthetic inventory bot logs in JSON format

import json
import random
from datetime import datetime, timedelta, timezone
import os

# Ensure output directory exists
os.makedirs("data", exist_ok=True)

# Configuration
NUM_LOGS = 10000
WAREHOUSE_IDS = list(range(1, 51))
STATUSES = ["success", "error", "retry"]
OUTPUT_FILE = "../data/fake_logs.json"

# Generate logs
with open(OUTPUT_FILE, "w") as f:
    for _ in range(NUM_LOGS):
        log_entry = {
            "timestamp": (datetime.now(timezone.utc) - timedelta(seconds=random.randint(0, 86400))).isoformat(),
            "duration": round(random.uniform(0.05, 2.5), 3),  # in seconds
            "status": random.choices(STATUSES, weights=[0.85, 0.1, 0.05])[0],
            "warehouse_id": random.choice(WAREHOUSE_IDS),
            "cpu_percent": round(random.uniform(10, 90), 2),
            "memory_mb": round(random.uniform(100, 800), 2)
        }
        f.write(json.dumps(log_entry) + "\n")

print(f"✅ Generated {NUM_LOGS} synthetic logs at {OUTPUT_FILE}")
