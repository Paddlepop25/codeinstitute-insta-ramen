import os
from flask import Flask, render_template, redirect, request, url_for, send_from_directory
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId
import re
import math
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/ubuntu/environment/uploads'
app.config['MONGO_DBNAME'] = 'ramen_database'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
def index():
    lastest_three=mongo.db.ramens.find().sort([("_id", DESCENDING)]).limit(3)
    return render_template('index.html', title="Home", lastest_three=lastest_three)
    
@app.route('/display_ramen/<ramen_id>', methods=['GET'])
def display_ramen(ramen_id):
    ramen = mongo.db.ramens.find_one({"_id": ObjectId(ramen_id)})
    return render_template('display_ramen.html', title="Display Ramen", ramen=ramen)   
    
@app.route('/get_ramen')
def get_ramen():
    ramens=mongo.db.ramens.find().sort([("_id", DESCENDING)])
    return render_template('ramen_collection.html', title="Ramen Collection", ramens=ramens)
    
@app.route('/ramen_asia')
def ramen_asia():
    ramens=mongo.db.ramens.find({'Continent': 'Asia'})
    return render_template('ramen_asia.html', title="Asian", ramens=ramens)
    
@app.route('/ramen_europe')
def ramen_europe():
    ramens=mongo.db.ramens.find({'Continent': 'Europe'})
    return render_template('ramen_europe.html', title="Europe", ramens=ramens)
    
@app.route('/ramen_americas')
def ramen_americas():
    ramens=mongo.db.ramens.find({'Continent': 'The Americas'})
    return render_template('ramen_americas.html', title="Europe", ramens=ramens)    
    
@app.route('/ramen_rest_world')
def ramen_rest_world():
    ramens=mongo.db.ramens.find({'Continent': 'The Rest'})
    return render_template('ramen_rest_world.html', title="Rest Of The World", ramens=ramens)    
    
@app.route('/ramen_world')
def ramen_world():
    ramens=mongo.db.ramens.find(
        {'$or':
            [{'Continent': 'Asia'},{'Continent': "Europe"},{'Continent': "The Americas"},{'Continent': "The Rest"}]
        }
        )
    return render_template('ramen_world.html', title="Rest Of The World", ramens=ramens)    

@app.route('/search_ramen')
def search_ramen():
    orig_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(orig_query)), '$options': 'i'}
    print(query)
    results=mongo.db.ramens.find({'Flavour': query})
    
    # if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         return redirect(url_for('uploaded_file',
    #                                 filename=filename))
                                    
    ramen = []
    for result in results:
        ramen.append(result)
    
    return render_template('ramen_search.html', title="Search Results", query=orig_query, ramen_search=ramen)
    
@app.route('/add_ramen')
def add_ramen():
    brands = mongo.db.brands.find()
    countries=mongo.db.countries.find()
    return render_template('add_ramen.html', title="Add a Ramen", countries=countries, brands=brands)
    
@app.route('/insert_ramen', methods=['POST'])
def insert_ramen():
    ramens = mongo.db.ramens
    new_ramen = {
        'Brand': request.form.get('Brand'),
        'Flavour':request.form.get('Flavour'),
        'Style': request.form.get('Style'),
        'Country':request.form.get('Country'),
        'Stars':int(request.form.get('Stars')),
        'Ratings':request.form.get('Ratings')
    }
    ramens.insert_one(new_ramen)
    return redirect(url_for('get_ramen'))    
    
@app.route('/edit_ramen/<ramen_id>', methods=['GET'])
def edit_ramen(ramen_id):
    ramen = mongo.db.ramens.find_one({"_id": ObjectId(ramen_id)})
    brands = mongo.db.brands.find()
    countries = mongo.db.countries.find()
    return render_template('edit_ramen.html', title="Edit Ramen", ramen=ramen, brands=brands, countries=countries)

@app.route('/update_ramen/<ramen_id>', methods=["POST"])
def update_ramen(ramen_id):
    ramen = mongo.db.ramens
    ramen.update( {'_id': ObjectId(ramen_id)},
    {
        'Brand': request.form.get('Brand'),
        'Flavour':request.form.get('Flavour'),
        'Style': request.form.get('Style'),
        'Country':request.form.get('Country'),
        'Stars':int(request.form.get('Stars')),
        'Ratings':request.form.get('Ratings')
    })
    return redirect(url_for('get_ramen'))
    
@app.route('/delete_ramen/<ramen_id>')
def delete_ramen(ramen_id):
    mongo.db.ramens.remove({'_id': ObjectId(ramen_id)})
    return redirect(url_for('get_ramen'))
    
@app.route('/get_brands')
def get_brands():
    brands = mongo.db.brands.find()
    return render_template('brands.html', title="Ramen Brands", brands=brands)

@app.route('/add_brands')
def add_brands():
    brands = mongo.db.brands.find()
    add_a_brand = mongo.db.ramens.find()
    return render_template('add_brands.html', title="Add a Brand", add_a_brand=add_a_brand, brands=brands)
    
@app.route('/insert_brand', methods=['POST'])
def insert_brand():
    brand = mongo.db.brands
    query = request.form.get('Brand').lower()
    find_brand = mongo.db.brands.find_one({'Brand': query})
    if find_brand is None:
        new_brand = {
            'Brand': request.form.get('Brand').lower()
        }
        brand.insert_one(new_brand)
    return redirect(url_for('add_ramen'))       
    
@app.errorhandler(404)
def error_404(not_found):
    return render_template('error404.html', title="Error 404", not_found=not_found)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)    