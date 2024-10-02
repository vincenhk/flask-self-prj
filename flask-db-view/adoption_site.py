import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import ForeignKey

from form import AddForm, DelForm, AddFormOwner

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

##########################################
########## SQL DATABASE SECTION ##########
##########################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


##########################################
################# MODELS #################
##########################################

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


##########################################
############# VIEW FUCTION ###############
##########################################

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('add.html', form=form)


@app.route('/list')
def list_pup():
    # puppy_list = Puppy.query.all()
    puppy_list = Puppy.query.all()
    # print(puppy_list)
    # print(len(puppy_list))
    # if len(puppy_list) == 0:
    #     return render_template('list.html', )
    return render_template('list.html', puppy_list=puppy_list)


@app.route('/add-owner', methods=['GET', 'POST'])
def add_owner():
    form = AddFormOwner()
    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup.data
        new_owner = Owner(name, pup_id)

        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('add-owner.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def del_pup():
    form = DelForm()
    if form.validate_on_submit():
        id_to_delete = form.id.data
        print("Delete id :", id_to_delete)
        pup = Puppy.query.get(id_to_delete)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
