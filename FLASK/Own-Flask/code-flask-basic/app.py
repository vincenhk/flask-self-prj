from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    v1 = "puppies"
    v2 = list(v1)
    return render_template('basic.html', x = v1, slice = v2)


if __name__ == '__main__':
    app.run(debug=True)