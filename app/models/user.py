from app.extensions import db

class User(db.Model):
    __tablename__ = "users"
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),  unique=True, nullable=False)
    name     = db.Column(db.String(128), nullable=False)
    role     = db.Column(db.String(32),  nullable=False)
    dept     = db.Column(db.String(64))
    icon     = db.Column(db.String(8),   default="👤")
    staff_id = db.Column(db.String(16),  unique=True)
    password_hash = db.Column(db.String(256))
