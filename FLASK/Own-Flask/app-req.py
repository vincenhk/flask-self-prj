from unittest import result

from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates-username")


@app.route('/')
def index():
    return render_template('check-form.html')


@app.route('/checker')
def user_checker():
    username = request.args.get('username')
    list_error = []

    if not (any(char.lower() in username for char in username)):
        list_error.append("Username is not contain lowercase.")

    if not (any(c.upper() in username for c in username)):
        list_error.append("Username is not contain uppercase.")

    if not username[-1:].isdigit():
        list_error.append("Username is not contain last character digit.")

    if len(list_error) > 0:
        return render_template('result-page.html', result=list_error)
    else:
        return render_template('result-page.html', result=username)


if __name__ == '__main__':
    app.run(debug=True)
