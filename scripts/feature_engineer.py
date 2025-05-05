import pandas as pd

from database_manager import DatabaseManager


class FeatureEngineer:
    def __init__(self):
        self.db = DatabaseManager()

    def load_clean_data(self):
        """Load cleaned stock data from database."""
        query = "SELECT * FROM clean_stock_data"
        df = pd.read_sql(query, self.db.engine)
        return df

    def engineer_features(self, df):
        """Create new features for machine learning."""
        print(f"Original data shape: {df.shape}")

        # Sort data by ticker and date
        df.sort_values(by=["ticker", "date"], inplace=True)

        # Create daily returns
        df["daily_return"] = df.groupby("ticker")["close_price"].pct_change()

        # Create moving averages (20-day and 50-day)
        df["ma_20"] = df.groupby("ticker")["close_price"].transform(
            lambda x: x.rolling(window=20, min_periods=1).mean()
        )
        df["ma_50"] = df.groupby("ticker")["close_price"].transform(
            lambda x: x.rolling(window=50, min_periods=1).mean()
        )

        # Create rolling volatility (20-day standard deviation)
        df["volatility_20"] = df.groupby("ticker")["close_price"].transform(
            lambda x: x.rolling(window=20, min_periods=1).std()
        )

        # Create RSI (Relative Strength Index) (14-day)
        df = self._add_rsi(df, window=14)

        print(f"Feature engineered data shape: {df.shape}")
        return df

    def _add_rsi(self, df, window=14):
        """Helper method to calculate RSI."""
        diff = df.groupby("ticker")["close_price"].diff()

        gain = diff.clip(lower=0)
        loss = -diff.clip(upper=0)

        avg_gain = gain.groupby(df["ticker"]).transform(
            lambda x: x.rolling(window=window, min_periods=1).mean()
        )
        avg_loss = loss.groupby(df["ticker"]).transform(
            lambda x: x.rolling(window=window, min_periods=1).mean()
        )

        rs = avg_gain / (avg_loss + 1e-10)  # small constant to avoid division by zero
        rsi = 100 - (100 / (1 + rs))

        df["rsi_14"] = rsi
        return df

    def insert_feature_data(self, feature_df):
        """Insert feature data into feature_stock_data table."""
        feature_df.to_sql(
            name="feature_stock_data",
            con=self.db.engine,
            if_exists="append",
            index=False,
        )
        print("Feature data inserted into feature_stock_data.")
