from src.dlProject import logger
from src.dlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.dlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.dlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.dlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.dlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

# import configuration manager
from src.dlProject.config.configuration import ConfigurationManager

# import data ingestion
from src.dlProject.components.data_ingestion import DataIngestion
#from src.dlProject.components.model_evaluation import ModelEvaluation



STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        "you need to call this main function in main.py to trigger the pipeline"
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        # logging the start of the stage, this will help in debugging
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main() # calling the main function, trigger the pipeline
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e  # check the output in STATUS.txt if true then move to next stage


STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e  # check the output in STATUS.txt if true then move to next stage

STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_trainer = ModelTrainerPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e  # check the output in STATUS.txt if true then move to next stage

STAGE_NAME = "Model Evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_eval = ModelEvaluationPipeline()
   model_eval.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e 
