# ROI Evaluation for InventoryRPA

This ROI model evaluates the cost-benefit of the InventoryRPA automation system based on synthetic monitoring data, maintenance strategy, and operational assumptions.

---

## 📊 Executive Summary

- **Monthly Transactions**: 360,000  
- **Marginal Compute Cost/Transaction**: $0.00000036  
- **Fully Loaded Cost/Transaction**: $0.00135  
- **Labor Minutes Saved/Workflow**: 30 minutes  
- **Monthly Labor Savings**: $525  
- **Downtime Avoided**: 3 hours/month  
- **Downtime Savings**: $450  
- **Monthly Maintenance & Infra Cost**: $485.13  
- **Net Monthly Benefit**: $489.87  
- **One-Time Setup Cost**: $1,800  
- **Payback Period**: ~3.7 months  
- **Annual ROI**: 224%

---

## 📦 Assumptions

- **Volume**: 12,000 transactions/day × 30 days = 360,000/month  
- **CPU Time/Transaction**: 0.03 seconds  
- **Error Rate**: 1.0% with 80% retry success  
- **Compute Cost**: $0.000012 per CPU-second  
- **Engineer Rate**: $60/hour  
- **Ops Rate**: $35/hour  
- **Manual Workflow Time**: 35 minutes  
- **Automated Workflow Time**: 5 minutes  
- **Incident Frequency**: 2/month  
- **MTTR Reduction**: 2.0 → 0.5 hours  
- **Downtime Cost**: $150/hour  

---

## 💻 Cost Per Transaction

- **Compute Only**:  
  \( 0.03 \text{ sec} × \$0.000012 = \$0.00000036 \)  
- **Fully Loaded**:  
  \( \$485.13 / 360,000 = \$0.00135 \)

---

## ⏱️ Labor Savings

- **Time Saved/Run**: 30 minutes  
- **Monthly Runs**: 30  
- **Total Hours Saved**: 15  
- **Monthly Labor Savings**:  
  \( 15 × \$35 = \$525 \)

---

## 🚨 Downtime Avoided

- **Incidents/Month**: 2  
- **Hours Saved**: 3  
- **Monthly Downtime Savings**:  
  \( 3 × \$150 = \$450 \)

---

## 💰 Financial Model

| Item                         | Value       |
|------------------------------|-------------|
| Transactions/month           | 360,000     |
| Compute cost (incl. retries) | $0.13       |
| Email & notifications        | $5          |
| Maintenance engineering      | $480        |
| **Total monthly costs**      | **$485.13** |
| Labor savings                | $525        |
| Downtime savings             | $450        |
| **Total monthly benefits**   | **$975**    |
| **Net monthly benefit**      | **$489.87** |
| One-time setup cost          | $1,800      |
| **Payback period**           | **3.7 mo**  |
| **Annual ROI**               | **224%**    |

---

## 📈 Synthetic Projections

| Scenario     | Month 1 | Month 6 | Month 12 | 12-mo Total | Notes              |
|--------------|---------|---------|----------|-------------|--------------------|
| Conservative | 360k    | 360k    | 360k     | 4.32M       | 0% growth          |
| Expected     | 360k    | 459k    | 604k     | 6.44M       | 5% monthly growth  |
| Aggressive   | 360k    | 579k    | 935k     | 9.39M       | 10% monthly growth |

---

## 📊 Monitoring Plan Tie-In

- **SLIs**: success rate, error rate, retries, p95 latency, CPU seconds  
- **SLOs**: success ≥ 99.7%, p95 latency ≤ 60 ms, retries ≤ 2.0%  
- **Alerts**: error rate > 1.5%, p95 latency > 6 min  
- **Logs**: JSONL format, 90-day retention  

---

## 🛠️ Maintenance Plan Tie-In

- **Weekly Health Checks**: 1 hr  
- **Monthly Dependency Updates**: 2 hr  
- **On-Call Buffer**: 5 hr  
- **Total Monthly Maintenance**: 8 hr × $60 = $480  

---

## ⚠️ Risks & Sensitivity

- **Error Rate Spike**: 1% → 3% triples retry cost  
- **Maintenance Doubling**: 8 → 16 hrs reduces net benefit  
- **Labor Savings Halved**: ROI drops unless volume or reliability improves  

---

## ✅ Recommendations

- Harden retry logic and error taxonomy  
- Add canary mini-runs post-deploy  
- Track per-SKU anomalies to quantify data quality  
- Review actual vs projected ROI quarterly