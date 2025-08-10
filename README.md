# InventoryRPA
A code-first RPA that replaces manual Excel counts by generating test data, cleaning and de-duplicating inventory, calculating reorder needs, and automatically emailing low-stock alerts.

---

## ▶️ Local Run

To run InventoryRPA locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/BBrown-Dev/InventoryRPA.git
   cd InventoryRPA
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the main script:
   ```bash
   python main.py
   ```

This will generate synthetic inventory data, process it, and log results to the console and log files.

---

## 📈 Metrics Demo

InventoryRPA includes a metrics endpoint for Prometheus-style monitoring.

### Enable Metrics

Set environment variables before running:

```bash
export ENABLE_METRICS=true
export METRICS_PORT=8000
python main.py
```

### Access Metrics

Once running, access metrics at:

```
http://localhost:8000/metrics
```

Sample output:

```
# HELP inventory_batches_total Total inventory batches processed
# TYPE inventory_batches_total counter
inventory_batches_total 1.0

# HELP inventory_items_processed_total Total inventory items processed
# TYPE inventory_items_processed_total counter
inventory_items_processed_total 12000.0

# HELP inventory_retries_total Total retry attempts
# TYPE inventory_retries_total counter
inventory_retries_total 120.0

# HELP inventory_failures_total Permanent failures
# TYPE inventory_failures_total counter
inventory_failures_total 24.0

# HELP inventory_batch_duration_seconds Batch processing time
# TYPE inventory_batch_duration_seconds gauge
inventory_batch_duration_seconds 4.32
```

You can scrape these metrics using Prometheus and visualize them in Grafana.

---

## 📜 Logs

Structured logs are written to `logs/inventory.log` in JSONL format.

Example:

```json
{"timestamp":"2025-08-10T14:00:02Z","batch_id":1,"processed":12000,"retries":120,"failures":24,"duration_s":4.32,"status":"success"}
```

Use `tail -f` to monitor logs in real time:

```bash
tail -f logs/inventory.log
```

---

## 🛠️ Future Enhancements

- Integrate Alertmanager for failure thresholds  
- Add Redis streams for horizontal scaling  
- Deploy with Kubernetes and HPA  
- Add Sentry for error tracking  
- Define SLOs for reliability monitoring

---

> For a scalable, observable, and automated inventory workflow, InventoryRPA is your go-to solution.