from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
raw_path = ROOT / "data" / "raw" / "transactions_raw.csv"
out_path = ROOT / "data" / "processed" / "transactions_clean.csv"

df = pd.read_csv(raw_path)
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")
df["amount_inr"] = pd.to_numeric(df["amount_inr"], errors="coerce")
df["category"] = df["category"].astype("string").str.strip().str.title()
df["category"] = df["category"].replace({"Grocery": "Groceries"})
df["payment_method"] = df["payment_method"].astype("string").str.strip()
df["description"] = df["description"].fillna("No description provided")

before = len(df)
df = df.dropna(subset=["transaction_date", "amount_inr"])
df = df[df["amount_inr"] > 0].copy()
df["month"] = df["transaction_date"].dt.to_period("M").astype(str)
df["year"] = df["transaction_date"].dt.year
df["month_number"] = df["transaction_date"].dt.month
df["day_name"] = df["transaction_date"].dt.day_name()
df["is_weekend"] = df["transaction_date"].dt.dayofweek >= 5

out_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out_path, index=False, date_format="%Y-%m-%d")
print(f"Raw rows: {before:,}")
print(f"Clean rows: {len(df):,}")
print(f"Rows removed: {before - len(df):,}")
print(f"Saved: {out_path}")
