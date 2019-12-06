import os 
import pandas as pd

errors_path = os.path.join("test_data_errors.csv") 
errors = pd.read_csv(errors_path)

telemetry_path = os.path.join("test_data_telemetry.csv")
telemetry = pd.read_csv(telemetry_path)

telemetry = pd.merge(telemetry, errors, on=['datetime', 'machineID'], how='left')
telemetry['errorID'] = telemetry['errorID'].fillna('none')
telemetry.to_csv('test_data_telemetry_errors.csv', index=False )