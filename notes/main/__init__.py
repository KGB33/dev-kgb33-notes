from flask import Blueprint

bp = Blueprint("main", __name__)

from notes.main import routes  # noqa: F401, E402
