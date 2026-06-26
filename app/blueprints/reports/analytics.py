"""Analytics helpers."""

def year_on_year_trend() -> list[dict]:
    return [
        {"year": y, "mean": m}
        for y, m in [("2018",5.8),("2019",6.1),("2020",6.4),("2021",6.8),("2022",7.0),("2023",7.1),("2024",7.3)]
    ]
