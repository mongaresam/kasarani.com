"""Student model — includes special-needs fields."""
from app.extensions import db

class Student(db.Model):
    __tablename__ = "students"
    id              = db.Column(db.String(20), primary_key=True)   # KT2024/F/012
    name            = db.Column(db.String(128), nullable=False)
    form            = db.Column(db.String(8))
    stream          = db.Column(db.String(4))
    gender          = db.Column(db.String(1))
    county          = db.Column(db.String(64))
    # Special needs
    hearing_level   = db.Column(db.String(16))   # Profound / Severe / Moderate
    hearing_aid     = db.Column(db.Boolean, default=True)
    ksl_level       = db.Column(db.String(32))
    fm_system       = db.Column(db.Boolean, default=False)
    iep_active      = db.Column(db.Boolean, default=True)
