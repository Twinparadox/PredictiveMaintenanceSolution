import flask
from flask import Flask, request, render_template
from sklearn.externals import joblib
import numpy as np
from scipy import misc
import json
import csv
import os #운영체제(Operating System)에서 제공하는 기능을 실행
import pandas as pd

i = 0
data = []
value  = []
with open('data/testData/model1/telemetry_json/machineID13.json') as f:
    for line in f:
        data.append(json.loads(line))


app = Flask(__name__)

@app.route('/')


@app.route('/graph')
def graph():
    return render_template('graph.html', update = "None", sensor = "")

@app.route('/draw', methods = ['POST', 'GET'])
def draw():
    global i
    global value
    
    i = i + 1
    
    value.append(data[i])
    print(value)
    
    return render_template('graph.html', update = data[i], sensor = value)

if __name__ == '__main__':
    # Flask 서비스 스타트
    app.run(host='192.168.0.34', port=8080)
