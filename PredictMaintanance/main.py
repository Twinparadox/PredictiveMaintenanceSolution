import flask
from flask import Flask, request, render_template
from sklearn.externals import joblib
import numpy as np
from scipy import misc

import os #운영체제(Operating System)에서 제공하는 기능을 실행
import pandas as pd


# datasets/features.csv 파일경로
features_path = os.path.join("data","labeled_features.csv") 
# features.csv파일 읽어오기
features = pd.read_csv(features_path)

# make test and training splits
test_date = pd.to_datetime('2015-10-01 01:00:00')

# test데이터 가져오기
test_X = pd.get_dummies(features.loc[pd.to_datetime(features['datetime']) > test_date].drop(['datetime','machineID','failure'], 1))

app = Flask(__name__)

i  = 10000

# 메인 페이지 라우팅
@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index2.html')


# 데이터 예측 처리
@app.route('/predict', methods=['POST'])

def make_prediction():
    global i
    
    i = i + 1
    
    data = test_X[i-1:i]
    print(data)
    if request.method == 'POST':

        prediction = model.predict(data)
        
        # 예측 값을 1차원 배열로부터 확인 가능한 문자열로 변환
        label = str(prediction)
        
        # 결과 리턴
        return render_template('index2.html', label=label)


if __name__ == '__main__':
    
    # 모델 로드
    # ml/model.py 선 실행 후 생성
    model = joblib.load('./model/my_model.pkl')
    # Flask 서비스 스타트
    app.run(host='192.168.0.34', port=8080)
