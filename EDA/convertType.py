import numpy as np
import os #운영체제(Operating System)에서 제공하는 기능을 실행
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd



# datasets/filename.csv 파일경로
path = os.path.join("datasets","unlabeledfeatures.csv") 
# filename.csv파일 읽어오기
file = pd.read_csv(path)


# 데이터를 제대로 불러왔는지 확인
# 시작부분 5개 데이터 출력
print(file.head())
# 끝 부분 5개 데이터 출력
print(file.tail())

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
file.info()

'''
machines.describe()

count : Null 값이 아닌 데이터의 개수
mean, std : 평균값, 최대값
min, max : 최소값, 최대값
25%, 50%, 75% :  백분위 값
'''
print(file.describe())

# object형식을 datetime형식으로 변환
file['datetime'] = file['datetime'].apply(pd.to_datetime)

# 제대로 변환됬는지 확인
file.info()

# 변환된 데이터 저장
file.to_csv('data/unlabeledfeatures.csv')


