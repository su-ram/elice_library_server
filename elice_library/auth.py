from flask import Blueprint, request, render_template, session, flash, redirect
from .models import User
from . import db

bp = Blueprint("auth", __name__)

@bp.route('/signup', methods=('GET', 'POST'))
def signup():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        duplicate = User.query.filter_by(email=email).first()

        if duplicate is not None:
            return render_template('auth/index.html'), 409

        user = User(name=name, email=email, password=password)

        db.session.add(user)
        db.session.flush()
        session['userid'] = user.id
        db.session.commit()

        return redirect('/book')

    return render_template('auth/signup.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        user =  User.query.filter_by(email=email).first()

        status_code = 200

        if user.password != password:
            status_code = 403
            return render_template('auth/index.html'), 403

        if user is not None:
            session['userid'] = user.id
            flash("성공적으로 로그인되었습니다.", category="success")
            return redirect('/book')

    return render_template('auth/index.html'), status_code

@bp.route('/logout')
def logout():

    if 'userid' in session.keys() and session['userid']:
        session.clear()

    return render_template('auth/index.html')
