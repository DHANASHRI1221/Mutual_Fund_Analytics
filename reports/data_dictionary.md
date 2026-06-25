# Data Dictionary

## 01_fund_master.csv

| Column        | Data Type | Description              |
| ------------- | --------- | ------------------------ |
| amfi_code     | Integer   | Unique AMFI Scheme Code  |
| scheme_name   | Text      | Mutual Fund Scheme Name  |
| fund_house    | Text      | Asset Management Company |
| category      | Text      | Equity/Debt Category     |
| sub_category  | Text      | Detailed Fund Category   |
| risk_category | Text      | Risk Level               |
| launch_date   | Date      | Scheme Launch Date       |

---

## 02_nav_history.csv

| Column    | Data Type | Description     |
| --------- | --------- | --------------- |
| amfi_code | Integer   | Scheme Code     |
| date      | Date      | NAV Date        |
| nav       | Float     | Net Asset Value |

---

## 03_aum_by_fund_house.csv

Stores monthly Assets Under Management (AUM) for each fund house.

---

## 04_monthly_sip_inflows.csv

Contains monthly SIP inflows and YoY growth.

---

## 05_category_inflows.csv

Contains monthly inflow/outflow by mutual fund category.

---

## 06_industry_folio_count.csv

Stores folio counts across the mutual fund industry.

---

## 07_scheme_performance.csv

Contains historical returns, Sharpe Ratio, Beta, Alpha and Expense Ratio.

---

## 08_investor_transactions.csv

Contains investor purchase, SIP, redemption and KYC information.

---

## 09_portfolio_holdings.csv

Contains fund portfolio holdings.

---

## 10_benchmark_indices.csv

Contains benchmark index prices used for comparison.

---

## Data Sources

* Bluestock Capstone Dataset
* MFAPI (https://api.mfapi.in/)
