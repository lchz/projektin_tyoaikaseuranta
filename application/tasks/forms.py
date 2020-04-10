from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, DecimalField, validators


class TaskForm(FlaskForm):
    name = StringField(
        'Name:', [validators.length(min=5, max=10), validators.required()])
    content = TextAreaField('Content:', [validators.length(min=5, max=10)])
    estimatedTime = DecimalField(
        'Estimated time:', [validators.required(), validators.NumberRange(min=0.0, max=100.0)])

    class Meta:
        csrf = False
