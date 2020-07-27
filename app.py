#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import flask
from flask import Flask, jsonify, request
from german_credit import get_predictions
import json

app = Flask(__name__)

@app.route("/predict", methods=["POST"])

def predict():
    predictions = get_predictions()
    output = {}
    for i in range(len(predictions)):
        if (predictions[i][0] > predictions[i][1]):
            output[i]  = 0
        else:
            output[i]  = 1
    return jsonify(output)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=False,threaded=False)

