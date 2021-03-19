from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
import json

app = Flask(__name__)

# Establish connection to mongodb hosted on mongodb Atlas
app.config[
    "MONGO_URI"
] = "mongodb+srv://root:weijian!96@dbproject.bhdqc.mongodb.net/dbproject?retryWrites=true&w=majority"
mongo = PyMongo(app)

# Declare the collection
products = mongo.db.products
roles = mongo.db.roles
stores = mongo.db.stores


@app.route("/", methods=["GET"])
def get_products():
    all_products = products.find({}, {"name": 1, "price": 1, "quantity": 1})
    # for i in all_products:
    #     print(i)
    return render_template("posDashboard.html", all_products=all_products)


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


# REGISTER PAGE API's
@app.route("/register", methods=["GET"])
def registerPage():
    return render_template("register.html")


@app.route("/getRoles", methods=["GET"])
def getRoles():
    all_roles = list(roles.find({}, {"_id": 0, "roleId": 1, "roleName": 1}))
    return json.dumps(all_roles)


@app.route("/getStores", methods=["GET"])
def getStores():
    all_stores = list(stores.find({}, {"_id": 0, "storeId": 1, "storeName": 1}))
    return json.dumps(all_stores)


if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=True, threaded=True, port=8080)
