from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ScrapingForm(FlaskForm):
    url = StringField(label='*Url:')
    submit = SubmitField(label='Enviar')
    