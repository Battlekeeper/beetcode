from flask import Flask,jsonify,request,abort
from flask_cors import CORS, cross_origin
import pymongo
import os
from dotenv import load_dotenv
import json
from codeValidator import validateCode
load_dotenv()

app = Flask(__name__)

db_client = pymongo.MongoClient(os.getenv('mongo_string'))
database = db_client.get_database("CodingChallengeBot")
collection = database.get_collection("Challenges")

cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

@cross_origin()
@app.route("/api/search", methods=['POST'])
def search():
    
    search_query = json.loads(request.get_data())
    
    mongo_query = {}

    if search_query["text"] != '':
        mongo_query["$text"] = {'$search': 'coin'}
    if search_query["lang"] != "any":
        mongo_query[f'code.{search_query["lang"]}'] = {"$exists": True}
    if search_query["difficulty"] != "any":
        mongo_query["difficulty"] = int(search_query["difficulty"])
    print(mongo_query)

    arr = list(collection.find(mongo_query).limit(10).skip(int(search_query["page"]) * 10))

    cleaned = list()

    for doc in arr:
        if ("code" in doc):
            cleaned.append({'_id': doc["_id"], 'name': doc["name"], 'difficulty': doc["difficulty"], 'langs': list(doc["code"].keys())})
    return jsonify(cleaned)

@cross_origin()
@app.route("/api/challenge/<id>", methods=['GET'])
def get_challenge(id):
    query = list(collection.find({"_id": id}))
    if len(query) > 0:
        return jsonify(query[0])
    else:
        abort(404)

@cross_origin()
@app.route("/api/runcode/<id>", methods=['POST'])
def run_code(id):
    query = list(collection.find({"_id": id}))

    recivedData = json.loads(request.get_data())
    #TODO: Validate the recived request
    
    if len(query) == 0:
        return abort(404)
    doc = query[0]

    response = validateCode(recivedData["code"], doc["code"][recivedData["lang"]]["exampleFixture"], recivedData["lang"])
    return response

app.run("0.0.0.0", 3001)