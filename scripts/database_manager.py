import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


class DatabaseManager:
    def __init__(self):
        load_dotenv()
        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.DB_NAME = os.getenv("DB_NAME")
        self.engine = self._create_engine()

    def _create_engine(self):
        return create_engine(
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}/{self.DB_NAME}"
        )

    def get_tickers(self):
        """Fetch tickers from tickers_reference table."""
        query = "SELECT ticker FROM tickers_reference"
        tickers_df = pd.read_sql(query, self.engine)
        return tickers_df["ticker"].tolist()

    def insert_dataframe(self, df, table_name):
        """Insert a DataFrame into a table."""
        df.to_sql(name=table_name, con=self.engine, if_exists="append", index=False)
