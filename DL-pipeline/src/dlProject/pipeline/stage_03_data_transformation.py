# src/stage_03_data_transformation.py

from src.dlProject.config.configuration import ConfigurationManager
from src.dlProject.components.data_transformation import DataTransformation
from src.dlProject import logger

STAGE_NAME = "DATA TRANSFORMATION STAGE"

class DataTransformationPipeline:
    """Final data transformation pipeline class"""
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        
        # Data cleaning: Resize images, handle invalid images
        data_transformation.clean_data()
        
        # Handle outliers: Placeholder logic
        data_transformation.handle_outliers()
        
        # Split data into train/test
        data_transformation.split_data()

if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}...")
        pipeline = DataTransformationPipeline()
        pipeline.main()
        logger.info(f"{STAGE_NAME} completed successfully!")
    except Exception as e:
        logger.exception(f"An error occurred in {STAGE_NAME}: {e}")
