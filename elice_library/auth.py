from flask import Blueprint, request, render_template, session, flash, redirect
from .models import User
from . import db
from .register_form import RegistrationForm

bp = Blueprint("auth", __name__)

@bp.route('/signup', methods=('GET', 'POST'))
def signup():

    form = RegistrationForm()

    if form.validate_on_submit():

        duplicate = User.query.filter_by(email=form.email.data).first()

        if duplicate is not None:
            return render_template('auth/index.html'), 409

        user = User(name=form.username.data, email=form.email.data, password=form.password.data)

        db.session.add(user)
        db.session.commit()
        session['userid'] = user.id

        return redirect('/book')

    return render_template('auth/signup.html', form=form)

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
