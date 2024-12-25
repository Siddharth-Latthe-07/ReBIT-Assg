import pandas as pd
import os
from src.mlProject import logger
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
from src.mlProject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        # Load the training data
        train_data = pd.read_csv(self.config.train_data_path)

        # Separate features and target
        X_train = train_data.drop(columns=[self.config.target_column])
        y_train = train_data[self.config.target_column]

        # Identify categorical and numerical columns
        categorical_columns = X_train.select_dtypes(include=['object']).columns
        numerical_columns = X_train.select_dtypes(include=['number']).columns

        # Preprocessing for categorical and numerical features
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_columns),  # Scale numerical features
                ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)  # Encode categorical features
            ]
        )

        # Create a pipeline with preprocessing and model
        model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', LogisticRegression(
                C=self.config.alpha, 
                l1_ratio=self.config.l1_ratio, 
                solver='saga', 
                penalty='elasticnet'
            ))
        ])

        # Train the model
        model.fit(X_train, y_train)

        # Save the trained model
        os.makedirs(self.config.root_dir, exist_ok=True)
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
        print(f"Model saved at: {os.path.join(self.config.root_dir, self.config.model_name)}")
