from sklearn.externals import joblib
import numpy as np
from scipy import misc

import os #운영체제(Operating System)에서 제공하는 기능을 실행
import pandas as pd


import json
import csv

model_num = 4

# datasets/features.csv 파일경로
data_path = os.path.join("test_data_features.csv") 
# features.csv파일 읽어오기
data = pd.read_csv(data_path)

model = data[data['model']==model_num]


for num in model['machineID'].unique():
    machine = model[model['machineID']==num]
    filename = 'machineID' + str(num) + '.csv'
    filepath = 'model' + str(model_num) + '/features/'
    machine.to_csv(filepath+filename, index=False )