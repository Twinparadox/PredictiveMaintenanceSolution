import flask
from flask import Flask, request, render_template, redirect, request
from sklearn.externals import joblib
import numpy as np
from scipy import misc

import os #운영체제(Operating System)에서 제공하는 기능을 실행
import pandas as pd


import json
import csv

# model1 machine path
machine13_path = os.path.join("data","testData","model1","features","machineID13.csv")
machine16_path = os.path.join("data","testData","model1","features","machineID16.csv")

# model2 machine path
machine11_path = os.path.join("data","testData","model2","features","machineID11.csv")
machine20_path = os.path.join("data","testData","model2","features","machineID20.csv")

# model3 machine path
machine1_path = os.path.join("data","testData","model3","features","machineID1.csv")
machine3_path = os.path.join("data","testData","model3","features","machineID3.csv")

# model4 machine path
machine2_path = os.path.join("data","testData","model4","features","machineID2.csv")
machine9_path = os.path.join("data","testData","model4","features","machineID9.csv")

# model1 machine
machine13 = pd.read_csv(machine13_path)
machine16 = pd.read_csv(machine16_path)

# model2 machine
machine11 = pd.read_csv(machine11_path)
machine20 = pd.read_csv(machine20_path)

# model3 machine
machine1 = pd.read_csv(machine1_path)
machine3 = pd.read_csv(machine3_path)

# model4 machine
machine2 = pd.read_csv(machine2_path)
machine9 = pd.read_csv(machine9_path)

# 불필요한 label 제거
machine13 = machine13.drop(['datetime','machineID','failure'], 1)
machine16 = machine16.drop(['datetime','machineID','failure'], 1)
machine11 = machine11.drop(['datetime','machineID','failure'], 1)
machine20 = machine20.drop(['datetime','machineID','failure'], 1)
machine1 = machine1.drop(['datetime','machineID','failure'], 1)
machine3 = machine3.drop(['datetime','machineID','failure'], 1)
machine2 = machine2.drop(['datetime','machineID','failure'], 1)
machine9 = machine9.drop(['datetime','machineID','failure'], 1)





# 데이터를 저장할 변수
machine13_json = []
machine16_json = []
machine11_json = []
machine20_json = []
machine1_json = []
machine3_json = []
machine2_json = []
machine9_json = []

machine13Data = ""
machine16Data = ""
machine11Data = ""
machine20Data = ""
machine1Data = ""
machine3Data = ""
machine2Data = ""
machine9Data = ""

machine13_sensorData_List = []
machine16_sensorData_List = []
machine11_sensorData_List = []
machine20_sensorData_List = []
machine1_sensorData_List = []
machine3_sensorData_List = []
machine2_sensorData_List = []
machine9_sensorData_List = []

# graph를 그릴 json 데이터 가져오기
with open('data/testData/model1/telemetry_json/machineID13.json') as f:
    for line in f:
        machine13_json.append(json.loads(line))
        
with open('data/testData/model1/telemetry_json/machineID16.json') as f:
    for line in f:
        machine16_json.append(json.loads(line))        
        
with open('data/testData/model2/telemetry_json/machineID11.json') as f:
    for line in f:
        machine11_json.append(json.loads(line))
        
with open('data/testData/model2/telemetry_json/machineID20.json') as f:
    for line in f:
        machine20_json.append(json.loads(line))       

with open('data/testData/model3/telemetry_json/machineID1.json') as f:
    for line in f:
        machine1_json.append(json.loads(line))
        
with open('data/testData/model3/telemetry_json/machineID3.json') as f:
    for line in f:
        machine3_json.append(json.loads(line))       
        
with open('data/testData/model4/telemetry_json/machineID2.json') as f:
    for line in f:
        machine2_json.append(json.loads(line))
        
with open('data/testData/model4/telemetry_json/machineID9.json') as f:
    for line in f:
        machine9_json.append(json.loads(line))       
        
        
        
        
app = Flask(__name__)

i  = 0

# 메인 페이지 라우팅
@app.route("/")
@app.route("/main")
def index():
    return flask.render_template('main.html')


# 데이터 예측 처리
@app.route('/predict', methods=['POST'])
def make_prediction():
    global i
    i = i + 1
    
    machine13_sensorData_List.append(machine13_json[i])
    machine16_sensorData_List.append(machine16_json[i])
    machine11_sensorData_List.append(machine11_json[i])
    machine20_sensorData_List.append(machine20_json[i])
    machine1_sensorData_List.append(machine1_json[i])
    machine3_sensorData_List.append(machine3_json[i])
    machine2_sensorData_List.append(machine2_json[i])
    machine9_sensorData_List.append(machine9_json[i])
    
    machine13Data = machine13[i-1:i]
    machine16Data = machine16[i-1:i]
    machine11Data = machine11[i-1:i]
    machine20Data = machine20[i-1:i]
    machine1Data = machine1[i-1:i]
    machine3Data = machine3[i-1:i]
    machine2Data = machine2[i-1:i]
    machine9Data = machine9[i-1:i]
    
    if request.method == 'POST':

        prediction1 = model.predict(machine13Data)
        prediction2 = model.predict(machine16Data)
        prediction3 = model.predict(machine11Data)
        prediction4 = model.predict(machine20Data)  
        prediction5 = model.predict(machine1Data)
        prediction6 = model.predict(machine3Data)
        prediction7 = model.predict(machine2Data)
        prediction8 = model.predict(machine9Data)
        
        # 예측 값을 1차원 배열로부터 확인 가능한 문자열로 변환
        label1 = str(prediction1)
        label2 = str(prediction2)
        label3 = str(prediction3)
        label4 = str(prediction4)
        label5 = str(prediction5)
        label6 = str(prediction6)
        label7 = str(prediction7)
        label8 = str(prediction8)
        
        # 결과 리턴
        return render_template('main.html', 
                               label1=label1, label2=label2, label3=label3, label4=label4, 
                               label5=label5, label6=label6, label7=label7, label8=label8)

# 그래프 페이지 이동
@app.route('/graph', methods=['POST', 'GET'])
def move_graph():
    
    if request.method == 'POST':
        return render_template('graph.html', update = "None", sensor = "")

# 센서 데이터 그래프 그리기
@app.route('/draw', methods=['POST'])
def draw_graph():
    global i

    return render_template('graph.html', update = machine13_json[i], sensor = machine13_sensorData_List)

if __name__ == '__main__':
    
    # 모델 로드
    # ml/model.py 선 실행 후 생성
    model = joblib.load('./model/my_model.pkl')
    # Flask 서비스 스타트
    app.run(host='localhost', port=8080)
