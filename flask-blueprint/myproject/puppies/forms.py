from wtforms import StringField, SubmitField, IntegerField
from flask_wtf import FlaskForm


class AddForm(FlaskForm):
    name = StringField('Name of Puppy : ')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):
    id = IntegerField("ID Number of Puppy to remove : ")
    submit = SubmitField("Remove Puppy")
