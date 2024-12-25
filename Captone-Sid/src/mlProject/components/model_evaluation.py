import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from src.mlProject.utils.common import save_json
from pathlib import Path
import joblib
from src.mlProject.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, predicted):
        # Handle the 'YES'/'NO' labels in a binary classification context
        try:
            precision = precision_score(actual, predicted, average="binary", pos_label='YES')
            recall = recall_score(actual, predicted, average="binary", pos_label='YES')
            f1 = f1_score(actual, predicted, average="binary", pos_label='YES')
        except ValueError as e:
            print(f"Error calculating metrics: {e}")
            raise

        accuracy = accuracy_score(actual, predicted)
        confusion = confusion_matrix(actual, predicted)
        report = classification_report(actual, predicted)

        return accuracy, precision, recall, f1, confusion, report

    def save_results(self):
        # Load test data and model
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        # Split features and target
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        # Generate predictions
        predicted_labels = model.predict(test_x)

        # Calculate metrics
        accuracy, precision, recall, f1, confusion, report = self.eval_metrics(test_y, predicted_labels)

        # Save metrics
        scores = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
            "confusion_matrix": confusion.tolist(),  # Convert to list for JSON serialization
            "classification_report": report,
        }

        # Save the metrics to a JSON file
        save_json(path=Path(self.config.metric_file_name), data=scores)

        print(f"Model evaluation completed. Metrics saved to: {self.config.metric_file_name}")
