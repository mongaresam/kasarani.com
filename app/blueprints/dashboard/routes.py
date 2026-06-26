import json
from flask import render_template, session
from . import dashboard_bp
from app.utils.roles import login_required
from app.demo_data import ANNOUNCEMENTS
from .services import get_dashboard_stats, get_performance_trend

@dashboard_bp.route("/")
@login_required
def index():
    u     = session["user_data"]
    stats = get_dashboard_stats()
    perf  = json.dumps(get_performance_trend())
    return render_template("dashboard/dashboard.html", u=u, stats=stats,
                           perf=perf, announcements=ANNOUNCEMENTS[:3])
