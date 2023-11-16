from flask import Flask,jsonify,request,abort
import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

db_client = pymongo.MongoClient(os.getenv('mongo_string'))
database = db_client.get_database("CodingChallengeBot")
collection = database.get_collection("Challenges")

@app.route("/api/search")
def search():
    arr = list(collection.find().limit(10))
    return jsonify(arr)

@app.route("/api/challenge/<id>")
def get_challenge(id):
    query = list(collection.find({"_id": id}))
    if len(query) > 0:
        return jsonify(query[0])
    else:
        abort(404)