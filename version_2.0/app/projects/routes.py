from io import BytesIO
from flask import render_template, request, send_file
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from . import projects

user_data = []

@projects.route('/')
def projects_list():
    form_data = {}
    notes_data = {}
    submit_form = False
    return render_template('projects/index.html', form_data=form_data, notes_data=notes_data, submit_form=submit_form)

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

    submit_form = True
    return render_template('projects/index.html', form_data=form_data, notes_data=selected_notes, submit_form=submit_form)

@projects.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    user_name = request.form.get('trainee_name')
    standort = request.form.get('location')
    ausbildungs_num = request.form.get('record_no')
    trainer = request.form.get('trainer_name')
    week_start = request.form.get('training_start')
    week_end = request.form.get('training_end')
    lf_code = request.form.get('lf-code')
    

    from .notesDatabase import notes
    selected_notes = notes.get(lf_code, {})

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
            'LF': lf_code,
            'notes': selected_notes,
        })

    pdf_file = generate_pdf_file()
    return send_file(pdf_file, as_attachment=True, download_name='Berichtsheft.pdf')

def generate_pdf_file():
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title_style.textColor = colors.blue
    title_style.fontSize = 24

    normal_style = styles['Normal']
    normal_style.fontSize = 12

    # Add title
    title = Paragraph("Berichtsheft Klasse 24/26", title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))

    

    # Add user data
    for i in user_data:
        user_info = [
            ["Vor- Nachname:", i['Vor- Nachname']],
            ["Standort:", i['Standort']],
            ["Ausbildungsnachweis NR:", i['Ausbildungsnachweis NR']],
            ["Trainer/Dozent:", i['Trainer/Dozent']],
            ["Ausbildungswoche-von:", i['Ausbildungswoche-von']],
            ["Ausbildungswoche-bis:", i['Ausbildungswoche-bis']],
        ]

        table = Table(user_info, colWidths=[150, 300])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 12))

        if 'notes' in i:
            notes_title = Paragraph("Notes:", normal_style)
            elements.append(notes_title)
            elements.append(Spacer(1, 12))
            for day, note in i['notes'].items():
                note_paragraph = Paragraph(f"<b>{day[:-1]}:</b> {note}", normal_style)
                elements.append(note_paragraph)
                elements.append(Spacer(1, 6))
            elements.append(Spacer(1, 24))

    # Add standard conclusion text
    introduction3 = Paragraph("Durch die nachfolgende Unterschrift wird die Richtigkeit und Vollständigkeit der obigen Angaben bestätigt.", normal_style)
    elements.append(introduction3)
    elements.append(Spacer(1, 20))
    # Add standard introduction text
    introduction = Paragraph("Datum, Unterschrift der/des Auszubildenden", normal_style)
    elements.append(introduction)
    elements.append(Spacer(1, 24))
    # Add standard introduction text
    introduction2 = Paragraph("Datum, Unterschrift der/des Ausbildenden (GFN GmbH,Praktikumsbetrieb)", normal_style)
    elements.append(introduction2)
    elements.append(Spacer(1, 28))
    

    doc.build(elements)

    buffer.seek(0)
    return buffer
