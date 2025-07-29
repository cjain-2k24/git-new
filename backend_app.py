from pymongo import MongoClient
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

app = Flask(__name__)
client = MongoClient(MONGO_URI)
db = client.todo_db
collection = db.todo_items

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = {
        "itemName": request.form.get("itemName"),
        "itemDescription": request.form.get("itemDescription"),
        "itemId": request.form.get("itemId"),
        "itemUUID": request.form.get("itemUUID"),
        "itemHash": request.form.get("itemHash")
    }
    collection.insert_one(data)
    return jsonify({"message": "Item stored successfully", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True, port=6000)
