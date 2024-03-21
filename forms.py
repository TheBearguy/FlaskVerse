# This file contains the forms for the application

from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import email_validator
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    userName = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',  validators=[DataRequired(), Length(min=8, max=20)])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class userNameOrEmailField(StringField):
    def validate(self, form, extra_validators=tuple()):
        if not super().validate(form):
            return False
        value = self.data.strip()

        if '@' in value:
            # Check for email
            try:
                email_validator.validate_email(value)
            except email_validator.EmailNotValidError:
                raise ValidationError('Invalid email address')
        else:
            # Check for username
            if not len(value) >= 2 and len(value) <= 30:
                raise ValidationError('Username must be between 2 and 30 characters long')
        return True


class LoginForm(FlaskForm):
    userNameOrEmail = StringField('UserName or Email', validators=[DataRequired(), Length(min=2, max=100)])
    password = PasswordField('Password',  validators=[DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
