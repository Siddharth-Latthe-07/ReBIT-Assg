from src.dlProject.config.configuration import ConfigurationManager
from src.dlProject.components.data_ingestion import DataIngestion
from src.dlProject import logger


STAGE_NAME = "DATA INGESTION STAGE"

class DataIngestionTrainingPipeline:
    "final data ingestion pipeline class"
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
        # now trigger this in main.py (endpoint)