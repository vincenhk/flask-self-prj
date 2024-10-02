from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField

app = Flask(__name__, template_folder='templates-alrt')

app.config['SECRET_KEY'] = 'mykey'


class SimpleForm(FlaskForm):
    submit = SubmitField('Click Me.')


@app.route('/', methods=['GET', 'POST'])
def index():
    form1 = SimpleForm()

    if form1.validate_on_submit():
        flash('You just clicked the button!')

        return redirect(url_for('index'))

    return render_template('index.html', form=form1)


if __name__ == '__main__':
    app.run(debug=True)
