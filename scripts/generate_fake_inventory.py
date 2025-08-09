# Generate a fake inventory dataset with edge cases
# This script creates a CSV file with inventory data, including negative quantities and duplicates.
# It uses the Faker library to generate random descriptions and costs.
# Ensure you have pandas and faker installed: pip install pandas faker
# The output file will be saved in a 'data' directory.

#!/usr/bin/env python3
import pandas as pd
from faker import Faker
from random import randint, uniform, choice
from pathlib import Path

fake = Faker()
SKUS = [f"SKU{str(i).zfill(5)}" for i in range(1, 501)]
LOCATIONS = ["WH1", "WH2", "WH3"]

def make_row(sku):
    # Introduce edge cases: negative qty, duplicates
    qty = randint(-5, 500)
    return {
        "SKU": sku,
        "Description": fake.word().capitalize(),
        "Location": choice(LOCATIONS),
        "OnHandQty": qty,
        "ReorderPoint": randint(20, 100),
        "UnitCost": round(uniform(2.5, 50.0), 2),
    }

if __name__ == "__main__":
    Path("../data").mkdir(exist_ok=True)
    rows = [make_row(s) for s in SKUS] + [make_row("SKU00001")]  # duplicate
    df = pd.DataFrame(rows)
    df.to_csv("../data/inventory_raw.csv", index=False)
    print("✅ Fake inventory written to data/inventory_raw.csv")
