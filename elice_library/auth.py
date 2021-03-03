from flask import Blueprint, url_for, render_template, session, flash, redirect
from .models import User
from . import db
from .signup_form import RegistrationForm
from .login_form import LoginForm

bp = Blueprint("auth", __name__)

@bp.route('/signup', methods=('GET', 'POST'))
def signup():

    form = RegistrationForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user :
            flash("중복된 이메일입니다.", category="error")

        else:
            user = User(name=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            session['userid'] = user.id

            return redirect(url_for('book.getAllBook'))

    return render_template('auth/signup.html', form=form)

@bp.route('/login', methods=('GET', 'POST'))
def login():

    form = LoginForm()
    status_code = 200

    if form.validate_on_submit():

        user =  User.query.filter_by(email=form.email.data).first()

        if user.password != form.password.data:
            flash("비밀번호 불일치", category="error")
            status_code = 403

        elif user :
            session['userid'] = user.id
            flash("성공적으로 로그인되었습니다.", category="success")
            return redirect(url_for('book.getAllBook'))

    return render_template('auth/index.html', form=form), status_code

@bp.route('/logout')
def logout():

    if 'userid' in session.keys() and session['userid']:
        session.clear()

    return redirect(url_for('auth.login'))
