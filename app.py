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


@app.route('/solvents', methods=['GET', 'POST'])
def solvents():
    searchtxt = request.form.get('searchtxt')
    if not searchtxt:
        searchtxt = ""
        mysol = mongo.db.solvents.find()
        counttxt = "Total number of solvents available"
    else:
        mysol = mongo.db.solvents.find({'$text': {'$search': searchtxt}})
        counttxt = "Solvent record(s) found"
    sol_count = mysol.count()
    return render_template("solvents.html", counttxt=counttxt, solvents=mysol, sol_count=sol_count, searchtxt=searchtxt)


@app.route('/consumables', methods=['GET', 'POST'])
def consumables():
    searchtxt = request.form.get('searchtxt')
    if not searchtxt:
        searchtxt = ""
        mycon = mongo.db.consumables.find()
        counttxt = "Total number of consumables available"
    else:
        mycon = mongo.db.consumables.find({'$text': {'$search': searchtxt}})
        counttxt = "Consumable record(s) found"
    con_count = mycon.count()
    return render_template("consumables.html", counttxt=counttxt, consumables=mycon, con_count=con_count, searchtxt=searchtxt)


@app.route('/addsolvents')
def addsolvents():
    return render_template("addsolvents.html")


@app.route('/addsolvents', methods=['POST'])
def addsolvents_add():
    mongo.db.solvents.insert_one(request.form.to_dict())
    return redirect(url_for('solvents'))


@app.route('/solquantchange/<solvent_id>')
def solquantchange(solvent_id):
    sol = mongo.db.solvents.find_one({"_id": ObjectId(solvent_id)})
    return render_template('solquantchange.html', solvent=sol)


@app.route('/solchange/<solvent_id>', methods=["POST"])
def solchange(solvent_id):
    mongo.db.solvents.update({'_id': ObjectId(solvent_id)},
    {
        'Name': request.form.get('Name'),
        'Supplier': request.form.get('Supplier'),
        'Cat_no': request.form.get('Cat_no'),
        'Grade': request.form.get('Grade'),
        'Min_Quantity': request.form.get('Min_Quantity'),
        'Quantity_Available': request.form.get('Quantity_Available'),
        'Quantity_Unit': request.form.get('Quantity_Unit'),
        'Price': request.form.get('Price'),
        'Currency': request.form.get('Currency'),
        'Comment': request.form.get('Comment')
    })
    return redirect(url_for('solvents'))


@app.route('/deletesolvent/<solvent_id>')
def deletesolvent(solvent_id):
    sol = mongo.db.solvents.find_one({"_id": ObjectId(solvent_id)})
    return render_template('deletesolvent.html', solvent=sol)


@app.route('/deletesolvent_delete/<solvent_id>')
def deletesolvent_delete(solvent_id):
    mongo.db.solvents.remove({'_id': ObjectId(solvent_id)})
    return redirect(url_for('solvents'))


@app.route('/addconsumables')
def addconsumables():
    return render_template("addconsumables.html")


@app.route('/addconsumables', methods=['POST'])
def addconsumables_add():
    mongo.db.consumables.insert_one(request.form.to_dict())
    return redirect(url_for('consumables'))


@app.route('/conquantchange/<consumable_id>')
def conquantchange(consumable_id):
    con = mongo.db.consumables.find_one({"_id": ObjectId(consumable_id)})
    return render_template('conquantchange.html', consumable=con)


@app.route('/conchange/<consumable_id>', methods=["POST"])
def conchange(consumable_id):
    mongo.db.consumables.update({'_id': ObjectId(consumable_id)},
    {
        'Name': request.form.get('Name'),
        'Supplier': request.form.get('Supplier'),
        'Cat_no': request.form.get('Cat_no'),
        'Min_Quantity': request.form.get('Min_Quantity'),
        'Quantity_Available': request.form.get('Quantity_Available'),
        'Quantity_Unit': request.form.get('Quantity_Unit'),
        'Price': request.form.get('Price'),
        'Currency': request.form.get('Currency'),
    })
    return redirect(url_for('consumables'))


@app.route('/deleteconsumable/<consumable_id>')
def deleteconsumable(consumable_id):
    con = mongo.db.consumables.find_one({"_id": ObjectId(consumable_id)})
    return render_template('deleteconsumable.html', consumable=con)


@app.route('/deleteconsumable_delete/<consumable_id>')
def deleteconsumable_delete(consumable_id):
    mongo.db.consumables.remove({'_id': ObjectId(consumable_id)})
    return redirect(url_for('consumables'))


@app.route('/request_table')
def request_table():
    return render_template("request_table.html")


@app.route('/requests')
def requests():
    return render_template("requests.html", requests=mongo.db.requests.find())


@app.route('/addrequest', methods=['POST'])
def addrequest():
    requests = mongo.db.requests
    requests.insert_one(request.form.to_dict())
    return redirect(url_for('request_table'))


@app.route('/requests_delete/<req_id>')
def requests_delete(req_id):
    mongo.db.requests.remove({'_id': ObjectId(req_id)})
    return redirect(url_for('requests'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)