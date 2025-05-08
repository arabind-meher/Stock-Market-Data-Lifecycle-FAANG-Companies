from datetime import datetime

import pandas as pd
import yfinance as yf


class StockFetcher:
    def __init__(self, start_date="2019-01-01", end_date=None):
        self.start_date = start_date
        self.end_date = end_date or datetime.today().strftime("%Y-%m-%d")

    def fetch_stock(self, ticker):
        """Download stock data for a single ticker."""
        print(f"Fetching {ticker}...")
        data = yf.download(
            tickers=ticker,
            start=self.start_date,
            end=self.end_date,
            interval="1d",
            group_by="ticker",
            auto_adjust=True,
        )

        if not data.empty:
            if isinstance(data.columns, pd.MultiIndex):
                # If data columns are multi-indexed
                data.columns = data.columns.get_level_values(1)

            data.reset_index(inplace=True)
            data["ticker"] = ticker

            # Select only the clean columns
            data = data[["Date", "Open", "High", "Low", "Close", "Volume", "ticker"]]
            return data
        else:
            print(f"Warning: No data fetched for {ticker}")
            return pd.DataFrame()

    def fetch_multiple_stocks(self, tickers):
        """Download stock data for multiple tickers."""
        all_data = []
        for ticker in tickers:
            print(f"Fetching {ticker}...")
            stock_data = self.fetch_stock(ticker)
            if not stock_data.empty:
                all_data.append(stock_data)
        if all_data:
            return pd.concat(all_data, ignore_index=True)
        else:
            print("No data fetched.")
            return pd.DataFrame()
