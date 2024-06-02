from flask import render_template
from . import user

@user.route('/')
def register():
    return render_template('user/register.html')