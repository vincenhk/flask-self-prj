from flask import Flask, render_template, redirect, flash, url_for, session
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = 'mykey'


class BreedForm(FlaskForm):
    submit = SubmitField('Submit')
    name = StringField('What breed are you?')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = BreedForm()

    if form.validate_on_submit():
        session['breed'] = form.name.data
        flash('You just change your breed {}'.format(session['breed']))

        return redirect(url_for('index'))

    return render_template('clickme.html', form=form )


if __name__ == '__main__':
    app.run(debug=True)
