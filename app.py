import os
import pymongo

if os.path.exists("env.py"):
        import env


from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


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
    return render_template("solvents.html", solvents=mongo.db.solvents.find())


@app.route('/consumables')
def consumables():
    return render_template("consumables.html", consumables=mongo.db.consumables.find())


@app.route('/request')
def request():
    return render_template("request.html")


@app.route('/adminsolvents')
def adminsolvents():
    return render_template("adminsolvents.html")


@app.route('/adminconsumables')
def adminconsumables():
    return render_template("adminconsumables.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)