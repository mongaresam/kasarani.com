from app.extensions import db

class Announcement(db.Model):
    __tablename__ = "announcements"
    id     = db.Column(db.Integer, primary_key=True)
    title  = db.Column(db.String(256))
    body   = db.Column(db.Text)
    date   = db.Column(db.String(32))
    type   = db.Column(db.String(32))
    urgent = db.Column(db.Boolean, default=False)
