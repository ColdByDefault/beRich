from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return render_template('main/index.html')
    
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/home')

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/account')

    return app
