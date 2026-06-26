import json
from flask import render_template, session
from . import reports_bp
from app.utils.roles import login_required

YEARLY = [
    {"year": y, "mean": m}
    for y, m in [("2018",5.8),("2019",6.1),("2020",6.4),("2021",6.8),("2022",7.0),("2023",7.1),("2024",7.3)]
]

@reports_bp.route("/")
@login_required
def index():
    u = session["user_data"]
    return render_template("reports/reports.html", u=u, yearly_json=json.dumps(YEARLY))
