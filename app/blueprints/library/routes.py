from flask import render_template, session, jsonify
from . import library_bp
from app.utils.roles import login_required
from app.demo_data import INVENTORY

@library_bp.route("/")
@login_required
def index():
    u = session["user_data"]
    return render_template("library/library.html", u=u, inventory=INVENTORY)

@library_bp.route("/api")
@login_required
def api():
    return jsonify(INVENTORY)
