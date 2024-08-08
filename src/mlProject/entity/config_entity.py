# from -> /workspaces/rudder/research/01_data_ingestion.ipynb __cell-5__

from dataclasses import dataclass
from pathlib import Path

# stage_01_DataIngestionConfig
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

# stage_02_DataValidationConfig
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict