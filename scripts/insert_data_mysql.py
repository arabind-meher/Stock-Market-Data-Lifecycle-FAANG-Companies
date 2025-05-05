from database_manager import DatabaseManager
from stock_fetcher import StockFetcher


def main():
    db = DatabaseManager()
    fetcher = StockFetcher()

    tickers = db.get_tickers()
    df = fetcher.fetch_multiple_stocks(tickers)

    if not df.empty:
        df.rename(
            columns={
                "Date": "date",
                "Open": "open_price",
                "High": "high_price",
                "Low": "low_price",
                "Close": "close_price",
                "Volume": "volume",
            },
            inplace=True,
        )

        print(f"Inserting {len(df)} rows into raw_stock_data...")
        db.insert_dataframe(df, table_name="raw_stock_data")
        print("Data insertion complete.")
    else:
        print("No data fetched. Nothing to insert.")


if __name__ == "__main__":
    main()
