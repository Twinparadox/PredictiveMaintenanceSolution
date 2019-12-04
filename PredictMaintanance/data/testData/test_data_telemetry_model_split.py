import csv
import json
import os
import pandas as pd

model_num = 'model4'
machineID_list = []

file_list = os.listdir(model_num + '/features/')

machine_list = [file for file in file_list if file.endswith(".csv")]

for machineID in machine_list:
    machineID_list.append(int(machineID[9:-4]))


# datasets/features.csv 파일경로
data_path = os.path.join("test_data_telemetry.csv") 
# features.csv파일 읽어오기
data = pd.read_csv(data_path)


for num in machineID_list:
    machine = data[data['machineID']==num]
    filename = 'machineID' + str(num) + '.csv'
    filepath = model_num + '/telemetry/'
    machine.to_csv(filepath+filename, index=False )



    