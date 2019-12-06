import os 
import pandas as pd

# datasets/features.csv 파일경로
data_path = os.path.join("PdM_errors.csv") 
# features.csv파일 읽어오기
data = pd.read_csv(data_path)

test_date = pd.to_datetime('2015-09-30 23:00:00')

data = data.loc[pd.to_datetime(data['datetime']) > test_date]

data.to_csv('testData/test_data_errors.csv', index=False )