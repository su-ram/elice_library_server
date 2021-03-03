from wtforms import StringField, PasswordField, SubmitField, validators
from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):

    username = StringField('Username', [
        validators.Length(min=2, max=20),
        validators.DataRequired(),
        validators.regexp(regex='^[가-힣a-zA-Z]+$')],
        render_kw={"class":"uk-input uk-form-width-medium","placeholder":"username"})

    email = StringField('Email Address', [
        validators.Length(min=6, max=30),
        validators.Email(message='Not a valid email address.'),
        validators.DataRequired()
    ], render_kw={"class":"uk-input uk-form-width-medium","placeholder":"email"})

    password = PasswordField('New Password', [
        validators.DataRequired(),
        ], render_kw={"class":"uk-input uk-form-width-medium","placeholder":"password"})

    confirm = PasswordField('Confirm Password',[
        validators.EqualTo('password')],
        render_kw={"class":"uk-input uk-form-width-medium","placeholder":"confirm"})

    submit = SubmitField('Submit')