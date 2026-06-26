from flask import render_template, session
from . import announcements_bp
from app.utils.roles import login_required
from app.demo_data import ANNOUNCEMENTS

@announcements_bp.route("/")
@login_required
def index():
    u = session["user_data"]
    return render_template("announcements/announcements.html", u=u, announcements=ANNOUNCEMENTS)
