
# Stock Data Lifecycle Project

## Overview
This project implements a complete **Stock Market Data Lifecycle**:
- Fetches historical stock price data using **Yahoo Finance API**.
- Stores raw and cleaned data into a **MySQL** database using **SQLAlchemy**.
- Applies **data cleaning** and **feature engineering** (moving averages, volatility, RSI).
- Conducts **interactive Exploratory Data Analysis (EDA)** with **Matplotlib**, **Seaborn**, and **ipywidgets**.

The project is organized using **Object-Oriented Programming (OOP)** principles for better modularity and scalability.

---

## Features
- **Automated Data Fetching** from Yahoo Finance.
- **Database Management** with SQLAlchemy (MySQL backend).
- **Preprocessing and Feature Engineering** (MA20, MA50, Volatility, RSI14).
- **Interactive Data Visualization** using widgets.
- **Versioned Release:** v1.0.0 (First Stable Release).

---

## Project Structure
```
├── scripts/
│   ├── fetch_data.py
│   ├── preprocess_data.py
│   ├── feature_engineering.py
│   └── eda.ipynb
├── database_manager.py
├── feature_engineer.py
├── README.md
```

---

## Tech Stack
- **Language:** Python
- **Database:** MySQL
- **Libraries:** 
  - pandas
  - yfinance
  - SQLAlchemy
  - matplotlib, seaborn
  - ipywidgets

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/arabind-meher/Stock-Market-Data-Lifecycle-FAANG-Companies.git
   ```

2. Set up a MySQL database and update connection strings if needed.

3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. Run scripts sequentially:
   - Fetch stock data
   - Preprocess the data
   - Apply feature engineering
   - Explore using EDA notebook

---

## Version History

| Version | Description               | Date        |
|---------|----------------------------|-------------|
| v1.0.0  | Initial complete pipeline | May 2025    |

---

## License
This project is licensed under the MIT License.

---

# Future Improvements
- Add ML models for stock trend prediction.
- Dockerize the entire project for easier deployment.
- Scheduled auto-updates for fetching latest data.
