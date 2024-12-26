import os
from src.mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
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
        """
        logger.info("Starting data cleaning process")

        # Example cleaning steps
        data.drop_duplicates(inplace=True)  # Remove duplicate rows
        data.dropna(inplace=True)  # Remove rows with missing values
        data.reset_index(drop=True, inplace=True)  # Reset index after cleaning
        
        logger.info("Data cleaning completed")
        logger.info(f"Data shape after cleaning: {data.shape}")

        return data


    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up


    def train_test_spliting(self):
        logger.info("Loading data for train-test splitting")
        data = pd.read_csv(self.config.data_path)

        # Clean the data
        logger.info("Cleaning the data before splitting")
        data = self.clean_data(data)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)