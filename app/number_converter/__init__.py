from flask import Blueprint

number_converter = Blueprint('number_converter', __name__, template_folder='templates', static_folder='static')

from . import routes
