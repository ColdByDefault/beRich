
from flask import render_template, request

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

    
        
    from .models import process_form_data
    from .notesDatabase import notes
    selected_notes = notes.get(form_data['LF'], {})
    process_form_data(form_data)

    

    return render_template('projects/index.html', form_data=form_data, notes_data=selected_notes)






