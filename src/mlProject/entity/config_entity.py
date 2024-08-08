# from -> /workspaces/rudder/research/01_data_ingestion.ipynb __cell-5__

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path