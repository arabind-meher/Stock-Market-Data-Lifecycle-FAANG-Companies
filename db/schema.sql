-- Create the stock_data database (only if it doesn't exist)
CREATE DATABASE IF NOT EXISTS stock;
USE stock;

-- 1. Create tickers_reference table
CREATE TABLE IF NOT EXISTS tickers_reference (
    ticker VARCHAR(10) PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL
);

-- 2. Create raw_stock_data table
CREATE TABLE IF NOT EXISTS raw_stock_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    date DATE NOT NULL,
    open_price FLOAT,
    high_price FLOAT,
    low_price FLOAT,
    close_price FLOAT,
    adj_close FLOAT,
    volume BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE KEY unique_ticker_date (ticker, date),
    INDEX idx_ticker (ticker),
    INDEX idx_date (date),

    FOREIGN KEY (ticker) REFERENCES tickers_reference(ticker)
);

-- 3. Create clean_stock_data table
CREATE TABLE IF NOT EXISTS clean_stock_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    date DATE NOT NULL,
    open_price FLOAT,
    high_price FLOAT,
    low_price FLOAT,
    close_price FLOAT,
    adj_close FLOAT,
    volume BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE KEY unique_ticker_date (ticker, date),
    INDEX idx_ticker (ticker),
    INDEX idx_date (date),

    FOREIGN KEY (ticker) REFERENCES tickers_reference(ticker)
);

-- 4. Create feature_stock_data table
CREATE TABLE IF NOT EXISTS feature_stock_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    date DATE NOT NULL,
    daily_return_pct FLOAT,
    moving_avg_5d FLOAT,
    moving_avg_10d FLOAT,
    volatility_5d FLOAT,
    rsi_14d FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE KEY unique_ticker_date (ticker, date),
    INDEX idx_ticker (ticker),
    INDEX idx_date (date),

    FOREIGN KEY (ticker) REFERENCES tickers_reference(ticker)
);
