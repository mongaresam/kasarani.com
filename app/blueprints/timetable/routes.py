from flask import render_template, session
from . import timetable_bp
from app.utils.roles import login_required

@timetable_bp.route("/")
@login_required
def index():
    u = session["user_data"]
    return render_template("timetable/timetable.html", u=u)
