from flask import Blueprint, url_for, render_template, flash, redirect, request
from .models import User, AnonymouseImage
from . import db
from .forms import *
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .upload_image import ProfileImage
import random
bp = Blueprint("auth", __name__)
profile_image = ProfileImage()

@bp.route('/signup', methods=('GET', 'POST'))
def signup():

    form = RegistrationForm()
    default_images = AnonymouseImage.query.all()
    for i in default_images:
        print(i)
    form.setDefaultUrls(default_images)

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user :
            flash("중복된 이메일입니다.", category="error")

        else:

            if form.default_images.data == '0':
                import random
                form.default_images.data = default_images[random.randrange(len(default_images))].url
            user = User(name=form.username.data, email=form.email.data, password=generate_password_hash(form.password.data), image=form.default_images.data)

            if form.image.data:
                file = form.image.data
                file.filename = str(user.id)+'.'+file.mimetype.split('/')[1]
                file.save('./elice_library/images/'+file.filename)
                image_url = profile_image.upload_image(file.filename)
                user.image = image_url

            db.session.add(user)
            db.session.commit()
            login_user(user=user)

            return redirect(url_for('book.getAllBook'))

    #

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
