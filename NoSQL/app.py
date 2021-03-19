from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

# Establish connection to mongodb hosted on mongodb Atlas
app.config[
    "MONGO_URI"
] = "mongodb+srv://root:weijian!96@dbproject.bhdqc.mongodb.net/dbproject?retryWrites=true&w=majority"
mongo = PyMongo(app)

# Declare the collection
products = mongo.db.products


@app.route("/", methods=["GET"])
def get_products():
    all_products = products.find({}, {"name": 1, "price": 1, "quantity": 1})
    # for i in all_products:
    #     print(i)
    return render_template("posDashboard.html", all_products=all_products)


if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=True, threaded=True, port=8080)
