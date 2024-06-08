from flask import render_template, send_from_directory
from . import library
import os

@library.route('/')
def index():
    lab_files_path = os.path.join(os.path.dirname(__file__), 'lab_files')
    files = os.listdir(lab_files_path)
    return render_template('library/index.html', files=files)

@library.route('/download/<filename>')
def download_file(filename):
    lab_files_path = os.path.join(os.path.dirname(__file__), 'lab_files')
    return send_from_directory(lab_files_path, filename, as_attachment=True)