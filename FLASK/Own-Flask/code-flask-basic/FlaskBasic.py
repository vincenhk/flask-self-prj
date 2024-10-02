from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'


@app.route('/info')
def info():
    return '<h1>Puppies are cute!</h1>'


@app.route('/profile/<username>')
def profile(username):
    if username[-1:] == 'y':
        username = username[:-1]+"iful"

    return '<h1>Profile puppies {}</h1>'.format(username)


# @app.route('/about')
# def about():
#     return render_template('basic.html')

if __name__ == '__main__':
    app.run(debug=True)
