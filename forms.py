from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import InputRequired


class search(FlaskForm):
    location = StringField('Search: ', validators=[InputRequired()])
    submit = SubmitField('Go')