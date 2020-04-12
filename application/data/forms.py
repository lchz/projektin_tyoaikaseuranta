from flask_wtf import FlaskForm
from wtforms import DateField, StringField

class DataForm(FlaskForm):
    fromDate = DateField("From Date", format='%Y-%m-%d')

    class Meta:
        csrf = False