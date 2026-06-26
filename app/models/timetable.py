from app.extensions import db

class TimetableEntry(db.Model):
    __tablename__ = "timetable"
    id      = db.Column(db.Integer, primary_key=True)
    form    = db.Column(db.String(8))
    stream  = db.Column(db.String(4))
    day     = db.Column(db.String(10))
    period  = db.Column(db.String(16))
    subject = db.Column(db.String(64))
    teacher = db.Column(db.String(64))
    term    = db.Column(db.String(8))
