from flask import render_template, session, jsonify
from . import students_bp
from app.utils.roles import login_required
from app.demo_data import STUDENTS

@students_bp.route("/")
@login_required
def index():
    u = session["user_data"]
    return render_template("students/students.html", u=u, students=STUDENTS)

@students_bp.route("/api")
@login_required
def api():
    return jsonify(STUDENTS)
