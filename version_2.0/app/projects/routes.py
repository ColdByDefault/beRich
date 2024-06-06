from io import BytesIO
from flask import render_template, request, send_file
from reportlab.pdfgen import canvas
from . import projects

user_data = []

@projects.route('/')
def projects_list():
    form_data = {}
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


@projects.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    user_name = request.form.get('trainee_name')
    standort = request.form.get('location')
    ausbildungs_num = request.form.get('record_no')
    trainer = request.form.get('trainer_name')
    week_start = request.form.get('training_start') 
    week_end = request.form.get('training_end')

    if ((user_name and standort) and
       (ausbildungs_num and trainer) and 
       (week_start and week_end)):
        user_data.append({
            'Vor- Nachname': user_name,
            'Standort': standort,
            'Ausbildungsnachweis NR': ausbildungs_num,
            'Trainer/Dozent': trainer,
            'Ausbildungswoche-von': week_start,
            'Ausbildungswoche-bis': week_end,
        })

    # Print user_data for debugging
    print("User Data:", user_data)

    pdf_file = generate_pdf_file()
    return send_file(pdf_file, as_attachment=True, download_name='Berichtsheft.pdf')

def generate_pdf_file():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, "Berichtsheft")

    y = 700
    for i in user_data:
        p.drawString(100, y, f"Vor- Nachname: {i['Vor- Nachname']}")
        p.drawString(100, y - 20, f"Standort: {i['Standort']}")
        p.drawString(100, y - 40, f"Ausbildungsnachweis NR: {i['Ausbildungsnachweis NR']}")
        p.drawString(100, y - 60, f"Trainer/Dozent: {i['Trainer/Dozent']}")
        p.drawString(100, y - 80, f"Ausbildungswoche-von: {i['Ausbildungswoche-von']}")
        p.drawString(100, y - 100, f"Ausbildungswoche-bis: {i['Ausbildungswoche-bis']}")
        y -= 140  # Move to the next entry

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer
