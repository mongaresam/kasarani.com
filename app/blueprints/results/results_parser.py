"""Import KCSE results from CSV / PDF (stub)."""
from app.utils.file_handlers import parse_csv_results

def import_results_csv(filepath: str) -> list[dict]:
    return parse_csv_results(filepath)
