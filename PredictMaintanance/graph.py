import flask
from flask import Flask, request, render_template, redirect, request
from sklearn.externals import joblib
import numpy as np
from scipy import misc
import os #운영체제(Operating System)에서 제공하는 기능을 실행
import pandas as pd
import json
import csv


period_start = 1
period_cnt = 24
i = 24

period_start = 480
period_cnt = 503
i = 503

all_data = []
all_value = []

data = []
value  = []

test_data = []
Y = []


with open('data/testData/model1/telemetry_labeled_errors_json/machineID13.json') as f:
    for line in f:
        data.append(json.loads(line))
        

machine13_path = os.path.join("data","testData","model1","features","machineID13.csv")        
machine13 = pd.read_csv(machine13_path)
machine13 = machine13.drop(['datetime','machineID','failure'], 1)
machine13Data = ""

app = Flask(__name__)

@app.route('/')
def index():
    global i
    global period_start
    global period_cnt
    
    value = data[period_start:i]
    
    print(machine13[i-1:i])
        
    machine13Data = machine13[i-1:i]
    prediction1 = model.predict(machine13Data)
    
    last = len(value) - 1
    value[last]['failure'] = prediction1[0]
    value[last]['comp1'] = machine13Data['comp1'].values[0]
    value[last]['comp2'] = machine13Data['comp2'].values[0]
    value[last]['comp3'] = machine13Data['comp3'].values[0]
    value[last]['comp4'] = machine13Data['comp4'].values[0]
    
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
    
    print(machine13[i-1:i])
    
    machine13Data = machine13[i-1:i]
    prediction1 = model.predict(machine13Data)
    
    send = data[i]
    send['failure']=prediction1[0]
    send['comp1'] = machine13Data['comp1'].values[0]
    send['comp2'] = machine13Data['comp2'].values[0]
    send['comp3'] = machine13Data['comp3'].values[0]
    send['comp4'] = machine13Data['comp4'].values[0]
    print(send)
    
    return json.dumps([send])

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
    # 모델 로드
    # ml/model.py 선 실행 후 생성
    model = joblib.load('./model/my_model.pkl')
    # Flask 서비스 스타트
    app.run(host='localhost', port=8080)
    
