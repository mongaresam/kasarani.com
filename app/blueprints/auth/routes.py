from flask import render_template, request, session, redirect, url_for
from . import auth_bp
from app.demo_data import USERS

@auth_bp.route("/", methods=["GET"])
def index():
    if "user" in session:
        return redirect(url_for("dashboard.index"))
    return redirect(url_for("auth.login"))

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        role     = request.form.get("role", "")
        password = request.form.get("password", "")
        if role in USERS and password == "demo1234":
            session["user"]      = role
            session["user_data"] = USERS[role]
            return redirect(url_for("dashboard.index"))
        error = "Invalid credentials. Use password: demo1234"
    return render_template("auth/login.html", roles=USERS, error=error)

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
