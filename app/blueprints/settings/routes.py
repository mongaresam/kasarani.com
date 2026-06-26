from flask import render_template, session
from . import settings_bp
from app.utils.roles import login_required

@settings_bp.route("/")
@login_required
def index():
    u = session["user_data"]
    return render_template("settings/settings.html", u=u)
