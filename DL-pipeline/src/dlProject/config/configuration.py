import os
from src.dlProject.constants import *
from src.dlProject.utils.common import read_yaml, create_directories
from src.dlProject.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainingConfig, ModelEvaluationConfig
                                        


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        self._inject_params()

        create_directories([self.config.artifacts_root])


    def _inject_params(self):
        """Replace placeholders in config.yaml with params.yaml values."""
        for key, value in self.params.items():
            for section in self.config:
                if isinstance(self.config[section], dict):
                    for sub_key, sub_value in self.config[section].items():
                        if sub_value == f"${{params.{key}}}":
                            self.config[section][sub_key] = value


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    # now update in components/data_ingestion.py


    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            image_extensions=config.image_extensions,

        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.output_dir])

        data_transformation_config = DataTransformationConfig(
            input_dir=config.input_dir,
            output_dir=config.output_dir,
            image_size=config.image_size,
            test_split_ratio=config.test_split_ratio,
        )

        return data_transformation_config
    

    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training

        create_directories([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            updated_model_path=config.updated_model_path,
            image_size=config.image_size,
            batch_size=config.batch_size,
            epochs=config.epochs,
            learning_rate=config.learning_rate,
            classes=config.classes,
        )

        return model_training_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            model_path=config.model_path,
            test_data_dir=config.test_data_dir,
            evaluation_report=config.evaluation_report,
            image_size=config.image_size,
            batch_size=config.batch_size
        )

        return model_evaluation_config


    



    
    
    


      