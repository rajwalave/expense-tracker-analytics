CREATE DATABASE IF NOT EXISTS expense_analytics;
USE expense_analytics;

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id VARCHAR(20) PRIMARY KEY,
    transaction_date DATE NOT NULL,
    category VARCHAR(50) NOT NULL,
    merchant VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    payment_method VARCHAR(40) NOT NULL,
    amount_inr DECIMAL(12,2) NOT NULL CHECK (amount_inr > 0),
    account_type VARCHAR(50) NOT NULL
);

CREATE INDEX idx_transactions_date ON transactions(transaction_date);
CREATE INDEX idx_transactions_category ON transactions(category);

-- After creating the table, import data/processed/transactions_clean.csv
-- with MySQL Workbench Table Data Import Wizard.
