import json
from flask import render_template, session
from . import academic_bp
from app.utils.roles import login_required
from .services import get_kcse_data, get_cbc_data

@academic_bp.route("/")
@login_required
def index():
    u    = session["user_data"]
    kcse = get_kcse_data()
    cbc  = get_cbc_data()
    return render_template("academic/academic.html", u=u,
                           kcse=kcse, kcse_json=json.dumps(kcse),
                           cbc=cbc,  cbc_json=json.dumps(cbc))
