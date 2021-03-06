from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')
    if len(username) < 3:
        raise ValidationError('Username is to short.')
    if len(username) > 30:
        raise ValidationError('Username is to long.')


def password_matches(form, field):
    password = form.data['password']
    repeat_password = form.data['repeat_password']
    if password != repeat_password:
        raise ValidationError('Passwords Don\'t match.')
    if len(password) < 6:
        raise ValidationError('Password is to short')
    if len(password) > 30:
        raise ValidationError('Password is to long')


class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), username_exists])
    email = StringField('email', validators=[
                        DataRequired(), user_exists, Email('Invalid Email Address')])
    password = StringField('password', validators=[
                           DataRequired(), password_matches])
    repeat_password = StringField('repeat_password', validators=[
                                  DataRequired()])
