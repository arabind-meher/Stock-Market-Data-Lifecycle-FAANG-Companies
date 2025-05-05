# Stock Market Data Lifecycle Project

## Overview

This project implements a full data lifecycle process for stock market data, focusing on FAANG companies (Facebook,
Amazon, Apple, Netflix, and Google).  
It covers data extraction, storage, feature engineering, exploratory data analysis (EDA), and visualization, preparing
the data for future machine learning models.

---

## Project Structure

- **Database**: MySQL
- **Programming Language**: Python 3.12.6
- **IDE**: PyCharm Professional (Student License)
- **Data Source**: Yahoo Finance via yfinance API
- **Data Scope**: 2019 to 2025 (up to the latest available data)

---

## Key Steps

1. **Data Extraction**
    - Automated fetching of stock data using Yahoo Finance API.

2. **Data Storage**
    - Raw data stored into MySQL (`raw_stock_data` table).
    - Feature engineered data stored separately (`feature_stock_data` table).

3. **Feature Engineering**
    - Added technical indicators: Moving Averages, Volatility, RSI, and Daily Returns.

4. **Exploratory Data Analysis (EDA)**
    - Basic visualizations: Line plots for stock prices.
    - COVID-19 Crash analysis (February - April 2020).
    - Volatility comparison across stocks.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-lifecycle-project.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Setup MySQL database:
    - Create the `stock` database using provided `schema.sql`.
    - Update database credentials in `config.yaml`.

5. Run the following scripts sequentially:
    - `scripts/fetch_data.py`
    - `scripts/insert_data_mysql.py`
    - `scripts/feature_engineering.py`
    - `scripts/eda.py` (or EDA.ipynb)

---

## Tools and Libraries Used

- **Python** (pandas, matplotlib, seaborn, SQLAlchemy, yfinance, ipywidgets)
- **MySQL**
- **SQLAlchemy**
- **PyCharm IDE**

---

## Future Improvements

- Build and train machine learning models for price prediction or trend classification.
- Deploy a dashboard for live stock analysis.
- Integrate news sentiment analysis as external features.

---

## Author

- **Name**: Arabind Meher
- **LinkedIn**: [linkedin.com/in/arabind-meher](https://www.linkedin.com/in/arabind-meher)
- **GitHub**: [github.com/arabind-meher](https://github.com/arabind-meher)

---
