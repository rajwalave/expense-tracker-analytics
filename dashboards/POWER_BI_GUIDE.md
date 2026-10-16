# Power BI Dashboard Guide

This repository includes a Power BI-ready clean CSV. Power BI Desktop is a separate application and a `.pbix` file is not included.

## Load the data
1. Open Power BI Desktop.
2. Choose **Get data → Text/CSV**.
3. Select `data/processed/transactions_clean.csv`.
4. Choose **Transform Data** if you want to inspect column types; set `transaction_date` to Date and `amount_inr` to Decimal Number.
5. Select **Close & Apply**.

## Suggested report layout
- KPI cards: Total Spend, Transaction Count, Average Transaction.
- Line chart: `month` on X-axis and Sum of `amount_inr` on Y-axis.
- Bar chart: `category` by Sum of `amount_inr`.
- Donut chart: `payment_method` by transaction count.
- Table: date, category, merchant, payment method, amount.
- Slicers: year, month, category, payment method, account type.

## Suggested DAX measures
```DAX
Total Spend = SUM(transactions_clean[amount_inr])

Transaction Count = COUNTROWS(transactions_clean)

Average Transaction = DIVIDE([Total Spend], [Transaction Count])

Spend Previous Month =
CALCULATE([Total Spend], DATEADD(transactions_clean[transaction_date], -1, MONTH))

Month-over-Month Change =
[Total Spend] - [Spend Previous Month]

Month-over-Month Change % =
DIVIDE([Month-over-Month Change], [Spend Previous Month])
```

If Power BI names the imported table differently, replace `transactions_clean` in the measures with the actual table name. For time-intelligence DAX, add a calendar table and mark it as a date table for a more robust model.
