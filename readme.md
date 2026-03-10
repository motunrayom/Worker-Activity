# Worker Activity & Continuity Tracking System


## 📌  Project Overview

This project analyzes worker activity logs to measure workforce continuity and stability. It identifies how consistently workers remain active over time without switching employers or roles, helping organizations assess workforce reliability, retention, and engagement patterns.


## 🎯  Problem Statement

Organizations managing distributed or contract-based workers often lack visibility into:

- Worker continuity and engagement trends

- Employer and role switching behavior

- Short-term inactivity gaps

- Workforce stability patterns

This solution processes worker activity logs and calculates a **continuity score** based on:

- Activity frequency (≤ 6-day gap)

- Employer consistency

- Role consistency

## 🛠 Tech Stack

- Python
- Pandas
- Datetime module
- CSV-based data processing

## ⚙️ How It Works

 1. Loads worker activity dataset.
 2. Sorts activity by Worker.
 3. Compares consecutive records.
 4. Checks:

  - Activity gap ≤ 6 days

  - No employer change

  - No role change
 5. Computes a continuity score.
 6. Outputs ranked results to results.csv.

## 📊 Output

|Worker   | Continuity|
|-------- | ----------|
| John    | 3 |
| Mary    | 2 |
| Paul  | 1|
