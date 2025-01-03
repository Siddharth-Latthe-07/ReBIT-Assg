import os
import urllib.request as request
from PIL import Image
from src.dlProject import logger
from src.dlProject.utils.common import get_size
from pathlib import Path
from src.dlProject.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_images(self):
        try:
            validation_status = True
            for dir_path in self.config.unzip_data_dir:
                if not os.path.exists(dir_path):
                    validation_status = False
                    raise FileNotFoundError(f"Directory {dir_path} not found!")

                for file_name in os.listdir(dir_path):
                    if not any(file_name.endswith(ext) for ext in self.config.image_extensions):
                        validation_status = False
                        print(f"Invalid file: {file_name} in {dir_path}")

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e

