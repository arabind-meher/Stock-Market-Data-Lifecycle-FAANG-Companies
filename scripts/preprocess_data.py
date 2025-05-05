from data_cleaner import DataCleaner


def main():
    cleaner = DataCleaner()

    # Load raw stock data
    raw_df = cleaner.load_raw_data()

    # Clean the raw stock data
    clean_df = cleaner.clean_data(raw_df)

    # Insert cleaned data
    cleaner.insert_clean_data(clean_df)


if __name__ == "__main__":
    main()
