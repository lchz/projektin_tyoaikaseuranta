from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("name", [validators.required()])
    password = PasswordField("password", [validators.required()])

    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    name = StringField("Name:", [validators.required(), validators.length(min=3)])
    username = StringField("Username:", [validators.required(), validators.length(min=3)])
    password = PasswordField("Password:", [validators.required(), validators.length(min=3)])
    
    class Meta:
        csrf = False
