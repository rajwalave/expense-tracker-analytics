# Expense Tracker Analytics & Spending Intelligence

An end-to-end **data analytics portfolio project** using Python, SQL, ETL, and Power BI to explore spending patterns, category trends, and monthly expense changes.

> **Dataset note:** The included transaction data is synthetic and generated for demonstration. It does not contain real personal financial information. Insights are examples, not claims about real spending behavior.

## Project goals
- Build a repeatable raw-to-clean ETL workflow.
- Analyze monthly, category, payment-method, and weekday/weekend spending.
- Produce reusable SQL queries and CSV reports.
- Prepare a Power BI dashboard with interactive filters.
- Document business questions, findings, and limitations.

## Sample metrics
The generated dataset contains **1,800 synthetic transactions** dated January 2025 through September 2026. Run the analysis script to calculate metrics from the data in your copy.

## Tech stack
- Python: pandas, NumPy, Matplotlib
- SQL: MySQL 8+
- Visualization: Power BI Desktop (separate install)
- Exploration: Jupyter Notebook

## Repository structure
```text
expense-tracker-analytics/
├── data/
│   ├── raw/transactions_raw.csv
│   └── processed/transactions_clean.csv
├── notebooks/01_expense_analytics_eda.ipynb
├── sql/schema.sql
├── sql/analysis_queries.sql
├── scripts/clean_data.py
├── scripts/analyze_data.py
├── dashboards/POWER_BI_GUIDE.md
├── images/
├── reports/
├── models/                  # reserved for optional future forecasting
├── requirements.txt
├── .gitignore
└── README.md
```

## Run it in VS Code (Windows)

### 1. Install Python
Install Python 3.10 or newer from https://www.python.org/downloads/windows/. During setup, enable **Add Python to PATH**.

### 2. Open the folder
Extract the ZIP, open VS Code, choose **File → Open Folder**, and select `expense-tracker-analytics`.

### 3. Open the terminal
In VS Code, choose **Terminal → New Terminal**.

### 4. Create and activate a virtual environment
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```
If PowerShell blocks activation, select Command Prompt as the VS Code terminal and run:
```bat
.venv\Scripts\activate.bat
```

### 5. Install packages
```bash
python -m pip install -r requirements.txt
```

### 6. Clean the raw data
```bash
python scripts/clean_data.py
```
This normalizes categories, fills missing descriptions, validates dates and amounts, and writes `data/processed/transactions_clean.csv`.

### 7. Run the analysis
```bash
python scripts/analyze_data.py
```
Review generated charts in `images/` and CSV/Markdown outputs in `reports/`.

### 8. Explore the notebook (optional)
```bash
jupyter notebook
```
Open `notebooks/01_expense_analytics_eda.ipynb` in the browser. You can also install the Jupyter extension in VS Code and open the notebook there.

## MySQL Workbench setup

1. Open MySQL Workbench and connect to your local MySQL Server.
2. Choose **File → Open SQL Script** and open `sql/schema.sql`.
3. Click the lightning-bolt Execute button.
4. In the SCHEMAS pane, refresh and select `expense_analytics`.
5. Right-click the `transactions` table and choose **Table Data Import Wizard**.
6. Select `data/processed/transactions_clean.csv` and map its columns to the matching table columns. Ensure the date is interpreted as `YYYY-MM-DD`.
7. Run queries from `sql/analysis_queries.sql`.

If the wizard has trouble with the CSV, use Python to load the clean CSV into MySQL or import through the wizard after checking the column mapping.

## Build the Power BI dashboard
Follow [`dashboards/POWER_BI_GUIDE.md`](dashboards/POWER_BI_GUIDE.md). The guide includes suggested visuals, slicers, and DAX measures. Power BI Desktop is separate; this repository provides the data and build instructions rather than a prebuilt `.pbix` file.

## Business questions
1. Which categories account for the most spending?
2. How does total spending change month to month?
3. Which payment methods are most frequently used?
4. Are average transaction amounts different on weekdays and weekends?
5. Which transactions are the largest and deserve a quick review?

## Data dictionary
| Column | Description |
|---|---|
| `transaction_id` | Unique synthetic transaction identifier |
| `transaction_date` | Transaction date |
| `category` | Normalized expense category |
| `merchant` | Example merchant label |
| `description` | Short transaction description |
| `payment_method` | UPI, card, cash, or net banking |
| `amount_inr` | Transaction amount in Indian rupees |
| `account_type` | Example account source |
| `month`, `year`, `month_number` | Derived calendar fields |
| `day_name`, `is_weekend` | Derived day-of-week features |

## Limitations
- Synthetic data is not representative of any particular person or population.
- No income or budget targets are provided, so savings cannot be calculated reliably.
- The project is descriptive analytics, not financial advice.
- No predictive model is included by default; build forecasting only after defining a meaningful target and evaluation method.

## Next improvements
- Add budget targets and budget-vs-actual reporting.
- Connect a real data source with consent and safe credential handling.
- Add automated tests and a scheduled ETL run.
- Add a forecasting model with time-based validation if it serves a clear use case.

## Author
Add your name, LinkedIn, and portfolio links here before publishing.
