# Extracts raw data from a CSV file and returns it as a pandas DataFrame.
# This module is part of a data processing pipeline.

import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def load_inventory(path: str) -> pd.DataFrame:
    file = Path(path)
    if not file.exists():
        logger.error(f"Raw file not found: {path}")
        raise FileNotFoundError(path)
    df = pd.read_csv(file)
    logger.info(f"Loaded {len(df)} rows from {path}")
    return df
