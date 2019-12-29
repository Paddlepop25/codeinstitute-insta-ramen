import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'ramen_database'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-mg1xb.mongodb.net/ramen_database?retryWrites=true&w=majority'

ramen = PyMongo(app)

@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template('index.html')
    
@app.route('/award_winning')
def award_winning():
    return render_template('award_winning.html')

@app.route('/get_ramen')
def get_ramen():
    return render_template('ramen.html', selections=ramen.db.selections.find())
    
@app.route('/add_ramen')
def add_ramen():
    return render_template('add_ramen.html')
    
@app.route('/insert_ramen', methods=['POST'])
def insert_ramen():
    new_ramen = ramen.db.selections
    new_ramen.insert_one(request.form.to_dict())
    return redirect(url_for('get_ramen'))    
    
@app.route('/edit_ramen/<selection_id>')
def edit_ramen(selection_id):
    the_ramen = ramen.db.selections.find_one({"_id": ObjectId(selection_id)})
    all_brands = ramen.db.brands.find()
    return render_template('edit_ramen.html', ramen=the_ramen,
                          brands=all_brands)     

# @app.route('/update_ramen/<selection_id>', methods=["POST"])
# def update_ramen(selection_id):
#     the_ramen = ramen.db.selections
#     the_ramen.update( {'_id': ObjectId(selection_id)},
#     {
#         'Review':request.form.get('Review'),
#         'Brand': request.form.get('Brand'),
#         'Flavour':request.form.get('Flavour'),
#         'Style': request.form.get('Style'),
#         'Country':request.form.get('Country'),
#         'Stars':request.form.get('Stars')
#     })
#     return redirect(url_for('get_ramen'))
    
@app.route('/delete_ramen/<selection_id>')
def delete_ramen(selection_id):
    ramen.db.selections.remove({'_id': ObjectId(selection_id)})
    return redirect(url_for('get_ramen'))
    
@app.route('/add_brands')
def add_brands():
    return render_template('add_brands.html')    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)    