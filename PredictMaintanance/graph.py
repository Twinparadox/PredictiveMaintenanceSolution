import flask
from flask import Flask, request, render_template
from sklearn.externals import joblib
import numpy as np
from scipy import misc
import json
import csv
import os #운영체제(Operating System)에서 제공하는 기능을 실행
import pandas as pd

period_start = 0
period_cnt = 25
i = 25
data = []
value  = []
with open('data/testData/model1/telemetry_json/machineID13.json') as f:
    for line in f:
        data.append(json.loads(line))


app = Flask(__name__)

@app.route('/')
def index():
    value = data[1:25]
    return render_template('index.html', initdata=value)

@app.route('/draw', methods = ['POST', 'GET'])
def draw():    
    global i
    global period_start
    global value
    
    i = i + 1
    period_start += 1
    
    value.append(data[i])
    print(data[i])
    
    return json.dumps([data[i]])

@app.route('/graph')
def graph():
    global i
    global period_start
    global value
    
    i = i + 1
    period_start += 1
    
    value.append(data[i])
    return render_template('graph.html', update = data[i], sensor = value)
    
#    return render_template('index.html', update = data[i], sensor = value)

if __name__ == '__main__':
    # Flask 서비스 스타트
    app.run(host='localhost', port=8080)
