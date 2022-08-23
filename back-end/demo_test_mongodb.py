from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://dev.metattri.com:27017/bupt"
mongo = PyMongo(app)
online_users = mongo.db.users.find({"online": True})
print(online_users)
