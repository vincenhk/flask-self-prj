from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    list = [1,2,3,4,5]
    return render_template('TemplateControlFlow.html', list=list)


if __name__ == '__main__':
    app.run(debug=True)