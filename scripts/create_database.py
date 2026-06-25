import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

# ==========================================
# Paths
# ==========================================

PROCESSED = Path("../data/processed")
DATABASE = "../bluestock_mf.db"

# ==========================================
# Create SQLite Engine
# ==========================================

engine = create_engine(f"sqlite:///{DATABASE}")

print("=" * 70)
print("Creating SQLite Database")
print("=" * 70)

# ==========================================
# Load all processed CSV files
# ==========================================

csv_files = sorted(PROCESSED.glob("*.csv"))

print(f"\nFound {len(csv_files)} processed CSV files.\n")

for file in csv_files:

    try:

        print(f"Loading {file.name}...")

        df = pd.read_csv(file)

        table_name = file.stem.lower()

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"✓ {table_name} loaded ({len(df)} rows)\n")

    except Exception as e:

        print(f"❌ Error loading {file.name}")
        print(e)

print("=" * 70)
print("Database Created Successfully!")
print("=" * 70)

# ==========================================
# Verify Tables
# ==========================================

print("\nVerifying Tables...\n")

with engine.connect() as conn:

    for file in csv_files:

        table = file.stem.lower()

        count = pd.read_sql(
            f"SELECT COUNT(*) AS total_rows FROM '{table}'",
            conn
        )

        print(f"{table:<35} {count.iloc[0,0]} rows")

print("\nAll tables verified successfully!")