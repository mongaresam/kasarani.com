from flask import Blueprint
academic_bp = Blueprint("academic", __name__, url_prefix="/academic")
from . import routes  # noqa
