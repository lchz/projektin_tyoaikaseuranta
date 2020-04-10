from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, DecimalField, validators


class ProjectForm(FlaskForm):
    name = StringField(
        'Name:', [validators.length(min=5, max=144), validators.required()])
    description = TextAreaField(
        'Description:', [validators.length(min=5, max=1000), validators.required()])

    class Meta:
        csrf = False
