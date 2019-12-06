import numpy as np
import os #운영체제(Operating System)에서 제공하는 기능을 실행
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

'''
features
'''
# datasets/features.csv 파일경로
features_path = os.path.join("../data/labeled_features.csv") 
# features.csv파일 읽어오기
features = pd.read_csv(features_path)

# 데이터를 제대로 불러왔는지 확인
# 시작부분 5개 데이터 출력
print('-------------------------features head-------------------------')
print(features.head())
print()
# 끝 부분 5개 데이터 출력
print('-------------------------features tail-------------------------')
print(features.tail())
print()

# 불러온 데이터의 정보 출력
'''
RangeIndex: 291300 entries, 0 to 291299 => 데이터 개수
Data columns (total 19 columns):: => feature 개수
<feature>        <개수>           <데이터 형식>
Unnamed: 0       291300 non-null int64
datetime         291300 non-null object
machineID        291300 non-null int64
voltmean         291300 non-null float64
rotatemean       291300 non-null float64
pressuremean     291300 non-null float64
vibrationmean    291300 non-null float64
voltsd           291300 non-null float64
rotatesd         291300 non-null float64
pressuresd       291300 non-null float64
vibrationsd      291300 non-null float64
error1count      291300 non-null float64
error2count      291300 non-null float64
error3count      291300 non-null float64
error4count      291300 non-null float64
error5count      291300 non-null float64
model            291300 non-null object
age              291300 non-null int64
failure          291300 non-null bool
dtypes: bool(1), float64(13), int64(3), object(2)
memory usage: 40.3+ MB

'''
print('-------------------------features info-------------------------')
features.info()
print()

'''
features.describe()

count : Null 값이 아닌 데이터의 개수
mean, std : 평균값, 최대값
min, max : 최소값, 최대값
25%, 50%, 75% :  백분위 값
'''
print('-------------------------features describe-------------------------')
print(features.describe())
print()

print('-------------------------check null in features-------------------------')
sns.heatmap(features.isnull(), cbar=False)
plt.savefig('figure/features/features_heatmap.png', dpi=300)
plt.show()

print('-------------------------check outlier in features-------------------------')
features.boxplot(column=['voltmean_24h', 'rotatemean_24h', 'pressuremean_24h', 'vibrationmean_24h'])
plt.title('mean data outlier', fontsize=20)
plt.savefig('figure/features/features_mean_outlier.png', dpi=300)
plt.show()

features.boxplot(column=['voltsd_24h', 'rotatesd_24h', 'pressuresd_24h', 'vibrationsd_24h'])
plt.title('sd data outlier', fontsize=20)
plt.savefig('figure/features/features_sd_outlier.png', dpi=300)
plt.show()

print('-------------------------machine1 sensor data mean plot-------------------------')
# machineID == 1인 데이터를 features_machine1에 저장
machine1 = features[features['machineID']==1]

# telemetr_machine1의 1월달의 24시간동안 volt, rotate, pressure, vibration mean값
fig, axes = plt.subplots(nrows=2, ncols=2)
fig.suptitle('machine1 24hour sensor data mean plot', y=1.1, fontsize=20)
machine1[machine1['datetime'] < '2015-02-01'].plot(ax = axes[0, 0], x = 'datetime', y = 'voltmean_24h', color = 'red')
axes[0,0].set_xticks([])
axes[0,0].set_title('machine1 24hour voltage mean')
axes[0,0].set_xlabel('datetime')
axes[0,0].set_ylabel('volt mean')

machine1[machine1['datetime'] < '2015-02-01'].plot(ax = axes[0, 1], x = 'datetime', y = 'rotatemean_24h', color = 'green')
axes[0,1].set_xticks([])
axes[0,1].set_title('machine1 24hour rotate mean')
axes[0,1].set_xlabel('datetime')
axes[0,1].set_ylabel('rotate mean')

machine1[machine1['datetime'] < '2015-02-01'].plot(ax = axes[1, 0], x = 'datetime', y = 'pressuremean_24h', color = 'blue')
axes[1,0].set_xticks([])
axes[1,0].set_title('machine1 24hour pressure mean')
axes[1,0].set_xlabel('datetime')
axes[1,0].set_ylabel('pressure mean')

machine1[machine1['datetime'] < '2015-02-01'].plot(ax = axes[1, 1], x = 'datetime', y = 'vibrationmean_24h', color = 'cyan')
axes[1,1].set_xticks([])
axes[1,1].set_title('machine1 24hour vibration mean')
axes[1,1].set_xlabel('datetime')
axes[1,1].set_ylabel('vibration mean')

plt.tight_layout()
plt.savefig('figure/features/machine1_mean_sensor_data.png', dpi=300)
plt.show()

print('-------------------------machine1 sensor data mean histogram-------------------------')
fig, axes = plt.subplots(nrows=2, ncols=2)
fig.suptitle('machine1 24hour sensor data mean histogram', y=1.1, fontsize=20)
machine1[machine1['datetime'] < '2015-02-01'].plot.hist(ax = axes[0, 0], x = 'datetime', y = 'voltmean_24h', color = 'red')
axes[0,0].set_xticks([])
axes[0,0].set_title('machine1 24hour voltage mean')
axes[0,0].set_xlabel('datetime')
axes[0,0].set_ylabel('volt mean')

machine1[machine1['datetime'] < '2015-02-01'].plot.hist(ax = axes[0, 1], x = 'datetime', y = 'rotatemean_24h', color = 'green')
axes[0,1].set_xticks([])
axes[0,1].set_title('machine1 24hour rotate mean')
axes[0,1].set_xlabel('datetime')
axes[0,1].set_ylabel('rotate mean')

machine1[machine1['datetime'] < '2015-02-01'].plot.hist(ax = axes[1, 0], x = 'datetime', y = 'pressuremean_24h', color = 'blue')
axes[1,0].set_xticks([])
axes[1,0].set_title('machine1 24hour pressure mean')
axes[1,0].set_xlabel('datetime')
axes[1,0].set_ylabel('pressure mean')

machine1[machine1['datetime'] < '2015-02-01'].plot.hist(ax = axes[1, 1], x = 'datetime', y = 'vibrationmean_24h', color = 'cyan')
axes[1,1].set_xticks([])
axes[1,1].set_title('machine1 24hour vibration mean')
axes[1,1].set_xlabel('datetime')
axes[1,1].set_ylabel('vibration mean')

plt.tight_layout()
plt.savefig('figure/features/machine1_mean_sensor_data2.png', dpi=300)
plt.show()

# features_machine1의 1월달의 24시간동안 volt, rotate, pressure, vibration standard deviation값
print('-------------------------machine1 sensor data standard deviation plot-------------------------')
fig, axes = plt.subplots(nrows=2, ncols=2)
fig.suptitle('machine1 24hour sensor data standard deviation plot', y=1.1, fontsize=20)
machine1[machine1['datetime'] < '2015-02-01'].plot(ax = axes[0, 0], x = 'datetime', y = 'voltsd_24h', color = 'red')
axes[0,0].set_xticks([])
axes[0,0].set_title('machine1 24hour voltage sd')
axes[0,0].set_xlabel('datetime')
axes[0,0].set_ylabel('volt sd')

machine1[machine1['datetime'] < '2015-02-01'].plot(ax = axes[0, 1], x = 'datetime', y = 'rotatesd_24h', color = 'green')
axes[0,1].set_xticks([])
axes[0,1].set_title('machine1 24hour rotate sd')
axes[0,1].set_xlabel('datetime')
axes[0,1].set_ylabel('rotate sd')

machine1[machine1['datetime'] < '2015-02-01'].plot(ax = axes[1, 0], x = 'datetime', y = 'pressuresd_24h', color = 'blue')
axes[1,0].set_xticks([])
axes[1,0].set_title('machine1 24hour pressure sd')
axes[1,0].set_xlabel('datetime')
axes[1,0].set_ylabel('pressure sd')

machine1[machine1['datetime'] < '2015-02-01'].plot(ax = axes[1, 1], x = 'datetime', y = 'vibrationsd_24h', color = 'cyan')
axes[1,1].set_xticks([])
axes[1,1].set_title('machine1 24hour vibration sd')
axes[1,1].set_xlabel('datetime')
axes[1,1].set_ylabel('vibration sd')

plt.tight_layout()
plt.savefig('figure/features/machine1_sd_sensor_data.png', dpi=300)
plt.show()

print('-------------------------machine1 sensor data standard deviation histogram-------------------------')
fig, axes = plt.subplots(nrows=2, ncols=2)
fig.suptitle('machine1 24hour sensor data standard deviation histogram', y=1.1, fontsize=20)
machine1[machine1['datetime'] < '2015-02-01'].plot.hist(ax = axes[0, 0], x = 'datetime', y = 'voltsd_24h', color = 'red')
axes[0,0].set_xticks([])
axes[0,0].set_title('machine1 24hour voltage sd')
axes[0,0].set_xlabel('datetime')
axes[0,0].set_ylabel('volt sd')

machine1[machine1['datetime'] < '2015-02-01'].plot.hist(ax = axes[0, 1], x = 'datetime', y = 'rotatesd_24h', color = 'green')
axes[0,1].set_xticks([])
axes[0,1].set_title('machine1 24hour rotate sd')
axes[0,1].set_xlabel('datetime')
axes[0,1].set_ylabel('rotate sd')

machine1[machine1['datetime'] < '2015-02-01'].plot.hist(ax = axes[1, 0], x = 'datetime', y = 'pressuresd_24h', color = 'blue')
axes[1,0].set_xticks([])
axes[1,0].set_title('machine1 24hour pressure sd')
axes[1,0].set_xlabel('datetime')
axes[1,0].set_ylabel('pressure sd')

machine1[machine1['datetime'] < '2015-02-01'].plot.hist(ax = axes[1, 1], x = 'datetime', y = 'vibrationsd_24h', color = 'cyan')
axes[1,1].set_xticks([])
axes[1,1].set_title('machine1 24hour vibration sd')
axes[1,1].set_xlabel('datetime')
axes[1,1].set_ylabel('vibration sd')

plt.tight_layout()
plt.savefig('figure/features/machine1_sd_sensor_data2.png', dpi=300)
plt.show()


print('-------------------------machine age with failures-------------------------')
plt.suptitle('comp maint count with age', y=1.1, fontsize=20)
plt.subplot(221)
failure_comp1 = features[features['failure']=='comp1']
plt.bar(failure_comp1['age'].sort_values().unique(), failure_comp1['age'].value_counts(sort=False).sort_index())
plt.title('comp1 maint')
plt.xlabel('age')
plt.ylabel('maint count')

plt.subplot(222)
failure_comp2 = features[features['failure']=='comp2']
plt.bar(failure_comp1['age'].sort_values().unique(), failure_comp2['age'].value_counts(sort=False).sort_index())
plt.title('comp2 maint')
plt.xlabel('age')
plt.ylabel('maint count')

plt.subplot(223)
failure_comp3 = features[features['failure']=='comp3']
plt.bar(failure_comp3['age'].sort_values().unique(), failure_comp3['age'].value_counts(sort=False).sort_index())
plt.title('comp3 maint')
plt.xlabel('age')
plt.ylabel('maint count')

plt.subplot(224)
failure_comp4 = features[features['failure']=='comp4']
plt.bar(failure_comp4['age'].sort_values().unique(), failure_comp4['age'].value_counts(sort=False).sort_index())
plt.title('comp4 maint')
plt.xlabel('age')
plt.ylabel('maint count')

plt.tight_layout()
plt.savefig('figure/features/failures_with_age.png', dpi=300)
plt.show()





