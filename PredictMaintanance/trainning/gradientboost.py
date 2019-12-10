import numpy as np
import os #운영체제(Operating System)에서 제공하는 기능을 실행
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import GradientBoostingClassifier
import operator
from sklearn.metrics import confusion_matrix, recall_score, accuracy_score, precision_score, fbeta_score
import pickle
from sklearn.externals import joblib

# labeled_features.csv 파일경로
features_path = os.path.join("../data/labeled_features.csv")
# features.csv파일 읽어오기
features = pd.read_csv(features_path)

# train set, validation set, test set을 나누기 위한 임계값 설정
train_date = pd.to_datetime('2015-07-31 01:00:00')
                   
# split out training and test data
train_y = features.loc[pd.to_datetime(features['datetime']) < train_date, 'failure']
train_X = pd.get_dummies(features.loc[pd.to_datetime(features['datetime']) < train_date].drop(['datetime','machineID','failure'], 1))

# train and predict using the model, storing results for later
my_model = GradientBoostingClassifier(random_state=42, max_depth=1)
my_model.fit(train_X, train_y)
# 모델 저장   
joblib.dump(my_model, 'my_model_GradientBoosting.pkl')


