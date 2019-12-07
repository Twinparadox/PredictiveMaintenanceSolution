# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:15:53 2019

@author: nww73
"""

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
    all_data.append(data)    
with open('data/testData/model1/telemetry_labeled_errors_json/machineID16.json') as f:
    data1 = []
    for line in f:
        data1.append(json.loads(line))    
    all_data.append(data)
    
with open('data/testData/model2/telemetry_labeled_errors_json/machineID11.json') as f:
    data1 = []
    for line in f:
        data1.append(json.loads(line))    
    all_data.append(data1)
with open('data/testData/model2/telemetry_labeled_errors_json/machineID20.json') as f:
    data1 = []
    for line in f:
        data1.append(json.loads(line))    
    all_data.append(data1)
    
with open('data/testData/model3/telemetry_labeled_errors_json/machineID1.json') as f:
    data1 = []
    for line in f:
        data1.append(json.loads(line))    
    all_data.append(data1)
with open('data/testData/model3/telemetry_labeled_errors_json/machineID3.json') as f:
    data1 = []
    for line in f:
        data1.append(json.loads(line))    
    all_data.append(data1)
    
with open('data/testData/model4/telemetry_labeled_errors_json/machineID2.json') as f:
    data1 = []
    for line in f:
        data1.append(json.loads(line))    
    all_data.append(data1)
with open('data/testData/model4/telemetry_labeled_errors_json/machineID9.json') as f:
    data1 = []
    for line in f:
        data1.append(json.loads(line))    
    all_data.append(data1)
    
        

machine13_path = os.path.join("data","testData","model1","features","machineID13.csv")        
machine13 = pd.read_csv(machine13_path)
machine13 = machine13.drop(['datetime','machineID','failure'], 1)
machine13Data = ""

machine11_path = os.path.join("data","testData","model2","features","machineID11.csv")        
machine11 = pd.read_csv(machine11_path)
machine11 = machine11.drop(['datetime','machineID','failure'], 1)
machine11Data = ""

machine1_path = os.path.join("data","testData","model3","features","machineID1.csv")        
machine1 = pd.read_csv(machine1_path)
machine1 = machine1.drop(['datetime','machineID','failure'], 1)
machine1Data = ""

machine2_path = os.path.join("data","testData","model4","features","machineID2.csv")        
machine2 = pd.read_csv(machine2_path)
machine2 = machine2.drop(['datetime','machineID','failure'], 1)
machine2Data = ""

app = Flask(__name__)

@app.route('/')
def index():
    global i
    global period_start
    global period_cnt
    
    m_id = request.args.get('machine', 0)
    
    if m_id==0:               
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
        
    elif m_id==2:        
        value = all_data[2][period_start:i]
        
        machine11Data = machine11[i-1:i]
        prediction1 = model.predict(machine11Data)        
        
        last= len(value) - 1
        value[last]['failure'] = prediction1[0]
        value[last]['comp1'] = machine11Data['comp1'].values[0]
        value[last]['comp2'] = machine11Data['comp2'].values[0]
        value[last]['comp3'] = machine11Data['comp3'].values[0]
        value[last]['comp4'] = machine11Data['comp4'].values[0]
        
    elif m_id==4:
        value = all_data[4][period_start:i]
        
        machine1Data = machine1[i-1:i]
        prediction1 = model.predict(machine1Data)        
        
        last= len(value) - 1
        value[last]['failure'] = prediction1[0]
        value[last]['comp1'] = machine1Data['comp1'].values[0]
        value[last]['comp2'] = machine1Data['comp2'].values[0]
        value[last]['comp3'] = machine1Data['comp3'].values[0]
        value[last]['comp4'] = machine1Data['comp4'].values[0]
        
    elif m_id==6:
        value = all_data[6][period_start:i]
        
        machine2Data = machine2[i-1:i]
        prediction1 = model.predict(machine2Data)        
        
        last= len(value) - 1
        value[last]['failure'] = prediction1[0]
        value[last]['comp1'] = machine2Data['comp1'].values[0]
        value[last]['comp2'] = machine2Data['comp2'].values[0]
        value[last]['comp3'] = machine2Data['comp3'].values[0]
        value[last]['comp4'] = machine2Data['comp4'].values[0]
    
    return render_template('index.html', initdata=value)


@app.route('/draw', methods = ['POST', 'GET'])
def draw():    
    global i
    global period_start
    global value
    
    i = i + 1
    period_start += 1
    
    m_id = request.form['machine']
    send = []
    
    if m_id==0:
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
        
    elif m_id==2:
        value.append(all_data[m_id][i])
        
        machine11Data = machine11[i-1:i]
        prediction1 = model.predict(machine11Data)
        
        send = all_data[m_id][i]
        send['failure']=prediction1[0]
        send['comp1'] = machine11Data['comp1'].values[0]
        send['comp2'] = machine11Data['comp2'].values[0]
        send['comp3'] = machine11Data['comp3'].values[0]
        send['comp4'] = machine11Data['comp4'].values[0]
        print(send)
        
    elif m_id==4:
        value.append(all_data[m_id][i])
        
        machine1Data = machine1[i-1:i]
        prediction1 = model.predict(machine1Data)
        
        send = all_data[m_id][i]
        send['failure']=prediction1[0]
        send['comp1'] = machine1Data['comp1'].values[0]
        send['comp2'] = machine1Data['comp2'].values[0]
        send['comp3'] = machine1Data['comp3'].values[0]
        send['comp4'] = machine1Data['comp4'].values[0]
        print(send)
        
    elif m_id==6:
        value.append(all_data[m_id][i])
        
        machine2Data = machine2[i-1:i]
        prediction1 = model.predict(machine2Data)
        
        send = all_data[m_id][i]
        send['failure']=prediction1[0]
        send['comp1'] = machine2Data['comp1'].values[0]
        send['comp2'] = machine2Data['comp2'].values[0]
        send['comp3'] = machine2Data['comp3'].values[0]
        send['comp4'] = machine2Data['comp4'].values[0]
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
    
