from flask import Blueprint

library = Blueprint('library', __name__, template_folder='templates', static_folder='static')

from . import routes