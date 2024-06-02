from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from datetime import timedelta

db = SQLAlchemy()
bcrypt = Bcrypt()
# Handling edited notes in Berich wep app on page
# Temporary storage 
temporary_notes_storage = {}

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static') # Create the app
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # create the database for user credintials
    
    app.permanent_session_lifetime = timedelta(days=1) # save the sessions on Server for 5 days
    
    app.secret_key = 'exsGTXk5rMUACXYT84XE5A'  # generated secret_key from secret_key_.py

    db.init_app(app)  # start the database
    
    migrate = Migrate(app, db) 
    #migrate, this is done once:
    #flask db init
    #flask db migrate -m "Initial migration."
    #flask db upgrade


    from .views import init_views
    
    init_views(app)

    return app
