import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

from IPython.display import Image
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import validation_curve
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import learning_curve
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import ShuffleSplit
from sklearn.naive_bayes import GaussianNB




# datasets/features.csv 파일경로
features_path = os.path.join("../../data/labeled_features.csv") 
# features.csv파일 읽어오기
features = pd.read_csv(features_path)

# train set, validation set, test set을 나누기 위한 임계값 설정
train_date = pd.to_datetime('2015-07-31 01:00:00')

# split out training and test data
y_train = features.loc[pd.to_datetime(features['datetime']) < train_date, 'failure']
X_train = pd.get_dummies(features.loc[pd.to_datetime(features['datetime']) < train_date].drop(['datetime','machineID','failure'], 1))

test_date = pd.to_datetime('2015-9-30 01:00:00')
X_test = features.loc[pd.to_datetime(features['datetime']) < test_date]
y_test = features.loc[pd.to_datetime(features['datetime']) < test_date]


test_date = pd.to_datetime('2015-8-01 01:00:00')
y_test = y_test.loc[pd.to_datetime(features['datetime']) > test_date, 'failure']
X_test = pd.get_dummies(X_test.loc[pd.to_datetime(features['datetime']) > test_date].drop(['datetime','machineID','failure'], 1))

'''
pipe_lr = Pipeline([('scl', StandardScaler()),
                    ('pca', PCA(n_components=2)),
                    ('clf', GradientBoostingClassifier(random_state=42))])

pipe_lr.fit(X_train, y_train)
print('Test Accuracy: %.3f' % pipe_lr.score(X_test, y_test))
y_pred = pipe_lr.predict(X_test)

scores = cross_val_score(estimator=pipe_lr,
                         X=X_train,
                         y=y_train,
                         cv=5,
                         n_jobs=-1)  # no. cpu cores to use. -1 all cores
'''
pipe_lr = Pipeline([('scl', StandardScaler()),
                    ('clf', GradientBoostingClassifier(random_state=42))])
print(pipe_lr.get_params().keys())

'''
train_sizes, train_scores, test_scores =\
                learning_curve(estimator=pipe_lr,
                               X=X_train,
                               y=y_train,
                               train_sizes=np.linspace(0.1, 1.0, 10),  # 10 evenly-spaced intervals
                               cv=5,  # 10-fold stratified CV
                               n_jobs=-1)

train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

plt.plot(train_sizes, train_mean,
         color='blue', marker='o',
         markersize=5, label='training accuracy')

plt.fill_between(train_sizes,
                 train_mean + train_std,
                 train_mean - train_std,
                 alpha=0.15, color='blue')

plt.plot(train_sizes, test_mean,
         color='green', linestyle='--',
         marker='s', markersize=5,
         label='validation accuracy')

plt.fill_between(train_sizes,
                 test_mean + test_std,
                 test_mean - test_std,
                 alpha=0.15, color='green')

plt.grid()
plt.xlabel('Number of training samples')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.ylim([0.8, 1.0])
plt.tight_layout()
plt.savefig('gradientboost_learning_curve.png', dpi=300)
plt.show()
'''

param_range = [100, 200, 300, 400, 500]
train_scores, test_scores = validation_curve(
                estimator=pipe_lr, 
                X=X_train, 
                y=y_train, 
                param_name='clf__n_estimators', 
                param_range=param_range,
                cv=5)

train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

plt.plot(param_range, train_mean, 
         color='blue', marker='o', 
         markersize=5, label='training accuracy')

plt.fill_between(param_range, train_mean + train_std,
                 train_mean - train_std, alpha=0.15,
                 color='blue')

plt.plot(param_range, test_mean, 
         color='green', linestyle='--', 
         marker='s', markersize=5, 
         label='validation accuracy')

plt.fill_between(param_range, 
                 test_mean + test_std,
                 test_mean - test_std, 
                 alpha=0.15, color='green')

plt.grid()
plt.xscale('log')
plt.legend(loc='lower right')
plt.xlabel('Parameter max_depth')
plt.ylabel('Accuracy')
plt.ylim([0.8, 1.0])
plt.tight_layout()
plt.savefig('gradientboost_validation_curve.png', dpi=300)
plt.show()



