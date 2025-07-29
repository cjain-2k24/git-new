from pymongo import MongoClient
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

app = Flask(__name__)
client = MongoClient(MONGO_URI)
db = client["Chintan"]
collection = db["Chintan-DB-Collection"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = {
        "itemName": request.form.get("itemName"),
        "itemDescription": request.form.get("itemDescription"),
        "itemId": request.form.get("itemId"),
        "itemUUID": request.form.get("itemUUID"),
        "itemHash": request.form.get("itemHash")
        }

    # Insert into MongoDB and get inserted_id
    result = collection.insert_one(data)

    # Return a serializable response
    response = {
        "message": "Item stored successfully",
        "inserted_id": str(result.inserted_id),  # ✅ Convert ObjectId to string
        "data": data
    }
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Make sure backend is on 5001 if frontend is on 5000
