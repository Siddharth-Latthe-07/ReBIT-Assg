import os
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.applications import MobileNetV2
from src.dlProject.entity.config_entity import ModelTrainingConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def build_base_model(self):
        base_model = MobileNetV2(
            weights="imagenet",
            include_top=False,
            input_shape=tuple(self.config.image_size)
        )
        base_model.trainable = False  # Freeze base model layers
        return base_model

    def build_updated_model(self, base_model: Model):
        x = Flatten()(base_model.output)
        x = Dense(128, activation="relu")(x)
        x = Dropout(0.5)(x)
        x = Dense(self.config.classes, activation="softmax")(x)
        updated_model = Model(inputs=base_model.input, outputs=x)
        return updated_model

    def compile_model(self, model: Model):
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=self.config.learning_rate),
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"]
        )
        return model

    def train_model(self, model: Model, train_data, val_data):
        history = model.fit(
            train_data,
            validation_data=val_data,
            epochs=self.config.epochs,
            batch_size=self.config.batch_size,
        )
        return history

    def save_model(self, model: Model, path: str):
        model.save(path)
