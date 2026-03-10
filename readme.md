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
 6. Outputs ranked results to `results.csv`.

## 📊 Example Input Dataset

```
Worker,Employer,Role,Date
1435,234,86,01/01/2020 17:00
1435,234,86,04/01/2020 12:30
1435,234,86,08/01/2020 07:00
135,45,696,25/01/2020 18:00
135,45,95,27/01/2020 18:00
135,45,95,29/01/2020 22:15
456,78,576,02/02/2020 05:00
456,78,576,29/11/2020 14:30

```

## 📊 Output Sample

```

|Worker   | Continuity|
|-------- | ----------|
| John    | 3 |
| Mary    | 2 |
| Paul  | 1|

```
The output is saved as: 

```
results.csv

```
---

## 🚀 How to Set Up & Run the Project

#### 1. Clone the GitHub Repository
Open your terminal and run the following command:

``` bash
git clone https://github.com/motunrayom/Worker-Activity.git
cd Worker-Activity
```
---

#### 2. Add the dataset 
Place your CSV dataset in the project directory.
If the file is not located in the project directory, the script will prompt you to provide the correct file path.

---

#### 3. Run the script

``` bash

python worker_continuity.py

```

---

#### 4. Output

The results of the analysis will be saved as `results.csv` in the project directory

---

## ⚡ Automation

To automate execution:
 - A bash script is included to run the Python script automatically.
 - You can schedule the script using:
   - Windows Task Scheduler
   - Cron Jobs (Linux/Mac)

---

## 📂 Project Structure

```
Worker-Activity
│
├── worker_continuity.py # Main script for calculating worker continuity
├── worker_activity.csv # Input dataset (sample)
├── results.csv # Output generated after running the script
├── run.sh # Bash script for automation (optional)
└── README.md # Project documentation

```