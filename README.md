# 🌑 Shadow Nirikshan Engine

**Shadow Nirikshan Engine** is a data-driven sustainability **decision support system**
designed to detect *invisible water and electricity waste* that occurs during
**periods of inactivity**.

<p align="center">
  <img src="assets/hero.png" alt="Shadow Nirikshan Engine Banner" width="800"/>
</p>


Built for **EXECUTE 5.0 Hackathon 2026**  
Theme: *Innovation for Sustainable Development*  
Team: **Binary Brains (IGDTUW)**

---

## 🚨 The Problem: Invisible Resource Waste

Most sustainability systems focus on **active usage**.
However, on Indian campuses and large facilities, the *largest losses* occur when:

- Buildings are empty
- Pumps are left ON overnight
- Lights and equipment run without intent
- Water tanks overflow silently

These losses are:
- ❌ Not visible
- ❌ Not reported
- ❌ Not intentional

We define this category as **Shadow Waste**.

---

## 💡 Our Insight: Absence Is a Signal

Instead of monitoring usage peaks,  
**Shadow Nirikshan Engine monitors silence**.

> If no activity is expected, any significant resource usage is suspicious.

This absence-driven intelligence is the core innovation of our system.

---

## 🧠 Solution Overview

Shadow Nirikshan Engine is a **scheduled analysis engine** that:

1. Ingests existing operational data (no new sensors)
2. Identifies **silence windows** using schedules
3. Learns **normal silence behavior** from historical data
4. Detects abnormal usage during inactivity
5. Generates **actionable decisions**, not just alerts

It is a **decision support system**, not a monitoring dashboard.

---

## 🏗️ System Architecture

Raw Data
↓
Silence Window Detection
↓
Baseline Learning (Normal Silence)
↓
Anomaly Detection (Shadow Waste)
↓
Decision & Action Generation


---

## 📊 Data Sources (Software-First)

Shadow Nirikshan works with **existing data**, even if imperfect:

- Electricity meter readings (building-level)
- Water pump ON/OFF logs
- Tank refill / tanker logs
- Class, lab, and hostel schedules
- Maintenance records

Designed specifically for **real Indian campuses** where data may be delayed,
manual, or incomplete.

---

## ⚙️ Tech Stack

- **Python 3**
- **Pandas / NumPy** — data processing
- **Streamlit** — demo interface
- **CSV-based ingestion** — no database dependency

---

## ▶️ How to Run the Pipeline (Terminal)

To run one complete **analysis cycle** from the terminal:

```bash
/usr/bin/python3 test_ingestion.py
```

## 🌍 Live Demo

👉 **Streamlit App:**  
https://shadow-nirikshan-engine.streamlit.app/

*(The demo simulates a scheduled analysis cycle and displays detected shadow waste with actionable recommendations.)*

