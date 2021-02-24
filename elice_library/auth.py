from flask import Blueprint, request, render_template, session, Response
from .models import User
from . import db

bp = Blueprint("auth", __name__, url_prefix="/")

@bp.route('/signup', methods=('GET', 'POST'))
def signup():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        duplicate = User.query.filter_by(email=email).first()

        if duplicate is not None:
            return Response(status=409)

        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

    return render_template('auth/signup.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        users =  User.query.filter_by(email=email).first()

        if users.password != password:
            return Response(status=403)

        if users is not None:
            session['isLogin'] = users.id

    return render_template('auth/index.html')

@bp.route('/logout')
def logout():

    if 'isLogin' in session.keys() and session['isLogin']:
        session.clear()
    else:
        return Response(status=400)

    return render_template('auth/index.html')
