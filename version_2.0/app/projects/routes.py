import os
from flask import Blueprint, jsonify, render_template, request, session
from werkzeug.utils import secure_filename
from . import projects



@projects.route('/')
def projects_list():
    return render_template('projects/index.html')

@projects.route('/submit_form', methods=['POST'])
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

    image = request.files['imageUpload']
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image_path = os.path.join(projects.static_folder, 'uploads', filename)
        image.save(image_path)
        session['image_path'] = image_path
        form_data['image_path'] = os.path.join('uploads', filename).replace('\\', '/')

    from .models import process_form_data
    from .notesDatabase import notes
    selected_notes = notes.get(form_data['LF'], {})
    process_form_data(form_data)

    return render_template('projects/index.html', form_data=form_data, notes_data=selected_notes, form_submitted=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

@projects.route('/submit-edits', methods=['POST'])
def submit_edits():
    temporary_notes_storage = {}
    data = request.get_json()
    temporary_notes_storage.update(data)
    return jsonify({"status": "Success", "message": "Notes updated temporarily."})



@projects.route('/coming_soon')
def coming_soon():
    return render_template('projects/index2.html')
