from app import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10))
    email = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(30))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
