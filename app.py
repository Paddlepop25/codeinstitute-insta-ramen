import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'ramen_database'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-mg1xb.mongodb.net/ramen_database?retryWrites=true&w=majority'

ramen = PyMongo(app)

@app.route('/')
@app.route('/award_winning')
def award_winning():
    return render_template('award_winning.html')

@app.route('/get_ramen')
def get_ramen():
    return render_template('get_ramen.html', selections=ramen.db.selections.find())
    
@app.route('/add_ramen')
def add_ramen():
    return render_template('add_ramen.html')
    
@app.route('/add_brands')
def add_brands():
    return render_template('add_brands.html')    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)    