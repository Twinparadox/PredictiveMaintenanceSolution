import numpy as np
import os #운영체제(Operating System)에서 제공하는 기능을 실행
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


'''
telemetry
'''
# datasets/telemetry.csv 파일경로
telemetry_path = os.path.join("../data/PdM_telemetry.csv") 
# telemetry.csv파일 읽어오기
telemetry = pd.read_csv(telemetry_path)

# 데이터를 제대로 불러왔는지 확인
# 시작부분 5개 데이터 출력
print('-------------------------telemetry head-------------------------')
print(telemetry.head())
print()
# 끝 부분 5개 데이터 출력
print('-------------------------telemetry tail-------------------------')
print(telemetry.tail())
print()

# 불러온 데이터의 정보 출력
'''
RangeIndex: 876100 entries, 0 to 876099 => 데이터 개수
Data columns (total 6 columns): => feature 개수
<feature>     <개수>          <데이터 형식>
datetime     876100 non-null object  
machineID    876100 non-null int64
volt         876100 non-null float64
rotate       876100 non-null float64
pressure     876100 non-null float64
vibration    876100 non-null float64
dtypes: float64(4), int64(1), object(1)

'''
print('-------------------------telemetry info-------------------------')
telemetry.info()
print()

'''
telemetry.describe()

count : Null 값이 아닌 데이터의 개수
mean, std : 평균값, 최대값
min, max : 최소값, 최대값
25%, 50%, 75% :  백분위 값
'''
print('-------------------------telemetry describe-------------------------')
print(telemetry.describe())
print()

print('-------------------------check null in telemetry-------------------------')
sns.heatmap(telemetry.isnull(), cbar=False)
plt.savefig('figure/telemetry/telemetry_heatmap.png', dpi=300)
plt.show()


print('-------------------------check outlier in telemetry-------------------------')
telemetry.boxplot(column=['volt', 'rotate', 'pressure', 'vibration'])
plt.title('check outlier in telemetry', y=1.1, fontsize=20)
plt.savefig('figure/telemetry/telemetry_outlier.png', dpi=300)
plt.show()

# telemetr_machine1의 1월달의 volt, rotate, pressure, vibration 값
print('-------------------------machine1 sensor data-------------------------')
# machineID == 1인 데이터를 telemetr_machine1에 저장
telemetry_machine1 = telemetry[telemetry['machineID']==1]
# machineID == 2인 데이터를 telemetr_machine2에 저장
telemetry_machine2 = telemetry[telemetry['machineID'] == 2]

fig, axes = plt.subplots(nrows=2, ncols=2)
fig.suptitle('machine1 sensor data', y=1.1, fontsize=20)
telemetry_machine1[telemetry_machine1['datetime'] < '2015-02-01'].plot(ax = axes[0, 0], x = 'datetime', y = 'volt', color = 'red')
axes[0,0].set_xticks([])
axes[0,0].set_title('machine1 voltage')
axes[0,0].set_xlabel('datetime')
axes[0,0].set_ylabel('volt')

telemetry_machine1[telemetry_machine1['datetime'] < '2015-02-01'].plot(ax = axes[0, 1], x = 'datetime', y = 'rotate', color = 'green')
axes[0,1].set_xticks([])
axes[0,1].set_title('machine1 rotate')
axes[0,1].set_xlabel('datetime')
axes[0,1].set_ylabel('rotate')

telemetry_machine1[telemetry_machine1['datetime'] < '2015-02-01'].plot(ax = axes[1, 0], x = 'datetime', y = 'pressure', color = 'blue')
axes[1,0].set_xticks([])
axes[1,0].set_title('machine1 pressure')
axes[1,0].set_xlabel('datetime')
axes[1,0].set_ylabel('pressure')

telemetry_machine1[telemetry_machine1['datetime'] < '2015-02-01'].plot(ax = axes[1, 1], x = 'datetime', y = 'vibration', color = 'cyan')
axes[1,1].set_xticks([])
axes[1,1].set_title('machine1 vibration')
axes[1,1].set_xlabel('datetime')
axes[1,1].set_ylabel('vibration')

plt.tight_layout()
plt.savefig('figure/telemetry/telemetry_machine1_sensor_data.png', dpi=300)
plt.show()

# telemetr_machine1의 1월달의 volt, rotate, pressure, vibration 값
print('-------------------------machine1 sensor data2-------------------------')

fig, axes = plt.subplots(nrows=2, ncols=2)
fig.suptitle('machine1 sensor data2', y=1.1, fontsize=20)
telemetry_machine1[telemetry_machine1['datetime'] < '2015-02-01'].plot.hist(ax = axes[0, 0], x = 'datetime', y = 'volt', color = 'red')
axes[0,0].set_title('machine1 voltage')
axes[0,0].set_ylabel('count')
axes[0,0].set_xlabel('volt')

telemetry_machine1[telemetry_machine1['datetime'] < '2015-02-01'].plot.hist(ax = axes[0, 1], x = 'datetime', y = 'rotate', color = 'green')
axes[0,1].set_title('machine1 rotate')
axes[0,1].set_ylabel('count')
axes[0,1].set_xlabel('rotate')

telemetry_machine1[telemetry_machine1['datetime'] < '2015-02-01'].plot.hist(ax = axes[1, 0], x = 'datetime', y = 'pressure', color = 'blue')
axes[1,0].set_title('machine1 pressure')
axes[1,0].set_xlabel('pressure')
axes[1,0].set_ylabel('count')

telemetry_machine1[telemetry_machine1['datetime'] < '2015-02-01'].plot.hist(ax = axes[1, 1], x = 'datetime', y = 'vibration', color = 'cyan')
axes[1,1].set_title('machine1 vibration')
axes[1,1].set_xlabel('vibration')
axes[1,1].set_ylabel('count')

plt.tight_layout()
plt.savefig('figure/telemetry/telemetry_machine1_sensor_data2.png', dpi=300)
plt.show()

# telemetr_machine2의 1월달의 volt, rotate, pressure, vibration 값
print('-------------------------machine2 sensor data-------------------------')
fig2, axes2 = plt.subplots(nrows=2, ncols=2)
fig2.suptitle('machine2 sensor data', y=1.1, fontsize=20)
telemetry_machine2[telemetry_machine2['datetime'] < '2015-02-01'].plot(ax = axes2[0,0], x = 'datetime', y = 'volt', color = 'red')
axes2[0,0].set_xticks([])
axes2[0,0].set_title('machine2 voltage')
axes2[0,0].set_xlabel('datetime')
axes2[0,0].set_ylabel('volt')

telemetry_machine2[telemetry_machine2['datetime'] < '2015-02-01'].plot(ax = axes2[0,1], x = 'datetime', y = 'rotate', color = 'green')
axes2[0,1].set_xticks([])
axes2[0,1].set_title('machine2 rotate')
axes2[0,1].set_xlabel('datetime')
axes2[0,1].set_ylabel('rotate')

telemetry_machine2[telemetry_machine2['datetime'] < '2015-02-01'].plot(ax = axes2[1,0], x = 'datetime', y = 'pressure', color = 'blue')
axes2[1,0].set_xticks([])
axes2[1,0].set_title('machine2 pressure')
axes2[1,0].set_xlabel('datetime')
axes2[1,0].set_ylabel('pressure')

telemetry_machine2[telemetry_machine2['datetime'] < '2015-02-01'].plot(ax = axes2[1,1], x = 'datetime', y = 'vibration', color = 'cyan')
axes2[1,1].set_xticks([])
axes2[1,1].set_title('machine2 vibration')
axes2[1,1].set_xlabel('datetime')
axes2[1,1].set_ylabel('vibration')

plt.tight_layout()
plt.savefig('figure/telemetry/telemetry_machine2_sensor_data.png', dpi=300)
plt.show()

print('-------------------------machine2 sensor data2-------------------------')
fig2, axes2 = plt.subplots(nrows=2, ncols=2)
fig2.suptitle('machine2 sensor data2', y=1.1, fontsize=20)
telemetry_machine2[telemetry_machine2['datetime'] < '2015-02-01'].plot.hist(ax = axes2[0,0], x = 'datetime', y = 'volt', color = 'red')
axes2[0,0].set_title('machine2 voltage')
axes2[0,0].set_xlabel('volt')
axes2[0,0].set_ylabel('count')

telemetry_machine2[telemetry_machine2['datetime'] < '2015-02-01'].plot.hist(ax = axes2[0,1], x = 'datetime', y = 'rotate', color = 'green')
axes2[0,1].set_title('machine2 rotate')
axes2[0,1].set_xlabel('rotate')
axes2[0,1].set_ylabel('count')

telemetry_machine2[telemetry_machine2['datetime'] < '2015-02-01'].plot.hist(ax = axes2[1,0], x = 'datetime', y = 'pressure', color = 'blue')
axes2[1,0].set_title('machine2 pressure')
axes2[1,0].set_xlabel('pressure')
axes2[1,0].set_ylabel('count')

telemetry_machine2[telemetry_machine2['datetime'] < '2015-02-01'].plot.hist(ax = axes2[1,1], x = 'datetime', y = 'vibration', color = 'cyan')
axes2[1,1].set_title('machine2 vibration')
axes2[1,1].set_xlabel('vibration')
axes2[1,1].set_ylabel('count')

plt.tight_layout()
plt.savefig('figure/telemetry/telemetry_machine2_sensor_data2.png', dpi=300)
plt.show()
'''
errors
'''
# datasets/errors.csv 파일경로
errors_path = os.path.join("../data/PdM_errors.csv") 
# errors.csv파일 읽어오기
errors = pd.read_csv(errors_path)

# 데이터를 제대로 불러왔는지 확인
# 시작부분 5개 데이터 출력
print('-------------------------errors head-------------------------')
print(errors.head())
print()

# 끝 부분 5개 데이터 출력
print('-------------------------errors tail-------------------------')
print(errors.tail())
print()

# 불러온 데이터의 정보 출력
'''
RangeIndex: 3919 entries, 0 to 3918 => 데이터 개수
Data columns (total 4 columns): => feature 개수
<feature>     <개수>          <데이터 형식>
Unnamed: 0    3919 non-null int64
datetime      3919 non-null object
machineID     3919 non-null int64
errorID       3919 non-null object
dtypes: int64(2), object(2)

'''
print('-------------------------errors info-------------------------')
errors.info()
print()

'''
errors.describe()

count : Null 값이 아닌 데이터의 개수
mean, std : 평균값, 최대값
min, max : 최소값, 최대값
25%, 50%, 75% :  백분위 값
'''
print('-------------------------errors describe-------------------------')
print(errors.describe())
print()

print('-------------------------check null in errors-------------------------')
sns.heatmap(errors.isnull(), cbar=False)
plt.title('check null in errors', y=1.1, fontsize=20)
plt.savefig('figure/errors/errors_heatmap.png', dpi=300)
plt.show()

# errorID 빈도 출력
print('-------------------------error type count-------------------------')
plt.bar(errors['errorID'].sort_values().unique(), errors['errorID'].value_counts(sort=True).sort_values(ascending=False))
plt.title('error type count', fontsize=20)
plt.xlabel('error type')
plt.ylabel('error count')
plt.savefig('figure/errors/errors_type_count.png', dpi=300)
plt.show()

# machineID == 1인 데이터를 error_machine1에 저장
error_machine1 = errors[errors['machineID'] == 1]
# machineID == 2인 데이터를 error_machine2에 저장
error_machine2 = errors[errors['machineID'] == 2]
# machineID == 3인 데이터를 error_machine3에 저장
error_machine3 = errors[errors['machineID'] == 3]
# machineID == 4인 데이터를 error_machine4에 저장
error_machine4 = errors[errors['machineID'] == 4]

# error_machine1의 error type별 error 빈도수 출력
print('-------------------------machines error type count-------------------------')
plt.suptitle('machines error type count', y=1.1, fontsize=20)
plt.subplot(311)
plt.bar(error_machine1['errorID'].sort_values().unique(), error_machine1['errorID'].value_counts(sort=False).sort_index(), color='red')
plt.title('machine1 error type count')
plt.xlabel('error type')
plt.ylabel('error count')

# error_machine2의 error type별 error 빈도수 출력
plt.subplot(312)
plt.bar(error_machine2['errorID'].sort_values().unique(), error_machine2['errorID'].value_counts(sort=False).sort_index(), color='green')
plt.title('machine2 error type count')
plt.xlabel('error type')
plt.ylabel('error count')

# error_machine3의 error type별 error 빈도수 출력
plt.subplot(313)
plt.bar(error_machine3['errorID'].sort_values().unique(), error_machine3['errorID'].value_counts(sort=False).sort_index(), color='blue')
plt.title('machine3 error type count')
plt.xlabel('error type')
plt.ylabel('error count')

# margin자동?
plt.tight_layout()
# 차트 출력
plt.savefig('figure/errors/errors_type_count.png', dpi=300)
plt.show()

# error_machine4의 errorID값을 1, 2, 3, 4, 5로 변경
error_machine4.loc[error_machine4.errorID=='error1', 'errorID'] = 1
error_machine4.loc[error_machine4.errorID=='error2', 'errorID'] = 2  
error_machine4.loc[error_machine4.errorID=='error3', 'errorID'] = 3  
error_machine4.loc[error_machine4.errorID=='error4', 'errorID'] = 4  
error_machine4.loc[error_machine4.errorID=='error5', 'errorID'] = 5  


'''
machines
'''
# datasets/machines.csv 파일경로
machines_path = os.path.join("../data/PdM_machines.csv") 
# machines.csv파일 읽어오기
machines = pd.read_csv(machines_path)

# 데이터를 제대로 불러왔는지 확인
# 시작부분 5개 데이터 출력
print('-------------------------machines head-------------------------')
print(machines.head())
print()

# 끝 부분 5개 데이터 출력
print('-------------------------machines tail-------------------------')
print(machines.tail())
print()

# 불러온 데이터의 정보 출력
'''
RangeIndex: 100 entries, 0 to 99 => 데이터 개수
Data columns (total 4 columns): => feature 개수
<feature>     <개수>          <데이터 형식>
datetime     876100 non-null object  
Unnamed: 0    100 non-null int64
machineID     100 non-null int64
model         100 non-null object
age           100 non-null int64
dtypes: int64(3), object(1)

'''
print('-------------------------machines info-------------------------')
machines.info()
print()

'''
machines.describe()

count : Null 값이 아닌 데이터의 개수
mean, std : 평균값, 최대값
min, max : 최소값, 최대값
25%, 50%, 75% :  백분위 값
'''
print('-------------------------machines describe-------------------------')
print(machines.describe())
print()

# model == 1인 데이터를 machines_model1에 저장
machines_model1 = machines[machines['model'] == 1]
# model == 2인 데이터를 machines_model2에 저장
machines_model2 = machines[machines['model'] == 2]
# model == 3인 데이터를 machines_model3에 저장
machines_model3 = machines[machines['model'] == 3]
# model == 4인 데이터를 machines_model4에 저장
machines_model4 = machines[machines['model'] == 4]

print('-------------------------check null in machines-------------------------')
sns.heatmap(machines.isnull(), cbar=False)
plt.title('check null in machines', y=1.1, fontsize=20)
plt.savefig('figure/machines/machines_heatmap.png', dpi=300)
plt.show()

# model1의 연식과 개수
plt.subplot(221)
print('-------------------------machines model counts-------------------------')
plt.suptitle('machines model count', y=1.1, fontsize=20)
plt.bar(machines_model1['age'].sort_values().unique(), machines_model1['age'].value_counts(sort=False).sort_index(), color='red')
plt.title('model1 age count')
plt.xlabel('age(years)')
plt.ylabel('count')

# model2의 연식과 개수
plt.subplot(222)
plt.bar(machines_model2['age'].sort_values().unique(), machines_model2['age'].value_counts(sort=False).sort_index(), color='green')
plt.title('model2 age count')
plt.xlabel('age(years)')
plt.ylabel('count')

# model3의 연식과 개수
plt.subplot(223)
plt.bar(machines_model3['age'].sort_values().unique(), machines_model3['age'].value_counts(sort=False).sort_index(), color='blue')
plt.title('model3 age count')
plt.xlabel('age(years)')
plt.ylabel('count')

# model4의 연식과 개수
plt.subplot(224)
plt.bar(machines_model4['age'].sort_values().unique(), machines_model4['age'].value_counts(sort=False).sort_index(), color='yellow')
plt.title('model4 age count')
plt.xlabel('age(years)')
plt.ylabel('count')

# margin자동?
plt.tight_layout()
# 차트 출력
plt.savefig('figure/machines/machines_model_counts.png', dpi=300)
plt.show()



'''
failures
'''
# data/failures.csv 파일경로
failures_path = os.path.join("../data/PdM_failures.csv") 
# machines.csv파일 읽어오기
failures = pd.read_csv(failures_path)

# 데이터를 제대로 불러왔는지 확인
# 시작부분 5개 데이터 출력
print('-------------------------failures head-------------------------')
print(failures.head())
print()

# 끝 부분 5개 데이터 출력
print('-------------------------failures tail-------------------------')
print(failures.tail())
print()

# 불러온 데이터의 정보 출력
'''
RangeIndex: 719 entries, 0 to 718 => 데이터 개수
Data columns (total 3 columns): => feature 개수
<feature>     <개수>          <데이터 형식>
Unnamed: 0    719 non-null int64
datetime      719 non-null object
machineID     719 non-null int64
dtypes: int64(2), object(1)

'''
print('-------------------------failures info-------------------------')
failures.info()
print()

'''
failures.describe()

count : Null 값이 아닌 데이터의 개수
mean, std : 평균값, 최대값
min, max : 최소값, 최대값
25%, 50%, 75% :  백분위 값
'''
print('-------------------------failures describe-------------------------')
print(failures.describe())
print()

print('-------------------------check null in failures-------------------------')
sns.heatmap(failures.isnull(), cbar=False)
plt.title('check null in failures', y=1.1, fontsize=20)
plt.savefig('figure/failures/failures_heatmap.png', dpi=300)
plt.show()

# machine별 고장 횟수
print('-------------------------machine failures count-------------------------')
plt.bar(failures['machineID'].sort_values().unique(), failures['machineID'].value_counts(sort=False).sort_index())
plt.title('machine failures count', fontsize=20)
plt.xlabel('machineID')
plt.ylabel('count')
plt.savefig('figure/failures/failures_count.png', dpi=300)
plt.show()

'''
maint
'''
# data/failures.csv 파일경로
maint_path = os.path.join("../data/PdM_maint.csv") 
# machines.csv파일 읽어오기
maint = pd.read_csv(maint_path)

# 데이터를 제대로 불러왔는지 확인
# 시작부분 5개 데이터 출력
print('-------------------------maint head-------------------------')
print(maint.head())
print()

# 끝 부분 5개 데이터 출력
print('-------------------------maint tail-------------------------')
print(maint.tail())
print()

# 불러온 데이터의 정보 출력
print('-------------------------maint info-------------------------')
maint.info()
print()


print('-------------------------maint describe-------------------------')
print(maint.describe())
print()

print('-------------------------check null in maint-------------------------')
sns.heatmap(maint.isnull(), cbar=False)
plt.title('check null in maint', y=1.1, fontsize=20)
plt.savefig('figure/maint/maint_heatmap.png', dpi=300)
plt.show()



# comp 점검 빈도 출력
print('-------------------------comp type count-------------------------')
plt.bar(maint['comp'].sort_values().unique(), maint['comp'].value_counts(sort=True).sort_values(ascending=False))
plt.title('comp type count', fontsize=20)
plt.xlabel('comp type')
plt.ylabel('comp count')
plt.savefig('figure/maint/maint_comp_count.png', dpi=300)
plt.show()

# machineID == 1인 데이터를 maint_machine1에 저장
maint_machine1 = maint[maint['machineID'] == 1]
# machineID == 2인 데이터를 error_machine2에 저장
maint_machine2 = maint[maint['machineID'] == 2]
# machineID == 3인 데이터를 error_machine3에 저장
maint_machine3 = maint[maint['machineID'] == 3]
# machineID == 4인 데이터를 error_machine4에 저장
maint_machine4 = maint[maint['machineID'] == 4]

# maint_machine1의 comp type별 점검 빈도수 출력
print('-------------------------machines comp type count-------------------------')
plt.suptitle('machines comp maint count', y=1.1, fontsize=20)
plt.subplot(221)
plt.bar(maint_machine1['comp'].sort_values().unique(), maint_machine1['comp'].value_counts(sort=False).sort_index(), color='red')
plt.title('machine1 comp count')
plt.xlabel('comp type')
plt.ylabel('comp count')

# maint_machine2의 comp type별 점검 빈도수 출력
plt.subplot(222)
plt.bar(maint_machine2['comp'].sort_values().unique(), maint_machine2['comp'].value_counts(sort=False).sort_index(), color='green')
plt.title('machine2 comp maint count')
plt.xlabel('comp type')
plt.ylabel('comp count')

# maint_machine3의 comp type별 점검 빈도수 출력
plt.subplot(223)
plt.bar(maint_machine3['comp'].sort_values().unique(), maint_machine3['comp'].value_counts(sort=False).sort_index(), color='blue')
plt.title('machine3 comp maint count')
plt.xlabel('comp type')
plt.ylabel('comp count')

# maint_machine4의 comp type별 점검 빈도수 출력
plt.subplot(224)
plt.bar(maint_machine4['comp'].sort_values().unique(), maint_machine4['comp'].value_counts(sort=False).sort_index(), color='cyan')
plt.title('machine4 comp maint count')
plt.xlabel('comp type')
plt.ylabel('comp count')

# margin자동?
plt.tight_layout()
# 차트 출력
plt.savefig('figure/maint/machines_comp_maint_count.png', dpi=300)
plt.show()



