import tensorflow as tf
import numpy as np
from PIL import Image
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        # Load the trained model from the specified path
        self.model = tf.keras.models.load_model(Path('artifacts/model_training/updated_model.h5'))

    def preprocess_image(self, image_path, target_size=(224, 224)):
        """Preprocess the image to the required format."""
        image = Image.open(image_path).convert("RGB")
        image = image.resize(target_size)
        image_array = np.array(image) / 255.0  # Normalize to [0, 1]
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
        return image_array

    def predict(self, image_path):
        """Predict the class of the image."""
        preprocessed_image = self.preprocess_image(image_path)
        prediction = self.model.predict(preprocessed_image)
        return prediction
