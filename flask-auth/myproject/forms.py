from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

from myproject.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password_field = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirmation',
                                                                                   message="Passwords must match")])
    password_confirmation = PasswordField('Password Confirm',
                                          validators=[DataRequired()])
    submit = SubmitField('Register!')

    @staticmethod
    def check_email(field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been already registered!')

    @staticmethod
    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been already registered!')
