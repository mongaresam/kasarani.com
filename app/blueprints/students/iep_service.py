"""Individualised Education Plan helpers (stub)."""

def get_iep(student_id: str) -> dict:
    return {
        "student_id": student_id,
        "hearing_aid": True,
        "ksl_level": "Advanced",
        "fm_system": True,
        "visual_alerts": True,
        "captioned_materials": True,
        "lip_reading_support": True,
        "iep_active": True,
        "last_updated": "2026",
    }
