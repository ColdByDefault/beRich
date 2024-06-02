from . import db


# User Info Database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    
    
# User inputs from berichts.html ==> send to backend route /submit_form
def process_form_data(data):
    print("Processing the following data:")
    for key, value in data.items():
        print(f"{key}: {value}")
    return data



