"""Chart data aggregation for the dashboard."""

def get_dashboard_stats() -> dict:
    return {
        "students": 56, "staff": 12, "resources": 842,
        "mean_grade": "7.3", "attendance": "94.2%", "depts": 6,
    }

def get_performance_trend() -> list[dict]:
    return [
        {"term": "F1T1", "mean": 6.2}, {"term": "F1T2", "mean": 6.5},
        {"term": "F2T1", "mean": 7.0}, {"term": "F2T2", "mean": 7.2},
        {"term": "F3T1", "mean": 7.1}, {"term": "F3T2", "mean": 7.6},
    ]
