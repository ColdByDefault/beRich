from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman
import logging
from logging.handlers import RotatingFileHandler
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address




db = SQLAlchemy()
csrf = CSRFProtect()
talisman = Talisman(content_security_policy=None)
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    db.init_app(app)
    csrf.init_app(app)
    talisman.init_app(app, force_https=True)
    limiter.init_app(app)
    
    
    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
    
    app.logger.setLevel(logging.INFO)
    app.logger.info('App startup')
    
    
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
    
    from .library import library as library_blueprint
    app.register_blueprint(library_blueprint, url_prefix='/library')
    
    from .number_converter import number_converter as number_converter_blueprint
    app.register_blueprint(number_converter_blueprint, url_prefix='/number_converter')

    
    with app.app_context():
        db.create_all()
        
    migrate = Migrate(app, db) 
    #migrate, this is done once:
    #flask db init
    #flask db migrate -m "Initial migration."
    #flask db upgrade
       
    return app
