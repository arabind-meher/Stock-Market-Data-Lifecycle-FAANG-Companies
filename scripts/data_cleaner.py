import pandas as pd

from database_manager import DatabaseManager


class DataCleaner:
    def __init__(self):
        self.db = DatabaseManager()

    def load_raw_data(self):
        """Load raw stock data from database."""
        query = "SELECT * FROM raw_stock_data"
        df = pd.read_sql(query, self.db.engine)
        return df

    def clean_data(self, df):
        """Clean raw stock data."""
        print(f"Original data shape: {df.shape}")

        # Drop duplicates based on ticker and date
        df.drop_duplicates(subset=["ticker", "date"], inplace=True)

        # Drop rows with any missing critical values
        df.dropna(
            subset=[
                "ticker",
                "date",
                "open_price",
                "high_price",
                "low_price",
                "close_price",
                "volume",
            ],
            inplace=True,
        )

        # Convert 'date' to datetime format (if needed)
        df["date"] = pd.to_datetime(df["date"])

        # Remove rows with impossible values (negative prices/volume)
        df = df[
            (df["open_price"] >= 0)
            & (df["high_price"] >= 0)
            & (df["low_price"] >= 0)
            & (df["close_price"] >= 0)
            & (df["volume"] >= 0)
        ]

        print(f"Cleaned data shape: {df.shape}")
        return df

    def insert_clean_data(self, clean_df):
        """Insert cleaned data into clean_stock_data table."""
        clean_df.to_sql(
            name="clean_stock_data", con=self.db.engine, if_exists="append", index=False
        )
        print("Clean data inserted into clean_stock_data.")
