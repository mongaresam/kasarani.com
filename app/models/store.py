from app.extensions import db

class StoreItem(db.Model):
    __tablename__ = "store_items"
    id        = db.Column(db.String(16), primary_key=True)
    name      = db.Column(db.String(128), nullable=False)
    category  = db.Column(db.String(32))
    qty       = db.Column(db.Integer, default=0)
    issued    = db.Column(db.Integer, default=0)
    condition = db.Column(db.String(16))
    dept      = db.Column(db.String(64))

    @property
    def available(self):
        return self.qty - self.issued

class StoreRequest(db.Model):
    __tablename__ = "store_requests"
    id       = db.Column(db.Integer, primary_key=True)
    item     = db.Column(db.String(128))
    dept     = db.Column(db.String(64))
    qty      = db.Column(db.Integer)
    priority = db.Column(db.String(8))
    by       = db.Column(db.String(64))
    approved = db.Column(db.Boolean, default=False)
