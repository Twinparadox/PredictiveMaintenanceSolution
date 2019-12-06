import matplotlib.pyplot as plt
import numpy as np

from sklearn.svm import SVC
from sklearn.model_selection import validation_curve

import pandas as pd
import os

# datasets/features.csv 파일경로
features_path = os.path.join("../data/labeled_features.csv")
# features.csv파일 읽어오기
features = pd.read_csv(features_path)

test_date = pd.to_datetime('2015-9-30 01:00:00')

X = pd.get_dummies(features.loc[pd.to_datetime(features['datetime']) < test_date].drop(['datetime','machineID','failure'], 1))
y = features.loc[pd.to_datetime(features['datetime']) < test_date, 'failure']




param_range = np.logspace(-6, -1, 5)
train_scores, test_scores = validation_curve(
    SVC(kernel='rbf', degree=3, coef0=0.1, C=5), X, y, param_name="gamma", param_range=param_range,
    cv=5, scoring="accuracy", n_jobs=-1)
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

plt.title("Validation Curve with SVM")
plt.xlabel(r"$\gamma$")
plt.ylabel("Score")
plt.ylim(0.0, 1.1)
lw = 2
plt.semilogx(param_range, train_scores_mean, label="Training score",
             color="darkorange", lw=lw)
plt.fill_between(param_range, train_scores_mean - train_scores_std,
                 train_scores_mean + train_scores_std, alpha=0.2,
                 color="darkorange", lw=lw)
plt.semilogx(param_range, test_scores_mean, label="Cross-validation score",
             color="navy", lw=lw)
plt.fill_between(param_range, test_scores_mean - test_scores_std,
                 test_scores_mean + test_scores_std, alpha=0.2,
                 color="navy", lw=lw)
plt.legend(loc="best")
plt.savefig('SVC_validation_curve.png', dpi=300)
plt.show()
