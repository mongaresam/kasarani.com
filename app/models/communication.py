from app.extensions import db

class Message(db.Model):
    __tablename__ = "messages"
    id       = db.Column(db.Integer, primary_key=True)
    sender   = db.Column(db.String(128))
    subject  = db.Column(db.String(256))
    body     = db.Column(db.Text)
    time     = db.Column(db.String(8))
    date     = db.Column(db.String(16))
    read     = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(8), default="normal")
