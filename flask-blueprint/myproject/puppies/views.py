from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Puppy
from myproject.puppies.forms import AddForm , DelForm

puppy_blueprint = Blueprint('puppies', __name__, template_folder='templates/puppies')


@puppy_blueprint.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))
    return render_template('add.html', form=form)


@puppy_blueprint.route('/delete', methods=['GET', 'POST'])
def delete_pup():
    form = DelForm()

    if form.validate_on_submit():
        id_chosen = form.id.data

        chosen_pup = Puppy.query.get(id_chosen)
        db.session.delete(chosen_pup)
        db.session.commit()
        return redirect(url_for('puppies.list_pup'))

    return render_template('delete.html', form=form)


@puppy_blueprint.route('/list_pup')
def list_pup():
    puppy_list = Puppy.query.all()
    return render_template('list.html', puppy_list=puppy_list)
