import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/solvents')
def solvents():
    return render_template("solvents.html")
    

@app.route('/consumables')
def consumables():
    return render_template("consumables.html")


@app.route('/request')
def request():
    return render_template("request.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)