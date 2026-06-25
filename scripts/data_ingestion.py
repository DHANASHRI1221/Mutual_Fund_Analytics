import pandas as pd
from pathlib import Path

# ==============================
# Paths
# ==============================

DATA_PATH = Path("../data/raw")
REPORT_PATH = Path("../reports/data_ingestion_report.txt")

# ==============================
# Load CSV Files
# ==============================

csv_files = list(DATA_PATH.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files.\n")

datasets = {}

with open(REPORT_PATH, "w", encoding="utf-8") as report:

    report.write("MUTUAL FUND ANALYTICS - DATA INGESTION REPORT\n")
    report.write("=" * 80 + "\n\n")

    for file in csv_files:

        df = pd.read_csv(file)
        datasets[file.name] = df

        # ---------------- Console Output ----------------

        print("=" * 80)
        print(file.name)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\n" + "=" * 80 + "\n")

        # ---------------- Report Output ----------------

        report.write("=" * 80 + "\n")
        report.write(f"{file.name}\n\n")

        report.write(f"Shape : {df.shape}\n\n")

        report.write("Data Types:\n")
        report.write(df.dtypes.to_string())
        report.write("\n\n")

        report.write("First 5 Rows:\n")
        report.write(df.head().to_string())
        report.write("\n\n")

        report.write("Missing Values:\n")
        report.write(df.isnull().sum().to_string())
        report.write("\n\n")

        report.write(f"Duplicate Rows : {df.duplicated().sum()}\n\n")

    # =====================================================
    # Explore Fund Master
    # =====================================================

    fund_master = datasets["01_fund_master.csv"]

    print("\n" + "=" * 80)
    print("FUND MASTER EXPLORATION")
    print("=" * 80)

    print("\nUnique Fund Houses")
    print(fund_master["fund_house"].unique())

    print("\nUnique Categories")
    print(fund_master["category"].unique())

    print("\nUnique Sub Categories")
    print(fund_master["sub_category"].unique())

    print("\nUnique Risk Categories")
    print(fund_master["risk_category"].unique())

    print("\nNumber of Fund Houses :", fund_master["fund_house"].nunique())
    print("Number of Categories :", fund_master["category"].nunique())
    print("Number of Sub Categories :", fund_master["sub_category"].nunique())
    print("Number of Risk Categories :", fund_master["risk_category"].nunique())

    print("\nSample AMFI Scheme Codes")
    print(fund_master[["amfi_code", "scheme_name"]].head())

    # Save to report

    report.write("\n")
    report.write("=" * 80 + "\n")
    report.write("FUND MASTER EXPLORATION\n")
    report.write("=" * 80 + "\n\n")

    report.write(f"Number of Fund Houses : {fund_master['fund_house'].nunique()}\n")
    report.write(f"Number of Categories : {fund_master['category'].nunique()}\n")
    report.write(f"Number of Sub Categories : {fund_master['sub_category'].nunique()}\n")
    report.write(f"Number of Risk Categories : {fund_master['risk_category'].nunique()}\n\n")

    report.write("Fund Houses:\n")
    report.write(str(fund_master["fund_house"].unique()))
    report.write("\n\n")

    report.write("Categories:\n")
    report.write(str(fund_master["category"].unique()))
    report.write("\n\n")

    report.write("Sub Categories:\n")
    report.write(str(fund_master["sub_category"].unique()))
    report.write("\n\n")

    report.write("Risk Categories:\n")
    report.write(str(fund_master["risk_category"].unique()))
    report.write("\n\n")

    report.write("\nSample AMFI Scheme Codes\n")
    report.write(
    fund_master[["amfi_code", "scheme_name"]]
    .head()
    .to_string(index=False)
    )
    report.write("\n\n")

    # =====================================================
    # Validate AMFI Codes
    # =====================================================

    nav_history = datasets["02_nav_history.csv"]

    master_codes = set(fund_master["amfi_code"])
    nav_codes = set(nav_history["amfi_code"])

    missing_codes = master_codes - nav_codes
    extra_codes = nav_codes - master_codes

    print("\n" + "=" * 80)
    print("AMFI CODE VALIDATION")
    print("=" * 80)

    print("Missing Codes :", missing_codes)
    print("Extra Codes :", extra_codes)

    report.write("=" * 80 + "\n")
    report.write("AMFI CODE VALIDATION\n")
    report.write("=" * 80 + "\n\n")


    report.write(f"Missing Codes : {missing_codes}\n")
    report.write(f"Extra Codes : {extra_codes}\n\n")

    if len(missing_codes) == 0 and len(extra_codes) == 0:
        report.write("Validation Result : PASSED\n")
        print("\nValidation Result : PASSED")
    else:
        report.write("Validation Result : FAILED\n")
        print("\nValidation Result : FAILED")

print("\nData ingestion completed successfully!")
print(f"Report saved to: {REPORT_PATH}")