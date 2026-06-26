"""KCSE results."""
from app.extensions import db

class KCSEResult(db.Model):
    __tablename__ = "kcse_results"
    id         = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), db.ForeignKey("students.id"))
    subject    = db.Column(db.String(64))
    grade      = db.Column(db.String(4))
    points     = db.Column(db.Integer)
    year       = db.Column(db.Integer)
    teacher    = db.Column(db.String(64))
