from flask import render_template, session, jsonify
from . import communication_bp
from app.utils.roles import login_required
from app.demo_data import MESSAGES

@communication_bp.route("/")
@login_required
def index():
    u = session["user_data"]
    return render_template("communication/communication.html", u=u, messages=MESSAGES)

@communication_bp.route("/api")
@login_required
def api():
    return jsonify(MESSAGES)
