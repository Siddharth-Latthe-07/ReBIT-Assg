from src.dlProject.config.configuration import ConfigurationManager
from src.dlProject.components.data_validation import DataValidation
from src.dlProject import logger


STAGE_NAME = "DATA VALIDATION STAGE"

class DataValidationTrainingPipeline:
    "final data validation pipeline class"
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        #data_validation.validate_directories()
        data_validation.validate_images()
    
