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

test_results = []
models = []

# make test and training splits
validation_date = pd.to_datetime('2015-9-30 01:00:00')
validation_data = pd.get_dummies(features.loc[pd.to_datetime(features['datetime']) < validation_date].drop(['datetime','machineID','failure'], 1))
test_result = pd.DataFrame(features.loc[pd.to_datetime(features['datetime']) < validation_date])

validation_date = pd.to_datetime('2015-8-01 01:00:00')
test_result = pd.DataFrame(test_result.loc[pd.to_datetime(features['datetime']) > validation_date])
validation_data = validation_data.loc[pd.to_datetime(features['datetime']) > validation_date]

my_model = joblib.load('my_model.pkl')



test_result['predicted_failure'] = my_model.predict(validation_data)
test_results.append(test_result)
models.append(my_model)

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
plt.show()

def Evaluate(predicted, actual, labels):
    output_labels = []
    output = []
    
    # Calculate and display confusion matrix
    cm = confusion_matrix(actual, predicted, labels=labels)
    print('Confusion matrix\n- x-axis is true labels (False, True)\n- y-axis is predicted labels')
    print(cm)
    '''
             False  True (predict)
     False [[120065 71] 
     True   [35     2229]]
     (True)
     
     False로 정확히 예측된 것이 120065개, False인데 True로 예측된 것이 71개
     True인데 Flase로 예측된 것이 35개, True로 정확히 예측된 것이 2229개
    '''
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
    
    # Calculate the macro versions of these metrics
    # macro 평균 : 단순 평균
    output.extend([[np.mean(precision)] * len(labels),
                   [np.mean(recall)] * len(labels),
                   [np.mean(f1)] * len(labels)])
    output_labels.extend(['macro precision', 'macro recall', 'macro F1'])
    
    # Find the one-vs.-all confusion matrix
    cm_row_sums = cm.sum(axis=1)
    cm_col_sums = cm.sum(axis=0)
    s = np.zeros((2, 2))
    for i in range(len(labels)):
        v = np.array([[cm[i, i],
                       cm_row_sums[i] - cm[i, i]],
                      [cm_col_sums[i] - cm[i, i],
                       np.sum(cm) + cm[i, i] - (cm_row_sums[i] + cm_col_sums[i])]])
        s += v
    s_row_sums = s.sum(axis = 1)
    
    # Add average accuracy and micro-averaged  precision/recall/F1
    # micro average: 전체 값들의 평균
    avg_accuracy = [np.trace(s) / np.sum(s)] * len(labels)
    micro_prf = [float(s[0,0]) / s_row_sums[0]] * len(labels)
    output.extend([avg_accuracy, micro_prf])
    output_labels.extend(['average accuracy',
                          'micro-averaged precision/recall/F1'])
    
    # Compute metrics for the majority classifier
    mc_index = np.where(cm_row_sums == np.max(cm_row_sums))[0][0]
    cm_row_dist = cm_row_sums / float(np.sum(cm))
    mc_accuracy = 0 * cm_row_dist
    mc_accuracy[mc_index] = cm_row_dist[mc_index]
    mc_recall = 0 * cm_row_dist
    mc_recall[mc_index] = 1
    mc_precision = 0 * cm_row_dist
    mc_precision[mc_index] = cm_row_dist[mc_index]
    mc_F1 = 0 * cm_row_dist
    mc_F1[mc_index] = 2 * mc_precision[mc_index] / (mc_precision[mc_index] + 1)
    output.extend([mc_accuracy.tolist(), mc_recall.tolist(),
                   mc_precision.tolist(), mc_F1.tolist()])
    output_labels.extend(['majority class accuracy', 'majority class recall',
                          'majority class precision', 'majority class F1'])
        
    # Random accuracy and kappa
    cm_col_dist = cm_col_sums / float(np.sum(cm))
    exp_accuracy = np.array([np.sum(cm_row_dist * cm_col_dist)] * len(labels))
    kappa = (accuracy - exp_accuracy) / (1 - exp_accuracy)
    output.extend([exp_accuracy.tolist(), kappa.tolist()])
    output_labels.extend(['expected accuracy', 'kappa'])
    

    # Random guess
    rg_accuracy = np.ones(len(labels)) / float(len(labels))
    rg_precision = cm_row_dist
    rg_recall = np.ones(len(labels)) / float(len(labels))
    rg_F1 = 2 * cm_row_dist / (len(labels) * cm_row_dist + 1)
    output.extend([rg_accuracy.tolist(), rg_precision.tolist(),
                   rg_recall.tolist(), rg_F1.tolist()])
    output_labels.extend(['random guess accuracy', 'random guess precision',
                          'random guess recall', 'random guess F1'])
    
    # Random weighted guess
    rwg_accuracy = np.ones(len(labels)) * sum(cm_row_dist**2)
    rwg_precision = cm_row_dist
    rwg_recall = cm_row_dist
    rwg_F1 = cm_row_dist
    output.extend([rwg_accuracy.tolist(), rwg_precision.tolist(),
                   rwg_recall.tolist(), rwg_F1.tolist()])
    output_labels.extend(['random weighted guess accuracy',
                          'random weighted guess precision',
                          'random weighted guess recall',
                          'random weighted guess F1'])

    output_df = pd.DataFrame(output, columns=labels)
    output_df.index = output_labels
                  
    return output_df

evaluation_results = []
for i, test_result in enumerate(test_results):
    print('\nSplit %d:' % (i+1))
    evaluation_result = Evaluate(actual = test_result['failure'],
                                 predicted = test_result['predicted_failure'],
                                 labels = ['none', 'comp1', 'comp2', 'comp3', 'comp4'])
    evaluation_results.append(evaluation_result)
    
print(evaluation_results[0])  # show full results for first split only