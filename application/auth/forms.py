from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField


class LoginForm(FlaskForm):
    username = StringField("Username:")
    password = PasswordField("Password:")

    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    name = StringField("Name:", [validators.length(min=3), validators.required()])
    username = StringField("Username:", [validators.unique(), validators.required(), validators.length(min=3)])
    password = PasswordField("Password:", [validators.required(), validators.length(min=3)])
    
    class Meta:
        csrf = False
