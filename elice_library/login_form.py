from flask_wtf import FlaskForm
from wtforms import *

class LoginForm(FlaskForm):

    email = StringField('Email Address', [
        validators.Length(min=6, max=30),
        validators.Email(message='Not a valid email address.'),
        validators.DataRequired()
    ], render_kw={"class": "uk-input uk-form-width-medium", "placeholder": "email"})

    password = PasswordField('New Password', [
        validators.DataRequired(),
    ], render_kw={"class": "uk-input uk-form-width-medium", "placeholder": "password"})

    login = SubmitField('로그인')
