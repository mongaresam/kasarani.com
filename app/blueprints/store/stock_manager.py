from app.demo_data import INVENTORY

def low_stock_items(threshold: int = 3) -> list[dict]:
    return [i for i in INVENTORY if i["available"] <= threshold]

def reorder_item(item_id: str) -> dict:
    """Stub: trigger a reorder for the given item."""
    return {"status": "reorder_placed", "item_id": item_id}
