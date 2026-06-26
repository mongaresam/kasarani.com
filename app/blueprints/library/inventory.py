"""Library-specific inventory helpers."""
from app.demo_data import INVENTORY

def low_stock_items(threshold: int = 3) -> list[dict]:
    return [i for i in INVENTORY if i["available"] <= threshold]
