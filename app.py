from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from domain.User import User

app = Flask(__name__)
api = Api(app)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

api.add_resource(User, '/user')
if __name__ == '__main__':
    app.run(debug=True)
