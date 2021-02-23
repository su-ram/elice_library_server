from elice_library import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(30))

    def __init__(self, name, email, password):
        self.email = email
        self.name = name
        self.password = password
