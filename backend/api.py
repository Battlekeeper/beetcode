from flask import Flask,jsonify,request
import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

db_client = pymongo.MongoClient(os.getenv('mongo_string'))
database = db_client.get_database("CodingChallengeBot")
collection = database.get_collection("Challenges")

@app.route("/")
def hello_world():
    arr = list(collection.find().limit(10))
    return jsonify(arr)