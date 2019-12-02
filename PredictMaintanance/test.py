import flask
from flask import Flask, request, render_template
from sklearn.externals import joblib
import numpy as np
from scipy import misc

import os #운영체제(Operating System)에서 제공하는 기능을 실행
import pandas as pd


app = Flask(__name__)


# 메인 페이지 라우팅
@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('test.html')


# 데이터 예측 처리



if __name__ == '__main__':
    
    # Flask 서비스 스타트
    app.run(host='192.168.0.34', port=8080)
