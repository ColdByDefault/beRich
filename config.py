



class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///base_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Your Secret Key'
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'Your CSRF Secret Key'
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Something'
