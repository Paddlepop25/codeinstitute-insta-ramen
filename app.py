import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'ramen_database'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-mg1xb.mongodb.net/ramen_database?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template('index.html')
    
@app.route('/award_winning')
def award_winning():
    return render_template('award_winning.html')

@app.route('/ramen_asia')
def ramen_asia():
    selections=mongo.db.selections.find()
    return render_template('ramen_asia.html', selections=selections)


@app.route('/get_ramen')
def get_ramen():
    selections=mongo.db.selections.find()
    return render_template('ramen.html', selections=selections)
    
@app.route('/add_ramen')
def add_ramen():
    return render_template('add_ramen.html', countries=mongo.db.countries.find())
    
@app.route('/insert_ramen', methods=['POST'])
def insert_ramen():
    ramen = mongo.db.selections
    brands = mongo.db.brands.find()
    ramen.insert_one(request.form.to_dict())
    brands.insert_one(request.form.to_dict())
    return redirect(url_for('get_ramen'))    
    
@app.route('/edit_ramen/<ramen_id>', methods=['GET', 'POST'])
def edit_ramen(ramen_id):
    edit_ramen = mongo.db.selections.find_one({"_id": ObjectId(ramen_id)})
    countries = mongo.db.countries.find()
    all_brands = mongo.db.brands.find()
    return render_template('edit_ramen.html', ramen=edit_ramen,
                          brands=all_brands, countries=countries)     

@app.route('/update_ramen/<ramen_id>', methods=["POST"])
def update_ramen(ramen_id):
    the_ramen = mongo.db.selections
    the_ramen.update( {'_id': ObjectId(ramen_id)},
    {
        'Brand': request.form.get('Brand'),
        'Flavour':request.form.get('Flavour'),
        'Style': request.form.get('Style'),
        'Country':request.form.get('Country'),
        'Stars':request.form.get('Stars')
    })
    return redirect(url_for('get_ramen'))
    
@app.route('/delete_ramen/<ramen_id>')
def delete_ramen(ramen_id):
    mongo.db.selections.remove({'_id': ObjectId(ramen_id)})
    return redirect(url_for('get_ramen'))
    
@app.route('/get_brands')
def get_brands():
    return render_template('brands.html',
                            brands=mongo.db.brands.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)    