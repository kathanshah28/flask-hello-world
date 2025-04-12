from flask import Flask, request, jsonify
import pickle
import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route('/predict', methods=["POST"])
def predict():
    data = request.get_json()
    features = data['features']
    
    # Predict using the loaded model
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    
    prediction = model.predict([features])
    return jsonify({"prediction": int(prediction[0])})


@app.route('/about')
def about():
    return 'About'
