from flask import render_template
from . import user

@user.route('/')
def login():
    return render_template('user/login.html')

@user.route('/register')
def register():
    return render_template('user/register.html')