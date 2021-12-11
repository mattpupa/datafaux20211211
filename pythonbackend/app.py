
# https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run
# https://www.youtube.com/watch?v=ZI9ndn2obDk&t=1s
# app.py

# Required imports
import os
import base64
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate("/Users/Matt/Desktop/Programming/Jekyll/Datafaux/pythonbackend/firebaseadminkey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
dataset_ref = db.collection('datasetResponses')



# https://cloud.google.com/run/docs/triggering/pubsub-push#run_pubsub_handler-python
@app.route("/", methods=["POST"])
def index():
    envelope = request.get_json()
    if not envelope:
        msg = "no Pub/Sub message received"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if not isinstance(envelope, dict) or "message" not in envelope:
        msg = "invalid Pub/Sub message format"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    pubsub_message = envelope["message"]

    name = "World"
    if isinstance(pubsub_message, dict) and "data" in pubsub_message:
        name = base64.b64decode(pubsub_message["data"]).decode("utf-8").strip()

    print(f"Hello {name}!")

    # https://firebase.google.com/docs/firestore/manage-data/add-data#python_6
    dataset_ref.add({
        'foo': 'bar'
    })

    return ("", 204)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
