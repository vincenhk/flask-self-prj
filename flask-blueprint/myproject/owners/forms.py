from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of puppy''s owner : ')
    pup = IntegerField('Puppy Id : ')
    submit = SubmitField("Add Owner")
