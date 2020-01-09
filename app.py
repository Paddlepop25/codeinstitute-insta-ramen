import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, ASCENDING, DESCENDING
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
    latest_three=mongo.db.ramens.find().sort([("_id", DESCENDING)]).limit(3)
    return render_template('index.html', title="Home", latest_three=latest_three)
    
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
    ramens=mongo.db.ramens.find({'continent': 'Asia'})
    return render_template('ramen_asia.html', title="Ramen from The Asia", ramens=ramens)
    
@app.route('/ramen_europe')
def ramen_europe():
    ramens=mongo.db.ramens.find({'continent': 'Europe'})
    return render_template('ramen_europe.html', title="Ramen from The Europe", ramens=ramens)
    
@app.route('/ramen_americas')
def ramen_americas():
    ramens=mongo.db.ramens.find({'continent': 'The Americas'})
    return render_template('ramen_americas.html', title="Ramen from The Americas", ramens=ramens)    
    
@app.route('/ramen_rest_world')
def ramen_rest_world():
    ramens=mongo.db.ramens.find({'continent': 'The Rest'})
    return render_template('ramen_rest_world.html', title="Ramen from the Rest Of The World", ramens=ramens)    
    
# @app.route('/ramen_world')
# def ramen_world():
#     ramens=mongo.db.ramens.find(
#         {'$or':
#             [{'continent': 'Asia'},{'continent': "Europe"},{'continent': "The Americas"},{'continent': "The Rest"}]
#         }
#         )
#     return render_template('ramen_world.html', title="Rest Of The World", ramens=ramens)    

@app.route('/search_ramen')
def search_ramen():
    orig_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(orig_query)), '$options': 'i'}
    print(query)
    results=mongo.db.ramens.find({'flavour': query})
    
    ramen = []
    for result in results:
        ramen.append(result)
    
    return render_template('ramen_search.html', title="Search Results", query=orig_query, ramen_search=ramen)
    
@app.route('/add_ramen')
def add_ramen():
    brands = mongo.db.brands.find().sort([("brand", ASCENDING)])
    countries=mongo.db.countries.find().sort([("country", ASCENDING)])
    return render_template('add_ramen.html', title="Add a Ramen", countries=countries, brands=brands)
    
@app.route('/insert_ramen', methods=['POST'])
def insert_ramen():
    ramens = mongo.db.ramens
    if "ramen_image" in request.files:
        ramen_image = request.files['ramen_image']
        mongo.save_file(ramen_image.filename, ramen_image)
        
    new_ramen = {
        'brand': request.form.get('brand'),
        'flavour':request.form.get('flavour'),
        'style': request.form.get('style'),
        'country':request.form.get('country'),
        'continent':request.form.get('continent'),
        'stars':int(request.form.get('stars')),
        'reviews':request.form.get('reviews'),
        'imageURL': ramen_image.filename
    }
    ramens.insert_one(new_ramen)
    return redirect(url_for('get_ramen'))    

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)
    
@app.route('/edit_ramen/<ramen_id>', methods=['GET'])
def edit_ramen(ramen_id):
    ramen = mongo.db.ramens.find_one({"_id": ObjectId(ramen_id)})
    brands = mongo.db.brands.find().sort([("brand", ASCENDING)])
    countries = mongo.db.countries.find().sort([("country", ASCENDING)])
    return render_template('edit_ramen.html', title="Edit Ramen", ramen=ramen, brands=brands, countries=countries)

@app.route('/update_ramen/<ramen_id>', methods=["POST"])
def update_ramen(ramen_id):
    ramen = mongo.db.ramens.find_one({"_id": ObjectId(ramen_id)})
    
    # try code
    brand = request.form.get('brand')
    flavour = request.form.get('flavour')
    style = request.form.get('style')
    country = request.form.get('country')
    stars = int(request.form.get('stars'))
    reviews = request.form.get('reviews')
    # end of try code
    
    if "ramen_image" in request.files and request.files['ramen_image'].filename != "":
        ramen_image = request.files['ramen_image']
        image_filename = ramen_image.filename
        mongo.save_file(ramen_image.filename, ramen_image)
    else:
        image_filename = ramen['imageURL']
        
    ramen.update( {'_id': ObjectId(ramen_id)},
    {
        'brand': brand,
        'flavour': flavour,
        'style': style,
        'country': country,
        'stars': int(stars),
        'reviews': reviews,
        'imageURI': image_filename
    })
    return redirect(url_for('get_ramen'))
    
@app.route('/delete_ramen/<ramen_id>')
def delete_ramen(ramen_id):
    mongo.db.ramens.remove({'_id': ObjectId(ramen_id)})
    return redirect(url_for('get_ramen'))

@app.route('/add_brands')
def add_brands():
    brand = mongo.db.brands.find()
    add_a_brand = mongo.db.ramens.find()
    return render_template('add_brands.html', title="Add a Brand", brand=brand)
    
@app.route('/insert_brand', methods=['POST'])
def insert_brand():
    brand = mongo.db.brands
    query = request.form.get('brand').lower()
    find_brand = mongo.db.brands.find_one({'brand': query})
    if find_brand is None:
        new_brand = {
            'brand': request.form.get('brand').lower()
        }
        brand.insert_one(new_brand)
    return redirect(url_for('add_ramen'))       
    
@app.errorhandler(404)
def error_404(not_found):
    return render_template('error404.html', title="Error 404")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)    