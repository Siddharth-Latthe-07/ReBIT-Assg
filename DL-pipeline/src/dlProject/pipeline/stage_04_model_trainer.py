from src.dlProject.config.configuration import ConfigurationManager
from src.dlProject.components.model_trainer import ModelTrainer
from src.dlProject.utils.common import load_data  # Assuming a helper to load data
from src.dlProject import logger

STAGE_NAME = "MODEL TRAINING STAGE"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_training_config()

        # Initialize Model Trainer
        model_trainer = ModelTrainer(config=model_training_config)

        # Build and compile model
        base_model = model_trainer.build_base_model()
        updated_model = model_trainer.build_updated_model(base_model=base_model)
        updated_model = model_trainer.compile_model(model=updated_model)

        # Load train and validation data
        train_data, val_data = load_data(
            train_dir="artifacts/data_transformation/train",
            test_dir="artifacts/data_transformation/test",
            image_size=model_training_config.image_size[:2],
            batch_size=model_training_config.batch_size
        )

        # Train model
        model_trainer.train_model(
            model=updated_model, 
            train_data=train_data, 
            val_data=val_data
        )

        # Save the updated model
        model_trainer.save_model(
            model=updated_model, 
            path=model_training_config.updated_model_path
        )

if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}...")
        pipeline = ModelTrainerPipeline()
        pipeline.main()
        logger.info(f"{STAGE_NAME} completed successfully!")
    except Exception as e:
        logger.exception(f"An error occurred in {STAGE_NAME}: {e}")
