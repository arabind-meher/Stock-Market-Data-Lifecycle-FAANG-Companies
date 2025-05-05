from database_manager import DatabaseManager
from stock_fetcher import StockFetcher

if __name__ == "__main__":
    db = DatabaseManager()
    fetcher = StockFetcher()

    tickers = db.get_tickers()
    df = fetcher.fetch_multiple_stocks(tickers)

    print(df.head())  # Check output
    # (Later) db.insert_dataframe(df, 'raw_stock_data')
