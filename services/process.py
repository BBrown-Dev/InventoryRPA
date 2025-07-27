# This module processes inventory data by cleaning and flagging it for further analysis.
# It handles negative quantities, removes duplicates, and computes reorder quantities.
# This module is part of a data processing pipeline for inventory management.
# It is designed to be used after raw data extraction and before any analysis or reporting.

import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)


def clean_and_flag(df: pd.DataFrame) -> pd.DataFrame:
    # Clean negative quantities
    df["OnHandQty"] = df["OnHandQty"].clip(lower=0)

    # Drop duplicates
    before = len(df)
    df = df.drop_duplicates(subset=["SKU", "Location"])
    logger.info(f"Dropped {before - len(df)} duplicate rows")

    # Compute reorder qty
    df["ReorderQty"] = np.maximum(0, df["ReorderPoint"] - df["OnHandQty"])
    return df
