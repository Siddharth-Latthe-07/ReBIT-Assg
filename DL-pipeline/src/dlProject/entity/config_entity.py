from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: list
    image_extensions: list


@dataclass(frozen=True)
class DataTransformationConfig:
    input_dir: Path
    output_dir: Path
    image_size: list[int]
    test_split_ratio: float


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    base_model_path: Path
    updated_model_path: Path
    image_size: list[int]
    batch_size: int
    epochs: int
    learning_rate: float
    classes: int


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    model_path: Path
    test_data_dir: Path
    evaluation_report: Path
    image_size: list[int]
    batch_size: int


