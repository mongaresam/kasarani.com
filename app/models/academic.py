"""CBC/CBE and 8-4-4 structures."""
from app.extensions import db

class Subject(db.Model):
    __tablename__ = "subjects"
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(64), nullable=False)
    dept       = db.Column(db.String(64))
    curriculum = db.Column(db.String(8))   # CBC | 844

class CBCAssessment(db.Model):
    __tablename__ = "cbc_assessments"
    id           = db.Column(db.Integer, primary_key=True)
    student_id   = db.Column(db.String(20), db.ForeignKey("students.id"))
    learning_area= db.Column(db.String(64))
    level        = db.Column(db.String(16))   # Exceeding / Meeting / Approaching
    score        = db.Column(db.Float)
    term         = db.Column(db.String(8))
