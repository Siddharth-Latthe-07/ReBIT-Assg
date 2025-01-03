import os
import cv2
import shutil
import logging
from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self, config):
        self.config = config
        self.input_dir = config.input_dir
        self.output_dir = config.output_dir
        self.image_size = tuple(config.image_size)
        self.test_split_ratio = config.test_split_ratio
        self.cleaned_data_dir = os.path.join(self.output_dir, "cleaned_data")

    def clean_data(self):
        """
        Cleans and resizes all images in the input directory.
        Saves the cleaned images to a `cleaned_data` directory.
        """
        os.makedirs(self.cleaned_data_dir, exist_ok=True)
        for category in os.listdir(self.input_dir):
            category_path = os.path.join(self.input_dir, category)
            output_category_path = os.path.join(self.cleaned_data_dir, category)
            os.makedirs(output_category_path, exist_ok=True)
            for img_name in os.listdir(category_path):
                img_path = os.path.join(category_path, img_name)
                try:
                    img = cv2.imread(img_path)
                    if img is None:
                        logging.warning(f"Invalid image: {img_path}. Skipping.")
                        continue
                    resized_img = cv2.resize(img, self.image_size)
                    cv2.imwrite(os.path.join(output_category_path, img_name), resized_img)
                except Exception as e:
                    logging.warning(f"Error processing image {img_path}: {e}")
        logging.info("Data cleaning and resizing completed.")

    def handle_outliers(self):
        """
        Placeholder for handling outliers in the dataset.
        Currently logs an informational message.
        """
        logging.info("Outlier analysis and handling (if any) completed.")

    def split_data(self):
        """
        Splits the cleaned data into training and testing sets.
        Saves the split data into `train` and `test` directories.
        """
        # Create train and test directories directly under the output directory
        train_dir = os.path.join(self.output_dir, "train")
        test_dir = os.path.join(self.output_dir, "test")
        os.makedirs(train_dir, exist_ok=True)
        os.makedirs(test_dir, exist_ok=True)

        # Iterate through each category in the cleaned data directory
        for category in os.listdir(self.cleaned_data_dir):
            category_path = os.path.join(self.cleaned_data_dir, category)
            if os.path.isdir(category_path):  # Ensure it's a directory
                images = [os.path.join(category_path, img) for img in os.listdir(category_path)]
                train_images, test_images = train_test_split(images, test_size=self.test_split_ratio, random_state=42)

                # Create category directories under train and test
                category_train_dir = os.path.join(train_dir, category)
                category_test_dir = os.path.join(test_dir, category)
                os.makedirs(category_train_dir, exist_ok=True)
                os.makedirs(category_test_dir, exist_ok=True)

                # Copy images to respective train and test directories
                for img_path in train_images:
                    shutil.copy(img_path, category_train_dir)
                for img_path in test_images:
                    shutil.copy(img_path, category_test_dir)

        logging.info("Data splitting into train and test completed.")
