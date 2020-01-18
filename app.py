import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, ASCENDING, DESCENDING
from bson.objectid import ObjectId
import re
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Setting environment and private key
app.config['MONGO_DBNAME'] = 'ramen_database'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

# Home page
@app.route('/')
def index():
    latest_three=mongo.db.ramens.find().sort([("_id", DESCENDING)]).limit(3)
    return render_template('index.html', title="Home", latest_three=latest_three)

# Display ramen page
@app.route('/display_ramen/<ramen_id>', methods=['GET'])
def display_ramen(ramen_id):
    ramen = mongo.db.ramens.find_one({"_id": ObjectId(ramen_id)})
    return render_template('display_ramen.html', title="Display Ramen", ramen=ramen)   

# Ramen Collection page    
@app.route('/get_ramen')
def get_ramen():
    ramens=mongo.db.ramens.find().sort([("_id", DESCENDING)])
    return render_template('ramen_collection.html', title="Ramen Collection", ramens=ramens)
    
# Ramen in Asia page    
@app.route('/ramen_asia')
def ramen_asia():
    ramens=mongo.db.ramens.find({'continent': 'Asia'})
    return render_template('ramen_asia.html', title="Ramen from Asia", ramens=ramens)

# Ramen in Europe page    
@app.route('/ramen_europe')
def ramen_europe():
    ramens=mongo.db.ramens.find({'continent': 'Europe'})
    return render_template('ramen_europe.html', title="Ramen from Europe", ramens=ramens)

# Ramen in the Americas page    
@app.route('/ramen_americas')
def ramen_americas():
    ramens=mongo.db.ramens.find({'continent': 'The Americas'})
    return render_template('ramen_americas.html', title="Ramen from The Americas", ramens=ramens)    
    
# Ramen in the Rest of the World page    
@app.route('/ramen_rest_world')
def ramen_rest_world():
    ramens=mongo.db.ramens.find({'continent': 'The Rest'})
    return render_template('ramen_rest_world.html', title="Ramen from the Rest Of The World", ramens=ramens)    

# Search for ramen flavours by users
@app.route('/search_ramen/', methods=["GET", "POST"])
def search_ramen():
    post_request = request.args['query']
    return render_template("ramen_search.html",
                            title="Search Results",
                            query=post_request,
                            ramen_search=mongo.db.ramens.find({"flavour" : {"$regex": post_request, "$options": "i"}}),
                            ramen_count=mongo.db.ramens.find({"flavour" : {"$regex": post_request, "$options": "i"}}).count())

# Add Ramen Page                           
@app.route('/add_ramen')
def add_ramen():
    brands = mongo.db.brands.find().sort([("brand", ASCENDING)])
    countries=mongo.db.countries.find().sort([("country", ASCENDING)])
    return render_template('add_ramen.html', title="Add a Ramen", countries=countries, brands=brands)

# Inserting ramen record into database    
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

# Uploading of image files
@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)


# Add brands page
@app.route('/add_brands')
def add_brands():
    brand = mongo.db.brands.find()
    add_a_brand = mongo.db.ramens.find()
    return render_template('add_brands.html', title="Add a Brand", brand=brand)
    
# Inserting ramen brand into database     
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
    
# Edit ramen page 
@app.route('/edit_ramen/<ramen_id>', methods=['GET'])
def edit_ramen(ramen_id):
    ramen = mongo.db.ramens.find_one({"_id": ObjectId(ramen_id)})
    brands = mongo.db.brands.find().sort([("brand", ASCENDING)])
    countries = mongo.db.countries.find().sort([("country", ASCENDING)])
    return render_template('edit_ramen.html', title="Edit Ramen", ramen=ramen, brands=brands, countries=countries)

# Save changes to edit form to database
@app.route('/update_ramen/<ramen_id>', methods=["POST"])
def update_ramen(ramen_id):
    ramen = mongo.db.ramens.find_one({"_id": ObjectId(ramen_id)})
    brand = request.form.get('brand')
    flavour = request.form.get('flavour')
    style = request.form.get('style')
    country = request.form.get('country')
    continent = request.form.get('continent')
    stars = int(request.form.get('stars'))
    reviews = request.form.get('reviews') 
        
    if 'ramen_image' in request.files and request.files['ramen_image'].filename != "":
        ramen_image = request.files['ramen_image']
        image_filename = ramen_image.filename
        mongo.save_file(ramen_image.filename, ramen_image)
    else:
        image_filename = ramen['imageURL']
        
    mongo.db.ramens.update( {'_id': ObjectId(ramen_id)},
    {
        'brand': brand,
        'flavour': flavour,
        'style': style,
        'country': country,
        'continent': continent,
        'stars': int(stars),
        'reviews': reviews,
        'imageURL': image_filename
    })
    return redirect(url_for('get_ramen'))

# Delete ramen from database
@app.route('/delete_ramen/<ramen_id>')
def delete_ramen(ramen_id):
    mongo.db.ramens.remove({'_id': ObjectId(ramen_id)})
    return redirect(url_for('get_ramen'))

# Error 404 page    
@app.errorhandler(404)
def error_404(not_found):
    return render_template('error404.html', title="Error 404")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)    