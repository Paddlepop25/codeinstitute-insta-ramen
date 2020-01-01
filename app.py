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
    
@app.route('/top_five')
def top_five():
    five_ramens=mongo.db.ramens.find({ 'Stars': {'$gt': 3, '$lt':5} }).limit(5)
    return render_template('top_five.html', five_ramens=five_ramens)

@app.route('/display_ramen/<ramen_id>', methods=['GET'])
def display_ramen(ramen_id):
    ramen = mongo.db.ramens.find_one({"_id": ObjectId(ramen_id)})
    return render_template('display_ramen.html', ramen=ramen)   
    
    
@app.route('/get_ramen')
def get_ramen():
    ramens=mongo.db.ramens.find()
    return render_template('ramen-collection.html', ramens=ramens)
    
    
# @app.route('/ramen_asia')
# def ramen_asia():
#     ramens=mongo.db.ramens.find(
#         {'$or':
#             [{'Country': 'Taiwan'},{'Country': "Japan"}]
#         }
#         )
#     return render_template('ramen_asia.html', ramens=ramens)

@app.route('/ramen_asia')
def ramen_asia():
    ramens=mongo.db.ramens.find(
        {'$or':
            [{'Country': 'Taiwan'},{'Country': "Japan"}]
        }
        )
    return render_template('ramen_asia.html', ramens=ramens)
    
@app.route('/ramen_world')
def ramen_world():
    ramens=mongo.db.ramens.find(
        {'$or':
            [{'Country': 'Brunei'},{'Country': "Singapore"}]
        }
        )
    return render_template('ramen_world.html', ramens=ramens)    

@app.route('/search_ramen/', methods=["GET", "POST"])
def search_ramen():
    if request.method == "POST":
        post_request = request.form.get('searchbar_input')
        print(post_request)
    # return render_template("search_ramen.html",
    #                         local_category=mongo.db.flavours.find(), 
    #                         recipes=mongo.db.recipes.find({"title" : {"$regex": post_request, "$options": "i"}}),
    #                         recipe_count=mongo.db.recipes.find({"title" : {"$regex": post_request, "$options": "i"}}).count())
    
    
@app.route('/add_ramen')
def add_ramen():
    return render_template('add_ramen.html', countries=mongo.db.countries.find())
    
@app.route('/insert_ramen', methods=['POST'])
def insert_ramen():
    ramens = mongo.db.ramens
    ramens.insert_one(request.form.to_dict())
    return redirect(url_for('get_ramen'))    
    
@app.route('/edit_ramen/<ramen_id>', methods=['GET'])
def edit_ramen(ramen_id):
    ramen = mongo.db.ramens.find_one({"_id": ObjectId(ramen_id)})
    countries = mongo.db.countries.find()
    return render_template('edit_ramen.html', ramen=ramen, countries=countries)
    

@app.route('/update_ramen/<ramen_id>', methods=["POST"])
def update_ramen(ramen_id):
    ramen = mongo.db.ramens
    ramen.update( {'_id': ObjectId(ramen_id)},
    {
        'Brand': request.form.get('Brand'),
        'Flavour':request.form.get('Flavour'),
        'Style': request.form.get('Style'),
        'Country':request.form.get('Country'),
        'Stars':request.form.get('Stars'),
        'Ratings':request.form.get('Ratings')
    })
    return redirect(url_for('get_ramen'))
    
@app.route('/delete_ramen/<ramen_id>')
def delete_ramen(ramen_id):
    mongo.db.ramens.remove({'_id': ObjectId(ramen_id)})
    return redirect(url_for('get_ramen'))
    
@app.route('/get_brands')
def get_brands():
    brands = mongo.db.ramens.find()
    return render_template('brands.html',
                            brands=brands)

@app.errorhandler(404)
def error_404(not_found):
    return render_template('error404.html', not_found=not_found)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)    