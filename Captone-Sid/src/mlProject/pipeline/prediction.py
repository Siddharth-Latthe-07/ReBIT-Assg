import joblib  # inside model trainer, you have the model, you can load it using joblib
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        # Load the trained model from the specified path
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    def predict(self, data):
        # Define the column names as expected by the model
        columns = [
            "GENDER", "AGE", "SMOKING", "YELLOW_FINGERS", "ANXIETY",
            "PEER_PRESSURE", "CHRONIC DISEASE", "FATIGUE ", "ALLERGY ",
            "WHEEZING", "ALCOHOL CONSUMING", "COUGHING", "SHORTNESS OF BREATH",
            "SWALLOWING DIFFICULTY", "CHEST PAIN"
        ]

        # Convert the input data to a DataFrame
        data_df = pd.DataFrame(data, columns=columns)

        # Predict using the loaded model
        prediction = self.model.predict(data_df)

        return prediction
