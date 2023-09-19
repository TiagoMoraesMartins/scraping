from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ScrapingForm(FlaskForm):
    url = StringField(label='*Url:', validators=[DataRequired()])
    submit = SubmitField(label='Enviar')
    