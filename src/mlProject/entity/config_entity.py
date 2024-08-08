from dataclasses import dataclass
from pathlib import Path

# from ->  /workspaces/rudder/research/01_data_ingestion.ipynb __cell-5__
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

# from -> /workspaces/rudder/research/02_data_validation.ipynb __cell-5__
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

# from -> /workspaces/rudder/research/03_data_transformation.ipynb __cell-5__
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path