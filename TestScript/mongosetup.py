import pymongo
from datetime import datetime
import pandas as pd
from pymongo import MongoClient

df = pd.read_csv("Cleaned_Online_Retail_Dataset-5.csv")

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient.dbproject
itemCol = mydb.Item
roleCol = mydb.Role
statsCol = mydb.Stats
storeCol = mydb.Store
storeItemCol = mydb.Store_Item
transactionCol = mydb.Transaction
userCol = mydb.User


def populateRole():
    rolelist = [
        {"roleId": 1, "roleName": "Employee"},
        {"roleId": 2, "roleName": "Manager"},
        {"roleId": 3, "roleName": "Executive"},
    ]

    x = roleCol.insert_many(rolelist)
    print("Populated roles collection")
    print(x)


def populateStats():
    statslist = [
        {"earnings": 149.97, "months": 2, "transactions": 1, "year": 2021},
        {"earnings": 760.35, "months": 3, "transactions": 3, "year": 2021},
    ]

    x = statsCol.insert_many(statslist)
    print("Populated stats collection")
    print(x)


def populateUser():
    userlist = [
        {
            "staffName": "John",
            "mobileNum": "91865923",
            "storeId": "1",
            "role": "1",
            "createdDate": "2021-03-19 10:42:25",
            "updatedDate": "2021-03-19 10:42:25",
            "loginUsername": "user1",
            "loginPassword": "password",
        },
        {
            "staffName": "Kelly",
            "mobileNum": "86499475",
            "storeId": "1",
            "role": "2",
            "createdDate": "2021-03-19 10:42:25",
            "updatedDate": "2021-03-19 10:42:25",
            "loginUsername": "user2",
            "loginPassword": "password",
        },
        {
            "staffName": "Bob",
            "mobileNum": "84658282",
            "storeId": "1",
            "role": "3",
            "createdDate": "2021-03-19 10:42:25",
            "updatedDate": "2021-03-19 10:42:25",
            "loginUsername": "user3",
            "loginPassword": "password",
        },
    ]

    x = userCol.insert_many(userlist)
    print("Populated users collection")
    for i in x.inserted_ids:
        populateTransaction(str(i))


def populateStore():
    storelist = [
        {
            "_id": 1,
            "storeName": "Raffles City Store",
            "storeId": "1",
            "createdDate": datetime.now(),
            "updatedDate": datetime.now(),
            "deletedDate": datetime.now(),
        }
    ]

    x = storeCol.insert_many(storelist)
    print("Populated store collection")
    print(x)


def populateTransaction(userId):
    transactionlist = [
        {
            "transactionBy": userId,
            "storeId": 1,
            "itemPurchased": 1,
            "quantityPurchased": "20",
            "price": "10",
            "datePurchased": "2021-03-19 13:15:05",
        }
    ]

    x = transactionCol.insert_many(transactionlist)
    print("Populated transaction collection for", userId)
    print(x)


def populateFromCSV():
    counter = 0
    for index, row in df.iterrows():
        counter = index + 1
        item = {
            "_id": counter,
            "itemId": counter,
            "itemName": row["Description"],
            "itemDesc": row["Description"],
            "price": str(row["UnitPrice"]),
            "updatedBy": 1,
            "quantity": row["Quantity"],
        }

        store_item = {
            "_id": counter,
            "storeId": 1,
            "itemId": counter,
            "itemName": row["Description"],
            "quantity": row["Quantity"],
            "price": str(row["UnitPrice"]),
        }

        itemCol.insert_one(item)
        storeItemCol.insert_one(store_item)

    print(counter)


if __name__ == "__main__":
    print("starting")
    # populateRole()
    # populateStats()
    # populateUser()
    # populateStore()
    populateFromCSV()