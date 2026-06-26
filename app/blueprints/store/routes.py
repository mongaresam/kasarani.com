from flask import render_template, session
from . import store_bp
from app.utils.roles import login_required
from app.demo_data import INVENTORY
from .stock_manager import low_stock_items

@store_bp.route("/")
@login_required
def index():
    u = session["user_data"]
    return render_template("store/store.html", u=u,
                           inventory=INVENTORY,
                           low_stock=low_stock_items())
