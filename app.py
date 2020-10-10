import os
import pymongo


from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myfirstcluster"
COLLECTION = "inventory_manager"


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'inventory_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/solvents')
def solvents():
    solvents = mongo.db.solvents.find()
    return render_template("solvents.html", solvents=solvents)


@app.route('/consumables')
def consumables():
    consumables = mongo.db.consumables.find()
    return render_template("consumables.html", consumables=consumables)


@app.route('/request_table')
def request_table():
    return render_template("request_table.html")


@app.route('/adminsolvents')
def adminsolvents():
    return render_template("adminsolvents.html")


@app.route('/adminconsumables')
def adminconsumables():
    return render_template("adminconsumables.html")


@app.route('/adminsolvents_add', methods=['POST'])
def adminsolvents_add():
    solvents = mongo.db.solvents
    solvents.insert_one(request.form.to_dict())
    return redirect(url_for('solvents'))


@app.route('/adminconsumables_add', methods=['POST'])
def adminconsumables_add():
    consumables = mongo.db.consumables
    consumables.insert_one(request.form.to_dict())
    return redirect(url_for('consumables'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)