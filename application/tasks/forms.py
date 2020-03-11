from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, DecimalField, validators


class TaskForm(FlaskForm):
    name = StringField(
        'Name:', [validators.length(min=5), validators.required()])
    content = TextAreaField('Content:', [validators.length(min=5)])
    estimatedTime = DecimalField(
        'Estimated time:', [validators.required(), validators.NumberRange(min=0.1)])
    status = BooleanField('Finished:')

    class Meta:
        csrf = False
