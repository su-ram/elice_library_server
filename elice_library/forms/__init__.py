from wtforms import StringField, PasswordField, SubmitField, validators, FileField, RadioField
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed

class RegistrationForm(FlaskForm):

    default_images = RadioField('Profile Images', choices=['0', 'upload'], default='0')

    def setDefaultUrls(self, urls):

        url_list = []
        for i in range(len(urls)):
            url_list.append((urls[i].url,urls[i].url))
        url_list.append(('0','0'))
        self.default_images.choices = url_list



    image = FileField(u'Image File',[
        FileAllowed(['jpg', 'png'], 'Images only!')])

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
        validators.DataRequired(),validators.regexp(regex='^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'),
        validators.length(min=8, max=20)
        ], render_kw={"class":"uk-input uk-form-width-medium","placeholder":"password"})

    confirm = PasswordField('Confirm Password',[
        validators.EqualTo('password')],
        render_kw={"class":"uk-input uk-form-width-medium","placeholder":"confirm"})

    submit = SubmitField('회원가입')

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