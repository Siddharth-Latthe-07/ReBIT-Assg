import os
from src.mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from src.mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def clean_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Perform data cleaning steps here.
        - Handle missing values
        - Remove duplicates
        - Format columns, etc.
        - Remove outliers
        """
        logger.info("Starting data cleaning process")

        # Remove duplicates
        data.drop_duplicates(inplace=True)
        
        # Handle missing values
        data.dropna(inplace=True)
        
        # Detect and remove outliers
        logger.info("Detecting and removing outliers")
        data = self.remove_outliers(data)

        # Reset index after cleaning
        data.reset_index(drop=True, inplace=True)
        
        logger.info("Data cleaning completed")
        logger.info(f"Data shape after cleaning: {data.shape}")

        return data

    def remove_outliers(self, data: pd.DataFrame, numeric_threshold: float = 3.0, categorical_threshold: float = 0.01) -> pd.DataFrame:
        """
        Remove outliers using:
        - Z-score method for numerical columns
        - Frequency threshold for categorical columns
        """
        # Handle numerical outliers using Z-score
        numeric_columns = data.select_dtypes(include=[np.number]).columns
        if not numeric_columns.empty:
            logger.info(f"Numeric columns for outlier detection: {list(numeric_columns)}")
            z_scores = np.abs((data[numeric_columns] - data[numeric_columns].mean()) / data[numeric_columns].std())
            data = data[(z_scores < numeric_threshold).all(axis=1)]
            logger.info(f"Data shape after removing numerical outliers: {data.shape}")

        # Handle categorical outliers using frequency threshold
        categorical_columns = data.select_dtypes(include=["object", "category"]).columns
        if not categorical_columns.empty:
            logger.info(f"Categorical columns for outlier detection: {list(categorical_columns)}")
            for col in categorical_columns:
                category_frequencies = data[col].value_counts(normalize=True)
                rare_categories = category_frequencies[category_frequencies < categorical_threshold].index
                logger.info(f"Rare categories in '{col}' below threshold ({categorical_threshold}): {list(rare_categories)}")
                
                # Remove rows containing rare categories
                data = data[~data[col].isin(rare_categories)]
                logger.info(f"Data shape after removing outliers from '{col}': {data.shape}")

        return data

    def train_test_spliting(self):
        """
        Perform train-test split and save the datasets as CSV files.
        """
        logger.info("Loading data for train-test splitting")
        data = pd.read_csv(self.config.data_path)

        # Clean the data
        logger.info("Cleaning the data before splitting")
        data = self.clean_data(data)

        # Split the data into training and test sets (75% train, 25% test).
        train, test = train_test_split(data, test_size=0.25, random_state=42)

        # Save the train and test sets
        train_path = os.path.join(self.config.root_dir, "train.csv")
        test_path = os.path.join(self.config.root_dir, "test.csv")
        train.to_csv(train_path, index=False)
        test.to_csv(test_path, index=False)

        logger.info("Split data into training and test sets")
        logger.info(f"Train set shape: {train.shape}")
        logger.info(f"Test set shape: {test.shape}")

        print(f"Train shape: {train.shape}")
        print(f"Test shape: {test.shape}")
