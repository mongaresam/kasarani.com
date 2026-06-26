from flask import Blueprint
communication_bp = Blueprint("communication", __name__, url_prefix="/communication")
from . import routes  # noqa
