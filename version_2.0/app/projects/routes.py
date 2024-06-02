from flask import render_template
from . import projects

@projects.route('/')
def index():
    return render_template('projects/index.html')


