# This file is part of the Data Processing Service.
# It is responsible for writing cleaned data to a specified path.

import logging

logger = logging.getLogger(__name__)


def write_clean(df, path: str):
    df.to_csv(path, index=False)
    logger.info(f"Wrote cleaned data to {path}")
