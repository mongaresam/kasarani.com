"""CSV / PDF upload helpers (stubs)."""

def parse_csv_results(filepath: str) -> list[dict]:
    """Parse a KNEC-style results CSV into a list of result dicts."""
    import csv
    rows = []
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(dict(row))
    return rows
