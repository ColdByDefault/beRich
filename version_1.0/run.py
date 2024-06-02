#ColdByDefault
from app import create_app


if __name__ == '__main__':
    
    app = create_app()
    
    app.run(host='0.0.0.0', port=5555, debug=True)
    
    
    
    
    
    
#To RESET sqlite://site.db
#from app import create_app#
#from app.models import db

#def reset_database():
#    app = create_app()
#    with app.app_context():
#        print("Dropping all tables...")
#        db.drop_all()
#        print("Creating all tables...")
#        db.create_all()  
#        print("Database has been reset.")
#
#if __name__ == "__main__":
#   if input("Are you sure you want to reset the database? This will delete all data permanently. (yes/no) ") == 'yes':
#        reset_database()
#    else:
#        print("Database reset cancelled.")
