import bcrypt
from flask_bcrypt import Bcrypt
from flask import flash, redirect, render_template, request, session, url_for
from . import user
from app.models import User
from app import db



@user.route('/', methods=['GET', 'POST'])
def login():
    bcrypt = Bcrypt()
    if request.method == "POST": # secure data request
        user = User.query.filter_by(username=request.form["userName"]).first() # take input from login.html
        if user and bcrypt.check_password_hash(user.password, request.form["userPassword"]):
            session["user"] = user.username
            print(f"Received name: {user}")  # Debug
            return redirect(url_for("main.index", content=user.username)) # send the content to home_page()
        else:
            flash("Ungültiges Username oder Passwort", "error")
    # Handle GET requests
    return render_template('user/login.html')

@user.route('/register', methods=['GET', 'POST'])
def register():
    bcrypt = Bcrypt()
    if request.method == "POST":
            username = request.form["newUser"]
            password = request.form["newPassword"]
            confirm_password = request.form["confPassword"]
            errors = False # same as is_valid, used one error for all in order to printout multi-error msgs in register.html

            from .validation import username_valid, password_valid
            # Check if user exists
            user_exists = User.query.filter_by(username=username).first() is not None
            if user_exists:
                flash("Dieser Benutzername ist bereits vergeben!", "warning")
                errors = True
            
            # Validate username
            if not username_valid(username):
                errors = True
            
            # Validate password including confirmation
            if not password_valid(password, confirm_password): # Back-end handling for pw confirmation
                errors = True
            
            if errors:
                return render_template('user/register.html')
            
            # If validations pass, hash the password and create a new user
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash("Registrierung erfolgreich! Sie können sich jetzt anmelden.", "success")
            return redirect(url_for('user.login'))
        
        # Handle GET requests
    return render_template('user/register.html')


@user.route('/profile')
def profile():
    if "user" not in session:
        flash("Sie müssen sich zuerst anmelden!", "warning")
        return redirect(url_for('user.login'))
    return render_template('user/profile.html', username=session["user"])


@user.route('/logout')
def logout():
    session.pop("user", None)
    session.clear()
    return redirect(url_for("main.index"))