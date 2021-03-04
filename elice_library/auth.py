from flask import Blueprint, url_for, render_template, flash, redirect
from .models import User
from . import db
from .forms import *
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
bp = Blueprint("auth", __name__)

@bp.route('/signup', methods=('GET', 'POST'))
def signup():

    form = RegistrationForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user :
            flash("중복된 이메일입니다.", category="error")

        else:

            user = User(name=form.username.data, email=form.email.data, password=generate_password_hash(form.password.data))
            db.session.add(user)
            db.session.commit()

            login_user(user=user)

            return redirect(url_for('book.getAllBook'))

    return render_template('auth/signup.html', form=form)

@bp.route('/login', methods=('GET', 'POST'))
def login():

    form = LoginForm()
    status_code = 200

    if form.validate_on_submit():

        user =  User.query.filter_by(email=form.email.data).first()

        if not user:
            flash("없는 계정입니다.", category="error")

        elif check_password_hash( form.password.data, user.password):
            flash("비밀번호 불일치", category="error")
            status_code = 403

        elif user :

            login_user(user=user)

            flash("성공적으로 로그인되었습니다.", category="success")
            return redirect(url_for('book.getAllBook'))

    return render_template('auth/index.html', form=form), status_code

@bp.route('/logout')
def logout():

    logout_user()

    return redirect(url_for('auth.login'))
