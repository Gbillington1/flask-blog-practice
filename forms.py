from flask_wtf import Form
from wtforms import BooleanField, StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class UserRegistrationForm(Form):
    username = StringField("Username",
                        validators = [DataRequired(), Length(min=2, max=20)]),
    email = StringField("Email", 
                        validators = [DataRequired(), Email()]),
    password = PasswordField("Password", 
                            validators = [DataRequired(), Length(min=6, max=30)]),
    confirm_password = PasswordField("Confirm Password", 
                                    validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")

class UserLoginForm(Form):
    email = StringField("Email", 
                        validators = [DataRequired(), Email()]),
    password = PasswordField("Password", 
                            validators = [DataRequired(), Length(min=6, max=30)]),
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")