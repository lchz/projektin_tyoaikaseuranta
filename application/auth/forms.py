from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("name", [validators.required()])
    password = PasswordField("password", [validators.required()])

    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    name = StringField("Name:", [validators.required(), validators.length(min=3, max=20, message="Name length between 3-20 characters")])
    username = StringField("Username:", [validators.required(), validators.length(min=3, max=20, message="Username length between 3-20 characters")])
    password = PasswordField("Password:", [validators.required(), validators.length(min=3, max=30, message="Password length between 3-30 characters")])
    
    class Meta:
        csrf = False
