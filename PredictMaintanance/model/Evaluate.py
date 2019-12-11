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

test_results = []
models = []

# make test and training splits
validation_date = pd.to_datetime('2015-9-30 01:00:00')
validation_data = pd.get_dummies(features.loc[pd.to_datetime(features['datetime']) < validation_date].drop(['datetime','machineID','failure'], 1))
test_result = pd.DataFrame(features.loc[pd.to_datetime(features['datetime']) < validation_date])

validation_date = pd.to_datetime('2015-8-01 01:00:00')
test_result = pd.DataFrame(test_result.loc[pd.to_datetime(features['datetime']) > validation_date])
validation_data = validation_data.loc[pd.to_datetime(features['datetime']) > validation_date]

my_model = joblib.load('my_model_RandomForestClassifier2.pkl')

test_result['predicted_failure'] = my_model.predict(validation_data)
test_results.append(test_result)
models.append(my_model)
'''
sns.set_style("darkgrid")
plt.figure(figsize=(10, 6))
labels, importances = zip(*sorted(zip(validation_data.columns, models[0].feature_importances_),
                                  reverse=True,
                                  key=operator.itemgetter(1)))
plt.xticks(range(len(labels)), labels)
_, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.bar(range(len(importances)), importances)
plt.ylabel('Importance')
plt.savefig('GradientBoostingClassifier_importance_feature.png', dpi=300)
plt.show()
'''
def Evaluate(predicted, actual, labels):
    output_labels = []
    output = []
    
    # Calculate and display confusion matrix
    cm = confusion_matrix(actual, predicted, labels=labels)
    print('Confusion matrix\n- x-axis is true labels (False, True)\n- y-axis is predicted labels')
    f = open('GradientBoostingClassifier_confusion_matrix.txt', 'w')
    print(cm, file = f)
    f.close()
    
    # 정확도 : 정확하게 측정된 비율
    # Calculate precision, recall, and F1 score
    # np.trace(cm) : confusion_matrix의 대각 원소의 합 => 정확히 예측된 경우
    # np.sum(cm) : confusion_matrix의 모든 원소의 합
    accuracy = np.array([float(np.trace(cm)) / np.sum(cm)] * len(labels))
    # 정밀도 : 정상이라고 예측한 것들 중 실제 정상인 값의 비율
    precision = precision_score(actual, predicted, average=None, labels=labels)
    # 재현율 : 실제 정상인 것들 중 정상이라고 예측한 비율
    recall = recall_score(actual, predicted, average=None, labels=labels)
    # F점수 : 정밀도와 재현율의 가중조화평균 가중치(베타)가 1인 경우 F1점수 라고 함
    f1 = 2 * precision * recall / (precision + recall)
    output.extend([accuracy.tolist(), precision.tolist(), recall.tolist(), f1.tolist()])
    output_labels.extend(['accuracy', 'precision', 'recall','F1'])
    
    output_df = pd.DataFrame(output, columns=labels)
    output_df.index = output_labels
                  
    return output_df

evaluation_results = []

evaluation_result = Evaluate(actual = test_result['failure'],
                                predicted = test_result['predicted_failure'],
                                labels = ['none', 'comp1', 'comp2', 'comp3', 'comp4'])
evaluation_results.append(evaluation_result)
    
f = open('GradientBoostingClassifier_evaluate.txt','w')
pd.set_option('display.max_columns', 100)
print(evaluation_results[0], file=f)  # show full results for first split only
f.close()