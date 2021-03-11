from flask import Flask, render_template
from flask_pymongo import PyMongo
app = Flask(__name__)

# Establish connection to mongodb hosted on mongodb Atlas
app.config['MONGO_URI'] = 'mongodb+srv://root:weijian!96@dbproject.bhdqc.mongodb.net/dbproject?retryWrites=true&w=majority'
mongo = PyMongo(app)

# Declare the collection
products = mongo.db.products

# @app.route('/')
# def index():
#     return render_template('posDashboard.html')

@app.route('/', methods=['GET'])
def get_products():
    all_products = products.find({},{"name":1, "price":1, "quantity":1})
    return render_template('posDashboard.html', all_products = all_products)
