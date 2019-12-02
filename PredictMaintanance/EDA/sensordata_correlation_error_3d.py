import numpy as np
import os #운영체제(Operating System)에서 제공하는 기능을 실행
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

# datasets/features.csv 파일경로
features_path = os.path.join("data","features.csv") 
# features.csv파일 읽어오기
features = pd.read_csv(features_path)

# machineID == 1인 데이터를 features_machine1에 저장
machine1 = features[features['machineID']==1]

error = machine1['error1count']

print('-------------------------volt, rotate, pressure mean correlation-------------------------')
fig = plt.figure()
ax = fig.gca(projection = '3d')

ax.scatter(machine1['voltmean'], machine1['rotatemean'], machine1['pressuremean'], c=error)
ax.set_title('volt rotate pressure mean correlation', y=1.1, fontsize=20)
ax.set_xlabel('volt')
ax.set_ylabel('rotate')
ax.set_zlabel('pressure')
plt.show()
print()

print('-------------------------volt, rotate, viberation mean correlation-------------------------')
fig = plt.figure()
ax = fig.gca(projection = '3d')

ax.scatter(machine1['voltmean'], machine1['rotatemean'], machine1['vibrationmean'], c=error)
ax.set_title('volt rotate vibration mean correlation', y=1.1, fontsize=20)
ax.set_xlabel('volt')
ax.set_ylabel('rotate')
ax.set_zlabel('vibration')
plt.show()
print()

print('-------------------------volt, pressure, viberation mean correlation-------------------------')
fig = plt.figure()
ax = fig.gca(projection = '3d')

ax.scatter(machine1['voltmean'], machine1['pressuremean'], machine1['vibrationmean'], c=error)
ax.set_title('volt pressure vibration mean correlation', y=1.1, fontsize=20)
ax.set_xlabel('volt')
ax.set_ylabel('pressure')
ax.set_zlabel('vibration')
plt.show()
print()

print('-------------------------rotate, pressure, viberation mean correlation-------------------------')
fig = plt.figure()
ax = fig.gca(projection = '3d')

ax.scatter(machine1['rotatemean'], machine1['pressuremean'], machine1['vibrationmean'], c=error)
ax.set_title('rotate pressure vibration mean correlation', y=1.1, fontsize=20)
ax.set_xlabel('rotate')
ax.set_ylabel('pressure')
ax.set_zlabel('vibration')
plt.show()
print()

print('-------------------------volt, rotate, pressure standard deviation correlation-------------------------')
fig = plt.figure()
ax = fig.gca(projection = '3d')

ax.scatter(machine1['voltsd'], machine1['rotatesd'], machine1['pressuresd'], c=error)
ax.set_title('volt rotate pressure sd correlation', y=1.1, fontsize=20)
ax.set_xlabel('volt')
ax.set_ylabel('rotate')
ax.set_zlabel('pressure')
plt.show()
print()

print('-------------------------volt, rotate, viberation standard deviation correlation-------------------------')
fig = plt.figure()
ax = fig.gca(projection = '3d')

ax.scatter(machine1['voltsd'], machine1['rotatesd'], machine1['vibrationsd'], c=error)
ax.set_title('volt rotate vibration sd correlation', y=1.1, fontsize=20)
ax.set_xlabel('volt')
ax.set_ylabel('rotate')
ax.set_zlabel('vibration')
plt.show()
print()

print('-------------------------volt, pressure, viberation standard deviation correlation-------------------------')
fig = plt.figure()
ax = fig.gca(projection = '3d')

ax.scatter(machine1['voltsd'], machine1['pressuresd'], machine1['vibrationsd'], c=error)
ax.set_title('volt pressure vibration sd correlation', y=1.1, fontsize=20)
ax.set_xlabel('volt')
ax.set_ylabel('pressure')
ax.set_zlabel('vibration')
plt.show()
print()

print('-------------------------rotate, pressure, viberation standard deviation correlation-------------------------')
fig = plt.figure()
ax = fig.gca(projection = '3d')

ax.scatter(machine1['rotatesd'], machine1['pressuresd'], machine1['vibrationsd'], c=error)
ax.set_title('rotate pressure vibration sd correlation', y=1.1, fontsize=20)
ax.set_xlabel('rotate')
ax.set_ylabel('pressure')
ax.set_zlabel('vibration')
plt.show()
print()