import numpy as np
import os #운영체제(Operating System)에서 제공하는 기능을 실행
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd



# datasets/filename.csv 파일경로
path = os.path.join("PdM_errors.csv") 
# filename.csv파일 읽어오기
file = pd.read_csv(path)
# object형식을 datetime형식으로 변환
file['datetime'] = file['datetime'].apply(pd.to_datetime)
# 변환된 데이터 저장
file.to_csv('data/PdM_errors.csv')


# datasets/filename.csv 파일경로
path = os.path.join("PdM_failures.csv") 
# filename.csv파일 읽어오기
file = pd.read_csv(path)
# object형식을 datetime형식으로 변환
file['datetime'] = file['datetime'].apply(pd.to_datetime)
# 변환된 데이터 저장
file.to_csv('data/PdM_failures.csv')

# datasets/filename.csv 파일경로
path = os.path.join("PdM_maint.csv") 
# filename.csv파일 읽어오기
file = pd.read_csv(path)
# object형식을 datetime형식으로 변환
file['datetime'] = file['datetime'].apply(pd.to_datetime)
# 변환된 데이터 저장
file.to_csv('data/PdM_maint.csv')


# datasets/filename.csv 파일경로
path = os.path.join("PdM_telemetry.csv") 
# filename.csv파일 읽어오기
file = pd.read_csv(path)
# object형식을 datetime형식으로 변환
file['datetime'] = file['datetime'].apply(pd.to_datetime)
# 변환된 데이터 저장
file.to_csv('data/PdM_telemetry.csv')



