# Set up DB inside the __init__.py
from myproject import db
from sqlalchemy import ForeignKey

class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    ## RELATION CONNECTION
    owner = db.relationship('Owner', backref='puppies', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f" ID {self.id}, Puppy name : {self.name.capitalize()} and owner {self.owner.name.capitalize()}"
        else:
            return f"ID {self.id}, Puppy name : {self.name.capitalize()} without owner"


class Owner(db.Model):
    __tablename__ = "owners"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id