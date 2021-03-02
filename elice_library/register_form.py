from wtforms import StringField, PasswordField, SubmitField, validators
from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):

    username = StringField('Username', [
        validators.Length(min=2, max=25, message='2자 이상 25자 이하로 입력해주세용.'),
        validators.DataRequired(message='입력해주세용')],
        render_kw={"class":"uk-input uk-form-width-medium","placeholder":"username"})

    email = StringField('Email Address', [
        validators.Length(min=6, max=35),
        validators.Email(message='Not a valid email address.'),
        validators.DataRequired()
    ], render_kw={"class":"uk-input uk-form-width-medium","placeholder":"email"})
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ], render_kw={"class":"uk-input uk-form-width-medium","placeholder":"password"})
    confirm = PasswordField('Confirm Password',[
        validators.EqualTo('password', message='비밀번호가 일치하지 않습니다.')],
        render_kw={"class":"uk-input uk-form-width-medium","placeholder":"confirm"})

    submit = SubmitField('Submit')