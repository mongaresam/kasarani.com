from flask import render_template, session, jsonify
from . import results_bp
from app.utils.roles import login_required

KCSE_RESULTS = [
    {"subject": "Mathematics",    "grade": "B",  "points": 7, "teacher": "Wanjiku"},
    {"subject": "English Language","grade": "C+","points": 6, "teacher": "Ouma"},
    {"subject": "Kiswahili",       "grade": "B-","points": 6, "teacher": "Muthoni"},
    {"subject": "Biology",         "grade": "B+","points": 8, "teacher": "Ochieng"},
    {"subject": "Chemistry",       "grade": "C+","points": 6, "teacher": "Ngugi"},
    {"subject": "Physics",         "grade": "C", "points": 5, "teacher": "Kariuki"},
    {"subject": "History",         "grade": "B", "points": 7, "teacher": "Atieno"},
    {"subject": "Geography",       "grade": "B-","points": 6, "teacher": "Rotich"},
]

@results_bp.route("/")
@login_required
def index():
    u     = session["user_data"]
    total = sum(s["points"] for s in KCSE_RESULTS)
    mean  = round(total / len(KCSE_RESULTS), 2)
    return render_template("results/results.html", u=u,
                           kcse=KCSE_RESULTS, total=total, mean=mean)

@results_bp.route("/api")
@login_required
def api():
    return jsonify(KCSE_RESULTS)
