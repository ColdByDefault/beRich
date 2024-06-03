from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_bcrypt import Bcrypt


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    db.init_app(app)
    
    
    @app.route('/')
    def home():
        return render_template('main/index.html')
    
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/home')

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/account')
    
    from .projects import projects as projects_blueprint
    app.register_blueprint(projects_blueprint, url_prefix='/projects')

    
    with app.app_context():
        db.create_all()
        
    migrate = Migrate(app, db) 
    #migrate, this is done once:
    #flask db init
    #flask db migrate -m "Initial migration."
    #flask db upgrade
       
    return app
