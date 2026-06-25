# Data Quality Summary

## Mutual Fund Analytics Platform

**Day 1 – Data Ingestion & Initial Data Validation**

---

## Project Objectives Completed

* Created the required project folder structure.
* Loaded all provided mutual fund datasets into Pandas.
* Retrieved live NAV data from the MFAPI.
* Performed initial data quality assessment.
* Explored Fund Master metadata.
* Validated AMFI Scheme Codes against NAV history.

---

# Dataset Summary

### Original Datasets Loaded

| Dataset                      | Status   |
| ---------------------------- | -------- |
| 01_fund_master.csv           | ✅ Loaded |
| 02_nav_history.csv           | ✅ Loaded |
| 03_aum_by_fund_house.csv     | ✅ Loaded |
| 04_monthly_sip_inflows.csv   | ✅ Loaded |
| 05_category_inflows.csv      | ✅ Loaded |
| 06_industry_folio_count.csv  | ✅ Loaded |
| 07_scheme_performance.csv    | ✅ Loaded |
| 08_investor_transactions.csv | ✅ Loaded |
| 09_portfolio_holdings.csv    | ✅ Loaded |
| 10_benchmark_indices.csv     | ✅ Loaded |

### Live NAV Data Retrieved

* HDFC Top 100 Direct
* SBI Bluechip
* ICICI Bluechip
* Nippon Large Cap
* Axis Bluechip
* Kotak Bluechip

---

# Initial Data Validation

The following validation checks were successfully completed for every dataset:

* Dataset loaded successfully.
* Dataset dimensions verified using `.shape`.
* Data types verified using `.dtypes`.
* Sample records inspected using `.head()`.
* Missing values identified.
* Duplicate records checked.

---

# Data Quality Assessment

## Missing Values

Only one dataset contains missing values.

| Dataset                    | Column         | Missing Values | Observation                                                                                                                |
| -------------------------- | -------------- | -------------: | -------------------------------------------------------------------------------------------------------------------------- |
| 04_monthly_sip_inflows.csv | yoy_growth_pct |             12 | Expected because the initial months do not have previous-year values required for Year-over-Year (YoY) growth calculation. |

All remaining datasets contain **no missing values**.

---

## Duplicate Records

No duplicate records were detected in any dataset.

**Duplicate Check Status:** ✅ Passed

---

## Data Type Observations

Several date-related columns are currently stored as **object** datatype.

Examples include:

* launch_date
* date
* month
* transaction_date
* portfolio_date

These columns will be converted to `datetime` format during the data preprocessing phase (Day 2).

---

# Fund Master Exploration

The Fund Master dataset contains:

| Metric          | Count |
| --------------- | ----: |
| Fund Houses     |    10 |
| Categories      |     2 |
| Sub-Categories  |    12 |
| Risk Categories |     5 |

### Categories Identified

* Equity
* Debt

### Risk Categories

* Low
* Moderate
* Moderately High
* High
* Very High

---

# AMFI Scheme Code Validation

A sample of AMFI Scheme Codes and corresponding scheme names was inspected to understand the dataset structure.

Validation was performed by comparing all AMFI Scheme Codes present in the **Fund Master** dataset against the **NAV History** dataset.

### Validation Result

* Missing Codes: `set()`
* Extra Codes: `set()`

**Status:** ✅ PASSED

All AMFI Scheme Codes in the Fund Master dataset were successfully validated against the NAV History dataset. No missing or unexpected scheme codes were detected.

---

# Overall Assessment

| Check                   | Status   |
| ----------------------- | -------- |
| File Loading            | ✅ Passed |
| Schema Validation       | ✅ Passed |
| Missing Value Analysis  | ✅ Passed |
| Duplicate Check         | ✅ Passed |
| Fund Master Exploration | ✅ Passed |
| AMFI Code Validation    | ✅ Passed |
| Live NAV Retrieval      | ✅ Passed |

---

# Conclusion

The Day 1 data ingestion pipeline was successfully completed.

All required datasets were loaded, validated, and inspected. Initial data quality checks indicate that the datasets are suitable for further preprocessing. The only identified issue is the presence of expected missing values in the `yoy_growth_pct` column of the monthly SIP inflows dataset.

The project is now ready to proceed to **Day 2: Data Cleaning, Preprocessing, and SQLite Database Design**.
