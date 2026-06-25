-- ===============================
-- STAR SCHEMA
-- Mutual Fund Analytics
-- ===============================

CREATE TABLE dim_fund (

    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    risk_category TEXT,
    launch_date DATE

);

CREATE TABLE dim_date (

    date_id INTEGER PRIMARY KEY,
    date DATE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    day INTEGER

);

CREATE TABLE fact_nav (

    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date DATE,
    nav REAL,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)

);

CREATE TABLE fact_transactions (

    transaction_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    investor_id INTEGER,
    transaction_date DATE,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    kyc_status TEXT,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)

);

CREATE TABLE fact_performance (

    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL,
    sharpe_ratio REAL,
    beta REAL,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)

);

CREATE TABLE fact_aum (

    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_house TEXT,
    month DATE,
    aum_crore REAL

);