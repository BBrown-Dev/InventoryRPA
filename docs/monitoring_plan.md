# Monitoring Strategy for InventoryRPA

## 📡 Telemetry Emission

The InventoryRPA bot emits telemetry using Python’s built-in `logging` module and `prometheus_client` for metrics:

- **Structured JSON Logs**:  
  Logs are emitted using `logging.handlers.TimedRotatingFileHandler` with a custom JSON formatter. Each log includes timestamp, log level, message, and optional metadata (i.e. warehouse ID and batch size).

- **Prometheus Metrics**:  
  Metrics like batch processing duration and error counts are exposed via a Prometheus HTTP endpoint using `prometheus_client.Summary` and `Counter`.

- **System Resource Metrics**:  
  `psutil` is used to track CPU usage, memory consumption, and disk I/O during bot execution.

## 🗂️ Storage Locations

- **Logs**: Saved as daily rotated JSON files in `/logs/inventory.log`.
- **Metrics**: Exposed at `http://localhost:9100/metrics` for Prometheus scraping.
- **Synthetic Data**: Generated using `/scripts/generate_fake_logs.py` and stored in `/data/`.

## 📊 Visualization & Alerting

- **Visualization**:  
  Metrics are visualized using a static HTML dashboard generated from Prometheus data or terminal dashboards using the `rich` library.

- **Alerting**:  
  Threshold-based alerts are emitted as structured log events. For example:
  - Batch duration > 2 seconds
  - Error rate > 5% in last 100 transactions
  - CPU usage > 85% sustained for 5 minutes

These alerts can be monitored by an orchestrator or DevOps script to trigger notifications or rollbacks.

## 📈 Key Performance Indicators (KPIs)

- `inv_batch_seconds`: Batch processing latency (P95, P99)
- `inv_error_count`: Number of failed transactions per hour
- `cpu_percent`: CPU usage during execution
- `mem_usage_mb`: Memory footprint of bot process
- `batch_success_rate`: Ratio of successful to total batches
- `retry_count`: Number of retries triggered per workflow

## 🛠️ Tools Used

- `logging` for structured logs
- `psutil` for system metrics
- `prometheus_client` for exposing metrics
- `sentry_sdk` (optional) for error tracking and stack traces

## 🧪 Synthetic Data Generator

Use created generator script `/scripts/generate_fake_logs.py` to simulate 10,000 rows of synthetic logs with timestamps, durations, and outcome tags. Example snippet:

```python
import json, random, time
from datetime import datetime

with open("../data/fake_logs.json", "w") as f:
    for _ in range(10000):
        log = {
            "timestamp": (datetime.now(timezone.utc) - timedelta(seconds=random.randint(0, 86400))).isoformat(),
            "duration": round(random.uniform(0.05, 2.5), 3),
            "status": random.choice(["success", "error", "retry"]),
            "warehouse_id": random.randint(1, 50)
        }
        f.write(json.dumps(log) + "\n")
