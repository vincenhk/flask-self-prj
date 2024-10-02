from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of Puppy : ')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):
    id = IntegerField("ID Number of Puppy to remove : ")
    submit = SubmitField("Remove Puppy")


class AddFormOwner(FlaskForm):
    name = StringField('Name of puppy''s owner : ')
    pup = IntegerField('Puppy Id : ')
    submit = SubmitField("Add Owner")
