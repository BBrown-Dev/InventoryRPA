# This test validates that load_inventory() correctly loads and parses a basic file structure.

from services.extract import load_inventory

def test_load_inventory_valid_csv(tmp_path):
    # Create a mock inventory CSV
    test_file = tmp_path / "inventory.csv"
    test_file.write_text("SKU,Location,OnHandQty,ReorderPoint\nSKU01,WH1,10,50")

    df = load_inventory(str(test_file))

    assert not df.empty
    assert list(df.columns) == ["SKU", "Location", "OnHandQty", "ReorderPoint"]
    assert df.iloc[0]["SKU"] == "SKU01"
