from feature_engineer import FeatureEngineer


def main():
    engineer = FeatureEngineer()

    # Load clean data
    clean_df = engineer.load_clean_data()

    # Create features
    feature_df = engineer.engineer_features(clean_df)

    # Insert features into database
    engineer.insert_feature_data(feature_df)


if __name__ == "__main__":
    main()
