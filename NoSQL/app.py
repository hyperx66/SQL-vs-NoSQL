from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import json
from time import gmtime, strftime
from bson.json_util import dumps

app = Flask(__name__)

# Establish connection to mongodb hosted on mongodb Atlas

# WEI JIAN ACCOUNT
# app.config[
#     "MONGO_URI"
# ] = "mongodb+srv://root:weijian!96@dbproject.bhdqc.mongodb.net/dbproject?retryWrites=true&w=majority"

# SHARED ACCOUNT
app.config[
    "MONGO_URI"
] = "mongodb+srv://admin:DBprojectCSC2008@dbproject.lkyvi.mongodb.net/dbproject?retryWrites=true&w=majority"
mongo = PyMongo(app)

# Declare the collection
products = mongo.db.products
roles = mongo.db.roles
stores = mongo.db.stores
users = mongo.db.users
items = mongo.db.Item


@app.route("/", methods=["GET"])
def get_products():
    all_products = products.find({}, {"name": 1, "price": 1, "quantity": 1})
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
    all_stores = list(stores.find(
        {}, {"_id": 0, "storeId": 1, "storeName": 1}))
    return json.dumps(all_stores)

@app.route("/loginUser", methods=["POST"])
def loginUser():
    username = request.form["username"]
    password = request.form["password"]

    cred_dict = {
        "loginUsername": username,
        "loginPassword": password
    }

    result = users.find_one(cred_dict)
    if result is not None:
        print("app.py LOG: logged in")
        print("app.py LOG: " + dumps(result))
        return dumps(result)
    else:
        print("app.py LOG: cannot find user/pass combo")
        return "0"

@app.route("/addUser", methods=["POST"])
def addUser():
    username = request.form["username"]
    password = request.form["password"]
    staffName = request.form["staffName"]
    mobileNum = request.form["mobileNum"]
    store = request.form["store"]
    role = request.form["role"]
    currentDateTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    mydict = {
        "staffName": staffName,
        "mobileNum": mobileNum,
        "storeId": store,
        "role": role,
        "createdDate": currentDateTime,
        "updatedDate": currentDateTime,
        "loginUsername": username,
        "loginPassword": password,
    }

    x = users.insert_one(mydict)
    if x is not None:
        return "1"
    else:
        return "0"

# Product Management


@app.route('/productManagement', methods=['GET'])
def productManagement():
    return render_template("productManagement.html")


@app.route('/getItemStore', methods=['GET'])
def get_ItemStore():
    all_products = list(items.find(
        {}, {"_id": 0, "itemid": 1, "itemName": 1, "price": 1, "quantity": 1}))
    print(json.dumps(all_products))
    return json.dumps(all_products)


# POS

@app.route("/getUser", methods=["GET"])
def getUser():
    user_arry = list(users.find({}, {"_id": 0, "staffName": 1}))
    print(user_arry)
    return json.dumps(user_arry)


@app.route("/getItemStore", methods=["GET"])
def getItemStore():
    all_products = list(items.find({}, {"_id": 0, "itemName": 1, "price": 1, "quantity": 1}))
    print(all_products)
    return json.dumps(all_products)


@app.route("/createTransaction", methods=["POST"])
def createTransaction():
    itemId = request.form["itemId"]
    chosenQuantity = request.form["chosenQuantity"]
    originalQuantity = request.form["originalQuantity"]
    resultingPrice = request.form["resultingPrice"]
    storeId = request.cookies.get("storeId")
    staffId = request.cookies.get("staffId")
    print(originalQuantity)
    print(staffId)

if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=True, threaded=True, port=8080)
