from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed" / "transactions_clean.csv"
REPORTS = ROOT / "reports"
IMAGES = ROOT / "images"
REPORTS.mkdir(exist_ok=True)
IMAGES.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["transaction_date"])
df["month"] = df["transaction_date"].dt.to_period("M").astype(str)

monthly = df.groupby("month", as_index=False)["amount_inr"].sum()
monthly.to_csv(REPORTS / "monthly_spend.csv", index=False)

category = df.groupby("category", as_index=False).agg(
    total_spend=("amount_inr", "sum"),
    transaction_count=("transaction_id", "count"),
    average_transaction=("amount_inr", "mean"),
).sort_values("total_spend", ascending=False)
category.to_csv(REPORTS / "category_summary.csv", index=False)

top = df.nlargest(10, "amount_inr")
top.to_csv(REPORTS / "top_10_transactions.csv", index=False)

total = df["amount_inr"].sum()
avg = df["amount_inr"].mean()
largest = df.loc[df["amount_inr"].idxmax()]
summary = [
    "# Expense Analytics — Automated Summary",
    "",
    f"- Transactions analyzed: **{len(df):,}**",
    f"- Total recorded spend: **₹{total:,.2f}**",
    f"- Average transaction: **₹{avg:,.2f}**",
    f"- Highest transaction: **₹{largest['amount_inr']:,.2f}** ({largest['category']}, {largest['transaction_date'].date()})",
    f"- Highest-spend category: **{category.iloc[0]['category']}** (₹{category.iloc[0]['total_spend']:,.2f})",
    "",
    "> These are descriptive statistics from a synthetic demonstration dataset, not personal financial advice."
]
(REPORTS / "executive_summary.md").write_text("\n".join(summary), encoding="utf-8")

plt.figure(figsize=(10,5))
plt.plot(monthly["month"], monthly["amount_inr"], marker="o")
plt.title("Monthly Expense Trend")
plt.xlabel("Month"); plt.ylabel("Spend (INR)")
plt.xticks(rotation=55, ha="right"); plt.tight_layout()
plt.savefig(IMAGES / "monthly_expense_trend.png", dpi=160); plt.close()

plt.figure(figsize=(10,5))
cat_plot = category.sort_values("total_spend")
plt.barh(cat_plot["category"], cat_plot["total_spend"])
plt.title("Total Spending by Category")
plt.xlabel("Spend (INR)"); plt.tight_layout()
plt.savefig(IMAGES / "category_spending.png", dpi=160); plt.close()

print("Analysis complete. Check reports/ and images/.")
print("\n".join(summary))
