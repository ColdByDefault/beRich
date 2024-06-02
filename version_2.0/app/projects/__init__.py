from flask import Blueprint

user = Blueprint('projects', __name__, template_folder='templates', static_folder='static')

from . import routes