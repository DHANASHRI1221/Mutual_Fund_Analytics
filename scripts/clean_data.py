import pandas as pd
from pathlib import Path

RAW = Path("../data/raw")
PROCESSED = Path("../data/processed")
PROCESSED.mkdir(exist_ok=True)

# ==============================
# Clean NAV History
# ==============================

print("Cleaning NAV History...")

nav = pd.read_csv(RAW / "02_nav_history.csv")

# Convert date column
nav["date"] = pd.to_datetime(nav["date"])

# Sort by scheme and date
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicate rows
nav = nav.drop_duplicates()

# Forward fill missing NAV values within each scheme
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Validate NAV values
assert (nav["nav"] > 0).all(), "Invalid NAV values found."

# Save cleaned file
nav.to_csv(PROCESSED / "clean_nav_history.csv", index=False)

print("✓ clean_nav_history.csv saved")

# ==============================
# Clean Investor Transactions
# ==============================

print("\nCleaning Investor Transactions...")

txn = pd.read_csv(RAW / "08_investor_transactions.csv")

# Convert transaction_date to datetime
txn["transaction_date"] = pd.to_datetime(txn["transaction_date"])

# Standardize transaction types
txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

# Validate allowed transaction types
allowed_types = ["Sip", "Lumpsum", "Redemption"]

invalid_transactions = txn[
    ~txn["transaction_type"].isin(allowed_types)
]

if len(invalid_transactions) == 0:
    print("✓ Transaction types validated")
else:
    print("Invalid Transaction Types Found:")
    print(invalid_transactions["transaction_type"].unique())

# Validate transaction amount
assert (txn["amount_inr"] > 0).all(), "Negative or zero transaction amount found."

print("✓ Transaction amounts validated")

# Validate KYC Status
allowed_kyc = ["Verified", "Pending"]

invalid_kyc = txn[
    ~txn["kyc_status"].isin(allowed_kyc)
]

if len(invalid_kyc) == 0:
    print("✓ KYC Status validated")
else:
    print("Invalid KYC Values:")
    print(invalid_kyc["kyc_status"].unique())

# Remove duplicates if any
txn = txn.drop_duplicates()

# Save cleaned dataset
txn.to_csv(
    PROCESSED / "clean_investor_transactions.csv",
    index=False
)

print("✓ clean_investor_transactions.csv saved")

# ==============================
# Clean Scheme Performance
# ==============================

print("\nCleaning Scheme Performance...")

perf = pd.read_csv(RAW / "07_scheme_performance.csv")

# Columns that should be numeric
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct",
    "aum_crore"
]

# Convert numeric columns
for col in numeric_cols:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

print("✓ Numeric columns validated")

# Check for missing numeric values
missing_numeric = perf[numeric_cols].isnull().sum()

print("\nMissing Numeric Values")
print(missing_numeric)

# Validate expense ratio
invalid_expense = perf[
    (perf["expense_ratio_pct"] < 0.1) |
    (perf["expense_ratio_pct"] > 2.5)
]

if invalid_expense.empty:
    print("✓ Expense Ratio validation passed")
else:
    print("Expense Ratio anomalies found:")
    print(invalid_expense[["scheme_name", "expense_ratio_pct"]])

# Flag unusual return values
anomalies = perf[
    (perf["return_1yr_pct"] < -100) |
    (perf["return_1yr_pct"] > 200)
]

print(f"Return anomalies found: {len(anomalies)}")

# Remove duplicate rows
perf = perf.drop_duplicates()

# Save cleaned dataset
perf.to_csv(
    PROCESSED / "clean_scheme_performance.csv",
    index=False
)

print("✓ clean_scheme_performance.csv saved")

# ==============================
# Copy Remaining Datasets
# ==============================

print("\nCopying Remaining Datasets...")

files_to_copy = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files_to_copy:
    df = pd.read_csv(RAW / file)
    df.to_csv(PROCESSED / file, index=False)
    print(f"✓ {file} copied")

print("\nAll cleaned datasets saved successfully!")