from flask import Blueprint, request, render_template
from .models import User
from . import db

bp = Blueprint("auth", __name__, url_prefix="/")

@bp.route('/signup', methods=('GET', 'POST'))
def signup():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user = User(name=name, email=email, password=password)

        db.session.add(user)
        db.session.commit()

    return render_template('auth/signup.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():

    if request.method == 'POST':
        email = request.form['email']
        users =  User.query.all()
        print(users)

    return render_template('auth/index.html')