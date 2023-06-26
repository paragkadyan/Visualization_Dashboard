from flask import Flask, jsonify
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['vdashboard']
collection = db['dashboarddata']

# API endpoint to retrieve data
@app.route('/api/data', methods=['GET'])
def get_data():
    data = list(collection.find())
    serialized_data = json_util.dumps(data)
    return jsonify(serialized_data)

if __name__ == '__main__':
    app.run(debug=True)
