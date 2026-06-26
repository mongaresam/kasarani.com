from app.extensions import db
import datetime

class LibraryItem(db.Model):
    __tablename__ = "library_items"
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

class LibraryIssue(db.Model):
    __tablename__ = "library_issues"
    id          = db.Column(db.Integer, primary_key=True)
    item_id     = db.Column(db.String(16), db.ForeignKey("library_items.id"))
    issued_to   = db.Column(db.String(128))
    issued_on   = db.Column(db.Date, default=datetime.date.today)
    due_back    = db.Column(db.String(32))
    returned    = db.Column(db.Boolean, default=False)
