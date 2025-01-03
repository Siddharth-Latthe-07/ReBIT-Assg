from src.dlProject.config.configuration import ConfigurationManager
from src.dlProject.components.model_evaluation import ModelEvaluator
from src.dlProject import logger

STAGE_NAME = "MODEL EVALUATION STAGE"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()

        # Initialize Model Evaluator
        model_evaluator = ModelEvaluator(config=model_evaluation_config)

        # Load test data
        test_data = model_evaluator.load_test_data()

        # Load trained model
        model = model_evaluator.load_model()

        # Evaluate model
        evaluation_report = model_evaluator.evaluate_model(model=model, test_data=test_data)

        # Save evaluation report
        model_evaluator.save_evaluation_report(report=evaluation_report)

if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}...")
        pipeline = ModelEvaluationPipeline()
        pipeline.main()
        logger.info(f"{STAGE_NAME} completed successfully!")
    except Exception as e:
        logger.exception(f"An error occurred in {STAGE_NAME}: {e}")
