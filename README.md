# Mutual Fund Analytics Platform

## Overview

This project is part of the **Bluestock Fintech Capstone Project**. It focuses on building a complete data pipeline for mutual fund analytics, including data ingestion, cleaning, database creation, and analytical SQL queries.

---

## Project Structure

```text
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── data_ingestion.py
│   ├── live_nav_fetch.py
│   ├── clean_data.py
│   ├── create_database.py
│   └── check_database.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── reports/
│   ├── data_ingestion_report.txt
│   ├── data_quality_summary.md
│   └── data_dictionary.md
│
├── dashboard/
├── notebooks/
├── requirements.txt
├── README.md
└── bluestock_mf.db
```

---

## Features

* Data ingestion of 10 mutual fund datasets
* Live NAV retrieval using MFAPI
* Data quality assessment
* Data cleaning and preprocessing
* SQLite database creation using SQLAlchemy
* Analytical SQL queries
* Data dictionary and documentation

---

## Technologies Used

* Python
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Requests
* Jupyter Notebook
* Git & GitHub

---

## Day 1 Deliverables

* Project folder structure
* Data ingestion pipeline
* Live NAV API integration
* Fund Master exploration
* AMFI code validation
* Data quality assessment

---

## Day 2 Deliverables

* Data cleaning and preprocessing
* Processed datasets generation
* SQLite database creation
* Star schema design
* Analytical SQL queries
* Data dictionary

---

## How to Run

### Clone the repository

```bash
git clone <repository-url>
cd MutualFundAnalytics
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run data ingestion

```bash
python scripts/data_ingestion.py
```

### Fetch live NAV

```bash
python scripts/live_nav_fetch.py
```

### Clean datasets

```bash
python scripts/clean_data.py
```

### Create SQLite database

```bash
python scripts/create_database.py
```

### Verify database

```bash
python scripts/check_database.py
```

---

## Outputs

* Cleaned datasets in `data/processed/`
* SQLite database (`bluestock_mf.db`)
* SQL schema (`sql/schema.sql`)
* Analytical SQL queries (`sql/queries.sql`)
* Data quality report
* Data dictionary

---

## Author

**Dhanashri Shivdas**
