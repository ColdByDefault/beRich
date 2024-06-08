from flask import render_template, send_from_directory
from . import library
import os

@library.route('/')
def index():
    lab_files_path = os.path.join(os.path.dirname(__file__), 'lab_files')
    lab_books_path = os.path.join(os.path.dirname(__file__), 'lab_books')
    
    files = [(file, 'cheat_sheet') for file in os.listdir(lab_files_path)]
    books = [(file, 'book') for file in os.listdir(lab_books_path)]
    
    items = files + books
    
    return render_template('library/index.html', items=items)

@library.route('/download-cheat-sheet/<filename>')
def download_file(filename):
    lab_files_path = os.path.join(os.path.dirname(__file__), 'lab_files')
    return send_from_directory(lab_files_path, filename, as_attachment=True)

@library.route('/download-book/<filename>')
def download_book(filename):
    lab_books_path = os.path.join(os.path.dirname(__file__), 'lab_books')
    return send_from_directory(lab_books_path, filename, as_attachment=True)