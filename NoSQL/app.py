from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import json
from time import gmtime, strftime
from bson.json_util import dumps
from bson.objectid import ObjectId

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
item = mongo.db.Item
roles = mongo.db.Role
stores = mongo.db.Store
users = mongo.db.User
storeItem = mongo.db.Store_Item
transaction = mongo.db.Transaction
stats = mongo.db.Stats

# @app.route("/", methods=["GET"])
# def get_products():
#     all_products = item.find({}, {"itemName": 1, "price": 1, "quantity": 1})
#     return render_template("posDashboard.html", all_products=all_products)


@app.route("/", methods=["GET"])
def get_products():
    return render_template("posDashboard.html")


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


@app.route("/loginUser", methods=["POST"])
def loginUser():
    username = request.form["username"]
    password = request.form["password"]

    cred_dict = {"loginUsername": username, "loginPassword": password}

    result = users.find_one(cred_dict)
    if result is not None:
        print("app.py loginUser LOG: logged in")
        print("app.py loginUser LOG: " + dumps(result))
        return dumps(result)
    else:
        print("app.py loginUser LOG: cannot find user/pass combo")
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


@app.route("/productManagement", methods=["GET"])
def productManagement():
    return render_template("productManagement.html")


@app.route("/getItemStore", methods=["GET"])
def get_ItemStore():
    storeId = int(request.cookies.get("storeId"))
    all_products = list(
        item.find({}, {"_id": 0, "itemId": 1, "itemName": 1, "price": 1, "quantity": 1})
    )
    new_all_products = []
    for product in all_products:
        prodItem = storeItem.find_one(
            {"StoreId": storeId, "ItemId": int(product["itemId"])}
        )
        product["quantity"] = prodItem["Quantity"]
        new_all_products.append(product)

    return json.dumps(new_all_products)


@app.route("/updateProduct", methods=["POST"])
def updateProduct():
    productName = request.form["productName"]
    productPrice = request.form["productPrice"]
    productQuantity = request.form["productQuantity"]
    itemId = request.form["itemId"]
    myquery = {"itemId": itemId}
    newvalues = {
        "$set": {
            "itemId": itemId,
            "itemName": productName,
            "price": productPrice,
            "quantity": productQuantity,
        }
    }
    x = item.update_one(myquery, newvalues)
    if x is not None:
        return "1"
    else:
        return "0"


# POS/Management Page
@app.route("/getUser", methods=["POST"])
def getUser():
    staff_id = request.cookies.get("staffId")
    print("app.py getUser LOG: " + staff_id)

    staffid_dict = {"_id": ObjectId(staff_id)}

    result = users.find_one(staffid_dict)

    if result is not None:
        print("app.py getUser LOG: found" + dumps(result))
        return dumps(result)
    else:
        print("app.py getUser LOG: cannot getUser")
        return "0"

# Staff DashBoard
@app.route("/staffDashboard", methods=["GET"])
def staffDashboard():
    return render_template("staffDashboard.html")

# getStats to populate Chart/Overview Values
"""
@app.route("/getStats", methods=["GET"])
def getStats():
    # Check form
    store_id = str(request.cookies.get("storeId"))
    print("app.py getStats LOG: " + store_id)
    return ("app.py getStats LOG: " + store_id)
"""



"""
@app.route("/getItemStore", methods=["GET"])
def getItemStore():
    all_products = list(
        item.find({}, {"_id": 0, "itemName": 1, "price": 1, "quantity": 1}))
    print(all_products)
    return json.dumps(all_products)
"""


@app.route("/createTransaction", methods=["POST"])
def createTransaction():
    print("Hi, testing 123")
    print(request.form)
    itemId = int(request.form["itemId"])
    chosenQuantity = request.form["chosenQuantity"]
    originalQuantity = request.form["originalQuantity"]
    resultingPrice = request.form["resultingPrice"]
    storeId = int(request.cookies.get("storeId"))
    staffId = request.cookies.get("staffId")
    currentDateTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print(storeId)
    print(staffId)
    print("Hello world")

    newQty = int(originalQuantity) - int(chosenQuantity)

    mydict = {
        "transactionBy": staffId,
        "storeId": storeId,
        "itemPurchased": itemId,
        "quantityPurchased": chosenQuantity,
        "price": resultingPrice,
        "datePurchased": currentDateTime,
    }
    x = transaction.insert_one(mydict)

    updateDict = {
        "StoreId": storeId,
        "ItemId": itemId,
        "Quantity": newQty,
    }
    myquery = {"StoreId": storeId, "ItemId": itemId}
    newvalues = {"$set": {"Quantity": newQty}}

    y = storeItem.update_one(myquery, newvalues)

    print("Hello hell")
    print("x is", x)
    print("y is", y)

    if x:
        return "1"
    else:
        return "0"


if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=True, threaded=True, port=8080)
