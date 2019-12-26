import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'ramen_database'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-mg1xb.mongodb.net/ramen_database?retryWrites=true&w=majority'
ramen = PyMongo(app)

@app.route('/')
@app.route('/get_flavours')
def get_flavours():
    return render_template('flavours.html', flavours=ramen.db.flavours.find())
# @app.route('/get_tasks')
# def get_tasks():
#     return render_template("tasks.html", tasks=mongo.db.tasks.find())    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)    