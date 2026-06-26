"""Common field validators."""

def is_valid_adm_number(adm: str) -> bool:
    """Check format KT<year>/<M|F>/<3-digit>."""
    import re
    return bool(re.match(r"^KT\d{4}/[MF]/\d{3}$", adm))
