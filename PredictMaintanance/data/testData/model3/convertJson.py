import csv
import json
import os

machineID_list = []

file_list = os.listdir('telemetry/')

machine_list = [file for file in file_list if file.endswith(".csv")]

'''
csvfile = open('file.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("FirstName","LastName","IDNumber","Message")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
'''

for machineID in machine_list:
    print(machineID[0:-4])
    machineID_list.append(machineID[0:-4])
    

for file in machineID_list:
    filename = file
    csvfile = open('telemetry/' + filename + '.csv', 'r')
    jsonfile = open('telemetry_json/' + filename + '.json', 'w')
    
    fieldnames = ("datetime","machineID","volt","rotate","pressure", "vibration")
    reader = csv.DictReader(csvfile, fieldnames)
    
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')
    
