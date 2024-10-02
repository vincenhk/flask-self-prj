from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/puppy/<name>')
def puppy(name):
    return render_template('puppy.html', name=name)


if __name__ == '__main__':
    app.run()
