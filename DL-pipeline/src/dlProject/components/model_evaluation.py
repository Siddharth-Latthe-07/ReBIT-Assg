import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from src.dlProject.entity.config_entity import ModelEvaluationConfig

class ModelEvaluator:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def load_test_data(self):
        test_datagen = ImageDataGenerator(rescale=1.0 / 255)
        test_data = test_datagen.flow_from_directory(
            self.config.test_data_dir,
            target_size=self.config.image_size[:2],
            batch_size=self.config.batch_size,
            class_mode="sparse",
            shuffle=False
        )
        return test_data

    def evaluate_model(self, model, test_data):
        test_loss, test_accuracy = model.evaluate(test_data)
        predictions = model.predict(test_data)
        predicted_classes = np.argmax(predictions, axis=1)
        true_classes = test_data.classes
        class_labels = list(test_data.class_indices.keys())

        return {
            "test_loss": float(test_loss),
            "test_accuracy": float(test_accuracy),
            "predicted_classes": predicted_classes.tolist(),
            "true_classes": true_classes.tolist(),
            "class_labels": class_labels
        }

    def save_evaluation_report(self, report):
        with open(self.config.evaluation_report, "w") as f:
            json.dump(report, f, indent=4)

    def load_model(self):
        model = load_model(self.config.model_path)
        return model
