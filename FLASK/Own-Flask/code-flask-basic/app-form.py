from doctest import debug

from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates-form")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup_form')
def signup_form():
    return render_template("signup.html")


@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    print(first, last)
    return render_template("thankyou.html", first=first, last=last)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('sorry.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
