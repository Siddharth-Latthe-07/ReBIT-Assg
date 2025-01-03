"""
write utility related functions here, some frequenct functions
say we are using config.yaml , schema.yaml, params.yaml, again and again
if we constantly want to use these files, we can write a function here,
we read yaml files using pyyaml lib

we can create seperate functions here where we call each yaml
and then do inter file import and read it
    
"""

import os
from box.exceptions import BoxValueError
import yaml
from src.dlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# ensure annotations in a decorator , we have installed ensure in requirements.txt
# we can use this decorator to ensure that the function has annotations

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any: #binary file
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data



@ensure_annotations
def get_size(path: Path) -> str: #get file size
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

"using create directories we can say create artifacts where we can ingest data"



def load_data(train_dir, test_dir, image_size, batch_size):
    # Training data generator with augmentation
    train_datagen = ImageDataGenerator(
        rescale=1./255,                   # Normalize pixel values to [0, 1]
        rotation_range=20,                # Randomly rotate images by up to 20 degrees
        width_shift_range=0.2,            # Randomly shift images horizontally by 20% of width
        height_shift_range=0.2,           # Randomly shift images vertically by 20% of height
        shear_range=0.2,                  # Apply random shearing transformations
        zoom_range=0.2,                   # Apply random zoom
        horizontal_flip=True,             # Randomly flip images horizontally
        fill_mode="nearest"               # Fill in missing pixels after transformations
    )
    
    # Validation/test data generator without augmentation
    test_datagen = ImageDataGenerator(rescale=1./255)

    # Training data generator
    train_data = train_datagen.flow_from_directory(
        train_dir,
        target_size=image_size,          # Resize images to (width, height)
        batch_size=batch_size,           # Number of images per batch
        class_mode="sparse"              # Labels as integers for sparse categorical cross-entropy
    )

    # Validation/test data generator
    val_data = test_datagen.flow_from_directory(
        test_dir,
        target_size=image_size,
        batch_size=batch_size,
        class_mode="sparse"
    )

    return train_data, val_data



# to add memory downsizing function for reference

# def downsize_memory(df: pd.DataFrame) -> pd.DataFrame: