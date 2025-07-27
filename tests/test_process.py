# Test cases for the clean_and_flag function in the process module.
# This module contains unit tests for the clean_and_flag function, ensuring it behaves as expected.
# It checks for correct handling of negative quantities, duplicate rows, and reorder quantity calculations.

import pandas as pd
from services.process import clean_and_flag


def test_clean_and_flag_logic():
    # Sample input with edge cases
    test_data = pd.DataFrame([
        {"SKU": "SKU00001", "Location": "WH1", "OnHandQty": -10, "ReorderPoint": 50},
        {"SKU": "SKU00001", "Location": "WH1", "OnHandQty": 20, "ReorderPoint": 40},  # duplicate
        {"SKU": "SKU00002", "Location": "WH2", "OnHandQty": 60, "ReorderPoint": 30}
    ])

    result = clean_and_flag(test_data)

    # Should drop duplicates and clip negative quantity
    assert len(result) == 2
    assert (result["OnHandQty"] >= 0).all()

    # Check computed ReorderQty
    row1 = result[result["SKU"] == "SKU00001"].iloc[0]
    assert row1["ReorderQty"] == max(0, row1["ReorderPoint"] - row1["OnHandQty"])

    row2 = result[result["SKU"] == "SKU00002"].iloc[0]
    assert row2["ReorderQty"] == 0  # OnHand > ReorderPoint → no reorder needed
