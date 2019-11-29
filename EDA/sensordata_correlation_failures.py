import numpy as np
import os #운영체제(Operating System)에서 제공하는 기능을 실행
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


# datasets/features.csv 파일경로
features_path = os.path.join("data","features.csv") 
# features.csv파일 읽어오기
features = pd.read_csv(features_path)

# machineID == 1인 데이터를 features_machine1에 저장
machine1 = features[features['machineID']==1]

print('-------------------------sensor data mean with failure-------------------------')
# machine1의 1월데이터를 failure로 그룹화
groups = machine1.groupby('failure')

fig, axes = plt.subplots(nrows=2, ncols=3)
fig.suptitle('data mean with failure', y=1.1, fontsize=20)
for name, group in groups:
    axes[0,0].plot(group.voltmean,
                    group.rotatemean,
                    marker = 'o',
                    linestyle='',
                    label=name)
axes[0,0].legend()
axes[0,0].set_title('volt with rotate')
axes[0,0].set_xlabel('voltmean')
axes[0,0].set_ylabel('rotatemean')

for name, group in groups:
    axes[0,1].plot(group.voltmean,
                    group.pressuremean,
                    marker = 'o',
                    linestyle='',
                    label=name)
axes[0,1].set_title('volt with pressure')
axes[0,1].set_xlabel('voltmean')
axes[0,1].set_ylabel('pressuremean')


for name, group in groups:
    axes[0,2].plot(group.voltmean,
                    group.vibrationmean,
                    marker = 'o',
                    linestyle='',
                    label=name)
axes[0,2].set_title('volt with vibration')
axes[0,2].set_xlabel('voltmean')
axes[0,2].set_ylabel('vibrationmean')


for name, group in groups:
    axes[1,0].plot(group.rotatemean,
                    group.pressuremean,
                    marker = 'o',
                    linestyle='',
                    label=name)
axes[1,0].set_title('rotate with pressure')
axes[1,0].set_xlabel('rotatemean')
axes[1,0].set_ylabel('pressuremean')

for name, group in groups:
    axes[1,1].plot(group.rotatemean,
                    group.vibrationmean,
                    marker = 'o',
                    linestyle='',
                    label=name)
axes[1,1].set_title('rotate with vibration')
axes[1,1].set_xlabel('rotatemean')
axes[1,1].set_ylabel('vibrationmean')

for name, group in groups:
    axes[1,2].plot(group.pressuremean,
                    group.vibrationmean,
                    marker = 'o',
                    linestyle='',
                    label=name)
axes[1,2].set_title('pressure with vibration')
axes[1,2].set_xlabel('pressuremean')
axes[1,2].set_ylabel('vibrationmean')

fig.tight_layout()
plt.show()

print('-------------------------sensor data standard deviation with failure-------------------------')
fig, axes = plt.subplots(nrows=2, ncols=3)
fig.suptitle('standard deviation data with failure', y=1.1, fontsize=20)
for name, group in groups:
    axes[0,0].plot(group.voltsd,
                    group.rotatesd,
                    marker = 'o',
                    linestyle='',
                    label=name)
axes[0,0].set_title('volt with rotate')
axes[0,0].set_xlabel('voltsd')
axes[0,0].set_ylabel('rotatesd')

for name, group in groups:
    axes[0,1].plot(group.voltsd,
                    group.pressuresd,
                    marker = 'o',
                    linestyle='',
                    label=name)
axes[0,1].set_title('volt with pressure')
axes[0,1].set_xlabel('voltsd')
axes[0,1].set_ylabel('pressuresd')


for name, group in groups:
    axes[0,2].plot(group.voltsd,
                    group.vibrationsd,
                    marker = 'o',
                    linestyle='',
                    label=name)
axes[0,2].set_title('volt with vibration')
axes[0,2].set_xlabel('voltsd')
axes[0,2].set_ylabel('vibrationsd')


for name, group in groups:
    axes[1,0].plot(group.rotatesd,
                    group.pressuresd,
                    marker = 'o',
                    linestyle='',
                    label=name)
axes[1,0].set_title('rotate with pressure')
axes[1,0].set_xlabel('rotatesd')
axes[1,0].set_ylabel('pressuresd')

for name, group in groups:
    axes[1,1].plot(group.rotatesd,
                    group.vibrationsd,
                    marker = 'o',
                    linestyle='',
                    label=name)
axes[1,1].set_title('rotate with vibration')
axes[1,1].set_xlabel('rotatesd')
axes[1,1].set_ylabel('vibrationsd')

for name, group in groups:
    axes[1,2].plot(group.pressuresd,
                    group.vibrationsd,
                    marker = 'o',
                    linestyle='',
                    label=name)
axes[1,2].set_title('pressure with vibration')
axes[1,2].set_xlabel('pressuresd')
axes[1,2].set_ylabel('vibrationsd')

fig.tight_layout()
plt.show()

