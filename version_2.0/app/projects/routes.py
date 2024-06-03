from flask import render_template
from . import projects

@projects.route('/')
def projects_list():
    return render_template('projects/index.html')



