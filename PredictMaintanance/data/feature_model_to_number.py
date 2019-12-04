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

# datasets/features.csv 파일경로
features_path = os.path.join("../data/labeled_features.csv") 
# features.csv파일 읽어오기
features = pd.read_csv(features_path)

for num in range(len(features)):
    features['model'][num] = features['model'][num][-1:]

features.to_csv('features.csv', index=False )


