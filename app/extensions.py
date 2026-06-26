# app/extensions.py
# FIX: Added user_loader callback required by flask-login.
# Without this, every page throws "Missing user_loader" exception.

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db           = SQLAlchemy()
migrate      = Migrate()
login_manager = LoginManager()
login_manager.login_view     = "auth.login"
login_manager.login_message  = "Please sign in to access KTSSD ERP."
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(user_id):
    """
    FIX: Required by flask-login. Since we use session-based demo auth
    (not database User objects), we return a lightweight proxy object
    so flask-login stays satisfied while our session dict drives access.
    """
    from app.demo_data import USERS
    from flask import session

    # user_id here is the role key stored in session["user"]
    if user_id in USERS:
        return _DemoUser(user_id, USERS[user_id])
    return None


class _DemoUser:
    """Minimal UserMixin-compatible object for demo session auth."""
    is_authenticated = True
    is_active        = True
    is_anonymous     = False

    def __init__(self, role_key: str, data: dict):
        self.id   = role_key
        self.name = data["name"]
        self.role = data["role"]
        self.dept = data["dept"]
        self.icon = data["icon"]

    def get_id(self):
        return self.id
