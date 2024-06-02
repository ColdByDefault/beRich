from flask import render_template, url_for, request, redirect, session, flash, jsonify
from werkzeug.utils import secure_filename
import os
from . import db, bcrypt, temporary_notes_storage
from .models import User



def init_views(app):
    # index.html
    @app.route('/')
    def home_page():
        return render_template('index.html')  
            
    
    @app.route('/login', methods=["GET", "POST"])
    def logIn():
        if request.method == "POST": # secure data request
            session.permanent = True
            user = User.query.filter_by(username=request.form["userName"]).first() # take input from login.html
            if user and bcrypt.check_password_hash(user.password, request.form["userPassword"]):
                session["user"] = user.username
                print(f"Received name: {user}")  # Debug
                return redirect(url_for("home_page", content=user.username)) # send the content to home_page()
            else:
                flash("Ungültiges Username oder Passwort", "error")
        # Handle GET requests
        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
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
                return render_template('register.html')
            
            # If validations pass, hash the password and create a new user
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash("Registrierung erfolgreich! Sie können sich jetzt anmelden.", "success")
            return redirect(url_for('logIn'))
        
        # Handle GET requests
        return render_template('register.html')
    
    @app.route('/my_profile')
    def my_profile():
        return render_template('myProfile.html')
    
    @app.route('/logout')
    def log_out():
        user = session.get("user") 
        if user:
            flash(f"{user} Sie haben sich abgemeldet!", "info")  
            
        image_path = session.pop('image_path', None)  
        if image_path:
            delete_image(image_path)
        session.pop("user", None)  
        print(f"{user} was popped!")

        return redirect(url_for('logIn'))

    def delete_image(image_path):
        print(f"Attempting to delete image at: {image_path}")
        if image_path and os.path.exists(image_path):
            try:
                os.remove(image_path)
                print(f"Image at {image_path} successfully deleted.")
            except OSError as e:
                print(f"Error deleting image at {image_path}: {e}")
        else:
            print(f"No file found at {image_path}")

    
    @app.route('/apps')
    def apps_page():
        return render_template('apps.html')
    
    
    # GitHub look-like README linked to BeRichtshefte GitHub tkinter            
    @app.route('/beRichReadMe')
    def read_me():
        return render_template('readme.html')
    
    @app.route('/berich', methods=["GET","POST"])
    def berich_app():
        if request.method == "POST":
            return render_template('berich.html')
        
        return render_template('berich.html')

   
    @app.route('/submit-edits', methods=['POST'])
    def submit_edits():
        data = request.get_json()
        temporary_notes_storage.update(data)
        return jsonify({"status": "Success", "message": "Notes updated temporarily."})
    
    @app.route('/submit_form', methods=['POST'])
    def submit_form():
        form_data = {
            'Vor- Nachname': request.form.get('trainee_name'),
            'Standort': request.form.get('location'),
            'Ausbildungsnachweis NR.': request.form.get('record_no'),
            'Trainer/Dozent': request.form.get('trainer_name'),
            'Ausbildungswoche-von': request.form.get('training_start'),
            'Ausbildungswoche-bis': request.form.get('training_end'),
            'LF': request.form.get('lf-code')
        }
        # Handle image upload
        print("Received form data")
        image = request.files['imageUpload']
        if image:
            print("Image file received:", image.filename)
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.static_folder, 'uploads', filename)
            image.save(image_path)
            print("Image saved at:", image_path)
            session['image_path'] = image_path
            form_data['image_path'] = os.path.join('uploads', filename).replace('\\', '/')
            

        else:
            print("Invalid file or no file uploaded")
        
            
        from .models import process_form_data
        from .notesDatabase import notes
        selected_notes = notes.get(form_data['LF'], {})
        process_form_data(form_data)

        

        return render_template('results.html', form_data=form_data, notes_data=selected_notes)

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}
    
    @app.route('/edited_results')
    def coming_soon():
        image_path = session.pop('image_path', None)  
        delete_image(image_path)
        return render_template('editedresults.html')