import sklearn
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

with open('model.pkl', "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET"])
def health_check():
    return "All good"

@app.route('/predict', methods=["POST"])
def predict():
    data = request.json['data']
    predictions = model.predict(data)
    return jsonify({'output':predictions})

app.run(host="0.0.0.0")